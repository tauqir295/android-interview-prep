---
hide:
  - toc
---

!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/security/">← Back to Security</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/security/${hash}`);
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

## Manifest and Component Hardening Deep Dive

## Overview
Most Android app attack surface is created by manifest and IPC configuration mistakes.

## Hardening Checklist
- Set `android:exported` explicitly for every component.
- Guard privileged components with signature permissions.
- Validate all Intent extras and URI inputs.
- Disable debug flags and unnecessary permissions in release builds.

## Component-Specific Notes
- Activities: allowlist deep link hosts and sanitize inputs.
- Services: require caller auth and enforce permission checks.
- Receivers: avoid broad implicit intents for sensitive actions.

## Testing Ideas
- Intent fuzzing for malformed extras.
- Spoofed caller tests for exported services/receivers.
- Manifest policy checks in CI.

## Senior-Level Insights
- Teams that codify these checks in lint and CI avoid most repeat security regressions.

