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

# What is MVVM in Android architecture?

**Difficulty:** `beginner` • **Tags:**
`architecture`
`mvvm`
`android`

??? question "What is MVVM in Android architecture?"

    MVVM separates UI rendering from business/data orchestration.

    Typical split:

    - View: renders state and forwards user actions
    - ViewModel: exposes lifecycle-aware UI state
    - Repository: abstracts data access

    Why teams use it:

    - better testability
    - cleaner separation of concerns
    - easier lifecycle-safe state handling


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/mvvm-and-viewmodel/#mvvm-basics)


---

<div id="viewmodel-role"></div>

# What is the role of a ViewModel in scalable Android apps?

**Difficulty:** `beginner` • **Tags:**
`architecture`
`viewmodel`
`state`

??? question "What is the role of a ViewModel in scalable Android apps?"

    ViewModel owns screen-level state and survives configuration changes.

    Key responsibilities:

    - transform domain data into UI-friendly state
    - coordinate use cases/repositories
    - expose immutable observable state
    - handle user intents/events

    It should avoid direct Android UI references.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/mvvm-and-viewmodel/#viewmodel-role)


---

<div id="savedstatehandle-usage"></div>

# When should you use SavedStateHandle in architecture design?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`viewmodel`
`state`

??? question "When should you use SavedStateHandle in architecture design?"

    Use `SavedStateHandle` for small, restorable screen state
    tied to process recreation.

    Good candidates:

    - selected tab/index
    - filter/sort selection
    - lightweight form progress

    Avoid storing large objects or domain caches in it.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/mvvm-and-viewmodel/#savedstatehandle-usage)


---

<div id="mvi-what-is"></div>

# What is MVI architecture?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`mvi`
`state`

??? question "What is MVI architecture?"

    MVI models UI as a loop: intent -> reducer -> new immutable state.

    Core benefits:

    - predictable state transitions
    - easier debugging/time-travel style reasoning
    - explicit event handling contract

    Tradeoff: can introduce boilerplate if over-applied.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/mvi-and-udf/#mvi-what-is)


---

<div id="mvi-vs-mvvm"></div>

# MVVM vs MVI - how do you choose?

**Difficulty:** `senior` • **Tags:**
`architecture`
`mvvm`
`mvi`

??? question "MVVM vs MVI - how do you choose?"

    Choose by complexity and team needs, not trend preference.

    MVVM:

    - lower ceremony
    - common Android default

    MVI:

    - stronger state/event determinism
    - better for complex interaction-heavy screens

    Many teams use MVVM + UDF patterns as a middle ground.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/mvi-and-udf/#mvi-vs-mvvm)


---

<div id="udf-principles"></div>

# What are the key principles of Unidirectional Data Flow?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`udf`
`state`

??? question "What are the key principles of Unidirectional Data Flow?"

    UDF means state flows down, events flow up.

    Interview-ready points:

    - single source of truth for screen state
    - immutable state exposure
    - explicit intent/event handlers
    - deterministic state transitions

    This reduces hidden mutation bugs.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/mvi-and-udf/#udf-principles)


---

<div id="clean-architecture-overview"></div>

# What is Clean Architecture in Android?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`clean-architecture`
`layers`

??? question "What is Clean Architecture in Android?"

    Clean Architecture organizes code by responsibility and dependency direction.

    Typical layers:

    - presentation
    - domain
    - data

    Main rule: inner layers should not depend on outer framework details.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/clean-architecture-layering/#clean-architecture-overview)


---

<div id="layer-dependency-rule"></div>

# What is the dependency rule in layered architecture?

**Difficulty:** `senior` • **Tags:**
`architecture`
`clean-architecture`
`dependency-inversion`

??? question "What is the dependency rule in layered architecture?"

    Dependencies must point inward toward stable policy layers.

    Practical implications:

    - UI depends on domain contracts
    - data implements domain abstractions
    - domain avoids Android/framework types

    This improves portability and test isolation.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/clean-architecture-layering/#layer-dependency-rule)


---

<div id="dependency-inversion-android"></div>

# How does dependency inversion apply to Android app architecture?

**Difficulty:** `senior` • **Tags:**
`architecture`
`solid`
`dependency-inversion`

??? question "How does dependency inversion apply to Android app architecture?"

    High-level policies should depend on abstractions, not concrete SDK/data details.

    In Android this usually means:

    - domain uses interfaces
    - data/network/db implement those interfaces
    - DI wires concrete implementations

    It keeps business logic resilient to infrastructure changes.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/clean-architecture-layering/#dependency-inversion-android)


---

<div id="repository-pattern-purpose"></div>

# Why use the Repository pattern?

**Difficulty:** `beginner` • **Tags:**
`architecture`
`repository`
`data`

??? question "Why use the Repository pattern?"

    Repository abstracts data origin and provides a clean API to higher layers.

    Benefits:

    - decouples UI/domain from network/db details
    - centralizes data policies
    - simplifies testing with fakes
    - enables caching/sync orchestration


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/repository-pattern-and-data-sources/#repository-pattern-purpose)


---

<div id="repository-single-source-truth"></div>

# How does a repository support a Single Source of Truth model?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`repository`
`state`

??? question "How does a repository support a Single Source of Truth model?"

    Repository enforces one authoritative read path for consumers.

    Common approach:

    - local DB is canonical source
    - network refresh updates DB
    - UI observes DB-backed streams

    This avoids competing data sources in UI.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/repository-pattern-and-data-sources/#repository-single-source-truth)


---

<div id="multiple-data-sources-orchestration"></div>

# How should repositories orchestrate network, cache, and database sources?

**Difficulty:** `senior` • **Tags:**
`architecture`
`repository`
`caching`

??? question "How should repositories orchestrate network, cache, and database sources?"

    Define explicit policies for freshness, fallback, and write ordering.

    Typical strategy:

    - read local first
    - fetch remote by staleness rules
    - merge/validate payload
    - persist then emit

    Keep these rules in repository, not UI.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/repository-pattern-and-data-sources/#multiple-data-sources-orchestration)


---

<div id="use-case-purpose"></div>

# What problem do use cases solve in architecture?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`use-cases`
`domain`

??? question "What problem do use cases solve in architecture?"

    Use cases encapsulate business actions independent of UI and data frameworks.

    They help by:

    - isolating domain logic
    - improving reuse across screens
    - making behavior unit-testable
    - reducing ViewModel complexity


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/use-cases-and-domain-layer/#use-case-purpose)


---

<div id="use-case-granularity"></div>

# How granular should use cases be?

**Difficulty:** `senior` • **Tags:**
`architecture`
`use-cases`
`design`

??? question "How granular should use cases be?"

    Use cases should represent coherent business actions, not tiny wrappers.

    Guidance:

    - too coarse: hard to compose/test
    - too fine: boilerplate and indirection
    - optimize for domain clarity and change boundaries

    Granularity is a context-based design decision.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/use-cases-and-domain-layer/#use-case-granularity)


---

<div id="domain-layer-when-to-add"></div>

# When is a dedicated domain layer worth adding?

**Difficulty:** `senior` • **Tags:**
`architecture`
`domain`
`clean-architecture`

??? question "When is a dedicated domain layer worth adding?"

    Add domain layer when business rules are non-trivial or reused.

    Signals:

    - multiple features share logic
    - policies outgrow ViewModels
    - testability/portability requirements increase

    For simple apps, extra layers can be unnecessary overhead.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/use-cases-and-domain-layer/#domain-layer-when-to-add)


---

<div id="dependency-injection-what-why"></div>

# Why is dependency injection important in Android architecture?

**Difficulty:** `beginner` • **Tags:**
`architecture`
`di`
`testability`

??? question "Why is dependency injection important in Android architecture?"

    DI manages object creation/wiring outside business logic.

    Benefits:

    - loose coupling
    - easier testing with fakes/mocks
    - centralized lifecycle/scope control
    - clearer dependency graph at scale


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/dependency-injection-strategies/#dependency-injection-what-why)


---

<div id="constructor-injection-vs-field-injection"></div>

# Constructor injection vs field injection - which is preferred?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`di`
`design`

??? question "Constructor injection vs field injection - which is preferred?"

    Constructor injection is usually preferred.

    Reasons:

    - explicit required dependencies
    - easier immutable object design
    - better unit-test ergonomics

    Field injection is useful in framework-controlled classes but less explicit.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/dependency-injection-strategies/#constructor-injection-vs-field-injection)


---

<div id="di-scope-management"></div>

# How do DI scopes affect memory and lifecycle behavior?

**Difficulty:** `senior` • **Tags:**
`architecture`
`di`
`lifecycle`

??? question "How do DI scopes affect memory and lifecycle behavior?"

    Scopes define object lifetime and reuse boundaries.

    Mis-scoping can cause:

    - leaks (too long-lived)
    - churn/perf cost (too short-lived)
    - inconsistent shared state

    Align scopes with Activity/Fragment/ViewModel/app lifetimes.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/dependency-injection-strategies/#di-scope-management)


---

<div id="hilt-benefits"></div>

# What architectural advantages does Hilt provide?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`hilt`
`di`

??? question "What architectural advantages does Hilt provide?"

    Hilt standardizes DI setup for Android component lifecycles.

    Key advantages:

    - less boilerplate than manual Dagger setup
    - predefined component hierarchy
    - easier onboarding and consistency
    - strong integration with ViewModel/WorkManager


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/hilt-in-production/#hilt-benefits)


---

<div id="hilt-component-lifetimes"></div>

# What Hilt component lifetimes should senior engineers know?

**Difficulty:** `senior` • **Tags:**
`architecture`
`hilt`
`lifecycle`

??? question "What Hilt component lifetimes should senior engineers know?"

    Senior interviews expect understanding of scope boundaries.

    Common lifetimes:

    - SingletonComponent: app-wide
    - ActivityRetainedComponent: across config changes
    - ViewModelComponent: ViewModel lifetime
    - Activity/Fragment components: UI-bound

    Wrong scope choices create subtle bugs.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/hilt-in-production/#hilt-component-lifetimes)


---

<div id="dagger-vs-hilt"></div>

# Dagger vs Hilt - what is the architectural tradeoff?

**Difficulty:** `senior` • **Tags:**
`architecture`
`dagger`
`hilt`

??? question "Dagger vs Hilt - what is the architectural tradeoff?"

    Hilt is Dagger with Android-focused conventions and generated glue code.

    Tradeoff framing:

    - Hilt: faster setup, consistent patterns
    - raw Dagger: maximum graph/control flexibility

    Choose based on customization needs and team productivity.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/dagger-and-component-graph/#dagger-vs-hilt)


---

<div id="dagger-component-subcomponent"></div>

# What should you understand about Dagger components and subcomponents?

**Difficulty:** `senior` • **Tags:**
`architecture`
`dagger`
`di`

??? question "What should you understand about Dagger components and subcomponents?"

    Components define object graph roots; subcomponents model child lifecycles.

    Important points:

    - parent can provide bindings to child
    - child can narrow scope/lifetime
    - graph shape affects compilation and maintainability

    Avoid overly complex graph hierarchies.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/dagger-and-component-graph/#dagger-component-subcomponent)


---

<div id="dagger-performance-tradeoffs"></div>

# What are Dagger/Hilt build and runtime tradeoffs at scale?

**Difficulty:** `staff` • **Tags:**
`architecture`
`dagger`
`scalability`

??? question "What are Dagger/Hilt build and runtime tradeoffs at scale?"

    DI frameworks improve structure but add compile-time and graph complexity costs.

    Staff-level concerns:

    - annotation processing build impact
    - module graph growth over time
    - debugging generated binding errors
    - balancing explicitness vs velocity


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/dagger-and-component-graph/#dagger-performance-tradeoffs)


---

<div id="service-locator-what-is"></div>

# What is a Service Locator pattern?

**Difficulty:** `beginner` • **Tags:**
`architecture`
`service-locator`
`di`

??? question "What is a Service Locator pattern?"

    Service Locator is a registry that provides dependencies on demand.

    It can simplify small systems but often hides real dependencies.

    Interview angle:

    - quick bootstrap option
    - weaker explicitness than constructor DI
    - can reduce testability if overused


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/service-locator-and-anti-patterns/#service-locator-what-is)


---

<div id="service-locator-vs-di"></div>

# Service Locator vs DI - why does this matter in interviews?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`service-locator`
`di`

??? question "Service Locator vs DI - why does this matter in interviews?"

    DI makes dependencies explicit in constructors; Service Locator hides them at call sites.

    Consequences:

    - DI is easier to reason about and test
    - Service Locator can create implicit coupling
    - hidden runtime failures are more likely

    Prefer DI for medium/large apps.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/service-locator-and-anti-patterns/#service-locator-vs-di)


---

<div id="modularization-why"></div>

# Why modularize Android apps?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`modularization`
`scalability`

??? question "Why modularize Android apps?"

    Modularization separates code by ownership and change boundaries.

    Benefits:

    - faster incremental builds
    - clearer feature boundaries
    - parallel team development
    - safer refactoring and release isolation


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/modularization-strategies/#modularization-why)


---

<div id="multi-module-architecture-shapes"></div>

# What multi-module structures are common in Android?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`modularization`
`multi-module`

??? question "What multi-module structures are common in Android?"

    Common structures include layered modules and feature-first modules.

    Typical options:

    - app + core + feature modules
    - domain/data/presentation split per feature
    - hybrid platform modules for shared infra

    Choose structure based on team and product complexity.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/modularization-strategies/#multi-module-architecture-shapes)


---

<div id="api-vs-implementation-modules"></div>

# How do API vs implementation module boundaries improve architecture?

**Difficulty:** `senior` • **Tags:**
`architecture`
`modularization`
`dependencies`

??? question "How do API vs implementation module boundaries improve architecture?"

    Expose only stable contracts and keep internals hidden.

    Benefits:

    - reduced coupling and accidental usage
    - clearer ownership contracts
    - better compile isolation
    - safer internal refactors

    Public surface area should stay intentionally small.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/modularization-strategies/#api-vs-implementation-modules)


---

<div id="feature-module-boundaries"></div>

# What defines a good feature module boundary?

**Difficulty:** `senior` • **Tags:**
`architecture`
`feature-modules`
`modularization`

??? question "What defines a good feature module boundary?"

    A good boundary aligns with user-facing capabilities and team ownership.

    Signs of healthy boundaries:

    - minimal cross-feature dependencies
    - explicit navigation/contracts
    - isolated tests and release paths
    - clear domain language per feature


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/feature-modules-and-boundaries/#feature-module-boundaries)


---

<div id="dynamic-feature-modules-when"></div>

# When should you use dynamic feature modules?

**Difficulty:** `senior` • **Tags:**
`architecture`
`feature-modules`
`scalability`

??? question "When should you use dynamic feature modules?"

    Use dynamic delivery when features are optional, heavy, or region-specific.

    Tradeoffs:

    - better install size/startup profile
    - added delivery/testing complexity
    - more runtime handling for missing modules

    Evaluate product value against operational cost.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/feature-modules-and-boundaries/#dynamic-feature-modules-when)


---

<div id="dependency-direction-between-modules"></div>

# How should dependency direction work between feature modules?

**Difficulty:** `senior` • **Tags:**
`architecture`
`modularization`
`dependency-inversion`

??? question "How should dependency direction work between feature modules?"

    Features should depend on shared contracts, not each other's internals.

    Recommended pattern:

    - keep cross-feature APIs contract-driven
    - avoid cyclic feature dependencies
    - place shared infra in core/platform modules

    This preserves build and team independence.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/feature-modules-and-boundaries/#dependency-direction-between-modules)


---

<div id="state-management-android-architecture"></div>

# What is a strong state management approach in Android architecture?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`state`
`ui`

??? question "What is a strong state management approach in Android architecture?"

    Keep state ownership explicit and state models immutable where possible.

    Common approach:

    - ViewModel owns screen state
    - UI renders state + emits events
    - repository/domain updates source state

    Avoid scattered mutable flags across layers.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/state-management-and-ssot/#state-management-android-architecture)


---

<div id="single-source-of-truth"></div>

# What does Single Source of Truth mean in practice?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`state`
`repository`

??? question "What does Single Source of Truth mean in practice?"

    One authoritative state source should drive reads for a given data set.

    In practice:

    - define canonical owner (often DB-backed)
    - route all writes through controlled paths
    - keep projections/derived views read-only

    This reduces inconsistency and race conditions.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/state-management-and-ssot/#single-source-of-truth)


---

<div id="immutable-ui-state-models"></div>

# Why model UI state as immutable data classes?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`state`
`testability`

??? question "Why model UI state as immutable data classes?"

    Immutable state makes transitions explicit and easier to test.

    Benefits:

    - predictable rendering behavior
    - simpler equality/change reasoning
    - safer concurrent/reactive usage
    - clearer reducer-style updates


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/state-management-and-ssot/#immutable-ui-state-models)


---

<div id="offline-first-principles"></div>

# What is offline-first architecture?

**Difficulty:** `senior` • **Tags:**
`architecture`
`offline-first`
`data`

??? question "What is offline-first architecture?"

    Offline-first treats local storage as primary read path,
    syncing with network opportunistically.

    Core principles:

    - local-first reads
    - resilient queued writes
    - explicit conflict policy
    - sync observability/telemetry


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/offline-first-and-sync/#offline-first-principles)


---

<div id="sync-strategies-pull-push"></div>

# Push, pull, and hybrid sync strategies - when to use each?

**Difficulty:** `senior` • **Tags:**
`architecture`
`sync`
`offline-first`

??? question "Push, pull, and hybrid sync strategies - when to use each?"

    Choose strategy by freshness needs, battery budget, and backend capability.

    Quick framing:

    - pull: simple, periodic consistency
    - push: lower latency updates
    - hybrid: practical balance for many products

    Design for retries and backoff from day one.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/offline-first-and-sync/#sync-strategies-pull-push)


---

<div id="conflict-resolution-sync"></div>

# How should architecture handle sync conflicts?

**Difficulty:** `staff` • **Tags:**
`architecture`
`sync`
`data-consistency`

??? question "How should architecture handle sync conflicts?"

    Conflict policy must be explicit and domain-aware.

    Common strategies:

    - last write wins (simple, risky)
    - version/vector based merge
    - server-authoritative with client reconciliation
    - user-assisted conflict resolution for critical entities

    Track conflict metrics to tune policy.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/offline-first-and-sync/#conflict-resolution-sync)


---

<div id="caching-strategies"></div>

# What caching strategies are common in Android architecture?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`caching`
`data`

??? question "What caching strategies are common in Android architecture?"

    Choose cache strategy per data volatility and UX expectations.

    Common options:

    - memory cache for hot short-lived reads
    - disk/DB cache for persistence
    - TTL or staleness-based refresh
    - cache-aside or network-bound-resource style


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/caching-and-pagination-architecture/#caching-strategies)


---

<div id="pagination-architecture"></div>

# What does a robust pagination architecture look like?

**Difficulty:** `senior` • **Tags:**
`architecture`
`pagination`
`data`

??? question "What does a robust pagination architecture look like?"

    Robust pagination handles loading state, errors, deduplication, and persistence.

    Must-have concerns:

    - stable page keys/cursors
    - append/prepend retry behavior
    - local cache coherence
    - refresh invalidation strategy


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/caching-and-pagination-architecture/#pagination-architecture)


---

<div id="stateflow-architecture"></div>

# How does StateFlow fit Android architecture design?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`stateflow`
`reactive`

??? question "How does StateFlow fit Android architecture design?"

    `StateFlow` is a lifecycle-friendly state stream for UI layers.

    Architectural usage:

    - ViewModel exposes immutable `StateFlow<UiState>`
    - UI collects and renders
    - updates come from repository/use-case pipelines

    Keep one-off events separate from persistent state.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/reactive-architecture-with-flows/#stateflow-architecture)


---

<div id="event-handling-one-off-events"></div>

# How should one-off events be handled in reactive architecture?

**Difficulty:** `senior` • **Tags:**
`architecture`
`events`
`reactive`

??? question "How should one-off events be handled in reactive architecture?"

    Model state and events as different channels.

    Typical pattern:

    - `StateFlow` for persistent UI state
    - `SharedFlow`/Channel for one-time events
    - consume events with lifecycle awareness

    Avoid encoding transient events as sticky state flags.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/reactive-architecture-with-flows/#event-handling-one-off-events)


---

<div id="error-handling-architecture"></div>

# What is a good error handling architecture for Android apps?

**Difficulty:** `senior` • **Tags:**
`architecture`
`error-handling`
`resilience`

??? question "What is a good error handling architecture for Android apps?"

    Handle errors by layer and map them to domain/UI semantics.

    Recommended approach:

    - classify technical vs business errors
    - normalize in repository/domain boundaries
    - expose user-actionable UI states
    - log structured diagnostics for operations


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/ui-state-and-event-modeling/#error-handling-architecture)


---

<div id="retry-strategies-architecture"></div>

# How do retry strategies fit architecture decisions?

**Difficulty:** `senior` • **Tags:**
`architecture`
`retry`
`resilience`

??? question "How do retry strategies fit architecture decisions?"

    Retry policy should be explicit, bounded, and context-aware.

    Common rules:

    - exponential backoff for transient failures
    - idempotency awareness for writes
    - user-driven retry for recoverable UI actions
    - circuit-breaker style guardrails for unstable backends


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/ui-state-and-event-modeling/#retry-strategies-architecture)


---

<div id="ui-state-modeling-architecture"></div>

# How should complex UI state be modeled architecturally?

**Difficulty:** `senior` • **Tags:**
`architecture`
`ui-state`
`state`

??? question "How should complex UI state be modeled architecturally?"

    Use explicit immutable state models with clear sub-states.

    Common shape:

    - loading/content/error/empty branches
    - data payload + UI metadata
    - separate ephemeral events

    Prefer readability and deterministic transitions over cleverness.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/ui-state-and-event-modeling/#ui-state-modeling-architecture)


---

<div id="navigation-architecture"></div>

# What are key principles of navigation architecture?

**Difficulty:** `intermediate` • **Tags:**
`architecture`
`navigation`
`modularization`

??? question "What are key principles of navigation architecture?"

    Navigation should use explicit destination contracts and clear ownership.

    Good practices:

    - central route definitions
    - pass IDs/contracts, not large mutable objects
    - keep navigation decisions near state owner
    - test back stack behavior for critical flows


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/navigation-and-deep-link-architecture/#navigation-architecture)


---

<div id="deep-link-architecture"></div>

# How should deep links be designed in modular Android apps?

**Difficulty:** `senior` • **Tags:**
`architecture`
`deep-links`
`navigation`

??? question "How should deep links be designed in modular Android apps?"

    Treat deep links as stable external API contracts.

    Architecture implications:

    - central validation and parsing
    - module-level routing boundaries
    - auth/feature-flag gating support
    - backward compatibility strategy


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/navigation-and-deep-link-architecture/#deep-link-architecture)


---

<div id="architecture-testability"></div>

# How do you design Android architecture for high testability?

**Difficulty:** `senior` • **Tags:**
`architecture`
`testing`
`testability`

??? question "How do you design Android architecture for high testability?"

    Testability improves when dependencies and state transitions are explicit.

    Design choices:

    - constructor-injected abstractions
    - pure use-case logic where possible
    - deterministic state reducers
    - contract tests at module boundaries


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/testing-architecture-and-testability/#architecture-testability)


---

<div id="scaling-architecture-for-team"></div>

# How does architecture impact team scalability?

**Difficulty:** `staff` • **Tags:**
`architecture`
`scalability`
`team`

??? question "How does architecture impact team scalability?"

    Architecture defines ownership boundaries, release independence, and coordination cost.

    Team-scale signals:

    - clear module ownership
    - low cross-team dependency hotspots
    - predictable integration contracts
    - standards for observability and quality gates


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/scalability-and-team-topologies/#scaling-architecture-for-team)


---

<div id="architecture-governance"></div>

# What is architecture governance in large Android codebases?

**Difficulty:** `staff` • **Tags:**
`architecture`
`governance`
`scalability`

??? question "What is architecture governance in large Android codebases?"

    Governance is how teams enforce architectural direction without blocking delivery.

    Typical mechanisms:

    - module ownership model
    - ADRs and decision logs
    - lint/static checks for boundaries
    - review standards and architecture forums


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/production-tradeoffs-and-decision-making/#architecture-governance)


---

<div id="production-architecture-tradeoffs"></div>

# How should senior engineers discuss architecture tradeoffs in interviews?

**Difficulty:** `senior` • **Tags:**
`architecture`
`tradeoffs`
`senior`

??? question "How should senior engineers discuss architecture tradeoffs in interviews?"

    Frame tradeoffs by context, constraints, and measurable outcomes.

    Strong answer structure:

    - what problem and constraints existed
    - options considered
    - decision and rationale
    - risks/mitigations
    - follow-up metrics and iteration

    Avoid presenting architecture as one-size-fits-all.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/architecture/production-tradeoffs-and-decision-making/#production-architecture-tradeoffs)

