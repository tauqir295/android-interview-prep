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
# Permissions Deep Dive

## Overview

Android permissions protect user data and sensitive device capabilities. Modern Android uses runtime permission prompts for dangerous permissions.

---

## Permission Categories

- **Normal**: auto-granted at install time.
- **Dangerous**: runtime user consent required.
- **Signature**: granted only to apps signed with same certificate.
- **Special**: managed through settings screens (e.g., overlay).

---

## Runtime Permission Flow

```kotlin
private val requestCamera = registerForActivityResult(
    ActivityResultContracts.RequestPermission()
) { granted ->
    if (granted) openCamera() else showPermissionRationaleOrFallback()
}

fun ensureCameraPermission() {
    when {
        ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) ==
            PackageManager.PERMISSION_GRANTED -> openCamera()
        shouldShowRequestPermissionRationale(Manifest.permission.CAMERA) -> showRationale()
        else -> requestCamera.launch(Manifest.permission.CAMERA)
    }
}
```

---

## Best Practices

- Ask only when feature is about to be used.
- Explain user value clearly before prompt.
- Gracefully degrade if denied.
- Re-check permission before every sensitive action.

---

## Android Version Notes

- Android 6.0 introduced runtime model.
- Scoped storage and media permissions evolved in Android 10+.
- Android 13 split media permissions by type (`READ_MEDIA_IMAGES`, etc).

---

## Common Mistakes

- Requesting many permissions at startup.
- Assuming previously granted permissions remain granted forever.
- Crashing on denial instead of fallback UX.

---

## Key Takeaways

- Permission handling is part of product UX, not just API usage.
- Keep requests contextual, minimal, and reversible.
- Always code for denial paths.

