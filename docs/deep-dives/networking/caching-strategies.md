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

## Caching Strategies Deep Dive

## Overview
HTTP caching reduces bandwidth and latency.
## Core Concepts
Cache-Control header values:
- `max-age=300`: cache 5 minutes
- `no-cache`: revalidate always
- `no-store`: never cache
- `private/public`: for CDN
## Code Examples
```kotlin
// OkHttp automatic caching
val httpClient = OkHttpClient.Builder()
    .cache(Cache(cacheDir, 10L * 1024 * 1024))  // 10MB
    .build()
```
## Senior-Level Insights
- Respect server Cache-Control headers
- Use ETags for validation
- Offline fallback: serve stale cache on error
