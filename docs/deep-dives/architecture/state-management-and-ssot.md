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

## State Management and SSOT Deep Dive

## Overview

State management is an ownership problem first, and a UI rendering problem second.
Single Source of Truth (SSOT) prevents divergence between competing state copies.

## Core Concepts

- one canonical state owner per concern
- immutable UI state models for deterministic rendering
- explicit event pathways for mutations
- derived/read-only projections for consumers

## Layer Responsibilities

- Presentation:
  - render `UiState`
  - emit intents/events only
- Domain/ViewModel:
  - process intents into state transitions
  - orchestrate use-case calls
- Data/repository:
  - maintain canonical persisted state
  - apply sync/cache policies

## Data Flow

1. User emits event (refresh/filter/retry).
2. ViewModel processes and invokes use case.
3. Use case/repository updates authoritative state.
4. State stream emits new model.
5. UI re-renders from latest immutable state.

## Internal Architecture

SSOT is usually implemented with local persistence as canonical read path,
then upstream refresh updates that store.

Key internal patterns:

- state reducers for predictable transitions
- state vs event channel separation
- idempotent write handling where possible

## Code Examples

```kotlin
data class FeedUiState(
    val isLoading: Boolean = false,
    val items: List<FeedItem> = emptyList(),
    val errorMessage: String? = null
)

class FeedViewModel(
    private val observeFeed: ObserveFeedUseCase,
    private val refreshFeed: RefreshFeedUseCase
) : ViewModel() {
    private val _uiState = MutableStateFlow(FeedUiState())
    val uiState: StateFlow<FeedUiState> = _uiState
}
```

## Common Interview Questions

- Why separate one-time events from persistent state?
- Where should SSOT live: ViewModel or repository?
- How do you prevent stale state races?
- Is immutable state always required?

## Production Considerations

- avoid hidden mutable singletons as state owners
- define clear state transition rules per feature
- include correlation IDs/log context for state-related failures
- test high-frequency event paths and cancellation behavior

## Scalability Tradeoffs

- Pros:
  - easier debugging and replay reasoning
  - lower inconsistency risk across features
- Cons:
  - more explicit modeling and boilerplate
  - strict patterns can feel heavy for trivial screens

## Senior-Level Insights

Senior-level discussions should include failure modes:
state divergence, duplicate write paths, and event replay bugs.
Mature teams treat state contracts as product-critical APIs.
