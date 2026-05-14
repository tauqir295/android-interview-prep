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

## Pagination Architecture Deep Dive

## Overview
Pagination splits large results into manageable pages for mobile.
## Core Concepts
Approaches:
1. **Offset/Limit**: Simple, page shifts with inserts
2. **Cursor**: Opaque token, handles concurrent inserts
3. **Keyset**: Last ID, maintains ordering
## Code Examples
```kotlin
// Paging 3 integration
class UserPagingSource : PagingSource<Int, User>() {
    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, User> {
        val page = params.key ?: 1
        val users = api.listUsers(page, params.loadSize)
        return LoadResult.Page(
            data = users,
            prevKey = if (page > 1) page - 1 else null,
            nextKey = page + 1
        )
    }
}
val pager = Pager(PagingConfig(pageSize = 20)) {
    UserPagingSource()
}
val flow = pager.flow.cachedIn(viewModelScope)
```
## Senior-Level Insights
- Cursor-based prevents duplicates
- Handle concurrent updates
- Cache pages locally where possible
