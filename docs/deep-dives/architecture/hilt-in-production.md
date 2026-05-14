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

# Hilt in Production Deep Dive

## Overview

Hilt standardizes dependency injection for Android lifecycle components.
Its value is consistency and lower setup cost across teams.

## Core Concepts

- annotation-driven graph wiring
- predefined component hierarchy
- scope annotations tied to lifecycle
- entry points for framework-created objects

## Layer Responsibilities

- App/platform layer:
  - define global bindings and singleton services
- Feature layer:
  - declare feature-scoped dependencies
- ViewModel layer:
  - consume use cases/repositories via constructor injection

## Data Flow

1. App starts and creates root component.
2. Android component creates child scope.
3. ViewModel receives injected dependencies.
4. Runtime resolves graph lazily/eagerly based on usage.

## Internal Architecture

Critical component lifetimes:

- `SingletonComponent` for process-wide services
- `ActivityRetainedComponent` for config-safe objects
- `ViewModelComponent` for screen logic scope
- `ActivityComponent`/`FragmentComponent` for UI-bound dependencies

## Code Examples

```kotlin
@HiltViewModel
class SettingsViewModel @Inject constructor(
    private val loadSettings: LoadSettingsUseCase
) : ViewModel()

@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    @Singleton
    fun provideApi(client: OkHttpClient): AppApi = AppApi(client)
}
```

## Common Interview Questions

- Hilt vs raw Dagger: what changes practically?
- Which scope should this dependency use?
- When do you need an entry point?
- How do you test Hilt-heavy modules?

## Production Considerations

- keep modules close to feature ownership boundaries
- avoid blanket singleton usage for mutable objects
- monitor annotation-processing cost in large projects
- document scope conventions for onboarding

## Scalability Tradeoffs

- Pros:
  - standardized DI architecture and fast team adoption
  - fewer custom graph plumbing errors
- Cons:
  - reduced flexibility for exotic graph patterns
  - generated code errors can be hard for new devs

## Senior-Level Insights

Senior engineers should explain scope discipline and governance.
Most Hilt failures at scale are ownership and lifecycle design issues,
not missing annotations.
