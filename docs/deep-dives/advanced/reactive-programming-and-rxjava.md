# Reactive Programming & RxJava Deep Dive

**Question ID**: advanced-21  
**Difficulty**: Senior  
**Tags**: architecture, reactive, async

## Core Concept

RxJava provides a library for reactive programming on the JVM using observables and composable, functional-style operators. It enables declarative asynchronous data pipelines with built-in backpressure handling to prevent memory overflow.

## Key Areas Covered

### Observable vs Flowable
- **Observable**: Simple stream, no backpressure handling; ideal for UI events, clicks, timers
- **Flowable**: Respects backpressure (slow consumer can signal upstream to pause); for high-volume data sources
- **Trade-off**: Observable easier to use, Flowable safer but with overhead

### Backpressure Strategies
- **Drop**: Discard items from buffer if consumer slow (data loss acceptable)
- **Buffer**: Accumulate items in memory (OOM risk if buffer unbounded)
- **Latest**: Only keep newest item (intermediate values discarded)
- **Pause Upstream**: Block producer until consumer ready (classic backpressure)

### Operator Fusion & Performance
- **RxJava 2 fusion**: Inlines simple operators (map, filter) into single loop instead of 3 separate passes
- **Memory efficiency**: Avoids intermediate object allocation
- **Composition**: Chain operators without performance cliff

### Cancellation & Disposal
- **Disposable**: Handle for cancelling subscription; prevents resource leaks
- **CompositeDisposable**: Aggregates multiple disposables for bulk cleanup
- **Common mistake**: Forgetting to unsubscribe → leaks streams, threads, timers

## Real-World Patterns

### Pattern: Backpressure Overflow
```
Source emits 1M items/sec
Consumer processes 1 item/ms (1000/sec)
Unbackpressured Observable buffers 999K items/sec → OOM
```

### Pattern: Operator Fusion Benefit
```
Observable.range(1, 1000000)
  .map(x -> x * 2)      // Without fusion: creates intermediate Observable
  .filter(x -> x % 2 == 0)  // Creates another Observable
  .map(x -> x + 1)      // Creates third Observable
  
With fusion: single loop, no intermediate allocations
```

### Pattern: Testing with TestScheduler
- Use `TestScheduler` to advance virtual time
- Emit items on predictable timeline
- Verify backpressure handling in unit tests

## Tradeoffs

| Factor | Observable | Flowable |
|--------|-----------|----------|
| Learning Curve | Easy | Steeper (backpressure contracts) |
| Memory | Unbounded buffer risk | Controlled via backpressure |
| Performance | Slightly faster | Slight overhead for pressure control |
| Use Case | UI, clicks, timers | File I/O, network, high-throughput streams |

## Interview Signals

### Strong answers include:
- Understanding when to use Observable vs Flowable (not just "always use Flowable")
- Recognizing backpressure as a contract between producer and consumer
- Knowing that unsubscribe chains and how disposal works
- Aware of operator fusion and its performance implications

### Weak answers:
- Treating Observable and Flowable as interchangeable
- Ignoring backpressure in high-volume scenarios
- Not knowing about disposal/memory leaks in long-lived subscriptions

## Related Deep Dives

- [Jetpack Compose Performance](./jetpack-compose-performance.md) - State management in async flows
- [Multithreading & Scheduler](./multithreading-and-scheduler-behavior.md) - Thread affinity with RxJava schedulers
- [Database Query Optimization](./room-database-query-optimization.md) - RxJava integration with Room DAOs

