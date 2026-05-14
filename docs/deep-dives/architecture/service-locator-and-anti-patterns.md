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

## Service Locator and Anti-Patterns Deep Dive

## Overview

Service Locator can bootstrap dependency access quickly,
but it often hides coupling and weakens architectural clarity.

## Core Concepts

- global or scoped registry returns dependencies at runtime
- call sites hide concrete dependency requirements
- implicit wiring increases runtime failure risk
- testing often needs registry mutation/reset behavior

## Layer Responsibilities

- Locator layer:
  - stores and returns object instances/providers
- Consumers:
  - pull dependencies rather than receive them explicitly
- Test layer:
  - overrides/replaces registry entries for test isolation

## Data Flow

1. Consumer requests service from locator.
2. Locator resolves key/provider.
3. Dependency is returned and used.
4. Missing/incorrect registration fails at runtime.

## Internal Architecture

Why this degrades over time:

- hidden dependency graph at call sites
- hard-to-track lifecycle ownership
- mutation-heavy test setup
- implicit global state leakage

Controlled usage can be acceptable in tiny apps or transitional migration phases.

## Code Examples

```kotlin
object ServiceLocator {
    lateinit var analytics: Analytics
}

class HomeViewModel : ViewModel() {
    fun trackOpen() {
        ServiceLocator.analytics.log("home_open")
    }
}
```

## Common Interview Questions

- Why is constructor DI generally preferred?
- Is Service Locator always an anti-pattern?
- How do hidden dependencies hurt testability?
- How would you migrate incrementally to DI?

## Production Considerations

- avoid introducing new locator-based dependencies
- migrate hotspots first (core services, ViewModels)
- keep temporary adapters during transition
- add static checks to block direct global locator usage

## Scalability Tradeoffs

- Pros:
  - fast startup for simple prototypes
  - low initial ceremony
- Cons:
  - hidden coupling and brittle tests
  - runtime misconfiguration failures
  - poor fit for multi-team codebases

## Senior-Level Insights

Senior candidates should present migration strategy,
not just anti-pattern labeling. Good answers discuss risk-managed refactors
and compatibility bridges while moving toward explicit DI.
