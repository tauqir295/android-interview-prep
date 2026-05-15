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

## Network Security and API Abuse Deep Dive

## Overview
Transport security protects confidentiality, while backend controls protect business logic.

## Network Security Config
- Disable cleartext traffic in release.
- Separate debug and release trust anchors.
- Restrict domain policies to what the app actually needs.

## Certificate Pinning Tradeoffs
- Adds MITM resistance for high-risk use cases.
- Requires backup pins, rotation runbooks, and outage fallback.

## API Abuse Controls
- Keep authorization server-side.
- Rate limit and anomaly-detect suspicious clients.
- Use short-lived tokens and device/session binding where appropriate.

## Senior-Level Insights
- Mobile transport controls are necessary but insufficient without backend abuse defenses.

