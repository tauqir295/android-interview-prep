# Deep Dive Mapping & Architecture
## Overview
This document tracks the active deep-dive mapping for the Android Interview Prep docs system.
Current state:
- Fundamentals mapping: complete
- Kotlin mapping: complete
- Compose mapping: complete
- Deep dive files for fundamentals and Kotlin: created
---
## Mapping Documents
Use these as the source of truth:
- `DEEP_DIVE_MAPPING.md` (this file, fundamentals + architecture status)
- `KOTLIN_DEEP_DIVE_MAPPING.md` (full Kotlin mapping)
- `COMPOSE_DEEP_DIVE_MAPPING.md` (full Compose mapping)
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
| Fundamentals deep dives | ✅ complete |
| Kotlin deep dives | ✅ complete |
| Compose mapping doc | ✅ complete |
| Generated docs pages | ✅ generated |
| Combined question index (`ALL_QUESTIONS.md`) | ✅ updated |
---
## Next Step
Continue adding new categories with the same architecture:
- concise YAML revision answers
- shared deep dives for depth
- route-style links and anchor-based navigation
