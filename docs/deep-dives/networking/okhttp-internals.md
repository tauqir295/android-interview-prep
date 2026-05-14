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

## OkHttp Internals Deep Dive

## Overview

OkHttp is the HTTP client layer that Retrofit delegates to. Understanding OkHttp's architecture is critical for production networking engineering on Android.

## Core Concepts

### Request/Response Lifecycle

1. Application creates `Request`
2. Interceptor chain processes
3. Connection pool consulted
4. TCP connection established or reused
5. TLS handshake if HTTPS
6. HTTP request sent
7. Response received and parsed
8. Interceptor chain (response phase)
9. Response returned to caller

### Interceptor Chain Architecture

OkHttp maintains two interceptor chains:

**Application Interceptors:**
- See only your application's original request
- Not called for retries or redirects
- Perfect for logging, auth injection
- Can short-circuit (return cached response)

**Network Interceptors:**
- See actual network traffic including redirects
- final `response` before actual network call
- Can measure real latency
- for debugging actual HTTP

## Internal Implementation

### Connection Pooling

OkHttp reuses connections via a pool:

```kotlin
OkHttpClient.Builder()
    .connectionPool(ConnectionPool(
        maxIdleConnections = 5,
        keepAliveDuration = 5, TimeUnit.MINUTES
    ))
    .build()
```

Pool keyed by: `host:port:scheme`

Benefits:
- reduces TLS handshakes
- improves throughput
- reduces battery usage

### Call Mechanics

Under the hood, synchronous `Call`:

```kotlin
interface Call <T> {
    fun execute(): Response<T>  // blocking
    fun enqueue(callback: Callback<T>)  // async
    fun clone(): Call<T>
    fun cancel()
}
```

Retrofit adapters convert this to `suspend` or `Flow`.

## Request/Response Flow

### Request Path

1. Application calls `retrofit.userService.getUser(1)`
2. Proxy method intercepts via dynamic code gen
3. RequestBuilder creates HTTP request
4. Retrofit passes to OkHttp Call
5. Application interceptors run
6. Connection pool consulted
7. If new connection: DNS → TCP → TLS
8. Request written to socket
9. Network interceptors run
10. Response read from socket
11. Converter deserializes JSON to object

### Response Path (Reverse)

Response flows back through interceptors in reverse (post-processing).

## Code Examples

### Custom Application Interceptor (Auth)

```kotlin
class AuthInterceptor : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val original = chain.request()
        val token = getToken()  // from storage
        
        val authenticated = original.newBuilder()
            .addHeader("Authorization", "Bearer $token")
            .build()
        
        return chain.proceed(authenticated)
    }
}

val httpClient = OkHttpClient.Builder()
    .addInterceptor(AuthInterceptor())
    .build()
```

### Retry Interceptor

```kotlin
class RetryInterceptor : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        var request = chain.request()
        var exception: IOException? = null
        
        repeat(3) { attempt ->
            try {
                return chain.proceed(request)
            } catch (e: IOException) {
                exception = e
                Thread.sleep(100L * (2.0).pow(attempt.toDouble()).toLong())
            }
        }
        
        throw exception ?: IOException("retry failed")
    }
}
```

## Common Interview Questions

**Q: Why does OkHttp cache connections?**
A: TLS handshakes are expensive (~100ms each). Reusing connections amortizes that cost.

**Q: What's the difference between application and network interceptors?**
A: Application interceptors see redirects as one flow. Network interceptors see each redirect as separate call.

**Q: Can you short-circuit OkHttp?**
A: Yes, via application interceptor returning a cached response without calling `chain.proceed()`.

## Production Considerations

### Timeouts Are Essential

```kotlin
OkHttpClient.Builder()
    .connectTimeout(30, TimeUnit.SECONDS)
    .readTimeout(30, TimeUnit.SECONDS)
    .writeTimeout(30, TimeUnit.SECONDS)
    .callTimeout(60, TimeUnit.SECONDS)  // includes retries
    .build()
```

Missing timeouts = potential ANRs on network hang.

### Connection Pool Size

Default: 5 idle connections, 5 minute keep-alive.

For high-throughput apps, increase:
```kotlin
ConnectionPool(maxIdleConnections = 10, keepAliveDuration = 5, TimeUnit.MINUTES)
```

### DNS Caching

OkHttp doesn't cache DNS by default. For production reliability:

```kotlin
class HostnameVerifier : HostnameVerifier {
    private val systemVerifier = HttpsURLConnection.getDefaultHostnameVerifier()
    
    override fun verify(hostname: String, session: SSLSession) =
        systemVerifier.verify(hostname, session)
}
```

## Performance Insights

### Interceptor overhead

Each interceptor adds slight latency. Minimize number of interceptors.

### Connection reuse > new connections

- New connection: ~150-300ms (TLS on 4G)
- Reused connection: ~5-10ms

Massive difference on recursive API calls.

### Memory usage

Connection pools consume memory. Monitor:
- active connections
- idle connections
- buffer sizes

## Senior-Level Insights

### Interceptor Composition

Multiple interceptors should be independent and composable:

```kotlin
// Anti-pattern: Logging depends on auth
interceptor1 = AuthInterceptor()
interceptor2 = LoggingInterceptor()  // assumes auth token present

// Better: Logging logs whatever headers exist
```

### Chunked Encoding

For streaming uploads, use `RequestBody`:

```kotlin
val body = object : RequestBody() {
    override fun contentType() = MediaType.parse("text/plain")
    
    override fun writeTo(sink: BufferedSink) {
        // Stream directly, no buffer
        for (chunk in dataStream) {
            sink.write(chunk)
        }
    }
}
```

### Connection Pool Lifecycle

OkHttp connection thread pool lives for entire app:

```kotlin
// Single shared instance (correct)
val httpClient = OkHttpClient.Builder()
    .connectionPool(ConnectionPool())
    .build()

// Within Retrofit
val retrofit = Retrofit.Builder()
    .client(httpClient)
    .build()
```

Creating new OkHttp clients = new thread pools = memory leak.
