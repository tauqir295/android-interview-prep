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

