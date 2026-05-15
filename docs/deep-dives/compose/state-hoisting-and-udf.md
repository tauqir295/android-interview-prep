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
## State Hoisting and UDF Deep Dive

## Overview

State hoisting and unidirectional data flow (UDF) are core to scalable Compose architecture.
They separate rendering from ownership and make behavior predictable under recomposition.

## Core Concepts

- state owner provides immutable UI state
- UI emits events upward via callbacks
- reducer/use-case updates state
- new state flows back down for rendering

This keeps updates explicit and avoids hidden mutable dependencies.

## Runtime Internals

Compose itself does not enforce business architecture, but runtime rewards clear boundaries:

- fewer mutable entry points reduce accidental invalidation
- stable, immutable screen models improve skippability
- stateless child composables create reusable composition groups

## Composition / Recomposition Flow

1. ViewModel emits `UiState`.
2. Screen composable reads state and renders branches.
3. User interaction invokes event callback.
4. State owner processes event and emits updated state.
5. Compose recomposes affected UI scopes.

## State Management

Recommended layering:

- domain/data state in repositories/use cases
- screen state in ViewModel
- local ephemeral interaction state in composables
- one-off events modeled separately (navigation/snackbar)

## Code Examples

```kotlin
data class FeedUiState(
    val isLoading: Boolean = false,
    val items: List<PostUi> = emptyList(),
    val error: String? = null
)

@Composable
fun FeedScreen(
    state: FeedUiState,
    onRetry: () -> Unit,
    onPostClick: (String) -> Unit
) {
    when {
        state.isLoading -> CircularProgressIndicator()
        state.error != null -> ErrorView(state.error, onRetry)
        else -> PostList(posts = state.items, onPostClick = onPostClick)
    }
}
```

## Common Interview Questions

- **Q:** Why hoist state if local state works?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
- **Q:** How do you model loading/content/error without flag explosion?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
- **Q:** Where should navigation events live?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
- **Q:** How do you prevent one-time event replay bugs?
  **A:** Answer from runtime mechanics: state ownership, recomposition triggers, effect lifecycle, and frame-time impact measured with tooling.
## Production Considerations

- Use immutable state data classes.
- Prefer intent/event sealed models for complex screens.
- Keep composables presentation-focused.
- Validate architecture with UI + ViewModel tests.

## Performance Insights

- Large monolithic `UiState` objects can trigger broad recomposition.
- Split screen sections and pass only required slices.
- Stable collections and item identities improve list performance.

## Senior-Level Insights

Senior answers should show architecture-performance linkage:

- UDF improves reasoning and debuggability
- state granularity affects recomposition cost
- explicit event contracts make large-team development safer

