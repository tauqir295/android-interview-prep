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

## Clean Architecture Layering Deep Dive

## Overview

Clean Architecture organizes code by policy boundaries and dependency direction.
The goal is long-term maintainability, not maximum layer count.

## Core Concepts

- inward dependency rule (outer depends on inner)
- framework-independent business policy
- stable interfaces at layer boundaries
- explicit mapping between transport/domain/UI models

## Layer Responsibilities

- Presentation:
  - state rendering and user interaction handling
- Domain:
  - business rules and use-case orchestration
- Data:
  - infrastructure details (network, db, files, caches)

## Data Flow

1. UI intent reaches ViewModel.
2. ViewModel triggers use case.
3. Use case calls domain repository interface.
4. Data implementation executes integration work.
5. Domain result returns and maps to `UiState`.

## Internal Architecture

Keep domain contracts stable and place implementation churn in data modules.

Typical package/module split:

- `presentation` (screen state + mappers)
- `domain` (use cases + contracts)
- `data` (adapters + source orchestration)

## Code Examples

```kotlin
interface ProductRepository {
    suspend fun getProduct(id: String): Product
}

class GetProductUseCase(
    private val repository: ProductRepository
) {
    suspend operator fun invoke(id: String): Product = repository.getProduct(id)
}
```

## Common Interview Questions

- **Q:** Does every app need all three layers?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** Where should model mapping live?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do you avoid over-abstraction?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How does this impact build speed?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
## Production Considerations

- introduce layers where complexity justifies them
- keep boundary ownership explicit
- codify dependency rules with lint/CI checks
- track refactor friction as architecture health signal

## Scalability Tradeoffs

- Pros:
  - clear boundaries and safer refactors
  - strong testing isolation
- Cons:
  - more indirection and code overhead
  - potential boilerplate in simple features

## Senior-Level Insights

Strong candidates discuss pragmatic architecture:
where strict layering was relaxed, what risks that introduced,
and which guardrails kept the codebase healthy.
