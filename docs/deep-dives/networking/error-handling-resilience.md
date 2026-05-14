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

## Error Handling & Resilience Deep Dive

## Overview
Network errors are inevitable. Handle gracefully.
## Core Concepts
Error categories:
- No connectivity (offline)
- Timeout
- 4xx client error (retry-safe: only 429)
- 5xx server error (retry-safe)
- Parse error (non-retriable)
## Code Examples
```kotlin
// Error classification
sealed class Result<T> {
    data class Success<T>(val data: T) : Result<T>()
    data class NetworkError<T>(val ex: IOException) : Result<T>()
    data class HttpError<T>(val code: Int) : Result<T>()
    data class ParseError<T>(val ex: Exception) : Result<T>()
}
// Retry decision
fun shouldRetry(result: Result<*>): Boolean {
    return result is Result.NetworkError || 
           result is Result.HttpError && result.code >= 500
}
```
## Senior-Level Insights
- Classify errors for metrics
- Fallback to cached data
- Expose errors to user appropriately
