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
## Rendering Pipeline Deep Dive

## Overview

Android frame rendering follows a measure-layout-draw pipeline coordinated with display vsync. Missing frame deadlines causes jank.

---

## Frame Pipeline

1. **Measure**: determine view sizes.
2. **Layout**: place views in parent bounds.
3. **Draw**: record drawing commands.
4. **RenderThread/GPU**: rasterize and compose.
5. **Display**: present frame on next vsync.

---

## Frame Budget

- 60 Hz -> 16.67 ms per frame.
- 120 Hz -> 8.33 ms per frame.
- Exceeding budget drops/skips frames.

---

## Common Jank Sources

- Heavy work on main thread during input/animation.
- Excessive layout passes (requestLayout storms).
- Overdraw and complex alpha blending.
- Expensive bitmap decode/transform at draw time.

---

## Optimization Strategies

- Flatten view hierarchies.
- Avoid invalidating large areas unnecessarily.
- Precompute text/layout data.
- Move expensive work off main thread.
- Use profiler tools to target hotspots.

---

## Interview Traps

- "GPU accelerated" does not mean main thread can block.
- Smoothness requires both CPU and GPU staying within frame budget.

---

## Key Takeaways

- Rendering performance is deadline-driven.
- Measure, profile, then optimize the true bottleneck.

