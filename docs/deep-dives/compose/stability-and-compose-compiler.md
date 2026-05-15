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
## Stability and Compose Compiler Deep Dive

## Overview

Stability and compiler transforms drive Compose skippability and recomposition cost.
This is a high-signal senior interview topic.

## Core Concepts

- stable vs unstable parameter types
- `@Stable` and `@Immutable` contracts
- compiler-generated restart/skip groups

## Runtime Internals

Compiler emits change flags and group metadata. Runtime uses these signals with
stability info to decide whether to re-run or skip group bodies.

## Composition / Recomposition Flow

- parent recomposes
- parameter change checks run
- stable unchanged inputs can be skipped
- unstable or changed inputs re-run group

## State Management

Immutable UI models and explicit state transitions generally improve stability.

## Code Examples

```kotlin
@Immutable
data class ProfileUi(
    val id: String,
    val name: String,
    val followers: Int
)
```

## Common Interview Questions

- **Q:** Is `@Stable` always safe to add?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
- **Q:** Why can wrong annotation usage cause stale UI?
  **A:** Describe data policy explicitly: freshness and invalidation rules, canonical local source, deterministic merge logic, and duplicate prevention with stable keys.
- **Q:** How do compiler metrics help optimization?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
## Production Considerations

- treat stability annotations as correctness contracts
- avoid mutable public state in UI models
- benchmark before and after stability changes

## Performance Insights

Higher skippability in hot composables can reduce frame-time variance.

## Senior-Level Insights

Great answers combine architecture and tooling: model design, compiler reports,
and runtime tracing together.
