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

## Scheduler and Thread Pools Deep Dive

## Overview

Coroutine scheduling ultimately depends on thread pools.
Understanding queueing and starvation is essential for production troubleshooting.

## Core Concepts

- dispatchers route work onto pools/executors
- pool saturation increases queueing latency
- starvation occurs when tasks cannot obtain execution time
- blocking calls can consume all available workers

## Internal Implementation

Dispatchers maintain task queues and worker handoff logic.
Fairness is best-effort; pathological workloads can monopolize workers.

Typical starvation triggers:

- long blocking calls on shared dispatcher
- unbounded fan-out launching thousands of jobs
- CPU-heavy loops without yielding/cooperative checks

## Threading Model

Main thread has strict responsiveness requirements.
Background pools balance throughput and latency under contention.
Treat thread pools as finite resources, not infinite capacity.

## Coroutine / Flow Behavior

Flow pipelines can overload pools when expensive operators run in parallel or
multiple collectors duplicate heavy upstream work.
Sharing and throttling are often more effective than adding more workers.

## Code Examples

```kotlin
val ioLimited = Dispatchers.IO.limitedParallelism(16)

suspend fun loadBatch(ids: List<String>) = coroutineScope {
    ids.map { id ->
        async(ioLimited) { repository.fetch(id) }
    }.awaitAll()
}
```

## Common Interview Questions

- What causes thread starvation in coroutine apps?
- Why can IO dispatcher still saturate?
- How do you identify scheduler bottlenecks?
- Should you create custom pools for every feature?

## Production Considerations

- monitor queue depth and task latency
- isolate particularly expensive workloads
- avoid blocking shared pools when possible
- prefer bounded concurrency to brute-force parallelism

## Performance Insights

Throughput tuning must consider tail latency and fairness.
A slightly lower parallelism cap can improve p95/p99 by reducing contention.

## Senior-Level Insights

Senior answers should include observability strategy: what signals indicate
starvation, and what mitigation playbooks teams follow during incidents.
