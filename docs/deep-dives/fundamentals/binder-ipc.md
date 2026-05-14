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

# Binder IPC Deep Dive

## Overview

Binder is Android's high-performance IPC mechanism enabling communication between processes (apps and system services) with identity and permission checks.

---

## Binder Model

- **Client** calls interface methods.
- **Kernel binder driver** transfers parcels safely.
- **Server** handles transactions on binder thread pool.

---

## AIDL Flow

1. Define `.aidl` interface.
2. Build generates Stub/Proxy classes.
3. Service implements Stub.
4. Client binds and calls methods through Proxy.

```kotlin
interface IRemoteService {
    fun getUserName(id: Int): String
}
```

---

## Parceling

- Data sent through `Parcel`.
- Prefer primitives/Parcelable for performance.
- Avoid large payloads; pass IDs and fetch from shared source where possible.

---

## Security

- Binder tracks caller UID/PID.
- Validate caller permissions in service.
- Exported bound services should enforce explicit auth checks.

---

## Interview Highlights

- Why Binder over sockets? (performance + framework integration)
- What is thread pool behavior on service side?
- Difference between in-process binding vs cross-process AIDL?

---

## Key Takeaways

- Binder is the backbone of Android IPC.
- AIDL is needed for typed cross-process contracts.
- Security and payload size are critical design points.

