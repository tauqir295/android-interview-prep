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
## Side Effects Overview Deep Dive

## Overview

Compose separates pure UI description from imperative work. Side-effect APIs exist
to run imperative logic safely with composition lifecycle awareness.

## Core Concepts

- keep composable bodies side-effect free
- use effect APIs for non-UI work
- choose API by restart/cancellation behavior

## Runtime Internals

Effects are scheduled relative to composition and commit phases. Their lifecycle
is tied to the composable scope and keys.

## Composition / Recomposition Flow

- composable enters composition
- effect starts according to API rules
- key changes can restart effect
- leaving composition cancels/disposes effect

## State Management

Use state as input for effect decisions, but avoid writing loops where effect
updates state that immediately restarts itself.

## Code Examples

```kotlin
@Composable
fun AnalyticsScreen(screenName: String) {
    SideEffect {
        analytics.setCurrentScreen(screenName)
    }
}
```

## Common Interview Questions

- Why not launch coroutines directly in composable body?
- Which effect API runs after commit?
- How do keys impact effect restarts?

## Production Considerations

- keep effects idempotent when possible
- isolate long-running work to proper scopes
- document key choices in sensitive effects

## Performance Insights

Unnecessary restarts can cause extra work and UI jank, especially if effect work
touches I/O or expensive observers.

## Senior-Level Insights

Senior candidates explain effect lifecycle semantics clearly and pick APIs based
on deterministic cleanup and restart guarantees.
