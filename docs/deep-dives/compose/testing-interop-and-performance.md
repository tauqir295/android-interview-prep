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
# Testing, Interop, and Performance Deep Dive

## Overview

This deep dive combines three high-impact interview themes: testing strategy,
View interop migration, and practical performance diagnostics.

## Core Concepts

- semantics-driven Compose UI testing
- `AndroidView` interoperability boundaries
- performance measurement over guesswork

## Runtime Internals

Compose tests query semantics tree; interop inserts View-backed nodes; performance
issues often emerge from recomposition, layout, or draw hotspots.

## Composition / Recomposition Flow

- state changes update semantics and visual nodes
- tests assert semantics tree output
- interop nodes update via bridge layer

## State Management

Keep deterministic test state inputs and avoid hidden global dependencies in composables.

## Code Examples

```kotlin
composeTestRule
    .onNodeWithTag("retry_button")
    .performClick()
```

```kotlin
AndroidView(factory = { context -> MapView(context) })
```

## Common Interview Questions

- What should UI tests assert in Compose?
- When is `AndroidView` acceptable vs technical debt?
- How do you triage Compose jank in production?

## Production Considerations

- build a test pyramid with fast deterministic layers
- isolate interop to explicit boundaries
- monitor frame time and startup regressions continuously

## Performance Insights

Most wins come from data/state architecture and hot-path simplification, not
micro-optimizing isolated composables.

## Senior-Level Insights

Staff-level answers connect quality strategy, migration risk management, and
observability-backed performance engineering.
