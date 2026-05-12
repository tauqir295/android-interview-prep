# Fundamentals Interview Questions

!!! info "Status"
    This section is currently being updated for 2026 Android standards.

## 📝 Introduction
Brief overview of why fundamentals is important in Android interviews.

## 🚀 Key Questions

!!! question "What is the Activity Lifecycle?"
    **Standard Answer:** The Activity lifecycle is a set of 7 core methods (`onCreate` through `onDestroy`) that the system calls as a user navigates into, out of, and back to your app. It allows the app to manage resources efficiently and preserve UI state.

    ??? info "🚀 View Detailed Deep Dive"
        === "Detailed Explanation"
            The lifecycle ensures that your app doesn't crash during a phone call, consume battery when not in use, or lose the user's progress.
            
            * **`onCreate()`**: Mandatory. Fired when the system first creates the activity. Perform one-time setup here (binding data, inflating UI).
            * **`onStart()`**: The activity is becoming visible to the user but is not yet in the foreground.
            * **`onResume()`**: The activity is now in the "top" position and the user can interact with it. 
            * **`onPause()`**: Used to pause ongoing actions (like animations) that shouldn't consume CPU while semi-visible (e.g., in Multi-window mode).
            * **`onStop()`**: The activity is no longer visible. Good place to release heavy resources.
            * **`onRestart()`**: Called after `onStop()` when the user navigates back to the activity.
            * **`onDestroy()`**: Final call before the activity is removed from memory.

        === "Internal Functions"
            The lifecycle isn't just magic; it's a orchestration between the **ActivityManagerService (AMS)** and the **ActivityThread**.

            ```kotlin
            // Logic inside ActivityThread.java (Simplified)
            private void handleStartActivity(ActivityClientRecord r) {
                // 1. Instrumentation calls the Activity's performStart
                r.activity.performStart("handleStartActivity");
                
                // 2. Which eventually triggers the developer's override
                final void performStart() {
                    mCalled = false;
                    onStart(); // Developer code runs here
                    if (!mCalled) {
                        throw new SuperNotCalledException(
                            "Activity " + mComponent + " did not call through to super.onStart()");
                    }
                }
            }
            ```
            **Key Internal:** The `mCalled` boolean is why you MUST call `super.onCreate()`. If it's false after the method returns, the app crashes.

        === "Follow-up Questions"
            * **Q: What happens if `super.onCreate()` is not called?**
                * **A:** The app will throw a `SuperNotCalledException`. The system uses this flag to ensure necessary internal setup is completed.
            * **Q: Difference between `onStart()` and `onResume()`?**
                * **A:** `onStart()` makes the Activity visible; `onResume()` makes it interactive. You can be in `onStart()` but have a dialog or system overlay preventing interaction (keeping you from `onResume()`).
            * **Q: What is the only method where the Bundle is NOT null after process death?**
                * **A:** Both `onCreate(savedInstanceState)` and `onRestoreInstanceState(bundle)` receive the data, but `onRestoreInstanceState` is only called if the bundle is definitely not null.

        === "Interviewer Traps"
            * **The Multi-Window Trap:** "If I open my app in split-screen, am I always in `onResume()`?"
                * **Fact:** No. Only the app the user last touched is `onResume()`. The other visible app is in `onPause()`.
            * **The Memory Trap:** "Can I rely on `onDestroy()` to save my data?"
                * **Fact:** **Never.** If the system is low on memory, it may kill your process directly after `onStop()` without ever calling `onDestroy()`. Always save persistent data in `onStop()` or `onPause()`.
            * **The Finish Trap:** "If I call `finish()` in `onCreate()`, which methods are called?"
                * **Fact:** The system immediately skips to `onDestroy()`. `onStart` and `onResume` are never reached.