---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/concurrency/">← Back to Concurrency</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/concurrency/${hash}`);
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

## Flow Sharing and Hot Streams Deep Dive
## Overview
`stateIn` and `shareIn` convert cold flows into shared hot streams,
helping avoid duplicated upstream work across collectors.
## Core Concepts
- cold source vs shared hot stream
- replay behavior and memory tradeoffs
- `SharingStarted` policies (`WhileSubscribed`, eager, lazy)
- state streams vs event streams
## Internal Implementation
`stateIn` maintains a latest value cache and a sharing job.
`shareIn` uses a shared upstream collector and multicast emissions to downstream
collectors, with configurable replay/buffer behavior.
## Threading Model
Sharing scope defines lifetime and dispatcher context.
Choosing too-wide scope creates long-lived producers and stale work.
## Coroutine / Flow Behavior
Hot streams continue based on sharing policy, not individual collectors.
Using `WhileSubscribed` can reduce wasted work in UI-driven contexts.
## Code Examples
```kotlin
val uiState: StateFlow<UiState> = repository.observeItems()
    .map { items -> UiState(items = items) }
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = UiState.Loading
    )
```
## Common Interview Questions
- When should you use `stateIn` vs `shareIn`?
- What replay value should be used for one-off events?
- How can sharing leak work in long-lived scopes?
- Why can `WhileSubscribed` improve battery/network usage?
## Production Considerations
- choose replay deliberately
- avoid event duplication with accidental replay > 0
- align sharing scope with lifecycle ownership
- measure upstream subscription churn
## Performance Insights
Sharing can cut repeated network/db work significantly, but over-sharing can
increase memory retention and stale background activity.
## Senior-Level Insights
Senior design answers should include explicit lifecycle ownership for each
hot stream and policies for when producers should stop.
