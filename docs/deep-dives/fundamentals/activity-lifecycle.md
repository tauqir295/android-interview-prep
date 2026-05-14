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
## Activity Lifecycle Deep Dive

## Overview
The Activity lifecycle is the set of states an Activity moves through, managed by the Android OS to optimize:
- **Memory Management:** Reclaiming RAM from background apps.
- **Battery Usage:** Stopping sensors/animations when not visible.
- **UI Restoration:** Preserving user input during interruptions.
- **Multitasking:** Handling seamless transitions between apps.
- **Process Recovery:** Recreating the UI after the system kills a task.

---

## Core Lifecycle States

### 1. Created (`onCreate`)
The entry point. Perform one-time setup here: inflate UI, initialize ViewModels, and bind data.
- **State:** The activity exists but is not visible.

### 2. Started (`onStart`)
The activity becomes visible to the user. The app prepares to enter the foreground.
- **State:** Visible, but not yet interactive.

### 3. Resumed (`onResume`)
The activity is in the foreground and has user focus. 
- **Action:** Start animations, camera previews, or high-frequency updates.
- **State:** **Interactive.**

### 4. Paused (`onPause`)
The activity is partially obscured (e.g., by a dialog or multi-window mode).
- **Critical:** Keep this lightweight. The next activity cannot start until this finishes.
- **State:** Partially visible, losing focus.

### 5. Stopped (`onStop`)
The activity is no longer visible. 
- **Action:** Save persistent data (database/network), stop heavy CPU tasks.
- **State:** Hidden, resides in the backstack.

### 6. Destroyed (`onDestroy`)
The final cleanup. Occurs when the user finishes the activity or the system needs space.
- **State:** Removed from memory.

---

## Common Lifecycle Triggers
- **Screen Rotation:** Destroys and recreates the activity (Configuration Change).
- **Incoming Calls:** Moves activity to `onPause` or `onStop`.
- **Split-Screen Mode:** Triggers lifecycle changes as focus shifts between windows.
- **App Switching:** Moves the current app to `onStop`.
- **Process Death:** The OS kills a `Stopped` activity to free RAM.

---

## Typical Lifecycle Implementation

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Log.d("Lifecycle", "onCreate: Activity created")
    }

    override fun onStart() {
        super.onStart()
        Log.d("Lifecycle", "onStart: Activity visible")
    }

    override fun onResume() {
        super.onResume()
        Log.d("Lifecycle", "onResume: Activity interactive")
    }

    override fun onPause() {
        super.onPause()
        Log.d("Lifecycle", "onPause: Focus lost")
    }

    override fun onStop() {
        super.onStop()
        Log.d("Lifecycle", "onStop: No longer visible")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("Lifecycle", "onDestroy: Activity destroyed")
    }
}
```
