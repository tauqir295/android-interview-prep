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

## Rate Limiting & Idempotency Deep Dive

## Overview
Rate limits prevent abuse. Idempotency enables safe retries.
## Core Concepts
Rate limit headers:
- X-RateLimit-Limit
- X-RateLimit-Remaining
- X-RateLimit-Reset
- Retry-After
Idempotency-Key: UUID for deduplication
## Code Examples
```kotlin
// Add Idempotency-Key to POST
val requestBody = RequestBody.create(...) 
val request = Request.Builder()
    .post(requestBody)
    .addHeader("Idempotency-Key", UUID.randomUUID().toString())
    .build()
```
## Senior-Level Insights
- Respect rate limits (back off exponentially)
- Per-user vs global limits
- Circuit breaker on repeated 429s
