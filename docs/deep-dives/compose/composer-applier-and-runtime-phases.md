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
## Composer, Applier, and Runtime Phases Deep Dive

## Overview

`Composer` computes structural updates, while `Applier` executes those updates
on the target UI tree.

## Core Concepts

- composition phase (compute changes)
- layout phase (measure/place)
- draw phase (render)
- applier operations (insert/move/remove/update)

## Runtime Internals

Compiler-generated composable code emits operations through `Composer`.
Applier-specific implementations map operations to concrete UI nodes.

## Composition / Recomposition Flow

- invalidated groups are recomposed
- composer records mutations
- applier commits node operations
- layout/draw run as required by invalidations

## State Management

State changes can trigger different phase costs depending on whether they affect
structure, layout constraints, or only drawing properties.

## Code Examples

```kotlin
@Composable
fun AlphaChip(text: String, enabled: Boolean) {
    Text(
        text = text,
        modifier = Modifier.alpha(if (enabled) 1f else 0.5f)
    )
}
```

## Common Interview Questions

- Is recomposition equivalent to layout + draw every time?
- What responsibilities belong to composer vs applier?

## Production Considerations

- optimize based on phase bottleneck, not assumptions
- profile structure/layout/draw costs separately

## Performance Insights

A change limited to draw properties is usually cheaper than one causing full
layout recalculation.

## Senior-Level Insights

Senior engineers explain phase-specific invalidation and use that model to pick
targeted optimizations.
