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
## App Startup Flow Deep Dive

## Overview

App startup is the path from launcher tap to first interactive frame. Interviewers care about startup stages and optimization strategy.

---

## Startup Stages

- **Cold start**: process not in memory.
- **Warm start**: process exists, activity recreated.
- **Hot start**: activity already in memory and resumed quickly.

---

## Cold Start Sequence

1. Launcher sends intent.
2. ActivityTaskManager/ActivityManager resolves target.
3. Process created (via Zygote fork).
4. `Application.onCreate()` runs.
5. Activity instance created.
6. `onCreate()` -> `onStart()` -> `onResume()`.
7. First frame rendered.

---

## Optimization Principles

- Keep `Application.onCreate()` minimal.
- Defer non-critical SDK initialization.
- Use lazy loading for feature modules and heavy objects.
- Move disk/network work off main thread.
- Track startup metrics in CI/release builds.

---

## Measuring Startup

- Android Studio profiler/traces.
- `reportFullyDrawn()` for meaningful readiness signal.
- Baseline Profiles to improve runtime performance.

---

## Interview Traps

- "First frame" is not equal to "fully usable UI".
- Splash screen should not mask heavy startup anti-patterns.

---

## Key Takeaways

- Startup quality is architecture + measurement + discipline.
- Optimize cold start first for user-perceived performance.

