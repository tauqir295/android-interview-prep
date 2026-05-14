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
## Null Safety and Smart Casts Deep Dive

## Overview

Null safety is one of Kotlin's biggest value propositions. It moves many null-related problems from runtime into the type system.

---

## Core Concepts

Kotlin distinguishes:

- `String` → non-nullable
- `String?` → nullable

Main tools:

- safe call `?.`
- Elvis `?:`
- not-null assertion `!!`
- smart casts after checks

---

## Internal Implementation

Kotlin null safety is mostly compiler enforced. The type system tracks nullable vs non-nullable references and emits checks where needed.

Platform types from Java weaken these guarantees because nullability may be unknown at compile time.

---

## JVM / Compiler Behavior

The compiler often inserts runtime null-checks for parameters and assumptions, especially around Java interop and non-null contracts.

Smart casts rely on flow analysis. They work only when the compiler can prove the reference is stable.

---

## Code Examples

```kotlin
val name: String? = input()
val length = name?.length ?: 0
```

```kotlin
if (value is String) {
    println(value.length) // smart cast
}
```

---

## Common Interview Questions

- Why can null still happen in Kotlin?
- What is a platform type?
- When do smart casts fail?
- Why is `!!` dangerous?

---

## Production Considerations

- avoid `!!` unless failure is intentional
- make nullability explicit in public APIs
- be careful at Java boundaries
- prefer safe transformations to assertions

---

## Performance Insights

Null safety is primarily a correctness feature. Runtime cost is usually minor compared with the stability benefit.

---

## Senior-Level Insights

Good candidates explain that Kotlin reduces null problems significantly, but cannot eliminate them when unsafe assertions, Java interop, reflection, or poor API design are involved.

