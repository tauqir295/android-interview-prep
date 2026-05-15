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

## Dependency Injection Strategies Deep Dive

## Overview

Dependency injection is an architectural tool for explicit object graph design.
At scale, DI quality affects reliability, testability, and developer velocity.

## Core Concepts

- constructor injection as default dependency declaration
- interface-driven boundaries for replaceability
- scope alignment with lifecycle to avoid leaks/churn
- composition root controls graph assembly

## Layer Responsibilities

- Presentation:
  - request/use dependencies via constructors (ViewModel, coordinators)
- Domain:
  - depend on interfaces for repositories/services
- Data:
  - provide concrete implementations and adapters
- Composition root (DI modules):
  - wire implementations to abstractions

## Data Flow

DI itself is not data flow; it enables flow paths.

1. App start creates root graph.
2. Feature entry creates scoped dependencies.
3. ViewModel receives use case and repository abstractions.
4. Use case calls data implementations through interfaces.

## Internal Architecture

Scoping decisions are architecture decisions:

- app-wide singletons for stateless shared services
- feature/session scopes for user-contextful components
- ViewModel scope for screen state orchestrators

Mis-scoping patterns to avoid:

- sharing mutable state as singleton unintentionally
- recreating expensive clients per request path

## Code Examples

```kotlin
class GetFeedUseCase(
    private val repository: FeedRepository
)

class FeedViewModel(
    private val getFeedUseCase: GetFeedUseCase
) : ViewModel()

@Module
@InstallIn(ViewModelComponent::class)
object FeedModule {
    @Provides
    fun provideGetFeedUseCase(repo: FeedRepository): GetFeedUseCase {
        return GetFeedUseCase(repo)
    }
}
```

## Common Interview Questions

- **Q:** Why is constructor injection preferred over field injection?
  **A:** Frame it around graph ownership: prefer constructor injection, align scopes to lifecycle boundaries, keep contracts explicit, and validate with test replacements.
- **Q:** How do you choose scope lifetimes?
  **A:** Frame it around graph ownership: prefer constructor injection, align scopes to lifecycle boundaries, keep contracts explicit, and validate with test replacements.
- **Q:** When is a Service Locator acceptable?
  **A:** Frame it around graph ownership: prefer constructor injection, align scopes to lifecycle boundaries, keep contracts explicit, and validate with test replacements.
- **Q:** How do you test graph-heavy code without brittle setup?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
## Production Considerations

- standardize module/package conventions for bindings
- keep binding ownership close to implementation modules
- fail fast on missing/wrong bindings in CI
- budget for annotation-processing build costs

## Scalability Tradeoffs

- Pros:
  - explicit contracts and easier test doubles
  - consistent wiring patterns across large teams
- Cons:
  - graph complexity and compile-time cost growth
  - steeper onboarding in very modular systems

## Senior-Level Insights

Strong senior answers discuss DI as socio-technical design:
who owns bindings, how graph changes are reviewed,
and how teams prevent dependency sprawl over time.
