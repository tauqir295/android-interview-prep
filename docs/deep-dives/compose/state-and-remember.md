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
# State and Remember Deep Dive

## Overview

State is the central driver of Compose rendering. `remember` stores values
across recompositions, while Compose snapshot state notifies the runtime when
values change.

## Core Concepts

- `mutableStateOf` creates observable state.
- `remember` preserves value while composable stays in composition.
- `rememberSaveable` restores value after configuration/process recreation.
- Keys control reset behavior for remembered values.

## Runtime Internals

`remember` stores values in slot table positions. If call order and keys match,
runtime reuses the stored value; otherwise, it drops and recreates it.

`MutableState` integrates with snapshots so writes can invalidate readers and
schedule recomposition safely.

## Composition / Recomposition Flow

- Compose reads `state.value` during composition.
- Runtime records that read for the current group.
- State write invalidates dependent group(s).
- Recomposition re-executes group and reuses remembered values when valid.

## State Management

Use ownership levels deliberately:

- local widget state: text field focus, expansion toggles
- screen state: ViewModel `StateFlow<UiState>`
- restorable UI state: `rememberSaveable`

Avoid storing mutable collections directly inside state without immutable wrappers.

## Code Examples

```kotlin
@Composable
fun SearchBar() {
    var query by rememberSaveable { mutableStateOf("") }

    TextField(
        value = query,
        onValueChange = { query = it },
        label = { Text("Search") }
    )
}

@Composable
fun UserCard(userId: String) {
    // Recreate avatar painter if identity input changes.
    val avatarPainter = remember(userId) { loadAvatarPainter(userId) }
    Image(painter = avatarPainter, contentDescription = null)
}
```

## Common Interview Questions

- Why does Compose prefer immutable UI models?
- When does `remember` lose state?
- How does `rememberSaveable` decide what can be saved?
- What are key-related state bugs in dynamic lists?

## Production Considerations

- Keep remembered state minimal and local.
- Hoist state if multiple children need shared ownership.
- Prefer stable IDs as keys.
- Use custom `Saver` for non-primitive restorable objects.

## Performance Insights

- Overusing `remember` for cheap values can add complexity without gains.
- Missing keys can retain stale expensive resources.
- Correct state boundaries reduce invalidation blast radius.

## Senior-Level Insights

At senior/staff interviews, explain both API and runtime model:

- remember is slot-table backed positional storage
- state writes are snapshot transactions
- incorrect identity assumptions are a top source of flaky UI behavior

