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
    // Keep default generated page link if URL parsing fails.
  }
})();
</script>
## Broadcast Receivers Deep Dive

## Overview

Broadcast Receivers let apps react to system-wide or app-defined events delivered as intents. They are lightweight event handlers and should complete quickly.

---

## Registration Models

### Manifest (Static) Receiver

```xml
<receiver android:name=".BootReceiver" android:exported="false">
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED" />
    </intent-filter>
</receiver>
```

- Works even when app process is not running.
- Limited by newer Android background policies.

### Runtime (Dynamic) Receiver

```kotlin
val receiver = object : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        // Quick handling
    }
}

registerReceiver(receiver, IntentFilter("com.example.ACTION_SYNC"))
```

- Active only while process/context is alive.
- Safer for in-app events and lifecycle control.

---

## Ordered vs Normal Broadcast

### Normal

- Delivered to all matching receivers without strict order.
- Receivers cannot stop propagation.

### Ordered

- Delivered by priority sequence.
- Receiver can change result and abort (legacy behavior nuances apply by API level).

---

## Performance Rules

- `onReceive()` runs on main thread.
- Keep work short (< 10s, ideally much less).
- Offload long work to `WorkManager` or foreground service.

```kotlin
override fun onReceive(context: Context, intent: Intent) {
    val work = OneTimeWorkRequestBuilder<SyncWorker>().build()
    WorkManager.getInstance(context).enqueue(work)
}
```

---

## Security Practices

- Set `android:exported` explicitly.
- Use custom permissions for sensitive broadcasts.
- Prefer explicit package targeting when possible.
- Validate intent extras before processing.

---

## Common Interview Questions

- **Q:** Why avoid long work in `onReceive()`?
  **A:** Answer with Android lifecycle and platform constraints first, then API behavior, and finally the production tradeoffs around reliability and user impact.
- **Q:** Static vs dynamic registration differences?
  **A:** Answer with Android lifecycle and platform constraints first, then API behavior, and finally the production tradeoffs around reliability and user impact.
- **Q:** How Android 8+ changed implicit broadcast behavior?
  **A:** State load and SLO assumptions first, identify the first bottleneck, choose scaling and consistency strategy, and explain fallback behavior for partial failures.

---
## Key Takeaways

- Broadcast Receivers are event listeners, not long-running workers.
- Choose registration type based on lifecycle and reliability needs.
- Use modern background APIs for heavy work.

