# Compose Deep Dive Mapping & Architecture

## Overview

This document maps Compose interview questions to shared deep dives.
The goal is to keep `data/compose.yaml` concise while placing runtime internals,
performance analysis, and architecture depth in dedicated markdown deep dives.

---

## Recommended Deep Dive Files

1. `docs/deep-dives/compose/compose-basics-and-composable-contract.md`
2. `docs/deep-dives/compose/state-and-remember.md`
3. `docs/deep-dives/compose/state-hoisting-and-udf.md`
4. `docs/deep-dives/compose/recomposition-and-skip-optimization.md`
5. `docs/deep-dives/compose/snapshot-system-and-observation.md`
6. `docs/deep-dives/compose/side-effects-overview.md`
7. `docs/deep-dives/compose/effects-coroutines-and-lifecycle.md`
8. `docs/deep-dives/compose/derived-state-and-remember-updated-state.md`
9. `docs/deep-dives/compose/compositionlocal-and-context-propagation.md`
10. `docs/deep-dives/compose/flow-integration-with-compose.md`
11. `docs/deep-dives/compose/stability-and-compose-compiler.md`
12. `docs/deep-dives/compose/slot-table-and-runtime-internals.md`
13. `docs/deep-dives/compose/composer-applier-and-runtime-phases.md`
14. `docs/deep-dives/compose/modifier-chain-and-node-graph.md`
15. `docs/deep-dives/compose/layout-measure-draw-pipeline.md`
16. `docs/deep-dives/compose/lazy-layouts-and-list-performance.md`
17. `docs/deep-dives/compose/navigation-in-compose.md`
18. `docs/deep-dives/compose/theming-and-material3.md`
19. `docs/deep-dives/compose/animation-in-compose.md`
20. `docs/deep-dives/compose/testing-interop-and-performance.md`

---

## Question-to-Deep-Dive Mapping

### 1. Compose Basics and Composable Contract
**File:** `docs/deep-dives/compose/compose-basics-and-composable-contract.md`

**Questions (4):**
- `compose-declarative-ui`
- `composable-function`
- `composable-lifecycle`
- `previews-in-compose`

**Recommended sections:**
- Overview
- Declarative model and mental shifts
- Composable function contract
- Composition lifecycle basics
- Preview tooling and caveats

---

### 2. State and Remember
**File:** `docs/deep-dives/compose/state-and-remember.md`

**Questions (3):**
- `mutable-state-in-compose`
- `remember-vs-rememberSaveable`
- `remember-key-parameter`

**Recommended sections:**
- Overview
- `MutableState` fundamentals
- `remember` and identity
- `rememberSaveable` and Saver model
- Key misuse pitfalls

---

### 3. State Hoisting and UDF
**File:** `docs/deep-dives/compose/state-hoisting-and-udf.md`

**Questions (4):**
- `state-hoisting`
- `unidirectional-data-flow-compose`
- `ui-state-modeling-compose`
- `event-handling-compose`

**Recommended sections:**
- Overview
- Stateless vs stateful composables
- UDF and screen architecture
- UI state modeling patterns
- Event contracts and anti-patterns

---

### 4. Recomposition and Skip Optimization
**File:** `docs/deep-dives/compose/recomposition-and-skip-optimization.md`

**Questions (6):**
- `recomposition-definition`
- `what-triggers-recomposition`
- `smart-recomposition`
- `skip-optimization`
- `unstable-parameter-recomposition`
- `prevent-unnecessary-recomposition`

**Recommended sections:**
- Overview
- Invalidation model
- Restart groups and skippability
- Stability-driven skip behavior
- Performance diagnostics and interview traps

---

### 5. Snapshot System and Observation
**File:** `docs/deep-dives/compose/snapshot-system-and-observation.md`

**Questions (2):**
- `snapshot-system`
- `snapshot-state-read-write`

**Recommended sections:**
- Overview
- Snapshot architecture
- Read/write tracking
- Atomic apply and conflict handling
- Threading constraints and pitfalls

---

### 6. Side Effects Overview
**File:** `docs/deep-dives/compose/side-effects-overview.md`

**Questions (3):**
- `side-effects-overview`
- `sideeffect-usage`
- `produceState-usage`

**Recommended sections:**
- Overview
- Why side-effect APIs exist
- Commit-phase effects
- State production patterns
- Common misuse patterns

---

### 7. Effects, Coroutines, and Lifecycle
**File:** `docs/deep-dives/compose/effects-coroutines-and-lifecycle.md`

**Questions (3):**
- `launchedeffect-usage`
- `disposableeffect-usage`
- `rememberCoroutineScope-usage`

**Recommended sections:**
- Overview
- Effect restart and key semantics
- Cleanup guarantees
- Composition-scoped coroutines
- Lifecycle interoperability

---

### 8. Derived State and rememberUpdatedState
**File:** `docs/deep-dives/compose/derived-state-and-remember-updated-state.md`

**Questions (2):**
- `derivedStateOf-purpose`
- `rememberUpdatedState-purpose`

**Recommended sections:**
- Overview
- Derived state memoization
- Stable callback capture in long-lived effects
- Performance tradeoffs and correctness traps

---

### 9. CompositionLocal and Context Propagation
**File:** `docs/deep-dives/compose/compositionlocal-and-context-propagation.md`

**Questions (1):**
- `compositionlocal-purpose`

**Recommended sections:**
- Overview
- Implicit dependency propagation
- Appropriate use cases
- Hidden dependency pitfalls
- Testing implications

---

### 10. Flow Integration with Compose
**File:** `docs/deep-dives/compose/flow-integration-with-compose.md`

**Questions (3):**
- `stateflow-with-compose`
- `collectAsState-vs-collectAsStateWithLifecycle`
- `snapshotFlow-usage`

**Recommended sections:**
- Overview
- StateFlow collection patterns
- Lifecycle-aware collection
- `snapshotFlow` bridging
- Backpressure and event/state modeling

---

### 11. Stability and Compose Compiler
**File:** `docs/deep-dives/compose/stability-and-compose-compiler.md`

**Questions (3):**
- `stability-in-compose`
- `stable-vs-immutable`
- `compose-compiler-role`

**Recommended sections:**
- Overview
- Stability inference model
- `@Stable` and `@Immutable` contracts
- Compiler transforms and generated groups
- Metrics-driven optimization workflow

---

### 12. Slot Table and Runtime Internals
**File:** `docs/deep-dives/compose/slot-table-and-runtime-internals.md`

**Questions (1):**
- `slot-table-purpose`

**Recommended sections:**
- Overview
- Slot table structure and groups
- Positional memoization
- Remember storage internals
- Runtime mutation constraints

---

### 13. Composer, Applier, and Runtime Phases
**File:** `docs/deep-dives/compose/composer-applier-and-runtime-phases.md`

**Questions (2):**
- `composer-and-applier`
- `compose-runtime-phases`

**Recommended sections:**
- Overview
- Composer responsibilities
- Applier contract
- Composition to apply flow
- Phase-level invalidation behavior

---

### 14. Modifier Chain and Node Graph
**File:** `docs/deep-dives/compose/modifier-chain-and-node-graph.md`

**Questions (1):**
- `modifier-chain-order`

**Recommended sections:**
- Overview
- Modifier ordering semantics
- Input/layout/draw interactions
- Node graph considerations
- Debugging modifier bugs

---

### 15. Layout, Measure, and Draw Pipeline
**File:** `docs/deep-dives/compose/layout-measure-draw-pipeline.md`

**Questions (2):**
- `custom-layout-basics`
- `measure-layout-draw-phases`

**Recommended sections:**
- Overview
- Constraints model
- Measure and placement internals
- Draw invalidation paths
- Custom layout pitfalls

---

### 16. Lazy Layouts and List Performance
**File:** `docs/deep-dives/compose/lazy-layouts-and-list-performance.md`

**Questions (2):**
- `lazycolumn-performance`
- `keys-in-lazycolumn`

**Recommended sections:**
- Overview
- Lazy list identity and reuse
- Key strategy and state retention
- Item-level recomposition control
- Jank and memory diagnostics

---

### 17. Navigation in Compose
**File:** `docs/deep-dives/compose/navigation-in-compose.md`

**Questions (2):**
- `navigation-compose-basics`
- `navigation-single-source-of-truth`

**Recommended sections:**
- Overview
- Route and argument contracts
- Back stack ownership
- Modular navigation architecture
- Deep links and testing concerns

---

### 18. Theming and Material 3
**File:** `docs/deep-dives/compose/theming-and-material3.md`

**Questions (1):**
- `theming-material3-compose`

**Recommended sections:**
- Overview
- Theme token layers
- Dynamic color strategy
- Design system integration
- Theming anti-patterns

---

### 19. Animation in Compose
**File:** `docs/deep-dives/compose/animation-in-compose.md`

**Questions (1):**
- `animations-compose`

**Recommended sections:**
- Overview
- API selection by complexity
- Transition orchestration
- Performance considerations
- Motion system interview discussions

---

### 20. Testing, Interop, and Performance
**File:** `docs/deep-dives/compose/testing-interop-and-performance.md`

**Questions (4):**
- `compose-testing-strategy`
- `semantics-and-test-tags`
- `androidview-interop`
- `compose-performance-checklist`

**Recommended sections:**
- Overview
- Compose testing architecture
- Semantics-first test design
- View interop migration patterns
- Production performance playbook

---

## Summary

- **Total Compose Questions:** 50
- **Total Shared Deep Dives:** 20
- **Audience:** mid, senior, and staff Android interviews
- **Design Goal:** concise generated answers + deep runtime and architecture coverage

