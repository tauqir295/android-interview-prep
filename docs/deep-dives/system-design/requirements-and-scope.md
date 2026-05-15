---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/system-design/">← Back to System Design</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/system-design/${hash}`);
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

## Requirements And Scope Deep Dive
## Overview
Most failed design answers come from weak scope control, not weak technical knowledge.
## Core Concepts
- Functional requirements: user-visible capabilities.
- Non-functional requirements: latency, reliability, throughput, security.
- Explicitly de-scope nice-to-have features.
## Internal Architecture
- Scope determines architecture complexity.
- Narrow scope allows simpler single-region design.
- Broad scope may require eventing, partitioning, and regional strategy.
## Data and Request Flow
- Define top 2-3 critical flows first.
- Add secondary flows only after core flow is stable.
## Scalability and Reliability
- Capacity targets should map to scope.
- Reliability target (e.g., 99.9%) changes retry, storage, and failover choices.
## Code Examples
```text
Inputs: users, regions, RPS, payload, freshness
Outputs: service topology, storage choice, scaling strategy
```
## Common Interview Questions
- **Q:** How do you gather requirements quickly?
  **A:** Structure the answer as constraints then tradeoffs: SLOs, capacity assumptions, bottlenecks, failure modes, and mitigation plans with clear triggers.
- **Q:** How do you prevent over-design?
  **A:** Structure the answer as constraints then tradeoffs: SLOs, capacity assumptions, bottlenecks, failure modes, and mitigation plans with clear triggers.
- **Q:** Which constraints change architecture the most?
  **A:** Structure the answer as constraints then tradeoffs: SLOs, capacity assumptions, bottlenecks, failure modes, and mitigation plans with clear triggers.
## Production Considerations
- Align scope with team size and on-call maturity.
- Document accepted risks explicitly.
## Tradeoffs
- Delivery speed vs architectural completeness.
- Product breadth vs system depth.
## Senior-Level Insights
- Great answers show what you intentionally did not build.
