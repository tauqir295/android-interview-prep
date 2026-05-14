# System Design Deep Dive Mapping & Architecture

## Overview

This document maps System Design interview questions to shared deep dives.
It keeps `data/system-design.yaml` concise while deep implementation detail lives in markdown.

---

## Recommended Deep Dive Files

1. `docs/deep-dives/system-design/system-design-fundamentals.md`
2. `docs/deep-dives/system-design/requirements-and-scope.md`
3. `docs/deep-dives/system-design/high-level-architecture.md`
4. `docs/deep-dives/system-design/data-modeling-and-storage.md`
5. `docs/deep-dives/system-design/consistency-and-transactions.md`
6. `docs/deep-dives/system-design/scalability-and-capacity-planning.md`
7. `docs/deep-dives/system-design/caching-strategies.md`
8. `docs/deep-dives/system-design/queueing-and-async-processing.md`
9. `docs/deep-dives/system-design/api-design-and-gateways.md`
10. `docs/deep-dives/system-design/security-and-compliance.md`
11. `docs/deep-dives/system-design/observability-and-slos.md`
12. `docs/deep-dives/system-design/resilience-and-failure-handling.md`
13. `docs/deep-dives/system-design/multi-region-and-disaster-recovery.md`
14. `docs/deep-dives/system-design/cost-optimization.md`
15. `docs/deep-dives/system-design/mobile-backend-for-frontend.md`
16. `docs/deep-dives/system-design/real-time-systems.md`
17. `docs/deep-dives/system-design/search-and-indexing.md`
18. `docs/deep-dives/system-design/analytics-pipeline-design.md`
19. `docs/deep-dives/system-design/migration-and-evolution-strategies.md`
20. `docs/deep-dives/system-design/tradeoffs-and-decision-frameworks.md`

---

## Question-to-Deep-Dive Mapping

### 1. System Design Fundamentals
**File:** `docs/deep-dives/system-design/system-design-fundamentals.md`

**Questions (2):**
- `system-design`
- `design-round-structure`

---

### 2. Requirements And Scope
**File:** `docs/deep-dives/system-design/requirements-and-scope.md`

**Questions (2):**
- `functional-vs-nonfunctional-requirements`
- `scope-definition`

---

### 3. High Level Architecture
**File:** `docs/deep-dives/system-design/high-level-architecture.md`

**Questions (3):**
- `high-level-components`
- `service-boundaries`
- `load-balancing`

---

### 4. Data Modeling And Storage
**File:** `docs/deep-dives/system-design/data-modeling-and-storage.md`

**Questions (2):**
- `data-modeling`
- `sql-vs-nosql`

---

### 5. Consistency And Transactions
**File:** `docs/deep-dives/system-design/consistency-and-transactions.md`

**Questions (2):**
- `consistency-models`
- `transactions-and-sagas`

---

### 6. Scalability And Capacity Planning
**File:** `docs/deep-dives/system-design/scalability-and-capacity-planning.md`

**Questions (2):**
- `estimations`
- `horizontal-scaling`

---

### 7. Caching Strategies
**File:** `docs/deep-dives/system-design/caching-strategies.md`

**Questions (2):**
- `cache-aside`
- `cache-invalidation`

---

### 8. Queueing And Async Processing
**File:** `docs/deep-dives/system-design/queueing-and-async-processing.md`

**Questions (3):**
- `message-queues`
- `event-driven-design`
- `backpressure-in-systems`

---

### 9. Api Design And Gateways
**File:** `docs/deep-dives/system-design/api-design-and-gateways.md`

**Questions (4):**
- `api-gateway`
- `rest-vs-grpc-design`
- `versioning-strategy`
- `rate-limiting`

---

### 10. Security And Compliance
**File:** `docs/deep-dives/system-design/security-and-compliance.md`

**Questions (4):**
- `authn-vs-authz`
- `security-hardening`
- `tenant-isolation`
- `data-retention`

---

### 11. Observability And Slos
**File:** `docs/deep-dives/system-design/observability-and-slos.md`

**Questions (2):**
- `slos-and-slas`
- `logging-metrics-tracing`

---

### 12. Resilience And Failure Handling
**File:** `docs/deep-dives/system-design/resilience-and-failure-handling.md`

**Questions (3):**
- `circuit-breaker`
- `bulkheads-and-timeouts`
- `idempotency`

---

### 13. Multi Region And Disaster Recovery
**File:** `docs/deep-dives/system-design/multi-region-and-disaster-recovery.md`

**Questions (2):**
- `multi-region`
- `disaster-recovery-rpo-rto`

---

### 14. Cost Optimization
**File:** `docs/deep-dives/system-design/cost-optimization.md`

**Questions (2):**
- `cost-vs-latency`
- `capacity-headroom`

---

### 15. Mobile Backend For Frontend
**File:** `docs/deep-dives/system-design/mobile-backend-for-frontend.md`

**Questions (2):**
- `bff-pattern`
- `edge-caching-mobile`

---

### 16. Real Time Systems
**File:** `docs/deep-dives/system-design/real-time-systems.md`

**Questions (2):**
- `realtime-chat-design`
- `fanout-problem`

---

### 17. Search And Indexing
**File:** `docs/deep-dives/system-design/search-and-indexing.md`

**Questions (3):**
- `indexing-strategy`
- `search-architecture`
- `eventual-consistency-search`

---

### 18. Analytics Pipeline Design
**File:** `docs/deep-dives/system-design/analytics-pipeline-design.md`

**Questions (2):**
- `analytics-pipeline`
- `batch-vs-stream`

---

### 19. Migration And Evolution Strategies
**File:** `docs/deep-dives/system-design/migration-and-evolution-strategies.md`

**Questions (2):**
- `migration-strangler`
- `schema-evolution`

---

### 20. Tradeoffs And Decision Frameworks
**File:** `docs/deep-dives/system-design/tradeoffs-and-decision-frameworks.md`

**Questions (4):**
- `tradeoff-framework`
- `cap-theorem-practical`
- `read-heavy-vs-write-heavy`
- `availability-vs-consistency`

---

## Summary

- **Total System Design Questions:** 50
- **Total Shared Deep Dives:** 20
- **Audience:** mid, senior, and staff Android interviews
- **Design Goal:** concise YAML revision answers + deep practical coverage
