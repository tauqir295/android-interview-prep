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

## Data Modeling And Storage Deep Dive
## Overview
Storage design should start from query patterns, write frequency, and consistency requirements.
## Core Concepts
- Model entities around access paths, not ER-diagram purity.
- Indexes improve reads but can increase write latency.
- Partitioning strategy matters at scale.
## Internal Architecture
- Operational DB for transactional workloads.
- Search/index store for low-latency discovery.
- Blob/object storage for large immutable media.
## Data and Request Flow
- Writes persist to source of truth first.
- Derived views/search indexes update asynchronously.
- Read path selects best store for latency requirements.
## Scalability and Reliability
- Hot partition detection and mitigation.
- Backfill/migration strategies for schema evolution.
- Backups and restore rehearsals.
## Code Examples
```text
Write: API -> Primary DB -> Change Event -> Indexer -> Search Index
Read:  API -> Search Index (list) -> DB (details)
```
## Common Interview Questions
- **Q:** SQL vs NoSQL: what decides?
  **A:** Structure the answer as constraints then tradeoffs: SLOs, capacity assumptions, bottlenecks, failure modes, and mitigation plans with clear triggers.
- **Q:** How do you handle schema migration safely?
  **A:** Structure the answer as constraints then tradeoffs: SLOs, capacity assumptions, bottlenecks, failure modes, and mitigation plans with clear triggers.
- **Q:** How do you avoid hot keys?
  **A:** Structure the answer as constraints then tradeoffs: SLOs, capacity assumptions, bottlenecks, failure modes, and mitigation plans with clear triggers.
## Production Considerations
- Enforce retention and PII handling policies.
- Instrument slow queries and index hit ratios.
## Tradeoffs
- Strong consistency vs lower latency reads.
- Denormalization speed vs update complexity.
## Senior-Level Insights
- Data lifecycle strategy is as important as schema design.
