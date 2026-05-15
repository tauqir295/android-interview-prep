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

## MVVM and ViewModel Deep Dive

## Overview

MVVM remains the most common Android app architecture baseline.
Its strength is separating rendering concerns from orchestration and data access.

## Core Concepts

- UI renders state, not repositories directly
- ViewModel owns screen state and user intent handling
- repositories/use cases provide business data
- lifecycle-aware state exposure prevents UI loss on rotation

## Layer Responsibilities

- View (Activity/Fragment/Compose screen):
  - collect state
  - dispatch user actions
- ViewModel:
  - transform domain outputs into UI models
  - coordinate async work and retries
- Data/domain layer:
  - implement business and source policies

## Data Flow

1. View dispatches action (`onRetry`, `onRefresh`, input change).
2. ViewModel updates loading/intermediate state.
3. ViewModel invokes use case or repository.
4. Result maps to new immutable `UiState`.
5. View observes and re-renders.

## Internal Architecture

Production MVVM often uses:

- `StateFlow<UiState>` for persistent state
- separate event stream for one-time effects
- reducer-style update helpers to keep transitions explicit
- SavedStateHandle for small restorable fields

## Code Examples

```kotlin
data class AccountUiState(
    val isLoading: Boolean = false,
    val account: AccountUi? = null,
    val error: String? = null
)

class AccountViewModel(
    private val loadAccount: LoadAccountUseCase,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {
    private val _uiState = MutableStateFlow(AccountUiState())
    val uiState: StateFlow<AccountUiState> = _uiState
}
```

## Common Interview Questions

- **Q:** Where does business logic end and UI logic begin?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** Should ViewModel call repository directly or via use cases?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do you model transient events in MVVM?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** What usually makes a ViewModel "too fat"?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
## Production Considerations

- keep ViewModel APIs small and explicit
- avoid Android framework objects in domain contracts
- standardize result/error mapping to reduce inconsistency
- audit long-running jobs for lifecycle leaks

## Scalability Tradeoffs

- Pros:
  - low ceremony and strong team familiarity
  - easy incremental adoption
- Cons:
  - ViewModel bloat risk without architecture guardrails
  - inconsistent event/state modeling across teams

## Senior-Level Insights

Senior-level answers should describe how MVVM evolved in real codebases:
what was pushed into use cases, what remained in ViewModel,
and how teams enforced consistency at scale.
