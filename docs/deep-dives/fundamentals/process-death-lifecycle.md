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

# Process Death Lifecycle Deep Dive

## Overview

Android can kill app processes under memory pressure. Robust apps restore state correctly when process is recreated.

---

## What Survives and What Doesn't

### Lost on Process Death

- In-memory objects
- ViewModel instances
- Ongoing in-process jobs

### Can Be Restored

- `savedInstanceState` UI state
- Persisted data from Room/files/preferences

---

## Recovery Pattern

1. Save lightweight UI state in `onSaveInstanceState`.
2. Keep source of truth in persistent storage.
3. Rehydrate screen state from repository on recreation.

```kotlin
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putInt("scroll", recyclerView.computeVerticalScrollOffset())
}
```

---

## Architecture Guidance

- UI state: Bundle + `SavedStateHandle`.
- Durable state: Room/DataStore/network cache.
- Avoid relying only on ViewModel for critical data.

---

## Interview Traps

- "ViewModel survives process death" -> false.
- Assuming `onDestroy()` always runs before death -> false.

---

## Key Takeaways

- Design for process death from day one.
- Persist essentials and restore deterministically.

