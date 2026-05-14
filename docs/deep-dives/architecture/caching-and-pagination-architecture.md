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

## Caching and Pagination Architecture Deep Dive

## Overview

Caching and pagination architecture determines perceived performance,
data consistency, and backend load behavior. Policy clarity matters more
than any single library choice.

## Core Concepts

- cache hierarchy (memory -> disk/db -> network)
- freshness policy (TTL, version, etag)
- pagination key strategy (page, cursor, token)
- invalidation triggers (manual, time, mutation, server signals)

## Layer Responsibilities

- Presentation:
  - display paged state and load/error indicators
- ViewModel/domain:
  - coordinate refresh/append intents
  - map cache/paging results to UI state
- Data:
  - enforce cache policy and page merge logic

## Data Flow

1. UI requests initial or next page.
2. Repository checks cache validity.
3. If needed, remote fetch runs with paging token.
4. Data is merged/deduplicated and persisted.
5. UI observes updated canonical paged state.

## Internal Architecture

Key internals to define early:

- canonical item identity and dedup rules
- append/prepend retry behavior
- refresh boundary and stale window policy
- invalidation after writes that change list ordering

## Code Examples

```kotlin
interface FeedPagingRepository {
    fun observeFeed(): Flow<List<FeedItem>>
    suspend fun refresh()
    suspend fun loadNextPage()
}

class FeedPagingPolicy(
    val staleAfterMs: Long,
    val pageSize: Int
)
```

## Common Interview Questions

- Where should pagination state live?
- Cursor vs offset pagination tradeoffs?
- How do you avoid duplicate items across pages?
- What should invalidate cached pages?

## Production Considerations

- instrument cache hit rate and page load latency
- backoff on repeated page fetch failures
- protect against thundering-herd refresh behavior
- validate paging under flaky network conditions

## Scalability Tradeoffs

- Pros:
  - better UX latency and lower backend pressure
  - smoother long-list performance
- Cons:
  - higher complexity in merge/invalidation logic
  - consistency edge cases under concurrent updates

## Senior-Level Insights

Staff-level answers should include operational metrics.
A good architecture defines how teams measure cache effectiveness,
page quality, and sync correctness over time.
