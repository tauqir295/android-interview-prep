---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/kotlin/">← Back to Kotlin</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/kotlin/${hash}`);
      return;
    }
    const referrer = document.referrer || "";
    if (referrer.includes("/android-interview-prep/generated/")) {
      link.setAttribute("href", referrer);
    }
  } catch (_) {}
})();
</script>

# Flow Fundamentals Deep Dive

## Overview

Flow is Kotlin's coroutine-based asynchronous stream API and a core part of modern Android data pipelines.

---

## Core Concepts

Key properties of `Flow`:

- cold by default
- sequential by default
- cancellation-aware
- coroutine based

A cold stream starts producing values for each collector independently.

---

## Internal Implementation

A flow builder defines a suspendable emission pipeline.
Collection triggers execution.

That means a `Flow` is closer to a reusable recipe for producing values than a constantly running producer.

---

## JVM / Compiler Behavior

Flow sits on top of coroutines and suspend machinery.
Many operators are implemented as chains of suspendable transformations.

---

## Code Examples

```kotlin
fun userFlow(): Flow<User> = flow {
    emit(loadUser())
}
```

```kotlin
viewModelScope.launch {
    userFlow().collect { user ->
        render(user)
    }
}
```

---

## Common Interview Questions

- What does “cold” mean in Flow?
- How is Flow different from LiveData or Rx streams?
- Why is Flow sequential by default?

---

## Production Considerations

Flow is powerful for:

- repository streams
- UI state pipelines
- database observation
- combining async sources

But careless operator chains and repeated collections can create inefficiency.

---

## Performance Insights

Understand:

- collection triggers execution
- repeated collectors repeat cold work
- buffering/concurrency operators affect throughput and ordering

---

## Senior-Level Insights

The strongest answers explain Flow not just as “reactive streams,” but as coroutine-native cold stream pipelines with explicit lifecycle and collection semantics.

