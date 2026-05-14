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
# Context Deep Dive

## Overview

Context is an abstract class that provides access to system resources and services. It's your bridge to the Android framework. Understanding Context's types and lifecycle is crucial for avoiding memory leaks and using Android APIs correctly.

---

## Context Architecture

### What Context Provides

```
Context is essentially:
├─ Access to system services (LocationManager, SensorManager, etc)
├─ Access to app resources (strings, drawables, colors)
├─ File I/O operations
├─ Starting Activities, Services, Broadcasting
├─ Loading preferences and databases
├─ Creating views and inflating layouts
└─ Access to application state
```

### Context Hierarchy

```
Context (abstract)
├─ ContextImpl (actual implementation)
│   ├─ Activity Context (MainActivity:this)
│   │   ├─ Can show dialogs
│   │   ├─ Can start activities
│   │   └─ Tied to Activity lifecycle
│   │
│   ├─ Service Context (Service:this)
│   │   ├─ No UI operations
│   │   └─ Tied to Service lifecycle
│   │
│   └─ Broadcast Receiver Context
│       ├─ Temporary
│       └─ Valid only during onReceive()
│
└─ Application Context (getApplicationContext())
    ├─ Singleton, app-wide scope
    ├─ Lives entire app lifetime
    └─ Cannot show UI operations
```

---

## Context Types

### Application Context

```kotlin
val appContext = context.applicationContext
// OR
val appContext = application  // In Activity/Service
```

**Characteristics:**
- Singleton (one per app)
- Lives entire app lifetime
- Cannot show UI dialogs/toasts
- Safe for long-lived objects

**Use for:**
- Global singletons
- Database operations
- SharedPreferences
- Any non-UI work

```kotlin
// ✅ CORRECT
val db = Room.databaseBuilder(applicationContext, MyDatabase::class.java, "db").build()

val prefs = applicationContext.getSharedPreferences("prefs", 0)

val singleton = object : MyService {
    val context = applicationContext  // Safe - won't leak
}
```

### Activity Context

```kotlin
// In Activity
val activityContext = this

// Or explicitly
val activityContext: Context = this
```

**Characteristics:**
- Tied to Activity lifecycle
- Multiple per app
- Can show UI operations (dialogs, toasts)
- Die when Activity destroyed

**Use for:**
- Showing dialogs, toasts in that Activity
- UI operations tied to Activity
- LayoutInflater creation
- Can pass to short-lived objects only

```kotlin
// ✅ CORRECT - Activity context for UI
AlertDialog.Builder(this)
    .setTitle("Confirm")
    .setPositiveButton("OK") { _, _ -> }
    .show()

// ✅ CORRECT - Application context for database
val db = Room.databaseBuilder(applicationContext, DB::class.java, "db").build()
```

### Service Context

```kotlin
// In Service
val serviceContext = this
```

**Characteristics:**
- Tied to Service lifecycle
- No UI operations possible
- Can request notifications (foreground services)

**Use for:**
- Non-UI background work
- Accessing services
- Starting intents

### Broadcast Receiver Context

```kotlin
// In onReceive()
fun onReceive(context: Context, intent: Intent) {
    // context valid ONLY during onReceive()
    // Do NOT store reference to it
}
```

**Important:** Context is temporary, don't store!

---

## Context Memory Leaks

### How They Happen

**Leak Chain:**
```
Long-lived Object → holds Activity Context
                 → Activity can't be garbage collected
                 → Activity's views can't be GC'd
                 → All resources tied to Activity leak
```

### Common Leak Patterns

**Pattern 1: Static Reference to Activity**

```kotlin
companion object {
    var activity: Activity? = null  // ❌ MEMORY LEAK
}

// Usage
MyService.activity = this

// Result: Activity in back stack can't be destroyed
```

**Fix: Use application context**
```kotlin
companion object {
    var context: Context? = null  // ✅ OK if using app context
}

// Usage
MyService.context = applicationContext
```

**Pattern 2: Inner Class Holding Activity**

```kotlin
class MyActivity : AppCompatActivity() {
    inner class MyThread : Thread() {  // ❌ LEAK
        override fun run() {
            Thread.sleep(60000)
        }
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        MyThread().start()  // Activity held for 60s
    }
}
```

**Fix: Static inner class with WeakReference**

```kotlin
class MyActivity : AppCompatActivity() {
    private static class MyThread(activity: MyActivity) : Thread() {
        private val activityRef = WeakReference(activity)
        
        override fun run() {
            val activity = activityRef.get()
            if (activity != null) {
                // Use activity
            }
        }
    }
}
```

**Pattern 3: Unregistered Listeners**

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    eventBus.register(this)  // ❌ If never unregistered
}

// Activity destroyed but still registered
// EventBus holds reference → leak
```

**Fix: Unregister in onDestroy()**

```kotlin
override fun onDestroy() {
    eventBus.unregister(this)
    super.onDestroy()
}
```

**Pattern 4: Handler with Delayed Messages**

```kotlin
private val handler = Handler(Looper.getMainLooper())

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    handler.postDelayed({
        // If this runs after Activity destroyed: leak
        updateUI()
    }, 60000)
}
```

**Fix: Remove messages or use coroutines**

```kotlin
override fun onDestroy() {
    handler.removeCallbacksAndMessages(null)  // Remove pending
    super.onDestroy()
}

// Better: Use coroutines
viewModel.doLongOperation()  // Auto-cancels with Activity
```

---

## Application vs Activity Context: Decision Matrix

| Operation | App Context | Activity Context |
|-----------|-------------|------------------|
| Start Activity | ❌ Needs FLAG_ACTIVITY_NEW_TASK | ✅ |
| Start Service | ✅ | ✅ |
| Send Broadcast | ✅ | ✅ |
| Show Dialog | ❌ Crashes | ✅ |
| Show Toast | ❌ Often fails | ✅ |
| Get SystemService | ✅ | ✅ |
| Create Database | ✅ | ✅ |
| Get SharedPreferences | ✅ | ✅ |
| Inflate Layout | ❌ Sometimes fails | ✅ |
| LayoutInflater.from() | ✅ | ✅ |
| Store in Singleton | ✅ (only app) | ❌ Leak risk |
| Store in Static | ✅ (only app) | ❌ Leak risk |
| Pass to Thread | ✅ | ❌ Leak risk |

---

## Context Lifetime Matching

### Golden Rule

```
SAFE: Context Lifetime >= Code Lifetime

Unsafe:
Context [---Activity---]
Code    [--------Thread---------]
                    ❌ Context dies, code still running
                    
Safe:
Context [----App Lifetime----]
Code    [---Activity-time-]
        ✅ Context lives longer
```

### Example: Global Listener

```kotlin
// ❌ WRONG
class GlobalListener(val context: Activity) {
    fun listen() {
        // context dies when Activity destroyed
        // Code still tries to use it
    }
}

// ✅ CORRECT
class GlobalListener(val context: Context) {
    fun listen() {
        if (context is Application) {
            // Safe - app context
        }
    }
}

// Usage
GlobalListener(applicationContext)  // Safe
GlobalListener(this)  // Depending on usage, might leak
```

---

## Best Practices

### 1. Prefer Application Context by Default

```kotlin
// Start with app context
val context = applicationContext

// Only use Activity context if UI operation required
if (needsDialog) {
    // OK to use Activity context for short operation
}
```

### 2. Never Store Activity Context in Singleton

```kotlin
// ❌ WRONG
object MySingleton {
    var activity: Activity? = null
}

// ✅ CORRECT
object MySingleton {
    var context: Context? = null
    
    fun setContext(context: Context) {
        this.context = context.applicationContext
    }
}
```

### 3. Use WeakReference for Long-Lived References

```kotlin
class MyService(activity: Activity) {
    private val activityRef = WeakReference(activity)
    
    fun doWork() {
        val activity = activityRef.get()
        if (activity != null) {
            // Use activity if still alive
        }
    }
}
```

### 4. Unregister All Listeners

```kotlin
override fun onDestroy() {
    // Unregister ALL listeners
    unregisterReceiver(myReceiver)
    eventBus.unregister(this)
    sensorManager.unregisterListener(mySensorListener)
    
    super.onDestroy()
}
```

### 5. Remove Pending Handler Messages

```kotlin
override fun onDestroy() {
    handler.removeCallbacksAndMessages(null)
    super.onDestroy()
}
```

### 6. Use ViewModel Instead of Storing Context

```kotlin
// ✅ BETTER
class MyViewModel : ViewModel() {
    val data = MutableLiveData<String>()
}

// ❌ OLD WAY
class MyService(val activity: Activity) {
    // Activity reference can leak
}
```

---

## Detecting Context Leaks

### LeakCanary

```gradle
debugImplementation 'com.squareup.leakcanary:leakcanary-android:2.12'
```

**Usage:**
- Automatically detects Activity leaks
- Shows leak chain in logcat
- One of the best tools for this

### Android Studio Profiler

1. Open Profiler
2. Start app
3. Perform actions (rotate, navigate)
4. Force GC
5. Check Memory tab
6. Look for retained objects

### Manual Detection

```kotlin
// After activity destroyed, check logcat
getContext().getString(R.string.app_name)  // If this works: leak

// Activity should be garbage collected by now
```

---

## Key Takeaways

✅ Application Context = app-wide, safe for singletons

✅ Activity Context = tied to Activity, can show UI

✅ Never store Activity Context in long-lived objects

✅ Use WeakReference if you must hold Activity reference

✅ Always unregister listeners in onDestroy()

✅ Match Context lifetime to code lifetime

✅ Prefer app context unless UI operation required

✅ Use LeakCanary to detect leaks automatically

