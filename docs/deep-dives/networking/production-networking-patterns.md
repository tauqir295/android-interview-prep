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

## Production Networking Patterns Deep Dive

## Overview
Production patterns: timeouts, security config, monitoring.
## Core Concepts
Timeouts prevent indefinite waits:
- connectTimeout: 10-30s
- readTimeout: 20-60s  
- writeTimeout: 20-60s
- callTimeout: includes retries
## Code Examples
```kotlin
val httpClient = OkHttpClient.Builder()
    .connectTimeout(30, TimeUnit.SECONDS)
    .readTimeout(60, TimeUnit.SECONDS)
    .writeTimeout(60, TimeUnit.SECONDS)
    .callTimeout(120, TimeUnit.SECONDS)
    .build()
// Network Security Config XML
<domain-config>
    <domain includeSubdomains="true">example.com</domain>
    <pin-set>
        <pin digest="SHA-256">...</pin>
    </pin-set>
</domain-config>
```
## Senior-Level Insights
- One OkHttp instance per app
- Connection pool management
- Timeouts must account for network latency
- Production monitoring: latency, errors, bandwidth
