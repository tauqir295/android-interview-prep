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
## AndroidManifest Deep Dive

## Overview

`AndroidManifest.xml` declares app identity, components, permissions, and capabilities so Android can install and run your app correctly.

---

## Core Sections

- `<manifest>`: package, version metadata.
- `<application>`: app-wide attributes (theme, label, icon, backup, etc).
- Component declarations:
  - `<activity>`
  - `<service>`
  - `<receiver>`
  - `<provider>`
- `<uses-permission>` and `<uses-feature>`

---

## Intent Filters

```xml
<activity android:name=".MainActivity" android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

- `MAIN + LAUNCHER` marks app entry activity.
- For deep links, use `VIEW + BROWSABLE + DEFAULT` with `<data .../>`.

---

## Exported Rules

- Android 12+ requires explicit `android:exported` for components with intent filters.
- Set `false` unless external access is required.

---

## Manifest Merge

Build tools merge manifests from:
- app module
- library modules
- build variants/flavors

Use `tools:` attributes to resolve conflicts.

---

## Interview Traps

- Missing `android:exported` causes install/build errors on modern SDKs.
- Wrong intent filter can unintentionally expose components.
- Manifest permissions are not enough for dangerous APIs; runtime request still required.

---

## Key Takeaways

- Manifest is app contract with Android OS.
- Keep declarations minimal and explicit.
- Validate exported surface area and deep link intent filters carefully.

