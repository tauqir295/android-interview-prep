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

## Testing Architecture and Testability Deep Dive

## Overview

Testability is an architectural property. Systems with explicit dependencies,
clear boundaries, and deterministic state transitions are easier to verify and evolve.

## Core Concepts

- dependency injection for replaceable collaborators
- contract-driven boundaries between modules/layers
- deterministic state reducers and use-case behavior
- test pyramid with fast lower-level coverage

## Layer Responsibilities

- Unit tests:
  - verify use cases, reducers, mappers
- Integration tests:
  - verify repository/source orchestration
- UI tests:
  - verify critical user journeys and rendering contracts

## Data Flow

1. Provide fake or test-double dependencies.
2. Trigger intent/use-case action.
3. Observe state/output transitions.
4. Assert deterministic expected behavior.
5. Validate boundary contracts in integration scenarios.

## Internal Architecture

Key architecture decisions for testability:

- constructor injection everywhere possible
- pure mapping/reducer functions
- abstraction boundaries at network/db/platform edges
- explicit time/thread control in async pipelines

## Code Examples

```kotlin
class LoginViewModelTest {
    private val repository = FakeAuthRepository()
    private val viewModel = LoginViewModel(LoginUseCase(repository))

    @Test
    fun emitsErrorStateWhenCredentialsInvalid() = runTest {
        viewModel.onSubmit("bad", "creds")
        assertTrue(viewModel.uiState.value is LoginUiState.Error)
    }
}
```

## Common Interview Questions

- **Q:** What should be unit vs integration tested?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do you test one-time events?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do you keep UI tests stable and valuable?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do contract tests help modular teams?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
## Production Considerations

- prioritize deterministic fast tests in CI gates
- track flaky-test rate as architecture health metric
- use fixture/data builders to reduce test duplication
- enforce test ownership at module boundaries

## Scalability Tradeoffs

- Pros:
  - safer refactors and faster incident recovery
  - clearer confidence signals for releases
- Cons:
  - upfront effort for harnesses/fakes
  - maintenance cost for poor test design

## Senior-Level Insights

Senior-level answers should include test strategy evolution.
The goal is not 100% coverage, but high signal coverage aligned with
risky paths and architectural boundaries.
