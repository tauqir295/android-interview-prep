---
hide:
  - toc
---

# Concurrency

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

<div id="structured-concurrency"></div>

## What is structured concurrency?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">concurrency</span>
  <span class="question-badge question-badge--tag">kotlin</span>
</div>

??? question "View Answer"

    Structured concurrency is a coroutine design principle
    where child coroutines are tied to a parent scope.

    This ensures:

    - automatic cancellation
    - lifecycle-aware execution
    - proper error propagation
    - prevention of coroutine leaks

    Core concepts:

    - CoroutineScope
    - Job hierarchy
    - parent-child relationships
    - cooperative cancellation


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-internals/#structured-concurrency">🚀 See Full Deep Dive</a>


---

<div id="suspend-functions"></div>

## What is a suspend function?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    A suspend function can suspend execution without blocking a thread.

    It can only be called from another suspend function or coroutine.

    Key points:

    - not necessarily asynchronous by itself
    - compiled into coroutine machinery
    - can resume later after suspension
    - used for non-blocking async work


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-internals/#suspend-functions">🚀 See Full Deep Dive</a>


---

<div id="continuation-and-cps"></div>

## What is a Continuation in Kotlin coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">runtime</span>
  <span class="question-badge question-badge--tag">kotlin</span>
</div>

??? question "View Answer"

    A Continuation represents the rest of a suspended computation.

    When a suspend function pauses, Kotlin stores state in a continuation
    so it can resume later from the correct point.

    Interview points:

    - coroutine state is captured in the continuation
    - used by suspend functions and builders
    - enables non-blocking suspension/resumption


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-internals/#continuation-and-cps">🚀 See Full Deep Dive</a>


---

<div id="coroutine-state-machine"></div>

## How does coroutine suspension work internally?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">compiler</span>
  <span class="question-badge question-badge--tag">internals</span>
</div>

??? question "View Answer"

    The Kotlin compiler rewrites suspend code into a resumable state machine.

    This transformation adds labels/state transitions and continuation handling
    around each suspension point.

    Why it matters:

    - explains how suspend functions resume
    - helps reason about allocation and debugging
    - is the basis for coroutine CPS transformation


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-internals/#coroutine-state-machine">🚀 See Full Deep Dive</a>


---

<div id="threads-vs-coroutines"></div>

## What is the difference between threads and coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">threading</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    Threads are OS-level execution units; coroutines are lightweight
    units of suspended work scheduled on threads.

    Practical distinction:

    - threads are heavier to create/switch
    - coroutines are cheaper and structured
    - multiple coroutines can share a small thread pool
    - coroutines do not replace threads for every use case


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/threads-vs-coroutines/#threads-vs-coroutines">🚀 See Full Deep Dive</a>


---

<div id="dispatchers-overview"></div>

## What are Dispatchers in Kotlin Coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">dispatchers</span>
  <span class="question-badge question-badge--tag">threading</span>
</div>

??? question "View Answer"

    Dispatchers decide where coroutine code runs.

    Common dispatchers:

    - `Main` for UI work
    - `IO` for blocking I/O
    - `Default` for CPU-heavy work

    Good interview answer: dispatchers are a scheduling policy,
    not a background-thread guarantee by themselves.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/threads-dispatchers-context/#dispatchers-overview">🚀 See Full Deep Dive</a>


---

<div id="withcontext-purpose"></div>

## What does `withContext` do and why is it important?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">threading</span>
  <span class="question-badge question-badge--tag">kotlin</span>
</div>

??? question "View Answer"

    `withContext` switches coroutine execution to another dispatcher
    for a scoped block of work.

    It is useful for:

    - moving blocking work off the main thread
    - returning results back to the original coroutine
    - keeping context switching explicit and readable


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/threads-dispatchers-context/#withcontext-purpose">🚀 See Full Deep Dive</a>


---

<div id="coroutine-scope"></div>

## What is `CoroutineScope` and why does it matter?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">scope</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    `CoroutineScope` defines the lifetime boundary for launching coroutines.

    It matters because it controls:

    - cancellation ownership
    - structured concurrency behavior
    - leak prevention
    - lifecycle alignment in Android


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/structured-scope-and-jobs/#coroutine-scope">🚀 See Full Deep Dive</a>


---

<div id="job-hierarchy"></div>

## How does coroutine job hierarchy work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">job</span>
  <span class="question-badge question-badge--tag">structure</span>
</div>

??? question "View Answer"

    Coroutine jobs form a parent-child hierarchy.

    When a parent job is cancelled, its children are cancelled too.
    Child failure can also propagate upward depending on scope type.

    Interview points:

    - explicit ownership tree
    - cooperative cancellation
    - failure propagation rules


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/structured-scope-and-jobs/#job-hierarchy">🚀 See Full Deep Dive</a>


---

<div id="supervisorjob"></div>

## What is the difference between `Job` and `SupervisorJob`?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">job</span>
  <span class="question-badge question-badge--tag">failure</span>
</div>

??? question "View Answer"

    A regular `Job` propagates child failure to the parent and can cancel siblings.

    `SupervisorJob` isolates child failures so one child can fail
    without automatically cancelling others.

    Use it when:

    - sibling tasks are independent
    - partial failure should not bring down the whole scope


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/structured-scope-and-jobs/#supervisorjob">🚀 See Full Deep Dive</a>


---

<div id="supervisorScope"></div>

## What does `supervisorScope` do?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">scope</span>
  <span class="question-badge question-badge--tag">failure</span>
</div>

??? question "View Answer"

    `supervisorScope` creates a scoped region where child failures are isolated.

    It is useful when you want to launch multiple related tasks and tolerate
    failure in one child while handling its result explicitly.

    Difference from `coroutineScope`:

    - failure isolation vs fail-fast cancellation
    - localized supervision boundary


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/structured-scope-and-jobs/#supervisorScope">🚀 See Full Deep Dive</a>


---

<div id="coroutine-cancellation"></div>

## How does coroutine cancellation work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">cancellation</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    Coroutine cancellation is cooperative.

    A coroutine stops when it checks for cancellation or reaches a cancellable
    suspension point.

    Important ideas:

    - `Job.cancel()` requests cancellation
    - suspension functions often detect it automatically
    - non-cooperative work must check manually


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/cancellation-exception-supervision/#coroutine-cancellation">🚀 See Full Deep Dive</a>


---

<div id="cooperative-cancellation"></div>

## What is cooperative cancellation?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">cancellation</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Cooperative cancellation means coroutines must periodically observe cancellation
    and stop themselves instead of being forcefully killed.

    This is important because it keeps cleanup predictable and avoids
    abrupt state corruption.

    Common tools:

    - `isActive`
    - `ensureActive()`
    - cancellable suspending functions


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/cancellation-exception-supervision/#cooperative-cancellation">🚀 See Full Deep Dive</a>


---

<div id="coroutine-exception-handling"></div>

## How are exceptions handled in coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">exceptions</span>
  <span class="question-badge question-badge--tag">supervision</span>
</div>

??? question "View Answer"

    Coroutine exception handling depends on the coroutine builder and scope.

    Key points:

    - `launch` propagates exceptions to its parent
    - `async` stores exceptions until awaited
    - failures can cancel sibling children in regular scopes
    - supervision changes propagation behavior


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/cancellation-exception-supervision/#coroutine-exception-handling">🚀 See Full Deep Dive</a>


---

<div id="coroutineexceptionhandler"></div>

## What is `CoroutineExceptionHandler` used for?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">exceptions</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    `CoroutineExceptionHandler` handles uncaught exceptions in root coroutines
    launched with `launch`.

    It is not a replacement for try/catch in suspend code.

    Use it to:

    - log/report uncaught failures
    - provide a last-resort safety net
    - centralize crash telemetry in root scopes


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/cancellation-exception-supervision/#coroutineexceptionhandler">🚀 See Full Deep Dive</a>


---

<div id="launch-vs-async"></div>

## What is the difference between `launch` and `async`?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">builders</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    `launch` is for fire-and-forget work; `async` is for concurrent work that
    produces a result.

    Interview framing:

    - `launch` returns `Job`
    - `async` returns `Deferred`
    - `async` exceptions are observed on `await()`
    - prefer the simplest builder that matches the need


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/launch-async-parallelism/#launch-vs-async">🚀 See Full Deep Dive</a>


---

<div id="lazy-async"></div>

## What is lazy async?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">async</span>
  <span class="question-badge question-badge--tag">scheduling</span>
</div>

??? question "View Answer"

    Lazy async defers coroutine start until the result is actually awaited
    or explicitly started.

    It can be useful when you want to create a deferred task graph but
    avoid doing work until the result is needed.

    Tradeoff: lazy start can make control flow harder to reason about.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/launch-async-parallelism/#lazy-async">🚀 See Full Deep Dive</a>


---

<div id="parallelism-limit"></div>

## How do you limit coroutine parallelism?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">parallelism</span>
</div>

??? question "View Answer"

    Limit parallelism by controlling dispatcher usage and the number of
    concurrently active jobs.

    Common approaches:

    - semaphore-style gating
    - dispatcher `limitedParallelism`
    - batching work into controlled chunks

    This prevents resource saturation and tail-latency spikes.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/launch-async-parallelism/#parallelism-limit">🚀 See Full Deep Dive</a>


---

<div id="thread-pools"></div>

## What are coroutine thread pools?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">threading</span>
  <span class="question-badge question-badge--tag">scheduler</span>
</div>

??? question "View Answer"

    Coroutine dispatchers usually run on top of shared thread pools.

    These pools multiplex many coroutines onto fewer OS threads,
    improving efficiency compared with one-thread-per-task models.

    Interview points:

    - pools are shared resources
    - pool saturation affects latency
    - CPU and blocking work should be separated carefully


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/scheduler-thread-pools/#thread-pools">🚀 See Full Deep Dive</a>


---

<div id="thread-starvation"></div>

## What is thread starvation in concurrency?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">threading</span>
  <span class="question-badge question-badge--tag">scheduler</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Thread starvation happens when tasks cannot get scheduled time on a thread
    or thread pool because resources are monopolized by other work.

    In Android apps it often appears when:

    - blocking code occupies shared pools
    - parallelism is unbounded
    - main-thread work is overloaded


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/scheduler-thread-pools/#thread-starvation">🚀 See Full Deep Dive</a>


---

<div id="limited-parallelism"></div>

## What is `limitedParallelism` in coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">parallelism</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    `limitedParallelism` constrains the amount of concurrent work scheduled
    through a dispatcher view.

    It is useful for:

    - protecting shared downstream resources
    - preventing resource thrash
    - balancing throughput and fairness

    Good interview answer: it is a concurrency control tool, not just an optimization.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/parallelism-and-scheduling/#limited-parallelism">🚀 See Full Deep Dive</a>


---

<div id="flow-what-is"></div>

## What is Flow in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">streams</span>
</div>

??? question "View Answer"

    Flow is Kotlin's asynchronous stream API.

    It is used to represent values that arrive over time while remaining
    cancellation-aware and coroutine-based.

    Key traits:

    - declarative stream pipeline
    - cold by default
    - integrates with coroutines and operators


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/flow-fundamentals/#flow-what-is">🚀 See Full Deep Dive</a>


---

<div id="cold-vs-hot-flow"></div>

## What is the difference between cold and hot flows?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">state</span>
</div>

??? question "View Answer"

    Cold flows start producing values per collector.
    Hot flows can emit independently of collectors.

    In interviews, explain:

    - cold = collector drives execution
    - hot = producer exists independently
    - StateFlow and SharedFlow are hot stream primitives


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/flow-fundamentals/#cold-vs-hot-flow">🚀 See Full Deep Dive</a>


---

<div id="backpressure"></div>

## What is backpressure in Flow?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">buffering</span>
</div>

??? question "View Answer"

    Backpressure is what happens when upstream produces data faster than
    downstream can consume it.

    Flow handles this through suspension, buffering, conflation,
    or explicit operator choices.

    Why it matters:

    - protects memory and responsiveness
    - affects latency and throughput
    - can change user-visible behavior


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/flow-fundamentals/#backpressure">🚀 See Full Deep Dive</a>


---

<div id="collectLatest"></div>

## When should you use `collectLatest`?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">cancellation</span>
  <span class="question-badge question-badge--tag">operators</span>
</div>

??? question "View Answer"

    Use `collectLatest` when new emissions should cancel the previous collector
    work and only the newest value matters.

    Common use cases:

    - search suggestions
    - rapid UI updates
    - debounced rendering pipelines


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/flow-operators-and-backpressure/#collectLatest">🚀 See Full Deep Dive</a>


---

<div id="flatMapLatest"></div>

## When should you use `flatMapLatest`?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">operators</span>
  <span class="question-badge question-badge--tag">cancellation</span>
</div>

??? question "View Answer"

    `flatMapLatest` switches to a new inner flow whenever the outer value changes,
    cancelling the previous inner stream.

    This is ideal for:

    - query-driven network search
    - live UI filters
    - state pipelines where only the newest source matters


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/flow-operators-and-backpressure/#flatMapLatest">🚀 See Full Deep Dive</a>


---

<div id="buffering-conflation"></div>

## What is buffering and conflation in Flow?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">buffering</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Buffering allows upstream and downstream to proceed with some decoupling.
    Conflation drops intermediate values and keeps the latest one.

    Use cases:

    - buffering for throughput
    - conflation for UI state that only needs the latest value

    Tradeoff: speed vs completeness of intermediate emissions.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/flow-operators-and-backpressure/#buffering-conflation">🚀 See Full Deep Dive</a>


---

<div id="stateflow-vs-sharedflow"></div>

## What is the difference between StateFlow and SharedFlow?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">state</span>
  <span class="question-badge question-badge--tag">events</span>
</div>

??? question "View Answer"

    StateFlow represents state with a current value.
    SharedFlow represents shared emissions/events without a required initial state.

    Good interview framing:

    - StateFlow for persistent UI state
    - SharedFlow for one-off events or broadcasts
    - both are hot and coroutine-friendly


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/stateflow-sharedflow-and-channels/#stateflow-vs-sharedflow">🚀 See Full Deep Dive</a>


---

<div id="channels-vs-sharedflow"></div>

## When should you use a Channel instead of SharedFlow?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">channels</span>
  <span class="question-badge question-badge--tag">events</span>
</div>

??? question "View Answer"

    Use a Channel when you want point-to-point handoff semantics or a queue-like
    one-consumer model.

    Use SharedFlow when you want multicasting or multiple subscribers.

    Interview nuance:

    - Channel = delivery semantics and backpressure control
    - SharedFlow = broadcast-style hot stream


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/stateflow-sharedflow-and-channels/#channels-vs-sharedflow">🚀 See Full Deep Dive</a>


---

<div id="statein-sharein"></div>

## What are `stateIn` and `shareIn` used for?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">sharing</span>
  <span class="question-badge question-badge--tag">state</span>
</div>

??? question "View Answer"

    `stateIn` converts a Flow into a hot StateFlow-like state holder.
    `shareIn` shares upstream work among multiple collectors.

    They are useful when:

    - expensive upstream work should be shared
    - UI needs lifecycle-friendly hot stream behavior
    - a cold stream should become reusable across collectors


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/flow-sharing-and-hot-streams/#statein-sharein">🚀 See Full Deep Dive</a>


---

<div id="one-off-events-with-sharedflow"></div>

## How do you model one-off events with SharedFlow?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">events</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    SharedFlow is often used to emit transient UI events such as navigation,
    toast messages, or snackbar actions.

    Good practice:

    - keep replay small or zero for one-off events
    - collect from lifecycle-aware UI scopes
    - avoid encoding events as sticky state


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/flow-sharing-and-hot-streams/#one-off-events-with-sharedflow">🚀 See Full Deep Dive</a>


---

<div id="callbackflow"></div>

## What is `callbackFlow`?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">callbacks</span>
  <span class="question-badge question-badge--tag">interop</span>
</div>

??? question "View Answer"

    `callbackFlow` bridges callback-based APIs into a Flow.

    It is useful when an API delivers values through listeners,
    observers, or callbacks rather than suspend/Flow primitives.

    Key concerns:

    - close resources in awaitClose
    - avoid leaking listeners
    - respect backpressure and cancellation


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/callbackflow-and-channelflow/#callbackflow">🚀 See Full Deep Dive</a>


---

<div id="channelflow"></div>

## What is `channelFlow`?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">channels</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    `channelFlow` is a builder for producing Flow values from multiple
    concurrent senders inside a coroutine scope.

    It is useful when emissions come from several concurrent sources and you
    need a single Flow channel to merge them safely.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/callbackflow-and-channelflow/#channelflow">🚀 See Full Deep Dive</a>


---

<div id="flow-callback-interop"></div>

## How do you bridge callbacks into Flow safely?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">callbacks</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    Bridge callbacks into Flow with a lifecycle-aware, cancellable adapter.

    Practical rules:

    - register listener when collection starts
    - unregister in awaitClose or equivalent cleanup
    - avoid blocking callback threads
    - keep backpressure and cancellation in mind


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/callbackflow-and-channelflow/#flow-callback-interop">🚀 See Full Deep Dive</a>


---

<div id="mutex"></div>

## What is `Mutex` in Kotlin coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">synchronization</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    `Mutex` is a coroutine-friendly mutual exclusion primitive.

    It protects critical sections without blocking a thread the way a JVM
    lock might.

    Interview points:

    - suspending lock acquisition
    - cooperative with coroutines
    - useful for protecting shared mutable state


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/synchronization-and-mutex/#mutex">🚀 See Full Deep Dive</a>


---

<div id="synchronization-strategies"></div>

## What are common synchronization strategies in concurrent code?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">synchronization</span>
  <span class="question-badge question-badge--tag">threading</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Synchronization strategies include mutexes, atomics, thread confinement,
    immutable data, and message passing.

    Good interview answer:

    - choose the simplest strategy that preserves correctness
    - prefer immutability when practical
    - use locks only around real shared mutable state


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/synchronization-and-mutex/#synchronization-strategies">🚀 See Full Deep Dive</a>


---

<div id="shared-mutable-state"></div>

## Why is shared mutable state dangerous?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">concurrency</span>
  <span class="question-badge question-badge--tag">state</span>
  <span class="question-badge question-badge--tag">race-conditions</span>
</div>

??? question "View Answer"

    Shared mutable state is hard to reason about because concurrent reads and
    writes can interleave unpredictably.

    Risks include:

    - race conditions
    - inconsistent reads
    - deadlocks and contention
    - difficult debugging


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/synchronization-and-mutex/#shared-mutable-state">🚀 See Full Deep Dive</a>


---

<div id="atomic-operations"></div>

## What are atomic operations used for?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">concurrency</span>
  <span class="question-badge question-badge--tag">atomic</span>
  <span class="question-badge question-badge--tag">synchronization</span>
</div>

??? question "View Answer"

    Atomic operations allow safe lock-free updates for certain shared values.

    They are useful when you need:

    - simple counters or flags
    - high-throughput coordination
    - predictable low-overhead synchronization

    They are not a universal replacement for locks.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/synchronization-and-mutex/#atomic-operations">🚀 See Full Deep Dive</a>


---

<div id="thread-confinement"></div>

## What is thread confinement?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">threading</span>
  <span class="question-badge question-badge--tag">concurrency</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    Thread confinement means restricting access to mutable state to a single thread
    or dispatcher.

    This simplifies correctness because only one execution context
    can mutate the state at a time.

    Common Android examples:

    - main-thread UI ownership
    - single-threaded executors for caches


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/thread-confinement-and-race-conditions/#thread-confinement">🚀 See Full Deep Dive</a>


---

<div id="race-conditions"></div>

## What is a race condition?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">concurrency</span>
  <span class="question-badge question-badge--tag">bugs</span>
  <span class="question-badge question-badge--tag">threading</span>
</div>

??? question "View Answer"

    A race condition happens when the behavior depends on the timing/order of
    concurrent operations.

    In practice it appears as:

    - inconsistent UI or state
    - flaky tests
    - intermittent crashes or stale data


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/thread-confinement-and-race-conditions/#race-conditions">🚀 See Full Deep Dive</a>


---

<div id="deadlocks"></div>

## What is a deadlock?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">concurrency</span>
  <span class="question-badge question-badge--tag">deadlocks</span>
  <span class="question-badge question-badge--tag">synchronization</span>
</div>

??? question "View Answer"

    A deadlock occurs when two or more tasks are waiting on each other
    and none can continue.

    Avoid deadlocks by:

    - minimizing lock scope
    - using consistent lock ordering
    - preferring non-blocking coordination when possible


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/thread-confinement-and-race-conditions/#deadlocks">🚀 See Full Deep Dive</a>


---

<div id="coroutine-testing"></div>

## How do you test coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    Test coroutines with a controlled test dispatcher and coroutine test scope.

    Good practices:

    - replace real dispatchers with test dispatchers
    - assert state transitions deterministically
    - avoid real delays and sleeps in tests


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-testing-and-virtual-time/#coroutine-testing">🚀 See Full Deep Dive</a>


---

<div id="virtual-time-testing"></div>

## How does virtual time testing work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">time</span>
</div>

??? question "View Answer"

    Virtual time testing advances coroutine-scheduled time without waiting in real time.

    This makes delay-based and timeout-based tests fast and deterministic.

    It is especially useful for:

    - retry logic
    - debounce behavior
    - cancellation timing


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-testing-and-virtual-time/#virtual-time-testing">🚀 See Full Deep Dive</a>


---

<div id="test-dispatchers"></div>

## Why use test dispatchers for coroutine tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">dispatchers</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    Test dispatchers let you control coroutine execution in tests.

    This helps you:

    - avoid flaky scheduler-dependent behavior
    - make execution deterministic
    - verify concurrency logic without real threads or delays


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-testing-and-virtual-time/#test-dispatchers">🚀 See Full Deep Dive</a>


---

<div id="coroutine-debugging"></div>

## How do you debug coroutines in production?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">debugging</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">observability</span>
</div>

??? question "View Answer"

    Debugging coroutines in production requires good tracing and context naming.

    Helpful techniques:

    - name coroutine jobs meaningfully
    - log structured context and cancellation events
    - correlate coroutine lifecycles with user actions and requests


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-debugging-and-observability/#coroutine-debugging">🚀 See Full Deep Dive</a>


---

<div id="trace-and-observability"></div>

## How should you observe coroutine and Flow behavior?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">observability</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    Observe coroutines and flows by adding tracing around launch/collection,
    measuring latency, and tracking cancellations/failures.

    Useful signals:

    - collection duration
    - emission count and rate
    - cancellation and error frequency


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/coroutine-debugging-and-observability/#trace-and-observability">🚀 See Full Deep Dive</a>


---

<div id="repeatOnLifecycle-flow-collection"></div>

## How should Flow be collected with Android lifecycle?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">android</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">lifecycle</span>
</div>

??? question "View Answer"

    Collect Flow with lifecycle awareness so UI stops observing when the screen
    is not active.

    This prevents wasted work and leaks.

    In Android, the common guidance is to tie collection to a lifecycle scope
    or repeat collection when the lifecycle is active.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/android-lifecycle-and-flow-collection/#repeatOnLifecycle-flow-collection">🚀 See Full Deep Dive</a>


---

<div id="main-safety"></div>

## What does main-safety mean?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">android</span>
  <span class="question-badge question-badge--tag">main-thread</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    Main-safety means code can be called from the main thread without blocking
    it for long periods.

    A main-safe API internally shifts blocking work off the UI thread,
    keeping UI responsive.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/android-lifecycle-and-main-safety/#main-safety">🚀 See Full Deep Dive</a>


---

<div id="anr-and-main-thread"></div>

## Why do blocking calls on the main thread cause ANRs?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">android</span>
  <span class="question-badge question-badge--tag">anr</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Blocking the main thread prevents input, rendering, and lifecycle work from
    progressing on time.

    If the app cannot respond within the system's expected window, it can trigger
    an ANR.

    The fix is to keep blocking work off the main thread and make APIs main-safe.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/android-lifecycle-and-main-safety/#anr-and-main-thread">🚀 See Full Deep Dive</a>


---

<div id="concurrency-performance-optimization"></div>

## How do you optimize concurrency performance in production?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">concurrency</span>
  <span class="question-badge question-badge--tag">coroutines</span>
</div>

??? question "View Answer"

    Optimize concurrency by reducing contention, limiting parallelism,
    and minimizing blocking work.

    Practical steps:

    - measure before tuning
    - keep main-thread work minimal
    - share expensive upstream work
    - use bounded pools and backpressure-aware flows


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/concurrency/production-concurrency-patterns-and-tuning/#concurrency-performance-optimization">🚀 See Full Deep Dive</a>

