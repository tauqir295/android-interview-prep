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

# UI State and Event Modeling Deep Dive

## Overview

UI architecture quality depends on modeling state and events explicitly.
Clear contracts prevent sticky-event bugs, duplicated retries,
and inconsistent error rendering.

## Core Concepts

- persistent `UiState` for renderable screen model
- transient event channel for one-time actions
- error taxonomy mapped to user-actionable outcomes
- retry policy as explicit state transition, not ad-hoc callbacks

## Layer Responsibilities

- UI:
  - render `UiState`
  - react to event stream once
- ViewModel/store:
  - own state transitions and event emission
  - map technical errors to UX-safe states
- Domain/data:
  - provide normalized result/error models

## Data Flow

1. Action intent enters ViewModel.
2. Use case/repository returns success or categorized failure.
3. ViewModel emits new `UiState` branch (loading/content/error/empty).
4. Optional one-time event emits for toast/navigation/dialog.
5. User retry intent triggers controlled transition.

## Internal Architecture

Good model patterns:

- sealed state branches for mutually exclusive UI modes
- separate retry metadata (attempt count, next allowed time)
- standardized error mapping layer (network/auth/business)
- idempotent reducer updates for repeated events

## Code Examples

```kotlin
sealed interface CheckoutUiState {
    data object Loading : CheckoutUiState
    data class Content(val total: String) : CheckoutUiState
    data class Error(val message: String, val canRetry: Boolean) : CheckoutUiState
}

sealed interface CheckoutEvent {
    data object ShowPaymentFailedToast : CheckoutEvent
}
```

## Common Interview Questions

- Why not keep one-off events inside state?
- How do you avoid event replay on rotation?
- Where should retry backoff decisions live?
- How do you keep error handling consistent across features?

## Production Considerations

- define shared UX error standards across teams
- log error category and user action path for observability
- cap auto-retry behavior to avoid backend abuse
- add regression tests for event replay edge cases

## Scalability Tradeoffs

- Pros:
  - clearer rendering logic and fewer race-condition bugs
  - easier incident analysis from explicit transitions
- Cons:
  - more model classes and conventions to maintain
  - potential verbosity in simple screens

## Senior-Level Insights

Senior engineers should tie state modeling to product reliability.
The best systems make failure states first-class,
not bolt-ons added after incidents.
