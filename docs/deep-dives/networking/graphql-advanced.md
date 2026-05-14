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

## GraphQL & Advanced Protocols Deep Dive

## Overview
GraphQL vs REST trade-offs + gRPC alternatives.
## Core Concepts
REST:
- Resource-oriented
- Fixed response shapes
- Over/under-fetching common
GraphQL:
- Query language
- Client specifies fields
- Reduces bandwidth
- Learning curve
gRPC:
- Binary protocol (faster)
- Protocol Buffers schemas
- Streaming support
- Less browser-friendly
## Code Examples
```kotlin
// Apollo Kotlin for GraphQL
val apolloClient = ApolloClient.Builder()
    .serverUrl("https://api.example.com/graphql")
    .build()
// Query
val query = GetUserQuery(id = "123")
val response = apolloClient.query(query).execute()
```
## Senior-Level Insights
- GraphQL best for complex queries
- gRPC for services/microservices
- REST for simple CRUD
