---
hide:
  - toc
---

# Performance

<script>
(function () {
  function openQuestionFromHash() {
    const hash = window.location.hash;
    if (!hash || hash.length <= 1) return;

    const anchor = document.querySelector(hash);
    if (!anchor) return;

    let node = anchor.nextElementSibling;
    while (node) {
      if (node.tagName === 'DETAILS') {
        node.open = true;
        anchor.scrollIntoView({ behavior: 'auto', block: 'start' });
        return;
      }
      node = node.nextElementSibling;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', openQuestionFromHash);
  } else {
    openQuestionFromHash();
  }

  window.addEventListener('hashchange', openQuestionFromHash);
})();
</script>


---

<div id="android-performance-fundamentals"></div>

## What are the main performance metrics in Android?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">metrics</span>
  <span class="question-badge question-badge--tag">monitoring</span>
</div>

??? question "View Answer"

    Key Android performance metrics:
    FPS/Jank:
    - FPS (frames per second): smooth 60 FPS target
    - Jank: frame drops below 60 FPS
    Memory:
    - Heap size: total allocated
    - PSS: proportional set size
    Battery & Network:
    - Battery drain rate
    - Network latency
    - Data usage
    Startup:
    - Cold start: app launch from dead
    - Warm start: from background


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/performance-metrics/#android-performance-fundamentals">🚀 See Full Deep Dive</a>


---

<div id="jank-and-ui-drops"></div>

## What causes jank and how do you fix it?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">ui</span>
  <span class="question-badge question-badge--tag">jank</span>
</div>

??? question "View Answer"

    Jank = frame drops below 60 FPS (16.6ms per frame).
    Common causes:
    - Heavy computation on main thread
    - Too many allocations (GC pauses)
    - Expensive layout passes
    - Slow drawing operations
    - Blocking I/O
    Fixes:
    - Move work to background thread
    - Reduce allocation rate
    - Optimize layouts (flatten hierarchy)
    - Use Hardware acceleration
    - Implement proper caching


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/jank-and-frame-drops/#jank-and-ui-drops">🚀 See Full Deep Dive</a>


---

<div id="memory-leaks"></div>

## What is a memory leak and how do you find them?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">memory</span>
  <span class="question-badge question-badge--tag">leaks</span>
  <span class="question-badge question-badge--tag">debugging</span>
</div>

??? question "View Answer"

    Memory leak = object not released when no longer needed.
    Common causes:
    - Static references to context
    - Inner classes holding outer reference
    - Listener/callback not unregistered
    - Handler posting delayed messages
    Detection tools:
    - LeakCanary library (automatic)
    - Android Profiler memory tab
    - Heap dumps + MAT analysis
    Prevention:
    - Use WeakReference for context
    - Unregister listeners in onDestroy
    - Avoid anonymous inner classes
    - Cancel delayed messages


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/memory-leaks/#memory-leaks">🚀 See Full Deep Dive</a>


---

<div id="garbage-collection"></div>

## How does garbage collection work in Android?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">memory</span>
  <span class="question-badge question-badge--tag">gc</span>
  <span class="question-badge question-badge--tag">runtime</span>
</div>

??? question "View Answer"

    GC (Garbage Collection) frees unused memory.
    Android ART uses:
    - Mark-sweep: pause app, scan heap
    - Generational GC: young objects collected more
    - CMS: marks while app runs
    GC pause impacts:
    - Causes frame drops (jank)
    - Allocation rate = GC frequency
    - Reduce allocations = fewer pauses
    Profile with:
    - Memory Profiler timeline
    - Logcat GC events
    - Perfetto for detailed events


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/memory-management/#garbage-collection">🚀 See Full Deep Dive</a>


---

<div id="battery-optimization"></div>

## How do you optimize battery usage?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">battery</span>
  <span class="question-badge question-badge--tag">optimization</span>
  <span class="question-badge question-badge--tag">power</span>
</div>

??? question "View Answer"

    Battery drain sources:
    - CPU compute
    - Screen brightness/duration
    - Networking (WiFi/cellular)
    - GPS/sensors
    - Location polling
    Optimization strategies:
    - Batch network requests (not individual)
    - Use Doze mode (WorkManager scheduling)
    - Reduce location precision
    - Disable sensors when not needed
    - Use push instead of polling
    - Aggregate sensor updates
    Tools:
    - Battery Historian
    - Perfetto energy profiling


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/battery-optimization/#battery-optimization">🚀 See Full Deep Dive</a>


---

<div id="rendering-pipeline"></div>

## What is Android rendering pipeline?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">rendering</span>
  <span class="question-badge question-badge--tag">graphics</span>
  <span class="question-badge question-badge--tag">pipeline</span>
</div>

??? question "View Answer"

    Android rendering (60-120 FPS):
    Phases:
    1. Input: user touch/events
    2. Animation: animate values
    3. Measure: calculate sizes
    4. Layout: position views
    5. Draw: render to bitmap
    6. Sync: GPU upload
    7. Display: swap buffers
    Budget: 8.3ms (120 FPS) to 16.6ms (60 FPS)
    Optimization:
    - Reduce draw complexity
    - Simplify layouts (flatten hierarchy)
    - Use hardware acceleration
    - Minimize redraws


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/rendering-pipeline/#rendering-pipeline">🚀 See Full Deep Dive</a>


---

<div id="overdraw"></div>

## What is overdraw and how do you detect it?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">rendering</span>
  <span class="question-badge question-badge--tag">overdraw</span>
  <span class="question-badge question-badge--tag">debugging</span>
</div>

??? question "View Answer"

    Overdraw = drawing pixels multiple times per frame.
    Example:
    - Background color filled
    - Card drawn on top (re-fills)
    - Text drawn on top (re-fills again)
    Detection:
    - Developer Options: Show GPU overdraw
    - Perfetto GPU profiling
    - Visual: areas glow bright
    Fixes:
    - Remove unnecessary backgrounds
    - Merge layers where possible
    - Use `clipRect` to limit drawing
    - Clip non-visible areas


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/rendering-optimization/#overdraw">🚀 See Full Deep Dive</a>


---

<div id="app-startup-time"></div>

## How do you reduce app startup time?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">startup</span>
  <span class="question-badge question-badge--tag">cold-start</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Startup phases:
    1. Process creation: Zygote fork
    2. App launch: onCreate()
    3. Activity: layout inflation
    4. First frame: rendering
    Optimization:
    - Defer heavy initialization
    - Use lazy initialization
    - Prewarm VMs on startup
    - Reduce layout complexity
    - Use App Startup library
    Profiling:
    - `adb shell am start -W` timing
    - Android Studio Profiler
    - Perfetto startup trace


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/app-startup/#app-startup-time">🚀 See Full Deep Dive</a>


---

<div id="memory-profiling"></div>

## How do you profile memory usage?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">memory</span>
  <span class="question-badge question-badge--tag">profiling</span>
  <span class="question-badge question-badge--tag">tools</span>
</div>

??? question "View Answer"

    Memory profiling tells where RAM goes.
    Tools:
    - Android Profiler: real-time memory
    - LeakCanary: automatic leak detection
    - Heap Dumps: snapshot analysis
    - MAT: heap dump deep dive
    - dumpsys: command-line info
    Key metrics:
    - Heap: app allocated memory
    - Native: C++ allocations
    - Graphics: GPU memory
    - Stack: thread stacks
    Workflow:
    1. Record memory profile
    2. Force GC
    3. Identify retained objects
    4. Check references (backpointers)
    5. Fix retention chains


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/memory-profiling/#memory-profiling">🚀 See Full Deep Dive</a>


---

<div id="cpu-profiling"></div>

## How do you profile CPU usage?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">cpu</span>
  <span class="question-badge question-badge--tag">profiling</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    CPU profiling shows processor time usage.
    Methods:
    - Sampled: interrupt periodically (~1000Hz)
    - Instrumented: log entry/exit
    - Method tracing: record call stacks
    Tools:
    - Android Profiler CPU tab
    - Perfetto: system-wide tracing
    - Simpleperf: low-overhead
    What to find:
    - Hot methods: consuming lots of time
    - Lock contention: threads waiting
    - Allocations: GC triggers
    - System calls: I/O blocking


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/cpu-profiling/#cpu-profiling">🚀 See Full Deep Dive</a>


---

<div id="layout-inflation"></div>

## How does layout inflation work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">layout</span>
  <span class="question-badge question-badge--tag">inflation</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    Layout inflation converts XML to view tree.
    Process:
    1. Parse XML
    2. Create ViewGroup/View objects
    3. Set attributes via reflection
    4. Add to parent
    Performance impact:
    - Creates objects (allocation/GC)
    - Reflection overhead
    - Slower for complex hierarchies
    Optimization:
    - ViewStub: defer inflation
    - Merge: reduces depth
    - Include: reuse layouts
    - Data binding: skip findViewById()
    - Compose: no XML inflation


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/layout-optimization/#layout-inflation">🚀 See Full Deep Dive</a>


---

<div id="anr-prevention"></div>

## What causes ANR and how do you prevent it?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">anr</span>
  <span class="question-badge question-badge--tag">responsiveness</span>
  <span class="question-badge question-badge--tag">threading</span>
</div>

??? question "View Answer"

    ANR (Application Not Responding):
    - Main thread blocked > 5 seconds
    - Broadcast receiver > 10 seconds
    - Service > 20 seconds
    Common causes:
    - Heavy computation on main thread
    - Network I/O blocking
    - Database queries not cached
    - Synchronized blocks with contention
    Prevention:
    - Use background threads (coroutines)
    - Move I/O off main thread
    - Cache expensive computations
    - Use async libraries (Retrofit)
    - Profile with Perfetto


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/anr-prevention/#anr-prevention">🚀 See Full Deep Dive</a>


---

<div id="bitmap-optimization"></div>

## How do you optimize bitmap memory usage?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">bitmap</span>
  <span class="question-badge question-badge--tag">memory</span>
  <span class="question-badge question-badge--tag">images</span>
</div>

??? question "View Answer"

    Bitmaps are large (width × height × 4 bytes).
    Optimization:
    - Downscale: load only needed resolution
    - Compression: use WebP (20-30% smaller)
    - Caching: cache in memory or disk
    - Sample size: decode at 1/2 or 1/4
    - Reuse: recycle old bitmaps
    Glide library handles most:
    - Automatic downscaling
    - Format optimization
    - Memory + disk cache
    - Lifecycle aware
    Avoid:
    - Huge bitmaps into memory
    - Keeping references forever
    - Ignoring OOM exceptions


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/bitmap-optimization/#bitmap-optimization">🚀 See Full Deep Dive</a>


---

<div id="database-performance"></div>

## How do you optimize database queries?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">database</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">room</span>
</div>

??? question "View Answer"

    Database optimization is critical.
    Strategies:
    - Index frequently-queried columns
    - Select only needed columns (not *)
    - Use pagination for large result sets
    - Batch insert/update (not individual)
    - Prepare statements (not ad-hoc SQL)
    - Use ViewModels to cache
    Room-specific:
    - Observe Flow<List<T>> for updates
    - Use @Query with parameters
    - Implement DAO pattern
    - Use database transactions
    Anti-patterns:
    - N+1 queries
    - Loading all data at once
    - Creating new database per query


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/database-optimization/#database-performance">🚀 See Full Deep Dive</a>


---

<div id="network-performance"></div>

## How do you optimize network requests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">network</span>
  <span class="question-badge question-badge--tag">optimization</span>
  <span class="question-badge question-badge--tag">bandwidth</span>
</div>

??? question "View Answer"

    Network is often the bottleneck.
    Optimization:
    - Batch requests (don't spam)
    - Compress responses (gzip)
    - Cache responses (HTTP headers)
    - Use CDN for static assets
    - Implement exponential backoff
    - Minimize payload size
    Monitoring:
    - Network Profiler: timing
    - Check bandwidth consumption
    - Latency baseline for networks
    Mobile-specific:
    - Account for variable latency
    - Implement offline fallback
    - Use Retrofit + OkHttp


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/network-optimization/#network-performance">🚀 See Full Deep Dive</a>


---

<div id="string-formatting"></div>

## What's the performance impact of string formatting?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">strings</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    String operations create allocations (GC).
    Performance (fastest to slowest):
    1. String literal: "hello"
    2. Simple concatenation: "a" + "b"
    3. StringBuilder: sb.append()
    4. String.format(): expensive
    5. String interpolation in loops
    BAD (allocation per loop):
    ```
    for (i in 1..1000) {
      val str = "Item $i"  // NEW allocation
    }
    ```
    GOOD:
    ```
    val sb = StringBuilder()
    for (i in 1..1000) {
      sb.setLength(0)
      sb.append("Item ").append(i)
    }
    ```


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/allocation-optimization/#string-formatting">🚀 See Full Deep Dive</a>


---

<div id="reflection-performance"></div>

## What's the performance cost of reflection?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">reflection</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    Reflection is flexible but slow.
    Cost examples (vs direct call):
    - Class.forName(): ~1000x slower
    - Method.invoke(): ~10-100x slower
    - Field.get(): ~50x slower
    Why so slow:
    - Runtime lookup of class/method/field
    - Security checks
    - No JIT optimization
    When it matters:
    - Called millions of times (NO)
    - Called in hot loops (NO)
    - Cold path (fine)
    - Framework code (unavoidable)
    Optimization:
    - Cache Method objects
    - Avoid in tight loops
    - Use code generation (Room, Dagger)


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/reflection-optimization/#reflection-performance">🚀 See Full Deep Dive</a>


---

<div id="view-recycling"></div>

## How does RecyclerView recycling work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">recyclerview</span>
  <span class="question-badge question-badge--tag">recycling</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    RecyclerView recycles views to save memory.
    Recycling pools:
    - Attached: currently visible
    - Scrap: removed, reusable
    - Cache: recently scrolled off
    - Recycled: available for reuse
    Reuse flow:
    1. Item scrolls out
    2. ViewHolder moves to scrap
    3. onBindViewHolder() called
    4. View updated without recreation
    Benefits:
    - Smooth scrolling (no lag)
    - Memory efficient
    - CPU efficient (no inflation)
    Best practices:
    - Keep onBindViewHolder() fast
    - Avoid heavy layouts per item
    - Use ViewStub for conditional
    - Pre-calculate view sizes


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/recyclerview-optimization/#view-recycling">🚀 See Full Deep Dive</a>


---

<div id="lazy-initialization"></div>

## What is lazy initialization?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">optimization</span>
  <span class="question-badge question-badge--tag">initialization</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Lazy initialization delays object creation.
    Example:
    ```kotlin
    private val expensive: Expensive by lazy {
      Expensive()  // created on first access
    }
    ```
    Benefits:
    - Faster app startup
    - Memory savings
    - Simpler dependency management
    Drawbacks:
    - First access has latency
    - Thread-safe overhead
    Good use cases:
    - Heavy database connections
    - Image caches
    - Analytics SDK
    - ML models
    Bad use cases:
    - UI-critical objects
    - Startup-critical paths


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/initialization-patterns/#lazy-initialization">🚀 See Full Deep Dive</a>


---

<div id="object-pooling"></div>

## What is object pooling?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">memory</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    Object pooling reuses objects to avoid allocation.
    Benefits:
    - Reduce GC pressure
    - Faster allocation
    - Predictable performance
    Drawbacks:
    - Complexity (reset state)
    - Memory still allocated
    - Only helps if allocation bottleneck
    Good use cases:
    - High-throughput servers
    - Real-time games
    - Allocation proven bottleneck
    Modern approach:
    - Kotlin object pools
    - Coroutine object reuse


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/allocation-optimization/#object-pooling">🚀 See Full Deep Dive</a>


---

<div id="perfetto-tracing"></div>

## What is Perfetto and how do you use it?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">profiling</span>
  <span class="question-badge question-badge--tag">tracing</span>
  <span class="question-badge question-badge--tag">tools</span>
</div>

??? question "View Answer"

    Perfetto is a system profiler for end-to-end analysis.
    Capabilities:
    - CPU usage per thread
    - GPU rendering analysis
    - Memory allocation timeline
    - Disk I/O traces
    - Network events
    - Power/battery drain
    How to use:
    1. Enable tracing
    2. Reproduce issue (30-60s)
    3. Stop tracing
    4. Load UI trace at ui.perfetto.dev
    What it shows:
    - Frame rendering
    - Thread activity
    - Kernel events
    - Power state changes


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/profiling-tools/#perfetto-tracing">🚀 See Full Deep Dive</a>


---

<div id="frame-rate-stability"></div>

## How do you ensure stable frame rates?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">rendering</span>
  <span class="question-badge question-badge--tag">frames</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Stable frame rate = consistent 60 FPS.
    Challenges:
    - Uneven workload distribution
    - GC pauses
    - Background tasks
    Solutions:
    - Frame budget: < 16.6ms per frame
    - Profile each frame
    - Use async tasks
    - Spread work across frames
    - Predict heavy frames
    Monitoring:
    - Perfetto frame timeline
    - Android Profiler FPS
    - Custom frame listeners
    Advanced:
    - Variable refresh rate
    - Frame choreographer


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/frame-stability/#frame-rate-stability">🚀 See Full Deep Dive</a>


---

<div id="cold-start-optimization"></div>

## What causes slow cold starts?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">startup</span>
  <span class="question-badge question-badge--tag">cold-start</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Cold start = app launch from dead process.
    Timeline:
    1. Zygote fork + JIT warmup
    2. dex verification
    3. Application.onCreate()
    4. Activity + layout inflation
    5. First frame render
    Common slow points:
    - Heavy init in Application
    - Database/SharedPreferences
    - Synchronous I/O
    - Complex theme init
    Optimizations:
    - Defer init to lazy
    - Use App Startup library
    - Avoid blocking foreground
    - Reduce Activity layout
    - Use splash screen


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/startup-optimization/#cold-start-optimization">🚀 See Full Deep Dive</a>


---

<div id="warm-cache"></div>

## How do you keep a warm cache?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">caching</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    Warm cache = pre-loaded data for instant access.
    Strategy:
    - Prefetch likely data
    - Load in background after startup
    - Keep in memory
    - Update periodically
    Examples:
    - User profile: load at startup
    - Common list: preload next page
    - Images: cache before displaying
    Implementation:
    - Use Flow.replay()
    - Background job for refresh
    - Memory bounds (evict on pressure)
    Tradeoff:
    - Pro: instant display
    - Con: memory overhead, staleness


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/caching-strategies/#warm-cache">🚀 See Full Deep Dive</a>


---

<div id="composition-performance"></div>

## How does Compose performance differ from Views?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">compose</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">ui</span>
</div>

??? question "View Answer"

    Compose vs Views performance is nuanced.
    Compose advantages:
    - Efficient recomposition (skips unchanged)
    - Less allocation overhead
    - Better compiler optimizations
    View advantages:
    - Lower overhead for simple UI
    - Hardware acceleration mature
    Recomposition cost:
    - Recomposition is fast (~microseconds)
    - Can add up in complex trees
    - Use Stability annotations
    Rendering is same:
    - Both use Android graphics
    - Same frame time budget
    Optimization:
    - Use remember() correctly
    - Avoid recomposition
    - Use @Stable
    - Profile recomposition


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/compose-performance/#composition-performance">🚀 See Full Deep Dive</a>


---

<div id="shader-compilation"></div>

## What is shader compilation?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">graphics</span>
  <span class="question-badge question-badge--tag">shaders</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Shader compilation happens at runtime (GPU).
    Impact:
    - First frame with new shader: slow
    - Subsequent: cached (fast)
    Symptom:
    - Jank on first appearance of UI effect
    Solutions:
    - Pre-compile shaders
    - Warm up GPU at startup
    - Use simpler shaders
    - Avoid new combinations
    Common causes:
    - Text rendering (fonts/sizes)
    - Complex effects (blur, shadow)
    - Gradient combinations


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/graphics-optimization/#shader-compilation">🚀 See Full Deep Dive</a>


---

<div id="memory-pressure"></div>

## How do you handle memory pressure?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">memory</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    Memory pressure = system running low on RAM.
    Symptoms:
    - App slowdowns (constant GC)
    - ANRs
    - Out of Memory crashes
    Handling:
    - Implement onLowMemory()
    - Clear caches aggressively
    - Reduce image quality
    - Free non-critical resources
    Example:
    ```kotlin
    override fun onLowMemory() {
      super.onLowMemory()
      imageCache.clear()
      dataCache.clear()
    }
    ```
    Prevention:
    - Don't allocate huge objects
    - Implement bounded caches
    - Monitor memory in tests


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/memory-management/#memory-pressure">🚀 See Full Deep Dive</a>


---

<div id="graphics-memory"></div>

## How much memory do graphics consume?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">graphics</span>
  <span class="question-badge question-badge--tag">memory</span>
  <span class="question-badge question-badge--tag">gpu</span>
</div>

??? question "View Answer"

    Graphics memory = GPU + framebuffer allocations.
    Allocations:
    - Framebuffer: width × height × 4
    - Texture: image data
    - GPU cache: driver overhead
    Rough numbers:
    - 1080p framebuffer: ~8.3 MB
    - Texture 1024x1024: ~4 MB
    - Multiple framebuffers: multiples
    Optimization:
    - Reduce texture size
    - Use TextureView sparingly
    - Reduce layer complexity
    - Monitor Profiler Graphics


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/memory-management/#graphics-memory">🚀 See Full Deep Dive</a>


---

<div id="power-consumption-profiling"></div>

## How do you profile power consumption?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">battery</span>
  <span class="question-badge question-badge--tag">profiling</span>
  <span class="question-badge question-badge--tag">power</span>
</div>

??? question "View Answer"

    Power profiling measures energy usage.
    Tools:
    - Battery Historian: visual drain timeline
    - Perfetto energy events: power state
    - Monsoon: hardware measurement
    What to measure:
    - CPU active vs idle
    - Screen on time
    - Radio state (WiFi, cellular)
    - Wake locks
    Interpretation:
    - Expected baseline
    - Spikes = power-hungry ops
    - Wakelocks = preventing sleep
    Optimization targets:
    - Reduce CPU work
    - Batch I/O
    - Use Doze scheduling


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/battery-profiling/#power-consumption-profiling">🚀 See Full Deep Dive</a>


---

<div id="systrace-analysis"></div>

## How do you use systrace?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">profiling</span>
  <span class="question-badge question-badge--tag">systrace</span>
  <span class="question-badge question-badge--tag">tracing</span>
</div>

??? question "View Answer"

    Systrace captures kernel + app events.
    Shows:
    - CPU frequency scaling
    - Thread scheduling
    - Disk I/O
    - Frame rendering
    - App event markers
    Interpreting:
    - Green = running
    - Yellow = waiting
    - Red = not scheduled
    vsync alignment:
    - Marks 16.6ms frame boundaries
    - if work extends past = jank


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/profiling-tools/#systrace-analysis">🚀 See Full Deep Dive</a>


---

<div id="custom-performance-monitoring"></div>

## How do implement custom monitoring?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">monitoring</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">custom</span>
</div>

??? question "View Answer"

    Custom monitoring tracks app-specific metrics.
    Implementation:
    ```kotlin
    object PerfMonitor {
      fun trackMethodTime(name: String, block: () -> Unit) {
        val start = System.nanoTime()
        block()
        val duration = (System.nanoTime() - start) / 1_000_000f
        report("$name: ${duration}ms")
      }
    }
    ```
    What to track:
    - API response times
    - Database query latency
    - Custom UI operations
    - Cache hit rates
    Reporting:
    - Firebase Performance
    - Crashlytics
    - Custom backend
    Best practices:
    - Sampling (not every call)
    - Async reporting
    - Aggregation


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/monitoring-implementation/#custom-performance-monitoring">🚀 See Full Deep Dive</a>


---

<div id="performance-testing"></div>

## How do you write performance tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">benchmarking</span>
</div>

??? question "View Answer"

    Performance tests measure speed/memory.
    Tools:
    - Jetpack Benchmark library
    - Macrobenchmark (full app)
    - Microbenchmark (code snippets)
    Example:
    ```kotlin
    @Test
    fun jsonParsingBenchmark() {
      val result = BenchmarkRule().measureRepeated {
        gson.fromJson(jsonString, User::class.java)
      }
      assert(result.median.nanos < 1_000_000)
    }
    ```
    Best practices:
    - Run on real device
    - Multiple iterations
    - Report distribution
    - Test realistic data


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/performance-testing/#performance-testing">🚀 See Full Deep Dive</a>


---

<div id="responsiveness-perception"></div>

## Perceived responsiveness vs actual performance?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">ux</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">perception</span>
</div>

??? question "View Answer"

    Perceived responsiveness ≠ actual performance.
    Factors:
    - Immediate feedback
    - Animation smoothness
    - Predictability
    - Touch feedback
    Techniques:
    - Show loading indicator immediately
    - Skeletons (UI placeholder)
    - Instant first frame
    - Smooth animations
    Example:
    - Actual: 2-second network request
    - Perceived: Fast (progress shown immediately)
    Lesson:
    - User perception matters more
    - UX design can fake responsiveness


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/ux-perception/#responsiveness-perception">🚀 See Full Deep Dive</a>


---

<div id="benchmark-tools"></div>

## Differences between profiling tools?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">profiling</span>
  <span class="question-badge question-badge--tag">tools</span>
  <span class="question-badge question-badge--tag">comparison</span>
</div>

??? question "View Answer"

    Android profiling tools serve different purposes.
    Tools:
    - Android Profiler: app, real-time
    - Perfetto: system, high detail
    - Systrace: kernel, very detailed
    - LeakCanary: memory leaks
    - Battery Historian: battery drain
    When to use:
    - Quick checks: Android Profiler
    - Deep dive: Perfetto/Systrace
    - Memory leaks: LeakCanary
    - Battery: Battery Historian


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/profiling-tools/#benchmark-tools">🚀 See Full Deep Dive</a>


---

<div id="performance-budgets"></div>

## What is a performance budget?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">budgets</span>
  <span class="question-badge question-badge--tag">strategy</span>
</div>

??? question "View Answer"

    Performance budget = explicit metric limit.
    Examples:
    - Cold start <= 5 seconds
    - Frame rate >= 60 FPS
    - Memory <= 100 MB
    - Network <= 2 MB per session
    Benefits:
    - Prevents regression
    - Guides priorities
    - Aligns team goals
    Enforcement:
    - Continuous benchmarking
    - CI checks (fail if exceeded)
    - Code review criteria
    Setting:
    - Baseline current performance
    - Set realistic goals
    - Account for device variability


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/performance-strategy/#performance-budgets">🚀 See Full Deep Dive</a>


---

<div id="gpu-rendering-cost"></div>

## What is the cost of GPU rendering?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">gpu</span>
  <span class="question-badge question-badge--tag">rendering</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    GPU rendering = off-loading work from CPU.
    Tradeoff:
    - Pro: Frees CPU for logic
    - Con: Setup/sync overhead
    - Con: Not always faster
    When GPU helps:
    - Complex graphics (transforms)
    - Many objects (batching)
    - Heavy shading
    When CPU is better:
    - Simple UI
    - Rare updates
    - Small viewport
    Optimization:
    - Batch draw calls
    - Use GPU for heavy work only
    - Reduce texture uploads


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/gpu-optimization/#gpu-rendering-cost">🚀 See Full Deep Dive</a>


---

<div id="kernel-linux-performance"></div>

## How does Linux kernel impact performance?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kernel</span>
  <span class="question-badge question-badge--tag">linux</span>
  <span class="question-badge question-badge--tag">system</span>
</div>

??? question "View Answer"

    Kernel scheduling impacts frame timing.
    Key subsystems:
    - Scheduler: which thread runs
    - MM: memory management
    - I/O scheduler: disk requests
    - Thermal: CPU throttling
    Performance factors:
    - Load average: threads waiting
    - Context switches: contention
    - Page faults: disk access
    Android-specific:
    - cpufreq: CPU scaling
    - Zygote: shared memory
    - ASHMEM: low-memory killer
    Visible from userspace:
    - Perfetto kernel events
    - Systrace scheduling
    - Load: `adb shell cat /proc/loadavg`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/system-internals/#kernel-linux-performance">🚀 See Full Deep Dive</a>


---

<div id="ahead-of-time-compilation"></div>

## What is AoT compilation?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">compilation</span>
  <span class="question-badge question-badge--tag">aot</span>
  <span class="question-badge question-badge--tag">runtime</span>
</div>

??? question "View Answer"

    AoT = compile before running.
    Android evolution:
    - Dalvik: JIT (slow startup)
    - ART: JIT + profile-guided opt
    - Modern: ReadyToRun (pre-compiled)
    Benefits of AoT:
    - Instant execution
    - Predictable performance
    - Lower battery
    Tradeoffs:
    - Larger app size
    - Less optimized (no profile)
    In practice:
    - System apps: mostly AoT
    - Third-party: mix
    - User interaction: JIT if slow


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/performance/compilation-optimization/#ahead-of-time-compilation">🚀 See Full Deep Dive</a>

