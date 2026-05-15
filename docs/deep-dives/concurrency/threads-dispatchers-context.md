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

## Threads, Dispatchers, and Context Switching Deep Dive

## Overview

Threads are execution resources; dispatchers are scheduling policies for coroutines.
The core Android interview point is that coroutine code still runs on threads,
but coroutines let you share those threads more efficiently.

## Core Concepts

- threads are OS-level execution units
- dispatchers choose where coroutine code runs
- `withContext` switches execution for a scoped block
- main-safety means callers do not need to manage thread hops themselves

## Internal Implementation

Dispatcher implementations usually sit on top of shared executors or thread pools.
Their job is to decide where to resume coroutines after suspension.

Key ideas:

- `Dispatchers.Main` targets UI work
- `Dispatchers.IO` is tuned for blocking I/O
- `Dispatchers.Default` is tuned for CPU work
- `withContext` captures and restores the coroutine context around a block

## Threading Model

The practical Android model is:

- UI interactions stay on main
- blocking file/db/network work moves off main
- CPU-heavy transforms move to Default or a bounded pool
- avoid pretending coroutine code is magically threadless

## Coroutine / Flow Behavior

Flow collectors often inherit the current context unless operators or collectors
explicitly switch dispatchers.
That means dispatcher selection directly affects collection latency, cancellation,
and UI responsiveness.

## Code Examples

```kotlin
suspend fun loadProfile(id: String): Profile = withContext(Dispatchers.IO) {
    api.getProfile(id)
}

viewModelScope.launch(Dispatchers.Main) {
    val profile = loadProfile("42")
    _uiState.value = profile.toUiState()
}
```

## Common Interview Questions

- **Q:** What should run on Main vs IO vs Default?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** Is `Dispatchers.IO` just a background thread pool?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** What does `withContext` guarantee?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** When does dispatcher switching become an anti-pattern?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
## Production Considerations

- keep main-thread blocks short and explicit
- avoid dispatcher hopping in tight loops
- centralize dispatcher injection for testability
- watch for hidden blocking calls in libraries

## Performance Insights

Too many context switches can add overhead, and misusing IO or Default can
cause pool contention. Match the dispatcher to the actual work type and keep
crossing boundaries intentional.

## Senior-Level Insights

Strong senior answers explain the difference between thread ownership,
dispatcher policy, and coroutine lifetime. They also discuss how to keep APIs
main-safe without leaking dispatcher choices to callers.
