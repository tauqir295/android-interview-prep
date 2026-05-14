# Fundamentals


---

# What is the Activity Lifecycle?

**Difficulty:** `beginner` • **Tags:**
`android`
`activity`
`lifecycle`

???+ question "What is the Activity Lifecycle?"

    The Activity Lifecycle is the sequence of states an Android
    Activity transitions through from creation to destruction.

    Android manages these lifecycle callbacks automatically to:

    - optimize memory usage
    - handle interruptions
    - restore UI state
    - support multitasking

    Core lifecycle states:

    - `onCreate()` → Initial setup; called once when Activity is created
    - `onStart()` → Activity becomes visible to the user
    - `onResume()` → Activity enters foreground and becomes interactive
    - `onPause()` → Activity partially loses focus; pause lightweight work
    - `onStop()` → Activity no longer visible; save heavy data/resources
    - `onDestroy()` → Final cleanup before Activity removal

    The lifecycle is fully managed by the Android OS based on:

    - user navigation
    - configuration changes
    - multitasking
    - memory pressure


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/fundamentals/activity-lifecycle/)

