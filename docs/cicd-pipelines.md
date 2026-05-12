# Cicd Pipelines

!!! tip "Key Interview Concept"
    Interviewers love asking about automation and how you ensure code quality before a release.

## 🏗️ Pipeline Stages
1. **Linting:** Checking for code style and static analysis.
2. **Unit Tests:** Ensuring logic works as expected.
3. **Build:** Generating the .aab (Android App Bundle).
4. **UI Tests:** Running Espresso/Compose tests on a device farm.
5. **Deploy:** Uploading to the Play Store Internal track.
