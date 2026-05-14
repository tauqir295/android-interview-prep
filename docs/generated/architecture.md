---
hide:
  - toc
---

# Architecture

<script>
(function () {
  function openQuestionFromHash() {
    const hash = window.location.hash;
    if (!hash || hash.length <= 1) return;

    const anchor = document.querySelector(hash);
    if (!anchor) return;

    let node = anchor.nextElementSibling;
    while (node) {
      if (node.tagName === 'DETAILS') {
        node.open = true;
        anchor.scrollIntoView({ behavior: 'auto', block: 'start' });
        return;
      }
      node = node.nextElementSibling;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', openQuestionFromHash);
  } else {
    openQuestionFromHash();
  }

  window.addEventListener('hashchange', openQuestionFromHash);
})();
</script>


---

<div id="mvvm-basics"></div>

## What is MVVM in Android architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">mvvm</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    MVVM separates UI rendering from business/data orchestration.

    Typical split:

    - View: renders state and forwards user actions
    - ViewModel: exposes lifecycle-aware UI state
    - Repository: abstracts data access

    Why teams use it:

    - better testability
    - cleaner separation of concerns
    - easier lifecycle-safe state handling


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/mvvm-and-viewmodel/#mvvm-basics">🚀 See Full Deep Dive</a>


---

<div id="viewmodel-role"></div>

## What is the role of a ViewModel in scalable Android apps?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">viewmodel</span>
  <span class="question-badge question-badge--tag">state</span>
</div>

??? question "View Answer"

    ViewModel owns screen-level state and survives configuration changes.

    Key responsibilities:

    - transform domain data into UI-friendly state
    - coordinate use cases/repositories
    - expose immutable observable state
    - handle user intents/events

    It should avoid direct Android UI references.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/mvvm-and-viewmodel/#viewmodel-role">🚀 See Full Deep Dive</a>


---

<div id="savedstatehandle-usage"></div>

## When should you use SavedStateHandle in architecture design?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">viewmodel</span>
  <span class="question-badge question-badge--tag">state</span>
</div>

??? question "View Answer"

    Use `SavedStateHandle` for small, restorable screen state
    tied to process recreation.

    Good candidates:

    - selected tab/index
    - filter/sort selection
    - lightweight form progress

    Avoid storing large objects or domain caches in it.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/mvvm-and-viewmodel/#savedstatehandle-usage">🚀 See Full Deep Dive</a>


---

<div id="mvi-what-is"></div>

## What is MVI architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">mvi</span>
  <span class="question-badge question-badge--tag">state</span>
</div>

??? question "View Answer"

    MVI models UI as a loop: intent -> reducer -> new immutable state.

    Core benefits:

    - predictable state transitions
    - easier debugging/time-travel style reasoning
    - explicit event handling contract

    Tradeoff: can introduce boilerplate if over-applied.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/mvi-and-udf/#mvi-what-is">🚀 See Full Deep Dive</a>


---

<div id="mvi-vs-mvvm"></div>

## MVVM vs MVI - how do you choose?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">mvvm</span>
  <span class="question-badge question-badge--tag">mvi</span>
</div>

??? question "View Answer"

    Choose by complexity and team needs, not trend preference.

    MVVM:

    - lower ceremony
    - common Android default

    MVI:

    - stronger state/event determinism
    - better for complex interaction-heavy screens

    Many teams use MVVM + UDF patterns as a middle ground.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/mvi-and-udf/#mvi-vs-mvvm">🚀 See Full Deep Dive</a>


---

<div id="udf-principles"></div>

## What are the key principles of Unidirectional Data Flow?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">udf</span>
  <span class="question-badge question-badge--tag">state</span>
</div>

??? question "View Answer"

    UDF means state flows down, events flow up.

    Interview-ready points:

    - single source of truth for screen state
    - immutable state exposure
    - explicit intent/event handlers
    - deterministic state transitions

    This reduces hidden mutation bugs.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/mvi-and-udf/#udf-principles">🚀 See Full Deep Dive</a>


---

<div id="clean-architecture-overview"></div>

## What is Clean Architecture in Android?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">clean-architecture</span>
  <span class="question-badge question-badge--tag">layers</span>
</div>

??? question "View Answer"

    Clean Architecture organizes code by responsibility and dependency direction.

    Typical layers:

    - presentation
    - domain
    - data

    Main rule: inner layers should not depend on outer framework details.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/clean-architecture-layering/#clean-architecture-overview">🚀 See Full Deep Dive</a>


---

<div id="layer-dependency-rule"></div>

## What is the dependency rule in layered architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">clean-architecture</span>
  <span class="question-badge question-badge--tag">dependency-inversion</span>
</div>

??? question "View Answer"

    Dependencies must point inward toward stable policy layers.

    Practical implications:

    - UI depends on domain contracts
    - data implements domain abstractions
    - domain avoids Android/framework types

    This improves portability and test isolation.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/clean-architecture-layering/#layer-dependency-rule">🚀 See Full Deep Dive</a>


---

<div id="dependency-inversion-android"></div>

## How does dependency inversion apply to Android app architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">solid</span>
  <span class="question-badge question-badge--tag">dependency-inversion</span>
</div>

??? question "View Answer"

    High-level policies should depend on abstractions, not concrete SDK/data details.

    In Android this usually means:

    - domain uses interfaces
    - data/network/db implement those interfaces
    - DI wires concrete implementations

    It keeps business logic resilient to infrastructure changes.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/clean-architecture-layering/#dependency-inversion-android">🚀 See Full Deep Dive</a>


---

<div id="repository-pattern-purpose"></div>

## Why use the Repository pattern?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">repository</span>
  <span class="question-badge question-badge--tag">data</span>
</div>

??? question "View Answer"

    Repository abstracts data origin and provides a clean API to higher layers.

    Benefits:

    - decouples UI/domain from network/db details
    - centralizes data policies
    - simplifies testing with fakes
    - enables caching/sync orchestration


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/repository-pattern-and-data-sources/#repository-pattern-purpose">🚀 See Full Deep Dive</a>


---

<div id="repository-single-source-truth"></div>

## How does a repository support a Single Source of Truth model?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">repository</span>
  <span class="question-badge question-badge--tag">state</span>
</div>

??? question "View Answer"

    Repository enforces one authoritative read path for consumers.

    Common approach:

    - local DB is canonical source
    - network refresh updates DB
    - UI observes DB-backed streams

    This avoids competing data sources in UI.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/repository-pattern-and-data-sources/#repository-single-source-truth">🚀 See Full Deep Dive</a>


---

<div id="multiple-data-sources-orchestration"></div>

## How should repositories orchestrate network, cache, and database sources?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">repository</span>
  <span class="question-badge question-badge--tag">caching</span>
</div>

??? question "View Answer"

    Define explicit policies for freshness, fallback, and write ordering.

    Typical strategy:

    - read local first
    - fetch remote by staleness rules
    - merge/validate payload
    - persist then emit

    Keep these rules in repository, not UI.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/repository-pattern-and-data-sources/#multiple-data-sources-orchestration">🚀 See Full Deep Dive</a>


---

<div id="use-case-purpose"></div>

## What problem do use cases solve in architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">use-cases</span>
  <span class="question-badge question-badge--tag">domain</span>
</div>

??? question "View Answer"

    Use cases encapsulate business actions independent of UI and data frameworks.

    They help by:

    - isolating domain logic
    - improving reuse across screens
    - making behavior unit-testable
    - reducing ViewModel complexity


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/use-cases-and-domain-layer/#use-case-purpose">🚀 See Full Deep Dive</a>


---

<div id="use-case-granularity"></div>

## How granular should use cases be?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">use-cases</span>
  <span class="question-badge question-badge--tag">design</span>
</div>

??? question "View Answer"

    Use cases should represent coherent business actions, not tiny wrappers.

    Guidance:

    - too coarse: hard to compose/test
    - too fine: boilerplate and indirection
    - optimize for domain clarity and change boundaries

    Granularity is a context-based design decision.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/use-cases-and-domain-layer/#use-case-granularity">🚀 See Full Deep Dive</a>


---

<div id="domain-layer-when-to-add"></div>

## When is a dedicated domain layer worth adding?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">domain</span>
  <span class="question-badge question-badge--tag">clean-architecture</span>
</div>

??? question "View Answer"

    Add domain layer when business rules are non-trivial or reused.

    Signals:

    - multiple features share logic
    - policies outgrow ViewModels
    - testability/portability requirements increase

    For simple apps, extra layers can be unnecessary overhead.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/use-cases-and-domain-layer/#domain-layer-when-to-add">🚀 See Full Deep Dive</a>


---

<div id="dependency-injection-what-why"></div>

## Why is dependency injection important in Android architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">di</span>
  <span class="question-badge question-badge--tag">testability</span>
</div>

??? question "View Answer"

    DI manages object creation/wiring outside business logic.

    Benefits:

    - loose coupling
    - easier testing with fakes/mocks
    - centralized lifecycle/scope control
    - clearer dependency graph at scale


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/dependency-injection-strategies/#dependency-injection-what-why">🚀 See Full Deep Dive</a>


---

<div id="constructor-injection-vs-field-injection"></div>

## Constructor injection vs field injection - which is preferred?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">di</span>
  <span class="question-badge question-badge--tag">design</span>
</div>

??? question "View Answer"

    Constructor injection is usually preferred.

    Reasons:

    - explicit required dependencies
    - easier immutable object design
    - better unit-test ergonomics

    Field injection is useful in framework-controlled classes but less explicit.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/dependency-injection-strategies/#constructor-injection-vs-field-injection">🚀 See Full Deep Dive</a>


---

<div id="di-scope-management"></div>

## How do DI scopes affect memory and lifecycle behavior?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">di</span>
  <span class="question-badge question-badge--tag">lifecycle</span>
</div>

??? question "View Answer"

    Scopes define object lifetime and reuse boundaries.

    Mis-scoping can cause:

    - leaks (too long-lived)
    - churn/perf cost (too short-lived)
    - inconsistent shared state

    Align scopes with Activity/Fragment/ViewModel/app lifetimes.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/dependency-injection-strategies/#di-scope-management">🚀 See Full Deep Dive</a>


---

<div id="hilt-benefits"></div>

## What architectural advantages does Hilt provide?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">hilt</span>
  <span class="question-badge question-badge--tag">di</span>
</div>

??? question "View Answer"

    Hilt standardizes DI setup for Android component lifecycles.

    Key advantages:

    - less boilerplate than manual Dagger setup
    - predefined component hierarchy
    - easier onboarding and consistency
    - strong integration with ViewModel/WorkManager


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/hilt-in-production/#hilt-benefits">🚀 See Full Deep Dive</a>


---

<div id="hilt-component-lifetimes"></div>

## What Hilt component lifetimes should senior engineers know?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">hilt</span>
  <span class="question-badge question-badge--tag">lifecycle</span>
</div>

??? question "View Answer"

    Senior interviews expect understanding of scope boundaries.

    Common lifetimes:

    - SingletonComponent: app-wide
    - ActivityRetainedComponent: across config changes
    - ViewModelComponent: ViewModel lifetime
    - Activity/Fragment components: UI-bound

    Wrong scope choices create subtle bugs.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/hilt-in-production/#hilt-component-lifetimes">🚀 See Full Deep Dive</a>


---

<div id="dagger-vs-hilt"></div>

## Dagger vs Hilt - what is the architectural tradeoff?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">dagger</span>
  <span class="question-badge question-badge--tag">hilt</span>
</div>

??? question "View Answer"

    Hilt is Dagger with Android-focused conventions and generated glue code.

    Tradeoff framing:

    - Hilt: faster setup, consistent patterns
    - raw Dagger: maximum graph/control flexibility

    Choose based on customization needs and team productivity.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/dagger-and-component-graph/#dagger-vs-hilt">🚀 See Full Deep Dive</a>


---

<div id="dagger-component-subcomponent"></div>

## What should you understand about Dagger components and subcomponents?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">dagger</span>
  <span class="question-badge question-badge--tag">di</span>
</div>

??? question "View Answer"

    Components define object graph roots; subcomponents model child lifecycles.

    Important points:

    - parent can provide bindings to child
    - child can narrow scope/lifetime
    - graph shape affects compilation and maintainability

    Avoid overly complex graph hierarchies.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/dagger-and-component-graph/#dagger-component-subcomponent">🚀 See Full Deep Dive</a>


---

<div id="dagger-performance-tradeoffs"></div>

## What are Dagger/Hilt build and runtime tradeoffs at scale?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">dagger</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    DI frameworks improve structure but add compile-time and graph complexity costs.

    Staff-level concerns:

    - annotation processing build impact
    - module graph growth over time
    - debugging generated binding errors
    - balancing explicitness vs velocity


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/dagger-and-component-graph/#dagger-performance-tradeoffs">🚀 See Full Deep Dive</a>


---

<div id="service-locator-what-is"></div>

## What is a Service Locator pattern?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">service-locator</span>
  <span class="question-badge question-badge--tag">di</span>
</div>

??? question "View Answer"

    Service Locator is a registry that provides dependencies on demand.

    It can simplify small systems but often hides real dependencies.

    Interview angle:

    - quick bootstrap option
    - weaker explicitness than constructor DI
    - can reduce testability if overused


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/service-locator-and-anti-patterns/#service-locator-what-is">🚀 See Full Deep Dive</a>


---

<div id="service-locator-vs-di"></div>

## Service Locator vs DI - why does this matter in interviews?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">service-locator</span>
  <span class="question-badge question-badge--tag">di</span>
</div>

??? question "View Answer"

    DI makes dependencies explicit in constructors; Service Locator hides them at call sites.

    Consequences:

    - DI is easier to reason about and test
    - Service Locator can create implicit coupling
    - hidden runtime failures are more likely

    Prefer DI for medium/large apps.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/service-locator-and-anti-patterns/#service-locator-vs-di">🚀 See Full Deep Dive</a>


---

<div id="modularization-why"></div>

## Why modularize Android apps?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">modularization</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    Modularization separates code by ownership and change boundaries.

    Benefits:

    - faster incremental builds
    - clearer feature boundaries
    - parallel team development
    - safer refactoring and release isolation


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/modularization-strategies/#modularization-why">🚀 See Full Deep Dive</a>


---

<div id="multi-module-architecture-shapes"></div>

## What multi-module structures are common in Android?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">modularization</span>
  <span class="question-badge question-badge--tag">multi-module</span>
</div>

??? question "View Answer"

    Common structures include layered modules and feature-first modules.

    Typical options:

    - app + core + feature modules
    - domain/data/presentation split per feature
    - hybrid platform modules for shared infra

    Choose structure based on team and product complexity.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/modularization-strategies/#multi-module-architecture-shapes">🚀 See Full Deep Dive</a>


---

<div id="api-vs-implementation-modules"></div>

## How do API vs implementation module boundaries improve architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">modularization</span>
  <span class="question-badge question-badge--tag">dependencies</span>
</div>

??? question "View Answer"

    Expose only stable contracts and keep internals hidden.

    Benefits:

    - reduced coupling and accidental usage
    - clearer ownership contracts
    - better compile isolation
    - safer internal refactors

    Public surface area should stay intentionally small.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/modularization-strategies/#api-vs-implementation-modules">🚀 See Full Deep Dive</a>


---

<div id="feature-module-boundaries"></div>

## What defines a good feature module boundary?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">feature-modules</span>
  <span class="question-badge question-badge--tag">modularization</span>
</div>

??? question "View Answer"

    A good boundary aligns with user-facing capabilities and team ownership.

    Signs of healthy boundaries:

    - minimal cross-feature dependencies
    - explicit navigation/contracts
    - isolated tests and release paths
    - clear domain language per feature


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/feature-modules-and-boundaries/#feature-module-boundaries">🚀 See Full Deep Dive</a>


---

<div id="dynamic-feature-modules-when"></div>

## When should you use dynamic feature modules?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">feature-modules</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    Use dynamic delivery when features are optional, heavy, or region-specific.

    Tradeoffs:

    - better install size/startup profile
    - added delivery/testing complexity
    - more runtime handling for missing modules

    Evaluate product value against operational cost.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/feature-modules-and-boundaries/#dynamic-feature-modules-when">🚀 See Full Deep Dive</a>


---

<div id="dependency-direction-between-modules"></div>

## How should dependency direction work between feature modules?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">modularization</span>
  <span class="question-badge question-badge--tag">dependency-inversion</span>
</div>

??? question "View Answer"

    Features should depend on shared contracts, not each other's internals.

    Recommended pattern:

    - keep cross-feature APIs contract-driven
    - avoid cyclic feature dependencies
    - place shared infra in core/platform modules

    This preserves build and team independence.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/feature-modules-and-boundaries/#dependency-direction-between-modules">🚀 See Full Deep Dive</a>


---

<div id="state-management-android-architecture"></div>

## What is a strong state management approach in Android architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">state</span>
  <span class="question-badge question-badge--tag">ui</span>
</div>

??? question "View Answer"

    Keep state ownership explicit and state models immutable where possible.

    Common approach:

    - ViewModel owns screen state
    - UI renders state + emits events
    - repository/domain updates source state

    Avoid scattered mutable flags across layers.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/state-management-and-ssot/#state-management-android-architecture">🚀 See Full Deep Dive</a>


---

<div id="single-source-of-truth"></div>

## What does Single Source of Truth mean in practice?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">state</span>
  <span class="question-badge question-badge--tag">repository</span>
</div>

??? question "View Answer"

    One authoritative state source should drive reads for a given data set.

    In practice:

    - define canonical owner (often DB-backed)
    - route all writes through controlled paths
    - keep projections/derived views read-only

    This reduces inconsistency and race conditions.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/state-management-and-ssot/#single-source-of-truth">🚀 See Full Deep Dive</a>


---

<div id="immutable-ui-state-models"></div>

## Why model UI state as immutable data classes?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">state</span>
  <span class="question-badge question-badge--tag">testability</span>
</div>

??? question "View Answer"

    Immutable state makes transitions explicit and easier to test.

    Benefits:

    - predictable rendering behavior
    - simpler equality/change reasoning
    - safer concurrent/reactive usage
    - clearer reducer-style updates


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/state-management-and-ssot/#immutable-ui-state-models">🚀 See Full Deep Dive</a>


---

<div id="offline-first-principles"></div>

## What is offline-first architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">offline-first</span>
  <span class="question-badge question-badge--tag">data</span>
</div>

??? question "View Answer"

    Offline-first treats local storage as primary read path,
    syncing with network opportunistically.

    Core principles:

    - local-first reads
    - resilient queued writes
    - explicit conflict policy
    - sync observability/telemetry


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/offline-first-and-sync/#offline-first-principles">🚀 See Full Deep Dive</a>


---

<div id="sync-strategies-pull-push"></div>

## Push, pull, and hybrid sync strategies - when to use each?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">sync</span>
  <span class="question-badge question-badge--tag">offline-first</span>
</div>

??? question "View Answer"

    Choose strategy by freshness needs, battery budget, and backend capability.

    Quick framing:

    - pull: simple, periodic consistency
    - push: lower latency updates
    - hybrid: practical balance for many products

    Design for retries and backoff from day one.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/offline-first-and-sync/#sync-strategies-pull-push">🚀 See Full Deep Dive</a>


---

<div id="conflict-resolution-sync"></div>

## How should architecture handle sync conflicts?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">sync</span>
  <span class="question-badge question-badge--tag">data-consistency</span>
</div>

??? question "View Answer"

    Conflict policy must be explicit and domain-aware.

    Common strategies:

    - last write wins (simple, risky)
    - version/vector based merge
    - server-authoritative with client reconciliation
    - user-assisted conflict resolution for critical entities

    Track conflict metrics to tune policy.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/offline-first-and-sync/#conflict-resolution-sync">🚀 See Full Deep Dive</a>


---

<div id="caching-strategies"></div>

## What caching strategies are common in Android architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">caching</span>
  <span class="question-badge question-badge--tag">data</span>
</div>

??? question "View Answer"

    Choose cache strategy per data volatility and UX expectations.

    Common options:

    - memory cache for hot short-lived reads
    - disk/DB cache for persistence
    - TTL or staleness-based refresh
    - cache-aside or network-bound-resource style


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/caching-and-pagination-architecture/#caching-strategies">🚀 See Full Deep Dive</a>


---

<div id="pagination-architecture"></div>

## What does a robust pagination architecture look like?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">pagination</span>
  <span class="question-badge question-badge--tag">data</span>
</div>

??? question "View Answer"

    Robust pagination handles loading state, errors, deduplication, and persistence.

    Must-have concerns:

    - stable page keys/cursors
    - append/prepend retry behavior
    - local cache coherence
    - refresh invalidation strategy


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/caching-and-pagination-architecture/#pagination-architecture">🚀 See Full Deep Dive</a>


---

<div id="stateflow-architecture"></div>

## How does StateFlow fit Android architecture design?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">stateflow</span>
  <span class="question-badge question-badge--tag">reactive</span>
</div>

??? question "View Answer"

    `StateFlow` is a lifecycle-friendly state stream for UI layers.

    Architectural usage:

    - ViewModel exposes immutable `StateFlow<UiState>`
    - UI collects and renders
    - updates come from repository/use-case pipelines

    Keep one-off events separate from persistent state.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/reactive-architecture-with-flows/#stateflow-architecture">🚀 See Full Deep Dive</a>


---

<div id="event-handling-one-off-events"></div>

## How should one-off events be handled in reactive architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">events</span>
  <span class="question-badge question-badge--tag">reactive</span>
</div>

??? question "View Answer"

    Model state and events as different channels.

    Typical pattern:

    - `StateFlow` for persistent UI state
    - `SharedFlow`/Channel for one-time events
    - consume events with lifecycle awareness

    Avoid encoding transient events as sticky state flags.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/reactive-architecture-with-flows/#event-handling-one-off-events">🚀 See Full Deep Dive</a>


---

<div id="error-handling-architecture"></div>

## What is a good error handling architecture for Android apps?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">error-handling</span>
  <span class="question-badge question-badge--tag">resilience</span>
</div>

??? question "View Answer"

    Handle errors by layer and map them to domain/UI semantics.

    Recommended approach:

    - classify technical vs business errors
    - normalize in repository/domain boundaries
    - expose user-actionable UI states
    - log structured diagnostics for operations


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/ui-state-and-event-modeling/#error-handling-architecture">🚀 See Full Deep Dive</a>


---

<div id="retry-strategies-architecture"></div>

## How do retry strategies fit architecture decisions?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">retry</span>
  <span class="question-badge question-badge--tag">resilience</span>
</div>

??? question "View Answer"

    Retry policy should be explicit, bounded, and context-aware.

    Common rules:

    - exponential backoff for transient failures
    - idempotency awareness for writes
    - user-driven retry for recoverable UI actions
    - circuit-breaker style guardrails for unstable backends


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/ui-state-and-event-modeling/#retry-strategies-architecture">🚀 See Full Deep Dive</a>


---

<div id="ui-state-modeling-architecture"></div>

## How should complex UI state be modeled architecturally?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">ui-state</span>
  <span class="question-badge question-badge--tag">state</span>
</div>

??? question "View Answer"

    Use explicit immutable state models with clear sub-states.

    Common shape:

    - loading/content/error/empty branches
    - data payload + UI metadata
    - separate ephemeral events

    Prefer readability and deterministic transitions over cleverness.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/ui-state-and-event-modeling/#ui-state-modeling-architecture">🚀 See Full Deep Dive</a>


---

<div id="navigation-architecture"></div>

## What are key principles of navigation architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">navigation</span>
  <span class="question-badge question-badge--tag">modularization</span>
</div>

??? question "View Answer"

    Navigation should use explicit destination contracts and clear ownership.

    Good practices:

    - central route definitions
    - pass IDs/contracts, not large mutable objects
    - keep navigation decisions near state owner
    - test back stack behavior for critical flows


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/navigation-and-deep-link-architecture/#navigation-architecture">🚀 See Full Deep Dive</a>


---

<div id="deep-link-architecture"></div>

## How should deep links be designed in modular Android apps?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">deep-links</span>
  <span class="question-badge question-badge--tag">navigation</span>
</div>

??? question "View Answer"

    Treat deep links as stable external API contracts.

    Architecture implications:

    - central validation and parsing
    - module-level routing boundaries
    - auth/feature-flag gating support
    - backward compatibility strategy


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/navigation-and-deep-link-architecture/#deep-link-architecture">🚀 See Full Deep Dive</a>


---

<div id="architecture-testability"></div>

## How do you design Android architecture for high testability?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">testability</span>
</div>

??? question "View Answer"

    Testability improves when dependencies and state transitions are explicit.

    Design choices:

    - constructor-injected abstractions
    - pure use-case logic where possible
    - deterministic state reducers
    - contract tests at module boundaries


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/testing-architecture-and-testability/#architecture-testability">🚀 See Full Deep Dive</a>


---

<div id="scaling-architecture-for-team"></div>

## How does architecture impact team scalability?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">scalability</span>
  <span class="question-badge question-badge--tag">team</span>
</div>

??? question "View Answer"

    Architecture defines ownership boundaries, release independence, and coordination cost.

    Team-scale signals:

    - clear module ownership
    - low cross-team dependency hotspots
    - predictable integration contracts
    - standards for observability and quality gates


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/scalability-and-team-topologies/#scaling-architecture-for-team">🚀 See Full Deep Dive</a>


---

<div id="architecture-governance"></div>

## What is architecture governance in large Android codebases?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">governance</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    Governance is how teams enforce architectural direction without blocking delivery.

    Typical mechanisms:

    - module ownership model
    - ADRs and decision logs
    - lint/static checks for boundaries
    - review standards and architecture forums


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/production-tradeoffs-and-decision-making/#architecture-governance">🚀 See Full Deep Dive</a>


---

<div id="production-architecture-tradeoffs"></div>

## How should senior engineers discuss architecture tradeoffs in interviews?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">tradeoffs</span>
  <span class="question-badge question-badge--tag">senior</span>
</div>

??? question "View Answer"

    Frame tradeoffs by context, constraints, and measurable outcomes.

    Strong answer structure:

    - what problem and constraints existed
    - options considered
    - decision and rationale
    - risks/mitigations
    - follow-up metrics and iteration

    Avoid presenting architecture as one-size-fits-all.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/architecture/production-tradeoffs-and-decision-making/#production-architecture-tradeoffs">🚀 See Full Deep Dive</a>

