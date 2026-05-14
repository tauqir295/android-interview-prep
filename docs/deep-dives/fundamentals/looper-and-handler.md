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
# Looper and Handler Deep Dive

## Overview

Looper and Handler enable thread-safe message passing in Android. Looper processes messages in a queue, Handler sends messages to that queue and executes them on a specific thread. This is the foundation for multi-threading and the Binder system.

---

## Looper Architecture
### What is Looper?
A Looper is a thread mechanism that:
1. Maintains a message queue
2. Continuously loops through it (hence "Looper")
3. Processes messages one at a time
4. Blocks when queue empty
```kotlin
// Looper lifecycle
Looper.prepare()           // Create Looper for thread
// ...do work...
Looper.loop()              // Start infinite loop
// Code after loop() never reached until quit()
```
### Main Thread Looper
The main thread automatically has a Looper:
```kotlin
// In ActivityThread (Android framework)
fun main(args: Array<String>) {
    Looper.prepareMainLooper()
    // ... create activities ...
    Looper.loop()
}
```
### Background Thread Looper
```kotlin
Thread {
    Looper.prepare()       // Create Looper for this thread
    val handler = Handler()  // Handler uses this thread's Looper
    // Do work, Handler messages will be processed
    Looper.loop()          // Start processing messages
}.start()
```
### Each Thread Max 1 Looper
```kotlin
// ❌ WRONG - second Looper.prepare() throws exception
Looper.prepare()
Looper.prepare()  // RuntimeException: already prepared
// ✅ CORRECT - 1 per thread max
Looper.prepare()
Looper.loop()  // Process messages on this thread
// After loop() returns, Looper.quit() was called
```
---
## Handler Deep Dive
### What is Handler?
Handler sends messages to a Looper's queue and executes callbacks on that Looper's thread.
```kotlin
// Create handler attached to main thread Looper
val mainHandler = Handler(Looper.getMainLooper())
// Create handler attached to current thread's Looper
val localHandler = Handler()
// Send work to execute on that thread
mainHandler.post {
    updateUI()  // Runs on main thread
}
```
### Handler Operations
**post() - Execute Runnable immediately**
```kotlin
handler.post(Runnable { doWork() })
```
**postDelayed() - Execute after delay**
```kotlin
handler.postDelayed(
    Runnable { doWork() },
    5000  // 5 seconds
)
```
**postAtTime() - Execute at specific time**
```kotlin
handler.postAtTime(
    Runnable { doWork() },
    SystemClock.uptimeMillis() + 5000
)
```
**sendMessage() - Send Message object**
```kotlin
val msg = Message.obtain().apply {
    what = MSG_UPDATE_UI
    arg1 = userId
}
handler.sendMessage(msg)
```
**sendDelayedMessage()**
```kotlin
handler.sendMessageDelayed(msg, 5000)
```
---
## HandlerThread
### What is HandlerThread
HandlerThread is a Thread subclass that automatically creates and starts a Looper.
```kotlin
// ❌ Manual Looper setup
val thread = Thread {
    Looper.prepare()
    val handler = Handler()
    // do work
    Looper.loop()
}
thread.start()
// ✅ Simpler with HandlerThread
val handlerThread = HandlerThread("MyThread")
handlerThread.start()
val handler = Handler(handlerThread.looper)
```
### HandlerThread Use Cases
**Background Image Processing:**
```kotlin
val backgroundThread = HandlerThread("ImageProcessing")
backgroundThread.start()
val imageHandler = Handler(backgroundThread.looper)
imageHandler.post {
    val bitmap = processBitmap(largeImage)
    mainHandler.post { displayBitmap(bitmap) }
}
```
**Database Operations:**
```kotlin
val dbThread = HandlerThread("DatabaseIO")
dbThread.start()
val dbHandler = Handler(dbThread.looper)
dbHandler.post {
    val user = database.userDao().loadUser(userId)
    mainHandler.post { displayUser(user) }
}
```
### Cleanup Important
```kotlin
override fun onDestroy() {
    handlerThread.quit()  // Or quitSafely()
    super.onDestroy()
}
```
---
## Handler Memory Leaks
### The Problem
Delayed Handler messages can leak Activity context:
```kotlin
class MyActivity : AppCompatActivity() {
    private val handler = Handler(Looper.getMainLooper())
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Post delayed message
        handler.postDelayed({
            updateUI()  // Implicit 'this' reference
        }, 60000)
    }
    override fun onDestroy() {
        // ❌ Activity destroyed but message still in queue
        // Message queued for 60 seconds holds Activity reference
        super.onDestroy()
    }
}
```
**Leak chain:**
```
Handler.MessageQueue → Message → Callback (Runnable with 'this')
                                  ↓
                              MyActivity (cannot GC)
                                  ↓
                              Views, resources (leaked)
```
### Solution 1: Remove Messages in onDestroy()
```kotlin
override fun onDestroy() {
    handler.removeCallbacksAndMessages(null)  // Remove all pending
    super.onDestroy()
}
```
### Solution 2: WeakReference Handler
```kotlin
class MyWeakHandler(activity: MyActivity) : Handler(Looper.getMainLooper()) {
    private val activityRef = WeakReference(activity)
    override fun handleMessage(msg: Message) {
        val activity = activityRef.get()
        if (activity != null) {
            // Use activity
        }
    }
}
// Usage
val handler = MyWeakHandler(this)
```
### Solution 3: Use Coroutines (BEST)
```kotlin
// Coroutines handle cleanup automatically
viewModelScope.launch {
    delay(60000)
    updateUI()  // Auto-cancels if Activity destroyed
}
```
---
## Message and MessageQueue
### Message Object
```kotlin
data class Message(
    val what: Int = 0,              // Message type
    val arg1: Int = 0,              // Additional data
    val arg2: Int = 0,              // Additional data
    val obj: Any? = null,           // Payload
    val replyTo: Messenger? = null  // Reply to address
)
```
### MessageQueue
```
What it is:
├─ Infinite queue of Messages
├─ Added via Handler.sendMessage()
├─ Processed by Looper one at a time
└─ Ordered by time/priority
```
### Processing Order
```
Queue:
[Message 1 @ t=0]
[Message 2 @ t=50]
[Message 3 @ t=100]
Looper processes in order:
t=0: Message 1 executed
t=50: Message 2 executed
t=100: Message 3 executed
```
---
## Common Patterns
### Cross-Thread Communication
```kotlin
// Thread 1 (Background)
Thread {
    Looper.prepare()
    val bgHandler = Handler()
    mainHandler.post {
        // Signal to main thread
        updateUI("Done")
    }
    Looper.loop()
}.start()
```
### HandlerThread + Handler
```kotlin
val workerThread = HandlerThread("Worker")
workerThread.start()
val workerHandler = Handler(workerThread.looper)
workerHandler.post {
    // This runs on worker thread
    val data = heavyComputation()
    // Post back to main
    mainHandler.post {
        displayResult(data)
    }
}
```
---
## Interview Q&A
**Q: Why use Handler instead of just Thread.join()?**
A: Handler enables message-driven architecture. join() blocks caller. Handler queues work for later.
**Q: Can you have multiple Handlers on one Looper?**
A: Yes! Multiple Handlers can post to same Looper's queue.
**Q: What happens if you call Looper.loop() twice?**
A: RuntimeException - already preparing.
**Q: Is Looper thread-safe?**
A: MessageQueue is thread-safe. Can post from any thread, executes on Looper's thread.
---
## Key Takeaways
✅ Looper = message queue processor on a thread
✅ Handler = sends messages to Looper's queue
✅ HandlerThread = Thread with automatic Looper
✅ Main thread has Looper automatically
✅ postDelayed() can leak if not removed
✅ Use removeCallbacksAndMessages() in onDestroy()
✅ Coroutines often better than manual Handler management
