# Fundamentals

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

<div id="activity-lifecycle-overview"></div>

# What is the Activity Lifecycle?

**Difficulty:** `beginner` • **Tags:**
`android`
`lifecycle`
`fundamentals`

??? question "What is the Activity Lifecycle?"

    The Activity Lifecycle is the sequence of states an Android Activity
    transitions through from creation to destruction.

    Android manages lifecycle callbacks automatically to:
    - optimize memory usage
    - restore UI state
    - handle multitasking
    - manage interruptions

    Core lifecycle methods:
    - onCreate()
    - onStart()
    - onResume()
    - onPause()
    - onStop()
    - onDestroy()


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/activity-lifecycle/#activity-lifecycle-overview)


---

<div id="onstart-vs-onresume"></div>

# What's the difference between onStart() and onResume()?

**Difficulty:** `beginner` • **Tags:**
`android`
`lifecycle`
`callbacks`

??? question "What's the difference between onStart() and onResume()?"

    onStart(): Called when Activity becomes visible to user.
    - Window not yet in focus
    - Activity cannot receive user input
    - Use for resource allocation needed for UI visibility

    onResume(): Called when Activity gains focus and is ready for interaction.
    - Window is in focus
    - Can receive user input
    - Use for animations, camera, location updates

    Simple rule: onStart = visible, onResume = interactive.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/activity-lifecycle/#onstart-vs-onresume)


---

<div id="onsaved-instance-state"></div>

# What is savedInstanceState and when is it called?

**Difficulty:** `intermediate` • **Tags:**
`android`
`lifecycle`
`state-preservation`

??? question "What is savedInstanceState and when is it called?"

    savedInstanceState is a Bundle used to preserve Activity state during
    predictable destruction (rotation, low memory).

    Called in order:
    1. onPause()
    2. onSaveInstanceState()
    3. onStop()

    Common use cases:
    - Save fragment state
    - Save scroll position
    - Save form data
    - Save UI state

    Note: NOT called during activity finish() or user back press.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/activity-lifecycle/#onsaved-instance-state)


---

<div id="onconfig-change"></div>

# What happens during configuration changes (rotation)?

**Difficulty:** `intermediate` • **Tags:**
`android`
`lifecycle`
`configuration`

??? question "What happens during configuration changes (rotation)?"

    When device is rotated or configuration changes:
    1. onPause() → onSaveInstanceState() → onStop() → onDestroy()
    2. onCreate() → onStart() → onResume()

    The Activity is DESTROYED and RECREATED.

    To preserve data:
    - Store in savedInstanceState Bundle
    - Use ViewModel (survives config changes)
    - Use retained fragments
    - Add android:configChanges to manifest

    Best practice: Use ViewModel for non-UI state.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/activity-lifecycle/#onconfig-change)


---

<div id="process-death-handling"></div>

# How does Android handle process death?

**Difficulty:** `intermediate` • **Tags:**
`android`
`lifecycle`
`process-management`

??? question "How does Android handle process death?"

    Process death occurs when Android kills app to free memory
    (no warning, no lifecycle callbacks).

    Recovery steps when user returns:
    1. OS restarts app process
    2. Activity onCreate() called with savedInstanceState
    3. App can restore state from Bundle

    Without state saving: Data loss, UI reset.

    Solutions:
    - Implement onSaveInstanceState()
    - Use ViewModel + Room
    - Persist critical data to disk/database
    - Use Hilt for dependency injection


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/activity-lifecycle/#process-death-handling)


---

<div id="lifecycle-callbacks-order"></div>

# What is the exact order of lifecycle callbacks?

**Difficulty:** `beginner` • **Tags:**
`android`
`lifecycle`
`callbacks`

??? question "What is the exact order of lifecycle callbacks?"

    NORMAL SEQUENCE:
    onCreate() → onStart() → onResume() → (user interaction) →
    onPause() → onStop() → onDestroy()

    VISIBLE BUT NOT INTERACTIVE:
    onStart() (no onResume yet - dialog shown)

    ANOTHER APP IN FOREGROUND:
    onPause() → onStop() (but not onDestroy)

    BACK TO APP:
    onStart() → onResume()

    DEVICE ROTATION:
    onPause() → onSaveInstanceState() → onStop() →
    onDestroy() → onCreate() → onStart() → onResume()


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/activity-lifecycle/#lifecycle-callbacks-order)


---

<div id="intent-explicit-implicit"></div>

# What's the difference between explicit and implicit intents?

**Difficulty:** `beginner` • **Tags:**
`android`
`intents`
`ipc`

??? question "What's the difference between explicit and implicit intents?"

    EXPLICIT INTENT:
    - Specifies exact component (Activity/Service)
    - Requires package name and class name
    - Use for internal app communication
    - Guaranteed to reach target

    IMPLICIT INTENT:
    - No target component specified
    - System matches intent to components via intent filters
    - Used for cross-app communication
    - May show chooser if multiple matches

    Example explicit:
    Intent(this, MainActivity::class.java)

    Example implicit:
    Intent(Intent.ACTION_VIEW, Uri.parse("https://..."))


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/intents/#intent-explicit-implicit)


---

<div id="intent-filters"></div>

# How do intent filters work?

**Difficulty:** `intermediate` • **Tags:**
`android`
`intents`
`manifest`

??? question "How do intent filters work?"

    Intent filters declare which implicit intents a component can handle.

    Defined in AndroidManifest.xml inside activity/service/broadcast receiver.

    Components:
    - action: What operation the component can perform
    - category: Additional flags about component
    - data: URI patterns, MIME types component accepts

    Matching process:
    1. System receives implicit intent
    2. Matches against all declared intent filters
    3. Returns list of matching components
    4. Shows chooser if multiple matches

    Example:
    - ACTION_VIEW + http:// MIME → Browser
    - ACTION_VIEW + image/* MIME → Gallery


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/intents/#intent-filters)


---

<div id="intent-resolution"></div>

# How does intent resolution work?

**Difficulty:** `intermediate` • **Tags:**
`android`
`intents`
`ipc`

??? question "How does intent resolution work?"

    Intent resolution is Android's process of finding the target
    component for an implicit intent.

    Steps:
    1. Find all installed apps with matching intent filters
    2. Filter by action (must match exactly)
    3. Filter by category (must have all requested)
    4. Filter by data (URI, MIME type must match)

    If multiple matches:
    - Shows chooser dialog
    - User selects preferred app
    - System can remember preference

    If no matches:
    - ActivityNotFoundException thrown

    Optimization: Use explicit intents for internal communication.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/intents/#intent-resolution)


---

<div id="intent-flags"></div>

# What are common intent flags and their purposes?

**Difficulty:** `intermediate` • **Tags:**
`android`
`intents`
`backstack`

??? question "What are common intent flags and their purposes?"

    FLAG_ACTIVITY_NEW_TASK:
    - Starts activity in new task
    - Used with contexts without activity (Services)

    FLAG_ACTIVITY_SINGLE_TOP:
    - If activity at top of stack, calls onNewIntent() instead of onCreate()
    - Prevents duplicate stack entries

    FLAG_ACTIVITY_CLEAR_TOP:
    - Clears all activities above target in stack
    - Target becomes top (or recreated if not running)

    FLAG_ACTIVITY_NO_HISTORY:
    - Activity won't be kept in history
    - Never appears in back button

    FLAG_ACTIVITY_CLEAR_TASK:
    - Clears entire task when new activity starts


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/intents/#intent-flags)


---

<div id="pending-intent"></div>

# What is a PendingIntent and when should you use it?

**Difficulty:** `intermediate` • **Tags:**
`android`
`intents`
`notifications`

??? question "What is a PendingIntent and when should you use it?"

    PendingIntent wraps an intent to be executed later by another app.

    Key property: Grants permission to foreign app to execute intent
    with YOUR app's identity and permissions.

    Common uses:
    - Notification tap actions
    - Alarm Manager
    - Widget buttons
    - Broadcast receivers

    Types:
    - PendingIntent.getActivity()
    - PendingIntent.getService()
    - PendingIntent.getBroadcast()

    Important: Use FLAG_IMMUTABLE (Android 12+) for security.
    Always provide proper flags when creating.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/intents/#pending-intent)


---

<div id="fragment-lifecycle"></div>

# What is the Fragment lifecycle?

**Difficulty:** `beginner` • **Tags:**
`android`
`fragments`
`lifecycle`

??? question "What is the Fragment lifecycle?"

    Fragment lifecycle is similar to Activity but with additional callbacks.

    Key lifecycle methods:
    - onCreate(): Fragment created
    - onCreateView(): Create fragment UI (return layout)
    - onViewCreated(): UI created, set up views
    - onStart(): Fragment visible
    - onResume(): Fragment interactive
    - onPause(): Fragment loses focus
    - onStop(): Fragment not visible
    - onDestroyView(): UI destroyed
    - onDestroy(): Fragment destroyed

    Key difference from Activity:
    - Fragments can be added/removed without destroying
    - UI lifecycle separate (onCreateView, onDestroyView)
    - Dependent on host Activity


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/fragments/#fragment-lifecycle)


---

<div id="fragment-vs-activity"></div>

# What are the differences between Fragments and Activities?

**Difficulty:** `intermediate` • **Tags:**
`android`
`fragments`
`architecture`

??? question "What are the differences between Fragments and Activities?"

    ACTIVITY:
    - Screen-level UI component
    - Entry point in manifest
    - Can exist standalone
    - Own window/UI context
    - Heavy component

    FRAGMENT:
    - Reusable UI component
    - Must be hosted in Activity
    - Can be easily replaced/swapped
    - Shares Activity's window
    - Lightweight, composable

    Use fragments for:
    - Modular UI components
    - Tab navigation
    - Master-detail layouts
    - Reusable screens

    Use activities for:
    - Screen entry points
    - Standalone screens
    - Navigation between major app sections


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/fragments/#fragment-vs-activity)


---

<div id="fragment-communication"></div>

# How do fragments communicate with each other?

**Difficulty:** `intermediate` • **Tags:**
`android`
`fragments`
`communication`

??? question "How do fragments communicate with each other?"

    APPROACH 1: Shared ViewModel (BEST PRACTICE)
    - Both fragments access same ViewModel
    - ViewModel lives in Activity scope
    - Use LiveData for reactive updates

    APPROACH 2: Interface Callback
    - Fragment implements listener interface
    - Activity receives callback
    - Activity communicates with other fragment
    - More verbose, legacy approach

    APPROACH 3: Shared Preferences / Database
    - Persist data to storage
    - Both fragments read/observe
    - Good for persistent data

    APPROACH 4: Bundle Arguments
    - Pass data between fragments
    - Only during fragment creation
    - Not for ongoing communication

    Modern approach: Use ViewModel + LiveData.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/fragments/#fragment-communication)


---

<div id="fragment-back-stack"></div>

# How does fragment back stack work?

**Difficulty:** `intermediate` • **Tags:**
`android`
`fragments`
`backstack`

??? question "How does fragment back stack work?"

    Fragment back stack is managed by FragmentManager.

    When you call:
    fragmentManager.beginTransaction()
      .replace(R.id.container, newFragment)
      .addToBackStack(null)
      .commit()

    Steps:
    1. Current fragment state saved
    2. New fragment created and added
    3. Transaction added to back stack
    4. User presses back: transaction reversed

    Key methods:
    - addToBackStack(): Add to back stack
    - popBackStack(): Remove from back stack
    - addToBackStack(tag): Named back stack entry

    Back navigation:
    - Pops last transaction
    - Replaces new fragment with old one
    - Restores previous fragment state

    Each Activity has own FragmentManager back stack.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/fragments/#fragment-back-stack)


---

<div id="fragment-arguments"></div>

# What's the best way to pass data to a Fragment?

**Difficulty:** `beginner` • **Tags:**
`android`
`fragments`
`data-passing`

??? question "What's the best way to pass data to a Fragment?"

    BEST PRACTICE: Use Bundle with constants

    Recommended pattern:
    companion object {
      private const val ARG_USER_ID = "user_id"
      
      fun newInstance(userId: Int) = MyFragment().apply {
        arguments = Bundle().apply {
          putInt(ARG_USER_ID, userId)
        }
      }
    }

    In onCreate():
    val userId = arguments?.getInt(ARG_USER_ID) ?: 0

    Why this approach:
    - Survives configuration changes
    - Works across process death
    - Type-safe with constants
    - Replicates Android best practices

    DON'T:
    - Pass large or non-Parcelable objects as arguments
    - Use constructors with parameters
    - Access fragments without factory method


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/fragments/#fragment-arguments)


---

<div id="context-what-is"></div>

# What is Context and what are its types?

**Difficulty:** `beginner` • **Tags:**
`android`
`context`
`fundamentals`

??? question "What is Context and what are its types?"

    Context is an abstract class that provides access to app resources
    and system services.

    Think of it as: "Reference to the current application state."

    Primary types:

    APPLICATION CONTEXT:
    - Lives entire app lifetime
    - Accessible via getApplicationContext()
    - Use for singletons, global listeners

    ACTIVITY CONTEXT:
    - Tied to Activity lifecycle
    - Available via 'this' or getContext()
    - Use for UI operations, dialogs
    - Destroyed when Activity destroyed

    Common uses:
    - Start activities/services
    - Get system services (LocationManager, etc)
    - Access resources (strings, drawables)
    - Create databases, SharedPreferences
    - Show toasts, dialogs


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/context/#context-what-is)


---

<div id="context-memory-leaks"></div>

# How can Context cause memory leaks?

**Difficulty:** `intermediate` • **Tags:**
`android`
`context`
`memory`

??? question "How can Context cause memory leaks?"

    Context memory leaks occur when Activity Context is referenced
    by long-lived objects.

    PROBLEMATIC PATTERNS:

    1. Activity context in singletons:
    object MySingleton {
      var context: Context? = null // WRONG!
    }

    2. Inner class references Activity:
    class MyInnerClass { // Holds Activity ref
      fun doWork() {}
    }

    3. Static references to Activity:
    companion object {
      var activity: Activity? = null // WRONG!
    }

    SOLUTIONS:
    - Use application context for singletons
    - Use static inner class + WeakReference
    - Use dependency injection
    - Never store Activity in long-lived objects

    Memory leak chain: Activity → thread → singleton → leak


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/context/#context-memory-leaks)


---

<div id="application-context-vs-activity-context"></div>

# When should you use Application Context vs Activity Context?

**Difficulty:** `intermediate` • **Tags:**
`android`
`context`
`best-practices`

??? question "When should you use Application Context vs Activity Context?"

    USE APPLICATION CONTEXT:
    - Get SharedPreferences
    - Create global singletons
    - Get system services used globally
    - Database creation
    - Any operation not tied to UI

    DON'T use for:
    - UI operations (dialogs crash if Activity destroyed)
    - Showing toasts in some cases
    - Creating LayoutInflater

    USE ACTIVITY CONTEXT:
    - Show dialogs
    - Create LayoutInflater
    - Start activities/services
    - UI-dependent operations
    - Access Activity-specific services

    DON'T use for:
    - Long-lived objects (memory leak risk)
    - Singletons
    - Static references

    Simple rule: Use app context if possible, activity context only
    when UI operation is tied to current Activity.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/context/#application-context-vs-activity-context)


---

<div id="context-lifecycle-awareness"></div>

# Why is it important to match Context lifetime with usage?

**Difficulty:** `intermediate` • **Tags:**
`android`
`context`
`lifecycle`

??? question "Why is it important to match Context lifetime with usage?"

    Mismatching Context lifetime with usage causes:
    - Memory leaks (Activity never garbage collected)
    - Crashes (UI operation on destroyed context)
    - Data loss (operations interrupted)

    EXAMPLE - Wrong:
    class Manager(val context: Activity) { // Holds Activity ref
      fun work() { /* does work */ }
    }
    // Activity destroyed but Manager still referenced → leak

    CORRECT - Right:
    class Manager(val context: Context) { // Use generic Context
      fun work() { /* does work */ }
    }
    val manager = Manager(applicationContext) // App context

    Key principle:
    Lifetime of Context >= Lifetime of code referencing it

    If code runs longer than Activity: use app context.
    If code tied to Activity: safe to use Activity context.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/context/#context-lifecycle-awareness)


---

<div id="memory-leak-what-is"></div>

# What is a memory leak in Android?

**Difficulty:** `beginner` • **Tags:**
`android`
`memory`
`performance`

??? question "What is a memory leak in Android?"

    A memory leak occurs when an object is no longer needed but remains
    referenced, preventing garbage collection.

    Memory leak chain:
    1. Object created
    2. No longer needed (Activity destroyed, etc)
    3. But still referenced by another object
    4. Garbage collector can't reclaim memory
    5. Memory usage grows

    Consequences:
    - Out of Memory (OOM) exceptions
    - App crashes
    - Degraded performance
    - Battery drain
    - Reduced available memory for other apps

    Common Android leak sources:
    - Static references to Activities
    - Long-lived objects holding Activity context
    - Unregistered listeners/callbacks
    - Handler messages with Activity context
    - Inner classes retaining Activity


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/memory-leaks/#memory-leak-what-is)


---

<div id="memory-detection"></div>

# How do you detect memory leaks?

**Difficulty:** `intermediate` • **Tags:**
`android`
`memory`
`debugging`

??? question "How do you detect memory leaks?"

    TOOLS:

    1. LeakCanary library:
    - Automatically detects leaks
    - Shows leak chain
    - Most practical tool

    2. Android Studio Memory Profiler:
    - Record heap allocations
    - Take heap dumps
    - Inspect object references

    3. Logcat:
    - Watch for OOM errors
    - Monitor memory growth

    PROCESS:
    1. Run app with LeakCanary/Profiler
    2. Perform action multiple times (navigate, rotate, etc)
    3. Look for memory growth pattern
    4. Take heap dump
    5. Inspect object references
    6. Trace back to root reference

    Key: Always check that objects can be garbage collected
    after they're no longer needed.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/memory-leaks/#memory-detection)


---

<div id="common-leak-patterns"></div>

# What are common memory leak patterns in Android?

**Difficulty:** `intermediate` • **Tags:**
`android`
`memory`
`patterns`

??? question "What are common memory leak patterns in Android?"

    PATTERN 1: Static Activity Reference
    companion object {
      var activity: Activity? = null // WRONG!
    }
    Fix: Don't store Activity references as static.

    PATTERN 2: Inner Class Holding Activity
    inner class MyThread : Thread() { // Holds Activity ref
      override fun run() { doWork() }
    }
    Fix: Use static inner class + WeakReference

    PATTERN 3: Unregistered Listeners
    registerReceiver(myReceiver, filter) // Never unregistered
    Fix: Always unregister in onPause/onDestroy

    PATTERN 4: Handler Messages
    handler.postDelayed({ toast.show() }, 60000)
    // If activity destroyed before delay ends: leak
    Fix: Remove messages in onDestroy

    PATTERN 5: Long-Lived Objects Holding Context
    singleton.context = this // Long-lived singleton
    Fix: Use app context or WeakReference


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/memory-leaks/#common-leak-patterns)


---

<div id="memory-leak-fixes"></div>

# What are best practices to prevent memory leaks?

**Difficulty:** `intermediate` • **Tags:**
`android`
`memory`
`best-practices`

??? question "What are best practices to prevent memory leaks?"

    1. Prefer application context over Activity context
    - Singletons, databases, shared preferences
    - Any global operation

    2. Use WeakReference for Activity references
    - Long-lived objects needing Activity
    - Handler.Callback with WeakReference<Activity>

    3. Always unregister listeners
    - Broadcast receivers: unregister in onDestroy
    - Sensors: unregister in onStop
    - Event buses: unsubscribe in onDestroy

    4. Remove handlers/callbacks before destroying
    - handler.removeCallbacks()
    - handler.removeMessages()
    - In onDestroy/onPause

    5. Use ViewBinding over findViewById
    - Automatic null-out in onDestroyView
    - Prevents view references

    6. Close resources properly
    - Close streams, databases, cursors
    - Try-with-resources for auto-close

    7. Use LeakCanary in development
    - Catches leaks automatically
    - Part of development workflow


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/memory-leaks/#memory-leak-fixes)


---

<div id="anr-what-is"></div>

# What is an ANR (Application Not Responding)?

**Difficulty:** `beginner` • **Tags:**
`android`
`performance`
`anr`

??? question "What is an ANR (Application Not Responding)?"

    ANR (Application Not Responding) occurs when main thread blocks
    for too long, preventing UI updates or input handling.

    Timeout thresholds:
    - Foreground input dispatch: ~5 seconds
    - Broadcast receiver: 10 seconds
    - Service timeouts vary by API level and state

    When ANR triggered:
    1. OS detects main thread unresponsive
    2. OS kills app
    3. System shows "waiting for..." dialog
    4. User can close app or wait

    Result:
    - App crash
    - Bad user experience
    - Potential uninstall
    - Play Store warnings

    Common causes:
    - Blocking main thread (I/O, network, computation)
    - Heavy UI operations
    - Infinite loops
    - Deadlock situations
    - Unoptimized database queries


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/anr-and-performance/#anr-what-is)


---

<div id="preventing-anr"></div>

# How do you prevent ANRs?

**Difficulty:** `intermediate` • **Tags:**
`android`
`performance`
`anr`

??? question "How do you prevent ANRs?"

    RULE 1: Keep main thread operations quick
    - Maximum 100-200ms for user-facing operations
    - Don't do I/O, network, or heavy computation on main thread

    SOLUTIONS:

    1. Use threads for heavy work:
    Thread { heavyWork() }.start()

    2. Use coroutines (modern approach):
    viewModelScope.launch(Dispatchers.Default) {
      heavyWork() // Off main thread
    }

    3. AsyncTask (legacy):
    AsyncTask.execute { heavyWork() }

    4. Optimize database queries:
    - Index frequently queried columns
    - Avoid complex queries on main thread
    - Use query optimization

    5. Lazy load data:
    - Load progressively
    - Show skeleton/placeholder
    - Fetch full data in background

    6. Profile with Profiler:
    - Find slow operations
    - Optimize hotspots


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/anr-and-performance/#preventing-anr)


---

<div id="main-thread-vs-background"></div>

# Why shouldn't you do network/I/O on main thread?

**Difficulty:** `intermediate` • **Tags:**
`android`
`threading`
`performance`

??? question "Why shouldn't you do network/I/O on main thread?"

    Main thread responsibilities:
    - Handle user input (taps, scrolls)
    - Update UI views
    - Render frames (16.67ms per frame)
    - Handle system messages

    Network/I/O characteristics:
    - Unpredictable duration (100ms to seconds+)
    - Can block indefinitely
    - May fail and retry

    If you block main thread with I/O:
    - Input not processed (janky/unresponsive)
    - Frames skipped (dropped frames, jank)
    - ANR timeout triggered
    - UI freezes visibly to user

    Solution: Off-load to background thread
    - Main thread: responsive UI
    - Background thread: I/O, network, computation
    - Post results back to main thread for UI updates

    Modern approach: Coroutines
    val data = withContext(Dispatchers.IO) { fetchData() }
    // Automatically switches context


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/anr-and-performance/#main-thread-vs-background)


---

<div id="jank-dropped-frames"></div>

# What's jank and how do you measure it?

**Difficulty:** `intermediate` • **Tags:**
`android`
`performance`
`rendering`

??? question "What's jank and how do you measure it?"

    JANK: Visible stutter in UI animations/scrolling.

    Cause: Dropping frames due to main thread blocking.

    Expected frame rate:
    - 60fps devices: frame every 16.67ms
    - 90fps devices: frame every 11.11ms
    - 120fps devices: frame every 8.33ms

    If main thread busy > frame time:
    - Frame dropped
    - Animation/scroll stutters visibly
    - User sees jank

    Measurement tools:

    1. Profile GPU Rendering (dev options):
    - Visual graph on screen
    - Shows frame times
    - Green = good, yellow/red = jank

    2. Android Studio Profiler:
    - CPU, Memory, Network profiling
    - See main thread operations

    3. FrameMetrics API:
    - Programmatically measure frame times
    - Real user monitoring

    4. Firebase Performance Monitoring:
    - Production monitoring
    - Real user metrics

    Prevention: Keep main thread responsive (<5ms per operation).


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/anr-and-performance/#jank-dropped-frames)


---

<div id="looper-what-is"></div>

# What is Looper and how does it work?

**Difficulty:** `intermediate` • **Tags:**
`android`
`threading`
`looper`

??? question "What is Looper and how does it work?"

    Looper: Thread mechanism for processing messages in a queue.

    How it works:
    1. Thread has message queue
    2. Looper continuously loops through queue
    3. Processes one message per iteration
    4. Blocks if queue empty
    5. Exits when quit() called

    Each thread has max 1 Looper.

    Main thread always has Looper:
    - Created automatically by Android system
    - Processes UI messages, events

    Background threads:
    - No Looper by default
    - Create manually if needed:
    Thread {
      Looper.prepare()
      // ... do work ...
      Looper.loop() // Start looping
    }.start()

    Why Looper matters:
    - Thread-safe message passing
    - Ordered message processing
    - Foundation for Handler/HandlerThread
    - UI updates only on main thread (main Looper)


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/looper-and-handler/#looper-what-is)


---

<div id="handler-what-is"></div>

# What is Handler and how does it relate to Looper?

**Difficulty:** `intermediate` • **Tags:**
`android`
`threading`
`handler`

??? question "What is Handler and how does it relate to Looper?"

    Handler: Interface for sending messages to a Thread's message queue.

    Relationship with Looper:
    1. Handler posts messages to queue
    2. Handler associated with Looper
    3. Looper processes messages from queue
    4. Handler executes callbacks on Looper's thread

    Creating Handler:
    Handler(Looper.getMainLooper()) // Posts to main thread
    Handler() // Posts to current thread's Looper

    Common uses:
    handler.post(Runnable) // Execute on handler's thread
    handler.postDelayed(Runnable, delay) // Delayed execution
    handler.sendMessage(Message) // Send message

    Example - Update UI after background work:
    Thread {
      val result = doHeavyWork()
      mainHandler.post {
        updateUI(result) // Runs on main thread
      }
    }.start()

    Key: Handler provides thread-safe way to run code on specific thread.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/looper-and-handler/#handler-what-is)


---

<div id="handler-thread"></div>

# What is HandlerThread and when should you use it?

**Difficulty:** `intermediate` • **Tags:**
`android`
`threading`
`handler`

??? question "What is HandlerThread and when should you use it?"

    HandlerThread: Thread with built-in Looper for handling messages.

    Benefits over plain Thread:
    - Looper automatically created and started
    - Ready to receive messages immediately
    - Clean shutdown with quit()
    - No need for manual Looper.prepare()/loop()

    Creating HandlerThread:
    val handlerThread = HandlerThread("MyThread")
    handlerThread.start()
    val handler = Handler(handlerThread.looper)

    Use cases:
    - Background image processing
    - File I/O operations
    - Database operations
    - Any repeatable background task

    Best practice: Combine with Handler for thread-safe updates.

    Handler posts work → HandlerThread queue → Looper processes

    Remember: Always call quit() when done to avoid thread leaks.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/looper-and-handler/#handler-thread)


---

<div id="handler-memory-leak"></div>

# How can Handler cause memory leaks?

**Difficulty:** `intermediate` • **Tags:**
`android`
`handler`
`memory`

??? question "How can Handler cause memory leaks?"

    Handler with delayed messages can leak Activity context.

    Problem scenario:
    handler.postDelayed(Runnable {
      // Runnable holds implicit 'this' reference (Activity)
    }, 60000)
    // If Activity destroyed before delay ends: leak

    Memory leak chain:
    1. Handler post delayed message
    2. Message queued for 60 seconds
    3. Activity destroyed (user navigates away)
    4. Message still in queue, holds Activity reference
    5. Activity cannot be garbage collected
    6. After 60 seconds, message executed (too late)

    SOLUTION 1: Use Handler with WeakReference
    class MyActivity : AppCompatActivity() {
      private val handler = Handler(Looper.getMainLooper())
      
      private inner class MyRunnable : Runnable {
        override fun run() { /* ... */ }
      }
    }

    SOLUTION 2: Remove messages in onDestroy
    override fun onDestroy() {
      handler.removeCallbacks(myRunnable)
      super.onDestroy()
    }

    MODERN: Use coroutines instead (automatic cleanup).


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/looper-and-handler/#handler-memory-leak)


---

<div id="service-what-is"></div>

# What is a Service in Android?

**Difficulty:** `beginner` • **Tags:**
`android`
`service`
`fundamentals`

??? question "What is a Service in Android?"

    Service: Component for long-running operations in background.

    Key characteristics:
    - No UI (unlike Activity)
    - Can run in background
    - Continues running even if app minimized
    - Has own lifecycle
    - Must be declared in manifest

    When to use:
    - Music playback
    - Download files
    - Upload media
    - Sync data with server
    - Long-running computations

    Service types:

    STARTED SERVICE:
    - Runs indefinitely
    - Stopped explicitly or by system
    - No connection to caller

    BOUND SERVICE:
    - Connected to caller via IPC
    - Provides interface for interaction
    - Stops when all clients unbind

    FOREGROUND SERVICE:
    - Runs with visible notification
    - Higher priority, but can still be stopped by system/user
    - Used for user-aware background work

    Important: Services run on main thread by default.
    Use threads inside service for heavy work.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/services/#service-what-is)


---

<div id="service-vs-thread"></div>

# What's the difference between Service and Thread?

**Difficulty:** `intermediate` • **Tags:**
`android`
`service`
`threading`

??? question "What's the difference between Service and Thread?"

    THREAD:
    - Tied to single process/app
    - Dies when app killed
    - Lightweight
    - No persistence

    SERVICE:
    - Can outlive Activity
    - System prioritizes keeping running
    - Has manifest declaration
    - Can be started by other apps (permission-based)
    - Less likely to be killed, but still possible

    USE CASE:
    Heavy computation + don't need UI after?
    → Thread

    Need background work to survive Activity destroy?
    → Service

    Example distinction:
    - Play music in Thread (stops when app closed)
    - Play music in Service (continues when minimized)

    KEY DIFFERENCE:
    Process priority:
    - Running service: Higher priority (less likely to be killed)
    - Background app with thread: Lower priority (killed first)

    System Management:
    - Service: Managed by system
    - Thread: Not managed by system


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/services/#service-vs-thread)


---

<div id="bound-service"></div>

# What is a bound service and how do you use it?

**Difficulty:** `intermediate` • **Tags:**
`android`
`service`
`ipc`

??? question "What is a bound service and how do you use it?"

    Bound Service: Service offering interface for IPC to clients.

    Steps to implement:

    1. Create Service with Binder:
    class MyBoundService : Service() {
      inner class LocalBinder : Binder() {
        fun getService() = this@MyBoundService
      }
    }

    2. Override onBind():
    override fun onBind(intent: Intent?): IBinder {
      return LocalBinder()
    }

    3. Bind from Activity:
    bindService(Intent(...), connection,
      Context.BIND_AUTO_CREATE)

    4. Use ServiceConnection:
    object : ServiceConnection {
      override fun onServiceConnected(...) {
        val binder = service as Binder
        val service = binder.getService()
      }
    }

    Lifecycle:
    - onBind() when first client binds
    - onUnbind() when last client unbinds
    - Service stops if no clients bound and not started

    Key: Bound service tied to client lifecycle.
    Unbind in onDestroy/onStop to prevent leaks.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/services/#bound-service)


---

<div id="intent-service"></div>

# What is IntentService and when should you use it?

**Difficulty:** `intermediate` • **Tags:**
`android`
`service`
`background-work`

??? question "What is IntentService and when should you use it?"

    IntentService (deprecated): Subclass of Service handling asynchronous requests.

    Benefits:
    - Background thread automatically created
    - Processes one intent at a time (queue)
    - Auto-stops when queue empty
    - No manual threading needed
    - Simple to use

    How it works:
    1. Create IntentService subclass
    2. Override onHandleIntent() (runs on bg thread)
    3. Send intents with startService()
    4. Threading automatically handled
    5. Auto-stops after processing

    Example:
    class DownloadService : IntentService("Download") {
      override fun onHandleIntent(intent: Intent?) {
        // Background thread, won't block UI
        val file = downloadFile() // Network call OK
      }
    }

    Problems (Android 8.0+):
    - Background execution restrictions
    - Use WorkManager instead

    MODERN APPROACH:
    Use WorkManager for background work (better lifecycle management,
    persistence, backoff policy).

    Legacy but useful for understanding architecture.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/services/#intent-service)


---

<div id="broadcast-receiver"></div>

# What is a Broadcast Receiver?

**Difficulty:** `beginner` • **Tags:**
`android`
`broadcasting`
`messaging`

??? question "What is a Broadcast Receiver?"

    Broadcast Receiver: Component for receiving system/app messages.

    Characteristics:
    - Listens for broadcast intents
    - Executes onReceive() when broadcast received
    - Can run even if app not open
    - No UI capability
    - Must be declared in manifest or registered

    System broadcasts:
    - ACTION_BATTERY_LOW
    - ACTION_CONNECTIVITY_CHANGE
    - ACTION_BOOT_COMPLETED
    - ACTION_PACKAGE_INSTALLED

    Types of receivers:

    STATIC (Manifest-declared):
    - Declared in AndroidManifest.xml
    - System can start app just to deliver broadcast

    DYNAMIC (Runtime-registered):
    - Registered in code via registerReceiver()
    - Active only while app running
    - Better for app-specific broadcasts

    Example:
    class MyReceiver : BroadcastReceiver() {
      override fun onReceive(context, intent) {
        // Process broadcast
      }
    }

    Use cases: Battery level, connectivity, SMS, time changes.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/broadcast-receivers/#broadcast-receiver)


---

<div id="broadcast-permissions"></div>

# How do you register broadcast receivers securely?

**Difficulty:** `intermediate` • **Tags:**
`android`
`broadcasting`
`security`

??? question "How do you register broadcast receivers securely?"

    DYNAMIC REGISTRATION (Recommended):

    1. Register in onCreate/onStart:
    registerReceiver(myReceiver, IntentFilter(ACTION))

    2. Unregister in onDestroy/onStop:
    unregisterReceiver(myReceiver)

    STATIC REGISTRATION (Manifest):
    <receiver android:name=".MyReceiver"
      android:permission="com.example.PERM" >
      <intent-filter>
        <action android:name="..." />
      </intent-filter>
    </receiver>

    SECURITY BEST PRACTICES:

    1. Use specific intent filters (not catch-all)
    Only catch broadcasts you need

    2. Check sender permissions:
    In onReceive(), verify sender is trusted

    3. Require permissions for safety:
    android:permission="my.permission"

    4. Limit receiving broadcasts:
    Use specific actions, not generic patterns

    5. Android 8.0+ restrictions:
    - Static receivers limited (battery optimization)
    - Use dynamic registration
    - Or use JobScheduler/WorkManager

    6. Always unregister dynamic receivers:
    Prevents memory leaks and battery drain


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/broadcast-receivers/#broadcast-permissions)


---

<div id="ordered-vs-sticky-broadcast"></div>

# What are ordered and sticky broadcasts?

**Difficulty:** `intermediate` • **Tags:**
`android`
`broadcasting`
`messaging`

??? question "What are ordered and sticky broadcasts?"

    NORMAL BROADCAST:
    - Sent to all matching receivers simultaneously
    - No guaranteed order
    - Receivers cannot affect each other

    ORDERED BROADCAST:
    - Delivered to receivers one at a time
    - In priority order
    - Each receiver can modify result or abort
    - Only next receiver gets modified data
    - Use: sendOrderedBroadcast()

    STICKY BROADCAST:
    - Deprecated and removed in Android 5.0+
    - Previously: Last broadcast value retained
    - New receivers got last value on register
    - Caused security/memory issues

    Example ordered broadcast:
    sendOrderedBroadcast(intent, null,
      resultReceiver, handler, resultCode,
      resultData, resultExtras)

    Receiver can:
    - setResultCode(newCode)
    - setResultData(newData)
    - abortBroadcast() // Stop delivery to others

    Use cases:
    - NORMAL: Multiple unrelated receivers
    - ORDERED: Chain of responsibility pattern
    - System broadcasts all normal

    Best practice: Prefer explicit app-scoped communication
    (shared ViewModel/Flow or explicit broadcasts).
    LocalBroadcastManager is deprecated.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/broadcast-receivers/#ordered-vs-sticky-broadcast)


---

<div id="permissions-model"></div>

# What is the Android permission model?

**Difficulty:** `beginner` • **Tags:**
`android`
`permissions`
`security`

??? question "What is the Android permission model?"

    ANDROID 5.0 (API 21) and below:
    - All permissions granted at install time
    - User reviews app's permission list pre-install
    - Cannot revoke individual permissions

    ANDROID 6.0+ (Runtime permissions):
    - Permissions granted at runtime
    - Dangerous permissions require explicit user request
    - User can revoke permissions anytime
    - App handles permission denials gracefully

    Permission categories:

    NORMAL PERMISSIONS (auto-granted):
    - ACCESS_NETWORK_STATE
    - INTERNET
    - Safe permissions, no user prompt
    - Declared only in manifest

    DANGEROUS PERMISSIONS (runtime):
    - CAMERA, MICROPHONE
    - READ_CONTACTS, WRITE_CALENDAR
    - ACCESS_FINE_LOCATION
    - Require explicit user request via dialog

    SIGNATURE PERMISSIONS:
    - Only apps signed with same cert

    CUSTOM PERMISSIONS:
    - App-defined permissions

    Best practice: Request permissions only when needed (ask on usage).


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/permissions/#permissions-model)


---

<div id="runtime-permissions"></div>

# How do you implement runtime permissions?

**Difficulty:** `intermediate` • **Tags:**
`android`
`permissions`
`runtime`

??? question "How do you implement runtime permissions?"

    STEPS:

    1. Declare in manifest:
    <uses-permission android:name="android.permission.CAMERA" />

    2. Check permission at runtime:
    if (ContextCompat.checkSelfPermission(this,
        Manifest.permission.CAMERA) 
        != PackageManager.PERMISSION_GRANTED) {
      // Request permission
    } else {
      // Use camera
    }

    3. Request permission:
    ActivityCompat.requestPermissions(this,
      arrayOf(Manifest.permission.CAMERA), 100)

    4. Handle response:
    override fun onRequestPermissionsResult(
        requestCode: Int, permissions: Array<out String>,
        grantResults: IntArray) {
      if (requestCode == 100) {
        if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
          useCamera()
        } else {
          showPermissionDeniedMessage()
        }
      }
    }

    MODERN APPROACH (Activity Result Contract):
    val cameraPermission = registerForActivityResult(
      ActivityResultContracts.RequestPermission()) { isGranted ->
      if (isGranted) useCamera()
      else showDeniedMessage()
    }
    cameraPermission.launch(CAMERA)

    Always handle permission denials gracefully.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/permissions/#runtime-permissions)


---

<div id="permission-groups"></div>

# What are permission groups and how do they work?

**Difficulty:** `intermediate` • **Tags:**
`android`
`permissions`
`groups`

??? question "What are permission groups and how do they work?"

    Permission Groups: Dangerous permissions organized by functional groups.

    System shows one prompt per group.

    Example groups:

    CALENDAR: READ_CALENDAR, WRITE_CALENDAR
    CAMERA: CAMERA
    CONTACTS: READ_CONTACTS, WRITE_CONTACTS, GET_ACCOUNTS
    LOCATION: ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION
    MICROPHONE: RECORD_AUDIO
    PHONE: PROCESS_OUTGOING_CALLS, READ_PHONE_STATE, etc.
    SENSORS: BODY_SENSORS
    SMS: READ_SMS, SEND_SMS, RECEIVE_SMS, etc.
    STORAGE: READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
    PHOTOS: READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO

    How it works:
    1. User grants CALENDAR group permission
    2. System may group prompts for user clarity
    3. Grant decisions are per permission and can vary by Android version

    Important: Each permission still must be declared in manifest.

    Best practice:
    - Request permissions on-demand (when first needed)
    - Request least required permissions
    - Explain why permission needed (context)
    - Handle denials gracefully (skip feature)


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/permissions/#permission-groups)


---

<div id="manifest-what-is"></div>

# What is AndroidManifest.xml and what does it contain?

**Difficulty:** `beginner` • **Tags:**
`android`
`manifest`
`fundamentals`

??? question "What is AndroidManifest.xml and what does it contain?"

    AndroidManifest.xml: Main configuration file for Android app.

    Contains:

    1. PACKAGE NAME:
    package="com.example.myapp"

    2. COMPONENTS:
    - Activities
    - Services
    - Broadcast receivers
    - Content providers

    3. PERMISSIONS:
    - Required permissions
    - Custom permissions

    4. FEATURES:
    - Hardware features (camera, GPS)
    - Software features

    5. VERSION INFO:
    - versionCode, versionName
    - targetSdkVersion, minSdkVersion

    6. APPLICATION METADATA:
    - App icon, label, theme
    - Backup agent
    - Hardware acceleration flags

    7. INTENT FILTERS:
    - Which implicit intents components handle
    - Which apps can start component

    Example:
    <manifest package="com.example.app" ...>
      <uses-permission android:name="..." />
      <application>
        <activity android:name=".MainActivity">
          <intent-filter>
            <action android:name="..." />
          </intent-filter>
        </activity>
      </application>
    </manifest>

    Note: Some settings now in build.gradle (build tools).


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/androidmanifest/#manifest-what-is)


---

<div id="manifest-intent-filters"></div>

# How do you declare intent filters in manifest?

**Difficulty:** `intermediate` • **Tags:**
`android`
`manifest`
`intents`

??? question "How do you declare intent filters in manifest?"

    Intent filters declare which implicit intents a component accepts.

    STRUCTURE:
    <activity android:name=".MainActivity">
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name=
          "android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    COMPONENTS:

    ACTION: What the component does
    <action android:name="android.intent.action.VIEW" />
    <action android:name="android.intent.action.SEND" />

    CATEGORY: Additional info about component
    <category android:name=
      "android.intent.category.DEFAULT" />
    <category
      android:name=
      "android.intent.category.LAUNCHER" />

    DATA: URI/MIME type patterns
    <data android:scheme="https"
          android:host="example.com"
          android:mimeType="text/*" />

    MATCHING RULES:
    - Implicit intent must match ALL declared filters
    - If multiple matches: chooser shown

    EXAMPLE - Web link handler:
    <intent-filter>
      <action android:name="
        android.intent.action.VIEW" />
      <category android:name="
        android.intent.category.DEFAULT" />
      <category android:name="
        android.intent.category.BROWSABLE" />
      <data android:scheme="https"
            android:host="example.com" />
    </intent-filter>


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/androidmanifest/#manifest-intent-filters)


---

<div id="binder-ipc"></div>

# What is Binder and how does IPC work in Android?

**Difficulty:** `intermediate` • **Tags:**
`android`
`ipc`
`binder`

??? question "What is Binder and how does IPC work in Android?"

    Binder: Android's Inter-Process Communication (IPC) mechanism.

    Architecture:
    - Client process passes data to kernel
    - Kernel validates and transfers to server process
    - Server Binder thread processes request
    - Response sent back through kernel

    Why Binder:
    - More efficient than traditional sockets
    - Thread pool management automatic
    - Reference counting built-in
    - Security: UID/PID tracking

    Common uses:
    - Bound services
    - System services (LocationManager, etc)
    - Inter-app communication
    - Activity manager, package manager

    AIDL (Android Interface Definition Language):
    - Define service interface
    - Compiler generates Binder stub/proxy
    - Client calls via proxy
    - Server handles in onBind()

    AIDL workflow:
    1. Define .aidl file
    2. Build system generates code
    3. Implement service
    4. Bind and call methods

    Most apps use high-level APIs (Intent, services)
    but Binder is underlying mechanism.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/binder-ipc/#binder-ipc)


---

<div id="zygote-process-creation"></div>

# What is Zygote and how does it create app processes?

**Difficulty:** `advanced` • **Tags:**
`android`
`internals`
`process`

??? question "What is Zygote and how does it create app processes?"

    Zygote: Special system process that launches all app processes.

    Problem it solves:
    - Android apps need Android runtime (VM, libraries)
    - Starting VM for each app slow
    - Zygote pre-starts VM with framework loaded

    How it works:

    1. Boot: Zygote process starts
       - Loads Android framework
       - Pre-initializes VM
       - Enters listening mode

    2. App launch requested:
       - Activity Manager requests process from Zygote
       - Zygote forks itself (fork = copy entire process)
       - Child process = new app process

    3. App process:
       - Inherits Zygote's loaded framework
       - Minimal initialization time
       - Ready to run app code

    Benefits:
    - App launch much faster
    - Less memory per app (shared framework)
    - Faster development iteration

    Process hierarchy:
    init → Zygote → ActivityManager → App processes

    Native/Java boundary:
    - Zygote is Java (runs on runtime)
    - Child processes also Java
    - System services communicate via Binder

    Multiple Zygotes:
    - Android 12+: Secondary Zygote for compatibility


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/zygote-process-creation/#zygote-process-creation)


---

<div id="art-vs-dalvik"></div>

# What is the difference between ART and Dalvik?

**Difficulty:** `advanced` • **Tags:**
`android`
`runtime`
`performance`

??? question "What is the difference between ART and Dalvik?"

    DALVIK (Android 2.2 - 4.4):
    - JIT (Just-In-Time) compilation
    - Compiles bytecode to native during app execution
    - Every run: recompiled (slower)
    - Lower app install size
    - Higher app startup time
    - Higher runtime memory usage

    ART (Android 5.0+):
    - AOT (Ahead-Of-Time) compilation
    - Compiles bytecode to native at install time
    - Always runs native code (faster)
    - Larger app install size
    - Faster app startup
    - Lower runtime memory usage
    - Predictable performance

    COMPARISON:

    Performance: ART faster (precompiled)
    Startup: ART much faster
    Battery: ART better (less CPU work)
    Storage: Dalvik smaller app size
    Install time: ART slower (compilation)

    JIT vs AOT:
    - JIT: optimize while running
    - AOT: optimize before running

    ART advantages:
    - More predictable performance
    - Better garbage collection
    - Improved debugging
    - Better battery life
    - Faster app startup

    Modern Android: Hybrid
    - Base app compiled AOT at install
    - JIT during app execution
    - Combines both benefits


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/art-vs-dalvik/#art-vs-dalvik)


---

<div id="app-startup-flow"></div>

# What happens when you launch an app?

**Difficulty:** `intermediate` • **Tags:**
`android`
`startup`
`lifecycle`

??? question "What happens when you launch an app?"

    APP STARTUP FLOW:

    1. User taps app icon
    2. Launcher sends Intent to ActivityManager
    3. ActivityManager checks if process exists
       - No: requests process from Zygote
       - Yes: use existing process
    4. Zygote fork creates new process (or uses existing)
    5. New process reads app manifest
    6. Process loads Application class
    7. Application.onCreate() called
    8. Process loads Activity
    9. Activity lifecycle starts: onCreate → onStart → onResume
    10. Activity rendered on screen

    OPTIMIZATION OPPORTUNITIES:

    1. App startup time stages:
    - Cold start: No process exists (slowest)
    - Warm start: Process exists but Activity not (medium)
    - Hot start: Activity in memory but paused (fastest)

    2. Optimize for cold start:
    - Lazy load modules
    - Don't block Application.onCreate()
    - Defer non-essential initialization
    - Use StartupManager library
    - Profiling: Use startup profiler

    3. Improve perceived performance:
    - Show splash screen
    - Load skeleton/placeholder
    - Progressive content loading

    System captures startup metrics:
    - first frame (visible)
    - fully drawn (interactive)

    Modern approach: Activity Result API, lazy
    Fragment initialization.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/app-startup-flow/#app-startup-flow)


---

<div id="recyclerview-efficiency"></div>

# Why is RecyclerView more efficient than ListView?

**Difficulty:** `intermediate` • **Tags:**
`android`
`ui`
`performance`

??? question "Why is RecyclerView more efficient than ListView?"

    LISTVIEW DRAWBACKS:
    - Creates View for each list item
    - Never destroys views when scrolled off
    - List of 100 items = 100 Views in memory
    - Heavy GC pressure
    - Janky scrolling

    RECYCLERVIEW IMPROVEMENTS:
    - Reuses View objects (recycled pools)
    - Only creates Views for visible items
    - Off-screen views returned to pool
    - Pool size = ~10-15 views
    - Original 100 items but only ~10 views created

    How recycling works:
    1. View scrolls off screen
    2. Adapter called with holder+position
    3. onBindViewHolder updates data
    4. View repositioned with new content
    5. No new View created

    ARCHITECTURE:
    - RecyclerView: Container
    - Adapter: Binds data to views
    - ViewHolder: Holds view references (pattern)
    - LayoutManager: Positions views
    - ItemAnimator: Animations

    Key efficiencies:
    - View reuse (memory efficient)
    - Predictable scroll performance
    - Animations support
    - Multiple layout types
    - Item decoration/spacing

    Best practices:
    - Use ViewBinding in ViewHolder
    - Avoid heavy operations in onBindViewHolder
    - Load images asynchronously
    - Use DiffUtil for updates


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/recyclerview-efficiency/#recyclerview-efficiency)


---

<div id="rendering-pipeline"></div>

# How does Android render UI frames?

**Difficulty:** `intermediate` • **Tags:**
`android`
`rendering`
`performance`

??? question "How does Android render UI frames?"

    RENDERING PIPELINE (per frame):

    1. MEASURE:
    - Layout system calculates view dimensions
    - ViewGroup measures children
    - Recursive: child measures own children

    2. LAYOUT:
    - System positions views using measured sizes
    - ViewGroup places children at x,y coordinates

    3. DRAW:
    - Canvas API draws views
    - Each View.onDraw() paints content
    - Composited into single frame buffer

    4. COMPOSITE:
    - Hardware accelerator combines layers
    - Handles transparency, transformations

    5. DISPLAY:
    - GPU sends frame to display
    - Vsync synchronized (60/90/120 fps)

    TIMING BUDGET (60 fps):
    - 16.67 milliseconds per frame
    - Measure/Layout/Draw/Composite: <16.67ms
    - Miss budget: Frame dropped, jank visible

    OPTIMIZATION:

    1. Reduce View hierarchy:
    - Fewer views = faster measure/layout
    - Use merge, include, ViewStub

    2. Use ViewHolder pattern:
    - Avoid repeated findViewById

    3. Avoid layout thrashing:
    - Don't measure in layout
    - Batch layout updates

    4. Use hardware acceleration:
    - Enabled by default
    - Use Layer types for animations

    Profiling: GPU rendering debug, Layout Inspector.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/rendering-pipeline/#rendering-pipeline)


---

<div id="storage-types"></div>

# What are the different storage options in Android?

**Difficulty:** `beginner` • **Tags:**
`android`
`storage`
`data`

??? question "What are the different storage options in Android?"

    1. SHARED PREFERENCES:
    - Key-value store
    - SharedPreferences.getSharedPreferences()
    - Best for small data (settings, flags)
    - Lightweight
    - NOT encrypted

    2. INTERNAL STORAGE:
    - App-private directory
    - Deleted when app uninstalled
    - Default choice for app data
    - Secure (not accessible by other apps)

    3. EXTERNAL STORAGE:
    - Public folders (/DCIM, /Pictures, /Documents)
    - Shared with other apps
    - Requires permissions
    - May not exist on all devices

    4. DATABASE (SQLite):
    - Structured data
    - Room library (ORM)
    - Relational queries
    - Good for complex data

    5. CONTENT PROVIDERS:
    - Expose data to other apps
    - Standardized data access interface
    - Used for contacts, photos, etc

    6. CACHE:
    - context.getCacheDir()
    - Temporary data
    - Can be cleared by system
    - Don't expect data persistence

    Rules:
    - Small settings: SharedPreferences
    - Complex data: Room Database
    - Cross-app: ContentProvider
    - Temporary: Cache
    - Media: External storage

    Best practice: Use Room for structured data.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/storage-types/#storage-types)


---

<div id="task-and-backstack"></div>

# What is a Task and back stack in Android?

**Difficulty:** `intermediate` • **Tags:**
`android`
`backstack`
`navigation`

??? question "What is a Task and back stack in Android?"

    TASK: Collection of activities arranged in backstack.

    Each task has:
    - One backstack
    - Activities from multiple apps possible
    - Identified by taskId
    - Shown in recents

    BACKSTACK: LIFO (Last-In-First-Out) structure
    - Activities arranged in order launched
    - Current activity at top
    - User press back: removes top activity

    EXAMPLE BACKSTACK (top to bottom):
    [Activity D] ← Current
    [Activity C]
    [Activity B]
    [Activity A] ← Home/root

    User presses back:
    [Activity D] removed → [Activity C] shown

    FLAGS AFFECTING BACKSTACK:

    FLAG_ACTIVITY_NEW_TASK:
    - New activity starts in new task

    FLAG_ACTIVITY_CLEAR_TOP:
    - Removes all activities above target
    - Target becomes top

    FLAG_ACTIVITY_SINGLE_TOP:
    - If activity at top: calls onNewIntent()
    - Doesn't create duplicate

    MULTI-APP TASKS:
    - TaskX contains ActivityA(App1), ActivityB(App2)
    - Back press: goes to App1 or App2
    - Task spans apps

    Best practice:
    - Use Navigation Component (handles backstack)
    - Understand task management
    - Use flags appropriately


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/task-and-backstack/#task-and-backstack)


---

<div id="process-death-lifecycle"></div>

# What happens to app state when process is killed?

**Difficulty:** `advanced` • **Tags:**
`android`
`lifecycle`
`process`

??? question "What happens to app state when process is killed?"

    PROCESS DEATH: OS kills app process to free memory (no warning).

    BEFORE KILL (chance to save):
    - onSaveInstanceState() called
    - Stored in Bundle
    - Persisted by system

    DURING KILL:
    - Process terminated
    - No cleanup callbacks possible
    - In-memory state lost
    - No warning given

    ON USER RETURN:
    - If Activity saved state:
      - OS recreates process
      - onCreate(savedInstanceState) called
      - App can restore Bundle data
    - If no saved state:
      - Activity restarted fresh
      - UI reset

    DATA LOSS:
    - In-memory variables lost
    - Unsaved changes lost
    - ViewModels destroyed
    - Connections closed

    PRESERVATION STRATEGIES:

    1. savedInstanceState:
    - Light data (Bundles, primitives)
    - ~100KB limit
    - Configuration changes + process death

    2. ViewModel:
    - Survives configuration changes
    - Lost on process death
    - Use with savedInstanceState

    3. Database:
    - Persistent storage
    - Survives everything
    - Use for critical data

    4. Preferences:
    - Settings persistence
    - Survives everything

    Best practice: ViewModel + Room Database + savedInstanceState
    for robust state management.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/process-death-lifecycle/#process-death-lifecycle)


---

<div id="multitasking-window-focus"></div>

# How does multitasking affect activity lifecycle?

**Difficulty:** `intermediate` • **Tags:**
`android`
`lifecycle`
`multitasking`

??? question "How does multitasking affect activity lifecycle?"

    MULTITASKING SCENARIOS:

    1. SPLIT SCREEN:
    - Two apps visible simultaneously
    - Both in foreground state
    - Both receive onResume()
    - Top activity interactive, other visible

    2. PICTURE-IN-PICTURE:
    - App playing video in small window
    - onPause() called (not visible)
    - Continues running
    - User can interact with background

    3. APP SWITCHING (Recents):
    - Swipe from other app
    - Current Activity: onPause → onStop
    - Switched app: onStart → onResume
    - Current app not destroyed (still in memory)

    LIFECYCLE IMPACT:

    Old app (going background):
    onPause() → onStop()

    New app (coming foreground):
    onStart() (if first time) or
    onStart() → onResume() (if was paused)

    IMPORTANT:
    - onPause() called for BOTH foreground apps
    - Only top activity "interactive"
    - Other visible but not interactive

    CONSEQUENCES:
    - Stop CPU-heavy operations in onPause()
    - Resume operations in onResume()
    - Don't assume onStop() means background
    - May be visible but not interactive

    Example: Video player in split screen
    - visible but onPause() called
    - Should pause playback in onPause()
    - Resume in onResume()


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/multitasking-window-focus/#multitasking-window-focus)

