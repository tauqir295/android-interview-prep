---
hide:
  - toc
---

# Kotlin

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

<div id="kotlin-language-features"></div>

## What makes Kotlin a good language for Android development?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">android</span>
  <span class="question-badge question-badge--tag">fundamentals</span>
</div>

??? question "View Answer"

    Kotlin is a modern JVM language designed to improve safety,
    readability, and developer productivity.
    Key advantages for Android:
    - null safety support
    - concise syntax
    - strong IDE tooling
    - Java interoperability
    - coroutine support
    In interviews, mention that Kotlin reduces boilerplate while still
    compiling to JVM bytecode and working well with existing Java code.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/kotlin-basics/#kotlin-language-features">🚀 See Full Deep Dive</a>


---

<div id="val-vs-var"></div>

## What is the difference between val and var in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">basics</span>
  <span class="question-badge question-badge--tag">immutability</span>
</div>

??? question "View Answer"

    `val` defines a read-only reference.
    `var` defines a mutable reference.
    Key distinction:
    - `val` cannot be reassigned after initialization
    - `var` can be reassigned
    Important interview nuance:
    - `val` does NOT make the object itself immutable
    - it only makes the reference stable
    Prefer `val` by default and use `var` only when mutation is required.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/kotlin-basics/#val-vs-var">🚀 See Full Deep Dive</a>


---

<div id="data-classes"></div>

## What is a data class in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">data-classes</span>
  <span class="question-badge question-badge--tag">basics</span>
</div>

??? question "View Answer"

    A data class is a class optimized for holding data.
    Kotlin automatically generates:
    - `equals()`
    - `hashCode()`
    - `toString()`
    - `copy()`
    - `componentN()` functions
    Use data classes for:
    - UI models
    - DTOs
    - state holders
    - domain values
    They are ideal when value equality matters more than identity.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/data-classes-and-generated-code/#data-classes">🚀 See Full Deep Dive</a>


---

<div id="data-class-generated-members"></div>

## What methods does Kotlin generate for a data class?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">data-classes</span>
  <span class="question-badge question-badge--tag">compiler</span>
</div>

??? question "View Answer"

    Kotlin generates several members from primary constructor properties:
    - `equals()` and `hashCode()`
    - `toString()`
    - `copy()`
    - `componentN()` destructuring functions
    Interview detail:
    - only properties in the primary constructor participate
    - body properties are excluded from generated equality/copy behavior
    This is important for state modeling and JVM behavior discussions.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/data-classes-and-generated-code/#data-class-generated-members">🚀 See Full Deep Dive</a>


---

<div id="object-keyword"></div>

## What does the object keyword do in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">object</span>
  <span class="question-badge question-badge--tag">language-features</span>
</div>

??? question "View Answer"

    The `object` keyword has multiple uses in Kotlin:
    - object declaration → singleton
    - object expression → anonymous object
    - companion object → class-level members
    Interview point:
    Kotlin uses one keyword for several object creation patterns,
    but each compiles differently on the JVM.
    Always clarify which form of `object` you mean.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/object-and-companion-objects/#object-keyword">🚀 See Full Deep Dive</a>


---

<div id="companion-objects"></div>

## What is a companion object in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">object</span>
  <span class="question-badge question-badge--tag">jvm</span>
</div>

??? question "View Answer"

    A companion object is an object tied to a class definition.
    It is commonly used for:
    - factory methods
    - constants
    - static-like APIs
    - interface implementations
    Important interview nuance:
    - Kotlin has no true `static` keyword
    - companion objects are regular objects with special syntax support
    On the JVM, they are not identical to Java static members.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/object-and-companion-objects/#companion-objects">🚀 See Full Deep Dive</a>


---

<div id="object-declaration-vs-object-expression"></div>

## What is the difference between an object declaration and an object expression?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">object</span>
  <span class="question-badge question-badge--tag">internals</span>
</div>

??? question "View Answer"

    Object declaration:
    - defines a named singleton
    - initialized lazily on first access
    Object expression:
    - creates an anonymous object immediately
    - often used for one-off implementations
    Use declaration for shared singleton behavior.
    Use expression for local, ad-hoc object creation.
    Interview detail: visibility and inferred type behavior differ,
    especially when returning anonymous objects from APIs.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/object-and-companion-objects/#object-declaration-vs-object-expression">🚀 See Full Deep Dive</a>


---

<div id="sealed-classes"></div>

## What is a sealed class in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">sealed</span>
  <span class="question-badge question-badge--tag">modeling</span>
</div>

??? question "View Answer"

    A sealed class restricts inheritance to a known set of subclasses.
    It is useful for:
    - UI state modeling
    - result wrappers
    - finite state machines
    - exhaustive `when` expressions
    Key benefit:
    the compiler knows all valid subtypes at compile time.
    This makes sealed hierarchies safer than open inheritance for
    closed-domain modeling.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/sealed-classes-and-enums/#sealed-classes">🚀 See Full Deep Dive</a>


---

<div id="sealed-vs-enum"></div>

## When should you use a sealed class instead of an enum?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">sealed</span>
  <span class="question-badge question-badge--tag">enums</span>
</div>

??? question "View Answer"

    Use an enum when you need a fixed set of simple constants.
    Use a sealed class when each case may carry different data
    or behavior.
    Quick comparison:
    - enum → single instance per constant
    - sealed class → richer subtype hierarchy
    - enum → good for flags/statuses
    - sealed class → good for UI states/results/events
    In interviews, emphasize flexibility vs simplicity.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/sealed-classes-and-enums/#sealed-vs-enum">🚀 See Full Deep Dive</a>


---

<div id="enum-class-use-cases"></div>

## What are enum classes useful for in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">enums</span>
  <span class="question-badge question-badge--tag">basics</span>
</div>

??? question "View Answer"

    Enum classes represent a fixed set of named constants.
    Common uses:
    - screen modes
    - status values
    - sorting types
    - feature flags with limited states
    They can also contain:
    - properties
    - functions
    - interface implementations
    Use enums when the domain is fixed and each value is conceptually
    a singleton.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/sealed-classes-and-enums/#enum-class-use-cases">🚀 See Full Deep Dive</a>


---

<div id="class-delegation"></div>

## What is delegation in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">delegation</span>
  <span class="question-badge question-badge--tag">composition</span>
</div>

??? question "View Answer"

    Kotlin supports class delegation using the `by` keyword.
    It lets one class forward interface implementation to another object.
    Benefits:
    - reduces boilerplate
    - favors composition over inheritance
    - keeps behavior reusable
    Interview angle:
    delegation is language-level support for composition patterns that
    would be more verbose in Java.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/delegation-and-delegated-properties/#class-delegation">🚀 See Full Deep Dive</a>


---

<div id="delegated-properties"></div>

## What are delegated properties in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">delegation</span>
  <span class="question-badge question-badge--tag">properties</span>
</div>

??? question "View Answer"

    Delegated properties outsource getter/setter logic to another object.
    Common delegates:
    - `lazy`
    - `observable`
    - `vetoable`
    - custom delegates
    This is useful when property behavior includes:
    - caching
    - validation
    - logging
    - lifecycle-aware initialization
    Delegation is one of Kotlin's most practical language features.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/delegation-and-delegated-properties/#delegated-properties">🚀 See Full Deep Dive</a>


---

<div id="lazy-delegation"></div>

## How does lazy initialization work in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">lazy</span>
  <span class="question-badge question-badge--tag">delegation</span>
</div>

??? question "View Answer"

    `lazy` delays object creation until first access.
    Benefits:
    - avoids unnecessary work
    - reduces startup cost
    - makes expensive initialization demand-driven
    Interview nuance:
    Kotlin offers thread-safety modes for `lazy`, and behavior differs
    depending on synchronization strategy.
    Use `lazy` when initialization is expensive and not always needed.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/delegation-and-delegated-properties/#lazy-delegation">🚀 See Full Deep Dive</a>


---

<div id="extension-functions"></div>

## What are extension functions in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">extensions</span>
  <span class="question-badge question-badge--tag">api-design</span>
</div>

??? question "View Answer"

    Extension functions let you add callable functions to an existing type
    without modifying its source code.
    They are useful for:
    - utility APIs
    - cleaner call sites
    - DSL-like helpers
    - Android-specific convenience methods
    Important interview point:
    extensions do not actually modify the class.
    They are resolved statically by the compiler.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/extension-functions/#extension-functions">🚀 See Full Deep Dive</a>


---

<div id="extension-function-resolution"></div>

## How are extension functions resolved in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">extensions</span>
  <span class="question-badge question-badge--tag">compiler</span>
</div>

??? question "View Answer"

    Extension functions are resolved statically.
    That means dispatch is based on the compile-time type,
    not the runtime type.
    Implications:
    - they do not truly override members
    - member functions always win over extensions
    - polymorphism does not work like normal virtual dispatch
    This is a common Kotlin interview trap.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/extension-functions/#extension-function-resolution">🚀 See Full Deep Dive</a>


---

<div id="scope-functions"></div>

## What are Kotlin scope functions?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">scope-functions</span>
  <span class="question-badge question-badge--tag">idioms</span>
</div>

??? question "View Answer"

    Scope functions execute a block in the context of an object.
    The main ones are:
    - `let`
    - `run`
    - `with`
    - `apply`
    - `also`
    They help with:
    - object configuration
    - null-safe chaining
    - side effects
    - expression-style code
    Use them carefully; overuse can reduce readability.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/scope-functions/#scope-functions">🚀 See Full Deep Dive</a>


---

<div id="let-vs-run-vs-apply-vs-also"></div>

## What is the difference between let, run, apply, also, and with?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">scope-functions</span>
  <span class="question-badge question-badge--tag">readability</span>
</div>

??? question "View Answer"

    The main differences are:
    - receiver name (`this` vs `it`)
    - return value (context object vs lambda result)
    Quick guide:
    - `let` → null-safe transforms
    - `run` → compute result with receiver
    - `apply` → configure object, return object
    - `also` → side effects, return object
    - `with` → grouped calls on receiver
    Interviewers care more about when to use them than memorizing a table.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/scope-functions/#let-vs-run-vs-apply-vs-also">🚀 See Full Deep Dive</a>


---

<div id="higher-order-functions"></div>

## What is a higher-order function in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">functional</span>
  <span class="question-badge question-badge--tag">lambdas</span>
</div>

??? question "View Answer"

    A higher-order function is a function that:
    - takes another function as a parameter, or
    - returns a function
    They are heavily used in Kotlin APIs such as:
    - collection operators
    - coroutines
    - Flow
    - DSL builders
    This style enables concise, reusable, expressive APIs.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/higher-order-functions-and-lambdas/#higher-order-functions">🚀 See Full Deep Dive</a>


---

<div id="lambdas-with-receiver"></div>

## What is a lambda with receiver in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">lambdas</span>
  <span class="question-badge question-badge--tag">dsl</span>
</div>

??? question "View Answer"

    A lambda with receiver gives the lambda an implicit receiver object,
    so members can be called without qualification.
    This powers:
    - builders
    - DSLs
    - `apply`-style APIs
    - Compose-style declarative patterns
    Interview point:
    it improves fluency, but can make scope and receiver resolution harder
    to follow if overused.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/higher-order-functions-and-lambdas/#lambdas-with-receiver">🚀 See Full Deep Dive</a>


---

<div id="inline-functions"></div>

## What is an inline function in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">inline</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    An inline function asks the compiler to copy the function body to the
    call site instead of generating a normal call.
    Benefits:
    - reduces lambda allocation overhead
    - enables non-local returns in some cases
    - works well for higher-order utility APIs
    Tradeoff:
    too much inlining can increase bytecode size.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/inline-functions/#inline-functions">🚀 See Full Deep Dive</a>


---

<div id="crossinline-vs-noinline"></div>

## What are crossinline and noinline in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">inline</span>
  <span class="question-badge question-badge--tag">compiler</span>
</div>

??? question "View Answer"

    These modifiers control lambda behavior inside inline functions.
    - `noinline` → do not inline this lambda
    - `crossinline` → inline it, but forbid non-local return
    Use them when an inline function mixes:
    - direct invocation
    - storage/passing of lambdas
    - callback wrapping
    This is a common advanced Kotlin interview topic.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/inline-functions/#crossinline-vs-noinline">🚀 See Full Deep Dive</a>


---

<div id="inline-performance-considerations"></div>

## When do inline functions help or hurt performance?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">inline</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Inline functions help when they remove overhead from small,
    frequently-called higher-order functions.
    They can hurt when:
    - function bodies are large
    - too much code is duplicated
    - bytecode size grows significantly
    Interview takeaway:
    inline is a targeted optimization, not something to apply everywhere.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/inline-functions/#inline-performance-considerations">🚀 See Full Deep Dive</a>


---

<div id="reified-generics"></div>

## What are reified type parameters in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">generics</span>
  <span class="question-badge question-badge--tag">inline</span>
</div>

??? question "View Answer"

    Reified type parameters let inline functions access generic type
    information at runtime.
    Normally, JVM type erasure removes generic type details.
    Reified types work because the function is inlined at the call site.
    This is useful for:
    - type-safe factories
    - serialization helpers
    - navigation/util APIs
    - reflection-light APIs
    Reified works only in inline functions.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/reified-generics/#reified-generics">🚀 See Full Deep Dive</a>


---

<div id="null-safety"></div>

## How does null safety work in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">null-safety</span>
  <span class="question-badge question-badge--tag">type-system</span>
</div>

??? question "View Answer"

    Kotlin separates nullable and non-nullable types.
    Example:
    - `String` → cannot hold null
    - `String?` → can hold null
    Core null-safety tools:
    - safe call `?.`
    - Elvis operator `?:`
    - smart casts
    - not-null assertion `!!`
    Kotlin reduces null bugs, but interop and unsafe operators can still
    reintroduce them.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/null-safety-and-smart-casts/#null-safety">🚀 See Full Deep Dive</a>


---

<div id="safe-call-elvis-not-null"></div>

## What are the safe call, Elvis operator, and not-null assertion in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">null-safety</span>
  <span class="question-badge question-badge--tag">operators</span>
</div>

??? question "View Answer"

    Common null-safety operators:
    - `?.` → call only if value is non-null
    - `?:` → provide fallback when value is null
    - `!!` → assert non-null and throw if wrong
    Interview advice:
    - prefer `?.` and `?:`
    - avoid `!!` unless failure is truly acceptable
    Overuse of `!!` is often treated as a code smell.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/null-safety-and-smart-casts/#safe-call-elvis-not-null">🚀 See Full Deep Dive</a>


---

<div id="smart-casts"></div>

## What are smart casts in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">type-system</span>
  <span class="question-badge question-badge--tag">compiler</span>
</div>

??? question "View Answer"

    Smart casts let the compiler automatically cast a value after a
    successful type or null check.
    Example cases:
    - `if (x is String)`
    - `if (value != null)`
    They work when the compiler can prove the reference is stable.
    They may fail for:
    - mutable properties
    - custom getters
    - shared state with uncertain mutation
    This reflects Kotlin's flow-sensitive type analysis.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/null-safety-and-smart-casts/#smart-casts">🚀 See Full Deep Dive</a>


---

<div id="generics-in-kotlin"></div>

## How do generics work in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">generics</span>
  <span class="question-badge question-badge--tag">type-system</span>
</div>

??? question "View Answer"

    Generics let classes and functions operate on types abstractly while
    preserving type safety.
    Common uses:
    - collections
    - repositories
    - wrappers like `Result<T>`
    - API abstractions
    On the JVM, Kotlin generics are mostly erased at runtime,
    just like Java generics.
    That is why some runtime generic checks are limited.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/generics-and-variance/#generics-in-kotlin">🚀 See Full Deep Dive</a>


---

<div id="variance-in-out"></div>

## What do in and out mean in Kotlin variance?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">generics</span>
  <span class="question-badge question-badge--tag">variance</span>
</div>

??? question "View Answer"

    Variance controls how generic types relate to each other.
    - `out` = producer / covariance
    - `in` = consumer / contravariance
    Use them to express safe subtype substitution.
    Interview tip:
    explain variance in terms of whether the type only produces values,
    consumes values, or does both.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/generics-and-variance/#variance-in-out">🚀 See Full Deep Dive</a>


---

<div id="star-projection"></div>

## What is a star projection in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">generics</span>
  <span class="question-badge question-badge--tag">variance</span>
</div>

??? question "View Answer"

    A star projection (`*`) represents an unknown type argument while still
    preserving safe usage rules.
    It is Kotlin's safer alternative to raw types.
    Use it when:
    - the exact generic type is irrelevant
    - you only need read-safe access
    - API flexibility matters more than precision
    It is useful in reflection-heavy or framework-style code.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/generics-and-variance/#star-projection">🚀 See Full Deep Dive</a>


---

<div id="collections-api"></div>

## What is important about Kotlin's collections API in interviews?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">collections</span>
  <span class="question-badge question-badge--tag">api</span>
</div>

??? question "View Answer"

    Kotlin's collections API is expressive and functional in style.
    Common operations:
    - `map`
    - `filter`
    - `flatMap`
    - `groupBy`
    - `associate`
    Interview focus:
    - readability vs performance
    - eager evaluation of collections
    - choosing the right operator chain
    It is powerful, but misuse can create unnecessary allocations.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/collections-and-sequences/#collections-api">🚀 See Full Deep Dive</a>


---

<div id="immutable-vs-mutable-collections"></div>

## What is the difference between read-only and mutable collections in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">collections</span>
  <span class="question-badge question-badge--tag">immutability</span>
</div>

??? question "View Answer"

    Kotlin distinguishes read-only collection interfaces from mutable ones.
    Important nuance:
    - read-only does not always mean truly immutable
    - it may only restrict mutation through that reference
    Interviewers often want you to understand the difference between:
    - API-level immutability
    - actual object immutability
    This matters when sharing state across layers or threads.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/collections-and-sequences/#immutable-vs-mutable-collections">🚀 See Full Deep Dive</a>


---

<div id="sequences-vs-collections"></div>

## When should you use Sequence instead of a regular collection chain?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">collections</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    `Sequence` evaluates operations lazily.
    Use it when:
    - processing large datasets
    - chaining many transformations
    - avoiding intermediate collection allocations matters
    Regular collections are often simpler and faster for small datasets.
    Interview answer:
    choose `Sequence` for allocation-sensitive pipelines,
    not automatically for every chain.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/collections-and-sequences/#sequences-vs-collections">🚀 See Full Deep Dive</a>


---

<div id="coroutines-what-are"></div>

## What are Kotlin Coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    Kotlin Coroutines are lightweight concurrency primitives for writing
    asynchronous code in a sequential style.
    They help simplify:
    - background work
    - async operations
    - structured concurrency
    - cancellation-aware code
    Core concepts:
    - `suspend` functions
    - `CoroutineScope`
    - `Dispatcher`
    - `Job`
    Coroutines are cheaper than threads but still require careful design.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/coroutines-foundations/#coroutines-what-are">🚀 See Full Deep Dive</a>


---

<div id="suspend-functions"></div>

## What is a suspend function in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">suspend</span>
</div>

??? question "View Answer"

    A `suspend` function can pause and resume without blocking the thread.
    Important clarification:
    - `suspend` does not automatically mean background thread
    - it means the function can cooperate with coroutine suspension
    Suspend functions are the building blocks of coroutine-based APIs.
    They usually compose with:
    - structured concurrency
    - cancellation
    - dispatcher switching


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/coroutines-foundations/#suspend-functions">🚀 See Full Deep Dive</a>


---

<div id="continuation-and-cps"></div>

## How do suspend functions work internally in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">compiler</span>
</div>

??? question "View Answer"

    Suspend functions are compiled into continuation-passing style (CPS).
    Internally, the compiler:
    - adds a `Continuation` parameter
    - rewrites code into resumable steps
    - builds a state machine for suspension points
    Interview takeaway:
    coroutines look sequential in source code, but compile into a very
    different lower-level form.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/coroutines-foundations/#continuation-and-cps">🚀 See Full Deep Dive</a>


---

<div id="dispatchers"></div>

## What are Dispatchers in Kotlin Coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">dispatchers</span>
</div>

??? question "View Answer"

    Dispatchers decide what thread or thread pool a coroutine runs on.
    Common ones:
    - `Dispatchers.Main`
    - `Dispatchers.IO`
    - `Dispatchers.Default`
    - `Dispatchers.Unconfined` (special case)
    Interview point:
    dispatchers affect execution context, scheduling, and performance.
    Choosing the wrong dispatcher can hurt responsiveness or waste threads.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/dispatchers-and-coroutine-scope/#dispatchers">🚀 See Full Deep Dive</a>


---

<div id="coroutine-scope"></div>

## What is CoroutineScope and why does it matter?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">scope</span>
</div>

??? question "View Answer"

    `CoroutineScope` defines the lifecycle boundary for launched coroutines.
    It matters because it controls:
    - cancellation ownership
    - structured concurrency
    - parent-child relationships
    - leak prevention
    Android examples:
    - `viewModelScope`
    - `lifecycleScope`
    A coroutine without the right scope is often a lifecycle bug.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/dispatchers-and-coroutine-scope/#coroutine-scope">🚀 See Full Deep Dive</a>


---

<div id="structured-concurrency"></div>

## What is structured concurrency in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">structured-concurrency</span>
</div>

??? question "View Answer"

    Structured concurrency means coroutines are launched within a scope that
    defines ownership and lifetime.
    Benefits:
    - child coroutines are tracked
    - cancellation propagates predictably
    - errors are easier to manage
    - work does not leak silently
    Interview summary:
    concurrency should be tied to a parent lifecycle, not launched freely.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/structured-concurrency-and-jobs/#structured-concurrency">🚀 See Full Deep Dive</a>


---

<div id="job-vs-supervisorjob"></div>

## What is the difference between Job and SupervisorJob?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">jobs</span>
</div>

??? question "View Answer"

    `Job` and `SupervisorJob` both manage coroutine lifecycle,
    but failure propagation differs.
    - `Job` → child failure cancels siblings/parent hierarchy
    - `SupervisorJob` → child failure is isolated
    Use `SupervisorJob` when independent child tasks should not take each
    other down.
    This is a common senior-level coroutine interview question.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/structured-concurrency-and-jobs/#job-vs-supervisorjob">🚀 See Full Deep Dive</a>


---

<div id="async-vs-launch"></div>

## What is the difference between launch and async in coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">concurrency</span>
</div>

??? question "View Answer"

    `launch` starts a coroutine that returns `Job`.
    `async` starts a coroutine that returns `Deferred<T>`.
    Use:
    - `launch` for fire-and-join style work
    - `async` when a result is needed
    Interview nuance:
    `async` is not automatically better for parallelism.
    It should be used when structured result handling is needed.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/structured-concurrency-and-jobs/#async-vs-launch">🚀 See Full Deep Dive</a>


---

<div id="job-hierarchy"></div>

## How does coroutine job hierarchy work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">jobs</span>
</div>

??? question "View Answer"

    Every coroutine has a `Job` in its context.
    Parent-child hierarchy controls:
    - cancellation propagation
    - completion waiting
    - exception handling behavior
    In structured concurrency:
    - parent waits for children
    - child cancellation can affect parent depending on job type
    Understanding job hierarchy is key to debugging coroutine behavior.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/structured-concurrency-and-jobs/#job-hierarchy">🚀 See Full Deep Dive</a>


---

<div id="coroutine-cancellation"></div>

## How does cancellation work in Kotlin Coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">cancellation</span>
</div>

??? question "View Answer"

    Coroutine cancellation is cooperative.
    That means code must reach suspension points or explicitly check for
    cancellation to stop promptly.
    Common tools:
    - `isActive`
    - `ensureActive()`
    - `yield()`
    - cancellable suspending functions
    Blocking code that ignores cancellation is a common production bug.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/cancellation-and-exception-handling/#coroutine-cancellation">🚀 See Full Deep Dive</a>


---

<div id="coroutine-exception-handling"></div>

## How are exceptions handled in Kotlin Coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">exceptions</span>
</div>

??? question "View Answer"

    Exception handling depends on coroutine builder type and hierarchy.
    Key ideas:
    - `launch` surfaces failures differently than `async`
    - parent-child structure matters
    - `CoroutineExceptionHandler` only handles uncaught exceptions
    - supervisor-style scopes isolate failures
    Interview answer should focus on propagation rules, not just try/catch.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/cancellation-and-exception-handling/#coroutine-exception-handling">🚀 See Full Deep Dive</a>


---

<div id="flow-what-is"></div>

## What is Flow in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">async-streams</span>
</div>

??? question "View Answer"

    Flow is Kotlin's cold asynchronous stream API.
    It is used for:
    - reactive pipelines
    - database observation
    - UI state transformation
    - incremental async values
    Important properties:
    - cold by default
    - sequential by default
    - coroutine-based
    - cancellation-aware
    Flow is central to modern Android state handling.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/flow-fundamentals/#flow-what-is">🚀 See Full Deep Dive</a>


---

<div id="cold-vs-hot-flow"></div>

## What is the difference between cold and hot streams in Kotlin?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">reactive</span>
</div>

??? question "View Answer"

    Cold streams start producing values per collector.
    Hot streams can emit independently of collectors.
    In Kotlin:
    - `Flow` is usually cold
    - `StateFlow` and `SharedFlow` are hot
    Interview framing:
    the difference is about producer lifecycle and sharing behavior,
    not just API names.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/flow-fundamentals/#cold-vs-hot-flow">🚀 See Full Deep Dive</a>


---

<div id="stateflow-vs-sharedflow"></div>

## What is the difference between StateFlow and SharedFlow?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">stateflow</span>
</div>

??? question "View Answer"

    `StateFlow` is for holding and exposing current state.
    `SharedFlow` is for broadcasting events or shared emissions.
    Quick comparison:
    - `StateFlow` always has a current value
    - `SharedFlow` can be configured for replay/buffering
    - `StateFlow` is state-oriented
    - `SharedFlow` is event/broadcast-oriented
    Choosing the wrong one often causes UI event bugs.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/stateflow-sharedflow-and-channels/#stateflow-vs-sharedflow">🚀 See Full Deep Dive</a>


---

<div id="channels-vs-sharedflow"></div>

## When should you use a Channel instead of SharedFlow?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">channels</span>
  <span class="question-badge question-badge--tag">flow</span>
</div>

??? question "View Answer"

    Channels are point-to-point communication primitives.
    SharedFlow is a broadcast-style hot stream.
    Use Channel when:
    - send/receive semantics matter
    - backpressure and buffering behavior are central
    - you need queue-like communication
    Use SharedFlow when multiple collectors should observe emissions.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/stateflow-sharedflow-and-channels/#channels-vs-sharedflow">🚀 See Full Deep Dive</a>


---

<div id="mutex-in-kotlin"></div>

## What is Mutex in Kotlin Coroutines and when should you use it?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">synchronization</span>
</div>

??? question "View Answer"

    `Mutex` is a coroutine-friendly mutual exclusion primitive.
    It is used to protect shared mutable state without blocking a thread.
    Use it when:
    - multiple coroutines update shared data
    - atomic updates are needed
    - thread-safe state transitions matter
    Interview detail:
    `Mutex` suspends waiting coroutines instead of blocking a thread.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/stateflow-sharedflow-and-channels/#mutex-in-kotlin">🚀 See Full Deep Dive</a>


---

<div id="kotlin-jvm-interoperability"></div>

## How does Kotlin interoperate with Java on the JVM?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">jvm</span>
  <span class="question-badge question-badge--tag">interop</span>
</div>

??? question "View Answer"

    Kotlin is designed for strong Java interoperability.
    It supports:
    - calling Java code directly
    - exposing Kotlin APIs to Java
    - sharing JVM libraries and tooling
    Common interop concerns:
    - nullability
    - checked exceptions
    - default arguments
    - static-like APIs
    - SAM conversions
    Good Kotlin interview answers usually mention both syntax and JVM impact.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/jvm-interop-and-bytecode/#kotlin-jvm-interoperability">🚀 See Full Deep Dive</a>


---

<div id="kotlin-bytecode-basics"></div>

## What should you know about Kotlin bytecode for interviews?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">bytecode</span>
  <span class="question-badge question-badge--tag">jvm</span>
</div>

??? question "View Answer"

    Kotlin source compiles to JVM bytecode, often with generated helper
    classes and methods that do not appear in source code.
    Important interview topics:
    - null-check generation
    - synthetic/default helper methods
    - lambda class generation
    - inline call-site expansion
    - suspend state machine generation
    Bytecode knowledge helps explain performance and interoperability.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/jvm-interop-and-bytecode/#kotlin-bytecode-basics">🚀 See Full Deep Dive</a>


---

<div id="suspend-state-machine"></div>

## How are coroutines compiled into a state machine?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">kotlin</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">bytecode</span>
</div>

??? question "View Answer"

    The compiler rewrites suspend code into a state machine that tracks the
    current execution label and continuation.
    At each suspension point:
    - local state may be stored
    - execution label is updated
    - continuation resumes later from the right state
    This explains how coroutines appear sequential while remaining resumable.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/kotlin/jvm-interop-and-bytecode/#suspend-state-machine">🚀 See Full Deep Dive</a>

