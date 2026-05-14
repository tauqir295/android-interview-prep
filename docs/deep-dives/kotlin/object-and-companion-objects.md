---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/kotlin/">← Back to Kotlin</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/kotlin/${hash}`);
      return;
    }
    const referrer = document.referrer || "";
    if (referrer.includes("/android-interview-prep/generated/")) {
      link.setAttribute("href", referrer);
    }
  } catch (_) {}
})();
</script>

# Object and Companion Objects Deep Dive

## Overview

Kotlin's `object` keyword covers several patterns:

- singleton declarations
- anonymous object expressions
- companion objects

Interviewers often test whether you understand both the syntax and the runtime differences.

---

## Core Concepts

### Object declaration

```kotlin
object Logger {
    fun log(message: String) = println(message)
}
```

- named singleton
- lazily initialized on first access
- useful for stateless shared utilities

### Object expression

```kotlin
val listener = object : Runnable {
    override fun run() = println("run")
}
```

- anonymous object
- created immediately
- often used for local callbacks

### Companion object

```kotlin
class User {
    companion object {
        const val TABLE = "users"
    }
}
```

- tied to a class
- often used for factories/constants
- Kotlin alternative to many Java static use cases

---

## Internal Implementation

Companion objects are still real objects.
They are not magical static blocks.

That means they can:

- implement interfaces
- hold state
- contain functions
- be referenced as objects

```kotlin
class FactoryHolder {
    companion object Factory : Comparator<Int> {
        override fun compare(a: Int, b: Int): Int = a - b
    }
}
```

---

## JVM / Compiler Behavior

On JVM, Kotlin often generates a companion instance field plus methods.

With annotations like `@JvmStatic`, interop can become more Java-friendly.

Interview nuance:

- companion objects are object instances
- Java statics are class-level members
- the call style may look similar, but the compiled model differs

---

## Code Examples

### Factory pattern

```kotlin
class User private constructor(val id: Long) {
    companion object {
        fun fromId(id: Long): User = User(id)
    }
}
```

### Anonymous object for one-off behavior

```kotlin
fun makeRunnable(): Runnable {
    return object : Runnable {
        override fun run() = println("working")
    }
}
```

---

## Common Interview Questions

- Is a companion object the same as `static`?
- When is an object declaration initialized?
- What is lost when returning an anonymous object from a public API?

---

## Production Considerations

Use object declarations for:

- stateless helpers
- shared formatters
- singleton configuration readers

Avoid hidden global mutable state unless truly necessary.

---

## Performance Insights

The main concern is usually not speed but initialization and hidden state.
Singleton misuse can quietly turn into global coupling.

---

## Senior-Level Insights

Strong answers emphasize:

- object forms model different intent
- companion objects are still objects
- singletons simplify access but can hurt testability if overused

