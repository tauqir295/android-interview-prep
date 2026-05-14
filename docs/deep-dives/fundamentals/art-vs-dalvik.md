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
# ART vs Dalvik Deep Dive

## Overview

Dalvik was Android's original runtime; ART replaced it with improved startup, performance, and tooling. Modern ART uses hybrid compilation strategies.

---

## Dalvik

- Primarily JIT-centric at runtime.
- Lower install-time overhead.
- More runtime compilation cost and variability.

## ART

- Ahead-of-time and profile-guided optimizations.
- Faster startup and better steady-state behavior.
- Improved GC, diagnostics, and tooling support.

---

## Practical Differences

- **Startup**: ART generally faster.
- **Battery**: ART often better due to reduced runtime compilation overhead.
- **Install/updates**: May involve compilation work depending on profile state.

---

## Interview Focus

- Explain JIT vs AOT tradeoff clearly.
- Mention modern ART is hybrid/profile-guided, not purely one mode.
- Connect runtime choice to UX metrics (cold start, jank, battery).

---

## Key Takeaways

- ART improved Android runtime consistency and performance.
- Modern behavior is hybrid and profile driven.
- Optimization still depends on app code quality and startup discipline.

