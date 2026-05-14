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

## MVI and UDF Deep Dive

## Overview

MVI and UDF emphasize explicit state transitions and predictable data flow.
They are especially useful for complex screens where event ordering and side effects
must stay debuggable.

## Core Concepts

- immutable UI state as render input
- intent/action as user or system event
- reducer as pure state-transition function
- effect channel for one-time side effects

UDF is the principle; MVI is a concrete implementation style.

## Layer Responsibilities

- UI layer:
  - renders `UiState`
  - emits intents/actions
- ViewModel/store:
  - reduces intents into new state
  - coordinates side effects through use cases
- Domain/data layers:
  - execute business and integration work
  - map results/errors to reducer inputs

## Data Flow

1. User action emits an intent.
2. Intent enters reducer/store pipeline.
3. Reducer computes new `UiState`.
4. UI re-renders from state.
5. One-time effects are emitted separately (navigation/snackbar/logging).

## Internal Architecture

A practical Android setup often keeps a single state store per screen.

Key internal design choices:

- single reducer vs split reducers by feature section
- serialized intent processing for determinism
- explicit effect middleware/interactor boundaries
- state persistence strategy for process recreation

## Code Examples

```kotlin
data class ProfileUiState(
    val isLoading: Boolean = false,
    val user: UserUi? = null,
    val error: String? = null
)

sealed interface ProfileIntent {
    data object Load : ProfileIntent
    data object Retry : ProfileIntent
}

private fun reduce(state: ProfileUiState, intent: ProfileIntent): ProfileUiState {
    return when (intent) {
        ProfileIntent.Load,
        ProfileIntent.Retry -> state.copy(isLoading = true, error = null)
    }
}
```

## Common Interview Questions

- MVI vs MVVM: when is MVI worth the overhead?
- How do you model one-time events without replay bugs?
- Should reducers be pure functions?
- How do you prevent state explosion on large screens?

## Production Considerations

- keep intent vocabulary small and domain-oriented
- avoid giant monolithic reducers by composing feature state slices
- enforce state/effect separation in code reviews
- log intent -> state transitions for incident debugging

## Scalability Tradeoffs

- Pros:
  - deterministic behavior and easier debugging
  - better reasoning about concurrency/order
- Cons:
  - extra ceremony and boilerplate
  - larger state models can become hard to maintain

## Senior-Level Insights

Senior candidates should discuss where MVI is selectively applied.
Strong teams often combine MVVM structure with UDF discipline,
rather than forcing strict MVI everywhere.
