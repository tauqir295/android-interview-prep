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
## Delegation and Delegated Properties Deep Dive

## Overview

Delegation is one of Kotlin's strongest language features for reducing boilerplate and favoring composition.

---

## Core Concepts

### Class delegation

```kotlin
interface Printer {
    fun print()
}

class ConsolePrinter : Printer {
    override fun print() = println("print")
}

class Screen(printer: Printer) : Printer by printer
```

This forwards interface implementation automatically.

### Property delegation

```kotlin
val config by lazy { loadConfig() }
```

The delegate owns access behavior.

---

## Internal Implementation

Delegated properties are compiled into calls to delegate operators such as:

- `getValue()`
- `setValue()`

Class delegation similarly becomes generated forwarding methods.

So Kotlin removes boilerplate, but the underlying implementation still uses regular method calls and generated glue.

---

## JVM / Compiler Behavior

`lazy` uses a delegate implementation chosen by thread-safety mode.

Common modes:

- synchronized (default)
- publication
- none

This matters in interview discussions because “lazy” behavior is not one-size-fits-all.

---

## Code Examples

### `lazy`

```kotlin
val repository by lazy(LazyThreadSafetyMode.NONE) {
    UserRepository()
}
```

### Observable property

```kotlin
var count: Int by Delegates.observable(0) { _, old, new ->
    println("$old -> $new")
}
```

---

## Common Interview Questions

- Why is delegation better than inheritance here?
- How does `lazy` behave with threads?
- What methods must a custom delegate implement?

---

## Production Considerations

Delegation is excellent for:

- reusable behaviors
- view binding style patterns
- state observation
- lightweight wrappers

But hidden magic can hurt readability if overused.

---

## Performance Insights

Delegation reduces manual boilerplate but still introduces generated calls.
In most app code the clarity benefit outweighs the tiny indirection cost.

---

## Senior-Level Insights

Strong candidates explain delegation as a language-supported composition mechanism, not just “syntactic sugar.”
That distinction matters in architecture discussions.

