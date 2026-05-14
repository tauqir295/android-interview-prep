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

## Core Concepts

## Runtime Internals

## Composition / Recomposition Flow

## State Management

## Code Examples

```kotlin
@Composable
fun Example() {
}
```

## Common Interview Questions

## Production Considerations

## Performance Insights

## Senior-Level Insights

### Retrofit as an Anti-Pattern in Some Cases

Retrofit is excellent for CRUD APIs but can be verbose for:

- Streaming APIs with continuous data
- WebSocket-based services
- gRPC calls (different protocol entirely)

### Call Adapter Architecture

Retrofit uses a `CallAdapter` pattern:

```kotlin
// Built-in adapters
Response<T> -> Call<T> (default OkHttp)
suspend T -> Call<T> (coroutines)
Flow<T> -> Call<T> (reactive)
```

This allows different async models without changing core logic. Staff engineers should understand how adapters compose with converters.

### Common Pitfall: Suspending Scope Cancellation

Never wrap suspend in `runBlocking` or `GlobalScope`:

```kotlin
// WRONG - defeats coroutine benefit
GlobalScope.launch {
    val user = userService.getUser(1)
}

// RIGHT - cancellation flows naturally
viewModelScope.launch {
    val user = userService.getUser(1)
}
```

### Interceptor Ordering

Order matters in OkHttp:

1. Application interceptors (auth injection)
2. Network interceptors (logging, compression)
3. Actual network call

Wrong order = auth not applied or logging sees wrong data.

