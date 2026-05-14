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
    // Keep default fundamentals link if URL parsing fails.
  }
})();
</script>

# Storage Types Deep Dive

## Overview

Android offers multiple storage options with different security, structure, and sharing behavior. Choosing the right one is a common interview topic.

---

## Storage Options

### SharedPreferences / DataStore

- Key-value preferences.
- Best for flags/settings.
- For modern apps, prefer `DataStore` over legacy preferences APIs.

### Internal Storage

- App-private files.
- Removed on uninstall.
- Good for private cached or persisted files.

### External/Scoped Storage

- Shared media/documents model.
- Scoped storage rules apply on modern Android.
- Use MediaStore / SAF depending on use case.

### Room/SQLite

- Structured relational data.
- Queryable and transactional.
- Best for offline-first and complex domain models.

### Cache Directories

- Temporary, reclaimable by system.
- Never store critical data only in cache.

---

## Selection Guide

- Settings -> DataStore/SharedPreferences
- Structured domain data -> Room
- User-visible media -> MediaStore
- Temporary payloads -> Cache

---

## Interview Traps

- Assuming external storage is always globally readable/writable.
- Storing large structured data in preferences.
- Ignoring migration/backup strategy.

---

## Key Takeaways

- Match storage choice to data lifetime and access pattern.
- Prefer modern APIs (Room, DataStore, scoped media APIs).

