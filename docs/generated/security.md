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


---

<div id="explain-android-security-basics-intents-exported-components-pendingint"></div>

## Explain Android security basics - intents, exported components, PendingIntent mutability, and deep link risks

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">android</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">intents</span>
  <span class="question-badge question-badge--tag">components</span>
  <span class="question-badge question-badge--tag">exported</span>
</div>

??? question "View Answer"

    Intent-based attacks remain one of the most common Android vulnerabilities; the export flag, PendingIntent mutability, and deep link validation are the key controls.

    In interviews, cover:

    - exported=true on Activity/Service/Receiver without permission check allows any app to start that component; attackers can inject data, bypass authentication screens, or exfiltrate data through exported content providers

    - API 31+: android:exported is mandatory for components with intent-filters; missing it causes install failure; always set false unless intentionally public

    - PendingIntent.FLAG_MUTABLE allows the recipient to modify the Intent extras; use FLAG_IMMUTABLE for all PendingIntents that don't need to be mutated; mutable PendingIntents can be exploited by a malicious forwarder

    - deep links: validate the scheme, host, and path; do not trust extras from an deep link intent without server-side validation; an attacker can craft a link that opens your Activity with malicious extras

    Strong answer tip:

    - intent redirection attack: an exported Activity reads an Intent from extras and starts it — this allows a malicious app to use your app as a proxy to reach non-exported components; never startActivity(intent.getParcelableExtra())

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-android-security-basics-intents-exported-components-pendingint">🚀 See Full Deep Dive</a>


---

<div id="explain-font-scaling-and-dynamic-type-designing-for-1-0-to-2-0-scale-f"></div>

## Explain font scaling and dynamic type - designing for 1.0× to 2.0× scale factors without layout breaking

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">android</span>
  <span class="question-badge question-badge--tag">accessibility</span>
  <span class="question-badge question-badge--tag">font-scaling</span>
  <span class="question-badge question-badge--tag">dynamic-type</span>
  <span class="question-badge question-badge--tag">layout</span>
</div>

??? question "View Answer"

    Android allows users to set font scale from 0.85× to 2.0× (and higher on some OEMs); layouts that use fixed heights, hardcoded line counts, or sp-in-dp mixing break at non-default scales.

    In interviews, cover:

    - always use sp for text sizes (they respect font scale); never dp for text sizes — this is the most common error

    - fixed-height containers that hold text will clip at 2× scale; use wrap_content or minimum height constraints; in Compose use wrapContentHeight() or the Intrinsic height pattern

    - maxLines with overflow=Ellipsis: test at 2× to ensure important information is not hidden; provide a "show more" affordance for critical content

    - test using: adb shell settings put system font_scale 2.0 to simulate max scale without changing device accessibility settings

    Strong answer tip:

    - on Android 13+, users can set Large Text independently of display size; test both dimension axes — a layout might work at 2× font scale but fail at 2× font scale + large display size simultaneously

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-font-scaling-and-dynamic-type-designing-for-1-0-to-2-0-scale-f">🚀 See Full Deep Dive</a>


---

<div id="explain-token-handling-access-tokens-vs-refresh-tokens-rotation-and-se"></div>

## Explain token handling - access tokens vs refresh tokens, rotation, and secure logout

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">authentication</span>
  <span class="question-badge question-badge--tag">tokens</span>
  <span class="question-badge question-badge--tag">oauth</span>
</div>

??? question "View Answer"

    Access tokens are short-lived credentials for API calls; refresh tokens are long-lived credentials used only to obtain new access tokens — their storage and rotation requirements differ significantly.

    In interviews, cover:

    - access token: keep in memory only (process-scope variable); short TTL (15 minutes typical); never persist to disk — if the process is killed and restarted, the refresh token obtains a new one

    - refresh token: persist in Android Keystore-backed EncryptedSharedPreferences or a keystore-wrapped encrypted file; long TTL (days/months); must be rotated on use (refresh token rotation) to detect theft

    - refresh token rotation: on each token refresh, the server issues a new refresh token and invalidates the old one; if an old refresh token is used again (stolen and replayed), the server detects reuse and revokes the entire session family

    - secure logout: delete the refresh token from secure storage, call the server-side token revocation endpoint, and clear in-memory access tokens; do not rely only on client-side clearing

    Strong answer tip:

    - biometric-protected refresh tokens: store the refresh token encrypted; decrypt it only after biometric authentication — this prevents token extraction even on a rooted device

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-token-handling-access-tokens-vs-refresh-tokens-rotation-and-se">🚀 See Full Deep Dive</a>


---

<div id="explain-sensitive-ui-input-security-pins-otps-keyboard-suggestions-aut"></div>

## Explain sensitive UI input security - PINs, OTPs, keyboard suggestions, autofill, and screenshots

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">ui</span>
  <span class="question-badge question-badge--tag">input</span>
  <span class="question-badge question-badge--tag">privacy</span>
  <span class="question-badge question-badge--tag">autofill</span>
</div>

??? question "View Answer"

    Sensitive input fields require explicit opt-out from OS intelligence features that cache and expose entered data.

    In interviews, cover:

    - disable suggestions and autocorrect for PIN/OTP fields: InputType.TYPE_TEXT_FLAG_NO_SUGGESTIONS | InputType.TYPE_TEXT_VARIATION_VISIBLE_PASSWORD in EditText; in Compose use KeyboardOptions(autoCorrect=false, keyboardType=KeyboardType.NumberPassword)

    - prevent autofill on sensitive fields: android:importantForAutofill="no" in Views or AutofillType.NONE in custom autofill services; Compose equivalent: Modifier.semantics { contentType = ContentType.None }

    - secure flag to prevent screenshots: WindowManager.LayoutParams.FLAG_SECURE on the Window; this also prevents the screen from appearing in Recents

    - clipboard: if the user copies a password/OTP, clear the clipboard after 30–60 seconds with ClipboardManager.setPrimaryClip(ClipData.newPlainText("",""))

    Strong answer tip:

    - keyboard caching: even with no-suggestions, some third-party keyboards (SwiftKey, Gboard before settings) may cache keystrokes; advise high-security apps to recommend device default keyboard and inform users

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-sensitive-ui-input-security-pins-otps-keyboard-suggestions-aut">🚀 See Full Deep Dive</a>


---

<div id="explain-clipboard-security-risks-otp-interception-clipboard-snooping-a"></div>

## Explain clipboard security risks - OTP interception, clipboard snooping, and safe UX patterns

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">clipboard</span>
  <span class="question-badge question-badge--tag">privacy</span>
  <span class="question-badge question-badge--tag">otp</span>
</div>

??? question "View Answer"

    A malicious app with READ_CLIPBOARD permission (pre-API 29) or through background reads (API 29-) can silently read clipboard contents including OTPs, passwords, and sensitive data.

    In interviews, cover:

    - API 29+: apps reading clipboard while in background show a toast notification (API 29) and are then blocked (API 31+); the restriction significantly reduced silent clipboard snooping

    - OTP intercept: before this restriction, banking malware read SMS OTP values copied to clipboard; now recommend users not copy OTPs and auto-fill them from SMS with SMS Retriever API instead

    - sensitive content in clipboard: any sensitive value put on the clipboard is accessible to all foreground apps and system; clear it after a timeout using Handler.postDelayed { clipManager.clearPrimaryClip() }

    - in-app clipboard actions: show a "Copied — will clear in 30s" indicator and programmatically clear; avoid leaving tokens, account numbers, or passwords in the clipboard permanently

    Strong answer tip:

    - API 33+: ClipDescription.hasMimeType() allows apps to check if clipboard contains sensitive marked content without reading it; combine with content:// URI-based sharing to avoid plain-text exposure

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-clipboard-security-risks-otp-interception-clipboard-snooping-a">🚀 See Full Deep Dive</a>


---

<div id="explain-account-takeover-ato-defenses-layered-approach-for-consumer-mo"></div>

## Explain account takeover (ATO) defenses - layered approach for consumer mobile apps

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">account-takeover</span>
  <span class="question-badge question-badge--tag">authentication</span>
  <span class="question-badge question-badge--tag">mfa</span>
</div>

??? question "View Answer"

    Account takeover is the primary fraud vector for consumer apps; defense requires layering detection signals, step-up authentication, and anomaly-based risk engines.

    In interviews, cover:

    - credential stuffing: automated attacks using leaked credential lists; defend with rate limiting on the login endpoint, device fingerprinting, and anomaly detection on login geography/time

    - risk signals: device attestation (Play Integrity), behavioral biometrics (typing speed, swipe pattern), unusual velocity (5 logins in 1 minute from the same device)

    - step-up auth: trigger MFA or re-authentication for high-risk actions (password change, new payment method, large transfer) even after initial login

    - account recovery: make recovery flows as secure as the primary login; email OTP or hardware key; avoid security questions (guessable) or SMS-only recovery (SIM-swap vulnerable)

    - suspicious activity notification: send a real-time push/email when a new device logs in, password is changed, or payment method is added

    Strong answer tip:

    - for high-value accounts, implement mutual TLS with client certificates bound to the device identity via Android Keystore — this ties the session to a specific hardware key that cannot be cloned

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-account-takeover-ato-defenses-layered-approach-for-consumer-mo">🚀 See Full Deep Dive</a>


---

<div id="explain-passkeys-and-fido2-for-consumer-android-apps-implementation-an"></div>

## Explain Passkeys and FIDO2 for consumer Android apps - implementation and UX tradeoffs

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">passkeys</span>
  <span class="question-badge question-badge--tag">fido2</span>
  <span class="question-badge question-badge--tag">authentication</span>
  <span class="question-badge question-badge--tag">biometrics</span>
</div>

??? question "View Answer"

    Passkeys replace passwords with a public-key cryptographic credential bound to the device; Android 9+ supports FIDO2 through the Credential Manager API.

    In interviews, cover:

    - how passkeys work: registration creates a public-private key pair; the private key stays on the device protected by the secure element or Android Keystore; the server stores the public key; authentication signs a server challenge with the private key — no password is ever transmitted

    - Android implementation: Credential Manager API (single API for passwords, passkeys, and federated credentials since API 28); FIDO2 support through Google Play Services and hardware security keys

    - phishing resistance: passkeys are origin-bound; a credential registered at example.com cannot be used by phishing-site.com — fundamental security advantage over passwords and TOTP

    - UX: passkey creation and authentication use biometric prompts (fingerprint/face); Cloud backup via Google Password Manager allows passkey sync across devices within the same account

    - transition: support both password and passkey during migration; offer passkey upgrade prompts post-login

    Strong answer tip:

    - linked domains: ensure .well-known/assetlinks.json is correctly configured; without it, Android will not associate the app with the web origin and passkey registration fails

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-passkeys-and-fido2-for-consumer-android-apps-implementation-an">🚀 See Full Deep Dive</a>


---

<div id="explain-session-fixation-and-session-hijacking-protections-in-android-"></div>

## Explain session fixation and session hijacking protections in Android apps

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">session</span>
  <span class="question-badge question-badge--tag">authentication</span>
  <span class="question-badge question-badge--tag">tokens</span>
</div>

??? question "View Answer"

    Session fixation and hijacking exploit weaknesses in how session tokens are generated, transmitted, or bound to a device identity.

    In interviews, cover:

    - session fixation: an attacker forces a victim to use a known session ID; defend by always regenerating the session token on successful login — never reuse a pre-authentication session token

    - session hijacking: theft of a valid session token via man-in-the-middle, log exposure, or storage extraction; defend with HTTPS everywhere, short session TTLs, and app-layer token binding

    - token binding: bind the session token to the device's TLS client certificate or use the Android Keystore to sign a challenge with each request (similar to mutual TLS) — the token becomes useless without the private key

    - concurrent session detection: track active sessions by device ID; alert users to unrecognized sessions; provide "log out everywhere" functionality

    Strong answer tip:

    - absolute session timeout: regardless of activity, sessions must expire after a maximum duration (e.g. 30 days); lazy expiry alone is insufficient for high-security applications

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-session-fixation-and-session-hijacking-protections-in-android-">🚀 See Full Deep Dive</a>


---

<div id="explain-push-messaging-security-fcm-token-management-spoofing-and-priv"></div>

## Explain push messaging security - FCM token management, spoofing, and privacy

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">fcm</span>
  <span class="question-badge question-badge--tag">push-notifications</span>
  <span class="question-badge question-badge--tag">privacy</span>
</div>

??? question "View Answer"

    FCM tokens are sensitive; they enable targeting a user's device with notifications that can be used for social engineering, data exfiltration via notification content, or notification spam.

    In interviews, cover:

    - token management: FCM registration tokens can change (app update, data clear, token rotation); always update the server-stored token immediately on onNewToken() callback; stale tokens cause missed notifications

    - server-side validation: never include sensitive data (auth tokens, PII) in FCM payloads — the server-side should send a data-only notification that triggers the app to fetch actual data securely with authentication

    - spoofing: an attacker with a valid FCM project can send messages to your tokens IF they are leaked; keep FCM API keys server-side only — never in the APK; use Firebase App Attestation if driving secure notification flows

    - notification phishing: craft legitimate-looking notifications that link to phishing UIs; validate deep link targets from notification taps before processing; treat notification extras as untrusted input

    Strong answer tip:

    - for high-security notifications (banking alerts, 2FA codes), encrypt the notification payload with the user's device-specific key derived from Android Keystore — only decryptable on the target device

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-push-messaging-security-fcm-token-management-spoofing-and-priv">🚀 See Full Deep Dive</a>


---

<div id="explain-device-compromise-handling-root-and-hook-detection-as-security"></div>

## Explain device compromise handling - root and hook detection as security risk signals

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">rasp</span>
  <span class="question-badge question-badge--tag">root-detection</span>
  <span class="question-badge question-badge--tag">frida</span>
  <span class="question-badge question-badge--tag">integrity</span>
</div>

??? question "View Answer"

    Root and hook detection should feed into a risk signal system rather than blocking access outright — false positives on legitimate root users (developers, power users) are too costly at scale.

    In interviews, cover:

    - signals: su binary presence, test-keys build tags, known root manager packages (Magisk), TracerPid in /proc/self/status (debugger attached), Frida port 27042 open, Xposed/LSPosed class loading, Play Integrity MEETS_BASIC_INTEGRITY=false

    - response tiers: one signal → silent telemetry; multiple signals → disable high-risk features (payments, PII export); critical signals + Play Integrity failure → step-up auth or forced logout

    - false positives: custom ROMs, developer devices, and some enterprise MDM configurations trigger root signals without being malicious; set thresholds based on device cohort telemetry before enforcing

    - Play Integrity as the gold standard: MEETS_STRONG_INTEGRITY verifies hardware-backed attestation — much harder to spoof than on-device software checks

    Strong answer tip:

    - never block the entire app on a single heuristic; implement graceful degradation — allow read-only access while blocking write/payment paths; log the attempt for fraud review

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-device-compromise-handling-root-and-hook-detection-as-security">🚀 See Full Deep Dive</a>


---

<div id="explain-secure-high-risk-action-policies-payments-profile-changes-and-"></div>

## Explain secure high-risk action policies - payments, profile changes, and step-up authentication

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">authentication</span>
  <span class="question-badge question-badge--tag">payments</span>
  <span class="question-badge question-badge--tag">step-up-auth</span>
</div>

??? question "View Answer"

    High-risk actions (adding a payment method, changing password, initiating a large transfer) require re-verification of identity at the time of the action, not just at login.

    In interviews, cover:

    - step-up authentication: after a successful standard login, high-risk actions prompt biometric re-verification or OTP confirmation — even if the session is valid and recent

    - time-bound authorization: issue a short-lived action token (5–15 minutes TTL) after step-up; the token authorizes only the specific action type; prevents token reuse for other sensitive operations

    - server-side enforcement: the client-side prompt is UX only; the server must reject high-risk actions that arrive without a valid step-up token regardless of session state

    - cooling period: after 3 failed step-up attempts, require account recovery flow — prevents brute force on biometric prompts or OTP codes

    Strong answer tip:

    - for payments specifically, bind the payment authorization to the device, amount, and recipient in the signed payload — a stolen step-up token cannot be replayed for a different payment target

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-secure-high-risk-action-policies-payments-profile-changes-and-">🚀 See Full Deep Dive</a>


---

<div id="explain-abuse-response-readiness-detection-throttling-and-incident-res"></div>

## Explain abuse response readiness - detection, throttling, and incident response for consumer apps

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">abuse</span>
  <span class="question-badge question-badge--tag">fraud</span>
  <span class="question-badge question-badge--tag">incident-response</span>
</div>

??? question "View Answer"

    Abuse response readiness means having monitoring, rate limiting, kill switches, and runbooks in place before an attack happens — not building them during one.

    In interviews, cover:

    - detection signals: unusual API call rates per device/user, geographic anomalies, device fingerprint clusters (all attacks from the same device farm), account velocity (50 new accounts from one device subnet)

    - throttling layer: exponential backoff requirements on login, OTP, and payment endpoints; 429 responses with Retry-After headers; device-level rate limiting through Play Integrity token verification frequency caps

    - kill switches: ability to force all clients to re-authenticate, revoke token families, disable specific features (gift card purchase, new account creation) without an app update

    - incident runbook: define escalation paths (security on-call → engineering lead → legal/comms); have pre-drafted user communications; document rollback steps for every high-risk backend change

    Strong answer tip:

    - red team exercises: regularly simulate attacks (credential stuffing, payment fraud, scraping) against staging environments and verify detection and response mechanisms fire correctly

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/#explain-abuse-response-readiness-detection-throttling-and-incident-res">🚀 See Full Deep Dive</a>

