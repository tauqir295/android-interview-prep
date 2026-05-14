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
# ANR and Performance Deep Dive

## Overview

ANR (Application Not Responding) occurs when the main thread blocks too long. The OS detects unresponsiveness and kills the app. Understanding main thread work, threading models, and performance profiling is crucial for shipping responsive Android apps.

---

## ANR Fundamentals

### What is ANR?

**ANR = Main Thread blocks > Timeout threshold**

OS detects main thread blocked → Kills app → "App not responding" dialog

### Timeout Thresholds

| Component | Timeout |
|-----------|---------|
| Foreground Activity | 5 seconds |
| Foreground Service | 5 seconds |
| Background Service | 60 seconds |
| Broadcast Receiver | 10 seconds |
| Content Provider | 10 seconds |

### When ANR Triggered

**Example: 5-second block in foreground Activity**

```
t=0s: User taps button
      onClick() starts heavy operation
      
t=5s: Main thread still blocked
      OS detects no response
      
t=5s: ANR kill triggered
      App process terminated
      
      System shows:
      "AppName has stopped responding"
      User can close or wait
```

### Consequences

- App crashes
- Bad review
- Users uninstall
- Play Store penalties
- Lost time investment

---

## Main Thread Responsibilities

### What Main Thread Does

1. **Handle User Input**
   - Tap, scroll, swipe
   - Must respond immediately (<100ms perceived)

2. **Update UI**
   - Draw to screen
   - Update views
   - Animations

3. **Render Frames**
   - 60fps = 16.67ms per frame
   - 90fps = 11.11ms per frame
   - 120fps = 8.33ms frametime

4. **Process System Messages**
   - Lifecycle callbacks
   - System broadcasts
   - Messages from Handler

### Why NOT to Block Main Thread

If main thread blocked for I/O:

```
t=0s: Network request starts on main thread
t=0s-5s: BLOCKED
       - Input events queued (UI feels frozen)
       - Frames skipped (animation stutters)
       - User can't scroll

t=5s: ANR kill
```

---

## Blocking Operations (What NOT to do)

### Network I/O

```kotlin
// ❌ WRONG - ANR risk
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    
    // This blocks main thread!
    val response = URL("https://api.example.com/data").readText()
    updateUI(response)
}
```

### File I/O

```kotlin
// ❌ WRONG - ANR risk
val file = File("/path/to/large/file")
val data = file.readBytes()  // Blocks! Could be seconds
```

### Database Queries

```kotlin
// ❌ WRONG on main thread
val users = database.userDao().getAllUsers()  // Room blocks main thread
displayUsers(users)
```

### Heavy Computation

```kotlin
// ❌ WRONG
val result = expensiveAlgorithm(largeDataset)  // Can take seconds
```

### Image Processing

```kotlin
// ❌ WRONG
val bitmap = BitmapFactory.decodeFile(largImagePath)  // Decoding slow
imageView.setImageBitmap(bitmap)
```

---

## Solutions: Threading Models

### Solution 1: Plain Thread

```kotlin
// ✅ CORRECT - off main thread
Thread {
    val response = URL("https://api.example.com/data").readText()
    
    // Post back to main thread for UI
    runOnUiThread {
        updateUI(response)
    }
}.start()
```

**Downside:** Manual management, verbose, error-prone

### Solution 2: AsyncTask (Legacy)

```kotlin
// ✅ CORRECT but deprecated
class FetchDataTask : AsyncTask<Void, Void, String>() {
    override fun doInBackground(vararg params: Void?): String {
        // Background thread
        return URL("https://api.example.com/data").readText()
    }
    
    override fun onPostExecute(result: String) {
        // Main thread
        updateUI(result)
    }
}

FetchDataTask().execute()
```

### Solution 3: Coroutines (BEST - MODERN)

```kotlin
// ✅ CORRECT - recommended
viewModelScope.launch {
    try {
        // Switched to IO dispatcher automatically
        val data = withContext(Dispatchers.IO) {
            URL("https://api.example.com/data").readText()
        }
        
        // Back on main dispatcher
        updateUI(data)
    } catch (e: Exception) {
        showError(e)
    }
}
```

**Why coroutines best:**
- Clean, readable syntax
- Automatic cancellation with scope
- Exception handling
- Less boilerplate

### Solution 4: LiveData + Repository

```kotlin
// ✅ CORRECT Architecture
class MyViewModel : ViewModel() {
    val data = dataRepository.observeData()  // LiveData
}

class DataRepository {
    fun observeData(): LiveData<Data> =
        liveData(Dispatchers.IO) {
            emit(fetchFromNetwork())  // Off main thread
        }
}

// Activity
viewModel.data.observe(this) { data ->
    updateUI(data)  // Main thread
}
```

---

## Jank and Frame Timing

### What is Jank?

**Jank = Visible stutter in UI, animation, scroll**

Root cause: Dropping frames due to main thread blocking

### Frame Timing Budget

```
60fps device:
  Frame time budget = 16.67ms
  
If main thread work > 16.67ms:
  Frame skipped
  User sees stutter
  = JANK

Multiple frames > budget:
  Multiple stutters
  Looks very janky
```

### Example: Janky Scroll

```
Frame 1: 10ms (✓ on time)
Frame 2: 5ms (✓ on time)
Frame 3: 25ms (❌ late - frame dropped, stutter visible)
Frame 4: 8ms (✓ on time)
Frame 5: 30ms (❌ late - stutter again)

Result: Janky scrolling experience
```

### Causes of Jank

1. **Heavy computation on main thread**
2. **Inefficient view hierarchy**
   - Too many views to measure/layout
   - Nested layouts
3. **Overdraw**
   - Drawing same pixels multiple times
4. **Memory pressure**
   - GC pauses
   - Excessive allocations
5. **I/O on main thread**
   - Reading files
   - Database queries
6. **Bitmap scaling/processing**
   - Not in background
7. **Layout thrashing**
   - Measuring in draw pass
8. **Large view animations**
   - Complex transformations

---

## Measuring Performance

### 1. Profile GPU Rendering (Device Settings)

```
Settings → Developer options → Profile GPU rendering → On screen as bars

Each bar represents one frame:
  Green = Good (under 16.67ms)
  Yellow = Warning (approaching deadline)
  Red = Bad (over deadline, frame dropped)
```

### 2. Android Studio Profiler

```
1. Run app
2. Android Studio → Profiler
3. Record CPU/Memory/etc
4. View frame times graph
5. Identify slow frames
```

### 3. Layout Inspector

```
1. Run app
2. Tools → Layout Inspector
3. See view hierarchy
4. Identify excessive nesting
```

### 4. Systrace

```bash
# Record trace
python systrace.py gfxinfo view -o trace.html

# Open HTML file in browser
# View frame rendering timeline
```

### 5. FrameMetrics API

```kotlin
// Programmatically measure frame times
onFrameMetricsAvailable { metrics ->
    val frameDuration = metrics.getMetric(FrameMetricsAggregator.TOTAL_INDEX)
    Log.d("Frame", "Duration: $frameDuration ms")
}
```

---

## Optimization Strategies

### 1. Reduce View Hierarchy

```kotlin
// ❌ Many nested layouts
<LinearLayout>
    <LinearLayout>
        <LinearLayout>
            <View/>
        </LinearLayout>
    </LinearLayout>
</LinearLayout>

// ✅ Flat hierarchy
<FrameLayout>
    <View/>
</FrameLayout>
```

### 2. Use Efficient Collections

```kotlin
// In RecyclerView
val notifyList = mutableListOf<Int>()  // Always notifyDataSetChanged

// ✅ Better: notify specific items
notifyItemRangeChanged(0, 5)
```

### 3. Lazy Load Data

```kotlin
// ✅ Show loading placeholder first
// Load full data in background
// Update when ready
```

### 4. Defer Non-Critical Work

```kotlin
// ✅ Defer analytics
analyticsQueue.add(event)
// Send later, not immediately
```

### 5. Use Smaller Images

```kotlin
// ❌ Load full size (2000x2000)
val bitmap = BitmapFactory.decodeResource(resources, R.drawable.large)

// ✅ Load optimized size
val options = BitmapFactory.Options().apply {
    inSampleSize = 4  // 1/4 size
}
val bitmap = BitmapFactory.decodeResource(resources, R.drawable.large, options)
```

---

## Common ANR Scenarios

### Scenario 1: Network Call on Main

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    
    // ❌ Can block 5+ seconds
    val response = httpClient.newCall(request).execute().body()?.string()
}
```

**Fix:** Use coroutines
```kotlin
viewModelScope.launch {
    val response = withContext(Dispatchers.IO) {
        httpClient.newCall(request).execute().body()?.string()
    }
    updateUI(response)
}
```

### Scenario 2: Database Query on Main

```kotlin
// ❌ Room blocks on main thread by default on older versions
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    val users = database.userDao().loadAllUsers()  // Blocks!
}
```

**Fix:** Use LiveData
```kotlin
class UserViewModel : ViewModel() {
    val users = database.userDao().getAllUsersLive()  // Returns LiveData
}

// In Activity
viewModel.users.observe(this) { users ->
    updateUI(users)
}
```

### Scenario 3: ContentResolver Query

```kotlin
// ❌ CAN block many seconds
override fun onCreate(savedInstanceState: Bundle?) {
    val cursor = contentResolver.query(
        ContactsContract.Contacts.CONTENT_URI,
        null, null, null, null
    )  // Might have thousands of contacts!
}
```

**Fix:** Query on background thread
```kotlin
viewModelScope.launch(Dispatchers.IO) {
    val contacts = loadContactsFromProvider()
    
    withContext(Dispatchers.Main) {
        displayContacts(contacts)
    }
}
```

---

## Key Takeaways

✅ ANR = Main thread blocked > timeout

✅ Keep main thread operations < 100-200ms

✅ Never do network, I/O, heavy computation on main thread

✅ Use coroutines (best), AsyncTask (old), or plain threads

✅ Measure with Profiler or GPS rendering

✅ Reduce view hierarchy depth

✅ Lazy load non-critical data

✅ Profile before optimizing

