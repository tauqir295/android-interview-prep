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

## Test Pyramid And Strategy Deep Dive
## Overview
The pyramid is a cost model: many cheap tests, fewer expensive ones.
## Core Concepts
- Unit tests validate decision logic.
- Integration tests validate contracts.
- UI/E2E validate key user outcomes.
## Test Pyramid and Strategy
- Keep the base broad and stable.
- Avoid over-investing in brittle UI tests.
- Use risk-based prioritization for top flows.
## Tooling and Infrastructure
- Distinct test modules and clear ownership.
- Stable test data builders and fixtures.
## Flaky Test Mitigation
- No sleeps; use explicit synchronization.
- Disable network/time nondeterminism.
## Code Examples
```kotlin
@Test
fun useCase_emitsError_whenDependencyFails() {
    // deterministic dependency behavior
}
```
## Common Interview Questions
- Is the pyramid still relevant with Compose?
- How do you justify fewer E2E tests?
## Production Considerations
- Tie strategy to release risk and incident history.
## Performance Insights
- A healthy pyramid keeps CI fast as the codebase grows.
## Senior-Level Insights
- Staff-level candidates explain organizational tradeoffs, not just tooling.
