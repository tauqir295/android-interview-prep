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

## Offline-First Architecture Deep Dive

## Overview
Offline-first: local DB is source of truth, sync when connected.
## Core Concepts
1. All reads from local DB
2. Writes queued, synced
3. Conflict resolution on sync
4. Seamless online/offline
## Code Examples
```kotlin
// Room as local source
@Dao
interface UserDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUser(user: User)
    @Query("SELECT * FROM users")
    fun getAllUsers(): Flow<List<User>>
}
// Repository coordinates
class UserRepository(
    private val api: UserApi,
    private val dao: UserDao
) {
    fun getUsers(): Flow<List<User>> = dao.getAllUsers()
    suspend fun syncUsers() {
        val remote = api.listUsers()
        dao.insertAll(remote)
    }
}
```
## Senior-Level Insights
- WorkManager for background sync
- Prioritize recent changes
- Handle partial sync failures
