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

## Shared State and Race Conditions Deep Dive
## Overview
Race conditions emerge when mutable state is accessed concurrently without a
clear synchronization or ownership model.
## Core Concepts
- shared mutable state as root risk
- atomic updates for simple state transitions
- thread confinement and actor-style ownership
- immutable snapshots for read-heavy systems
## Internal Implementation
Races occur because interleaving is non-deterministic.
Even simple read-modify-write operations can break invariants without atomicity.
Atomics solve specific primitive updates; complex invariants require
serialization (`Mutex`) or single-owner message passing.
## Threading Model
Confining mutable state to one dispatcher/thread removes many classes of race.
Cross-thread mutation should happen through explicit synchronization primitives.
## Coroutine / Flow Behavior
Flows can hide race sources when multiple collectors mutate shared maps/lists.
Favor immutable emissions and centralized state reducers.
## Code Examples
```kotlin
private val counter = AtomicInteger(0)
fun incrementSafe(): Int = counter.incrementAndGet()
private val singleThread = Dispatchers.Default.limitedParallelism(1)
suspend fun confinedUpdate(state: MutableStateFlow<Int>) {
    withContext(singleThread) {
        state.value = state.value + 1
    }
}
```
## Common Interview Questions
- Why can `x = x + 1` fail under concurrency?
- When are atomics enough, and when are they not?
- How does thread confinement simplify correctness?
- What architecture reduces race-condition surface area?
## Production Considerations
- minimize shared mutable structures
- centralize mutation points
- encode invariants in reducers/use-cases
- run stress tests for high-contention paths
## Performance Insights
Eliminating shared mutable state often improves both correctness and latency
by reducing lock contention and retry loops.
## Senior-Level Insights
Senior candidates should articulate invariant protection strategy per subsystem,
not just list primitives.
