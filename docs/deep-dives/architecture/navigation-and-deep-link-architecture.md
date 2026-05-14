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

## Navigation and Deep Link Architecture Deep Dive

## Overview

Navigation architecture should be contract-driven, testable, and module-aware.
Deep links should be treated as external APIs that require compatibility
and security considerations.

## Core Concepts

- destination contracts over raw string usage
- route argument validation at boundaries
- deep links as versioned external entry points
- ownership of back stack behavior per app shell/feature shell

## Layer Responsibilities

- Presentation/navigation layer:
  - route to destinations and map arguments
  - execute UI-level transitions
- Feature layer:
  - expose destination entry contracts
  - keep internal navigation details encapsulated
- Platform/security layer:
  - validate deep link origins and payloads
  - enforce auth and feature-gating requirements

## Data Flow

1. Navigation event occurs (user action or deep link intent).
2. Router validates destination and arguments.
3. Feature entry point receives contract-safe input.
4. Feature ViewModel loads state based on IDs/keys.
5. UI renders and handles back behavior with explicit policy.

## Internal Architecture

Recommended patterns:

- central route registry with typed helpers
- feature-level navigation interfaces
- deep-link parser + validator pipeline
- fallback path for unsupported or stale links

Avoid passing heavyweight mutable objects through routes;
pass stable IDs and rehydrate from repository/domain layers.

## Code Examples

```kotlin
sealed interface AppRoute {
    data object Home : AppRoute
    data class OrderDetails(val orderId: String) : AppRoute
}

fun NavController.navigate(route: AppRoute) {
    when (route) {
        AppRoute.Home -> navigate("home")
        is AppRoute.OrderDetails -> navigate("orders/${route.orderId}")
    }
}
```

## Common Interview Questions

- How do you design navigation for multi-module apps?
- Where should deep link validation and auth checks happen?
- How do you keep route contracts backward compatible?
- What are common back-stack bugs and how do you prevent them?

## Production Considerations

- log deep-link parse failures and destination fallbacks
- keep route schema changes backwards-compatible where possible
- test cold-start deep links, authenticated flows, and process-death recovery
- document cross-feature navigation contracts as stable APIs

## Scalability Tradeoffs

- Pros:
  - clearer ownership and safer feature independence
  - better QA and observability for routing issues
- Cons:
  - typed contract layers add upfront complexity
  - migration cost from ad-hoc navigation can be high

## Senior-Level Insights

Strong senior answers link navigation architecture to product reliability.
At scale, deep links are integration points with marketing, web, and partner systems,
so architecture must prioritize compatibility, security, and diagnostics.
