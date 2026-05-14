# Testing Deep Dive Mapping & Architecture

## Overview

This document maps Testing interview questions to shared deep dives.
It keeps `data/testing.yaml` concise while deep implementation detail lives in markdown.

---

## Recommended Deep Dive Files

1. `docs/deep-dives/testing/testing-fundamentals.md`
2. `docs/deep-dives/testing/test-pyramid-and-strategy.md`
3. `docs/deep-dives/testing/unit-testing-viewmodel.md`
4. `docs/deep-dives/testing/repository-and-data-layer-testing.md`
5. `docs/deep-dives/testing/integration-testing.md`
6. `docs/deep-dives/testing/ui-testing-with-compose.md`
7. `docs/deep-dives/testing/espresso-and-ui-automation.md`
8. `docs/deep-dives/testing/mocking-fakes-and-stubs.md`
9. `docs/deep-dives/testing/coroutine-and-flow-testing.md`
10. `docs/deep-dives/testing/stateflow-sharedflow-testing.md`
11. `docs/deep-dives/testing/network-testing-and-mockwebserver.md`
12. `docs/deep-dives/testing/database-testing-room.md`
13. `docs/deep-dives/testing/testability-and-architecture.md`
14. `docs/deep-dives/testing/flaky-test-diagnostics.md`
15. `docs/deep-dives/testing/performance-and-benchmark-testing.md`
16. `docs/deep-dives/testing/snapshot-and-golden-testing.md`
17. `docs/deep-dives/testing/contract-testing.md`
18. `docs/deep-dives/testing/e2e-testing-and-release-gates.md`
19. `docs/deep-dives/testing/ci-cd-test-pipelines.md`
20. `docs/deep-dives/testing/test-metrics-and-quality-governance.md`

---

## Question-to-Deep-Dive Mapping

### 1. Testing Fundamentals
**File:** `docs/deep-dives/testing/testing-fundamentals.md`

**Questions (2):**
- `testing-strategy`
- `qa-dev-collaboration`

---

### 2. Test Pyramid And Strategy
**File:** `docs/deep-dives/testing/test-pyramid-and-strategy.md`

**Questions (4):**
- `test-pyramid`
- `unit-vs-integration`
- `hermetic-tests`
- `risk-based-testing`

---

### 3. Unit Testing Viewmodel
**File:** `docs/deep-dives/testing/unit-testing-viewmodel.md`

**Questions (3):**
- `viewmodel-unit-tests`
- `usecase-tests`
- `clock-abstraction`

---

### 4. Repository And Data Layer Testing
**File:** `docs/deep-dives/testing/repository-and-data-layer-testing.md`

**Questions (2):**
- `repository-tests`
- `datasource-tests`

---

### 5. Integration Testing
**File:** `docs/deep-dives/testing/integration-testing.md`

**Questions (1):**
- `integration-boundary`

---

### 6. Ui Testing With Compose
**File:** `docs/deep-dives/testing/ui-testing-with-compose.md`

**Questions (2):**
- `compose-ui-tests`
- `semantics-testing`

---

### 7. Espresso And Ui Automation
**File:** `docs/deep-dives/testing/espresso-and-ui-automation.md`

**Questions (3):**
- `espresso-basics`
- `idling-resources`
- `android-test-runner`

---

### 8. Mocking Fakes And Stubs
**File:** `docs/deep-dives/testing/mocking-fakes-and-stubs.md`

**Questions (3):**
- `mocks-vs-fakes`
- `stub-vs-spy`
- `test-data-builders`

---

### 9. Coroutine And Flow Testing
**File:** `docs/deep-dives/testing/coroutine-and-flow-testing.md`

**Questions (3):**
- `coroutine-test`
- `virtual-time`
- `flow-test-patterns`

---

### 10. Stateflow Sharedflow Testing
**File:** `docs/deep-dives/testing/stateflow-sharedflow-testing.md`

**Questions (2):**
- `stateflow-testing`
- `sharedflow-events-testing`

---

### 11. Network Testing And Mockwebserver
**File:** `docs/deep-dives/testing/network-testing-and-mockwebserver.md`

**Questions (1):**
- `mockwebserver`

---

### 12. Database Testing Room
**File:** `docs/deep-dives/testing/database-testing-room.md`

**Questions (2):**
- `room-inmemory-tests`
- `migration-tests`

---

### 13. Testability And Architecture
**File:** `docs/deep-dives/testing/testability-and-architecture.md`

**Questions (3):**
- `testable-architecture`
- `dependency-injection-testing`
- `test-maintenance-cost`

---

### 14. Flaky Test Diagnostics
**File:** `docs/deep-dives/testing/flaky-test-diagnostics.md`

**Questions (3):**
- `flaky-tests`
- `stabilize-ui-tests`
- `retry-in-tests`

---

### 15. Performance And Benchmark Testing
**File:** `docs/deep-dives/testing/performance-and-benchmark-testing.md`

**Questions (2):**
- `benchmark-tests`
- `macrobenchmark`

---

### 16. Snapshot And Golden Testing
**File:** `docs/deep-dives/testing/snapshot-and-golden-testing.md`

**Questions (2):**
- `golden-tests`
- `visual-regression`

---

### 17. Contract Testing
**File:** `docs/deep-dives/testing/contract-testing.md`

**Questions (3):**
- `api-contract-tests`
- `consumer-contract`
- `contract-mocks`

---

### 18. E2E Testing And Release Gates
**File:** `docs/deep-dives/testing/e2e-testing-and-release-gates.md`

**Questions (2):**
- `e2e-tests`
- `release-gates`

---

### 19. Ci Cd Test Pipelines
**File:** `docs/deep-dives/testing/ci-cd-test-pipelines.md`

**Questions (3):**
- `ci-pipeline`
- `sharding-tests`
- `test-environments`

---

### 20. Test Metrics And Quality Governance
**File:** `docs/deep-dives/testing/test-metrics-and-quality-governance.md`

**Questions (4):**
- `test-reporting`
- `quality-gates`
- `mutation-testing`
- `postmortem-regression-tests`

---

## Summary

- **Total Testing Questions:** 50
- **Total Shared Deep Dives:** 20
- **Audience:** mid, senior, and staff Android interviews
- **Design Goal:** concise YAML revision answers + deep practical coverage
