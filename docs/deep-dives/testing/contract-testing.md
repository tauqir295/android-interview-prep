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

## Contract Testing Deep Dive
## Overview
This testing area improves confidence by focusing on producer-consumer alignment, schema evolution safety, and mock drift prevention.
## Core Concepts
- Prefer deterministic tests over broad but brittle coverage.
- Test behavior contracts rather than implementation details.
- Keep test ownership close to code ownership.
## Test Pyramid and Strategy
- Place this topic at the correct layer in the pyramid.
- Reserve expensive tests for high-risk regressions.
- Use risk history to prioritize suite depth.
## Tooling and Infrastructure
- Standardize fixture builders and dependency overrides.
- Keep environment setup hermetic and repeatable.
- Use CI sharding to maintain feedback speed.
## Flaky Test Mitigation
- Remove hidden time and thread dependencies.
- Replace sleeps with explicit synchronization.
- Quarantine only as a temporary safety valve.
## Code Examples
```kotlin
@Test
fun sample() = runTest {
    // Arrange
    // Act
    // Assert
}
```
## Common Interview Questions
- **Q:** Why does this test belong at this layer?
  **A:** Answer by test pyramid intent: unit for logic speed, integration for boundaries, and end-to-end for critical journeys with flakiness controls.
- **Q:** What failure mode does this suite catch best?
  **A:** Answer by test pyramid intent: unit for logic speed, integration for boundaries, and end-to-end for critical journeys with flakiness controls.
- **Q:** How do you keep signal high as suite size grows?
  **A:** Answer by test pyramid intent: unit for logic speed, integration for boundaries, and end-to-end for critical journeys with flakiness controls.
## Production Considerations
- Tie test gates to release risk and incident history.
- Track regression escape rate as an outcome metric.
- Keep slow, low-signal tests under review.
## Performance Insights
- Fast suites enable frequent refactoring and safer iteration.
- Deterministic async testing reduces rerun waste in CI.
## Senior-Level Insights
- Great answers explain tradeoffs between confidence, cost, and team velocity.
