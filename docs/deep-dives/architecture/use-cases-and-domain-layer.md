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

## Use Cases and Domain Layer Deep Dive

## Overview

Use cases encapsulate business actions so policy decisions are not scattered
across ViewModels or repository implementations. A domain layer pays off when
business behavior is complex or reused across features.

## Core Concepts

- use case = coherent business action
- domain entities/value objects express business language
- domain contracts isolate policy from framework details
- composition of use cases supports larger workflows

## Layer Responsibilities

- Presentation:
  - trigger use cases based on UI intent
  - render resulting state
- Domain:
  - hold business rules and orchestration policies
  - remain framework-agnostic
- Data:
  - fulfill domain contracts with integration details

## Data Flow

1. UI emits intent.
2. ViewModel invokes a use case.
3. Use case applies domain rules and calls repository contracts.
4. Repository/data layer executes integration work.
5. Domain result is mapped to UI state.

## Internal Architecture

Use-case design heuristics:

- one clear business outcome per use case
- avoid thin pass-through wrappers unless establishing boundary
- compose related use cases for larger scenarios
- keep input/output models domain-centric and stable

Common smell: "god use case" that mixes orchestration, validation,
and technical error handling without separation.

## Code Examples

```kotlin
class PlaceOrderUseCase(
    private val cartRepository: CartRepository,
    private val paymentRepository: PaymentRepository,
    private val orderRepository: OrderRepository
) {
    suspend operator fun invoke(input: PlaceOrderInput): PlaceOrderResult {
        val cart = cartRepository.getActiveCart(input.userId)
        require(cart.items.isNotEmpty()) { "Cart cannot be empty" }

        val payment = paymentRepository.authorize(input.paymentMethod, cart.total)
        return orderRepository.createOrder(cart, payment)
    }
}
```

## Common Interview Questions

- **Q:** When does a domain layer become over-engineering?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How many use cases per feature is too many?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** Where should validation rules live?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do you test use-case orchestration effectively?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
## Production Considerations

- keep domain API naming aligned with product language
- treat use-case signatures as long-lived contracts
- add focused unit tests for business invariants
- prevent Android framework leakage into domain types

## Scalability Tradeoffs

- Pros:
  - better policy reuse and clearer business boundaries
  - improved testability and refactor safety
- Cons:
  - additional indirection for simple CRUD apps
  - maintenance overhead if boundaries are poorly defined

## Senior-Level Insights

Senior candidates should explain how domain boundaries evolved with product complexity.
Great answers include examples where introducing or removing a domain layer
improved delivery and reliability outcomes.
