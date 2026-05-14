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

## Modularization Strategies Deep Dive

## Overview

Modularization improves build performance and ownership clarity when boundaries
reflect business capabilities and dependency direction rules.

## Core Concepts

- split by feature ownership and change cadence
- keep API surface explicit and minimal
- avoid cyclic dependencies between modules
- enforce contracts through architecture checks

## Layer Responsibilities

- App shell module:
  - startup wiring, global navigation graph, DI root
- Core/platform modules:
  - shared infrastructure (network, logging, analytics)
- Feature modules:
  - feature UI orchestration and local domain policies
- Shared contract modules:
  - interfaces/events used across features

## Data Flow

1. Feature UI triggers action in feature ViewModel.
2. ViewModel calls feature/domain use case.
3. Use case uses contracts from shared/core modules.
4. Data module implementation executes and returns domain results.
5. Feature maps domain output to UI state.

## Internal Architecture

Common module patterns:

- vertical feature slices (`:feature:checkout`, `:feature:profile`)
- horizontal platform modules (`:core:network`, `:core:database`)
- contract-only modules for inter-feature communication

Tooling to keep boundaries healthy:

- dependency graph visualization
- forbidden dependency lint rules
- API/ABI boundary checks in CI

## Code Examples

```kotlin
// In :feature:orders-api
interface OrdersNavigator {
    fun openOrderDetails(orderId: String)
}

// In :feature:orders-impl
class OrdersNavigatorImpl(
    private val navController: NavController
) : OrdersNavigator {
    override fun openOrderDetails(orderId: String) {
        navController.navigate("orders/$orderId")
    }
}
```

## Common Interview Questions

- When does modularization become over-engineering?
- How do you handle shared code without creating a "god core" module?
- API vs implementation dependency - what changes in build behavior?
- How do teams migrate a monolith incrementally?

## Production Considerations

- start with a few high-value boundaries, then iterate
- assign explicit owners per module
- define deprecation/migration policy for shared APIs
- measure build and integration metrics continuously

## Scalability Tradeoffs

- Pros:
  - parallel team delivery and safer refactoring
  - improved incremental build performance
- Cons:
  - coordination overhead for shared contracts
  - potential over-fragmentation and dependency friction

## Senior-Level Insights

Senior engineers should connect module boundaries to team topology.
Good architecture reduces cross-team blocking and makes ownership visible.
