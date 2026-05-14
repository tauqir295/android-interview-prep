---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/fundamentals/">← Back to Fundamentals</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/fundamentals/${hash}`);
      return;
    }

    const referrer = document.referrer || "";
    if (referrer.includes("/android-interview-prep/generated/")) {
      link.setAttribute("href", referrer);
    }
  } catch (_) {
    // Keep default fundamentals link if URL parsing fails.
  }
})();
</script>

# Services Deep Dive

## Overview

A Service is an Android component used for background work that should continue independently of UI screens. Services do not provide UI and are managed by the system with their own lifecycle.

---

## Service Types

### Started Service

- Started with `startService()` or `startForegroundService()`.
- Runs until `stopSelf()`/`stopService()` is called.
- Good for one-off background tasks.

### Bound Service

- Started with `bindService()`.
- Exposes APIs via `IBinder`.
- Runs while clients are bound (unless also started).
- Useful for in-process or cross-process IPC.

### Foreground Service

- Must show persistent notification.
- Higher priority, less likely to be killed.
- Required for user-visible long-running tasks.

---

## Lifecycle

### Started Service Flow

```kotlin
override fun onCreate() {
    super.onCreate()
}

override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
    // Do work off main thread
    return START_NOT_STICKY
}

override fun onDestroy() {
    super.onDestroy()
}
```

### Restart Modes

- `START_NOT_STICKY`: Do not recreate after kill.
- `START_STICKY`: Recreate service, intent may be null.
- `START_REDELIVER_INTENT`: Recreate and redeliver last intent.

---

## Service vs Thread

- **Thread**: execution unit, tied to process lifetime.
- **Service**: component managed by Android lifecycle.
- Service work still needs threading (`Dispatchers.IO`, `Executor`, etc).

---

## Bound Service Example

```kotlin
class PlayerService : Service() {
    private val binder = LocalBinder()

    inner class LocalBinder : Binder() {
        fun getService(): PlayerService = this@PlayerService
    }

    override fun onBind(intent: Intent?): IBinder = binder

    fun play(trackId: String) {
        // business logic
    }
}
```

```kotlin
private val connection = object : ServiceConnection {
    override fun onServiceConnected(name: ComponentName?, service: IBinder?) {
        val binder = service as PlayerService.LocalBinder
        val playerService = binder.getService()
        playerService.play("track_1")
    }

    override fun onServiceDisconnected(name: ComponentName?) = Unit
}
```

---

## Android 8+ Background Limits

- Background service starts are restricted.
- Use `startForegroundService()` when required.
- Prefer `WorkManager` for deferrable background work.

---

## Interview Traps

- Service does **not** run on a separate thread by default.
- Foreground service requires notification promptly.
- `IntentService` is deprecated; use `WorkManager`.

---

## Key Takeaways

- Services represent background-capable components, not threading primitives.
- Choose started, bound, or foreground based on interaction and visibility.
- Use modern background APIs (`WorkManager`) for resilient scheduling.

