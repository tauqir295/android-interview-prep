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

## Launch, Async, and Parallelism Deep Dive

## Overview

`launch` and `async` are the most used coroutine builders, but misuse creates
silent failures, unnecessary parallelism, or result-handling bugs.

## Core Concepts

- `launch` for fire-and-forget side effects
- `async` for concurrent result production (`Deferred`)
- lazy async defers start until needed
- bounded parallelism protects downstream systems

## Internal Implementation

`launch` propagates uncaught exceptions immediately to parent/root.
`async` captures exceptions and rethrows on `await()`, which changes failure timing.

Lazy deferred jobs are created but not started until `start()`/`await()`.

## Threading Model

Builders do not define threads on their own; dispatcher and context do.
Parallelism should be explicit and bounded to avoid pool saturation.

## Coroutine / Flow Behavior

Builder choices often appear inside Flow pipelines and repository orchestration.
Unbounded parallel `async` usage can amplify pressure on APIs/DB and hurt tail latency.

## Code Examples

```kotlin
suspend fun loadDashboard(): Dashboard = coroutineScope {
    val user = async { api.loadUser() }
    val feed = async { api.loadFeed() }
    Dashboard(user.await(), feed.await())
}

suspend fun loadConditionally(flag: Boolean): String = coroutineScope {
    val deferred = async(start = CoroutineStart.LAZY) { api.loadHeavy() }
    if (flag) deferred.await() else "skipped"
}
```

## Common Interview Questions

- **Q:** When is `launch` preferable to `async`?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** Why can forgotten `await()` hide failures?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** Is lazy async good by default?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** How do you cap parallel requests safely?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
## Production Considerations

- always consume `Deferred` results intentionally
- cap fan-out with semaphore/limited parallelism
- prefer simple sequential flow unless parallelism is justified
- measure backend impact before increasing concurrency

## Performance Insights

Parallelism helps throughput only until contention dominates.
Beyond that, queueing and context-switch overhead reduce efficiency.

## Senior-Level Insights

Senior engineers should explain concurrency budgets: how many tasks can run
in parallel per feature, and how those limits are enforced and observed.
