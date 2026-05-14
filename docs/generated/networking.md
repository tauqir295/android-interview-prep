---
hide:
  - toc
---

# Networking

<script>
(function () {
  function openQuestionFromHash() {
    const hash = window.location.hash;
    if (!hash || hash.length <= 1) return;

    const anchor = document.querySelector(hash);
    if (!anchor) return;

    let node = anchor.nextElementSibling;
    while (node) {
      if (node.tagName === 'DETAILS') {
        node.open = true;
        anchor.scrollIntoView({ behavior: 'auto', block: 'start' });
        return;
      }
      node = node.nextElementSibling;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', openQuestionFromHash);
  } else {
    openQuestionFromHash();
  }

  window.addEventListener('hashchange', openQuestionFromHash);
})();
</script>


---

<div id="retrofit-fundamentals"></div>

## What is Retrofit?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">retrofit</span>
  <span class="question-badge question-badge--tag">http</span>
</div>

??? question "View Answer"

    Retrofit is a type-safe HTTP client for Android built on top of OkHttp.

    Retrofit simplifies:

    - REST API integration
    - request creation
    - response parsing
    - serialization/deserialization

    Core concepts:

    - interface-based APIs
    - annotations
    - converters
    - coroutine support


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/retrofit-fundamentals/#retrofit-fundamentals">🚀 See Full Deep Dive</a>


---

<div id="retrofit-converters"></div>

## How do Retrofit converters work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">retrofit</span>
  <span class="question-badge question-badge--tag">serialization</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Retrofit converters handle serialization/deserialization between
    JSON and Kotlin objects.

    Popular converters:

    - GsonConverterFactory
    - MoshiConverterFactory
    - kotlinx.serialization

    Converter responsibility:

    - parse response body to objects
    - serialize objects to request body
    - handle content types
    - raise parsing exceptions


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/serialization-strategies/#retrofit-converters">🚀 See Full Deep Dive</a>


---

<div id="coroutines-retrofit"></div>

## How does Retrofit work with Kotlin Coroutines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">retrofit</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Retrofit provides suspend function support for coroutines,
    eliminating the need for Callback-based APIs.

    Advantages:

    - no callback hell
    - structured concurrency
    - cancellation support
    - exception propagation

    Under the hood:

    - adapters convert suspend to Call
    - Retrofit wraps in coroutine adapters
    - exceptions throw to caller
    - automatic cancellation on scope exit


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/retrofit-fundamentals/#coroutines-retrofit">🚀 See Full Deep Dive</a>


---

<div id="okhttp-interceptors"></div>

## What is an OkHttp Interceptor?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">okhttp</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">interceptors</span>
</div>

??? question "View Answer"

    Interceptors are OkHttp components that observe/modify HTTP requests/responses.

    Two types:

    - Application interceptors: see application code logic
    - Network interceptors: see actual network traffic

    Common uses:

    - logging
    - authentication (token injection)
    - request modification
    - response transformation
    - error handling


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/okhttp-internals/#okhttp-interceptors">🚀 See Full Deep Dive</a>


---

<div id="okhttp-connection-pooling"></div>

## How does OkHttp connection pooling work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">okhttp</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    OkHttp maintains a pool of reusable HTTP connections to avoid
    expensive reconnections.

    Benefits:

    - reduced latency
    - better throughput
    - lower CPU/battery usage
    - automatic reuse

    How it works:

    - connections cached by host:port:scheme
    - TTL enforced by keep-alive timeout
    - stale connections pruned
    - pool size configurable


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/okhttp-internals/#okhttp-connection-pooling">🚀 See Full Deep Dive</a>


---

<div id="rest-principles"></div>

## What are REST API principles?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">rest</span>
  <span class="question-badge question-badge--tag">api-design</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    REST (Representational State Transfer) is an architectural style
    for building scalable web services.

    Core principles:

    - resource-oriented URLs
    - standard HTTP methods
    - stateless communication
    - cacheable representations
    - client-server separation

    HTTP methods:

    - GET: retrieve
    - POST: create
    - PUT: replace
    - PATCH: partial update
    - DELETE: remove


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/rest-api-principles/#rest-principles">🚀 See Full Deep Dive</a>


---

<div id="http-methods"></div>

## When should you use HTTP PUT vs PATCH?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">rest</span>
  <span class="question-badge question-badge--tag">api-design</span>
  <span class="question-badge question-badge--tag">http</span>
</div>

??? question "View Answer"

    PUT and PATCH both modify resources but behave differently.

    PUT (complete replacement):

    - replaces entire resource
    - requires full new state
    - idempotent
    - typically 200/204 response

    PATCH (partial update):

    - modifies only specified fields
    - doesn't require full state
    - idempotent (with conditionals)
    - more bandwidth-efficient
    - typically 200/204 response

    Generally: use PATCH for Android to save bandwidth.


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/rest-api-principles/#http-methods">🚀 See Full Deep Dive</a>


---

<div id="json-serialization"></div>

## What are differences between Gson, Moshi, and Kotlin Serialization?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">serialization</span>
  <span class="question-badge question-badge--tag">json</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Three popular JSON serialization libraries for Android.

    Gson:

    - reflection-based (slower)
    - no compile-time checks
    - flexible with malformed JSON
    - mature ecosystem

    Moshi:

    - reflection + adapters
    - customizable
    - faster than Gson
    - better error messages

    Kotlin Serialization:

    - compiler plugin (fastest)
    - compile-time safety
    - no reflection needed
    - newer but growing adoption


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/serialization-strategies/#json-serialization">🚀 See Full Deep Dive</a>


---

<div id="authentication"></div>

## How should you implement authentication in mobile apps?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">authentication</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Authentication secures API access. Common strategies:

    JWT (JSON Web Tokens):

    - token-based (not session-based)
    - include in Authorization header
    - exp claim for expiration
    - refresh token for renewal

    OAuth 2.0:

    - delegated access
    - third-party sign-in
    - symmetric exchange flows
    - authorization code flow (mobile)

    Best practices:

    - store tokens securely (EncryptedSharedPreferences)
    - use refresh mechanism
    - never hardcode secrets
    - use interceptors for injection


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/authentication-security/#authentication">🚀 See Full Deep Dive</a>


---

<div id="https-tls"></div>

## What is HTTPS and TLS?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">https</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    HTTPS encrypts HTTP traffic using TLS (Transport Layer Security).

    Benefits:

    - confidentiality (data cannot be read)
    - integrity (data cannot be modified)
    - authentication (server verified)
    - prevents man-in-the-middle attacks

    How it works:

    - client initiates TLS handshake
    - server shares certificate
    - symmetric key negotiated
    - encrypted connection established

    On Android:

    - HTTPS enforced by default (Network Security Config)
    - certificate validation automatic


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/authentication-security/#https-tls">🚀 See Full Deep Dive</a>


---

<div id="certificate-pinning"></div>

## What is certificate pinning?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">okhttp</span>
</div>

??? question "View Answer"

    Certificate pinning is a security technique that roots trust
    in a specific certificate rather than the entire CA hierarchy.

    Benefits:

    - prevents compromised CAs
    - blocks rogue certificates
    - cryptographic trust anchoring

    How it works:

    - app stores certificate public key
    - validates server cert against pinned key
    - fails if mismatch

    OkHttp implementation:

    - CertificatePinner class
    - configure pins in build
    - specify host(s) to pin
    - use wildcard domains if needed


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/certificate-pinning/#certificate-pinning">🚀 See Full Deep Dive</a>


---

<div id="retry-strategies"></div>

## How should you implement retry logic?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">resilience</span>
  <span class="question-badge question-badge--tag">error-handling</span>
</div>

??? question "View Answer"

    Retry logic handles transient network failures automatically.

    When to retry:

    - network timeouts
    - 5xx server errors
    - connection resets
    - DNS failures

    Do NOT retry:

    - 4xx client errors (except 429 rate limit)
    - authentication failures
    - payload errors

    Implementation patterns:

    - simple retry with delay
    - exponential backoff
    - jitter to prevent thundering herd
    - max retry limit


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/retry-exponential-backoff/#retry-strategies">🚀 See Full Deep Dive</a>


---

<div id="exponential-backoff"></div>

## What is exponential backoff?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">optimization</span>
  <span class="question-badge question-badge--tag">resilience</span>
</div>

??? question "View Answer"

    Exponential backoff increases delay between retries
    to prevent server overload.

    Formula:

    delay = base * (2 ^ attempt) + jitter

    Benefits:

    - reduces server load
    - prevents thundering herd
    - increases success rate
    - network stabilization

    Example:

    - attempt 1: 1s
    - attempt 2: 2s
    - attempt 3: 4s
    - attempt 4: 8s

    Best practices:

    - add random jitter
    - set maximum delay
    - set maximum retries
    - respect Retry-After header


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/retry-exponential-backoff/#exponential-backoff">🚀 See Full Deep Dive</a>


---

<div id="pagination"></div>

## How does pagination work in REST APIs?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">pagination</span>
  <span class="question-badge question-badge--tag">rest</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Pagination splits large result sets into smaller pages
    to reduce memory/bandwidth.

    Common approaches:

    - Offset/Limit: offset + limit query params
    - Cursor-based: opaque cursor token
    - Keyset: last ID from previous page

    Pagination parameters:

    - page or offset
    - limit or pageSize
    - cursor or pageToken
    - totalCount (optional)

    Response:

    - items array
    - hasMore boolean
    - nextPageToken
    - totalCount (optional)

    When to use:

    - offset/limit: simple, not ideal for real-time
    - cursor: recommended, handles inserts/deletes


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/pagination-architecture/#pagination">🚀 See Full Deep Dive</a>


---

<div id="paging-3"></div>

## What is Paging 3 library?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">pagination</span>
  <span class="question-badge question-badge--tag">paging3</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    Paging 3 is Android's best-practice pagination library
    built on Flow for seamless list loading.

    Core components:

    - PagingSource: provides page data
    - Pager: creates PagingData Flow
    - PagingDataAdapter: RecyclerView adapter

    Benefits:

    - automatic caching
    - cancellation support
    - separation of concerns
    - Flow-based reactive
    - handles duplicate loads

    Architecture:

    - repository provides PagingSource
    - viewmodel exposes Pager.flow
    - UI subscribes and displays


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/pagination-architecture/#paging-3">🚀 See Full Deep Dive</a>


---

<div id="http-caching"></div>

## How does HTTP caching work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">caching</span>
  <span class="question-badge question-badge--tag">http</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    HTTP caching reduces bandwidth by reusing responses.

    Cache control headers:

    - Cache-Control: max-age (seconds)
    - Expires: absolute time
    - ETag: version identifier
    - Last-Modified: resource timestamp

    Caching types:

    - private (browser cache only)
    - public (shared cache)
    - no-cache (validate always)
    - no-store (never cache)

    OkHttp caching:

    - automatic by default
    - configurable cache size
    - respects Cache-Control headers
    - offline page fallback possible


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/caching-strategies/#http-caching">🚀 See Full Deep Dive</a>


---

<div id="etags-conditional"></div>

## What are ETags and conditional requests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">caching</span>
  <span class="question-badge question-badge--tag">http</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    ETags and conditional requests minimize bandwidth
    by validating cached responses.

    ETags:

    - unique identifier for resource version
    - server sends with response
    - client includes in future requests
    - server returns 304 Not Modified if unchanged

    Conditional requests:

    - If-None-Match: ETag validation
    - If-Modified-Since: timestamp validation
    - server responds 304 Not Modified
    - client reuses cached response

    Benefits:

    - save bandwidth
    - validate without full transfer
    - handle resource updates
    - prevent stale data


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/caching-strategies/#etags-conditional">🚀 See Full Deep Dive</a>


---

<div id="offline-first"></div>

## What is offline-first architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">offline</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Offline-first prioritizes local-first operation,
    syncing when network available.

    Principles:

    - always use local database first
    - sync to server when connected
    - seamless online/offline transitions
    - user experience consistency

    Architecture:

    - local Room database
    - repository handles sync
    - background sync workers
    - conflict resolution

    Benefits:

    - instant UI responsiveness
    - works without network
    - resilient to connection loss
    - better battery life


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/offline-first-architecture/#offline-first">🚀 See Full Deep Dive</a>


---

<div id="sync-engine"></div>

## How do you implement a sync engine?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">offline</span>
  <span class="question-badge question-badge--tag">sync</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    A sync engine keeps local and remote data consistent.

    Components:

    - sync worker: runs on schedule
    - local database: source of truth
    - remote API: server state
    - conflict resolver: handles mismatches

    Sync flow:

    - fetch remote changes (pull)
    - apply to local database
    - upload local changes (push)
    - resolve conflicts
    - mark synced

    Challenges:

    - conflict resolution
    - duplicate prevention
    - partial sync recovery
    - offline queue management


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/offline-first-architecture/#sync-engine">🚀 See Full Deep Dive</a>


---

<div id="conflict-resolution"></div>

## How should you handle sync conflicts?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">sync</span>
  <span class="question-badge question-badge--tag">offline</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    Conflict resolution determines which data wins when
    both local and remote changes exist.

    Strategies:

    - last-write-wins: use timestamp
    - remote-wins: server always correct
    - local-wins: device always correct
    - merge: combine changes intelligently
    - manual: show UI for user choice

    Implementation:

    - version vectors: track causality
    - timestamps: simple but flawed
    - operation-based: log changes
    - state-based: full state comparison

    Production patterns:

    - merge non-conflicting fields
    - use timestamps wisely
    - log conflicts for debugging
    - expose unresolved conflicts in UI


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/conflict-resolution/#conflict-resolution">🚀 See Full Deep Dive</a>


---

<div id="websockets"></div>

## What are WebSockets?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">websockets</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">real-time</span>
</div>

??? question "View Answer"

    WebSockets provide full-duplex communication over TCP,
    enabling real-time bidirectional messaging.

    Benefits:

    - persistent connection
    - low latency
    - bidirectional messaging
    - event-driven
    - better than polling

    Use cases:

    - chat applications
    - live notifications
    - real-time dashboards
    - multiplayer games

    Libraries:

    - OkHttp WebSocket support
    - Scarlet library
    - Kotlin Flows for events


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/websockets-streaming/#websockets">🚀 See Full Deep Dive</a>


---

<div id="streaming-downloads"></div>

## How do you handle streaming and large file downloads?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">streaming</span>
  <span class="question-badge question-badge--tag">optimization</span>
</div>

??? question "View Answer"

    Streaming and downloads require special handling to avoid
    memory issues and provide progress feedback.

    Streaming approaches:

    - ResponseBody streaming
    - byte[] chunking
    - reactive publishers
    - progress callbacks

    Best practices:

    - write to disk, not memory
    - implement progress listener
    - handle pause/resume
    - validate downloaded file
    - use download manager

    Implementation:

    - Retrofit ResponseBody
    - OkHttp interceptors for progress
    - WorkManager for background jobs
    - MediaStore for saved files


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/websockets-streaming/#streaming-downloads">🚀 See Full Deep Dive</a>


---

<div id="network-error-handling"></div>

## How should you handle network errors?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">error-handling</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">resilience</span>
</div>

??? question "View Answer"

    Network error handling ensures app gracefully handles
    connectivity issues and API errors.

    Error types:

    - no connectivity
    - timeouts
    - 4xx client errors
    - 5xx server errors
    - parsing errors

    Handling strategies:

    - retry transient errors
    - show user-friendly errors
    - log for debugging
    - fallback to cached data
    - offline queue for sync

    Response codes:

    - 401: authentication failure
    - 403: permission denied
    - 429: rate limited
    - 5xx: server error (retry)


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/error-handling-resilience/#network-error-handling">🚀 See Full Deep Dive</a>


---

<div id="resiliency-patterns"></div>

## What are network resiliency patterns?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">resilience</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">patterns</span>
</div>

??? question "View Answer"

    Resiliency patterns make apps robust to network failures.

    Patterns:

    - Circuit breaker: stop retries on repeated failure
    - Bulkhead: isolate failures
    - Timeout: prevent hanging requests
    - Retry: automatic failure recovery
    - Fallback: use cached/default data

    Implementation:

    - OkHttp timeouts
    - exponential backoff
    - health checks
    - circuit breaker library (Resilience4j)

    Benefits:

    - improved user experience
    - reduced server load
    - cascading failure prevention
    - automatic recovery


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/error-handling-resilience/#resiliency-patterns">🚀 See Full Deep Dive</a>


---

<div id="compression"></div>

## How does request/response compression work?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">optimization</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">compression</span>
</div>

??? question "View Answer"

    Compression reduces bandwidth by encoding data.

    HTTP compression:

    - gzip: most common
    - deflate: less common
    - brotli: newer, better ratio

    How it works:

    - client sends Accept-Encoding header
    - server compresses with matching algorithm
    - server sends Content-Encoding header
    - client decompresses

    OkHttp:

    - automatic by default
    - transparent to application
    - reduces bandwidth 60-80%
    - minimal CPU overhead


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/compression-optimization/#compression">🚀 See Full Deep Dive</a>


---

<div id="battery-optimization"></div>

## How do you optimize for battery usage in networking?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">optimization</span>
  <span class="question-badge question-badge--tag">battery</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Battery optimization reduces networking's power consumption.

    Techniques:

    - batch requests (not individual)
    - use connection pooling
    - compress responses
    - avoid polling
    - use WorkManager
    - sync intelligently

    DON'Ts:

    - frequent network requests
    - polling background services
    - large uncompressed payloads
    - excessive logging

    Tools:

    - Battery Historian
    - Perfetto for tracing
    - NetworkProfiler in Studio


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/compression-optimization/#battery-optimization">🚀 See Full Deep Dive</a>


---

<div id="graphql-rest"></div>

## What are differences between GraphQL and REST?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">graphql</span>
  <span class="question-badge question-badge--tag">rest</span>
  <span class="question-badge question-badge--tag">api-design</span>
</div>

??? question "View Answer"

    GraphQL and REST are different API design philosophies.

    REST:

    - resource-oriented
    - multiple endpoints per domain
    - fixed response structures
    - over/under fetching common

    GraphQL:

    - query-oriented
    - single endpoint
    - client specifies fields
    - exact data fetching
    - supports subscriptions

    Trade-offs:

    REST: simpler caching, broader tooling
    GraphQL: flexible queries, reduced over-fetching

    For Android:

    - REST simpler for mobile
    - GraphQL better for diverse clients
    - Apollo Kotlin library for GraphQL


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/graphql-advanced/#graphql-rest">🚀 See Full Deep Dive</a>


---

<div id="grpc-basics"></div>

## What is gRPC?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">grpc</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">protocols</span>
</div>

??? question "View Answer"

    gRPC is a modern RPC framework using Protocol Buffers
    and HTTP/2 for efficient communication.

    Benefits:

    - faster than JSON/REST
    - strongly typed via protobuf
    - multiplexing with HTTP/2
    - streaming support
    - language-independent

    Use cases:

    - microservices
    - high-performance APIs
    - streaming data
    - real-time communication

    Complexity:

    - steeper learning curve
    - less browser-friendly
    - newer ecosystem


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/graphql-advanced/#grpc-basics">🚀 See Full Deep Dive</a>


---

<div id="network-monitoring"></div>

## How do you monitor and debug network traffic?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">debugging</span>
  <span class="question-badge question-badge--tag">monitoring</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Network debugging reveals actual traffic and helps diagnose issues.

    Tools:

    - OkHttp logging interceptor
    - Android Studio Network Profiler
    - Chucker library
    - Stetho library
    - Charles proxy
    - Wireshark

    What to log:

    - URL and method
    - request headers
    - response status
    - response time
    - response size
    - errors

    Chucker features:

    - intercepts HTTP requests
    - in-app notification
    - request/response inspection
    - replay requests


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/network-monitoring-debugging/#network-monitoring">🚀 See Full Deep Dive</a>


---

<div id="rate-limiting"></div>

## How do you handle rate limiting?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">rate-limiting</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">resilience</span>
</div>

??? question "View Answer"

    Rate limiting controls request frequency per API.

    Server communicates limits via headers:

    - X-RateLimit-Limit: max requests
    - X-RateLimit-Remaining: quota left
    - X-RateLimit-Reset: reset timestamp
    - Retry-After: wait before retry

    Client-side handling:

    - predict when limit reached
    - queue requests
    - exponential backoff
    - respect Retry-After
    - show user feedback

    Implementation:

    - track rate-limit headers
    - use CircuitBreaker pattern
    - queue strategy (FIFO/priority)


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/rate-limiting-idempotency/#rate-limiting">🚀 See Full Deep Dive</a>


---

<div id="idempotency"></div>

## What is idempotency in APIs?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">rest</span>
  <span class="question-badge question-badge--tag">api-design</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Idempotency ensures repeated requests have same effect
    as single request, crucial for reliability.

    Idempotent methods:

    - GET: always safe
    - DELETE: delete again = 204
    - PUT: replace again = same result

    Non-idempotent:

    - POST: create again = duplicate
    - PATCH: sometimes idempotent

    Implementation:

    - Idempotency-Key header (UUID)
    - server deduplicates by key
    - caches result with key
    - returns cached on retry

    Benefits:

    - safe retries
    - conflict prevention
    - exactly-once semantics


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/rate-limiting-idempotency/#idempotency">🚀 See Full Deep Dive</a>


---

<div id="multipart-uploads"></div>

## How do you implement multipart file uploads?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">file-upload</span>
  <span class="question-badge question-badge--tag">retrofit</span>
</div>

??? question "View Answer"

    Multipart uploads handle mixed binary/text data
    in single request.

    Retrofit multipart:

    - @Multipart annotation
    - @Part for file field
    - @Part for text fields
    - RequestBody wrapping

    Best practices:

    - compress before upload
    - show progress indicator
    - handle upload resume
    - validate after upload
    - background worker for large

    Chunks:

    - upload in chunks
    - resumable upload
    - verify integrity
    - range requests


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/multipart-uploads/#multipart-uploads">🚀 See Full Deep Dive</a>


---

<div id="api-versioning"></div>

## How should you version your APIs?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">api-design</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    API versioning enables evolution without breaking clients.

    Strategies:

    - URL path: /v1/users /v2/users
    - header: Accept: application/vnd.api+v2+json
    - query param: /users?version=2
    - custom header: X-API-Version: 2

    Best practices:

    - support 2-3 versions simultaneously
    - provide migration guide
    - deprecate with warning
    - sunset timeline
    - clear documentation

    Client-side:

    - respect API version
    - handle version changes
    - migrate gradually
    - test against versions


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/api-versioning-scalability/#api-versioning">🚀 See Full Deep Dive</a>


---

<div id="scalability-cdn"></div>

## What is CDN and when to use it?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">scalability</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">cdn</span>
</div>

??? question "View Answer"

    CDN (Content Delivery Network) caches content globally
    for lower latency and bandwidth savings.

    Benefits:

    - geographically distributed
    - reduced latency
    - bandwidth savings
    - offload server load
    - DDoS protection

    Use cases:

    - static assets (images, JS)
    - video/media streaming
    - mobile app updates
    - download packages

    For Android:

    - CDN for APK/updates
    - asset CDN for images
    - API gateway CDN


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/api-versioning-scalability/#scalability-cdn">🚀 See Full Deep Dive</a>


---

<div id="request-cancellation"></div>

## How do you cancel network requests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">cancellation</span>
  <span class="question-badge question-badge--tag">coroutines</span>
</div>

??? question "View Answer"

    Request cancellation prevents unnecessary network usage
    and improves responsiveness.

    Retrofit with coroutines:

    - automatic cancellation on scope exit
    - respects job.cancel()
    - cleans up OkHttp Call

    OkHttp Call:

    - .cancel() method
    - prevents further progress
    - saves bandwidth
    - closes connections

    Use cases:

    - navigation away (view destroyed)
    - user explicitly cancels
    - timeout exceeded
    - parent scope cancelled


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/rate-limiting-idempotency/#request-cancellation">🚀 See Full Deep Dive</a>


---

<div id="network-security-config"></div>

## What is Network Security Configuration?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    Network Security Configuration declaratively specifies
    HTTPS/TLS settings per domain.

    Features:

    - enforce HTTPS
    - certificate pinning
    - custom CA certificates
    - domain-specific rules
    - development vs production

    Configuration:

    - XML file in res/xml/
    - applied system-wide
    - per-domain override
    - certificate pins

    Benefits:

    - prevents MITM attacks
    - gradual certificate migration
    - dev shortcuts (cleartext HTTP)
    - centralized security policy


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/production-networking-patterns/#network-security-config">🚀 See Full Deep Dive</a>


---

<div id="timeouts"></div>

## How should you configure network timeouts?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">optimization</span>
  <span class="question-badge question-badge--tag">okhttp</span>
</div>

??? question "View Answer"

    Timeouts prevent indefinite waiting for network responses.

    OkHttp timeout types:

    - connectTimeout: TCP connection
    - readTimeout: data arrival
    - writeTimeout: data upload
    - callTimeout: entire call

    Configuration:

    - HttpClient.newBuilder().connectTimeout(30, SECONDS)
    - per-request overrides possible
    - consider network conditions
    - balance UX vs resource usage

    Android best practices:

    - connection: 10-30 seconds
    - read: 20-60 seconds
    - write: 20-60 seconds
    - retry on timeout


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/production-networking-patterns/#timeouts">🚀 See Full Deep Dive</a>


---

<div id="performance-monitoring"></div>

## How do you monitor API performance?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">monitoring</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">networking</span>
</div>

??? question "View Answer"

    Performance monitoring tracks latency, success rates,
    and resource usage.

    Metrics to track:

    - response time distribution
    - success/failure rates
    - error types
    - payload sizes
    - request throughput

    Tools:

    - Firebase Performance Monitoring
    - Crashlytics for errors
    - custom analytics
    - server logs

    Implementation:

    - timing instrumentation
    - error categorization
    - network state detection
    - batch reporting


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/networking/production-networking-patterns/#performance-monitoring">🚀 See Full Deep Dive</a>

