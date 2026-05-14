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

# Collections and Sequences Deep Dive

## Overview

Kotlin collections are highly expressive, but interview discussions often focus on eagerness, allocation behavior, and immutability semantics.

---

## Core Concepts

Common operations:

- `map`
- `filter`
- `flatMap`
- `groupBy`
- `associate`

Key nuance:

- `List<T>` is read-only from that API surface
- it is not necessarily deeply immutable

Sequences differ because they are lazy.

---

## Internal Implementation

Collection chains usually allocate intermediate collections.
Sequence chains defer work and process lazily.

That means sequences can reduce allocations, but also add iterator/lazy overhead.

---

## JVM / Compiler Behavior

The compiler does not magically optimize every chain away.
Standard library operations still correspond to loops, lambdas, and allocated containers depending on API choice.

---

## Code Examples

```kotlin
val names = users
    .filter { it.active }
    .map { it.name }
```

```kotlin
val names = users.asSequence()
    .filter { it.active }
    .map { it.name }
    .toList()
```

---

## Common Interview Questions

- When should you use `Sequence`?
- Are Kotlin collections immutable?
- Why can operator chains become allocation-heavy?

---

## Production Considerations

Use collection chains for readable business logic.
Switch to sequences only when dataset size and allocation pressure justify it.

---

## Performance Insights

- small collections: eager collections are often fine
- large pipelines: sequences may help
- hot paths: benchmark rather than assume

---

## Senior-Level Insights

Strong answers avoid blanket rules like “Sequence is always faster.” Context matters.

