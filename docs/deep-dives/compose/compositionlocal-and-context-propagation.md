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
# CompositionLocal and Context Propagation Deep Dive

## Overview

`CompositionLocal` provides implicit dependency propagation through the compose tree.
It is powerful for environment-like values and risky for hidden business dependencies.

## Core Concepts

- providers set values for subtree
- consumers read local values without explicit params
- great for theme/system ambient data

## Runtime Internals

Reads of locals are tracked like other composition inputs. Provider changes invalidate
consumers in affected subtree.

## Composition / Recomposition Flow

- local provided at parent
- descendants read local
- provider value changes
- dependent descendants recompose

## State Management

Use locals for cross-cutting environment values, not for feature business state ownership.

## Code Examples

```kotlin
val LocalSpacing = compositionLocalOf { 8.dp }

@Composable
fun AppTheme(content: @Composable () -> Unit) {
    CompositionLocalProvider(LocalSpacing provides 12.dp) {
        content()
    }
}
```

## Common Interview Questions

- When should you avoid `CompositionLocal`?
- How does it differ from dependency injection?

## Production Considerations

- document every custom local clearly
- keep number of custom locals manageable
- provide test replacements for deterministic UI tests

## Performance Insights

Broad provider updates can invalidate large subtrees; scope providers as tightly
as practical.

## Senior-Level Insights

Senior-level guidance: use `CompositionLocal` as environment plumbing, not as an
escape hatch for architectural shortcuts.
