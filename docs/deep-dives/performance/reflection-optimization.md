---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/performance/">← Back to Performance</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/performance/${hash}`);
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

## Reflection Optimization Deep Dive
## Overview
This topic matters in Android interviews because performance work requires hot-path reflection removal, codegen alternatives, and cached lookup strategy rather than guesswork.
## Core Concepts
- Measure before optimizing.
- Focus on user-visible latency and stability.
- Keep regressions detectable through budgets.
## Internal Implementation
- Identify critical path in UI, data, and background work.
- Isolate expensive operations away from the main thread.
- Use bounded concurrency to reduce contention.
## Measurement and Profiling Flow
- Reproduce issue with a stable scenario.
- Capture traces/profiles across CPU, memory, and rendering.
- Validate fix with before/after metrics under same conditions.
## Optimization Techniques
- Remove unnecessary work first.
- Reduce allocation and synchronization pressure.
- Stage rollouts with monitoring guardrails.
## Code Examples
```kotlin
val start = System.nanoTime()
renderFrame()
val ms = (System.nanoTime() - start) / 1_000_000.0
```
## Common Interview Questions
- **Q:** Which metric tells you this optimization worked?
  **A:** Answer with measurement-first reasoning: define the baseline, optimize the highest-impact bottleneck, and prove improvement with user-visible metrics.
- **Q:** How do you avoid premature optimization?
  **A:** Answer with measurement-first reasoning: define the baseline, optimize the highest-impact bottleneck, and prove improvement with user-visible metrics.
- **Q:** What tradeoff did you accept to improve responsiveness?
  **A:** Answer with measurement-first reasoning: define the baseline, optimize the highest-impact bottleneck, and prove improvement with user-visible metrics.
## Production Considerations
- Define performance budgets per critical user journey.
- Alert on regressions, not just absolute incidents.
- Track low-end device behavior separately.
## Performance Insights
- Most wins come from reducing work, not micro-optimizations.
- Smoothness consistency often matters more than peak throughput.
## Senior-Level Insights
- Strong candidates connect technical changes to product impact and team process.
