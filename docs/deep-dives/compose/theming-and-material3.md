---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/compose/">← Back to Compose</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/compose/${hash}`);
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
## Theming and Material 3 Deep Dive

## Overview

Compose theming is a design-system contract using color, typography, and shape tokens,
commonly powered by Material 3.

## Core Concepts

- `MaterialTheme` token provision
- light/dark mode and dynamic color
- custom design tokens layered on top

## Runtime Internals

Theme values are provided through composition locals; changes invalidate consumers
that read those tokens.

## Composition / Recomposition Flow

- theme provider updates token set
- token consumers are invalidated
- affected UI branches recompose

## State Management

Theme selection (user/system) should come from app-level state and be applied
at shell/root composition boundary.

## Code Examples

```kotlin
MaterialTheme(
    colorScheme = if (isDark) darkColorScheme() else lightColorScheme(),
    typography = AppTypography,
    shapes = AppShapes
) {
    AppContent()
}
```

## Common Interview Questions

- How do you support dynamic color and brand colors together?
- Where should theme switching state live?

## Production Considerations

- keep token names domain-friendly
- avoid hardcoded colors in feature composables
- verify accessibility contrast and large-text behavior

## Performance Insights

Frequent top-level theme toggles can trigger broad recomposition; scope theme
changes intentionally.

## Senior-Level Insights

Senior-level discussion should include governance of design tokens across teams
and avoiding theme drift in large codebases.
