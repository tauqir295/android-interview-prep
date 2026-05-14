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

## Synchronization and Mutex Deep Dive
## Overview
Correctness in concurrent code starts with controlling shared mutable state.
`Mutex` is a coroutine-native primitive for serializing critical sections
without blocking threads.
## Core Concepts
- mutual exclusion for write-sensitive regions
- coroutine suspension while waiting for lock ownership
- lock granularity and ownership boundaries
- alternatives: atomics, confinement, immutable snapshots
## Internal Implementation
`Mutex` in `kotlinx.coroutines` is suspend-aware. Waiting coroutines are queued
and resumed when the lock is released. This differs from JVM monitor locks,
which block the underlying thread.
Fairness is not a universal guarantee; design for correctness first,
then tune contention hotspots based on measurement.
## Threading Model
`withLock` can run on any dispatcher, but the protected state should have
clear access boundaries. Mixing long blocking calls inside critical sections
causes pool contention and latency spikes.
## Coroutine / Flow Behavior
In Flow pipelines, shared caches or dedupe maps often need serialized updates.
Use short critical regions around mutation, then emit outside the lock when
possible to avoid lock convoy behavior.
## Code Examples
```kotlin
private val cacheLock = Mutex()
private val cache = mutableMapOf<String, User>()
suspend fun getOrLoadUser(id: String): User {
    cacheLock.withLock {
        cache[id]?.let { return it }
    }
    val loaded = api.getUser(id)
    cacheLock.withLock {
        return cache.getOrPut(id) { loaded }
    }
}
```
## Common Interview Questions
- When is `Mutex` better than `synchronized` in coroutine code?
- Why should lock scope be as small as possible?
- When should you prefer atomics over lock-based protection?
- How do you avoid deadlocks with multiple locks?
## Production Considerations
- guard only truly shared mutable state
- keep critical sections small and non-blocking
- use immutable snapshots for read-mostly paths
- capture contention metrics on hot locks
## Performance Insights
Most performance loss is lock contention, not lock acquisition itself.
Reducing lock hold time usually beats introducing complicated lock-free logic.
## Senior-Level Insights
Senior answers should frame synchronization as a design choice:
where shared state exists, why it exists, and what invariant each lock protects.
