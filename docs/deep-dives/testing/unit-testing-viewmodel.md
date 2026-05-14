---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/testing/">← Back to Testing</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/testing/${hash}`);
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

## Unit Testing Viewmodel Deep Dive
## Overview
ViewModel unit tests should validate state transitions and intent handling, not framework internals.
## Core Concepts
- Inputs: intents/actions/events.
- Outputs: immutable UI state + one-off events.
- Dependencies replaced with deterministic fakes/mocks.
## Test Pyramid and Strategy
- Keep ViewModel tests at unit layer for speed.
- Verify happy path, error path, and loading path.
## Tooling and Infrastructure
- `runTest` + test dispatcher.
- Assert state timeline, not only final state.
## Flaky Test Mitigation
- Avoid real dispatcher/thread usage.
- Control time for debounce/retry logic.
## Code Examples
```kotlin
@Test
fun loadProfile_updatesUiState() = runTest {
    // Given fake repository success
    // When load invoked
    // Then loading -> content state emitted
}
```
## Common Interview Questions
- What exactly do you assert in ViewModel tests?
- How do you test one-off events safely?
## Production Considerations
- Keep ViewModel APIs deterministic and test-friendly.
## Performance Insights
- Fast unit suites enable frequent refactors.
## Senior-Level Insights
- Good tests encode domain behavior, not implementation noise.
