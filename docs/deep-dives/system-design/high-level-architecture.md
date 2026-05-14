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

## High Level Architecture Deep Dive
## Overview
A good high-level architecture shows clear boundaries, clear ownership, and clear failure domains.
## Core Concepts
- Stateless compute tier for elasticity.
- Stateful tier optimized for access patterns.
- Async processing for decoupling and smoothing spikes.
## Internal Architecture
- API gateway handles auth, routing, quotas.
- BFF adapts backend contracts for Android app needs.
- Domain services encapsulate business logic and data ownership.
## Data and Request Flow
- Read path: Gateway -> BFF -> service -> cache/DB.
- Write path: validate -> persist -> publish event -> downstream processing.
## Scalability and Reliability
- Use autoscaling for stateless nodes.
- Isolate heavy jobs in worker pools.
- Protect dependencies with budgets, retries, and fallback.
## Code Examples
```text
[Gateway] -> [BFF] -> [User Service] -> [User DB]
                   -> [Feed Service] -> [Cache + Feed DB]
```
## Common Interview Questions
- Why include a BFF?
- How do you split service boundaries?
- What is your fallback plan on dependency failure?
## Production Considerations
- Version APIs safely.
- Keep observability at each boundary.
- Prefer gradual migration over big-bang rewrites.
## Tradeoffs
- Monolith simplicity vs microservice autonomy.
- Fewer services vs independent scaling.
## Senior-Level Insights
- Boundary quality predicts long-term team velocity.
