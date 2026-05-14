# Compose

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

<div id="compose-declarative-ui"></div>

# What makes Jetpack Compose a declarative UI toolkit?

**Difficulty:** `beginner` • **Tags:**
`compose`
`fundamentals`
`ui`

??? question "What makes Jetpack Compose a declarative UI toolkit?"

    Compose is declarative because UI is a function of state.

    You describe what UI should look like for current state,
    and Compose updates it when state changes.

    Key interview points:

    - no manual view mutation for most updates
    - composables are state-driven functions
    - runtime handles incremental UI updates
    - easier unidirectional data flow patterns


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/compose-basics-and-composable-contract/#compose-declarative-ui)


---

<div id="composable-function"></div>

# What is a composable function?

**Difficulty:** `beginner` • **Tags:**
`compose`
`composables`
`ui`

??? question "What is a composable function?"

    A composable function is a Kotlin function annotated with `@Composable`
    that emits UI into the Compose tree.

    Important details:

    - called from other composables
    - can read state and react to changes
    - should be side-effect free in the UI phase
    - participates in recomposition and skipping


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/compose-basics-and-composable-contract/#composable-function)


---

<div id="composable-lifecycle"></div>

# How should you think about composable lifecycle compared to Activity lifecycle?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`lifecycle`
`architecture`

??? question "How should you think about composable lifecycle compared to Activity lifecycle?"

    Composables do not have a lifecycle identical to Activities or Fragments.

    They can enter and leave composition many times based on state and tree changes.

    In interviews, explain:

    - composable lifetime is composition-scoped
    - effects must be tied to composition lifecycle
    - remember state is lost when node leaves composition
    - business state should live in ViewModel/domain layers


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/compose-basics-and-composable-contract/#composable-lifecycle)


---

<div id="previews-in-compose"></div>

# What are Compose previews and their limitations?

**Difficulty:** `beginner` • **Tags:**
`compose`
`tooling`
`previews`

??? question "What are Compose previews and their limitations?"

    Previews render composables in Android Studio without running full app flow.

    Useful for quick UI iteration and visual validation.

    Limitations to mention:

    - limited runtime environment
    - navigation and dependency graphs may need fakes
    - async side effects can behave differently
    - not a replacement for UI tests


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/compose-basics-and-composable-contract/#previews-in-compose)


---

<div id="mutable-state-in-compose"></div>

# What is `MutableState` in Compose?

**Difficulty:** `beginner` • **Tags:**
`compose`
`state`
`runtime`

??? question "What is `MutableState` in Compose?"

    `MutableState<T>` is an observable state holder integrated with Compose snapshots.

    When `value` changes, composables that read it become eligible for recomposition.

    Typical usage:

    - `var text by remember { mutableStateOf("") }`
    - local UI state in composables
    - immutable state models for larger screens
    - avoid mutating nested mutable objects without state wrappers


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/state-and-remember/#mutable-state-in-compose)


---

<div id="remember-vs-rememberSaveable"></div>

# What is the difference between `remember` and `rememberSaveable`?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`state`
`configuration`

??? question "What is the difference between `remember` and `rememberSaveable`?"

    `remember` keeps state across recompositions while the composable stays in composition.

    `rememberSaveable` also survives Activity recreation using saved instance state.

    Interview-ready distinction:

    - `remember`: transient UI memory only
    - `rememberSaveable`: survives rotation/process recreation scenarios
    - `rememberSaveable` needs savable types or custom Saver
    - long-lived/business state still belongs in ViewModel


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/state-and-remember/#remember-vs-rememberSaveable)


---

<div id="remember-key-parameter"></div>

# Why do keys matter in `remember`?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`remember`
`recomposition`

??? question "Why do keys matter in `remember`?"

    Keys control when remembered value should be recreated.

    If keys change, Compose discards old remembered value and computes a new one.

    Practical points:

    - use stable identity inputs as keys
    - missing keys can keep stale state
    - over-changing keys can cause unnecessary resets
    - same concept appears in list item keys


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/state-and-remember/#remember-key-parameter)


---

<div id="state-hoisting"></div>

# What is state hoisting in Compose?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`state`
`architecture`

??? question "What is state hoisting in Compose?"

    State hoisting means moving state ownership to a higher-level composable
    and passing state + events down.

    Why it is preferred:

    - improves reusability and testability
    - keeps child composables stateless when possible
    - aligns with unidirectional data flow
    - simplifies screen-level orchestration with ViewModel


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/state-hoisting-and-udf/#state-hoisting)


---

<div id="unidirectional-data-flow-compose"></div>

# How does unidirectional data flow apply in Compose UI architecture?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`architecture`
`state`

??? question "How does unidirectional data flow apply in Compose UI architecture?"

    In UDF, state flows downward and events flow upward.

    Typical pattern:

    - ViewModel exposes immutable UI state
    - composable renders that state
    - user events are callbacks to ViewModel
    - ViewModel reduces events into new state

    This reduces hidden mutations and makes behavior predictable.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/state-hoisting-and-udf/#unidirectional-data-flow-compose)


---

<div id="ui-state-modeling-compose"></div>

# How should UI state be modeled for complex Compose screens?

**Difficulty:** `senior` • **Tags:**
`compose`
`architecture`
`state`

??? question "How should UI state be modeled for complex Compose screens?"

    Model screen state as immutable data classes with explicit sub-states
    (loading, content, error, empty).

    Interview-friendly guidance:

    - one source of truth per screen
    - keep transient one-off events separate from state
    - avoid many unrelated mutable flags
    - design state to match rendering branches


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/state-hoisting-and-udf/#ui-state-modeling-compose)


---

<div id="event-handling-compose"></div>

# What are best practices for event handling in Compose?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`architecture`
`events`

??? question "What are best practices for event handling in Compose?"

    Events should be explicit callbacks from UI to state owner.

    Good interview answer includes:

    - pass lambdas like `onRetry`, `onItemClick`
    - avoid business logic inside composables
    - map UI events to intents/actions in ViewModel
    - keep event handling idempotent when possible


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/state-hoisting-and-udf/#event-handling-compose)


---

<div id="recomposition-definition"></div>

# What is recomposition in Jetpack Compose?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`recomposition`
`runtime`

??? question "What is recomposition in Jetpack Compose?"

    Recomposition is re-execution of composable functions whose observed state changed.

    Compose tracks state reads and only re-runs affected parts of the tree.

    Key concepts to mention:

    - state read tracking
    - invalidation of composition scopes
    - selective updates instead of full redraw
    - skip optimization for unchanged inputs


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/recomposition-and-skip-optimization/#recomposition-definition)


---

<div id="what-triggers-recomposition"></div>

# What triggers recomposition?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`recomposition`
`state`

??? question "What triggers recomposition?"

    Recomposition is triggered when snapshot-observed state used by a composable changes.

    Common triggers:

    - `MutableState` value updates
    - new values emitted via collected flows
    - changed parameters from parent composable
    - structural tree changes (conditionals/lists)

    Not every state change causes full-screen recomposition.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/recomposition-and-skip-optimization/#what-triggers-recomposition)


---

<div id="smart-recomposition"></div>

# What is smart recomposition?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`recomposition`
`optimization`

??? question "What is smart recomposition?"

    Smart recomposition means Compose re-runs only invalidated scopes,
    not the entire UI tree.

    It relies on:

    - state read boundaries
    - restart groups in compiler-generated code
    - parameter change checks
    - skipping groups when inputs are stable and unchanged


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/recomposition-and-skip-optimization/#smart-recomposition)


---

<div id="skip-optimization"></div>

# What is skip optimization in Compose?

**Difficulty:** `senior` • **Tags:**
`compose`
`recomposition`
`compiler`

??? question "What is skip optimization in Compose?"

    Skip optimization lets Compose avoid re-running a composable group
    when its inputs are considered unchanged.

    Interview points:

    - depends on stability analysis and equality checks
    - unstable parameters reduce skipping opportunities
    - fewer skipped groups can increase frame cost
    - metrics/tools can reveal skip behavior


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/recomposition-and-skip-optimization/#skip-optimization)


---

<div id="unstable-parameter-recomposition"></div>

# Why do unstable parameters often cause extra recomposition?

**Difficulty:** `senior` • **Tags:**
`compose`
`stability`
`performance`

??? question "Why do unstable parameters often cause extra recomposition?"

    Unstable types are assumed to potentially change in ways Compose cannot safely infer,
    so groups become less skippable.

    Consequences:

    - more recomposition work
    - harder performance tuning
    - frequent invalidation in list-heavy screens
    - pressure on frame budget


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/recomposition-and-skip-optimization/#unstable-parameter-recomposition)


---

<div id="prevent-unnecessary-recomposition"></div>

# How do you reduce unnecessary recomposition in production apps?

**Difficulty:** `senior` • **Tags:**
`compose`
`recomposition`
`performance`

??? question "How do you reduce unnecessary recomposition in production apps?"

    Reduce recomposition by improving state boundaries and input stability.

    Practical tactics:

    - hoist and split state by UI responsibility
    - pass stable, minimal parameters
    - use `derivedStateOf` for derived expensive values
    - provide keys in lazy lists
    - profile with layout inspector and tracing


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/recomposition-and-skip-optimization/#prevent-unnecessary-recomposition)


---

<div id="snapshot-system"></div>

# What is the Compose snapshot system?

**Difficulty:** `senior` • **Tags:**
`compose`
`snapshot`
`runtime`

??? question "What is the Compose snapshot system?"

    Snapshots are Compose runtime's state consistency mechanism.

    They track reads/writes to observable state and coordinate safe updates
    with recomposition.

    Interview highlights:

    - MVCC-like model for state access
    - change application invalidates readers
    - enables thread-safe state transactions with rules
    - foundation for automatic UI reactivity


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/snapshot-system-and-observation/#snapshot-system)


---

<div id="snapshot-state-read-write"></div>

# How are state reads and writes observed by Compose runtime?

**Difficulty:** `senior` • **Tags:**
`compose`
`snapshot`
`recomposition`

??? question "How are state reads and writes observed by Compose runtime?"

    During composition, runtime records state reads per scope.

    Later, writes to those state objects invalidate dependent scopes
    and schedule recomposition.

    This model provides:

    - precise dependency tracking
    - selective invalidation
    - deterministic update behavior
    - better performance than coarse full-tree updates


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/snapshot-system-and-observation/#snapshot-state-read-write)


---

<div id="side-effects-overview"></div>

# Why does Compose provide side-effect APIs?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`side-effects`
`runtime`

??? question "Why does Compose provide side-effect APIs?"

    Composables should describe UI, but apps still need imperative work
    (coroutines, listeners, analytics, cleanup).

    Side-effect APIs provide lifecycle-aware hooks for that work.

    Mention in interviews:

    - choose API by lifecycle and restart behavior
    - avoid launching side effects directly in composable body
    - keep effects scoped and cancelable


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/side-effects-overview/#side-effects-overview)


---

<div id="sideeffect-usage"></div>

# When should `SideEffect` be used?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`side-effects`
`runtime`

??? question "When should `SideEffect` be used?"

    `SideEffect` runs after every successful recomposition commit.

    Use it to publish Compose state to non-Compose objects that need
    latest values on each commit.

    Guardrails:

    - keep work fast and idempotent
    - avoid long-running jobs in `SideEffect`
    - prefer `LaunchedEffect` for suspend work


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/side-effects-overview/#sideeffect-usage)


---

<div id="produceState-usage"></div>

# What problem does `produceState` solve?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`state`
`side-effects`

??? question "What problem does `produceState` solve?"

    `produceState` bridges external async sources into Compose `State<T>`.

    It launches a coroutine tied to composition and updates `value`.

    Useful for:

    - repository/data source integration
    - converting callbacks or suspend fetches to UI state
    - lifecycle-scoped loading without manual job wiring


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/side-effects-overview/#produceState-usage)


---

<div id="launchedeffect-usage"></div>

# How does `LaunchedEffect` work and when should you use it?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`side-effects`
`coroutines`

??? question "How does `LaunchedEffect` work and when should you use it?"

    `LaunchedEffect(keys...)` starts a coroutine when entering composition,
    and restarts it when keys change.

    Use it for composition-scoped suspend work.

    Interview points:

    - cancellation on leaving composition
    - key changes restart effect
    - good for one-off screen tasks and collectors
    - avoid using unstable/changing keys unintentionally


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/effects-coroutines-and-lifecycle/#launchedeffect-usage)


---

<div id="disposableeffect-usage"></div>

# When do you use `DisposableEffect`?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`side-effects`
`lifecycle`

??? question "When do you use `DisposableEffect`?"

    `DisposableEffect(keys...)` is for registering something that needs cleanup,
    such as listeners or observers.

    It provides `onDispose` for deterministic teardown.

    Common interview examples:

    - register/unregister lifecycle observer
    - subscribe/unsubscribe callback APIs
    - resource attach/detach tied to composition


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/effects-coroutines-and-lifecycle/#disposableeffect-usage)


---

<div id="rememberCoroutineScope-usage"></div>

# What is `rememberCoroutineScope` used for?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`coroutines`
`side-effects`

??? question "What is `rememberCoroutineScope` used for?"

    `rememberCoroutineScope` returns a composition-aware `CoroutineScope`
    you can use from callbacks like button clicks.

    Difference from `LaunchedEffect`:

    - `LaunchedEffect`: automatic launch during composition
    - `rememberCoroutineScope`: manual launch on events
    - both cancel when leaving composition
    - still keep business logic in ViewModel when appropriate


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/effects-coroutines-and-lifecycle/#rememberCoroutineScope-usage)


---

<div id="derivedStateOf-purpose"></div>

# What is `derivedStateOf` and when does it help?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`state`
`performance`

??? question "What is `derivedStateOf` and when does it help?"

    `derivedStateOf` memoizes derived values from other state objects
    and recalculates only when dependencies change.

    It helps when:

    - derivation is non-trivial
    - source state updates frequently
    - you want to reduce unnecessary downstream recomposition
    - computed value is consumed by multiple UI branches


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/derived-state-and-remember-updated-state/#derivedStateOf-purpose)


---

<div id="rememberUpdatedState-purpose"></div>

# Why is `rememberUpdatedState` important in long-lived effects?

**Difficulty:** `senior` • **Tags:**
`compose`
`side-effects`
`state`

??? question "Why is `rememberUpdatedState` important in long-lived effects?"

    `rememberUpdatedState` gives effects access to the latest lambda/value
    without restarting the effect.

    This is useful when restart would be expensive or semantically wrong.

    Typical use case:

    - timer/listener effect keeps running
    - callback reference updates on recomposition
    - effect reads latest callback safely


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/derived-state-and-remember-updated-state/#rememberUpdatedState-purpose)


---

<div id="compositionlocal-purpose"></div>

# What is `CompositionLocal` and when should it be used?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`architecture`
`compositionlocal`

??? question "What is `CompositionLocal` and when should it be used?"

    `CompositionLocal` passes values implicitly down the composition tree
    without threading parameters through each layer.

    Best for cross-cutting concerns like theme, density, or environment values.

    Cautions:

    - avoid hiding business dependencies
    - document provided locals clearly
    - overuse can hurt readability and testability


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/compositionlocal-and-context-propagation/#compositionlocal-purpose)


---

<div id="stateflow-with-compose"></div>

# How do you integrate `StateFlow` with Compose UI?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`stateflow`
`architecture`

??? question "How do you integrate `StateFlow` with Compose UI?"

    Expose UI state from ViewModel as `StateFlow<UiState>` and collect in UI.

    Compose side typically uses lifecycle-aware collection API.

    Interview points:

    - single source of truth in ViewModel
    - immutable state objects
    - Compose observes and renders latest state
    - events flow back via callbacks


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/flow-integration-with-compose/#stateflow-with-compose)


---

<div id="collectAsState-vs-collectAsStateWithLifecycle"></div>

# `collectAsState` vs `collectAsStateWithLifecycle` - what is the difference?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`stateflow`
`lifecycle`

??? question "`collectAsState` vs `collectAsStateWithLifecycle` - what is the difference?"

    Both convert Flow emissions to Compose `State`.

    `collectAsStateWithLifecycle` adds Android lifecycle awareness,
    reducing unnecessary collection when UI is not active.

    Interview framing:

    - prefer lifecycle-aware API on Android screens
    - plain `collectAsState` is fine in non-lifecycle contexts
    - prevents background collection leaks/waste


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/flow-integration-with-compose/#collectAsState-vs-collectAsStateWithLifecycle)


---

<div id="snapshotFlow-usage"></div>

# What is `snapshotFlow` and when would you use it?

**Difficulty:** `senior` • **Tags:**
`compose`
`flow`
`snapshot`

??? question "What is `snapshotFlow` and when would you use it?"

    `snapshotFlow` converts reads of Compose snapshot state into a cold Flow.

    It is useful when coroutine/Flow pipelines need Compose state changes.

    Good examples:

    - track scroll thresholds
    - debounce UI-derived signals
    - bridge Compose state to repository/analytics layers


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/flow-integration-with-compose/#snapshotFlow-usage)


---

<div id="stability-in-compose"></div>

# What does stability mean in Compose?

**Difficulty:** `senior` • **Tags:**
`compose`
`stability`
`compiler`

??? question "What does stability mean in Compose?"

    Stability describes whether a type can be reliably checked for meaningful change
    to support skipping recomposition.

    Stable inputs improve skippability and runtime efficiency.

    Interview signals:

    - inferred by compiler + annotations
    - immutable data patterns help
    - mutable public properties often hurt stability


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/stability-and-compose-compiler/#stability-in-compose)


---

<div id="stable-vs-immutable"></div>

# What is the difference between `@Stable` and `@Immutable`?

**Difficulty:** `senior` • **Tags:**
`compose`
`stability`
`annotations`

??? question "What is the difference between `@Stable` and `@Immutable`?"

    `@Immutable` indicates object state does not change after construction.

    `@Stable` indicates changes are observable and equality semantics are reliable
    for Compose optimization.

    Interview caveat:

    - annotations are contracts, not magic performance buttons
    - misuse can lead to stale UI or incorrect assumptions


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/stability-and-compose-compiler/#stable-vs-immutable)


---

<div id="compose-compiler-role"></div>

# What is the role of the Compose compiler?

**Difficulty:** `senior` • **Tags:**
`compose`
`compiler`
`runtime`

??? question "What is the role of the Compose compiler?"

    The Compose compiler transforms composable code into runtime calls
    that manage composition, recomposition, and skipping.

    Key outcomes:

    - inserts restart/skip groups
    - adds change-tracking parameters
    - performs stability-driven optimizations
    - enables tooling metrics for analysis


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/stability-and-compose-compiler/#compose-compiler-role)


---

<div id="slot-table-purpose"></div>

# What is the Slot Table in Compose runtime?

**Difficulty:** `staff` • **Tags:**
`compose`
`runtime`
`slot-table`

??? question "What is the Slot Table in Compose runtime?"

    Slot Table is the runtime data structure that stores composition groups,
    remembered values, and positional metadata.

    It enables efficient tree updates without rebuilding everything.

    Interview highlights:

    - positional memoization model
    - group identity and structure tracking
    - powers `remember` and node reuse behavior


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/slot-table-and-runtime-internals/#slot-table-purpose)


---

<div id="composer-and-applier"></div>

# What are `Composer` and `Applier` in Compose internals?

**Difficulty:** `staff` • **Tags:**
`compose`
`internals`
`runtime`

??? question "What are `Composer` and `Applier` in Compose internals?"

    `Composer` records and reconciles composition operations.
    `Applier` applies resulting tree changes to target UI tree implementation.

    In Android UI:

    - `Composer` decides what changed
    - `Applier` performs node insert/move/remove updates
    - separation supports different tree backends


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/composer-applier-and-runtime-phases/#composer-and-applier)


---

<div id="compose-runtime-phases"></div>

# What are the major runtime phases in Compose frame updates?

**Difficulty:** `senior` • **Tags:**
`compose`
`runtime`
`rendering`

??? question "What are the major runtime phases in Compose frame updates?"

    Compose update pipeline can be framed as:

    - composition (compute UI structure)
    - layout (measure/place)
    - drawing (render to canvas)

    Recomposition affects composition, but layout/draw can run independently
    when only size/visual invalidations occur.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/composer-applier-and-runtime-phases/#compose-runtime-phases)


---

<div id="modifier-chain-order"></div>

# Why does modifier order matter in Compose?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`modifier`
`ui`

??? question "Why does modifier order matter in Compose?"

    Modifiers are applied in sequence, and each step wraps or transforms behavior.

    Reordering can change:

    - layout size constraints
    - drawing/clipping outcome
    - pointer input hit areas
    - semantics/accessibility output

    Explain with simple examples like `padding` before vs after `clickable`.


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/modifier-chain-and-node-graph/#modifier-chain-order)


---

<div id="custom-layout-basics"></div>

# What should you know before writing custom layouts in Compose?

**Difficulty:** `senior` • **Tags:**
`compose`
`layout`
`performance`

??? question "What should you know before writing custom layouts in Compose?"

    Understand constraints-driven measurement and explicit placement APIs.

    Core interview points:

    - measure children with provided constraints
    - place children in layout block
    - avoid repeated expensive measurement work
    - preserve predictable intrinsic sizing behavior


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/layout-measure-draw-pipeline/#custom-layout-basics)


---

<div id="measure-layout-draw-phases"></div>

# Explain measure, layout, and draw phases in Compose.

**Difficulty:** `intermediate` • **Tags:**
`compose`
`layout`
`rendering`

??? question "Explain measure, layout, and draw phases in Compose."

    Measure determines child sizes under constraints.
    Layout places children in parent coordinates.
    Draw renders pixels based on final layout tree.

    Important interview note:

    - not every state change forces all three phases equally
    - phase-specific invalidations are key for performance


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/layout-measure-draw-pipeline/#measure-layout-draw-phases)


---

<div id="lazycolumn-performance"></div>

# How do you optimize `LazyColumn` performance?

**Difficulty:** `senior` • **Tags:**
`compose`
`lazycolumn`
`performance`

??? question "How do you optimize `LazyColumn` performance?"

    Optimize item stability, keys, and per-item work.

    Practical checklist:

    - provide stable item keys
    - avoid heavy allocations in item content
    - keep item state scoped correctly
    - minimize nested lazy containers
    - profile jank with real datasets


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/lazy-layouts-and-list-performance/#lazycolumn-performance)


---

<div id="keys-in-lazycolumn"></div>

# Why are keys important in `LazyColumn` items?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`lazycolumn`
`state`

??? question "Why are keys important in `LazyColumn` items?"

    Keys preserve item identity across insertions, deletions, and moves.

    Without stable keys:

    - item state can jump to wrong rows
    - animations and reuse become less predictable
    - recomposition work can increase
    - scroll position behavior may degrade


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/lazy-layouts-and-list-performance/#keys-in-lazycolumn)


---

<div id="navigation-compose-basics"></div>

# What are core principles of navigation in Compose?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`navigation`
`architecture`

??? question "What are core principles of navigation in Compose?"

    Use a route graph with explicit destinations and argument contracts.

    Strong interview answer includes:

    - single `NavHost` per feature shell/app shell
    - pass IDs, not large objects
    - keep navigation decisions near state owner
    - support deep links and back stack predictability


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/navigation-in-compose/#navigation-compose-basics)


---

<div id="navigation-single-source-of-truth"></div>

# How do you keep navigation maintainable at scale in Compose apps?

**Difficulty:** `senior` • **Tags:**
`compose`
`navigation`
`architecture`

??? question "How do you keep navigation maintainable at scale in Compose apps?"

    Treat destinations as typed contracts and centralize route definitions.

    Maintainability practices:

    - sealed route models or typed destinations
    - feature-level navigation modules
    - avoid scattering route strings
    - make back stack and result passing explicit


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/navigation-in-compose/#navigation-single-source-of-truth)


---

<div id="theming-material3-compose"></div>

# How does theming work in Compose with Material 3?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`theming`
`material3`

??? question "How does theming work in Compose with Material 3?"

    Material theme is provided via composition locals (color scheme,
    typography, shapes) and consumed by Material components.

    Interview points:

    - app-level theme as design system boundary
    - support light/dark and dynamic color strategy
    - keep custom tokens consistent with brand system
    - avoid hardcoded colors in feature UI


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/theming-and-material3/#theming-material3-compose)


---

<div id="animations-compose"></div>

# What animation APIs should you discuss in Compose interviews?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`animation`
`ui`

??? question "What animation APIs should you discuss in Compose interviews?"

    Focus on choosing API by use case complexity.

    Common set:

    - `animate*AsState` for simple value transitions
    - `AnimatedVisibility` and `AnimatedContent` for content transitions
    - `updateTransition` for coordinated multi-property animations
    - infinite/repeatable animations for decorative motion


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/animation-in-compose/#animations-compose)


---

<div id="compose-testing-strategy"></div>

# What is a strong testing strategy for Compose UI?

**Difficulty:** `senior` • **Tags:**
`compose`
`testing`
`architecture`

??? question "What is a strong testing strategy for Compose UI?"

    Use a testing pyramid: state logic tests, composable behavior tests,
    and targeted integration/end-to-end flows.

    Interview-ready points:

    - verify semantics, not implementation details
    - inject fake state/data for deterministic tests
    - isolate flaky async behavior with test dispatchers
    - keep UI tests focused on high-value user journeys


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/testing-interop-and-performance/#compose-testing-strategy)


---

<div id="semantics-and-test-tags"></div>

# How do semantics and test tags help Compose testing?

**Difficulty:** `intermediate` • **Tags:**
`compose`
`testing`
`semantics`

??? question "How do semantics and test tags help Compose testing?"

    Compose tests query semantics tree, not view IDs.

    `Modifier.testTag()` and semantic properties provide stable selectors.

    Best practices:

    - prefer meaningful semantics for accessibility + tests
    - avoid brittle text-only selectors when dynamic
    - keep tags unique within test scope


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/testing-interop-and-performance/#semantics-and-test-tags)


---

<div id="androidview-interop"></div>

# When and how should you use `AndroidView` interop?

**Difficulty:** `senior` • **Tags:**
`compose`
`interoperability`
`views`

??? question "When and how should you use `AndroidView` interop?"

    `AndroidView` embeds legacy View-based UI inside Compose.

    Use it for incremental migration or SDK widgets not available in Compose.

    Interview cautions:

    - manage View lifecycle and state sync carefully
    - avoid frequent View recreation
    - keep interop boundaries explicit and temporary when possible


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/testing-interop-and-performance/#androidview-interop)


---

<div id="compose-performance-checklist"></div>

# What is your practical Compose performance checklist?

**Difficulty:** `staff` • **Tags:**
`compose`
`performance`
`optimization`

??? question "What is your practical Compose performance checklist?"

    A strong answer balances architecture and runtime-level tuning.

    Quick checklist:

    - stabilize data models and parameters
    - reduce unnecessary recomposition scopes
    - optimize lazy list item content and keys
    - move heavy work off main thread
    - measure with tracing, profiler, and macrobenchmark


    [🚀 See Full Deep Dive](/android-interview-prep/deep-dives/compose/testing-interop-and-performance/#compose-performance-checklist)

