# Room Database Query Optimization Deep Dive

**Question ID**: advanced-26  
**Difficulty**: Intermediate  
**Tags**: database, persistence, performance

## Core Concept

Room is Android's recommended SQLite abstraction, providing compile-time SQL validation and reactive queries. N+1 queries (loading parent then looping children) and missing indices are the primary performance killers; proper schema design prevents both.

## Key Areas Covered

### N+1 Query Pattern
- **Anti-pattern**: Load all users (1 query) → loop each user → load their posts (N queries) = N+1 total
- **Cost**: With 100 users, 101 queries instead of 1 JOIN
- **Detection**: Use systrace with "database" events; slow queries show long durations
- **Solution**: Single JOIN query: `SELECT u.*, p.* FROM users u JOIN posts p ON u.id = p.user_id`
- **Room support**: @Relations annotation automates joins for nested objects

### Indices for Query Performance
- **Table scan**: Without index, query reads entire table to find rows (O(n) with n = millions)
- **B-tree index**: Index on queried column → binary search (O(log n))
- **Cost trade-off**: Index adds write overhead (insert/update must update index) but saves read time
- **Strategy**: Index all frequently queried columns (user_id, timestamp, status)
- **Example**: `@Entity(indices = [@Index("user_id"), @Index(["timestamp", "user_id"])])`

### RxJava Integration
- **@Query returns Observable<List<User>>**: Room emits new list whenever table changes
- **Automatic resubscription**: If user deletes a post, Observable emits updated user list
- **Performance risk**: If listener does heavy work (sort, filter), jank on every update
- **Optimization**: Defer computation to background thread (Observable.subscribeOn(Schedulers.io()))

### Transaction Safety
- **@Transaction**: Ensures multi-step query completes atomically; no partial reads if writes interleave
- **Lock contention**: Long transactions block other writers (lock held during entire operation)
- **Example**: @Transaction fun getUserWithPosts() = joinedQuery() does 2 queries atomically
- **Trade-off**: Atomicity vs throughput; short transactions faster but risk inconsistency

### Connection Pool
- **SQLiteOpenHelper**: Manages single writer, multiple readers
- **Room uses shared pool**: Reuses connections across queries (faster than opening new)
- **WAL (Write-Ahead Logging)**: Enables concurrent reads while writes pending (better throughput)

## Real-World Patterns

### Pattern: N+1 Query Convert to Join
```kotlin
// Problem: N+1 queries
val users = db.userDao().getAllUsers()  // 1 query
users.forEach { user ->
  user.posts = db.postDao().getPostsByUserId(user.id)  // N queries
}

// Better: Single JOIN
@Query("SELECT u.*, p.* FROM users u LEFT JOIN posts p ON u.id = p.user_id")
fun getUsersWithPosts(): Flow<List<UserWithPosts>>
```

### Pattern: Missing Index on Filtered Column
```kotlin
// Problem: 1M posts, query "SELECT * FROM posts WHERE user_id = ?" scans all 1M rows
@Query("SELECT * FROM posts WHERE user_id = :userId")
fun getPostsByUser(userId: Int): Flow<List<Post>>

// Problem query: full table scan, 500ms
// Better: Add index
@Entity(indices = [@Index("user_id")])
data class Post(...)

// With index: binary search, 1ms
```

### Pattern: Async Database Access
```kotlin
// Problem: Database on main thread → ANR
val user = db.userDao().getUser(1)

// Better: Use suspend functions and launch in IO context
@Query("SELECT * FROM users WHERE id = :id")
suspend fun getUser(id: Int): User

// Usage
viewModelScope.launch {
  val user = userDao.getUser(1)  // Runs on IO, doesn't block UI
}
```

## Tradeoffs

| Factor | Comprehensive Join | Separate Queries |
|--------|-----------------|-----------------|
| Query Speed | Single round-trip | N round-trips |
| Memory | One DTO per user | Potential Object bloat |
| Code Clarity | Complex SQL | Simple, readable |
| Flexibility | Joins limit composition | Easy to recompose subsets |

## Interview Signals

### Strong answers include:
- Understanding N+1 detection and how to fix with JOINs
- Knowing index trade-offs (write overhead vs read speed)
- Aware of Room's Observable integration and reactive gotchas
- Can explain transaction isolation and when to use @Transaction
- Understanding async database access (not blocking main thread)

### Weak answers:
- Treating N+1 as "acceptable" or not recognizing the problem
- Thinking indices have no cost (forgetting write overhead)
- Not knowing Observable emits on table changes (architectural surprise)
- Unaware of main thread database access ANR risk

## Common Mistakes

- **Complex queries on main thread**: Causes ANR, UI blocks
- **Observable listeners doing work**: Heavy computation on each emission → jank
- **Indices on low-cardinality columns**: Index on status field (3 values) doesn't help
- **Missing PRIMARY KEY**: Causes implicit `rowid` lookups (slow)

## Performance Debug Approach

1. **Database Profiler**: View Query times in Android Profiler
2. **Systrace**: Look for "database" events, identify slow queries
3. **adb shell sqlite3**: Connect to app's database, EXPLAIN QUERY PLAN to see if index used
4. **Logcat**: Enable SQL logging to see actual queries executed

## Related Deep Dives

- [Reactive Programming & RxJava](./reactive-programming-and-rxjava.md) - Observable subscriptions and backpressure in Room
- [Multithreading & Scheduler](./multithreading-and-scheduler-behavior.md) - Thread affinity for async database access
- [Gradle Plugin Architecture](./gradle-plugin-architecture.md) - Room annotation processor for compile-time validation

