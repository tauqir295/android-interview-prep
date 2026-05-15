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

## System Design Fundamentals Deep Dive
## Overview
System design interviews test whether you can move from ambiguous requirements to a practical architecture with clear tradeoffs.
## Core Concepts
- Start with requirements, constraints, and success metrics.
- Define scale assumptions early (QPS, data size, latency targets).
- Prioritize correctness and operability over novelty.
## Internal Architecture
- Client -> edge/API gateway -> stateless services -> data stores.
- Separate read-heavy and write-heavy paths where possible.
- Keep boundaries explicit for ownership and failure isolation.
## Data and Request Flow
- Request enters gateway, is authenticated, then routed to service.
- Service reads cache first, then storage fallback on miss.
- Write path records durable state before async fan-out.
## Scalability and Reliability
- Horizontal scaling for stateless services.
- Backpressure + rate limiting at ingress.
- Timeouts, retries with jitter, and circuit breakers.
## Code Examples
```text
Mobile App -> API Gateway -> BFF -> Services -> DB
                               \-> Queue -> Workers
```
## Common Interview Questions
- **Q:** How do you structure an answer in 35-45 minutes?
  **A:** Structure the answer as constraints then tradeoffs: SLOs, capacity assumptions, bottlenecks, failure modes, and mitigation plans with clear triggers.
- **Q:** What assumptions should you state first?
  **A:** Structure the answer as constraints then tradeoffs: SLOs, capacity assumptions, bottlenecks, failure modes, and mitigation plans with clear triggers.
- **Q:** Which tradeoffs matter most for Android clients?
  **A:** State load and SLO assumptions first, identify the first bottleneck, choose scaling and consistency strategy, and explain fallback behavior for partial failures.
## Production Considerations
- Define SLIs/SLOs before choosing technology.
- Plan observability from day one.
- Keep migration strategy for schema/API changes.
## Tradeoffs
- Simplicity vs flexibility.
- Consistency vs availability.
- Latency vs cost.
## Senior-Level Insights
- Strong candidates make uncertainty explicit.
- Staff-level answers include rollout and failure modes.
