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

## Compression & Optimization Deep Dive

## Overview
Compression (gzip, brotli) reduces bandwidth.
## Core Concepts
- Accept-Encoding request header
- Content-Encoding response header
- OkHttp handles automatically
- Saves ~60-80% bandwidth
## Code Examples
```kotlin
// Already transparent in OkHttp
val httpClient = OkHttpClient.Builder()
    .addNetworkInterceptor { chain ->
        val response = chain.proceed(chain.request())
        // OkHttp automatically decompresses
        response
    }
    .build()
```
## Senior-Level Insights
- Compression trade-off: CPU vs bandwidth
- For images: compress beforehand (WebP, HEIC)
- Disable for pre-compressed (videos)
