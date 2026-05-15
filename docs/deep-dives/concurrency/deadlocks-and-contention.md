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

## Deadlocks and Contention Deep Dive
## Overview
Deadlocks and heavy contention are two of the most expensive concurrency bugs:
correctness failures on one end and severe latency regressions on the other.
## Core Concepts
- deadlock: cyclic waiting between resources
- contention: many workers competing for shared resources
- livelock/starvation as related failure modes
- prevention through ordering and bounded concurrency
## Internal Implementation
Deadlocks emerge from waiting graphs: coroutine A waits on resource held by B,
while B waits on A (or a longer cycle). Coroutines make this less visible
because suspension hides blocking semantics behind `await`/`withLock` calls.
Contention appears when synchronization points serialize otherwise parallel work,
creating queue buildup and poor tail latency.
## Threading Model
Main-thread deadlocks often involve nested dispatch to main while already
holding a lock from background code. Worker-pool deadlocks can appear when
all threads block waiting for tasks that cannot start.
## Coroutine / Flow Behavior
Flow pipelines can deadlock indirectly if collectors wait for producers that are
blocked by downstream callbacks. Contention appears as long collector backlogs,
frequent context switching, and growing buffer pressure.
## Code Examples
```kotlin
private val lockA = Mutex()
private val lockB = Mutex()
suspend fun badOrder() {
    lockA.withLock {
        lockB.withLock {
            // work
        }
    }
}
suspend fun saferOrder() {
    // enforce a single global lock ordering policy
    lockA.withLock {
        lockB.withLock {
            // work
        }
    }
}
```
## Common Interview Questions
- **Q:** How do deadlocks happen in coroutine code?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** How do you diagnose lock contention in production?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** Why can bounded parallelism reduce contention?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** What is the difference between deadlock and starvation?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
## Production Considerations
- define lock ordering and document it
- avoid nested locking unless necessary
- isolate blocking operations from shared pools
- keep fallback paths when shared resources degrade
## Performance Insights
Contention is often a queuing problem. Reduce shared hot spots,
partition state, and cap fan-out before scaling threads.
## Senior-Level Insights
Staff-level interviews expect a prevention strategy: lock hierarchy,
concurrency budgets, and telemetry to detect rising wait times early.
