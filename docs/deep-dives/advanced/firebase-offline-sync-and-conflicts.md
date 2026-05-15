# Firebase Offline Sync & Conflict Resolution Deep Dive

**Question ID**: advanced-30  
**Difficulty**: Senior  
**Tags**: firebase, sync, reliability

## Core Concept

Firebase Realtime Database queues offline writes locally; when reconnected, syncs to cloud. Conflicts arise when device and cloud both modify same record—resolution requires strategy to prevent silent data loss.

## Key Areas Covered

### Offline Write Queuing
- **Automatic queueing**: Writes enqueued locally while offline; persisted to disk
- **Sync on reconnect**: Upon reconnection, queued writes synced to cloud atomically (FIFO order preserved)
- **Visibility**: App sees updates immediately (optimistic), cloud sees them moments later
- **Risk**: If both device and cloud write same field, conflict occurs

### Conflict Resolution Strategies

#### Last-Write-Wins (LWW)
- **Simple**: Server timestamp determines winner; latest write overwrites
- **Problem**: Earlier write discarded silently (data loss)
- **Example**: User edits note offline at 2pm, cloud updated by another device at 1:50pm → user's edit lost

#### Timestamp-Based
- **Better than LWW**: Compare timestamps to resolve
- **Clock skew risk**: Device clock can be wrong (set to year 2000); cloud timestamp older than device
- **Advantage**: No explicit versioning needed
- **Disadvantage**: Doesn't preserve intent; both writes might be important

#### Vector Clocks
- **Causality tracking**: Each write tags with version number; detects concurrent writes
- **Merge function**: Custom logic decides which write "wins" or merges both
- **Advantage**: Preserves all edits; merge can combine them intelligently
- **Disadvantage**: Complex to implement; requires custom conflict resolution

#### CRDTs (Conflict-free Replicated Data Types)
- **Append-only logs**: Instead of mutable fields, record all changes as immutable events
- **Merge properties**: Any two histories can be merged without data loss (commutative)
- **Example**: Counter CRDT: increment A by 2, increment B by 3 → final value 5 (order doesn't matter)
- **Advantage**: No conflicts (by design); all edits preserved
- **Disadvantage**: Non-obvious semantics; hard to retrofit into existing apps

### Firestore Transactions
- **Multi-document ACID**: All reads/writes atomic; other clients see consistent snapshot
- **Offline limitation**: Offline writes can't participate in transaction
- **Result**: Transaction committed without offline write, then offline write syncs → atomicity broken
- **Mitigation**: Avoid transactions across offline-writable fields

### Real-World Issue: Data Loss
```
Time 1: User A (device offline) writes note = "Important task"
Time 2: User B (cloud online) writes note = "Deleted by accident"
Time 3: User A reconnects; offline write synced
Result with LWW: If User B's write is later, User A's data lost silently
```

## Real-World Patterns

### Pattern: Last-Write-Wins Problem
```java
// Offline write
firebase.setValue("task", "My task")  // Queued

// Meanwhile, cloud updated (another device)
firebase.setValue("task", "Overwritten")  // Server timestamp T+10s

// On sync: LWW sees T+10s > T+0s, server write wins
// Result: Offline write lost silently
```

### Pattern: Vector Clock Merge
```
Device history: [write1(name="Alice", T=1), write2(age=30, T=2)]
Cloud history: [write1(name="Alice", T=1), write3(email="a@b.com", T=1.5)]

Merge: {name="Alice", age=30, email="a@b.com"}  // All three writes preserved
```

### Pattern: CRDT Counter Example
```
Offline increment: counter += 5  // Logged as [device_id, 5]
Cloud increment: counter += 3    // Logged as [server_id, 3]

Merge: Total = 5 + 3 = 8  // Both increments preserved, order irrelevant
Traditional merge (LWW): Would pick one (data loss)
```

### Pattern: Offline Transactions (Anti-pattern)
```java
// Problem: Offline transaction not atomic
runTransaction {
  val user = read("users/1")
  user.gold -= 100
  val item = read("items/1")
  item.quantity -= 1
  writeUser(user)
  writeItem(item)
  // If offline here: both writes queued but separate from transaction context
}

// Better: Single path update (atomic)
firebase.setValue("users/1/gold", userWithGold)  // Atomic
```

## Tradeoffs

| Factor | Optimistic Sync | Pessimistic (Require Online) |
|--------|-----|----------|
| UX Responsiveness | Immediate (offline writes visible) | Delayed (blocked until online) |
| Conflict Risk | High (concurrent writes) | None (network enforces serialization) |
| Battery | Better (no polling) | Worse (checks connection) |
| Complexity | High (conflict resolution) | Low (no conflicts) |

## Interview Signals

### Strong answers include:
- Understanding offline writes queued locally and synced atomically on reconnect
- Knowing last-write-wins is simple but causes silent data loss
- Aware of vector clocks and how they preserve edit causality
- Understanding CRDTs as solution (append-only, conflict-free by design)
- Aware of Firestore transaction gotcha (offline writes break atomicity)

### Weak answers:
- Thinking offline writes automatically "merge" (they don't; conflict resolution required)
- Not recognizing silent data loss with LWW (assuming it's fine)
- Unaware of CRDT approach (thinking only option is complex versioning)
- Not considering that both edits might be important (assuming one "wins")

## Common Mistakes

- **Assuming LWW is sufficient**: Works until user experiences data loss
- **Nested transactions with offline writes**: Offline write not included in transaction boundary
- **Clock skew**: Relying on device time (user sets phone to 1970, breaks timestamp comparison)
- **Not logging conflicts**: Silent resolution hides bugs; should log when conflict occurs

## Design Patterns for Reliable Sync

1. **Server authority**: Don't attempt merge; let server decide (simple, may lose data)
2. **Client merge**: Device and cloud negotiate (complex, preserves both)
3. **CRDTs**: Structure data as conflict-free types (hard to retrofit, very safe)
4. **Pessimistic lock**: Prevent concurrent writes (responsive but requires online)

## Performance Debug Approach

1. **Firebase Emulator**: Test offline/online scenarios locally
2. **Logcat "Firebase"**: Track synced writes, conflicts
3. **Database Rules**: Add logging when conflicts detected
4. **Manual testing**: Two devices, offline one device, edit same field, reconnect, verify result

## Related Deep Dives

- [WorkManager & Background Execution](./workmanager-and-background-execution.md) - Sync strategy with WorkManager
- [Reactive Programming](./reactive-programming-and-rxjava.md) - Observable sync status in Firebase listeners
- [Database Query Optimization](./room-database-query-optimization.md) - Local-first sync with Room

