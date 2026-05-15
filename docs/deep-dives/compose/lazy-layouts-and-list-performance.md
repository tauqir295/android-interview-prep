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
## Lazy Layouts and List Performance Deep Dive

## Overview

`LazyColumn`/`LazyRow` optimize large collections by composing only needed items,
but identity and item-content design determine real performance.

## Core Concepts

- lazy item composition
- stable keys for identity
- item-level state ownership
- list scroll and prefetch behavior

## Runtime Internals

Lazy layouts maintain item providers and viewport-driven composition windows.
Wrong keys can break slot reuse and state placement.

## Composition / Recomposition Flow

- viewport changes trigger item composition/disposal
- changed item state invalidates affected rows
- stable keys preserve item identity through moves

## State Management

Keep per-item transient state inside keyed item scope; keep business state in ViewModel.

## Code Examples

```kotlin
LazyColumn {
    items(messages, key = { it.id }) { message ->
        MessageRow(message = message)
    }
}
```

## Common Interview Questions

- **Q:** Why do items "jump" without keys?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
- **Q:** How do you reduce jank on long feeds?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
## Production Considerations

- avoid expensive work inside item lambdas
- use paging/windowing for very large data sets
- profile with realistic datasets and devices

## Performance Insights

List performance regressions often come from unstable models, heavy item composition,
and missing keys rather than lazy container itself.

## Senior-Level Insights

Strong answers combine architecture (state granularity) with runtime mechanics
(identity, reuse, and viewport-driven composition).
