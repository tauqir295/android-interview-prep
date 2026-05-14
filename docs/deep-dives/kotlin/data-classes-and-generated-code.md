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
# Data Classes and Generated Code Deep Dive

## Overview

Data classes are Kotlin's value-oriented modeling tool. They remove boilerplate while making equality, debugging, and copying semantics explicit.

---

## Core Concepts

A data class is best when the object primarily represents data rather than identity-heavy behavior.

```kotlin
data class User(
    val id: Long,
    val name: String
)
```

Kotlin generates:

- `equals()`
- `hashCode()`
- `toString()`
- `copy()`
- `componentN()`

---

## Internal Implementation

The compiler only uses properties in the primary constructor for generated member behavior.

```kotlin
data class Session(val token: String) {
    var isExpired: Boolean = false
}
```

Here:

- `token` participates in equality/hash/copy
- `isExpired` does not

That is an important interview trap.

---

## JVM / Compiler Behavior

Kotlin data classes compile to normal JVM classes with generated methods.

Conceptually, the compiler emits methods similar to:

```kotlin
override fun equals(other: Any?): Boolean
override fun hashCode(): Int
override fun toString(): String
fun copy(id: Long = this.id, name: String = this.name): User
operator fun component1(): Long
operator fun component2(): String
```

Default arguments in `copy()` also generate additional helper methods on JVM.

---

## Code Examples

### Copying immutable state

```kotlin
data class UiState(
    val loading: Boolean,
    val title: String
)

val oldState = UiState(loading = true, title = "Home")
val newState = oldState.copy(loading = false)
```

### Destructuring

```kotlin
val user = User(1L, "Mina")
val (id, name) = user
```

---

## Common Interview Questions

- What gets included in generated equality?
- Is a data class automatically immutable?
- Why is `copy()` useful in Android UI state?
- When should you avoid data classes?

---

## Production Considerations

Use data classes for:

- UI state
- API models
- cached domain values
- immutable state containers

Avoid overusing them for objects with strong identity/lifecycle semantics.

---

## Performance Insights

Data classes are usually efficient enough, but beware of:

- repeated `copy()` on large nested graphs
- accidental deep-state churn in UI reducers
- large generated `toString()` logs in hot paths

---

## Senior-Level Insights

The strongest interview answers distinguish:

- value semantics vs identity semantics
- generated convenience vs real allocation cost
- immutable state modeling vs mutable entities

That distinction matters heavily in Android architecture and state management.

