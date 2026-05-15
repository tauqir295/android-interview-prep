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
  } catch (_) {
    // Keep default generated page link if URL parsing fails.
  }
})();
</script>
## Generics and Variance Deep Dive

## Overview

Kotlin generics improve type safety, but their most important interview topics are variance and type erasure.

---

## Core Concepts

Generics let APIs work across different types safely:

```kotlin
class Box<T>(val value: T)
```

Variance controls subtype relationships:

- `out` = producer
- `in` = consumer

Star projection (`*`) represents an unknown type argument safely.

---

## Internal Implementation

On JVM, generic type arguments are largely erased at runtime.
That means many generic guarantees exist mainly at compile time.

This is why runtime checks and reified solutions matter.

---

## JVM / Compiler Behavior

### Covariance

```kotlin
interface Source<out T>
```

### Contravariance

```kotlin
interface Consumer<in T>
```

### Star projection

```kotlin
val list: List<*> = listOf("a", "b")
```

Kotlin avoids Java-style raw type ambiguity by making unknown generic usage safer.

---

## Code Examples

```kotlin
fun copyAll(from: List<out Number>, to: MutableList<in Number>) {
    from.forEach { to.add(it) }
}
```

---

## Common Interview Questions

- **Q:** What is variance?
  **A:** Tie Kotlin language features to production outcomes: safety, readability, testability, and runtime or allocation tradeoffs when relevant.
- **Q:** What is the producer/consumer rule?
  **A:** Tie Kotlin language features to production outcomes: safety, readability, testability, and runtime or allocation tradeoffs when relevant.
- **Q:** Why does type erasure matter?
  **A:** Tie Kotlin language features to production outcomes: safety, readability, testability, and runtime or allocation tradeoffs when relevant.
- **Q:** Why is `List<String>` not automatically `List<Any>`?
  **A:** Tie Kotlin language features to production outcomes: safety, readability, testability, and runtime or allocation tradeoffs when relevant.

---
## Production Considerations

Variance improves API correctness, especially in libraries and architecture boundaries. Poor variance choices can make APIs painful or unsafe.

---

## Performance Insights

The main cost is not performance but complexity. The challenge is making APIs type-safe without making them unreadable.

---

## Senior-Level Insights

Strong answers connect generic theory to real API design:

- safe library surfaces
- better abstraction boundaries
- reduced casting
- more predictable contracts

