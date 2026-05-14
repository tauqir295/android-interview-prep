---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/compose/">← Back to Compose</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/compose/${hash}`);
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
# Navigation in Compose Deep Dive

## Overview

Compose navigation should be treated as explicit route contracts, not ad-hoc string pushes.
Maintainability comes from typed arguments and clear ownership of navigation decisions.

## Core Concepts

- route graph and destination contracts
- argument passing by IDs
- back stack semantics
- deep link handling

## Runtime Internals

Navigation state updates drive destination composable changes and back stack mutations.
Each destination composes/disposes with navigation lifecycle transitions.

## Composition / Recomposition Flow

- event triggers navigation action
- nav state mutates
- destination composition changes
- previous destination may remain on back stack

## State Management

Store screen state in destination-scoped ViewModels and avoid leaking navigation concerns
into presentational child composables.

## Code Examples

```kotlin
NavHost(navController = navController, startDestination = "home") {
    composable("home") { HomeRoute(onOpenDetails = { id -> navController.navigate("details/$id") }) }
    composable("details/{id}") { backStackEntry ->
        DetailsRoute(itemId = backStackEntry.arguments?.getString("id") ?: "")
    }
}
```

## Common Interview Questions

- Should you pass full objects or IDs through routes?
- How do you test navigation contracts?

## Production Considerations

- centralize route declarations
- support deep links explicitly
- keep back behavior deterministic and test-covered

## Performance Insights

Navigation bugs often look like UI bugs; clear contract boundaries reduce churn
and costly rework.

## Senior-Level Insights

Senior answers discuss modular navigation ownership and migration strategy for
multi-module apps.
