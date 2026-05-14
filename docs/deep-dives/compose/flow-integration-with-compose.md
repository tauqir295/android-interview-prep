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
# Flow Integration with Compose Deep Dive

## Overview

Compose commonly consumes `StateFlow` and other Flows from ViewModel layers.
This section focuses on lifecycle-aware collection and snapshot bridging.

## Core Concepts

- collect flow to UI state
- lifecycle-aware collection on Android screens
- separate state streams from one-off event streams

## Runtime Internals

Flow emissions update Compose `State`, which invalidates dependent scopes and
triggers recomposition scheduling.

## Composition / Recomposition Flow

- collector receives emission
- state holder updates
- dependent composables recompose
- unchanged branches may still be skipped

## State Management

Prefer immutable `UiState` and explicit event channels for navigation/snackbar.

## Code Examples

```kotlin
@Composable
fun HomeRoute(viewModel: HomeViewModel) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    HomeScreen(state = state, onRetry = viewModel::retry)
}
```

## Common Interview Questions

- `collectAsState` vs `collectAsStateWithLifecycle`?
- How to model one-time events safely?
- Why use `snapshotFlow`?

## Production Considerations

- avoid collecting high-frequency streams without need
- debounce/filter upstream when possible
- verify cancellation when screen leaves foreground

## Performance Insights

Excess emissions with large UI models can amplify recomposition work. Consider
state granularity and emission strategy.

## Senior-Level Insights

Senior candidates should explain end-to-end data flow from repository emission
to recomposition behavior and lifecycle management.
