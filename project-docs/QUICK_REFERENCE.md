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
✅ Cicd questions: 50 (20 deep dives)
✅ Advanced questions: 50 (20 deep dives)
✅ Future Tech questions: 50 (20 deep dives)
✅ System Design questions: 50 (20 deep dives)
✅ Testing questions: 50 (20 deep dives)
✅ Behavioral questions: 50 (20 deep dives)
✅ Total questions: 631
✅ Total deep dive topics: 261
✅ Active categories with deep dives: 13
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
- `docs/deep-dives/cicd/` (20 files)
- `docs/deep-dives/advanced/` (20 files)
- `docs/deep-dives/future-tech/` (20 files)
- `docs/deep-dives/system-design/` (20 files)
- `docs/deep-dives/testing/` (20 files)
- `docs/deep-dives/behavioral/` (20 files)
Purpose:
- detailed internals and tradeoffs
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
## Category Status
- Fundamentals: `data/fundamentals.yaml` -> `docs/generated/fundamentals.md`
- Kotlin: `data/kotlin.yaml` -> `docs/generated/kotlin.md`
- Compose: `data/compose.yaml` -> `docs/generated/compose.md`
- Concurrency: `data/concurrency.yaml` -> `docs/generated/concurrency.md`
- Architecture: `data/architecture.yaml` -> `docs/generated/architecture.md`
- Networking: `data/networking.yaml` -> `docs/generated/networking.md`
- Performance: `data/performance.yaml` -> `docs/generated/performance.md`
- Cicd: `data/cicd.yaml` -> `docs/generated/cicd.md`
- Advanced: `data/advanced.yaml` -> `docs/generated/advanced.md`
- Future Tech: `data/future-tech.yaml` -> `docs/generated/future-tech.md`
- System Design: `data/system-design.yaml` -> `docs/generated/system-design.md`
- Testing: `data/testing.yaml` -> `docs/generated/testing.md`
- Behavioral: `data/behavioral.yaml` -> `docs/generated/behavioral.md`

## Mapping Documents
- `project-docs/DEEP_DIVE_MAPPING.md`
- `project-docs/KOTLIN_DEEP_DIVE_MAPPING.md`
- `project-docs/COMPOSE_DEEP_DIVE_MAPPING.md`
- `project-docs/CONCURRENCY_DEEP_DIVE_MAPPING.md`
- `project-docs/ARCHITECTURE_DEEP_DIVE_MAPPING.md`
- `project-docs/NETWORKING_DEEP_DIVE_MAPPING.md`
- `project-docs/PERFORMANCE_DEEP_DIVE_MAPPING.md`
- `project-docs/CICD_DEEP_DIVE_MAPPING.md`
- `project-docs/ADVANCED_DEEP_DIVE_MAPPING.md`
- `project-docs/FUTURE_TECH_DEEP_DIVE_MAPPING.md`
- `project-docs/SYSTEM_DESIGN_DEEP_DIVE_MAPPING.md`
- `project-docs/TESTING_DEEP_DIVE_MAPPING.md`
- `project-docs/BEHAVIORAL_DEEP_DIVE_MAPPING.md`
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
- YAML remains concise and interview-focused
- Deep details are in markdown deep dives
- Rendering is aligned with MkDocs Material templates
- Deep dives use hash-aware back-navigation
- Combined index is generated from YAML by script
