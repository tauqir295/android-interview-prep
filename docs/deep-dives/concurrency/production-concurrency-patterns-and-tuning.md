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

## Production Concurrency Patterns and Tuning Deep Dive
## Overview
Production concurrency is a reliability discipline, not just raw throughput.
The goal is predictable latency under load while preserving correctness.
## Core Concepts
- bounded parallelism and backpressure
- main-safe API boundaries
- isolation between CPU and blocking I/O workloads
- observability-driven tuning
## Internal Implementation
High-quality systems define concurrency budgets per feature path.
Budgets are enforced via dispatcher selection, semaphore limits,
and bounded queue/buffer settings.
## Threading Model
Separate CPU-heavy transforms from blocking calls:
- `Default` for compute-heavy pure work
- `IO` for blocking boundaries
- main thread only for UI state publication
## Coroutine / Flow Behavior
Hot shared streams should use controlled replay/buffer sizes.
Shared upstream work (`stateIn`/`shareIn`) reduces duplication but must be
scoped correctly to avoid leaks and stale collectors.
## Code Examples
```kotlin
private val networkGate = Semaphore(permits = 8)
suspend fun <T> boundedNetworkCall(block: suspend () -> T): T {
    return networkGate.withPermit {
        withContext(Dispatchers.IO) { block() }
    }
}
```
## Common Interview Questions
- How do you prevent a coroutine fan-out storm?
- What metrics guide concurrency tuning?
- How do you balance throughput vs tail latency?
- Why are bounded queues safer than unbounded buffers?
## Production Considerations
- define feature-level concurrency limits
- keep cancellation cooperative end-to-end
- fail fast when dependency saturation is detected
- add circuit-breaker/retry policies with jitter
## Performance Insights
Unbounded concurrency often looks fast in local tests and fails in production.
Bounded, observable pipelines usually win on p95/p99 behavior.
## Senior-Level Insights
At staff level, discuss concurrency as capacity planning:
resource budgets, overload policy, and operational runbooks.
