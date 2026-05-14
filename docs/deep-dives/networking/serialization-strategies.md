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

## Serialization Strategies Deep Dive

## Overview
Serialization converts Kotlin objects to/from JSON. Performance and flexibility vary across libraries.

## Core Concepts

### Serialization Libraries

**Gson (Google):**
- Reflection-based
- Flexible, lenient parsing
- No compile-time checks
- mature, widely used

**Moshi (Square):**
- Reflection + type adapters
- Customizable parsing
- Better error messages
- faster than Gson

**Kotlin Serialization (JetBrains):**
- Compiler plugin generates code
- No reflection needed
- Compile-time safety
- Newer, growing adoption

## Internal Implementation

### Gson vs Moshi vs Kotlin Serialization Comparison

| Aspect | Gson | Moshi | Kotlin Serialization |
|--------|------|-------|----------------------|
| Speed | 250μs | 150μs | 50μs |
| Reflection | Yes | Partial | No |
| Type Safety | Runtime | Runtime | Compile-time |
| Error Messages | Good | Excellent | Good |
| Setup | Easy | Medium | Medium |

## Request/Response Flow

1. OkHttp receives response bytes
2. Retrofit converter deserializes
3. Object passed to collecting flow/callback

## Code Examples

### Custom Gson Serializer

```kotlin
data class User(val id: Int, val createdAt: Date)

class DateSerializer : JsonSerializer<Date>,
    JsonDeserializer<Date> {
    private val fmt = SimpleDateFormat("yyyy-MM-dd")
    
    override fun serialize(src: Date?, typeOfSrc: Type?,
        context: JsonSerializationContext?) = JsonPrimitive(fmt.format(src))
    
    override fun deserialize(json: JsonElement?, typeOfT: Type?,
        context: JsonDeserializationContext?) = 
        fmt.parse(json?.asString ?: "")
}
```

## Common Interview Questions

**Q: Why is Kotlin Serialization faster?**
A: Compiler generates code instead of using reflection at runtime.

**Q: Should I migrate from Gson?**
A: Only if performance is critical. Gson ecosystem is larger.

## Production Considerations

### Backwards Compatibility

When API adds fields:

```kotlin
@Serializable
data class User(
    val id: Int,
    val name: String,
    @Transient  // skip serialization
    val newFeature: String = "default"
)
```

## Performance Insights

### Caching Serializers

Create serializers once:

```kotlin
val gson = GsonBuilder()
    .registerTypeAdapter(...)
    .build()

// reuse
val user = gson.fromJson(json, User::class.java)
```

## Senior-Level Insights

### Version Stability

Track API schema versions:

```kotlin
// v1 field removed, v2 added
if (apiVersion >= 2) {
    useNewField()
}
```
