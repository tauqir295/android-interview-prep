---
hide:
  - toc
---

!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/security/">← Back to Security</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/security/${hash}`);
      return;
    }
    const referrer = document.referrer || "";
    if (referrer.includes("/android-interview-prep/generated/")) {
      link.setAttribute("href", referrer);
    }
  } catch (_) {
    // Keep default generated page link if URL parsing fails.
  }
})();
</script>

## RASP and Runtime Self-Protection — Complete Deep Dive

## What Is RASP?

**Runtime Application Self-Protection (RASP)** embeds security controls directly inside the app process. Unlike perimeter defenses (WAFs, firewalls) or pre-launch attestation (Play Integrity API), RASP observes the *live execution environment* and can react in real time — without a server round-trip.

The goal is not to make the app *unbreakable* — that is impossible on a rooted or attacker-controlled device. The goal is to **raise the cost of attack** to the point where it becomes economically impractical, and to **generate a telemetry signal** that backend fraud detection can act on.

```
┌─────────────────────────────────────────────┐
│                 Attacker's View             │
│                                             │
│  App Binary  →  [Root]  →  [Hook]  →  Profit│
│                   ↑           ↑             │
│               RASP blocks  RASP blocks      │
└─────────────────────────────────────────────┘
```

**RASP detection categories:**

| Category | What it guards against |
|---|---|
| Root / device compromise | OS trust model broken; su available |
| Debugger detection | Live analysis / step-through debugging |
| Hook framework detection | Frida, Xposed, LSPosed method interception |
| APK integrity / anti-tamper | Repackaged or patched binary |
| Emulator detection | Automated abuse, bot farms, reverse-engineering rigs |
| Dynamic code loading | Malicious dex/so injected at runtime |
| SSL pinning bypass detection | Intercepting network traffic |
| Memory integrity | Critical values patched in RAM |

---

## 1. Root and Device Compromise Detection

### 1.1 File-System Indicators

Root tools leave predictable artefacts. Scan them in a `suspend`-friendly coroutine launched early in `Application.onCreate()`.

```kotlin
object RootDetector {

    private val SU_PATHS = listOf(
        "/system/bin/su", "/system/xbin/su", "/sbin/su",
        "/data/local/bin/su", "/data/local/xbin/su",
        "/data/local/su", "/system/sd/xbin/su",
        "/system/bin/failsafe/su", "/su/bin/su"
    )

    private val ROOT_PACKAGES = listOf(
        "com.topjohnwu.magisk",       // Magisk Manager
        "com.noshufou.android.su",    // SuperUser
        "eu.chainfire.supersu",       // SuperSU
        "com.koushikdutta.superuser",
        "com.thirdparty.superuser",
        "com.yellowes.su"
    )

    /** Returns a confidence score 0..100 */
    fun score(context: Context): Int {
        var score = 0
        if (suBinaryPresent()) score += 40
        if (rootPackageInstalled(context)) score += 30
        if (testKeysPresent()) score += 15
        if (magiskMountVisible()) score += 15
        return score.coerceAtMost(100)
    }

    private fun suBinaryPresent(): Boolean =
        SU_PATHS.any { File(it).exists() }

    private fun rootPackageInstalled(context: Context): Boolean {
        val pm = context.packageManager
        return ROOT_PACKAGES.any {
            runCatching { pm.getPackageInfo(it, 0); true }.getOrDefault(false)
        }
    }

    private fun testKeysPresent(): Boolean =
        Build.TAGS?.contains("test-keys") == true

    private fun magiskMountVisible(): Boolean = runCatching {
        File("/proc/self/mountinfo").readLines()
            .any { it.contains("magisk", ignoreCase = true) }
    }.getOrDefault(false)
}
```

### 1.2 `su` Execution Test

Attempting to execute `su` is a higher-confidence check, but it has a side-effect (it spawns a process). Only do this in high-risk flows.

```kotlin
fun canExecuteSu(): Boolean = runCatching {
    val process = Runtime.getRuntime().exec(arrayOf("/system/xbin/which", "su"))
    val result = process.inputStream.bufferedReader().readLine()
    process.destroy()
    !result.isNullOrBlank()
}.getOrDefault(false)
```

### 1.3 Build Property Checks

```kotlin
fun isBuildCompromised(): Boolean {
    // ro.build.tags should be "release-keys" on production devices
    if (Build.TAGS?.contains("test-keys") == true) return true
    // ro.debuggable should be 0 on production
    val debuggable = runCatching {
        val c = Class.forName("android.os.SystemProperties")
        val m = c.getMethod("get", String::class.java)
        m.invoke(null, "ro.debuggable") as String
    }.getOrDefault("0")
    if (debuggable == "1") return true
    return false
}
```

### 1.4 Magisk / Zygisk Specific Detection

Magisk Hide and Zygisk make it harder to detect root, but some signals still leak:

```kotlin
fun detectMagisk(): Boolean {
    // Check for Magisk app even if renamed
    val magiskPaths = listOf(
        "/data/adb/magisk",
        "/data/adb/modules",
        "/data/adb/post-fs-data.d",
        "/data/adb/service.d"
    )
    if (magiskPaths.any { File(it).exists() }) return true

    // Zygisk module directory
    if (File("/data/adb/modules").exists()) return true

    // Check for Magisk's tmpfs mounts
    return runCatching {
        File("/proc/mounts").readLines()
            .any { it.contains("magisk") || it.contains("/sbin/.magisk") }
    }.getOrDefault(false)
}
```

### 1.5 Pairing with Play Integrity

On-device checks can be spoofed. Always layer with Play Integrity's server-side verdict:

```kotlin
// In your ViewModel or use-case
suspend fun getIntegrityVerdict(context: Context): IntegrityVerdict {
    val nonce = generateSecureNonce() // 16+ bytes, base64url encoded
    val request = IntegrityTokenRequest.newBuilder()
        .setNonce(nonce)
        .build()

    val tokenProvider = IntegrityManagerFactory.create(context)
    val response = tokenProvider.requestIntegrityToken(request).await()

    // Send response.token() to YOUR backend for decryption + verdict parsing
    // Never trust the verdict decoded on-device
    return backend.verifyIntegrity(response.token())
}

data class IntegrityVerdict(
    val appRecognized: Boolean,       // PLAY_RECOGNIZED
    val deviceMeetsBasicIntegrity: Boolean,
    val deviceMeetsStrongIntegrity: Boolean
)
```

---

## 2. Debugger Detection

### 2.1 Java/Kotlin Layer

```kotlin
object DebuggerDetector {

    fun isDebuggerAttached(): Boolean =
        Debug.isDebuggerConnected() || Debug.waitingForDebugger()

    fun isDebuggableBuild(context: Context): Boolean {
        val flags = context.applicationInfo.flags
        return (flags and ApplicationInfo.FLAG_DEBUGGABLE) != 0
    }

    /** Continuous monitoring — call from a background thread */
    fun startContinuousMonitoring(onDetected: () -> Unit) {
        Thread {
            while (true) {
                if (isDebuggerAttached()) {
                    onDetected()
                    break
                }
                Thread.sleep(3000 + (Math.random() * 2000).toLong())
            }
        }.apply {
            isDaemon = true
            name = "security-watchdog"
            start()
        }
    }
}
```

### 2.2 Native Layer — TracerPid Check

The kernel exposes the PID of any attached tracer in `/proc/self/status`:

```c
// native/security/anti_debug.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <jni.h>

static int get_tracer_pid(void) {
    FILE *f = fopen("/proc/self/status", "r");
    if (!f) return -1;

    char line[256];
    int tracer_pid = 0;
    while (fgets(line, sizeof(line), f)) {
        if (strncmp(line, "TracerPid:", 10) == 0) {
            tracer_pid = atoi(line + 10);
            break;
        }
    }
    fclose(f);
    return tracer_pid;
}

JNIEXPORT jboolean JNICALL
Java_com_example_security_NativeRasp_isTracerPresent(JNIEnv *env, jclass cls) {
    return (jboolean)(get_tracer_pid() > 0);
}
```

```kotlin
// Kotlin side
object NativeRasp {
    init { System.loadLibrary("rasp") }

    external fun isTracerPresent(): Boolean
    external fun ptraceSelfTest(): Boolean
    external fun detectFridaMaps(): Boolean
    external fun detectFridaNativeSymbols(): Boolean
    external fun isCriticalFunctionHooked(): Boolean
    external fun timingCheck(): Boolean
}
```

### 2.3 ptrace Self-Attachment Trick

```c
// Only ONE process can ptrace a given PID at a time.
// If our own ptrace(PTRACE_TRACEME) fails → someone else already attached.
#include <sys/ptrace.h>
#include <errno.h>

JNIEXPORT jboolean JNICALL
Java_com_example_security_NativeRasp_ptraceSelfTest(JNIEnv *env, jclass cls) {
    if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) == -1) {
        // errno == EPERM means already being traced
        return (jboolean)(errno == EPERM);
    }
    // Detach immediately to avoid affecting normal execution
    ptrace(PTRACE_DETACH, 0, NULL, NULL);
    return JNI_FALSE;
}
```

### 2.4 Timing-Based Anti-Debug

Debuggers introduce measurable latency. Use both Kotlin and C timers:

```kotlin
object TimingDetector {
    // A simple 10k-iteration hash loop should not take > 5ms on modern hardware
    private const val EXPECTED_MAX_NS = 5_000_000L

    fun isSuspiciouslySlowExecution(): Boolean {
        val start = System.nanoTime()
        var hash = 0L
        repeat(10_000) { hash = hash * 31 + it }
        val elapsed = System.nanoTime() - start
        return elapsed > EXPECTED_MAX_NS
    }
}
```

```c
// High-resolution native timing via clock_gettime
#include <time.h>

static long long get_monotonic_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (long long)ts.tv_sec * 1000000000LL + ts.tv_nsec;
}

JNIEXPORT jboolean JNICALL
Java_com_example_security_NativeRasp_timingCheck(JNIEnv *env, jclass cls) {
    long long start = get_monotonic_ns();
    volatile int x = 0;
    for (int i = 0; i < 100000; i++) x += i;  // ~0.1ms normally
    long long elapsed = get_monotonic_ns() - start;
    // If > 50ms, something slows execution (debugger, emulator overhead)
    return (jboolean)(elapsed > 50000000LL);
}
```

---

## 3. Hook Framework Detection

### 3.1 Frida Detection

Frida is the most common Android hooking framework. It leaves multiple artefacts:

```kotlin
object FridaDetector {

    fun detect(): FridaSignals {
        return FridaSignals(
            mapsContainFrida = checkProcMaps(),
            portOpen = checkFridaPort(),
            socketPresent = checkFridaSocket(),
            nativeSymbols = NativeRasp.detectFridaNativeSymbols()
        )
    }

    /** Scan /proc/self/maps for frida-agent or gadget */
    private fun checkProcMaps(): Boolean = runCatching {
        File("/proc/self/maps").readLines().any { line ->
            line.contains("frida", ignoreCase = true) ||
            line.contains("gum-js-loop", ignoreCase = true) ||
            line.contains("gmain", ignoreCase = true)
        }
    }.getOrDefault(false)

    /** Frida server listens on 27042 by default */
    private fun checkFridaPort(): Boolean = runCatching {
        java.net.Socket().use { socket ->
            socket.connect(
                java.net.InetSocketAddress("127.0.0.1", 27042),
                100  // 100ms timeout
            )
            true  // Connected → Frida server running
        }
    }.getOrDefault(false)

    /** Check named pipes/sockets under /proc/self/fd */
    private fun checkFridaSocket(): Boolean = runCatching {
        File("/proc/self/fd").listFiles()?.any { fd ->
            val target = fd.canonicalPath
            target.contains("frida") || target.contains("linjector")
        } ?: false
    }.getOrDefault(false)
}

data class FridaSignals(
    val mapsContainFrida: Boolean,
    val portOpen: Boolean,
    val socketPresent: Boolean,
    val nativeSymbols: Boolean
) {
    val confidence: Int get() = listOf(
        mapsContainFrida, portOpen, socketPresent, nativeSymbols
    ).count { it } * 25
}
```

**Native Frida detection — scanning loaded library exports:**

```c
// Search for frida's gum_init or gum_interceptor_obtain symbols
#include <dlfcn.h>
#include <string.h>

static const char* FRIDA_EXPORTS[] = {
    "gum_init",
    "gum_interceptor_obtain",
    "frida_get_address",
    "_frida_g_thread_new",
    NULL
};

JNIEXPORT jboolean JNICALL
Java_com_example_security_NativeRasp_detectFridaNativeSymbols(
        JNIEnv *env, jclass cls) {
    void *handle = dlopen(NULL, RTLD_NOW);  // open current process
    for (int i = 0; FRIDA_EXPORTS[i] != NULL; i++) {
        if (dlsym(handle, FRIDA_EXPORTS[i]) != NULL) {
            dlclose(handle);
            return JNI_TRUE;
        }
    }
    dlclose(handle);
    return JNI_FALSE;
}
```

### 3.2 Xposed / LSPosed Detection

```kotlin
object XposedDetector {

    fun detect(): Boolean =
        classLoaderContainsXposed() ||
        callStackContainsXposed() ||
        xposedBridgeReachable() ||
        xposedDirExists()

    private fun classLoaderContainsXposed(): Boolean = runCatching {
        Class.forName("de.robv.android.xposed.XposedBridge")
        true
    }.getOrDefault(false)

    private fun xposedBridgeReachable(): Boolean = runCatching {
        // XposedBridge.disableHooks field exists if Xposed is active
        val cls = Class.forName("de.robv.android.xposed.XposedBridge")
        cls.getDeclaredField("disableHooks")
        true
    }.getOrDefault(false)

    /** Inspect current thread's stack for Xposed frame */
    private fun callStackContainsXposed(): Boolean {
        val stack = Thread.currentThread().stackTrace
        return stack.any { frame ->
            frame.className.contains("xposed", ignoreCase = true) ||
            frame.className.contains("lsposed", ignoreCase = true)
        }
    }

    private fun xposedDirExists(): Boolean =
        File("/data/data/de.robv.android.xposed.installer").exists() ||
        File("/data/app/de.robv.android.xposed.installer").exists()
}
```

### 3.3 Generic Inline Hook Detection (Native)

When Frida or a custom framework hooks a native function, it typically patches the first instruction(s) with a branch (`B` / `BL` on ARM64 or `JMP` on x86_64):

```c
#include <stdint.h>
#include <string.h>
#include <dlfcn.h>

// ARM64: a typical function prologue starts with STP x29, x30, [sp, #-...]
// A hooked function starts with: B <target> (opcode bits [31:26] == 0b000101)
static int is_function_hooked_arm64(void *func_ptr) {
    uint8_t *bytes = (uint8_t *)func_ptr;
    uint32_t instr;
    memcpy(&instr, bytes, 4);
    uint8_t opcode = (instr >> 26) & 0x3F;
    // 0x05 = B (unconditional branch), 0x25 = BL (branch with link)
    return (opcode == 0x05 || opcode == 0x25);
}

JNIEXPORT jboolean JNICALL
Java_com_example_security_NativeRasp_isCriticalFunctionHooked(
        JNIEnv *env, jclass cls) {
    // Verify SSL_write is not hooked (common MITM target)
    void *fn = dlsym(RTLD_DEFAULT, "SSL_write");
    if (!fn) return JNI_FALSE;
    return (jboolean)is_function_hooked_arm64(fn);
}
```

### 3.4 Hardening the Detection Logic Itself

```kotlin
// Bad: trivial to find and hook at startup via Frida
override fun onCreate() {
    if (XposedDetector.detect()) finish()
}

// Better: randomized timing + coroutine-based background monitoring
class SecurityWatchdog(
    private val context: Context,
    private val scope: CoroutineScope
) {
    fun start(onThreatDetected: (String) -> Unit) {
        scope.launch(Dispatchers.IO) {
            while (isActive) {
                val delayMs = 30_000L + Random.nextLong(20_000L)
                delay(delayMs)

                val threats = buildList {
                    if (RootDetector.score(context) > 60) add("root")
                    if (FridaDetector.detect().confidence >= 50) add("frida")
                    if (XposedDetector.detect()) add("xposed")
                    if (NativeRasp.isTracerPresent()) add("debugger")
                }
                threats.forEach { onThreatDetected(it) }
            }
        }
    }
}
```

---

## 4. APK Integrity and Anti-Tamper

### 4.1 Signature Certificate Verification

```kotlin
object ApkIntegrityChecker {

    /**
     * Returns the SHA-256 of the first signing certificate.
     * Compare against a value stored on YOUR backend — never hardcode in the APK.
     */
    fun getSignatureHash(context: Context): String {
        val info = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
            context.packageManager.getPackageInfo(
                context.packageName,
                PackageManager.GET_SIGNING_CERTIFICATES
            )
        } else {
            @Suppress("DEPRECATION")
            context.packageManager.getPackageInfo(
                context.packageName,
                PackageManager.GET_SIGNATURES
            )
        }

        val certBytes = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
            info.signingInfo.apkContentsSigners[0].toByteArray()
        } else {
            @Suppress("DEPRECATION")
            info.signatures[0].toByteArray()
        }

        return MessageDigest.getInstance("SHA-256")
            .digest(certBytes)
            .joinToString("") { "%02x".format(it) }
    }

    /**
     * Verify against expected hash fetched from backend over pinned TLS.
     * Call this on session start, not just at app launch.
     */
    suspend fun verifySignature(context: Context, backend: SecurityApi): Boolean {
        val actual = getSignatureHash(context)
        val expected = backend.getExpectedSignatureHash(
            versionCode = BuildConfig.VERSION_CODE
        )
        return actual == expected
    }
}
```

### 4.2 APK File Hash Verification

```kotlin
fun computeApkHash(context: Context): String {
    val apkPath = context.packageCodePath  // e.g. /data/app/.../base.apk
    val digest = MessageDigest.getInstance("SHA-256")
    File(apkPath).inputStream().buffered(65536).use { input ->
        val buffer = ByteArray(65536)
        var read: Int
        while (input.read(buffer).also { read = it } != -1) {
            digest.update(buffer, 0, read)
        }
    }
    return digest.digest().joinToString("") { "%02x".format(it) }
}
```

### 4.3 Native Library Integrity

```kotlin
fun verifyNativeLibHash(context: Context, libName: String): Boolean {
    val libPath = "${context.applicationInfo.nativeLibraryDir}/lib$libName.so"
    val actual = computeFileHash(File(libPath))
    // Expected comes from backend, bound to versionCode + ABI
    val expected = BuildConfig.NATIVE_LIB_HASHES[libName] ?: return false
    return actual == expected
}

private fun computeFileHash(file: File): String {
    val digest = MessageDigest.getInstance("SHA-256")
    file.inputStream().buffered(65536).use { input ->
        val buf = ByteArray(65536)
        var read: Int
        while (input.read(buf).also { read = it } != -1) digest.update(buf, 0, read)
    }
    return digest.digest().joinToString("") { "%02x".format(it) }
}
```

### 4.4 Guarding a Critical Code Path

```kotlin
// At a payment or high-sensitivity flow entry point:
suspend fun initiatePayment(amount: Long) {
    val rootScore = RootDetector.score(context)
    val sigOk = ApkIntegrityChecker.verifySignature(context, api)
    val noFrida = FridaDetector.detect().confidence < 25
    val noDebugger = !DebuggerDetector.isDebuggerAttached()

    if (rootScore > 60 || !sigOk || !noFrida || !noDebugger) {
        telemetry.reportIntegrityFailure(
            userId = currentUser.id,
            rootScore = rootScore,
            sigOk = sigOk,
            fridaConf = FridaDetector.detect().confidence
        )
        throw SecurityException("Integrity check failed. Transaction blocked.")
    }

    paymentProcessor.charge(amount)
}
```

---

## 5. Emulator Detection

### 5.1 Build Property Signals

```kotlin
object EmulatorDetector {

    data class EmulatorSignals(
        val suspiciousFingerprint: Boolean,
        val genericManufacturer: Boolean,
        val emulatorModel: Boolean,
        val missingTelephony: Boolean,
        val noRealSensors: Boolean,
        val genericNetworkInterface: Boolean
    ) {
        val score: Int get() = listOf(
            suspiciousFingerprint,
            genericManufacturer,
            emulatorModel,
            missingTelephony,
            noRealSensors,
            genericNetworkInterface
        ).count { it }

        val isLikelyEmulator: Boolean get() = score >= 3
    }

    fun analyze(context: Context): EmulatorSignals = EmulatorSignals(
        suspiciousFingerprint = isFingerprintSuspicious(),
        genericManufacturer = isManufacturerGeneric(),
        emulatorModel = isModelEmulator(),
        missingTelephony = isTelephonyMissing(context),
        noRealSensors = hasNoRealSensors(context),
        genericNetworkInterface = hasGenericNetworkInterface()
    )

    private fun isFingerprintSuspicious(): Boolean {
        val fp = Build.FINGERPRINT ?: return true
        return fp.contains("generic") ||
               fp.contains("unknown") ||
               fp.startsWith("google/sdk_gphone") ||
               fp.contains("emulator") ||
               fp.contains("Android SDK built")
    }

    private fun isManufacturerGeneric(): Boolean =
        Build.MANUFACTURER?.lowercase() in setOf("unknown", "genymotion", "bluestacks")

    private fun isModelEmulator(): Boolean {
        val model = Build.MODEL?.lowercase() ?: return true
        return model.contains("sdk_gphone") ||
               model.contains("emulator") ||
               model.contains("android sdk") ||
               model.contains("bluestacks")
    }

    private fun isTelephonyMissing(context: Context): Boolean = runCatching {
        val tm = context.getSystemService(Context.TELEPHONY_SERVICE) as TelephonyManager
        @Suppress("DEPRECATION")
        tm.deviceId.isNullOrBlank() || tm.deviceId == "000000000000000"
    }.getOrDefault(true)

    private fun hasNoRealSensors(context: Context): Boolean {
        val sm = context.getSystemService(Context.SENSOR_SERVICE) as SensorManager
        val hasAccel = sm.getDefaultSensor(Sensor.TYPE_ACCELEROMETER) != null
        val hasGyro  = sm.getDefaultSensor(Sensor.TYPE_GYROSCOPE) != null
        return !hasAccel || !hasGyro
    }

    private fun hasGenericNetworkInterface(): Boolean = runCatching {
        val interfaces = java.net.NetworkInterface.getNetworkInterfaces()?.toList() ?: return true
        val names = interfaces.map { it.name }
        // Real devices have wlan0; pure emulators typically only have eth0
        !names.any { it.startsWith("wlan") } && names.any { it.startsWith("eth") }
    }.getOrDefault(false)
}
```

### 5.2 Sensor Consistency Check

```kotlin
// Real devices have correlated sensor noise. Emulators often return constant zeros.
class SensorConsistencyChecker(context: Context) : SensorEventListener {
    private val sensorManager = context.getSystemService(SensorManager::class.java)
    private val samples = mutableListOf<FloatArray>()

    fun startSampling() {
        val accel = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
        accel?.let { sensorManager.registerListener(this, it, SensorManager.SENSOR_DELAY_NORMAL) }
    }

    /** Returns true if accelerometer is stuck at constant zero — typical of emulators */
    fun isConstantZero(): Boolean {
        if (samples.size < 20) return false
        return samples.all { sample -> sample.all { v -> v == 0f } }
    }

    override fun onSensorChanged(event: SensorEvent) {
        if (samples.size < 100) samples.add(event.values.copyOf())
    }

    override fun onAccuracyChanged(sensor: Sensor, accuracy: Int) {}
}
```

| Signal | Real device | Emulator / AVD |
|---|---|---|
| `Build.FINGERPRINT` | OEM/device name | Contains "generic", "unknown" |
| `Build.MANUFACTURER` | OEM name | "unknown" or "Google" (AVD) |
| `Build.MODEL` | Device model | "sdk_gphone", "Emulator" |
| Sensor availability | Full IMU | Few or no sensors / constant zero |
| Telephony `deviceId` | Real IMEI | null or "000000…" |
| Network interfaces | wlan0 + rmnet | eth0 only |

Combine at least 3–4 signals before acting; pair with Play Integrity's `MEETS_DEVICE_INTEGRITY` for high-confidence verdicts.

---

## 6. SSL Pinning Bypass Detection

### 6.1 Detecting User-Installed CAs

```kotlin
object SslPinningMonitor {

    /**
     * Detect whether a user-installed CA is trusted — typical setup for
     * proxy-based MITM attacks (Charles Proxy, Burp Suite, mitmproxy).
     */
    fun userCaInstalled(): Boolean = runCatching {
        val keyStore = KeyStore.getInstance("AndroidCAStore")
        keyStore.load(null)
        keyStore.aliases().toList().any { alias ->
            // User-installed CAs have "user:" prefix in the alias
            alias.startsWith("user:")
        }
    }.getOrDefault(false)

    /**
     * Detect TrustManager replacement — a non-system TrustManager may
     * be a bypassed/no-op implementation (e.g. all-trusting TM).
     */
    fun isTrustManagerReplaced(): Boolean = runCatching {
        val tmFactory = TrustManagerFactory.getInstance(
            TrustManagerFactory.getDefaultAlgorithm()
        )
        tmFactory.init(null as KeyStore?)
        tmFactory.trustManagers
            .filterIsInstance<X509TrustManager>()
            .any { tm ->
                val pkg = tm.javaClass.name
                !pkg.startsWith("com.android.org.conscrypt") &&
                !pkg.startsWith("sun.security")
            }
    }.getOrDefault(false)
}
```

### 6.2 Network Security Config Hardening

```xml
<!-- res/xml/network_security_config.xml -->
<network-security-config>
    <!-- Block user CAs and plaintext traffic app-wide -->
    <base-config cleartextTrafficPermitted="false">
        <trust-anchors>
            <!-- Only trust system CAs, NOT user-installed certificate authorities -->
            <certificates src="system" />
        </trust-anchors>
    </base-config>

    <!-- Extra certificate pin for your API domain -->
    <domain-config>
        <domain includeSubdomains="true">api.example.com</domain>
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
        <pin-set expiration="2027-01-01">
            <!-- Primary leaf cert pin (SHA-256 of SubjectPublicKeyInfo, base64) -->
            <pin digest="SHA-256">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=</pin>
            <!-- Backup pin — rotate before primary expires -->
            <pin digest="SHA-256">BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

```kotlin
// OkHttp-level certificate pinner (defence in depth over network_security_config)
val certificatePinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
    .add("api.example.com", "sha256/BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=")
    .build()

val client = OkHttpClient.Builder()
    .certificatePinner(certificatePinner)
    .addInterceptor { chain ->
        // Extra: abort if user CA detected
        if (SslPinningMonitor.userCaInstalled()) {
            throw SecurityException("User CA detected — aborting request")
        }
        chain.proceed(chain.request())
    }
    .build()
```

---

## 7. Dynamic Code Loading Controls

### 7.1 Restricting DexClassLoader

```kotlin
object DynamicCodeGuard {

    /**
     * Validates the dex source path before loading.
     * Never load from external storage or world-readable directories.
     */
    fun safeDexClassLoader(
        dexPath: String,
        optimizedDir: String?,
        libraryPath: String?,
        parent: ClassLoader?
    ): DexClassLoader {
        val dexFile = File(dexPath)
        require(dexFile.exists()) { "Dex file not found: $dexPath" }
        require(!dexFile.canWrite()) { "Dex file is world-writable — refusing to load" }

        // Must be inside the app's private data directory
        val canonical = dexFile.canonicalPath
        require(canonical.startsWith("/data/data/") || canonical.startsWith("/data/user/")) {
            "Dex file is not in app-private storage: $canonical"
        }

        return DexClassLoader(dexPath, optimizedDir, libraryPath, parent)
    }
}
```

### 7.2 Detecting Injected Dex at Runtime

```kotlin
fun detectInjectedDex(context: Context): Boolean {
    val legitimatePaths = setOf(
        context.applicationInfo.sourceDir,
        context.applicationInfo.dataDir
    )

    var current: ClassLoader? = context.classLoader
    while (current != null) {
        if (current is BaseDexClassLoader) {
            runCatching {
                val pathListField = BaseDexClassLoader::class.java
                    .getDeclaredField("pathList")
                    .apply { isAccessible = true }
                val pathList = pathListField.get(current)
                val elementsField = pathList.javaClass
                    .getDeclaredField("dexElements")
                    .apply { isAccessible = true }
                val elements = elementsField.get(pathList) as Array<*>

                for (element in elements) {
                    val dexFileField = element?.javaClass
                        ?.getDeclaredField("dexFile")
                        ?.apply { isAccessible = true }
                    val dexFile = dexFileField?.get(element)
                    val name = dexFile?.javaClass?.getMethod("getName")?.invoke(dexFile) as? String
                        ?: continue
                    if (legitimatePaths.none { name.startsWith(it) }) {
                        return true  // Dex loaded from unexpected location
                    }
                }
            }
        }
        current = current.parent
    }
    return false
}
```

### 7.3 Android Policy Safeguards

- Android 9 (API 28)+ blocks loading executable code from world-writable locations — ensure `targetSdkVersion` ≥ 28.
- Prefer **Play Feature Delivery** or **Play Asset Delivery**; Google's infrastructure provides integrity guarantees over dynamic modules.
- Audit every third-party SDK that uses reflection or `DexClassLoader` at runtime.

---

## 8. Memory Integrity — Protecting Critical Values

### 8.1 In-Memory Encryption with AndroidKeyStore

```kotlin
class SecureSessionToken(rawToken: String) {

    private val canaryBefore = Random.nextLong()
    private val encryptedToken: ByteArray = encrypt(rawToken.toByteArray())
    private val canaryAfter = canaryBefore xor 0xDEADBEEFCAFEBABEL

    fun getToken(): String {
        // Canary check — detect if memory around this object was patched
        check(canaryAfter == canaryBefore xor 0xDEADBEEFCAFEBABEL) {
            "Memory integrity violation detected"
        }
        return String(decrypt(encryptedToken))
    }

    private fun getOrCreateKey(): SecretKey {
        val ks = KeyStore.getInstance("AndroidKeyStore").also { it.load(null) }
        if (ks.containsAlias("session_key")) {
            return (ks.getEntry("session_key", null) as KeyStore.SecretKeyEntry).secretKey
        }
        return KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, "AndroidKeyStore")
            .apply {
                init(
                    KeyGenParameterSpec.Builder(
                        "session_key",
                        KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
                    )
                    .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                    .setKeySize(256)
                    .build()
                )
            }.generateKey()
    }

    private fun encrypt(data: ByteArray): ByteArray {
        val key = getOrCreateKey()
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        cipher.init(Cipher.ENCRYPT_MODE, key)
        return cipher.iv + cipher.doFinal(data)  // prepend 12-byte IV
    }

    private fun decrypt(data: ByteArray): ByteArray {
        val key = getOrCreateKey()
        val iv = data.copyOf(12)
        val ciphertext = data.copyOfRange(12, data.size)
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        cipher.init(Cipher.DECRYPT_MODE, key, GCMParameterSpec(128, iv))
        return cipher.doFinal(ciphertext)
    }
}
```

### 8.2 Zeroing Sensitive Data After Use

```kotlin
// Kotlin doesn't allow direct byte-array zeroing of String internals,
// but you can use ByteArray and zero it manually.
fun withSensitiveBytes(data: ByteArray, block: (ByteArray) -> Unit) {
    try {
        block(data)
    } finally {
        data.fill(0)  // Overwrite with zeros immediately after use
    }
}

// Usage
withSensitiveBytes(password.toByteArray()) { bytes ->
    val hash = argon2Hash(bytes)
    uploadHash(hash)
}
// 'bytes' is zeroed here: password bytes not lingering in heap
```

---

## 9. RASP Response Strategy

### 9.1 Tiered Response Matrix

| Signal confidence | Example condition | Response |
|---|---|---|
| Low (1 signal) | Single suspicious build prop | Silent telemetry; investigate offline |
| Medium (2–3 signals) | Frida port open OR TracerPid > 0 | Disable high-risk features (payments, PII export) |
| High (3–4 signals) | Root + Frida + no integrity verdict | Step-up auth; session invalidation |
| Critical | Strong integrity failure + definitive detection | Forced logout; optional hard stop |

### 9.2 Response Implementation

```kotlin
class RaspResponseHandler(
    private val analytics: SecurityAnalytics,
    private val featureFlags: FeatureFlags,
    private val authRepository: AuthRepository
) {

    enum class ThreatLevel { CLEAN, LOW, MEDIUM, HIGH, CRITICAL }

    fun computeThreatLevel(
        rootScore: Int,
        fridaConf: Int,
        xposed: Boolean,
        debugger: Boolean,
        integrityOk: Boolean
    ): ThreatLevel {
        val signals = listOf(
            rootScore > 60,
            fridaConf >= 50,
            xposed,
            debugger,
            !integrityOk
        ).count { it }

        return when (signals) {
            0    -> ThreatLevel.CLEAN
            1    -> ThreatLevel.LOW
            2    -> ThreatLevel.MEDIUM
            3    -> ThreatLevel.HIGH
            else -> ThreatLevel.CRITICAL
        }
    }

    suspend fun respond(userId: String, level: ThreatLevel, signals: Map<String, Any>) {
        // Always report telemetry regardless of level
        analytics.report(
            event = SecurityEvent.RASP_DETECTION,
            userId = userId,
            threatLevel = level.name,
            signals = signals
        )

        when (level) {
            ThreatLevel.LOW -> { /* Observe only */ }
            ThreatLevel.MEDIUM -> {
                featureFlags.disablePayments()
                featureFlags.disablePiiExport()
            }
            ThreatLevel.HIGH -> {
                featureFlags.disableAll()
                authRepository.invalidateSession(userId)
            }
            ThreatLevel.CRITICAL -> {
                authRepository.revokeAllSessions(userId)
                withContext(Dispatchers.Main) { showSecurityDialog() }
            }
            ThreatLevel.CLEAN -> { /* Normal operation */ }
        }
    }

    private fun showSecurityDialog() {
        // Show a non-dismissable dialog explaining the security issue.
        // Do NOT crash silently — users deserve an explanation.
    }
}
```

### 9.3 False Positive Calibration

```kotlin
// WRONG: crash all users if any heuristic fires
fun onThreatDetected() {
    throw SecurityException("Device compromised")  // ← kills legitimate users
}

// RIGHT: tiered + telemetry-driven threshold calibration
class FalsePositiveCalibrator {

    private val pendingSignals = mutableMapOf<String, MutableList<Long>>()

    fun recordSignal(signalName: String) {
        pendingSignals.getOrPut(signalName) { mutableListOf() }
            .add(System.currentTimeMillis())
    }

    // Escalate only if the same signal fires 5+ times in 24h — not a one-off
    fun shouldEscalate(signalName: String): Boolean {
        val timestamps = pendingSignals[signalName] ?: return false
        val cutoff = System.currentTimeMillis() - 86_400_000L
        return timestamps.count { it > cutoff } >= 5
    }
}
```

---

## 10. Putting It All Together — RASP Orchestrator

```kotlin
class RaspOrchestrator @Inject constructor(
    private val context: Context,
    private val scope: CoroutineScope,
    private val responseHandler: RaspResponseHandler,
    private val analytics: SecurityAnalytics
) {
    fun initialize(userId: String) {
        scope.launch(Dispatchers.IO) {
            val result = runEagerChecks()
            responseHandler.respond(userId, result.level, result.signals)
            startPeriodicChecks(userId)
        }
    }

    private fun runEagerChecks(): ScanResult {
        val rootScore = RootDetector.score(context)
        val frida     = FridaDetector.detect()
        val xposed    = XposedDetector.detect()
        val debugger  = DebuggerDetector.isDebuggerAttached()
        val emulator  = EmulatorDetector.analyze(context)
        val userCa    = SslPinningMonitor.userCaInstalled()

        val signals = mapOf(
            "root_score"       to rootScore,
            "frida_confidence" to frida.confidence,
            "xposed"           to xposed,
            "debugger"         to debugger,
            "emulator_score"   to emulator.score,
            "user_ca"          to userCa
        )

        val level = responseHandler.computeThreatLevel(
            rootScore   = rootScore,
            fridaConf   = frida.confidence,
            xposed      = xposed,
            debugger    = debugger,
            integrityOk = true  // updated after Play Integrity API call completes
        )
        return ScanResult(level, signals)
    }

    private fun startPeriodicChecks(userId: String) {
        scope.launch(Dispatchers.IO) {
            while (isActive) {
                // Randomized interval 30–90s — unpredictable to automated bypass scripts
                delay(30_000L + Random.nextLong(60_000L))
                val result = runEagerChecks()
                if (result.level != ThreatLevel.CLEAN) {
                    responseHandler.respond(userId, result.level, result.signals)
                }
            }
        }
    }

    data class ScanResult(
        val level: RaspResponseHandler.ThreatLevel,
        val signals: Map<String, Any>
    )
}
```

---

## 11. ProGuard / R8 Configuration for RASP Code

```proguard
# Keep RASP entry point and JNI bridge visible to your own code
-keep class com.example.security.RaspOrchestrator { *; }
-keep class com.example.security.NativeRasp { native <methods>; }

# Aggressively rename all internal detection classes/methods
-keepnames class com.example.security.** { *; }

# Obfuscate string literals inside RASP classes
# (requires io.michaelrocks:paranoid or similar library)
-keep @io.michaelrocks.paranoid.Obfuscate class * { *; }

# Ensure security-critical private methods are not inlined away by R8
-keepclassmembers class com.example.security.** {
    private <methods>;
}

# Don't let R8 remove "unused" detection results — they have side effects
-keepclassmembers class com.example.security.** {
    public boolean detect*();
    public int score*();
}
```

---

## 12. Commercial vs DIY RASP

| Aspect | DIY (custom) | Commercial SDK (Guardsquare, Appdome, Promon) |
|---|---|---|
| **Control** | Full | Limited to SDK configuration |
| **Maintenance** | Your team owns signature updates | Vendor provides automatic updates |
| **Detection breadth** | What your team implements | Hundreds of checks + device telemetry |
| **Evasion risk** | Attackers can reverse your logic | Code virtualisation raises bar significantly |
| **False positive rate** | Must calibrate on your own device cohort | SDK tuned against massive real-device corpus |
| **Cost** | Engineering time | $10k–$100k+/yr license |
| **Best for** | High-control fintech, crypto wallets | Mid-size apps needing fast broad coverage |

**Recommendation:** start with a DIY implementation covering the six core checks (root, debugger, Frida, Xposed, emulator, APK integrity) and evaluate commercial options when handling payments > $1M/month, or when compliance mandates it (PCI-DSS, PSD2 SCA, healthcare/HIPAA).

---

## Senior-Level Insights

- **No single check is bypass-proof.** Determined attackers with physical-device access (e.g. Frida gadget embedded inside a recompiled APK) will eventually bypass any software control. RASP raises cost and slows attackers, giving backend fraud detection time to act on patterns.
- **False positives are the biggest production risk.** On a 10M-user app, a 0.1 % false positive rate locks out 10,000 legitimate users per release. Validate every detection threshold against real device telemetry cohorts before enforcing in production.
- **RASP + Play Integrity + backend fraud signals** form a layered defence. RASP reacts instantly in-process. Play Integrity certifies device state with Google-backed hardware attestation. Backend behavioural analysis catches coordinated bot farms that defeat hardware attestation.
- **Detection evasion is an arms race.** Frida, Magisk, and emulator fingerprint spoofing all evolve quickly. Treat RASP as a living system: version your detection logic, A/B test new checks in telemetry-only mode before enforcement, and subscribe to security research feeds (NowSecure, Guardsquare blog, Black Hat proceedings).
- **Native code raises the bar significantly.** Detection logic compiled into a `.so` and obfuscated by LLVM is orders of magnitude harder to bypass with Frida scripts than equivalent Kotlin/Java logic. Move the most sensitive checks to JNI.
- **Legal and privacy considerations.** Reading `/proc/self/maps`, inspecting installed packages, or querying telephony identifiers may have privacy ramifications in some jurisdictions. Review with legal before shipping, especially under GDPR (EU) or markets with strict local privacy laws. Disclose integrity monitoring in your privacy policy.
