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

## Parallelism and Scheduling Deep Dive

## Overview

Parallelism is a capacity control decision, not just a performance trick.
In coroutine systems, limiting parallelism often improves stability and p99 latency.

## Core Concepts

- logical concurrency vs actual parallel execution
- `limitedParallelism` constrains concurrent tasks
- fairness and throughput tradeoffs
- contention-aware scheduling

## Internal Implementation

`limitedParallelism` creates a constrained dispatcher view that throttles active
work while still using the parent dispatcher's infrastructure.

This provides a lightweight control boundary without introducing a new executor.

## Threading Model

Limiting parallelism helps protect scarce resources:

- DB connection pools
- remote APIs with rate limits
- CPU-heavy transforms

It does not eliminate thread contention; it reduces pressure on shared pools.

## Coroutine / Flow Behavior

In Flow-heavy systems, parallel map/merge operations can overwhelm downstream.
Applying bounded concurrency keeps pipelines predictable under load.

## Code Examples

```kotlin
val limited = Dispatchers.Default.limitedParallelism(4)

suspend fun process(items: List<Item>) = coroutineScope {
    items.map { item ->
        async(limited) { transform(item) }
    }.awaitAll()
}
```

## Common Interview Questions

- **Q:** When should you use `limitedParallelism`?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** Is it equivalent to a fixed thread pool?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** How do you pick the limit value?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** What metrics validate the chosen bound?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
## Production Considerations

- start conservative and tune with metrics
- separate limits per bottlenecked dependency
- revisit limits as workload profile changes
- avoid one global limit for unrelated workloads

## Performance Insights

High parallelism can improve average throughput but hurt tail latency.
Bounded scheduling often stabilizes responsiveness and reduces queue collapse.

## Senior-Level Insights

Staff-level discussions should include concurrency budgets and SLO alignment:
parallelism choices should be tied to reliability targets, not guesswork.
