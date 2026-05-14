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

## Flow Fundamentals Deep Dive

## Overview

Flow is Kotlin's asynchronous stream API. It provides a way to model values over
time while preserving coroutine cancellation and structured behavior.

## Core Concepts

- flows are cold by default
- collection triggers execution
- operators transform values declaratively
- cancellation is integrated into the stream lifecycle

## Internal Implementation

A Flow builder describes a pipeline more than a running producer.
When collected, the upstream logic begins executing in the collector's coroutine
context.

Important internals:

- each collector gets its own cold execution unless sharing is added
- suspension is used instead of blocking where possible
- flow builders and operators compose into coroutine state machines

## Threading Model

Flow does not define threads by itself. The collector context and dispatcher
choice determine where the pipeline runs.
You still need to choose the right dispatcher for blocking or CPU-bound work.

## Coroutine / Flow Behavior

Cold vs hot is the key interview distinction:

- cold flows start with collection
- hot flows emit independently of collectors
- buffering/backpressure decisions affect user-visible behavior

## Code Examples

```kotlin
fun userFlow(): Flow<User> = flow {
    emit(loadUser())
}

viewModelScope.launch {
    userFlow().collect { user ->
        render(user)
    }
}
```

## Common Interview Questions

- What makes Flow different from Rx streams?
- Why is Flow cold by default?
- When does a collector start executing the upstream pipeline?
- How does cancellation affect collection?

## Production Considerations

- keep expensive upstream work shared when multiple collectors exist
- prefer lifecycle-aware collection in Android UI
- choose operators deliberately to avoid accidental work amplification
- avoid blocking inside flow builders

## Performance Insights

Flow is powerful but not free. Operator chains, context switching, and duplicate
collection can all create overhead if the pipeline is poorly designed.

## Senior-Level Insights

Senior answers should explain that Flow is both a data model and an execution
model: it is declared like a pipeline but runs within coroutines and dispatchers.
