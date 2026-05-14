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

# Dagger and Component Graph Deep Dive

## Overview

Dagger gives fine-grained control over dependency graph architecture.
It is powerful for complex systems but requires strong design discipline.

## Core Concepts

- component defines injectable graph boundary
- subcomponent models child lifecycle scope
- module provides/binds dependencies
- compile-time validation catches wiring errors early

## Layer Responsibilities

- Core platform modules:
  - provide shared infra services
- Feature graph modules:
  - declare feature-specific implementations
- Entry components:
  - expose required dependencies to Android boundary classes

## Data Flow

1. Root component initializes global graph.
2. Child/subcomponent is created per feature or lifecycle scope.
3. Requested object graph is resolved through providers/bindings.
4. Injected classes execute domain/data flow.

## Internal Architecture

Graph design decisions:

- subcomponents vs component dependencies
- multibinding for extensibility points
- scope boundaries to prevent accidental object sharing

Complexity risks:

- cyclic dependencies through bindings
- over-centralized mega-modules
- slow builds due to graph explosion

## Code Examples

```kotlin
@Singleton
@Component(modules = [NetworkModule::class, RepositoryModule::class])
interface AppComponent {
    fun feedComponentFactory(): FeedComponent.Factory
}

@Subcomponent(modules = [FeedModule::class])
@FeatureScope
interface FeedComponent {
    @Subcomponent.Factory
    interface Factory {
        fun create(): FeedComponent
    }
}
```

## Common Interview Questions

- When to use subcomponents vs component dependencies?
- How do scopes map to Android lifecycles?
- Why might Dagger builds become slow?
- How do you debug missing binding chains?

## Production Considerations

- keep module ownership per team/feature
- reduce public graph surface to essential contracts
- fail PRs on unauthorized graph coupling
- maintain graph diagrams for critical modules

## Scalability Tradeoffs

- Pros:
  - maximal flexibility and explicit control
  - strong compile-time graph safety
- Cons:
  - high setup/maintenance complexity
  - steeper onboarding and debugging costs

## Senior-Level Insights

Staff-level discussion should cover how graph governance evolves:
ownership rules, build performance budgets,
and strategies to prevent dependency sprawl.
