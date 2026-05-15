---
hide:
  - toc
---

# Security

<script>
(function () {
  function openQuestionFromHash() {
    const hash = window.location.hash;
    if (!hash || hash.length <= 1) return;

    const anchor = document.querySelector(hash);
    if (!anchor) return;

    let node = anchor.nextElementSibling;
    while (node) {
      if (node.tagName === 'DETAILS') {
        node.open = true;
        anchor.scrollIntoView({ behavior: 'auto', block: 'start' });
        return;
      }
      node = node.nextElementSibling;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', openQuestionFromHash);
  } else {
    openQuestionFromHash();
  }

  window.addEventListener('hashchange', openQuestionFromHash);
})();
</script>


---

<div id="security-threat-modeling"></div>

## How do you threat model an Android app before release?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">threat-modeling</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    Threat modeling is about finding high-impact abuse paths before attackers do.

    In interviews, cover:

    - assets you protect (PII, auth tokens, payment flows)
    - trust boundaries (device, app, backend, third-party SDKs)
    - likely attackers and abuse paths
    - prioritized mitigations with measurable risk reduction

    Strong answer tip:

    - explain one real issue you prevented with threat modeling


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/threat-modeling-and-attack-surface/#security-threat-modeling">🚀 See Full Deep Dive</a>


---

<div id="security-manifest-hardening"></div>

## What manifest hardening checks do you always enforce?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">manifest</span>
  <span class="question-badge question-badge--tag">hardening</span>
</div>

??? question "View Answer"

    Manifest hardening minimizes accidental exposure at install time.

    In interviews, cover:

    - explicit `android:exported` for every component
    - minimum required permissions only
    - `usesCleartextTraffic` and backup policy settings
    - custom permission protection levels for sensitive flows

    Strong answer tip:

    - mention automated lint/CI rules that block unsafe manifest changes


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/manifest-and-component-hardening/#security-manifest-hardening">🚀 See Full Deep Dive</a>


---

<div id="security-exported-components"></div>

## How do you secure exported Activities, Services, and Receivers?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">components</span>
  <span class="question-badge question-badge--tag">intents</span>
</div>

??? question "View Answer"

    Exported component security is about strict input validation and caller trust.

    In interviews, cover:

    - why exported components increase attack surface
    - caller verification and signature permissions
    - intent schema validation and default-deny behavior
    - tests for spoofed intents and privilege escalation attempts

    Strong answer tip:

    - describe one exploit pattern (intent spoofing) and your mitigation


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/manifest-and-component-hardening/#security-exported-components">🚀 See Full Deep Dive</a>


---

<div id="security-data-at-rest"></div>

## How do you protect sensitive data at rest on Android?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">storage</span>
  <span class="question-badge question-badge--tag">encryption</span>
</div>

??? question "View Answer"

    Data-at-rest protection combines least retention, strong crypto, and key isolation.

    In interviews, cover:

    - avoid storing secrets unless required
    - EncryptedSharedPreferences / SQLCipher-style patterns where needed
    - scoped storage and private app directories
    - secure deletion and data lifecycle considerations

    Strong answer tip:

    - connect storage controls to a specific compliance or threat scenario


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/data-protection-and-keystore/#security-data-at-rest">🚀 See Full Deep Dive</a>


---

<div id="security-keystore"></div>

## When do you use Android Keystore, and what are the common pitfalls?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">keystore</span>
  <span class="question-badge question-badge--tag">cryptography</span>
</div>

??? question "View Answer"

    Android Keystore protects key material from app memory and most filesystem attacks.

    In interviews, cover:

    - key generation and non-exportable private keys
    - hardware-backed keys and attestation support
    - key invalidation events (biometric enrollment, lock changes)
    - fallback strategy when hardware support is unavailable

    Strong answer tip:

    - explain key rotation and migration without user data loss


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/data-protection-and-keystore/#security-keystore">🚀 See Full Deep Dive</a>


---

<div id="security-network-config"></div>

## How do you use Network Security Config in production apps?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">tls</span>
</div>

??? question "View Answer"

    Network Security Config enforces transport security policy by environment.

    In interviews, cover:

    - cleartext disabled by default
    - debug-only trust anchors vs release trust anchors
    - per-domain policy for certificate expectations
    - rollout strategy to avoid breaking older clients

    Strong answer tip:

    - call out how you keep debug allowances out of release builds


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/network-security-and-api-abuse/#security-network-config">🚀 See Full Deep Dive</a>


---

<div id="security-cert-pinning"></div>

## When is certificate pinning worth the operational cost?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">certificate-pinning</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Pinning reduces MITM risk but increases outage risk if not rotated carefully.

    In interviews, cover:

    - threat model that justifies pinning
    - backup pins and expiration planning
    - staged rollout and kill-switch strategy
    - monitoring for TLS and pin failures in production

    Strong answer tip:

    - discuss both security gain and operational blast radius


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/network-security-and-api-abuse/#security-cert-pinning">🚀 See Full Deep Dive</a>


---

<div id="security-webview-hardening"></div>

## What are your WebView hardening defaults?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">webview</span>
  <span class="question-badge question-badge--tag">hardening</span>
</div>

??? question "View Answer"

    WebView hardening is about reducing script and bridge abuse.

    In interviews, cover:

    - disable JavaScript unless absolutely required
    - never expose unsafe JS interfaces
    - strict URL allowlisting and safe browsing
    - blocked file/content access where unnecessary

    Strong answer tip:

    - mention how you test for open-redirect and deep-link abuse paths


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/webview-and-client-side-hardening/#security-webview-hardening">🚀 See Full Deep Dive</a>


---

<div id="security-secret-management"></div>

## How do you keep API keys and secrets out of the APK?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">secrets</span>
  <span class="question-badge question-badge--tag">build</span>
</div>

??? question "View Answer"

    Client apps cannot safely hold true secrets, so design for exposure resistance.

    In interviews, cover:

    - classify public identifiers vs real secrets
    - move sensitive operations server-side
    - short-lived tokens and scoped credentials
    - build-time controls to prevent accidental secret commits

    Strong answer tip:

    - explain why obfuscation is not secret management


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/release-hardening-and-runtime-integrity/#security-secret-management">🚀 See Full Deep Dive</a>


---

<div id="security-r8-obfuscation"></div>

## What does R8/ProGuard protect, and what does it not protect?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">r8</span>
  <span class="question-badge question-badge--tag">reverse-engineering</span>
</div>

??? question "View Answer"

    Obfuscation raises reverse-engineering cost, but it is not a cryptographic control.

    In interviews, cover:

    - what shrinking/obfuscation changes in release binaries
    - where sensitive logic still remains recoverable
    - balancing stack trace quality with hardening
    - keeping mapping files secure and operationally accessible

    Strong answer tip:

    - combine obfuscation with backend authorization and abuse detection


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/release-hardening-and-runtime-integrity/#security-r8-obfuscation">🚀 See Full Deep Dive</a>


---

<div id="security-play-integrity"></div>

## How do you use Play Integrity API without locking out legitimate users?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">play-integrity</span>
  <span class="question-badge question-badge--tag">attestation</span>
</div>

??? question "View Answer"

    Integrity signals should inform risk decisions, not become a single hard block.

    In interviews, cover:

    - server-side verification flow and replay protection
    - risk tiers for suspicious vs clearly malicious devices
    - progressive friction (step-up auth) instead of blanket denial
    - monitoring false positives by market/device segment

    Strong answer tip:

    - describe a policy that balances fraud reduction and user retention


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/release-hardening-and-runtime-integrity/#security-play-integrity">🚀 See Full Deep Dive</a>


---

<div id="security-logging-pii"></div>

## How do you prevent sensitive data leaks through logs and analytics?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">privacy</span>
  <span class="question-badge question-badge--tag">observability</span>
</div>

??? question "View Answer"

    Logging safety requires explicit data classification and redaction by default.

    In interviews, cover:

    - never log credentials, tokens, or full PII
    - centralized redaction utilities and safe logging wrappers
    - privacy review for analytics schemas and events
    - retention controls and incident response for accidental leaks

    Strong answer tip:

    - show how your team enforced this with CI checks and code review rules


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/release-hardening-and-runtime-integrity/#security-logging-pii">🚀 See Full Deep Dive</a>


---

<div id="security-rasp-overview"></div>

## What is RASP and how does it apply to Android app security?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">runtime-protection</span>
</div>

??? question "View Answer"

    Runtime Application Self-Protection (RASP) embeds security controls directly inside the app so it can detect and respond to attacks while running.

    In interviews, cover:

    - RASP vs perimeter defenses: RASP acts from inside the process, not at the network edge
    - key detection categories: root, debugger, hook frameworks, emulators, tampered binaries
    - response strategies: silent reporting, graceful degradation, forced logout, or hard crash
    - balancing aggression against false positive rate on legitimate devices

    Strong answer tip:

    - distinguish RASP (active self-defense) from attestation (Play Integrity) and explain when you need both


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#security-rasp-overview">🚀 See Full Deep Dive</a>


---

<div id="security-root-detection"></div>

## How do you detect rooted or compromised devices at runtime?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">root-detection</span>
</div>

??? question "View Answer"

    Root detection is a probabilistic signal used to adjust trust level, not a hard gate.

    In interviews, cover:

    - file-system indicators: su binary, known root manager paths, magisk mount points
    - property checks: ro.build.tags, ro.debuggable, OTA keys
    - shell command execution tests and response analysis
    - Play Integrity verdict as a complementary, harder-to-spoof layer

    Strong answer tip:

    - explain that determined attackers can bypass any single check, so you layer signals and act proportionally rather than blocking all root users outright


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#security-root-detection">🚀 See Full Deep Dive</a>


---

<div id="security-hook-detection"></div>

## How do you detect Frida, Xposed, or LSPosed hooks at runtime?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">hook-detection</span>
  <span class="question-badge question-badge--tag">reverse-engineering</span>
</div>

??? question "View Answer"

    Hook framework detection targets the artifacts that instrumentation tools leave in the process.

    In interviews, cover:

    - Frida: detect frida-server port, frida-gadget library names in /proc/self/maps, pipe names, and native library scanning
    - Xposed/LSPosed: check for XposedBridge class presence, known module paths, and zygote load markers
    - method pointer integrity checks and unexpected inline hooks in native memory
    - native-layer detection to raise cost for script-level bypasses

    Strong answer tip:

    - mention that obfuscating your own detection code and running checks at unpredictable times makes bypassing significantly harder


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#security-hook-detection">🚀 See Full Deep Dive</a>


---

<div id="security-debugger-detection"></div>

## How do you detect debugger attachment and reverse-engineering tools at runtime?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">anti-debug</span>
</div>

??? question "View Answer"

    Anti-debug controls raise the cost of live analysis and slow down dynamic reverse engineering.

    In interviews, cover:

    - Java/Kotlin: Debug.isDebuggerConnected() and android:debuggable manifest flag checks
    - native: ptrace self-attachment trick to occupy the ptrace slot before an attacker can
    - TracerPid field in /proc/self/status to detect attached debuggers
    - timing attacks: measure execution time of sensitive paths; abnormal delay suggests single-stepping

    Strong answer tip:

    - combine anti-debug with certificate/signature checks and hook detection so multiple layers must all be bypassed simultaneously


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#security-debugger-detection">🚀 See Full Deep Dive</a>


---

<div id="security-anti-tamper"></div>

## How do you implement APK integrity and anti-tamper checks?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">integrity</span>
  <span class="question-badge question-badge--tag">anti-tamper</span>
</div>

??? question "View Answer"

    Anti-tamper checks verify the app has not been repackaged or patched after signing.

    In interviews, cover:

    - signature certificate hash check at runtime via PackageManager
    - APK hash / file-level checksum verification at launch
    - Play Integrity's appRecognitionVerdict as a server-side complement
    - native library hash check for critical .so files

    Strong answer tip:

    - store expected hashes server-side and rotate them at release so they cannot be patched out of the binary; bind sensitive API access to a valid integrity verdict


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#security-anti-tamper">🚀 See Full Deep Dive</a>


---

<div id="security-emulator-detection"></div>

## How do you detect emulated environments for abuse prevention?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">emulator-detection</span>
  <span class="question-badge question-badge--tag">abuse-prevention</span>
</div>

??? question "View Answer"

    Emulator detection is used to flag automation, bot farms, and fraud at scale.

    In interviews, cover:

    - Build property heuristics: FINGERPRINT, MANUFACTURER, MODEL containing "generic", "goldfish", "emulator"
    - hardware sensor absence or implausible sensor data
    - telephony checks: missing IMEI/IMSI, operator name anomalies
    - Play Integrity's deviceRecognitionVerdict as a harder-to-spoof signal

    Strong answer tip:

    - emulator detection is a risk signal, not a block; legitimate testers and accessibility users may also show unusual signals, so apply progressive friction rather than denial


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#security-emulator-detection">🚀 See Full Deep Dive</a>


---

<div id="security-rasp-response-strategy"></div>

## What response strategies should a RASP system use when a threat is detected?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">incident-response</span>
</div>

??? question "View Answer"

    RASP response must balance security effectiveness against user experience and false positives.

    In interviews, cover:

    - silent telemetry: log and report without acting, for low-confidence signals
    - graceful degradation: disable sensitive features (payments, PII) rather than full denial
    - step-up authentication: challenge the user with MFA before high-risk actions
    - forced logout or session invalidation for high-confidence compromise signals
    - hard crash as a last resort only for the highest-confidence, highest-stakes scenarios

    Strong answer tip:

    - every RASP action must be calibrated against false positive rates by device cohort; a policy that works on your test set can still misclassify millions of real users at scale


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#security-rasp-response-strategy">🚀 See Full Deep Dive</a>


---

<div id="security-dynamic-code-loading"></div>

## How do you control dynamic code loading to prevent code injection attacks?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">dynamic-code-loading</span>
  <span class="question-badge question-badge--tag">code-injection</span>
</div>

??? question "View Answer"

    Dynamic code loading is a common attack vector for post-install malware and repackaged apps.

    In interviews, cover:

    - avoid DexClassLoader / PathClassLoader with untrusted dex sources
    - verify code origin: only load dex from app's own private directory or verified CDN with hash check
    - use the android:usesCleartextTraffic restriction and HTTPS-only code delivery
    - Android 9+ enforces restrictions on loading code from world-writable locations

    Strong answer tip:

    - tie dynamic code loading to Play Asset Delivery or Feature Delivery with integrity verification rather than loading arbitrary URLs


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#security-dynamic-code-loading">🚀 See Full Deep Dive</a>


---

<div id="security-biometric-auth"></div>

## How do you implement biometric authentication securely in Android?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">biometric</span>
  <span class="question-badge question-badge--tag">authentication</span>
  <span class="question-badge question-badge--tag">keystore</span>
</div>

??? question "View Answer"

    Secure biometric authentication cryptographically binds authentication to Keystore-backed keys.

    In interviews, cover:

    - use BiometricPrompt with a CryptoObject backed by a Keystore key
    - set setUserAuthenticationRequired(true) and setInvalidatedByBiometricEnrollment(true)
    - handle key invalidation gracefully when new biometrics are enrolled
    - never rely on the boolean callback alone; always verify the CryptoObject operation result

    Strong answer tip:

    - explain the difference between Class 2 (weak) and Class 3 (strong) authenticators and why only Class 3 can unlock hardware-backed Keystore keys


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/data-protection-and-keystore/#security-biometric-auth">🚀 See Full Deep Dive</a>


---

<div id="security-third-party-sdk-risk"></div>

## How do you audit and manage the security risk introduced by third-party SDKs?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">supply-chain</span>
  <span class="question-badge question-badge--tag">third-party-sdks</span>
</div>

??? question "View Answer"

    Third-party SDKs are a critical supply-chain attack surface in mobile apps.

    In interviews, cover:

    - maintain an SDK inventory with version, permissions requested, and data-sharing profile
    - review SDK permissions and manifest merges for unexpected component exposure
    - network traffic analysis to verify SDKs communicate only with declared endpoints
    - dependency vulnerability scanning (OWASP Dependency-Check, Gradle dependency audit)
    - contractual and legal review for data processing agreements

    Strong answer tip:

    - treat SDK upgrades as you would any dependency change: review changelogs for security advisories and test in a controlled rollout before full release


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/threat-modeling-and-attack-surface/#security-third-party-sdk-risk">🚀 See Full Deep Dive</a>


---

<div id="security-deep-link-security"></div>

## How do you prevent insecure deep link and intent URI handling?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">deep-links</span>
  <span class="question-badge question-badge--tag">intents</span>
  <span class="question-badge question-badge--tag">input-validation</span>
</div>

??? question "View Answer"

    Deep links are an untrusted entry point that can drive users into unintended states.

    In interviews, cover:

    - verify the origin app and scheme/host allowlist before acting on deep link data
    - never pass raw URI parameters to WebViews, startActivity, or database queries without validation
    - use Android App Links (assetlinks.json) over plain URI schemes to prevent hijacking
    - test for open-redirect, parameter injection, and privilege-escalation via crafted links

    Strong answer tip:

    - treat every deep link as an unauthenticated external request: validate, sanitize, and require authentication before any sensitive action


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/manifest-and-component-hardening/#security-deep-link-security">🚀 See Full Deep Dive</a>


---

<div id="security-input-validation"></div>

## How do you defend against injection and input-based attacks in Android?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">input-validation</span>
  <span class="question-badge question-badge--tag">injection</span>
  <span class="question-badge question-badge--tag">sql-injection</span>
</div>

??? question "View Answer"

    Input validation prevents a wide class of injection, XSS, and path traversal bugs.

    In interviews, cover:

    - use parameterized queries or Room's compile-time SQL to eliminate SQLite injection
    - sanitize content shown in WebViews; avoid evaluateJavascript with user data
    - validate and canonicalize file paths before use; block directory traversal sequences
    - define an explicit allowlist for any user-supplied data driving control flow

    Strong answer tip:

    - layer validation at the point where data enters the app (network, intent, UI) and again before it reaches a sink (database, webview, filesystem)


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/webview-and-client-side-hardening/#security-input-validation">🚀 See Full Deep Dive</a>

