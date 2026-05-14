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

## Retry & Exponential Backoff Deep Dive

## Overview
Retry logic + exponential backoff handle transient failures without overwhelming servers.
## Core Concepts
- Idempotent operations (GET, PUT, DELETE) can retry
- Non-idempotent (POST create) need caution
- Exponential backoff: 2^attempt * base + jitter
## Code Examples
```kotlin
// OkHttp retry interceptor
class RetryInterceptor : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        repeat(3) { attempt ->
            try {
                return chain.proceed(chain.request())
            } catch (e: IOException) {
                if (attempt == 2) throw
                Thread.sleep(100 * (2.0.pow(attempt.toDouble())).toLong())
            }
        }
    }
}
```
## Senior-Level Insights
- Jitter prevents thundering herd
- Set max total time, not just attempts
- Backoff: connect > read > write timeouts
