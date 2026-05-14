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

# Multitasking and Window Focus Deep Dive

## Overview

Modern Android supports split-screen, picture-in-picture, and rapid app switching. Lifecycle transitions depend on both visibility and input focus.

---

## Visibility vs Focus

- An activity can be visible but not focused.
- Focus loss often triggers `onPause()`.
- Full invisibility transitions toward `onStop()`.

---

## Typical Scenarios

### Split Screen

- Multiple activities may be visible.
- Only one is primary focused for input at a time.

### Picture-in-Picture

- Host activity enters PiP mode.
- Lifecycle and UI logic should adapt to reduced surface.

### App Switching

- Foreground activity pauses/stops as another app resumes.

---

## Practical Handling

- Pause camera/mic/sensors in `onPause()` when appropriate.
- Resume interaction-specific resources in `onResume()`.
- Persist transient UI state before potential stop/kill.

---

## Interview Traps

- Equating visible with focused is incorrect.
- Heavy cleanup in `onPause()` can degrade transitions.

---

## Key Takeaways

- Build lifecycle logic around visibility + focus, not only foreground/background.
- Test on split-screen and PiP to validate assumptions.

