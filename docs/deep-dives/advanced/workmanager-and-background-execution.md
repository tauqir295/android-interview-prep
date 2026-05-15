# WorkManager & Background Execution Deep Dive

**Question ID**: advanced-27  
**Difficulty**: Intermediate  
**Tags**: background, reliability, power

## Core Concept

WorkManager provides a unified API for scheduling work with persistence, automatic retries, and constraint awareness. Unlike JobScheduler or foreground services, WorkManager guarantees eventual execution even across app restarts and device reboots.

## Key Areas Covered

### WorkManager Persistence
- **Database-backed**: Work persisted to SQLite; survives app restart, device reboot, or process kill
- **Auto-retry**: Exponential backoff by default (delays 30s, 5m, 30m, etc.)
- **Guarantee level**: "Eventually" (may delay hours due to constraints; not "immediately")
- **Verification**: Device can be powered off for hours; work executes when device reboots and constraints met

### JobScheduler vs WorkManager
- **JobScheduler**: Periodic jobs aligned to system windows (batched, optimized)
- **WorkManager**: Persistent one-time or periodic work; survives reboot
- **Timing**: JobScheduler more precise (minutes window); WorkManager less precise (hours possible)
- **Decision**: JobScheduler for system-level optimization; WorkManager for critical app work

### Foreground Services
- **Always-on**: Exempt from Doze, cachekill; visible notification required
- **User awareness**: "X is draining battery" warning increases uninstall risk
- **Use case**: Music playback, navigation (user initiated, ongoing)
- **Guarantee**: Immediate execution while service running
- **Trade-off**: Battery impact but responsive UX

### Constraint Model
- **Network**: Work runs only if connected (or specific Wifi)
- **Battery**: Work deferred if below 25% or in low-power mode
- **Idle**: Work runs only when device idle (screen off, no active work)
- **Charging**: Work runs only if plugged in (saves battery)
- **Combination**: All constraints must be met (AND logic); no OR

### Chaining & Conditional Execution
- **workRequest1 > workRequest2**: Sequential execution (request2 runs after request1)
- **Conditional**: Can fork execution based on request1 outcome (success/failure)
- **Cleanup**: Chained work aborts if predecessor fails (unless configured differently)

## Real-World Patterns

### Pattern: Reliable Analytics via WorkManager
```kotlin
// Problem: JobScheduler discards work on device reboot
val job = JobInfo.Builder(ANALYTICS_JOB_ID, ...)
  .setRequiresDeviceIdle(true)
  .setRequirescharging(true)
  .build()
jobScheduler.schedule(job)  // Lost if device reboots

// Better: WorkManager persists and retries
class AnalyticsWorker : Worker() {
  override fun doWork(): Result {
    api.sendAnalytics()
    return Result.success()  // Auto-retry if fails
  }
}

val analyticsWork = OneTimeWorkRequestBuilder<AnalyticsWorker>()
  .setConstraints(Constraints.Builder().setRequiresCharging(true).build())
  .setBackoffCriteria(LINEAR, 15, MINUTES)
  .build()
WorkManager.getInstance(context).enqueueUniqueWork("analytics", KEEP, analyticsWork)
```

### Pattern: Periodic Job Without Exact Timing
```kotlin
// Problem: Expecting periodic job to run exactly every 15 minutes
val periodicWork = PeriodicWorkRequestBuilder<RefreshWorker>(15, MINUTES).build()
WorkManager.getInstance(context).enqueueUniquePeriodicWork("refresh", KEEP, periodicWork)

// Reality: May run at 15m, 22m, 18m (±flex window); OS optimizes across all periodic jobs
// If constraints (Wifi, charging) unmet, deferred indefinitely
```

### Pattern: Conditional Work Chain
```kotlin
val fetchWork = OneTimeWorkRequestBuilder<FetchWorker>().build()
val processWork = OneTimeWorkRequestBuilder<ProcessWorker>().build()
val notifyWork = OneTimeWorkRequestBuilder<NotifyWorker>().build()

WorkManager.getInstance(context)
  .beginWith(fetchWork)
  .then(processWork)
  .then(notifyWork)
  .enqueue()

// If fetchWork fails, processWork and notifyWork don't run
```

## Tradeoffs

| Factor | WorkManager | JobScheduler | Foreground Service |
|--------|-----------|------------|-----------------|
| Reliability | High (persistent) | Medium (discarded on reboot) | High (while running) |
| Timing | Imprecise (hours) | Precise (minutes) | Immediate |
| Battery | Good (batched by OS) | Good (optimized) | Poor (always-on) |
| Constraints | Rich (network, idle, etc.) | Basic (connectivity) | None |
| Visibility | Silent | Silent | Visible notification |

## Interview Signals

### Strong answers include:
- Understanding WorkManager persists across reboot vs JobScheduler doesn't
- Knowing WorkManager guarantee is "eventually" not "immediately"
- Aware of constraint combinations (all AND'd, not OR'd)
- Can explain when to use foreground service (user-initiated, ongoing)
- Understanding retry strategy and exponential backoff
- Knowing work chains allow conditional execution

### Weak answers:
- Thinking WorkManager guarantees immediate execution (it doesn't)
- Not knowing JobScheduler discards work on reboot (whereas WorkManager doesn't)
- Confusing WorkManager with ScheduledExecutorService (no persistence)
- Assuming periodic job runs exactly on interval (OS batches and optimizes)

## Common Mistakes

- **No constraints**: Work runs immediately even in low battery (bad UX)
- **Forgetting about reboot**: Job lost on power-off with JobScheduler
- **Expecting exact timing**: Periodic work is ±flex, OS groups jobs
- **Over-chaining**: Deep work chains hard to debug and maintain

## Performance Debug Approach

1. **adb shell dumpsys jobscheduler**: See scheduled jobs
2. **Logcat "WorkManager"**: See work execution, retries, failures
3. **Device Profiler**: Monitor battery/network consumption
4. **Manual test**: Reboot device, verify work executes on startup

## Related Deep Dives

- [Power Management & Doze](./power-management-doze-and-jobs.md) - Doze constraints on work
- [Reactive Programming](./reactive-programming-and-rxjava.md) - RxJava ResultListeners in work callbacks
- [Multithreading & Scheduler](./multithreading-and-scheduler-behavior.md) - Thread affinity in Worker.doWork()

