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
## Derived State and rememberUpdatedState Deep Dive

## Overview

These APIs solve two different problems: efficient derived calculations and
safe access to latest values inside long-lived effects.

## Core Concepts

- `derivedStateOf`: memoize computed state by dependencies
- `rememberUpdatedState`: update captured reference without restarting effect

## Runtime Internals

`derivedStateOf` participates in snapshot observation. Recalculation happens only
when dependencies change; downstream readers observe the derived state.

## Composition / Recomposition Flow

- source state changes
- derived value invalidates if dependency changed
- consumers recompose with updated computed value

## State Management

Use derived state for expensive projections, not for trivial string concatenation.
Use updated-state for callback freshness in timers/listeners.

## Code Examples

```kotlin
@Composable
fun TimedAction(onTimeout: () -> Unit) {
    val latestOnTimeout by rememberUpdatedState(onTimeout)
    LaunchedEffect(Unit) {
        delay(3_000)
        latestOnTimeout()
    }
}
```

## Common Interview Questions

- **Q:** Why not key `LaunchedEffect` with callback directly?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
- **Q:** Does `derivedStateOf` always improve performance?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
## Production Considerations

- avoid premature optimization
- verify with profiling when derived state adds value
- document intent when using updated-state to avoid confusion

## Performance Insights

`derivedStateOf` can reduce unnecessary invalidations in hot UI paths such as
scroll and search filtering.

## Senior-Level Insights

Strong answers include tradeoffs: both APIs add complexity, so they should be
used where correctness or measurable performance benefit exists.
