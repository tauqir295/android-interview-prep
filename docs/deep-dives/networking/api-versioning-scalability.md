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

## API Versioning & Scalability Deep Dive

## Overview
API versioning enables evolution. CDN scales static assets.
## Core Concepts
Versioning strategies:
1. Path: /v1/users
2. Header: Accept: application/vnd.api+v2
3. Query: /users?version=2
CDN caches static globally.
## Code Examples
```kotlin
// Retrofit with version header
val httpClient = OkHttpClient.Builder()
    .addNetworkInterceptor { chain ->
        val request = chain.request().newBuilder()
            .addHeader("API-Version", "2")
            .build()
        chain.proceed(request)
    }
    .build()
```
## Senior-Level Insights
- Support 2-3 versions simultaneously
- Deprecate old versions on timeline
- Use CDN for APK/updates
- API-as-backend vs backend-for-frontend
