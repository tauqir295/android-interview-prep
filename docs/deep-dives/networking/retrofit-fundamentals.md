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

## Retrofit Fundamentals Deep Dive
## Overview
This topic is essential for Android networking interviews because it combines robust API design, converter behavior, and coroutine execution over OkHttp.
## Core Concepts
- Keep API contracts explicit and versioned.
- Separate transport errors from domain errors.
- Prefer deterministic request/response mapping.
## Internal Implementation
- Retrofit handles interface parsing and adapter wiring.
- OkHttp performs connection management and interceptors.
- Converters map payloads into stable models.
## Request/Response Flow
- Build request from endpoint + headers + body.
- Execute call through interceptor chain.
- Map HTTP response into success/error result types.
## Caching & Persistence
- Use HTTP cache directives where possible.
- Persist critical data for offline reads.
- Define stale-read and refresh strategy explicitly.
## Code Examples
```kotlin
interface UserApi {
    @GET("users")
    suspend fun users(): List<UserDto>
}
```
## Common Interview Questions
- **Q:** How do you structure API interfaces for long-term maintainability?
  **A:** Answer with API contract and failure semantics: timeout and retry policy, idempotency, error mapping, and observability for client and server behavior.
- **Q:** Where should retry and timeout logic live?
  **A:** Answer with API contract and failure semantics: timeout and retry policy, idempotency, error mapping, and observability for client and server behavior.
- **Q:** How do you expose failures to the UI layer?
  **A:** Answer with API contract and failure semantics: timeout and retry policy, idempotency, error mapping, and observability for client and server behavior.
## Production Considerations
- Add telemetry around status codes and latency percentiles.
- Guard against schema drift with robust parsing defaults.
- Use idempotency where retries can duplicate side effects.
## Performance Insights
- Reuse connections aggressively through OkHttp pooling.
- Minimize payload size and serialization overhead.
## Senior-Level Insights
- Strong answers include migration strategy and backward compatibility policy.
