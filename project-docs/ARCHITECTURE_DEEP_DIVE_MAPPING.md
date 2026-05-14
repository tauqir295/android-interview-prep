# Architecture Deep Dive Mapping & Architecture

## Overview

This document maps Android architecture interview questions to shared deep dives.
The goal is to keep `data/architecture.yaml` concise while placing layered design,
modularization, DI internals, and production tradeoffs into dedicated deep dives.

---

## Recommended Deep Dive Files

1. `docs/deep-dives/architecture/mvvm-and-viewmodel.md`
2. `docs/deep-dives/architecture/mvi-and-udf.md`
3. `docs/deep-dives/architecture/clean-architecture-layering.md`
4. `docs/deep-dives/architecture/repository-pattern-and-data-sources.md`
5. `docs/deep-dives/architecture/use-cases-and-domain-layer.md`
6. `docs/deep-dives/architecture/dependency-injection-strategies.md`
7. `docs/deep-dives/architecture/hilt-in-production.md`
8. `docs/deep-dives/architecture/dagger-and-component-graph.md`
9. `docs/deep-dives/architecture/service-locator-and-anti-patterns.md`
10. `docs/deep-dives/architecture/modularization-strategies.md`
11. `docs/deep-dives/architecture/feature-modules-and-boundaries.md`
12. `docs/deep-dives/architecture/state-management-and-ssot.md`
13. `docs/deep-dives/architecture/offline-first-and-sync.md`
14. `docs/deep-dives/architecture/caching-and-pagination-architecture.md`
15. `docs/deep-dives/architecture/reactive-architecture-with-flows.md`
16. `docs/deep-dives/architecture/ui-state-and-event-modeling.md`
17. `docs/deep-dives/architecture/navigation-and-deep-link-architecture.md`
18. `docs/deep-dives/architecture/testing-architecture-and-testability.md`
19. `docs/deep-dives/architecture/scalability-and-team-topologies.md`
20. `docs/deep-dives/architecture/production-tradeoffs-and-decision-making.md`

---

## Question-to-Deep-Dive Mapping

### 1. MVVM and ViewModel
**File:** `docs/deep-dives/architecture/mvvm-and-viewmodel.md`

**Questions (3):**
- `mvvm-basics`
- `viewmodel-role`
- `savedstatehandle-usage`

**Recommended sections:**
- Overview
- ViewModel responsibility boundaries
- lifecycle-aware state ownership
- SavedStateHandle guidance
- interview traps around "fat ViewModel"

---

### 2. MVI and UDF
**File:** `docs/deep-dives/architecture/mvi-and-udf.md`

**Questions (3):**
- `mvi-what-is`
- `mvi-vs-mvvm`
- `udf-principles`

**Recommended sections:**
- Overview
- intent/state/effect modeling
- reducers and deterministic transitions
- MVI vs MVVM tradeoffs
- production ceremony vs clarity discussion

---

### 3. Clean Architecture Layering
**File:** `docs/deep-dives/architecture/clean-architecture-layering.md`

**Questions (3):**
- `clean-architecture-overview`
- `layer-dependency-rule`
- `dependency-inversion-android`

**Recommended sections:**
- Overview
- dependency rule internals
- boundary contracts
- SOLID alignment
- pragmatic deviations in Android apps

---

### 4. Repository Pattern and Data Sources
**File:** `docs/deep-dives/architecture/repository-pattern-and-data-sources.md`

**Questions (3):**
- `repository-pattern-purpose`
- `repository-single-source-truth`
- `multiple-data-sources-orchestration`

**Recommended sections:**
- Overview
- data source orchestration patterns
- SSOT enforcement
- caching refresh policies
- failure and fallback behavior

---

### 5. Use Cases and Domain Layer
**File:** `docs/deep-dives/architecture/use-cases-and-domain-layer.md`

**Questions (3):**
- `use-case-purpose`
- `use-case-granularity`
- `domain-layer-when-to-add`

**Recommended sections:**
- Overview
- domain boundary heuristics
- use case composition
- granularity tradeoffs
- avoiding over-abstraction

---

### 6. Dependency Injection Strategies
**File:** `docs/deep-dives/architecture/dependency-injection-strategies.md`

**Questions (3):**
- `dependency-injection-what-why`
- `constructor-injection-vs-field-injection`
- `di-scope-management`

**Recommended sections:**
- Overview
- object graph design
- constructor injection defaults
- scope/lifecycle alignment
- test replacement strategy

---

### 7. Hilt in Production
**File:** `docs/deep-dives/architecture/hilt-in-production.md`

**Questions (2):**
- `hilt-benefits`
- `hilt-component-lifetimes`

**Recommended sections:**
- Overview
- Hilt component hierarchy
- scope pitfalls
- migration strategy from manual DI
- operational maintainability notes

---

### 8. Dagger and Component Graph
**File:** `docs/deep-dives/architecture/dagger-and-component-graph.md`

**Questions (3):**
- `dagger-vs-hilt`
- `dagger-component-subcomponent`
- `dagger-performance-tradeoffs`

**Recommended sections:**
- Overview
- graph composition patterns
- subcomponent vs component dependency
- build-time/runtime tradeoffs
- debugging large graph failures

---

### 9. Service Locator and Anti-Patterns
**File:** `docs/deep-dives/architecture/service-locator-and-anti-patterns.md`

**Questions (2):**
- `service-locator-what-is`
- `service-locator-vs-di`

**Recommended sections:**
- Overview
- explicit vs implicit dependency wiring
- anti-pattern signals
- migration from locator to DI
- interview edge cases

---

### 10. Modularization Strategies
**File:** `docs/deep-dives/architecture/modularization-strategies.md`

**Questions (3):**
- `modularization-why`
- `multi-module-architecture-shapes`
- `api-vs-implementation-modules`

**Recommended sections:**
- Overview
- module shape options
- API surface governance
- build performance implications
- organizational alignment

---

### 11. Feature Modules and Boundaries
**File:** `docs/deep-dives/architecture/feature-modules-and-boundaries.md`

**Questions (3):**
- `feature-module-boundaries`
- `dynamic-feature-modules-when`
- `dependency-direction-between-modules`

**Recommended sections:**
- Overview
- feature boundary heuristics
- dependency direction rules
- dynamic feature adoption tradeoffs
- release strategy considerations

---

### 12. State Management and SSOT
**File:** `docs/deep-dives/architecture/state-management-and-ssot.md`

**Questions (3):**
- `state-management-android-architecture`
- `single-source-of-truth`
- `immutable-ui-state-models`

**Recommended sections:**
- Overview
- state ownership matrix
- immutable model patterns
- SSOT enforcement in repositories
- consistency and race-condition pitfalls

---

### 13. Offline-First and Sync
**File:** `docs/deep-dives/architecture/offline-first-and-sync.md`

**Questions (3):**
- `offline-first-principles`
- `sync-strategies-pull-push`
- `conflict-resolution-sync`

**Recommended sections:**
- Overview
- sync topology options
- write queue architecture
- conflict policies
- telemetry and operational safeguards

---

### 14. Caching and Pagination Architecture
**File:** `docs/deep-dives/architecture/caching-and-pagination-architecture.md`

**Questions (2):**
- `caching-strategies`
- `pagination-architecture`

**Recommended sections:**
- Overview
- cache hierarchy decisions
- pagination key and invalidation design
- stale data/freshness policy
- scalability and memory tradeoffs

---

### 15. Reactive Architecture with Flows
**File:** `docs/deep-dives/architecture/reactive-architecture-with-flows.md`

**Questions (2):**
- `stateflow-architecture`
- `event-handling-one-off-events`

**Recommended sections:**
- Overview
- state vs event stream modeling
- lifecycle-aware collection
- backpressure and throughput concerns
- correctness pitfalls with replay/buffering

---

### 16. UI State and Event Modeling
**File:** `docs/deep-dives/architecture/ui-state-and-event-modeling.md`

**Questions (3):**
- `error-handling-architecture`
- `retry-strategies-architecture`
- `ui-state-modeling-architecture`

**Recommended sections:**
- Overview
- UI state schemas
- error taxonomy and mapping
- retry/backoff design
- user experience resilience patterns

---

### 17. Navigation and Deep Link Architecture
**File:** `docs/deep-dives/architecture/navigation-and-deep-link-architecture.md`

**Questions (2):**
- `navigation-architecture`
- `deep-link-architecture`

**Recommended sections:**
- Overview
- route contract design
- deep link validation/security
- back stack ownership and testing
- modular navigation scaling patterns

---

### 18. Testing Architecture and Testability
**File:** `docs/deep-dives/architecture/testing-architecture-and-testability.md`

**Questions (1):**
- `architecture-testability`

**Recommended sections:**
- Overview
- test pyramid by layer
- deterministic state testing
- dependency replacement patterns
- long-term regression strategy

---

### 19. Scalability and Team Topologies
**File:** `docs/deep-dives/architecture/scalability-and-team-topologies.md`

**Questions (1):**
- `scaling-architecture-for-team`

**Recommended sections:**
- Overview
- code ownership and dependency boundaries
- communication topology impact
- release and integration workflows
- governance and platform team roles

---

### 20. Production Tradeoffs and Decision-Making
**File:** `docs/deep-dives/architecture/production-tradeoffs-and-decision-making.md`

**Questions (2):**
- `architecture-governance`
- `production-architecture-tradeoffs`

**Recommended sections:**
- Overview
- architecture decision records
- tradeoff framing method
- risk and mitigation planning
- measurable outcome reviews

---

## Summary

- **Total Architecture Questions:** 50
- **Total Shared Deep Dives:** 20
- **Audience:** mid, senior, and staff Android interviews
- **Design Goal:** concise YAML revision answers + deep architecture tradeoff coverage

