# Quick Reference: Interview Prep Content Status
## Current Project Snapshot
```
✅ Architecture questions: 50 (20 deep dives)
✅ Compose questions: 50 (20 deep dives)
✅ Concurrency questions: 50 (20 deep dives)
✅ Kotlin questions: 51 (20 deep dives)
✅ Networking questions: 38 (20 deep dives)
✅ Performance questions: 38 (20 deep dives)
✅ Total questions: 286
✅ Total deep dive topics: 120
✅ Active categories with deep dives: 6
✅ Generated docs pages: 13 categories
```
---
## Content Layers
### 1) Generated Question Pages (YAML -> Markdown)
- `data/*.yaml` (5 active: architecture, compose, concurrency, kotlin, networking)
- `docs/generated/*.md` (13 category pages)
Purpose:
- concise interview answers
- fast revision
- deep-dive linking
### 2) Deep Dive Markdown Pages
- `docs/deep-dives/architecture/` (20 files)
- `docs/deep-dives/compose/` (20 files)
- `docs/deep-dives/concurrency/` (20 files)
- `docs/deep-dives/kotlin/` (20 files)
- `docs/deep-dives/networking/` (20 files)
- `docs/deep-dives/performance/` (20 files)
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
- Questions: **54** (legacy, no deep dives)
- File: `data/fundamentals.yaml`
- Generated page: `docs/generated/fundamentals.md`

## Kotlin Status
- Questions: **51**
- Deep dives: **20**
- File: `data/kotlin.yaml`
- Generated page: `docs/generated/kotlin.md`
Deep dives in place under:
`docs/deep-dives/kotlin/`

## Compose Status
- Questions: **50**
- Deep dives: **20**
- File: `data/compose.yaml`
- Generated page: `docs/generated/compose.md`
Deep dives in place under:
`docs/deep-dives/compose/`
- Top 5: fully authored
- Remaining 15: scaffolded with core content

## Concurrency Status
- Questions: **50**
- Deep dives: **20**
- File: `data/concurrency.yaml`
- Generated page: `docs/generated/concurrency.md`
Deep dives in place under:
`docs/deep-dives/concurrency/`
- All 20: fully authored

## Architecture Status
- Questions: **50**
- Deep dives: **20**
- File: `data/architecture.yaml`
- Generated page: `docs/generated/architecture.md`
Deep dives in place under:
`docs/deep-dives/architecture/`
- Top 5: fully authored
- Remaining 15: scaffolded with core content

## Networking Status
- Questions: **38**
- Deep dives: **20**
- File: `data/networking.yaml`
- Generated page: `docs/generated/networking.md`
Deep dives in place under:
`docs/deep-dives/networking/`
- Top 5: fully authored
- Remaining 15: scaffolded with core content

## Performance Status
- Questions: **38**
- Deep dives: **20**
- File: `data/performance.yaml`
- Generated page: `docs/generated/performance.md`
Deep dives in place under:
`docs/deep-dives/performance/`
- Top 5: fully authored
- Remaining 15: scaffolded with core content

## Mapping Documents
- `DEEP_DIVE_MAPPING.md` (architecture status)
- `KOTLIN_DEEP_DIVE_MAPPING.md` (Kotlin mapping)
- `COMPOSE_DEEP_DIVE_MAPPING.md` (Compose mapping)
- `CONCURRENCY_DEEP_DIVE_MAPPING.md` (Concurrency mapping)
- `ARCHITECTURE_DEEP_DIVE_MAPPING.md` (Architecture mapping)
- `NETWORKING_DEEP_DIVE_MAPPING.md` (Networking mapping)
- `PERFORMANCE_DEEP_DIVE_MAPPING.md` (Performance mapping)
- `ALL_QUESTIONS.md` (consolidated index)
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
- YAML remains concise and interview-focused (under 25 lines per answer)
- Deep details are in markdown deep dives
- Formatted consistently for MkDocs Material rendering
- All 100 deep dives include hash-aware back-navigation
- Material UI card styling applied globally
---

## Next Recommended Work
1. Complete authoring for remaining 10 Compose/Architecture/Networking/Performance scaffolded deep dives.
2. Add new categories (System Design, Testing, Behavioral) with same 2-layer architecture.
3. Enhance existing Fundamentals with deep dives (currently no deep-dive set).
4. Create cross-category search/tagging system for discovery.
5. Add interview scenario builders leveraging existing Q&A.
