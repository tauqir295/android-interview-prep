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
# Layout, Measure, and Draw Pipeline Deep Dive

## Overview

Compose rendering uses measure, layout, and draw phases with clear responsibilities.
Understanding phase cost is key for UI performance interviews.

## Core Concepts

- constraints flow downward
- sizes flow upward
- placement happens in layout block
- draw happens after geometry is finalized

## Runtime Internals

`LayoutNode` and measure policies coordinate child measurement and placement,
then draw modifiers and content execute in draw phase.

## Composition / Recomposition Flow

- composition emits layout tree
- measure computes bounds
- layout places children
- draw renders visuals

## State Management

Structure state so frequent changes only affect necessary phases where possible.

## Code Examples

```kotlin
@Composable
fun TwoPane(modifier: Modifier = Modifier, left: @Composable () -> Unit, right: @Composable () -> Unit) {
    Layout(content = { left(); right() }, modifier = modifier) { measurables, constraints ->
        val half = constraints.maxWidth / 2
        val leftPlaceable = measurables[0].measure(constraints.copy(maxWidth = half))
        val rightPlaceable = measurables[1].measure(constraints.copy(maxWidth = half))

        layout(constraints.maxWidth, maxOf(leftPlaceable.height, rightPlaceable.height)) {
            leftPlaceable.placeRelative(0, 0)
            rightPlaceable.placeRelative(half, 0)
        }
    }
}
```

## Common Interview Questions

- What is intrinsic measurement and when is it costly?
- Why can nested unconstrained layouts cause performance issues?

## Production Considerations

- avoid repeated expensive measurement logic
- validate custom layouts on low-end devices

## Performance Insights

Phase-aware optimizations outperform generic "optimize recomposition" advice.

## Senior-Level Insights

Senior-level candidates reason about constraints and phase invalidations when
debugging layout jank.
