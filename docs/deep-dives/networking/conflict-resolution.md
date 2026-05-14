---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/networking/">← Back to Networking</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/networking/${hash}`);
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

## Conflict Resolution Deep Dive

## Overview
When local and remote changes conflict, determine winner.
## Core Concepts
Strategies:
- Last-write-wins (simplest, timestamp-based)
- Remote-wins (server authority)
- Merge (combine non-conflicting fields)
- Manual (show UI)
## Code Examples
```kotlin
// Last-write-wins merge
fun mergeUser(local: User, remote: User): User {
    return if (local.modifiedAt > remote.modifiedAt) {
        local
    } else {
        remote
    }
}
// Merge fields
fun mergeUser(local: User, remote: User): User {
    return User(
        id = remote.id,
        name = remote.name ?: local.name,
        email = local.email,  // prefer local
        modifiedAt = maxOf(local.modifiedAt, remote.modifiedAt)
    )
}
```
## Senior-Level Insights
- Log conflicts for analytics
- Version vectors for causal ordering
- Expose unresolved conflicts in UI
