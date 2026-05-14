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

# Memory Leaks Deep Dive

## Overview

A memory leak in Android occurs when an object is no longer needed but remains referenced, preventing garbage collection. The result is growing memory usage, eventual OutOfMemoryError, and app crashes. Android-specific leaks often involve holding Context or Activity references in long-lived objects.

---

## Memory Management Basics

### Garbage Collector & Reachability

**How GC Works:**
```
1. Mark phase: Find all reachable objects from GC roots
2. Sweep phase: Delete unreachable objects
3. Compact phase: Reorder memory

Unreachable objects = collected
Still referenced objects = kept in memory (even if unused)
```

### GC Roots (What keeps objects alive)

```
├─ Running threads
├─ Stack variables (local scope)
├─ Static references
├─ JNI references
├─ Monitored objects
└─ System classes
```

### Memory Leak Definition

```
Object A no longer needed
But still referenced by Object B
Object B still referenced by active code
Result: A never garbage collected → LEAK
```

---

## Common Android Leak Patterns

### Pattern 1: Static Reference to Activity

```kotlin
class MyAnalytics {
    companion object {
        var activity: Activity? = null  // ❌ LEAK
    }
    
    fun trackEvent() {
        activity?.let { act ->
            // Activity reference never released
        }
    }
}

// In MainActivity
override fun onCreate() {
    MyAnalytics.activity = this
    // Activity destroyed, but MyAnalytics.activity still holds reference
}
```

**Leak Chain:**
```
MyAnalytics.activity → MainActivity (static ref)
                    → Views
                    → Resources
                    ❌ ALL LEAKED
```

**Fix:**
```kotlin
companion object {
    var context: Context? = null  // Use app context instead
}

override fun onCreate() {
    MyAnalytics.context = applicationContext  // Won't leak
}
```

### Pattern 2: Inner Class Holding Outer Activity

```kotlin
class MyActivity : AppCompatActivity() {
    inner class MyThread : Thread() {  // ❌ LEAK
        override fun run() {
            Thread.sleep(60000)
            // During sleep, implicit 'this@MyActivity' ref held
        }
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        MyThread().start()  // Activity held for 60 seconds
    }
}
```

**Leak Chain:**
```
MyThread → (implicit this$0) → MyActivity → All resources
```

**Fix:**
```kotlin
private static class MyThread extends Thread {  // Static = no implicit Activity ref
    private final WeakReference<MyActivity> activityRef;
    
    MyThread(MyActivity activity) {
        this.activityRef = new WeakReference<>(activity);
    }
    
    override fun run() {
        val activity = activityRef.get()  // May be null if GC'd
        if (activity != null) {
            // Use activity
        }
    }
}
```

### Pattern 3: Handler with Delayed Messages

```kotlin
class MyActivity : AppCompatActivity() {
    private val handler = Handler(Looper.getMainLooper())
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        handler.postDelayed({
            // Runnable implicitly holds 'this' Activity reference
            updateUI()  // This runs 60s later
        }, 60000)
    }
    
    override fun onDestroy() {
        super.onDestroy()
        // ❌ If not removed, Activity leaked for 60s
    }
}
```

**Leak Chain:**
```
Handler.MessageQueue → Message → Callback (Runnable)
                                          → (implicit this) → Activity
```

**Fix:**
```kotlin
override fun onDestroy() {
    handler.removeCallbacksAndMessages(null)  // Remove pending messages
    super.onDestroy()
}

// OR use coroutines (auto-cleanup)
viewModel.doWork()  // Auto-cancelled when Activity destroyed
```

### Pattern 4: Unregistered Listener/Broadcast Receiver

```kotlin
class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        eventBus.register(this)  // ❌ If never unregistered
        
        // Activity destroyed but still registered
        // EventBus holds reference → Activity can't be GC'd
    }
    
    // ❌ onDestroy never called, or unregister missing
}
```

**Fix:**
```kotlin
override fun onDestroy() {
    eventBus.unregister(this)
    super.onDestroy()
}
```

### Pattern 5: Long-Lived Singleton Holding Activity Context

```kotlin
object MySingleton {
    var context: Context? = null  // Activity context stored
}

class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        MySingleton.context = this  // ❌ Activity stored in singleton
        // Activity destroyed but singleton still holds reference
    }
}
```

**Fix:**
```kotlin
object MySingleton {
    var context: Context? = null
}

class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        MySingleton.context = applicationContext  // App context - safe
    }
}
```

---

## WeakReference vs SoftReference

### WeakReference

```kotlin
val weakRef = WeakReference<Activity>(activity)

// Usage
val activity = weakRef.get()
if (activity != null) {
    activity.doSomething()
}
// If no strong reference elsewhere, GC collects immediately
```

**When to use:** 
- Storing references to Activities
- Objects that can be recreated
- Short-term caching

### SoftReference

```kotlin
val softRef = SoftReference<Bitmap>(bitmap)

// Usage
val bitmap = softRef.get()
if (bitmap != null) {
    drawBitmap(bitmap)
}
// GC keeps alive unless memory pressure
```

**When to use:**
- Image caches
- Objects expensive to recreate
- Long-term caching

---

## Detection Tools

### LeakCanary (BEST TOOL)

**Setup:**
```gradle
debugImplementation 'com.squareup.leakcanary:leakcanary-android:2.12'
```

**Features:**
- Automatically detects Activity leaks
- Shows leak chain in logcat
- Provides fix suggestions
- No code changes needed

**How it works:**
```
1. Watches destroyed activities
2. Forces GC
3. Checks if still in memory
4. If yes: Dumps heap, analyzes leak chain
```

### Android Studio Memory Profiler

```
1. Run app in debuggable mode
2. Open Android Studio → Profiler
3. Click Memory section
4. Perform rotations, navigate, etc
5. Force garbage collection (GC button)
6. Inspect heap dump
7. Look for retained Activities
```

### Logcat Monitoring

```bash
adb logcat | grep -i "finalize"
adb logcat | grep -i "OutOfMemory"
adb logcat | grep -i "leak"
```

### Manual Detection (Monkey Testing)

```kotlin
// Rotate device multiple times while app running
// Watch memory in Profiler
// Check if memory grows unbounded
```

---

## Prevention Strategies

### 1. Context Usage

```kotlin
// ✅ Use application context for singletons/long-lived objects
val context = applicationContext

// ❌ Don't store Activity context in singletons
companion object {
    var activity: Activity? = null  // WRONG
}
```

### 2. Static Inner Classes with WeakReference

```kotlin
// ✅ Correct pattern for holding Activity reference
private static class MyTask extends AsyncTask {
    private final WeakReference<MyActivity> activityRef;
    
    MyTask(MyActivity activity) {
        this.activityRef = new WeakReference<>(activity);
    }
    
    protected void onPostExecute(Result result) {
        MyActivity activity = activityRef.get();
        if (activity != null) {
            activity.updateUI(result);
        }
    }
}
```

### 3. Always Unregister Listeners

```kotlin
override fun onResume() {
    super.onResume()
    eventBus.register(this)
}

override fun onPause() {
    eventBus.unregister(this)
    super.onPause()
}
```

### 4. Remove Handler Messages

```kotlin
override fun onDestroy() {
    handler.removeCallbacksAndMessages(null)
    super.onDestroy()
}
```

### 5. Use Lifecycle-Aware Components

```kotlin
// ✅ ViewModel + LiveData (auto lifecycle aware)
viewModel.data.observe(this) { data ->
    updateUI(data)
}

// ❌ Manual subscription (must unsubscribe)
subscription = dataSource.subscribe { data ->
    updateUI(data)
}
override fun onDestroy() {
    subscription.dispose()
}
```

### 6. Clean Up Binding References

```kotlin
private var binding: ActivityBinding? = null

override fun onDestroyView() {
    binding = null  // Null out binding
    super.onDestroyView()
}
```

### 7. Don't Pass Activity to Threads

```kotlin
// ❌ WRONG
Thread {
    val activity: Activity = this@MyActivity
    Thread.sleep(60000)
    activity.updateUI()
}.start()

// ✅ CORRECT: Use WeakReference
val threadSafe = Thread {
    val ref = WeakReference(this@MyActivity)
    Thread.sleep(60000)
    ref.get()?.updateUI()
}.apply { start() }
```

---

## Production Monitoring

### Firebase Performance Monitoring

```kotlin
val memory = Runtime.getRuntime().let {
    (it.totalMemory() - it.freeMemory()) / 1024 / 1024
}
Analytics.log("memory_used_mb", memory.toDouble())
```

### Custom Memory Tracking

```kotlin
fun trackMemory(tag: String) {
    val runtime = Runtime.getRuntime()
    val usedMemory = (runtime.totalMemory() - runtime.freeMemory()) / 1024 / 1024
    Log.d(tag, "Memory: $usedMemory MB")
}

// In various lifecycle methods
override fun onPause() {
    trackMemory("onPause")
    super.onPause()
}
```

---

## Interview Knowledge

**Q: What's the difference between OutOfMemoryError and memory leak?**
A: Memory leak = unused object still referenced (prevents GC)
   OOM = not enough memory left to allocate new objects
   Leaks cause OOM if allowed to accumulate

**Q: Does assigning null prevent leaks?**
A: No, if object still referenced elsewhere, it's still a leak

**Q: Why not always use WeakReference?**
A: Weak references can be GC'd at any time
   Use only when cleanup acceptable
   For critical objects, hold strong references

---

## Key Takeaways

✅ Leak = unused object still referenced

✅ Common: Static refs, unregistered listeners, stored contexts

✅ LeakCanary = best tool for detection

✅ Use application context for long-lived objects

✅ Always unregister listeners/receivers in onDestroy()

✅ Use WeakReference for Activity references

✅ Remove Handler messages in onDestroy()

✅ Use ViewModel/LiveData instead of manual management

