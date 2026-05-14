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
## Slot Table and Runtime Internals Deep Dive

## Overview

The slot table is Compose runtime's structural memory for composition groups,
remembered values, and positional metadata.

## Core Concepts

- group structure and anchors
- positional memoization
- remember value storage
- key-based identity adjustments

## Runtime Internals

Composer writes group operations into slot table during composition. On updates,
runtime reuses or edits groups instead of rebuilding the full tree.

## Composition / Recomposition Flow

- traverse existing groups
- detect structural changes
- insert/move/remove group operations
- update remembered slots and apply node edits

## State Management

`remember` correctness depends on stable call ordering and keys relative to slot positions.

## Code Examples

```kotlin
@Composable
fun ItemRow(item: ItemUi) {
    val formatter = remember(item.id) { NumberFormat.getInstance() }
    Text(formatter.format(item.count))
}
```

## Common Interview Questions

- What breaks positional memoization?
- How are list item moves handled with and without keys?

## Production Considerations

- keep composition structure predictable
- use explicit item keys in dynamic collections
- avoid implicit identity assumptions in complex conditionals

## Performance Insights

Healthy slot reuse avoids unnecessary churn in composition memory and apply work.

## Senior-Level Insights

Staff-level conversations often include slot-table mental model for debugging
state jump bugs and list identity issues.
