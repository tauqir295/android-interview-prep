---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/concurrency/">← Back to Concurrency</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/concurrency/${hash}`);
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

## CallbackFlow and ChannelFlow Deep Dive
## Overview
`callbackFlow` and `channelFlow` bridge callback or multi-producer systems
into structured Flow pipelines.
## Core Concepts
- adapter pattern from callback APIs to Flow
- proper registration/unregistration lifecycle
- backpressure with channel capacity and send strategy
- multi-producer safety inside `channelFlow`
## Internal Implementation
`callbackFlow` exposes a channel-backed producer scope.
`awaitClose` is the cleanup contract and must release listeners/resources.
`channelFlow` allows launching child coroutines that concurrently `send` into
one downstream flow channel.
## Threading Model
Callbacks may fire on arbitrary threads. Emission to flow must remain
thread-safe, non-blocking where possible, and cancellation-aware.
## Coroutine / Flow Behavior
Backpressure choices (`buffer`, conflation, default channel capacity)
change delivery semantics and memory behavior under bursty callbacks.
## Code Examples
```kotlin
fun LocationClient.locationUpdates(): Flow<Location> = callbackFlow {
    val listener = object : Listener {
        override fun onLocation(location: Location) {
            trySend(location).isSuccess
        }
    }
    register(listener)
    awaitClose { unregister(listener) }
}
```
## Common Interview Questions
- Why is `awaitClose` mandatory in most callback adapters?
- When is `channelFlow` preferred over `callbackFlow`?
- How do you avoid dropping critical callback events?
- What happens if callback thread is blocked by flow emission?
## Production Considerations
- always clean up listeners
- avoid heavy work in callback thread
- choose buffer strategy by event criticality
- guard adapters with timeout/error telemetry
## Performance Insights
Most callback-flow issues are leak and burst handling problems,
not operator selection. Measure burst rate and channel pressure.
## Senior-Level Insights
Staff-level answers should discuss migration strategy:
wrapping legacy callback SDKs into flow-first APIs with explicit ownership.
