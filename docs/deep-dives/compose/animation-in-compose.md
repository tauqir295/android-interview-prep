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
## Animation in Compose Deep Dive

## Overview

Compose animation APIs range from simple value transitions to coordinated multi-state
motion systems.

## Core Concepts

- `animate*AsState` for simple property animation
- `AnimatedVisibility` / `AnimatedContent` for content transitions
- `Transition` APIs for coordinated animations

## Runtime Internals

Animation state updates over frames, driving recomposition and draw invalidation
for animated properties.

## Composition / Recomposition Flow

- target state changes
- animation engine interpolates values per frame
- consumers recompose/draw with new frame values

## State Management

Model animation trigger state explicitly and avoid coupling animation state tightly
with business domain state.

## Code Examples

```kotlin
val alpha by animateFloatAsState(targetValue = if (expanded) 1f else 0f, label = "alpha")
Text("Details", modifier = Modifier.alpha(alpha))
```

## Common Interview Questions

- **Q:** Which API to choose for simple vs complex transitions?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
- **Q:** How do you reduce jank in animation-heavy screens?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
## Production Considerations

- cap concurrent animations in dense lists
- align motion spec with design system
- test reduced-motion and accessibility cases

## Performance Insights

Animation smoothness depends on stable frame budget; expensive recomposition or
layout work during animation is a common jank source.

## Senior-Level Insights

Senior candidates discuss animation as system design: API choice, consistency,
performance budgeting, and UX intent.
