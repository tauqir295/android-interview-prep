---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/concurrency/">← Back to Concurrency</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/concurrency/${hash}`);
      return;
    }
    const referrer = document.referrer || "";
    if (referrer.includes("/android-interview-prep/generated/")) {
      link.setAttribute("href", referrer);
    }
  } catch (_) {
    // Keep default generated page link if URL parsing fails.
  }
})();
</script>

## Android Lifecycle and Main Safety Deep Dive
## Overview
Main safety is about guaranteeing that APIs can be invoked from UI code without
blocking the main thread and risking jank or ANRs.
## Core Concepts
- main-safe suspend API contracts
- lifecycle-aware cancellation
- strict separation of UI and blocking I/O
- ANR prevention via cooperative architecture
## Internal Implementation
A main-safe repository/use case shifts blocking sections internally using
`withContext(Dispatchers.IO)` while preserving a simple suspend API for callers.
Lifecycle scopes cancel in-flight work when UI is destroyed/stopped,
preventing stale updates and leaked tasks.
## Threading Model
UI reads and state publication stay on main; expensive compute or blocking I/O
runs on background dispatchers with bounded parallelism.
## Coroutine / Flow Behavior
Flows collected on main should emit lightweight UI models.
Heavy mapping should happen upstream before reaching renderer-level collectors.
## Code Examples
```kotlin
class UserRepository(
    private val dao: UserDao,
    private val api: UserApi
) {
    suspend fun refreshUser(id: String): User = withContext(Dispatchers.IO) {
        val network = api.fetchUser(id)
        dao.insert(network)
        network
    }
}
```
## Common Interview Questions
- What does "main-safe" mean in practice?
- Why should callers not care which dispatcher a repository uses?
- How do main-thread violations lead to ANRs?
- How does lifecycle cancellation reduce stale UI updates?
## Production Considerations
- enforce strict-mode policies in debug builds
- audit blocking APIs used from presentation layer
- bound retries/timeouts to avoid long main-thread stalls in callbacks
- monitor frame drops and ANR traces
## Performance Insights
Most ANR regressions are architecture issues: unclear thread ownership,
blocking dependencies, or missing cancellation boundaries.
## Senior-Level Insights
At staff level, articulate thread-ownership contracts across layers and how
those contracts are validated by tests, lint rules, and telemetry.
