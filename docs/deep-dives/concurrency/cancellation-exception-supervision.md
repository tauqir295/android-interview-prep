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

## Cancellation, Exceptions, and Supervision Deep Dive

## Overview

Cancellation in coroutines is cooperative, while exception propagation depends on
whether the scope is regular or supervised. This is one of the most common senior
interview topics because it mixes control flow, resilience, and lifecycle behavior.

## Core Concepts

- cancellation is a request, not a hard kill
- suspend points are cancellation-aware
- exceptions may cancel sibling coroutines in regular scopes
- supervision isolates failures when appropriate

## Internal Implementation

When a job is cancelled, coroutines observe that state and stop at suspension
points or when explicitly checking `isActive` / `ensureActive()`.

Exception model highlights:

- `launch` surfaces uncaught exceptions to its parent/root handler
- `async` stores exceptions until awaited
- `CoroutineExceptionHandler` is a root-level safety net, not a general catch-all

## Threading Model

Cancellation is independent of the thread a coroutine runs on.
A coroutine can be cancelled on any dispatcher; the important part is whether the
work cooperates with cancellation.

## Coroutine / Flow Behavior

Flow operators such as `collectLatest` and `flatMapLatest` rely on cancellation
semantics to cancel previous work when newer values arrive.
This is why cancellation knowledge is essential for Flow debugging.

## Code Examples

```kotlin
suspend fun loadData() = coroutineScope {
    val a = async { fetchA() }
    val b = async { fetchB() }
    a.await() + b.await()
}

suspend fun loop() {
    while (currentCoroutineContext().isActive) {
        delay(100)
    }
}
```

## Common Interview Questions

- **Q:** What is cooperative cancellation?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** How does `async` differ from `launch` in error handling?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** When do sibling coroutines get cancelled?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** What does `CoroutineExceptionHandler` actually catch?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
## Production Considerations

- cancel work when UI or requests are no longer relevant
- make sure cleanup runs in `finally` blocks
- do not swallow cancellation exceptions accidentally
- use supervision only where sibling independence is intended

## Performance Insights

Proper cancellation prevents wasted CPU, duplicate network calls,
and long-running work continuing after the user no longer needs it.

## Senior-Level Insights

The strongest senior answers connect cancellation to lifecycle boundaries,
error isolation, and the behavior of Flow operators under changing inputs.
