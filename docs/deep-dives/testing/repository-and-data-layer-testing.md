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

## Repository And Data Layer Testing Deep Dive
## Overview
Repository tests validate orchestration across local cache, network, and sync logic.
## Core Concepts
- Clear source-of-truth policy.
- Deterministic fallback rules.
- Explicit cache invalidation behavior.
## Test Pyramid and Strategy
- Unit test orchestration branches first.
- Add integration tests for persistence/network boundary.
## Tooling and Infrastructure
- Fake local store + fake remote API for unit speed.
- In-memory DB + MockWebServer for integration confidence.
## Flaky Test Mitigation
- No shared singleton test state.
- Stable fixture data and repeatable ordering.
## Code Examples
```kotlin
@Test
fun repository_usesCacheThenRefreshesFromNetwork() = runTest {
    // Assert stale-while-revalidate behavior
}
```
## Common Interview Questions
- How do you test offline-first repository behavior?
- What do you mock vs keep real?
## Production Considerations
- Validate retry and conflict-resolution paths.
## Performance Insights
- Keep integration tests narrow to maintain CI throughput.
## Senior-Level Insights
- Strong candidates explain consistency and sync semantics, not just assertions.
