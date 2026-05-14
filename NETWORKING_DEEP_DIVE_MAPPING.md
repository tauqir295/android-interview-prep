# Networking & Offline-First Deep Dive Mapping

This document maps Networking section questions to shared deep-dive topics.

## Architecture Overview

The Networking section contains:

- **Total Questions:** 50
- **Total Deep Dives:** 20
- **Strategy:** multiple questions per deep dive

Each deep dive covers:
- Core fundamentals and internals
- Android-specific production patterns
- Senior-level architectural insights
- Interview traps and considerations

---

## Recommended Deep Dive Files

### 1. `retrofit-fundamentals.md`
Retrofit library, converters, coroutine integration, type-safety, call adapters.

### 2. `okhttp-internals.md`
OkHttp architecture, interceptors, connection pooling, HTTP stack, request/response cycle.

### 3. `rest-api-principles.md`
REST fundamentals, HTTP methods, API design, resource orientation, standard practices.

### 4. `serialization-strategies.md`
Gson vs Moshi vs Kotlin Serialization, reflection vs reflection-free, performance, compatibility.

### 5. `authentication-security.md`
JWT tokens, OAuth 2.0, secure storage, token refresh, interceptor-level injection, browser-security model.

### 6. `certificate-pinning.md`
Certificate pinning, TLS/SSL, public key pinning, OkHttp CertificatePinner, HTTPS validation.

### 7. `retry-exponential-backoff.md`
Retry strategies, exponential backoff, jitter, thundering herd, retry limits, when NOT to retry.

### 8. `pagination-architecture.md`
Pagination strategies (offset/limit, cursor, keyset), Paging 3 library, RemoteMediator, CombinedLoadStates.

### 9. `caching-strategies.md`
HTTP caching, Cache-Control headers, OkHttp cache, offline fallback, ETag/conditional requests.

### 10. `offline-first-architecture.md`
Offline-first principles, local database source-of-truth, sync mechanics, online/offline transitions.

### 11. `conflict-resolution.md`
Sync conflicts, conflict resolution strategies, version vectors, last-write-wins, merge patterns, operational transformation.

### 12. `websockets-streaming.md`
WebSocket protocol, bidirectional communication, Scarlet library, streaming downloads, progress callbacks.

### 13. `error-handling-resilience.md`
Network error categorization, resilience patterns, recovery strategies, fallback mechanisms, error user-feedback.

### 14. `compression-optimization.md`
gzip/brotli compression, Accept-Encoding headers, bandwidth savings, battery optimization, connection pooling.

### 15. `graphql-advanced.md`
GraphQL vs REST trade-offs, Apollo Kotlin, query language, subscription model, gRPC basics.

### 16. `network-monitoring-debugging.md`
HTTP interceptor logging, Network Profiler, Chucker integration, Stetho, request/response inspection, debugging workflow.

### 17. `rate-limiting-idempotency.md`
Rate limit headers (X-RateLimit-*), Retry-After, idempotency keys, request deduplication, circuit breakers.

### 18. `multipart-uploads.md`
Multipart requests, @Multipart/@Part annotations, file handling, resumable uploads, chunked uploads, validation.

### 19. `api-versioning-scalability.md`
API versioning strategies (path, header, param), backward compatibility, deprecation, CDN usage, scalability.

### 20. `production-networking-patterns.md`
Production patterns, timeouts (connect/read/write), Network Security Config, performance monitoring, edge cases.

---

## Question-to-Deep Dive Mapping

| Question | Deep Dive |
|----------|-----------|
| retrofit-fundamentals | retrofit-fundamentals |
| retrofit-converters | serialization-strategies |
| coroutines-retrofit | retrofit-fundamentals |
| okhttp-interceptors | okhttp-internals |
| okhttp-connection-pooling | okhttp-internals |
| rest-principles | rest-api-principles |
| http-methods | rest-api-principles |
| json-serialization | serialization-strategies |
| authentication | authentication-security |
| https-tls | authentication-security |
| certificate-pinning | certificate-pinning |
| retry-strategies | retry-exponential-backoff |
| exponential-backoff | retry-exponential-backoff |
| pagination | pagination-architecture |
| paging-3 | pagination-architecture |
| http-caching | caching-strategies |
| etags-conditional | caching-strategies |
| offline-first | offline-first-architecture |
| sync-engine | offline-first-architecture |
| conflict-resolution | conflict-resolution |
| websockets | websockets-streaming |
| streaming-downloads | websockets-streaming |
| network-error-handling | error-handling-resilience |
| resiliency-patterns | error-handling-resilience |
| compression | compression-optimization |
| battery-optimization | compression-optimization |
| graphql-rest | graphql-advanced |
| grpc-basics | graphql-advanced |
| network-monitoring | network-monitoring-debugging |
| rate-limiting | rate-limiting-idempotency |
| idempotency | rate-limiting-idempotency |
| multipart-uploads | multipart-uploads |
| api-versioning | api-versioning-scalability |
| scalability-cdn | api-versioning-scalability |
| request-cancellation | rate-limiting-idempotency |
| network-security-config | production-networking-patterns |
| timeouts | production-networking-patterns |
| performance-monitoring | production-networking-patterns |

---

## Summary

- **Published Questions:** 50
- **Shared Deep Dives:** 20
- **Reuse Ratio:** 2.5 questions per deep dive (optimal balance)
- **Coverage:** Fundamentals → Internals → Patterns → Production

All deep dives follow the standard template with required sections and proper back-navigation.

