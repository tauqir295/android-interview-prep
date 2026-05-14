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

# Repository Pattern and Data Sources Deep Dive

## Overview

Repository architecture abstracts data origin and centralizes consistency policy.
In production Android apps, repositories are where cache, sync, and fallback logic
should live instead of leaking into ViewModels.

## Core Concepts

- repository exposes stable domain-facing API
- local and remote sources remain implementation details
- single source of truth (SSOT) enforced at repository boundary
- mapping and error normalization happen before upstream exposure

## Layer Responsibilities

- Presentation/ViewModel:
  - consume repository through use cases/contracts
  - avoid source-specific logic
- Domain:
  - define repository interfaces and business semantics
- Data:
  - implement source orchestration
  - handle persistence/network/retry policy

## Data Flow

1. Consumer requests data from repository.
2. Repository reads canonical local source.
3. Freshness rules decide whether remote fetch is needed.
4. Remote result is validated/mapped and persisted.
5. Updated canonical source emits new data upstream.

## Internal Architecture

Typical repository internals:

- remote source adapter (API)
- local source adapter (DB/cache)
- mapper layer (DTO <-> entity <-> UI model)
- policy engine (TTL, backoff, conflict handling)

Important anti-patterns:

- leaking Retrofit/Room types to domain/UI
- duplicating fetch policy across features
- bypassing repository for "quick fixes"

## Code Examples

```kotlin
interface ArticleRepository {
    fun observeArticles(): Flow<List<Article>>
    suspend fun refreshArticles(force: Boolean = false)
}

class ArticleRepositoryImpl(
    private val api: ArticleApi,
    private val dao: ArticleDao,
    private val clock: Clock
) : ArticleRepository {
    override fun observeArticles(): Flow<List<Article>> = dao.observeAll()

    override suspend fun refreshArticles(force: Boolean) {
        if (force || dao.isStale(clock.now())) {
            val remote = api.getArticles()
            dao.replaceAll(remote.map { it.toEntity() })
        }
    }
}
```

## Common Interview Questions

- Should repositories return `Flow`, `suspend`, or both?
- Where should mapping happen?
- How do you enforce SSOT in multi-feature apps?
- Repository vs use case: where do rules belong?

## Production Considerations

- document freshness and retry policies explicitly
- include tracing around source decisions (local vs remote)
- protect write paths with idempotency/retry semantics
- keep repository APIs stable to minimize cross-team churn

## Scalability Tradeoffs

- Pros:
  - consistency and reuse of data policy
  - lower UI-layer complexity
- Cons:
  - repository can become a god object without boundaries
  - policy complexity grows with product scope

## Senior-Level Insights

Senior-level answers should discuss repository ownership and governance.
At scale, success depends on keeping repository contracts stable while letting
data-source implementations evolve safely.
