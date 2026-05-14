---
hide:
  - toc
---
!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/fundamentals/">← Back to Fundamentals</a>
<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/fundamentals/${hash}`);
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
## RecyclerView Efficiency Deep Dive

## Overview

RecyclerView is efficient because it reuses view holders, minimizes view inflation, and delegates layout/animations to specialized components.

---

## Why RecyclerView Beats ListView

- ViewHolder pattern is first-class.
- Better recycling and pooling.
- Flexible `LayoutManager` implementations.
- Built-in animation and diff-friendly update patterns.

---

## Core Components

- `RecyclerView`
- `Adapter`
- `ViewHolder`
- `LayoutManager`
- Optional `ItemAnimator` and `ItemDecoration`

---

## Performance Practices

- Use `ListAdapter` + `DiffUtil`.
- Keep `onBindViewHolder()` lightweight.
- Avoid nested heavy layouts in item XML.
- Use stable IDs when appropriate.
- Pre-size image requests and cache aggressively.

```kotlin
class UserAdapter : ListAdapter<User, UserVH>(UserDiff()) {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserVH =
        UserVH(ItemUserBinding.inflate(LayoutInflater.from(parent.context), parent, false))

    override fun onBindViewHolder(holder: UserVH, position: Int) {
        holder.bind(getItem(position))
    }
}
```

---

## Interview Traps

- Calling `notifyDataSetChanged()` too often hurts performance.
- Doing expensive formatting or image decoding in bind causes jank.

---

## Key Takeaways

- RecyclerView performance is mostly about efficient bind work and diffed updates.
- Good item layout design matters as much as adapter logic.

