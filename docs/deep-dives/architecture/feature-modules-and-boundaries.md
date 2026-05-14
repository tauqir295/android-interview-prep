---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/architecture/">← Back to Architecture</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/architecture/${hash}`);
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

# Feature Modules and Boundaries Deep Dive

## Overview

Feature modules help scale product development when boundaries match user capability
and team ownership. Good boundaries reduce coupling and release risk.

## Core Concepts

- feature-first module slicing by business capability
- explicit inter-feature contracts
- local ownership of UI/domain behavior
- dependency direction toward shared contracts, not peer internals

## Layer Responsibilities

- Feature module:
  - feature UI orchestration
  - feature-specific use cases and mappers
- Shared/core modules:
  - common infra and cross-feature contracts
- App shell:
  - top-level wiring and navigation composition

## Data Flow

1. Feature UI triggers feature use case.
2. Use case calls local/shared contracts.
3. Data is resolved by owning feature/data module.
4. Result maps back into feature-local UI state.
5. Cross-feature navigation/events use contract interfaces.

## Internal Architecture

Boundary signals for healthy feature modules:

- minimal imports from peer feature modules
- API-only contract exposure
- no direct access to peer internal models
- isolated tests and build targets

Dynamic feature modules add delivery flexibility but operational complexity.

## Code Examples

```kotlin
// contract module
interface ProfileEntry {
    fun open(userId: String)
}

// feature implementation module
class ProfileEntryImpl(
    private val nav: Navigator
) : ProfileEntry {
    override fun open(userId: String) = nav.go("profile/$userId")
}
```

## Common Interview Questions

- How do you choose feature boundaries initially?
- How do you prevent cross-feature dependency creep?
- When are dynamic feature modules worth it?
- How do you handle shared design-system dependencies?

## Production Considerations

- enforce dependency rules in CI
- version and deprecate feature contracts explicitly
- assign clear module ownership and on-call accountability
- track build and integration cost per module

## Scalability Tradeoffs

- Pros:
  - team autonomy and safer parallel delivery
  - more targeted releases and refactors
- Cons:
  - contract coordination overhead
  - increased dependency management complexity

## Senior-Level Insights

Senior discussions should include boundary evolution.
As product scope changes, feature boundaries should be revisited,
not treated as permanent architecture law.
