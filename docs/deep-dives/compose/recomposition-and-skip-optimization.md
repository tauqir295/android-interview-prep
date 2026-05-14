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
# Recomposition and Skip Optimization Deep Dive

## Overview

Recomposition is selective re-execution of composables affected by state changes.
Skip optimization allows runtime to avoid re-running groups whose inputs are unchanged.

## Core Concepts

- invalidation: marking a composition scope dirty
- restart groups: compiler-defined recomposition units
- skippable groups: eligible for fast path when parameters unchanged
- stability: influences whether change detection is reliable

## Runtime Internals

Compose compiler inserts bookkeeping parameters and group markers.
At runtime, `Composer` evaluates whether a group can be skipped based on:

- parameter change flags
- stability metadata
- group restartability/skippability

Unstable parameter types often reduce skip opportunities.

## Composition / Recomposition Flow

1. Initial composition records state reads.
2. State mutation invalidates readers.
3. Recomposer schedules work on next frame.
4. Invalidated groups are revisited.
5. Groups with unchanged/stable inputs are skipped.
6. Apply phase commits node changes.

## State Management

State design strongly affects recomposition behavior:

- isolate fast-changing state to narrow scopes
- avoid passing large unstable models down deep trees
- use derived state for frequently recomputed projections
- use stable item keys in lazy lists

## Code Examples

```kotlin
@Composable
fun InboxScreen(state: InboxUiState) {
    val unreadCount by remember(state.messages) {
        derivedStateOf { state.messages.count { !it.isRead } }
    }

    Column {
        Text("Unread: $unreadCount")
        LazyColumn {
            items(state.messages, key = { it.id }) { message ->
                MessageRow(message = message)
            }
        }
    }
}
```

```kotlin
@Composable
fun SearchResultList(
    query: String,
    results: List<ResultUi>
) {
    // Keep expensive filtering scoped and memoized to inputs.
    val visible by remember(query, results) {
        derivedStateOf { results.filter { it.title.contains(query, ignoreCase = true) } }
    }
    LazyColumn { items(visible, key = { it.id }) { ResultRow(it) } }
}
```

## Common Interview Questions

- What exactly triggers recomposition?
- Why does unstable input type hurt performance?
- Is recomposition the same as redraw?
- How do you diagnose "too much recomposition"?

## Production Considerations

- Profile before micro-optimizing.
- Keep composables focused and parameter surfaces minimal.
- Watch for frequently recreated lambdas/objects in hot paths.
- Prefer immutable UI models with stable identity fields.

## Performance Insights

- Not all recompositions are bad; unnecessary broad recompositions are.
- High skip rates in hot areas usually improve frame consistency.
- Large list screens are sensitive to key and stability mistakes.

## Senior-Level Insights

Top-tier answers discuss tradeoffs:

- readability first, then targeted optimization
- use compiler metrics/tracing for evidence-driven tuning
- architecture decisions upstream determine runtime cost downstream

