# Quick Reference: Interview Prep Content Status
## Current Project Snapshot
```
✅ Fundamentals questions: 54
✅ Kotlin questions: 51
✅ Total questions: 105
✅ Fundamentals deep dives: 21 (created)
✅ Kotlin deep dives: 20 (created)
✅ Total deep dive topics: 41
✅ Generated docs pages: 13 categories
```
---
## Content Layers
### 1) Generated Question Pages (YAML -> Markdown)
- `data/fundamentals.yaml`
- `data/kotlin.yaml`
- `docs/generated/fundamentals.md`
- `docs/generated/kotlin.md`
Purpose:
- concise interview answers
- fast revision
- deep-dive linking
### 2) Deep Dive Markdown Pages
- `docs/deep-dives/fundamentals/` (21 files)
- `docs/deep-dives/kotlin/` (20 files)
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
Deep dives in place under:
`docs/deep-dives/fundamentals/`
---
## Kotlin Status
- Questions: **51**
- Deep dives: **20**
- File: `data/kotlin.yaml`
- Generated page: `docs/generated/kotlin.md`
Deep dives in place under:
`docs/deep-dives/kotlin/`
---
## Mapping Documents
- `DEEP_DIVE_MAPPING.md` (Fundamentals mapping)
- `KOTLIN_DEEP_DIVE_MAPPING.md` (Kotlin mapping)
- `ALL_QUESTIONS.md` (combined list: fundamentals + kotlin)
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
- Formatting now avoids broken list rendering patterns
- Generated markdown is stable for MkDocs Material
---
## Next Recommended Work
1. Keep adding new categories with the same 2-layer architecture.
2. Maintain route-style deep-dive links in YAML.
3. Update `ALL_QUESTIONS.md` whenever new YAML questions are added.
4. Keep deep-dive headers/back-link pattern consistent across categories.
