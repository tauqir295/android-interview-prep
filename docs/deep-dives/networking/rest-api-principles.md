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

## REST API Principles Deep Dive

## Overview

REST (Representational State Transfer) is an architectural style for distributed systems communication. Understanding REST principles is foundational for mobile networking.

## Core Concepts

### Six REST Constraints

1. **Client-Server:** UI separate from data storage
2. **Stateless:** Each request contains all needed context
3. **Cacheable:** Responses marked as cacheable/non-cacheable
4. **Uniform Interface:** Consistent resource identification
5. **Layered System:** Client can't tell if connected to end server
6. **Code on Demand:** Optional; servers can extend client functionality

### Resource-Oriented Design

REST is resource-oriented, not action-oriented:

```
Wrong (RPC-style):
/getUser?id=123
/deleteUser?id=123
/updateUser?id=123&name=John

Right (REST):
GET /users/123
DELETE /users/123
PUT /users/123
```

Resources are nouns. HTTP methods are verbs.

### HTTP Status Codes

**2xx (Success):**
- 200 OK: request succeeded
- 201 Created: resource created
- 204 No Content: success, no body

**3xx (Redirect):**
- 301 Moved Permanently: resource moved
- 304 Not Modified: cached response valid

**4xx (Client Error):**
- 400 Bad Request: invalid request
- 401 Unauthorized: authentication required
- 403 Forbidden: authentication OK, but no permission
- 404 Not Found: resource doesn't exist
- 429 Too Many Requests: rate limited

**5xx (Server Error):**
- 500 Internal Server Error: server broke
- 503 Service Unavailable: temporarily down

## Internal Implementation

### URL Structure

```
https://api.example.com/v1/users/123/posts
|_____________________________|  |||||
        Authority             Path segments
```

Path design:

```
/users/:id           # GET one, POST new, DELETE one
/users               # GET list, POST new
/users/:id/posts     # nested resource
```

### Content Negotiation

Clients indicate desired format:

```
Accept: application/json
Accept: application/xml
Accept: text/plain
```

Server responds:

```
Content-Type: application/json; charset=utf-8
```

## Request/Response Flow

### Complete Request Example

```
GET /users/123 HTTP/1.1
Host: api.example.com
Authorization: Bearer token123
Accept: application/json
```

### Complete Response Example

```
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=300
ETag: "abc123"

{
  "id": 123,
  "name": "John",
  "email": "john@example.com"
}
```

## Code Examples

### Retrofit REST API Interface

```kotlin
interface UserApi {
    @GET("users")
    suspend fun listUsers(
        @Query("page") page: Int = 1,
        @Query("limit") limit: Int = 20
    ): Response<List<User>>
    
    @GET("users/{id}")
    suspend fun getUser(@Path("id") id: Int): User
    
    @POST("users")
    suspend fun createUser(@Body user: User): User
    
    @PUT("users/{id}")
    suspend fun updateUser(
        @Path("id") id: Int,
        @Body user: User
    ): User
    
    @DELETE("users/{id}")
    suspend fun deleteUser(@Path("id") id: Int)
}
```

## Common Interview Questions

**Q: Is REST a standard or a style?**
A: It's an architectural style/constraint set, not a standard. HTTP is the standard.

**Q: Should I cache POST requests?**
A: Generally no. POST is for creating, which should always hit server.

**Q: What's idempotence in REST?**
A: Repeated calls have same effect as single call. GET/PUT/DELETE are idempotent. POST is not.

## Production Considerations

### API Versioning

```
(1) URL path: /v1/users /v2/users
(2) Header: Accept: application/vnd.api+v2+json
(3) Query: /users?version=2
```

Best: separate versions entirely so can deprecate.

### Rate Limiting

Server should communicate limits:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1631234567
Retry-After: 60
```

Client must respect these.

### Pagination

For large result sets:

```
GET /users?page=1&limit=20
GET /users?page=2&limit=20

// Or cursor-based
GET /users?limit=20
GET /users?limit=20&cursor=abc123
```

## Performance Insights

### Bandwidth Optimization

- Use gzip compression
- Only request needed fields (GraphQL advantages)
- Pagination to avoid huge payloads

### Caching Strategy

```
GET /users/123
  Cache-Control: max-age=300  # cache 5 min
GET /users/123/posts
  Cache-Control: no-cache     # revalidate always
POST /users
  Cache-Control: private, no-cache  # don't cache
```

## Senior-Level Insights

###HATEOAS (Hypermedia)

Advanced REST includes hypermedia links:

```json
{
  "id": 123,
  "name": "John",
  "_links": {
    "self": {"href": "/users/123"},
    "posts": {"href": "/users/123/posts"},
    "friends": {"href": "/users/123/friends"}
  }
}
```

Enables client discovery without hardcoding URLs. Rarely used in Android but important concept.

### REST Maturity Levels

1. **Level 0:** RPC (action-based URLs)
2. **Level 1:** Resource-oriented (URLs)
3. **Level 2:** HTTP methods + status codes
4. **Level 3:** Hypermedia (HATEOAS)

Most mobile APIs are Level 2. Level 3 more common in web.

### When REST Isn't Enough

- Real-time: use WebSockets
- Complex queries: consider GraphQL
- Binary data: gRPC
- Event streams: Server-Sent Events
