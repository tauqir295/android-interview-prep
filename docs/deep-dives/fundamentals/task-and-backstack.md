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
## Task and Back Stack Deep Dive

## Overview

A task is a collection of activities arranged in a back stack. Back navigation pops activities in LIFO order and task/intent flags can significantly change behavior.

---

## Core Concepts

- **Task**: logical user journey container.
- **Back stack**: activity stack inside task.
- **Recents screen**: task-level entry point.

---

## Launch and Back Behavior

- New activity usually pushed to current task stack.
- Back pops top activity.
- If root popped, task leaves foreground.

---

## Important Flags

- `FLAG_ACTIVITY_NEW_TASK`: launch in new or existing task by affinity.
- `FLAG_ACTIVITY_CLEAR_TOP`: pop above target if already in stack.
- `FLAG_ACTIVITY_SINGLE_TOP`: reuse top instance via `onNewIntent()`.

---

## Launch Modes (high level)

- `standard`
- `singleTop`
- `singleTask`
- `singleInstance` / `singleInstancePerTask`

Use sparingly; prefer Navigation Component defaults unless specific behavior needed.

---

## Interview Traps

- Mixing launch modes and flags can create unexpected UX.
- Deep links may create parallel task flows if misconfigured.

---

## Key Takeaways

- Understand default stack behavior first, then add flags intentionally.
- Validate navigation with real back/recents testing.

