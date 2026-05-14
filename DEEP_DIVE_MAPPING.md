# Deep Dive Mapping & Architecture
## Overview
This document tracks the active deep-dive mapping for the Android Interview Prep docs system.
Current state:
- Fundamentals mapping: complete
- Kotlin mapping: complete
- Compose mapping: complete
- Concurrency mapping: complete
- Architecture mapping: complete
- Deep dive files for fundamentals, Kotlin, Compose, Concurrency, and Architecture: created
---
## Mapping Documents
Use these as the source of truth:
- `DEEP_DIVE_MAPPING.md` (this file, fundamentals + architecture status)
- `KOTLIN_DEEP_DIVE_MAPPING.md` (full Kotlin mapping)
- `COMPOSE_DEEP_DIVE_MAPPING.md` (full Compose mapping)
- `CONCURRENCY_DEEP_DIVE_MAPPING.md` (full Concurrency mapping)
- `ARCHITECTURE_DEEP_DIVE_MAPPING.md` (full Architecture mapping)
---
## Fundamentals Mapping
### Files and Question Coverage
| Deep Dive File | Questions |
|---|---:|
| `docs/deep-dives/fundamentals/activity-lifecycle.md` | 6 |
| `docs/deep-dives/fundamentals/intents.md` | 5 |
| `docs/deep-dives/fundamentals/fragments.md` | 5 |
| `docs/deep-dives/fundamentals/context.md` | 4 |
| `docs/deep-dives/fundamentals/memory-leaks.md` | 4 |
| `docs/deep-dives/fundamentals/anr-and-performance.md` | 4 |
| `docs/deep-dives/fundamentals/looper-and-handler.md` | 4 |
| `docs/deep-dives/fundamentals/services.md` | 4 |
| `docs/deep-dives/fundamentals/broadcast-receivers.md` | 3 |
| `docs/deep-dives/fundamentals/permissions.md` | 3 |
| `docs/deep-dives/fundamentals/androidmanifest.md` | 2 |
| `docs/deep-dives/fundamentals/binder-ipc.md` | 1 |
| `docs/deep-dives/fundamentals/zygote-process-creation.md` | 1 |
| `docs/deep-dives/fundamentals/art-vs-dalvik.md` | 1 |
| `docs/deep-dives/fundamentals/app-startup-flow.md` | 1 |
| `docs/deep-dives/fundamentals/recyclerview-efficiency.md` | 1 |
| `docs/deep-dives/fundamentals/rendering-pipeline.md` | 1 |
| `docs/deep-dives/fundamentals/storage-types.md` | 1 |
| `docs/deep-dives/fundamentals/task-and-backstack.md` | 1 |
| `docs/deep-dives/fundamentals/process-death-lifecycle.md` | 1 |
| `docs/deep-dives/fundamentals/multitasking-window-focus.md` | 1 |
**Total:** 54 fundamentals questions -> 21 fundamentals deep dives
---
## Kotlin Mapping
Kotlin mapping and per-topic sections are maintained in:
- `KOTLIN_DEEP_DIVE_MAPPING.md`
Kotlin deep-dive files currently present under `docs/deep-dives/kotlin/`:
1. `kotlin-basics.md`
2. `data-classes-and-generated-code.md`
3. `object-and-companion-objects.md`
4. `sealed-classes-and-enums.md`
5. `delegation-and-delegated-properties.md`
6. `extension-functions.md`
7. `scope-functions.md`
8. `higher-order-functions-and-lambdas.md`
9. `inline-functions.md`
10. `reified-generics.md`
11. `null-safety-and-smart-casts.md`
12. `generics-and-variance.md`
13. `collections-and-sequences.md`
14. `coroutines-foundations.md`
15. `dispatchers-and-coroutine-scope.md`
16. `structured-concurrency-and-jobs.md`
17. `cancellation-and-exception-handling.md`
18. `flow-fundamentals.md`
19. `stateflow-sharedflow-and-channels.md`
20. `jvm-interop-and-bytecode.md`
**Total:** 51 Kotlin questions -> 20 Kotlin deep dives
---
## Compose Mapping
Compose mapping and per-topic sections are maintained in:
- `COMPOSE_DEEP_DIVE_MAPPING.md`

Compose deep-dive files are planned under `docs/deep-dives/compose/`:
1. `compose-basics-and-composable-contract.md`
2. `state-and-remember.md`
3. `state-hoisting-and-udf.md`
4. `recomposition-and-skip-optimization.md`
5. `snapshot-system-and-observation.md`
6. `side-effects-overview.md`
7. `effects-coroutines-and-lifecycle.md`
8. `derived-state-and-remember-updated-state.md`
9. `compositionlocal-and-context-propagation.md`
10. `flow-integration-with-compose.md`
11. `stability-and-compose-compiler.md`
12. `slot-table-and-runtime-internals.md`
13. `composer-applier-and-runtime-phases.md`
14. `modifier-chain-and-node-graph.md`
15. `layout-measure-draw-pipeline.md`
16. `lazy-layouts-and-list-performance.md`
17. `navigation-in-compose.md`
18. `theming-and-material3.md`
19. `animation-in-compose.md`
20. `testing-interop-and-performance.md`

**Total:** 50 Compose questions -> 20 Compose deep dives
---
## Concurrency Mapping
Concurrency mapping and per-topic sections are maintained in:
- `CONCURRENCY_DEEP_DIVE_MAPPING.md`

Concurrency deep-dive files currently present under `docs/deep-dives/concurrency/`:
1. `coroutine-internals.md`
2. `threads-dispatchers-context.md`
3. `structured-scope-and-jobs.md`
4. `cancellation-exception-supervision.md`
5. `launch-async-parallelism.md`
6. `scheduler-thread-pools.md`
7. `parallelism-and-scheduling.md`
8. `flow-fundamentals.md`
9. `flow-operators-and-backpressure.md`
10. `stateflow-sharedflow-and-channels.md`
11. `flow-sharing-and-hot-streams.md`
12. `callbackflow-and-channelflow.md`
13. `synchronization-and-mutex.md`
14. `shared-state-and-race-conditions.md`
15. `deadlocks-and-contention.md`
16. `coroutine-testing-and-virtual-time.md`
17. `coroutine-debugging-and-observability.md`
18. `android-lifecycle-and-flow-collection.md`
19. `android-lifecycle-and-main-safety.md`
20. `production-concurrency-patterns-and-tuning.md`

**Total:** 50 Concurrency questions -> 20 Concurrency deep dives
---
## Architecture Mapping
Architecture mapping and per-topic sections are maintained in:
- `ARCHITECTURE_DEEP_DIVE_MAPPING.md`

Architecture deep-dive files currently present under `docs/deep-dives/architecture/`:
1. `mvvm-and-viewmodel.md`
2. `mvi-and-udf.md`
3. `clean-architecture-layering.md`
4. `repository-pattern-and-data-sources.md`
5. `use-cases-and-domain-layer.md`
6. `dependency-injection-strategies.md`
7. `hilt-in-production.md`
8. `dagger-and-component-graph.md`
9. `service-locator-and-anti-patterns.md`
10. `modularization-strategies.md`
11. `feature-modules-and-boundaries.md`
12. `state-management-and-ssot.md`
13. `offline-first-and-sync.md`
14. `caching-and-pagination-architecture.md`
15. `reactive-architecture-with-flows.md`
16. `ui-state-and-event-modeling.md`
17. `navigation-and-deep-link-architecture.md`
18. `testing-architecture-and-testability.md`
19. `scalability-and-team-topologies.md`
20. `production-tradeoffs-and-decision-making.md`

**Total:** 50 Architecture questions -> 20 Architecture deep dives
---
## Networking Mapping
Networking mapping and per-topic sections are maintained in:
- `NETWORKING_DEEP_DIVE_MAPPING.md`

Networking deep-dive files currently present under `docs/deep-dives/networking/`:
1. `networking-basics.md`
2. `http-and-https.md`
3. `rest-and-soap.md`
4. `graphql-basics.md`
5. `websockets-and-long-polling.md`
6. `caching-and-persistence.md`
7. `retrofit-and-okhttp.md`
8. `coroutines-and-networking.md`
9. `error-handling-and-retry.md`
10. `security-and-authentication.md`
11. `performance-optimization.md`
12. `testing-networking.md`
13. `mocking-and-stubbing.md`
14. `networking-in-compose.md`
15. `advanced-retrofit-features.md`
16. `okhttp-interceptors-and-logging.md`
17. `graphql-advanced-features.md`
18. `websocket-advanced-usage.md`
19. `networking-best-practices.md`
20. `production-networking-patterns.md`

**Total:** 50 Networking questions -> 20 Networking deep dives
---
## Link Convention (Important)
Use site route links in YAML:
```yaml
deep_dive: /android-interview-prep/deep-dives/fundamentals/activity-lifecycle/
```
Do not use old filesystem-style links:
```text
/docs/deep-dives/fundamentals/activity-lifecycle.md
```
---
## Rendering and Generation Rules
- Keep YAML answers concise (revision-sheet style).
- Put large explanations in deep dives only.
- Fix formatting issues in YAML source, not generated markdown files.
- Regenerate with `scripts/generate_docs.py` after any YAML/template change.
---
## Deep Dive Scaffold Template
Use the reusable deep-dive template to avoid navigation regressions:
- Template: `templates/deep-dive.md.j2`
- Scaffold script: `scripts/scaffold_deep_dive.py`

Example:
```bash
python3 scripts/scaffold_deep_dive.py \
  --category compose \
  --category-title Compose \
  --topic-slug recomposition-and-skip-optimization \
  --topic-title "Recomposition and Skip Optimization"
```

This scaffold includes the hash/referrer-aware `back-to-questions` link block
so deep dives return to the correct question anchor.
---
## Navigation Rules
Implemented globally:
- generated question anchors by `id`
- deep-dive links include `#question-id`
- deep-dive back link returns to matching question anchor
- generated question blocks collapsed by default
- target question auto-opens on hash return
---
## Status
| Area | Status |
|---|---|
| Fundamentals YAML | ✅ complete |
| Kotlin YAML | ✅ complete |
| Compose YAML | ✅ complete |
| Concurrency YAML | ✅ complete |
| Architecture YAML | ✅ complete |
| Networking YAML | ✅ complete |
| Performance YAML | ✅ complete |
| Fundamentals deep dives | ✅ complete |
| Kotlin deep dives | ✅ complete |
| Compose mapping doc | ✅ complete |
| Concurrency mapping doc | ✅ complete |
| Architecture mapping doc | ✅ complete |
| Networking mapping doc | ✅ complete |
| Performance mapping doc | ✅ complete |
| Generated docs pages | ✅ generated |
| Combined question index (`ALL_QUESTIONS.md`) | ✅ updated |
---
## Next Step
Continue adding new categories with the same architecture:
- concise YAML revision answers
- shared deep dives for depth
- route-style links and anchor-based navigation
