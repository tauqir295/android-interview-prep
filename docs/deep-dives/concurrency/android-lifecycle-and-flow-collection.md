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

## Android Lifecycle and Flow Collection Deep Dive
## Overview
Lifecycle-aware Flow collection prevents wasted work, leaks, and duplicate
collectors after configuration or navigation transitions.
## Core Concepts
- `repeatOnLifecycle` for active-window collection
- `viewModelScope` for producer lifetime
- UI collector ownership in Fragment/Compose lifecycle scopes
- restartable collection semantics
## Internal Implementation
`repeatOnLifecycle` launches a child collector when lifecycle reaches target
state and cancels it when lifecycle falls below that state. This makes
collection restartable and avoids background collection when UI is stopped.
## Threading Model
Collection often starts on main for UI updates, while upstream may move work
with `flowOn`. Keep rendering lightweight and move expensive transforms upstream.
## Coroutine / Flow Behavior
Restartable collectors must tolerate re-subscription. Hot sources with replay
need careful configuration to avoid duplicate event handling on re-entry.
## Code Examples
```kotlin
viewLifecycleOwner.lifecycleScope.launch {
    viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state ->
            render(state)
        }
    }
}
```
## Common Interview Questions
- **Q:** Why is plain `launch { flow.collect {} }` risky in Fragments?
  **A:** Start from delivery semantics: use StateFlow for durable state, SharedFlow or Channel for transient events, and lifecycle-aware collection to prevent duplicate work.
- **Q:** How does `repeatOnLifecycle` differ from one-time collection?
  **A:** Start from delivery semantics: use StateFlow for durable state, SharedFlow or Channel for transient events, and lifecycle-aware collection to prevent duplicate work.
- **Q:** How do you avoid duplicate event consumption on recreation?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
- **Q:** What should be hot vs cold in ViewModel streams?
  **A:** Answer with correctness first and throughput second: cancellation model, dispatcher choice, bounded parallelism, and contention or latency measurements.
## Production Considerations
- tie collection to screen visibility state
- keep event channels separate from persistent state
- audit collectors during navigation backstack changes
- test lifecycle transitions explicitly
## Performance Insights
Stopping unnecessary collection in background states improves battery,
network usage, and reduces hidden memory churn.
## Senior-Level Insights
Staff-level discussion should include lifecycle ownership contracts between
presentation and domain/data layers, not only API usage.
