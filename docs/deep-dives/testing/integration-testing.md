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

## Integration Testing Deep Dive
## Overview
Integration tests verify that component boundaries work together under realistic contracts.
## Core Concepts
- Focus on seams: API, DB, serialization, auth, and feature wiring.
- Test real adapters where regressions are costly.
## Test Pyramid and Strategy
- Keep integration tests fewer than unit tests.
- Prioritize paths linked to previous incidents.
## Tooling and Infrastructure
- MockWebServer for HTTP contracts.
- In-memory Room for repository+DAO wiring.
- Dependency injection overrides for test modules.
## Flaky Test Mitigation
- Isolate environment and reset state per test.
- Avoid global mutable config.
## Code Examples
```kotlin
@Test
fun apiResponse_mapsToDomain_andPersistsLocally() = runTest {
    // network -> mapper -> dao -> readback assertions
}
```
## Common Interview Questions
- **Q:** What belongs in integration vs E2E?
  **A:** Answer by test pyramid intent: unit for logic speed, integration for boundaries, and end-to-end for critical journeys with flakiness controls.
- **Q:** How do you keep integration tests maintainable?
  **A:** Answer by test pyramid intent: unit for logic speed, integration for boundaries, and end-to-end for critical journeys with flakiness controls.
## Production Considerations
- Integration coverage should mirror critical release gates.
## Performance Insights
- Parallelize suites and shard by module.
## Senior-Level Insights
- Mature teams continuously rebalance integration scope from incident data.
