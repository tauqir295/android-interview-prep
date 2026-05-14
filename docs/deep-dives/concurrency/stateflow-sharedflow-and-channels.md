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

## StateFlow, SharedFlow, and Channels Deep Dive
## Overview
These primitives represent different messaging semantics:
state, broadcast events, and point-to-point queues.
## Core Concepts
- `StateFlow`: state holder with current value
- `SharedFlow`: multicast stream with configurable replay
- `Channel`: queue/handoff semantics
- delivery guarantees and subscriber topology
## Internal Implementation
`StateFlow` is a specialized `SharedFlow` optimized for current-state access.
`SharedFlow` maintains replay cache and subscriber coordination.
`Channel` coordinates send/receive with capacity/backpressure semantics.
## Threading Model
All three are coroutine-friendly and can be used across dispatchers, but
ownership and collection lifecycle should remain explicit in architecture.
## Coroutine / Flow Behavior
UI state should generally be `StateFlow`.
One-off UI events usually fit `SharedFlow` with low replay.
Work-queue or request-response pipelines often map better to `Channel`.
## Code Examples
```kotlin
private val _state = MutableStateFlow(UiState())
val state: StateFlow<UiState> = _state
private val _events = MutableSharedFlow<UiEvent>(replay = 0)
val events: SharedFlow<UiEvent> = _events
private val workQueue = Channel<WorkItem>(capacity = Channel.BUFFERED)
```
## Common Interview Questions
- Why are one-off events awkward with plain `StateFlow`?
- When is a `Channel` safer than `SharedFlow`?
- How does replay affect duplicate UI actions?
- How do you model state and events separately in ViewModel?
## Production Considerations
- separate state stream from event stream
- keep replay minimal for transient events
- document consumer assumptions for channels
- test collector restart behavior
## Performance Insights
Misconfigured replay/capacity can create memory pressure or dropped signals.
Tune by event criticality and collector speed.
## Senior-Level Insights
Great answers center on semantics first, API second:
choose primitive by delivery contract, not popularity.
