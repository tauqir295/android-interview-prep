---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/compose/">← Back to Compose</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/compose/${hash}`);
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
## Effects, Coroutines, and Lifecycle Deep Dive

## Overview

`LaunchedEffect`, `DisposableEffect`, and `rememberCoroutineScope` connect coroutines
and callback-style resources to composition lifecycle.

## Core Concepts

- `LaunchedEffect`: composition-scoped coroutine
- `DisposableEffect`: setup + guaranteed cleanup
- `rememberCoroutineScope`: manual event-driven launches

## Runtime Internals

Effect jobs are attached to composition scope. Key changes trigger cancellation
and restart for keyed effects.

## Composition / Recomposition Flow

- enter composition -> start keyed effect
- key change -> cancel old job, launch new one
- leave composition -> cancel/dispose deterministically

## State Management

Use `rememberUpdatedState` when effect must keep running but consume latest callback.

## Code Examples

```kotlin
@Composable
fun LocationObserver(onLocation: (Location) -> Unit) {
    DisposableEffect(Unit) {
        val listener = startLocationUpdates(onLocation)
        onDispose { listener.stop() }
    }
}
```

## Common Interview Questions

- `LaunchedEffect(Unit)` vs `rememberCoroutineScope`?
- How do you avoid stale lambda capture?
- When is cleanup guaranteed?

## Production Considerations

- avoid unstable keys for long-lived jobs
- keep cleanup paths explicit
- use lifecycle-aware collection in screen composables

## Performance Insights

Frequent effect restart in scroll-heavy or rapidly changing UIs can become an
invisible source of overhead.

## Senior-Level Insights

Best answers show precise cancellation semantics and justify effect API choices
using lifecycle and correctness constraints.
