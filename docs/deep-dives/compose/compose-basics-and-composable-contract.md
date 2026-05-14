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
## Compose Basics and Composable Contract Deep Dive

## Overview

Jetpack Compose shifts Android UI from imperative view mutation to declarative rendering.
At interview level, the key message is: UI is a function of current state.

## Core Concepts

- Declarative UI: describe desired UI, not mutation steps.
- `@Composable` contract: function can emit UI into composition tree.
- Composition tree: hierarchical structure produced by composables.
- Identity by call position + keys: important for state retention.

## Runtime Internals

Compose compiler rewrites composables into functions that receive a `Composer`
and change-tracking flags. This enables restart groups, skipping, and remember slots.

Important internals to mention:

- positional memoization model
- compiler-generated group boundaries
- runtime-managed tree diff/apply behavior

## Composition / Recomposition Flow

1. Initial composition executes composables and builds groups.
2. Runtime tracks state reads for each group.
3. On state change, affected groups are invalidated.
4. Recomposition re-executes invalidated groups only.
5. Apply phase updates UI nodes.

## State Management

For basics, state should follow this separation:

- local ephemeral UI state with `remember`
- restorable UI state with `rememberSaveable`
- screen/business state in ViewModel

Avoid mixing state ownership across multiple layers without clear boundaries.

## Code Examples

```kotlin
@Composable
fun ProfileHeader(name: String, isOnline: Boolean) {
    Row {
        Text(text = name)
        if (isOnline) {
            Text(text = " • Online")
        }
    }
}

@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    Column {
        Text("Count: $count")
        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}
```

## Common Interview Questions

- Why is Compose called declarative?
- Is a composable lifecycle same as Activity lifecycle?
- Why should composables avoid side effects during rendering?
- How does Compose know which UI to update?

## Production Considerations

- Keep composables small and single-purpose.
- Pass explicit state + callbacks to improve testability.
- Avoid hidden dependencies for business logic.
- Use previews for fast UI iteration, but validate with tests.

## Performance Insights

- Smaller, focused composables create cleaner recomposition boundaries.
- Stable inputs improve skipping opportunities.
- Excessive lambda/object allocation in hot paths can increase frame cost.

## Senior-Level Insights

Strong senior answers connect API ergonomics to runtime behavior:

- compiler inserts change tracking and restart groups
- runtime re-executes selectively rather than re-rendering whole screen
- architectural state boundaries directly influence performance characteristics

