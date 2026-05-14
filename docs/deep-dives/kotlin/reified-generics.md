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
# Reified Generics Deep Dive

## Overview

Reified generics are one of Kotlin's most interview-worthy features because they connect language syntax to JVM type erasure and compiler inlining.

---

## Core Concepts

Normally, JVM generics are erased at runtime.

Kotlin solves some of that limitation with reified type parameters in inline functions:

```kotlin
inline fun <reified T> Any.isType(): Boolean = this is T
```

---

## Internal Implementation

Because the function is inlined, the compiler can substitute real type checks at the call site.

That is why this is possible only inside `inline` functions.

---

## JVM / Compiler Behavior

Without reified support, this is not possible safely:

```kotlin
fun <T> check(value: Any): Boolean {
    // cannot use `is T` here normally
    return false
}
```

With reified:

```kotlin
inline fun <reified T> check(value: Any): Boolean = value is T
```

---

## Code Examples

```kotlin
inline fun <reified T> Gson.fromJsonTyped(json: String): T {
    return fromJson(json, T::class.java)
}
```

---

## Common Interview Questions

- Why does reified require inline?
- How does it relate to type erasure?
- When is reified more useful than reflection?

---

## Production Considerations

Reified generics improve API ergonomics, but still depend on JVM/runtime limits. They are especially useful for utility libraries and framework helpers.

---

## Performance Insights

The main tradeoff is still inline-related bytecode duplication, not magic runtime cost.

---

## Senior-Level Insights

Strong answers connect reified generics to compiler substitution, not just “Kotlin can access generic types at runtime.” The mechanism matters.

