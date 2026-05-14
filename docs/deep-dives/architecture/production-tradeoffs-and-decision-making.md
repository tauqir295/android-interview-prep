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

# Production Tradeoffs and Decision-Making Deep Dive

## Overview

Architecture decisions are context-bound tradeoffs, not universal truths.
Senior interviews often evaluate decision quality under constraints,
not pattern memorization.

## Core Concepts

- explicit decision framing (problem, options, constraints)
- ADRs to document rationale and consequences
- risk-driven architecture (failure modes first)
- feedback loops through operational metrics

## Layer Responsibilities

- Feature teams:
  - propose and validate local architecture decisions
- Platform/architecture leads:
  - define cross-system guardrails
- Engineering leadership:
  - align technical decisions with product and org constraints

## Data Flow

1. Problem statement and constraints are captured.
2. Candidate options are evaluated against quality attributes.
3. Decision is recorded with expected outcomes and risks.
4. Implementation ships with observability hooks.
5. Metrics/postmortems refine future decisions.

## Internal Architecture

Useful decision tools:

- quality attribute matrix (latency, reliability, maintainability, cost)
- blast-radius analysis for boundary changes
- migration plans with rollback strategy
- decision expiry review for long-lived assumptions

## Code Examples

```kotlin
// ADR metadata model example.
data class ArchitectureDecision(
    val id: String,
    val context: String,
    val decision: String,
    val consequences: List<String>
)
```

## Common Interview Questions

- How do you choose between speed and maintainability?
- What does a strong architecture proposal include?
- How do you know when to revisit old decisions?
- How do you communicate tradeoffs to non-architect stakeholders?

## Production Considerations

- require written rationale for high-impact architecture changes
- define measurable success/failure criteria before rollout
- include rollback plans in design reviews
- revisit major decisions after incidents or scale shifts

## Scalability Tradeoffs

- Pros:
  - better decision traceability and institutional learning
  - reduced repeated debate on solved problems
- Cons:
  - additional process overhead
  - risk of documentation drift without ownership

## Senior-Level Insights

Strong senior/staff answers show structured reasoning.
They explain what was chosen, what was rejected,
what risks were accepted, and how outcomes were measured.
