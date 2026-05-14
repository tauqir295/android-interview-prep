# Quick Reference: Interview Prep Content Status
## Current Project Snapshot
```
✅ Fundamentals questions: 54 (21 deep dives)
✅ Kotlin questions: 51 (20 deep dives)
✅ Compose questions: 50 (20 deep dives)
✅ Concurrency questions: 50 (20 deep dives)
✅ Architecture questions: 50 (20 deep dives)
✅ Networking questions: 38 (20 deep dives)
✅ Performance questions: 38 (20 deep dives)
✅ System Design questions: 50 (20 deep dives)
✅ Testing questions: 50 (20 deep dives)
✅ Behavioral questions: 50 (20 deep dives)
✅ Total questions: 481
✅ Total deep dive topics: 201
✅ Active categories with deep dives: 10
✅ Generated docs pages: 13 categories
```
---
## Content Layers
### 1) Generated Question Pages (YAML -> Markdown)
- `data/*.yaml`
- `docs/generated/*.md`
Purpose:
- concise interview answers
- fast revision
- deep-dive linking
### 2) Deep Dive Markdown Pages
- `docs/deep-dives/fundamentals/` (21 files)
- `docs/deep-dives/kotlin/` (20 files)
- `docs/deep-dives/compose/` (20 files)
- `docs/deep-dives/concurrency/` (20 files)
- `docs/deep-dives/architecture/` (20 files)
- `docs/deep-dives/networking/` (20 files)
- `docs/deep-dives/performance/` (20 files)
- `docs/deep-dives/system-design/` (20 files)
- `docs/deep-dives/testing/` (20 files)
- `docs/deep-dives/behavioral/` (20 files)
Purpose:
- detailed internals
- production insights
- interviewer traps
- advanced follow-ups
---
## Route Convention (Current Standard)
Use site routes in YAML deep-dive links:
```yaml
deep_dive: /android-interview-prep/deep-dives/fundamentals/activity-lifecycle/
```
Do not use file-system style links like:
```text
/docs/deep-dives/fundamentals/activity-lifecycle.md
```
---
## Navigation Behavior
Implemented behavior:
- generated question pages include stable anchors per question ID
- deep-dive links include `#question-id`
- deep-dive back links return to generated page with the same anchor
- question lists are collapsed by default
- matching question auto-opens on return from deep dive
---
## Fundamentals Status
- Questions: **54**
- Deep dives: **21**
- File: `data/fundamentals.yaml`
- Generated page: `docs/generated/fundamentals.md`
Deep dives in place under: `docs/deep-dives/fundamentals/`

## Kotlin Status
- Questions: **51**
- Deep dives: **20**
- File: `data/kotlin.yaml`
- Generated page: `docs/generated/kotlin.md`
Deep dives in place under: `docs/deep-dives/kotlin/`

## Compose Status
- Questions: **50**
- Deep dives: **20**
- File: `data/compose.yaml`
- Generated page: `docs/generated/compose.md`
Deep dives in place under: `docs/deep-dives/compose/`

## Concurrency Status
- Questions: **50**
- Deep dives: **20**
- File: `data/concurrency.yaml`
- Generated page: `docs/generated/concurrency.md`
Deep dives in place under: `docs/deep-dives/concurrency/`

## Architecture Status
- Questions: **50**
- Deep dives: **20**
- File: `data/architecture.yaml`
- Generated page: `docs/generated/architecture.md`
Deep dives in place under: `docs/deep-dives/architecture/`

## Networking Status
- Questions: **38**
- Deep dives: **20**
- File: `data/networking.yaml`
- Generated page: `docs/generated/networking.md`
Deep dives in place under: `docs/deep-dives/networking/`

## Performance Status
- Questions: **38**
- Deep dives: **20**
- File: `data/performance.yaml`
- Generated page: `docs/generated/performance.md`
Deep dives in place under: `docs/deep-dives/performance/`

## System Design Status
- Questions: **50**
- Deep dives: **20**
- File: `data/system-design.yaml`
- Generated page: `docs/generated/system-design.md`
Deep dives in place under: `docs/deep-dives/system-design/`

## Testing Status
- Questions: **50**
- Deep dives: **20**
- File: `data/testing.yaml`
- Generated page: `docs/generated/testing.md`
Deep dives in place under: `docs/deep-dives/testing/`

## Behavioral Status
- Questions: **50**
- Deep dives: **20**
- File: `data/behavioral.yaml`
- Generated page: `docs/generated/behavioral.md`
Deep dives in place under: `docs/deep-dives/behavioral/`

## Mapping Documents
- `DEEP_DIVE_MAPPING.md`
- `KOTLIN_DEEP_DIVE_MAPPING.md`
- `COMPOSE_DEEP_DIVE_MAPPING.md`
- `CONCURRENCY_DEEP_DIVE_MAPPING.md`
- `ARCHITECTURE_DEEP_DIVE_MAPPING.md`
- `NETWORKING_DEEP_DIVE_MAPPING.md`
- `PERFORMANCE_DEEP_DIVE_MAPPING.md`
- `SYSTEM_DESIGN_DEEP_DIVE_MAPPING.md`
- `TESTING_DEEP_DIVE_MAPPING.md`
- `BEHAVIORAL_DEEP_DIVE_MAPPING.md`
- `project-docs/ALL_QUESTIONS.md` (consolidated index)
---
## Build/Generate Commands
```bash
cd /home/mta/AndroidStudioProjects/android-interview-prep
python3 scripts/generate_docs.py
```
Optional site build:
```bash
cd /home/mta/AndroidStudioProjects/android-interview-prep
mkdocs build
```
---
## Quality Notes
- YAML remains concise and interview-focused (under ~25 lines per answer)
- Deep details are in markdown deep dives
- Formatted consistently for MkDocs Material rendering
- Deep dives include hash-aware back-navigation
- Material UI card styling applied globally

## Next Recommended Work
1. Finish full authoring pass for any scaffold-style deep dives.
2. Keep new categories on the same 2-layer architecture.
3. Keep `project-docs/ALL_QUESTIONS.md` generated from YAML only.
4. Add lint checks for deep-dive back-navigation snippet presence.
