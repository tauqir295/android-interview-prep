---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/architecture/">← Back to Architecture</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/architecture/${hash}`);
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

## Reactive Architecture with Flows Deep Dive

## Overview

Reactive architecture models data and UI as streams over time. In Android,
`StateFlow` and `Flow` pipelines enable lifecycle-aware rendering and clearer
state propagation across layers.

## Core Concepts

- persistent UI state stream (`StateFlow`)
- one-off event stream (`SharedFlow`/Channel)
- upstream operators for mapping/filtering/debouncing
- structured concurrency and cancellation-aware collection

## Layer Responsibilities

- Presentation:
  - collect state streams and render
  - collect event streams for transient effects
- ViewModel/domain:
  - merge intents and data streams
  - expose immutable state and explicit events
- Data:
  - expose source streams (DB/network sync updates)

## Data Flow

1. Source streams emit changes (DB/network/user intent).
2. ViewModel combines/transforms streams.
3. New `UiState` emits via `StateFlow`.
4. UI collects with lifecycle awareness.
5. Transient actions emit via dedicated event stream.

## Internal Architecture

Design choices that matter:

- where to combine streams (domain vs ViewModel)
- replay/buffer configuration for event channels
- backpressure and sampling strategy on high-frequency streams
- cancellation boundaries tied to lifecycle scope

Pitfall to avoid: representing one-time navigation/snackbar as persistent state flags.

## Code Examples

```kotlin
class SearchViewModel(
    observeQuery: Flow<String>,
    private val repository: SearchRepository
) : ViewModel() {

    val uiState: StateFlow<SearchUiState> = observeQuery
        .debounce(300)
        .distinctUntilChanged()
        .flatMapLatest { query -> repository.search(query) }
        .map { results -> SearchUiState(results = results) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), SearchUiState())
}
```

## Common Interview Questions

- **Q:** `StateFlow` vs `SharedFlow` for UI architecture?
  **A:** Start from delivery semantics: use StateFlow for durable state, SharedFlow or Channel for transient events, and lifecycle-aware collection to prevent duplicate work.
- **Q:** Where should operators live: UI, ViewModel, or domain?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do you prevent duplicate collectors and wasted work?
  **A:** Start from delivery semantics: use StateFlow for durable state, SharedFlow or Channel for transient events, and lifecycle-aware collection to prevent duplicate work.
- **Q:** How do you model retries in stream pipelines?
  **A:** Use a delivery pipeline narrative: separate pre-submit and post-submit checks, gate promotion on quality signals, roll out gradually, and keep an immediate halt path.
## Production Considerations

- set explicit sharing policies (`WhileSubscribed`, timeout)
- instrument stream latency and emission volume
- centralize error mapping for consistent UX behavior
- guard expensive upstream work with memoization/cache strategies

## Scalability Tradeoffs

- Pros:
  - composable data pipelines and clear async modeling
  - strong lifecycle/cancellation semantics
- Cons:
  - operator chains can become hard to reason about
  - debugging complex stream interactions requires discipline

## Senior-Level Insights

Senior engineers should discuss stream contract governance:
what constitutes state vs event, where transformations belong,
and how to keep reactive pipelines understandable across teams.
