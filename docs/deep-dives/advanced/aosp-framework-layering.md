---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/advanced/">← Back to Advanced & Internals</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/advanced/${hash}`);
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

## Aosp Framework Layering Deep Dive

## Overview

- Define constraints and target outcomes clearly.
- Explain tradeoffs and alternatives.
- Connect decisions to reliability, maintainability, and delivery speed.

## Core Concepts

- Define constraints and target outcomes clearly.
- Explain tradeoffs and alternatives.
- Connect decisions to reliability, maintainability, and delivery speed.

## Internal Implementation

- Define constraints and target outcomes clearly.
- Explain tradeoffs and alternatives.
- Connect decisions to reliability, maintainability, and delivery speed.

## Runtime / System Flow

- Define constraints and target outcomes clearly.
- Explain tradeoffs and alternatives.
- Connect decisions to reliability, maintainability, and delivery speed.

## Architecture and Tradeoffs

- Define constraints and target outcomes clearly.
- Explain tradeoffs and alternatives.
- Connect decisions to reliability, maintainability, and delivery speed.

## Code Examples

```kotlin
fun decision() = "Measure before optimize"
```

## Common Interview Questions

- **Q:** What role does RenderThread play?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
- **Q:** What is init.rc and why does it matter?
  **A:** Answer with internals-first reasoning: describe the subsystem boundaries, explain the runtime behavior and bottlenecks, then show how you would validate with traces and measurable latency or memory budgets.
- **Q:** How do AOSP boundaries influence app architecture?
  **A:** Answer with internals-first reasoning: describe the subsystem boundaries, explain the runtime behavior and bottlenecks, then show how you would validate with traces and measurable latency or memory budgets.
## Production Considerations

- Define constraints and target outcomes clearly.
- Explain tradeoffs and alternatives.
- Connect decisions to reliability, maintainability, and delivery speed.

## Performance Insights

- Define constraints and target outcomes clearly.
- Explain tradeoffs and alternatives.
- Connect decisions to reliability, maintainability, and delivery speed.

## Senior-Level Insights

- Define constraints and target outcomes clearly.
- Explain tradeoffs and alternatives.
- Connect decisions to reliability, maintainability, and delivery speed.
