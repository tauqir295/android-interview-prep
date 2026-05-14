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

## Consistency And Transactions Deep Dive
## Overview
Distributed systems trade strict consistency for availability and latency under failure.
## Core Concepts
- Strong consistency for critical invariants.
- Eventual consistency for scalable derived views.
- Idempotency and ordering are essential for retries.
## Internal Architecture
- Transaction boundary lives inside one service/database when possible.
- Cross-service workflows use sagas and compensating actions.
## Data and Request Flow
- Command accepted -> durable write -> outbox event.
- Consumers apply events idempotently.
- Reconciliation jobs correct drift over time.
## Scalability and Reliability
- Exactly-once is expensive; aim for effectively-once via idempotency.
- Include dedupe keys and replay-safe handlers.
## Code Examples
```text
Order Created -> Payment Reserved -> Inventory Reserved -> Confirmed
                      on failure -> Compensation steps
```
## Common Interview Questions
- When do you use ACID transactions?
- How do you explain saga failure handling?
- How do you guarantee no duplicate side effects?
## Production Considerations
- Keep audit trails for state transitions.
- Provide operator tooling for stuck workflows.
## Tradeoffs
- Transactional simplicity vs cross-service scalability.
- Immediate consistency vs higher throughput.
## Senior-Level Insights
- Mature designs include reconciliation and operational playbooks.
