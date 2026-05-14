---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/networking/">← Back to Networking</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/networking/${hash}`);
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

## Multipart Uploads Deep Dive

## Overview
Multipart requests handle mixed binary/text data.
## Core Concepts
Use @Multipart @Part annotations in Retrofit.
## Code Examples
```kotlin
@Multipart
@POST("upload")
suspend fun uploadFile(
    @Part("description") description: RequestBody,
    @Part file: MultipartBody.Part
): Response
// Usage
val file = File(path)
val requestBody = file.asRequestBody("image/jpeg".toMediaType())
val part = MultipartBody.Part.createFormData("file", file.name, requestBody)
val description = "My image".toRequestBody("text/plain".toMediaType())
api.uploadFile(description, part)
```
## Senior-Level Insights
- Chunk large files
- Implement upload progress
- Resume capability for large uploads
