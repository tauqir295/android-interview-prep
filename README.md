# Android Interview Prep

Interview question bank and deep-dive notes for Android topics.

## Website

- Live docs: https://tauqir295.github.io/android-interview-prep/

## Main Folders

- `data/` question definitions in YAML
- `docs/deep-dives/` long-form topic notes
- `docs/generated/` auto-generated category pages
- `scripts/` documentation generation utilities

## Local Workflow

1. Update or add questions in `data/*.yaml`.
2. Add or update deep-dive files under `docs/deep-dives/`.
3. Regenerate generated pages.

## Regenerate Docs

```bash
python3 scripts/generate_docs.py
```
