# Kotlin Deep Dive Mapping & Architecture

## Overview

This document maps Kotlin interview questions to shared deep dives. The goal is to keep `data/kotlin.yaml` concise while putting compiler, JVM, coroutine, and Flow internals into dedicated markdown deep dives.

---

## Recommended Deep Dive Files

1. `docs/deep-dives/kotlin/kotlin-basics.md`
2. `docs/deep-dives/kotlin/data-classes-and-generated-code.md`
3. `docs/deep-dives/kotlin/object-and-companion-objects.md`
4. `docs/deep-dives/kotlin/sealed-classes-and-enums.md`
5. `docs/deep-dives/kotlin/delegation-and-delegated-properties.md`
6. `docs/deep-dives/kotlin/extension-functions.md`
7. `docs/deep-dives/kotlin/scope-functions.md`
8. `docs/deep-dives/kotlin/higher-order-functions-and-lambdas.md`
9. `docs/deep-dives/kotlin/inline-functions.md`
10. `docs/deep-dives/kotlin/reified-generics.md`
11. `docs/deep-dives/kotlin/null-safety-and-smart-casts.md`
12. `docs/deep-dives/kotlin/generics-and-variance.md`
13. `docs/deep-dives/kotlin/collections-and-sequences.md`
14. `docs/deep-dives/kotlin/coroutines-foundations.md`
15. `docs/deep-dives/kotlin/dispatchers-and-coroutine-scope.md`
16. `docs/deep-dives/kotlin/structured-concurrency-and-jobs.md`
17. `docs/deep-dives/kotlin/cancellation-and-exception-handling.md`
18. `docs/deep-dives/kotlin/flow-fundamentals.md`
19. `docs/deep-dives/kotlin/stateflow-sharedflow-and-channels.md`
20. `docs/deep-dives/kotlin/jvm-interop-and-bytecode.md`

---

## Question-to-Deep-Dive Mapping

### 1. Kotlin Basics
**File:** `docs/deep-dives/kotlin/kotlin-basics.md`

**Questions (2):**
- `kotlin-language-features`
- `val-vs-var`

**Recommended sections:**
- Overview
- Kotlin design goals
- Readability vs verbosity
- Immutability mindset
- JVM positioning
- Android engineering relevance

---

### 2. Data Classes and Generated Code
**File:** `docs/deep-dives/kotlin/data-classes-and-generated-code.md`

**Questions (2):**
- `data-classes`
- `data-class-generated-members`

**Recommended sections:**
- Overview
- Generated methods
- Equality semantics
- `copy()` behavior
- Destructuring
- JVM generated code notes

---

### 3. Object and Companion Objects
**File:** `docs/deep-dives/kotlin/object-and-companion-objects.md`

**Questions (3):**
- `object-keyword`
- `companion-objects`
- `object-declaration-vs-object-expression`

**Recommended sections:**
- Object forms in Kotlin
- Singleton behavior
- Companion object internals
- Static-like APIs on JVM
- Object expression typing rules

---

### 4. Sealed Classes and Enums
**File:** `docs/deep-dives/kotlin/sealed-classes-and-enums.md`

**Questions (3):**
- `sealed-classes`
- `sealed-vs-enum`
- `enum-class-use-cases`

**Recommended sections:**
- Closed hierarchies
- Exhaustive `when`
- Enums vs sealed tradeoffs
- Modeling state/results
- Serialization and maintainability notes

---

### 5. Delegation and Delegated Properties
**File:** `docs/deep-dives/kotlin/delegation-and-delegated-properties.md`

**Questions (3):**
- `class-delegation`
- `delegated-properties`
- `lazy-delegation`

**Recommended sections:**
- Composition via `by`
- Property delegates
- `lazy` internals
- Observable/vetoable delegates
- Thread-safety considerations

---

### 6. Extension Functions
**File:** `docs/deep-dives/kotlin/extension-functions.md`

**Questions (2):**
- `extension-functions`
- `extension-function-resolution`

**Recommended sections:**
- Extension syntax
- Static dispatch rules
- Member precedence
- API design use cases
- Interview traps

---

### 7. Scope Functions
**File:** `docs/deep-dives/kotlin/scope-functions.md`

**Questions (2):**
- `scope-functions`
- `let-vs-run-vs-apply-vs-also`

**Recommended sections:**
- Receiver vs argument semantics
- Return values
- Readability tradeoffs
- Common Android use cases

---

### 8. Higher-Order Functions and Lambdas
**File:** `docs/deep-dives/kotlin/higher-order-functions-and-lambdas.md`

**Questions (2):**
- `higher-order-functions`
- `lambdas-with-receiver`

**Recommended sections:**
- Function types
- Higher-order APIs
- Lambdas with receiver
- DSL patterns
- Allocation and readability notes

---

### 9. Inline Functions
**File:** `docs/deep-dives/kotlin/inline-functions.md`

**Questions (3):**
- `inline-functions`
- `crossinline-vs-noinline`
- `inline-performance-considerations`

**Recommended sections:**
- Inline expansion
- Lambda allocation avoidance
- Non-local returns
- `crossinline` and `noinline`
- Bytecode size tradeoffs

---

### 10. Reified Generics
**File:** `docs/deep-dives/kotlin/reified-generics.md`

**Questions (1):**
- `reified-generics`

**Recommended sections:**
- Type erasure
- Why reified requires inline
- Common Android use cases
- API design patterns

---

### 11. Null Safety and Smart Casts
**File:** `docs/deep-dives/kotlin/null-safety-and-smart-casts.md`

**Questions (3):**
- `null-safety`
- `safe-call-elvis-not-null`
- `smart-casts`

**Recommended sections:**
- Nullable vs non-nullable types
- Operator semantics
- Flow-sensitive typing
- Interop pitfalls
- Production nullability patterns

---

### 12. Generics and Variance
**File:** `docs/deep-dives/kotlin/generics-and-variance.md`

**Questions (3):**
- `generics-in-kotlin`
- `variance-in-out`
- `star-projection`

**Recommended sections:**
- Type erasure
- Variance rules
- Producers vs consumers
- Star projections
- API design implications

---

### 13. Collections and Sequences
**File:** `docs/deep-dives/kotlin/collections-and-sequences.md`

**Questions (3):**
- `collections-api`
- `immutable-vs-mutable-collections`
- `sequences-vs-collections`

**Recommended sections:**
- Collections operator model
- Read-only vs immutable
- Sequence laziness
- Allocation/performance tradeoffs

---

### 14. Coroutines Foundations
**File:** `docs/deep-dives/kotlin/coroutines-foundations.md`

**Questions (3):**
- `coroutines-what-are`
- `suspend-functions`
- `continuation-and-cps`

**Recommended sections:**
- Coroutine model
- Suspend semantics
- Continuation passing style
- State machine overview
- Threading misconceptions

---

### 15. Dispatchers and Coroutine Scope
**File:** `docs/deep-dives/kotlin/dispatchers-and-coroutine-scope.md`

**Questions (2):**
- `dispatchers`
- `coroutine-scope`

**Recommended sections:**
- Dispatcher roles
- Main/IO/Default tradeoffs
- Scope ownership
- Android lifecycle scopes
- Context composition

---

### 16. Structured Concurrency and Jobs
**File:** `docs/deep-dives/kotlin/structured-concurrency-and-jobs.md`

**Questions (4):**
- `structured-concurrency`
- `job-vs-supervisorjob`
- `async-vs-launch`
- `job-hierarchy`

**Recommended sections:**
- Parent-child relationships
- Job tree behavior
- `launch` vs `async`
- Supervisor semantics
- Failure propagation

---

### 17. Cancellation and Exception Handling
**File:** `docs/deep-dives/kotlin/cancellation-and-exception-handling.md`

**Questions (2):**
- `coroutine-cancellation`
- `coroutine-exception-handling`

**Recommended sections:**
- Cooperative cancellation
- Cancellation checks
- Exception propagation
- `CoroutineExceptionHandler`
- Production pitfalls

---

### 18. Flow Fundamentals
**File:** `docs/deep-dives/kotlin/flow-fundamentals.md`

**Questions (2):**
- `flow-what-is`
- `cold-vs-hot-flow`

**Recommended sections:**
- Cold stream model
- Collector lifecycle
- Operators basics
- Backpressure and cancellation
- Android state pipelines

---

### 19. StateFlow, SharedFlow, and Channels
**File:** `docs/deep-dives/kotlin/stateflow-sharedflow-and-channels.md`

**Questions (3):**
- `stateflow-vs-sharedflow`
- `channels-vs-sharedflow`
- `mutex-in-kotlin`

**Recommended sections:**
- Hot flow primitives
- State vs event modeling
- Channel semantics
- Buffering/replay
- Synchronization with `Mutex`

---

### 20. JVM Interop and Bytecode
**File:** `docs/deep-dives/kotlin/jvm-interop-and-bytecode.md`

**Questions (3):**
- `kotlin-jvm-interoperability`
- `kotlin-bytecode-basics`
- `suspend-state-machine`

**Recommended sections:**
- Kotlin ↔ Java interop
- Default args and generated helpers
- Nullability at Java boundaries
- Bytecode structure
- Coroutine state machines

---

## Summary

- **Total Kotlin Questions:** 51
- **Total Shared Deep Dives:** 20
- **Audience:** mid, senior, and staff Android interviews
- **Design Goal:** concise generated answers + rich deep dives

