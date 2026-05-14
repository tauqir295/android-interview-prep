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
# Cancellation and Exception Handling Deep Dive

## Overview

Cancellation and exception propagation are where coroutine understanding becomes production-relevant.

---

## Core Concepts

### Cancellation

Coroutine cancellation is cooperative.
It works well when code reaches suspension points or checks cancellation explicitly.

### Exceptions

Exception behavior depends on:

- coroutine builder (`launch` vs `async`)
- parent-child hierarchy
- supervisor boundaries
- where exceptions are observed

---

## Internal Implementation

Cancellation is represented by job state changes and propagated through job hierarchy.

A coroutine that never suspends or checks cancellation may continue running longer than expected.

---

## JVM / Compiler Behavior

Suspend functions cooperate with cancellation through coroutine machinery, not through thread interruption alone.

`CoroutineExceptionHandler` is only for uncaught exceptions; it is not a general substitute for structured error handling.

---

## Code Examples

```kotlin
while (isActive) {
    doWorkChunk()
}
```

```kotlin
try {
    doWork()
} catch (e: CancellationException) {
    throw e
}
```

---

## Common Interview Questions

- Why is cancellation called cooperative?
- Why should `CancellationException` usually be rethrown?
- Why doesn't `CoroutineExceptionHandler` catch everything?

---

## Production Considerations

Common bugs:

- swallowing cancellation accidentally
- blocking threads inside coroutines
- assuming `try/catch` and handler behavior are identical across builders

---

## Performance Insights

Cancellation responsiveness matters for UI, battery, and resource cleanup. Poor cancellation behavior can waste work and degrade UX.

---

## Senior-Level Insights

Good coroutine engineers think about cancellation and exception strategy during API design, not only when debugging failures.

