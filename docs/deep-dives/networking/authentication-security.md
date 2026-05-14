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

## Authentication & Security Deep Dive

## Overview
Authentication proves identity. Securely integrating auth into mobile is critical for production systems.

## Core Concepts

### JWT (JSON Web Tokens)

Structure: `header.payload.signature`

Contains:
- `exp`: expiration timestamp
- `sub`: subject (user ID)
- `iat`: issued at time
- custom claims

### OAuth 2.0 for Mobile

Authorization code flow (for third-party login):

1. App opens browser to provider
2. User grants permission
3. Provider sends authorization code
4. App exchanges code for token
5. App can now access resources

### Secure Token Storage

Never hardcode or store in plain SharedPreferences:

```kotlin
// Use EncryptedSharedPreferences
val encryptedPrefs = EncryptedSharedPreferences.create(
    context,
    "secret",
    MasterKey.Builder(context).build(),
    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
)

encryptedPrefs.edit().putString("auth_token", token).commit()
```

## Internal Implementation

### Token Refresh Flow

When token expires:

```kotlin
class TokenRefreshingInterceptor : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val response = chain.proceed(chain.request())
        
        if (response.code == 401) {
            synchronized(this) {
                val newToken = refreshToken()
                response.close()
                return chain.proceed(addToken(chain.request(), newToken))
            }
        }
        return response
    }
}
```

## Request/Response Flow

1. User logs in with credentials
2. Server validates, returns tokens
3. Access token stored securely
4. Refresh token stored separately (longer TTL)
5. All requests include access token
6. On 401, refresh flow triggered

## Code Examples

### JWT Token Structure

```kotlin
// Manually decode (never verify without server)
val parts = token.split(".")
val payload = String(Base64.getDecoder().decode(parts[1]))
// {"sub":"user123","exp":1640000000,"iat":1640000000}
```

### OkHttp Auth Interceptor

```kotlin
class AuthInterceptor(tokenProvider: TokenProvider) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val originalRequest = chain.request()
        val token = tokenProvider.getToken()
        
        val authenticatedRequest = originalRequest.newBuilder()
            .addHeader("Authorization", "Bearer $token")
            .build()
        
        return chain.proceed(authenticatedRequest)
    }
}
```

## Common Interview Questions

**Q: Should tokens be refreshed proactively?**
A: Yes, refresh shortly before expiration to avoid race conditions.

**Q: Can JWT be revoked?**
A: Client can't know. Server maintains blacklist or uses short TTL.

**Q: Is PKCE required for mobile?**
A: Yes for OAuth. Mobile can't keep secrets, so code challenge/verifier used.

## Production Considerations

### Token Lifetimes

- Access: 15-60 min (short, limited damage if leaked)
- Refresh: 7-30 days (enables long sessions)
- ID token (if OAuth): short like access

### Multi-Account Support

Some apps support multiple accounts:

```kotlin
// Store tokens per user ID
val userTokens = mapOf(
    "user1" -> token1,
    "user2" -> token2
)

fun selectAccount(userId: String) {
    currentToken = userTokens[userId]
}
```

## Performance Insights

### Cache Tokens in Memory

Avoid repeated disk access:

```kotlin
private var tokenCache: String? = null
private var cacheTime: Long = 0

fun getToken(): String {
    if (System.currentTimeMillis() - cacheTime < 5000) {
        return tokenCache!!  // recent cache
    }
    tokenCache = loadFromDisk()
    cacheTime = System.currentTimeMillis()
    return tokenCache!!
}
```

## Senior-Level Insights

### Device Binding for Security

Link tokens to device to prevent theft:

```kotlin
val deviceId = Settings.Secure.getString(
    context.contentResolver,
    Settings.Secure.ANDROID_ID
)

// Include in token or sign with device key
```

### Biometric Integration

Protect token access with fingerprint/face:

```kotlin
BiometricPrompt(this, executor, callback).authenticate(promptInfo)
// Only on success do we unlock token
```
