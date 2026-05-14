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

## Testing Fundamentals Deep Dive
## Overview
Testing strategy should maximize confidence per minute of execution and maintenance cost.
## Core Concepts
- Fast, deterministic tests close to business logic.
- Fewer but meaningful integration tests.
- Selective UI and end-to-end tests for critical journeys.
## Test Pyramid and Strategy
- Unit tests: broad coverage, low runtime cost.
- Integration tests: boundary correctness.
- UI/E2E tests: user-critical flows only.
## Tooling and Infrastructure
- JUnit + coroutine test APIs.
- MockWebServer for network determinism.
- CI sharding for parallel execution.
## Flaky Test Mitigation
- Eliminate timing assumptions.
- Replace real clocks and dispatchers.
- Isolate shared mutable test state.
## Code Examples
```kotlin
@Test
fun repository_returnsCachedValueBeforeNetwork() {
    // Arrange
    // Act
    // Assert
}
```
## Common Interview Questions
- How do you pick the right test layer?
- What makes a suite trustworthy?
- How do you reduce flaky runs?
## Production Considerations
- Test failures should be actionable.
- Keep test runtime budgets for CI.
## Performance Insights
- Prioritize test parallelism and hermetic setup.
## Senior-Level Insights
- Strong strategy balances speed, reliability, and maintainability.
