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
  } catch (_) {
    // Keep default generated page link if URL parsing fails.
  }
})();
</script>
## StateFlow, SharedFlow, and Channels Deep Dive

## Overview

These primitives solve different streaming and coordination problems in coroutine-based systems.

---

## Core Concepts

### StateFlow

- always has a current value
- best for state exposure
- good for UI state models

### SharedFlow

- hot broadcast stream
- configurable replay/buffering
- good for events/shared emissions

### Channel

- point-to-point communication primitive
- queue-like semantics
- send/receive model

### Mutex

- protects shared mutable state cooperatively
- suspends instead of blocking threads

---

## Internal Implementation

These primitives differ in ownership and delivery semantics:

- state retention (`StateFlow`)
- broadcast fan-out (`SharedFlow`)
- queue handoff (`Channel`)
- mutual exclusion (`Mutex`)

Interviewers often care more about correct use-case matching than API memorization.

---

## JVM / Compiler Behavior

All of them are coroutine/runtime constructs, not magical language features. Their behavior emerges from concurrency contracts and buffering rules.

---

## Code Examples

```kotlin
private val _state = MutableStateFlow(UiState())
val state: StateFlow<UiState> = _state
```

```kotlin
private val events = MutableSharedFlow<String>()
```

```kotlin
val mutex = Mutex()
mutex.withLock {
    updateSharedState()
}
```

---

## Common Interview Questions

- **Q:** StateFlow vs SharedFlow?
  **A:** Start from delivery semantics: use StateFlow for durable state, SharedFlow or Channel for transient events, and lifecycle-aware collection to prevent duplicate work.
- **Q:** Channel vs SharedFlow?
  **A:** Start from delivery semantics: use StateFlow for durable state, SharedFlow or Channel for transient events, and lifecycle-aware collection to prevent duplicate work.
- **Q:** When use `Mutex` instead of synchronized locking?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.

---
## Production Considerations

Common mistakes:

- using `StateFlow` for one-off UI events
- using channels where broadcast behavior is needed
- ignoring replay/buffer semantics
- mutating shared state without synchronization

---

## Performance Insights

Hot stream choice affects:

- memory retention
- buffering pressure
- event loss or duplication
- collector coordination cost

---

## Senior-Level Insights

Strong engineers choose these primitives based on delivery semantics and lifecycle guarantees, not habit.

