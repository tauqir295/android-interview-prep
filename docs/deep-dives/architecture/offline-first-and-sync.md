---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/architecture/">← Back to Architecture</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/architecture/${hash}`);
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

# Offline-First and Sync Deep Dive

## Overview

Offline-first architecture treats local data as primary for reads and resilience.
Network becomes synchronization infrastructure, not a mandatory read dependency.

## Core Concepts

- local-first reads for responsiveness and availability
- queued writes with retry/backoff
- explicit sync lifecycle and observability
- deterministic conflict resolution policy

## Layer Responsibilities

- Presentation:
  - render local-backed state immediately
  - show sync status/errors transparently
- Domain/use cases:
  - apply business invariants before enqueueing writes
- Data/sync engine:
  - persist write queue
  - schedule pull/push sync
  - reconcile conflicts and update canonical store

## Data Flow

1. User action writes to local store (or queue + local mutation).
2. UI reflects updated local state optimistically.
3. Sync worker pushes pending operations.
4. Server response is reconciled and persisted.
5. Canonical local state emits final representation.

## Internal Architecture

Typical internal components:

- local DB as SSOT
- operation queue with metadata (attempt count, timestamps)
- sync orchestrator (WorkManager + backoff)
- merge/conflict policy module

Conflict handling examples:

- last-write-wins for low-risk fields
- version-based merge for collaborative entities
- user-assisted merge for critical records

## Code Examples

```kotlin
data class PendingOp(
    val id: String,
    val entityId: String,
    val type: String,
    val payload: String,
    val attempt: Int
)

interface SyncCoordinator {
    suspend fun enqueueWrite(op: PendingOp)
    suspend fun runSyncCycle()
}
```

## Common Interview Questions

- How do you guarantee eventual consistency?
- When is optimistic UI unsafe?
- How do you avoid infinite retry loops?
- Where should conflict resolution policy live?

## Production Considerations

- instrument queue depth, sync latency, and conflict rate
- use idempotency keys for retried write operations
- provide backpressure when backend/system health degrades
- ensure secure local storage for sensitive offline data

## Scalability Tradeoffs

- Pros:
  - resilient UX under poor connectivity
  - smoother user interaction latency
- Cons:
  - higher complexity in sync and reconciliation logic
  - larger operational/debugging surface area

## Senior-Level Insights

Staff-level answers connect architecture with operations:
what metrics triggered incidents, how policies evolved,
and how teams balanced consistency guarantees vs product latency goals.
