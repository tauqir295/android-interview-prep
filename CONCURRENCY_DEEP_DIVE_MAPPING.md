# Concurrency Deep Dive Mapping & Architecture

## Overview

This document maps Concurrency interview questions to shared deep dives.
The goal is to keep `data/concurrency.yaml` concise while moving internals,
threading behavior, and production pitfalls into focused deep dives.

---

## Recommended Deep Dive Files

1. `docs/deep-dives/concurrency/coroutine-internals.md`
2. `docs/deep-dives/concurrency/threads-dispatchers-context.md`
3. `docs/deep-dives/concurrency/structured-scope-and-jobs.md`
4. `docs/deep-dives/concurrency/cancellation-exception-supervision.md`
5. `docs/deep-dives/concurrency/launch-async-parallelism.md`
6. `docs/deep-dives/concurrency/scheduler-thread-pools.md`
7. `docs/deep-dives/concurrency/parallelism-and-scheduling.md`
8. `docs/deep-dives/concurrency/flow-fundamentals.md`
9. `docs/deep-dives/concurrency/flow-operators-and-backpressure.md`
10. `docs/deep-dives/concurrency/stateflow-sharedflow-and-channels.md`
11. `docs/deep-dives/concurrency/flow-sharing-and-hot-streams.md`
12. `docs/deep-dives/concurrency/callbackflow-and-channelflow.md`
13. `docs/deep-dives/concurrency/synchronization-and-mutex.md`
14. `docs/deep-dives/concurrency/shared-state-and-race-conditions.md`
15. `docs/deep-dives/concurrency/deadlocks-and-contention.md`
16. `docs/deep-dives/concurrency/coroutine-testing-and-virtual-time.md`
17. `docs/deep-dives/concurrency/coroutine-debugging-and-observability.md`
18. `docs/deep-dives/concurrency/android-lifecycle-and-flow-collection.md`
19. `docs/deep-dives/concurrency/android-lifecycle-and-main-safety.md`
20. `docs/deep-dives/concurrency/production-concurrency-patterns-and-tuning.md`

---

## Question-to-Deep-Dive Mapping

### 1. Coroutine Internals
**File:** `docs/deep-dives/concurrency/coroutine-internals.md`

**Questions (4):**
- `structured-concurrency`
- `suspend-functions`
- `continuation-and-cps`
- `coroutine-state-machine`

---

### 2. Threads, Dispatchers, and Context Switching
**File:** `docs/deep-dives/concurrency/threads-dispatchers-context.md`

**Questions (3):**
- `threads-vs-coroutines`
- `dispatchers-overview`
- `withcontext-purpose`

---

### 3. Structured Scope and Jobs
**File:** `docs/deep-dives/concurrency/structured-scope-and-jobs.md`

**Questions (4):**
- `coroutine-scope`
- `job-hierarchy`
- `supervisorjob`
- `supervisorScope`

---

### 4. Cancellation, Exceptions, and Supervision
**File:** `docs/deep-dives/concurrency/cancellation-exception-supervision.md`

**Questions (4):**
- `coroutine-cancellation`
- `cooperative-cancellation`
- `coroutine-exception-handling`
- `coroutineexceptionhandler`

---

### 5. Launch, Async, and Parallelism
**File:** `docs/deep-dives/concurrency/launch-async-parallelism.md`

**Questions (3):**
- `launch-vs-async`
- `lazy-async`
- `parallelism-limit`

---

### 6. Scheduler and Thread Pools
**File:** `docs/deep-dives/concurrency/scheduler-thread-pools.md`

**Questions (2):**
- `thread-pools`
- `thread-starvation`

---

### 7. Parallelism and Scheduling
**File:** `docs/deep-dives/concurrency/parallelism-and-scheduling.md`

**Questions (1):**
- `limited-parallelism`

---

### 8. Flow Fundamentals
**File:** `docs/deep-dives/concurrency/flow-fundamentals.md`

**Questions (3):**
- `flow-what-is`
- `cold-vs-hot-flow`
- `backpressure`

---

### 9. Flow Operators and Backpressure
**File:** `docs/deep-dives/concurrency/flow-operators-and-backpressure.md`

**Questions (3):**
- `collectLatest`
- `flatMapLatest`
- `buffering-conflation`

---

### 10. StateFlow, SharedFlow, and Channels
**File:** `docs/deep-dives/concurrency/stateflow-sharedflow-and-channels.md`

**Questions (2):**
- `stateflow-vs-sharedflow`
- `channels-vs-sharedflow`

---

### 11. Flow Sharing and Hot Streams
**File:** `docs/deep-dives/concurrency/flow-sharing-and-hot-streams.md`

**Questions (2):**
- `statein-sharein`
- `one-off-events-with-sharedflow`

---

### 12. CallbackFlow and ChannelFlow
**File:** `docs/deep-dives/concurrency/callbackflow-and-channelflow.md`

**Questions (3):**
- `callbackflow`
- `channelflow`
- `flow-callback-interop`

---

### 13. Synchronization and Mutex
**File:** `docs/deep-dives/concurrency/synchronization-and-mutex.md`

**Questions (2):**
- `mutex`
- `synchronization-strategies`

---

### 14. Shared State and Race Conditions
**File:** `docs/deep-dives/concurrency/shared-state-and-race-conditions.md`

**Questions (3):**
- `shared-mutable-state`
- `atomic-operations`
- `thread-confinement`

---

### 15. Deadlocks and Contention
**File:** `docs/deep-dives/concurrency/deadlocks-and-contention.md`

**Questions (2):**
- `race-conditions`
- `deadlocks`

---

### 16. Coroutine Testing and Virtual Time
**File:** `docs/deep-dives/concurrency/coroutine-testing-and-virtual-time.md`

**Questions (3):**
- `coroutine-testing`
- `virtual-time-testing`
- `test-dispatchers`

---

### 17. Coroutine Debugging and Observability
**File:** `docs/deep-dives/concurrency/coroutine-debugging-and-observability.md`

**Questions (2):**
- `coroutine-debugging`
- `trace-and-observability`

---

### 18. Android Lifecycle and Flow Collection
**File:** `docs/deep-dives/concurrency/android-lifecycle-and-flow-collection.md`

**Questions (1):**
- `repeatOnLifecycle-flow-collection`

---

### 19. Android Lifecycle and Main Safety
**File:** `docs/deep-dives/concurrency/android-lifecycle-and-main-safety.md`

**Questions (2):**
- `main-safety`
- `anr-and-main-thread`

---

### 20. Production Concurrency Patterns and Tuning
**File:** `docs/deep-dives/concurrency/production-concurrency-patterns-and-tuning.md`

**Questions (1):**
- `concurrency-performance-optimization`

---

## Summary

- **Total Concurrency Questions:** 50
- **Total Shared Deep Dives:** 20
- **Audience:** mid, senior, and staff Android interviews
- **Design Goal:** concise YAML revision answers + deep coroutine/runtime coverage
