---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/architecture/">← Back to Architecture</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/architecture/${hash}`);
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

## Scalability and Team Topologies Deep Dive

## Overview

Application architecture and team architecture co-evolve.
Technical boundaries that ignore ownership and communication patterns
usually fail at scale.

## Core Concepts

- Conway's Law impact on module boundaries
- explicit ownership for code and contracts
- integration points as socio-technical bottlenecks
- platform enablement for shared standards

## Layer Responsibilities

- Feature teams:
  - own feature modules, quality, and runtime outcomes
- Platform/core teams:
  - provide shared infrastructure and guardrails
- Architecture governance:
  - define and evolve boundary standards

## Data Flow

1. Team-owned feature emits requirements for shared capabilities.
2. Platform modules expose stable contracts.
3. Feature integrations consume contracts and report regressions.
4. Governance loop adjusts contracts/tools based on delivery friction.

## Internal Architecture

Patterns that help team scale:

- clear module ownership metadata
- ADR process for high-impact decisions
- automated dependency policy checks
- release and rollback strategy per boundary

Anti-patterns:

- shared "misc" modules without ownership
- cross-feature internals access as shortcuts
- architecture decisions undocumented after implementation

## Code Examples

```kotlin
// Example ownership metadata representation.
data class ModuleOwner(
    val module: String,
    val team: String,
    val slackChannel: String
)
```

## Common Interview Questions

- **Q:** How does architecture reduce cross-team blocking?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** What boundaries should a platform team own?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do you measure architecture scalability?
  **A:** Answer by defining boundaries and ownership first, then place business rules in the correct layer, and finish with testability and change-resilience tradeoffs.
- **Q:** How do you evolve ownership during re-orgs?
  **A:** Use STAR with explicit tradeoffs: context, options considered, decision rationale, quantified result, and what process change you institutionalized.
## Production Considerations

- publish ownership and dependency maps
- enforce compatibility/deprecation windows for shared APIs
- include architecture health KPIs in engineering reviews
- align incident response with module ownership

## Scalability Tradeoffs

- Pros:
  - predictable delivery and clearer accountability
  - faster onboarding through explicit boundaries
- Cons:
  - governance overhead
  - coordination cost for cross-cutting changes

## Senior-Level Insights

Staff candidates should discuss tradeoffs between autonomy and standardization.
The best systems provide local team freedom with global guardrails.
