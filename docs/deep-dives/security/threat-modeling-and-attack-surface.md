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

## Threat Modeling and Attack Surface Deep Dive

## Overview
Threat modeling identifies realistic abuse paths before they become incidents.

## Core Concepts
- Assets: auth tokens, PII, payment actions, privileged APIs.
- Entry points: exported components, deep links, WebView, local storage, network calls.
- Trust boundaries: device, app sandbox, backend, third-party SDKs.

## Practical Framework
- Enumerate attacker goals and capabilities.
- Map data flows and privileges.
- Score risks by impact x likelihood.
- Prioritize mitigations and detection controls.

## Common Interview Questions
- **Q:** How is a mobile threat model different from backend threat modeling?
  **A:** Answer in layered controls: model threats, harden identity and transport, protect keys and secrets, add runtime integrity signals, and define response playbooks.
- **Q:** Which findings should block release?
  **A:** Lead with correctness then throughput: choose dispatcher by workload type, keep critical sections small, cap parallelism, and monitor tail latency and queue depth.
## Production Considerations
- Re-run threat models for major feature launches, auth changes, and SDK additions.
- Tie findings to backlog items with owners and deadlines.

## Senior-Level Insights
- Strong candidates connect mitigations to measurable risk reduction and incident trends.

