---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/networking/">← Back to Networking</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/networking/${hash}`);
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

## Certificate Pinning Deep Dive

## Overview
Certificate pinning roots trust in specific server certificates, preventing MITM attacks via compromised CAs.
## Core Concepts
CertificatePinner pins SHA-256 hashes of certificates:
```kotlin
CertificatePinner.Builder()
    .add("example.com", "sha256/AAAA...")
    .add("*.example.com", "sha256/BBBB...")
    .build()
```
## Code Examples
```kotlin
val pinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/47DEQpj8HBSa...")
    .build()
val httpClient = OkHttp.Builder()
    .certificatePinner(pinner)
    .build()
```
## Senior-Level Insights
- Pin multiple hashes for failover
- Update hashes when certificates rotate
- Handle pin failures gracefully (log, but allow optional bypass for dev)
