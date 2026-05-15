---
hide:
  - toc
---

# System Design

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

<div id="system-design"></div>

## What is Android system design in interviews?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">interview</span>
</div>

??? question "View Answer"

    System design interviews reward structured thinking: clarify the problem, narrow scope intelligently, and make tradeoffs explicit before diving into components.

    In interviews, cover:

    - separate functional requirements from scale, latency, availability, compliance, and cost constraints because architecture follows those boundaries
    - time-box assumptions and rough estimations so the discussion stays grounded rather than hand-wavy
    - define the first viable version of the system before exploring advanced optimizations or multi-region complexity
    - use a repeatable structure—requirements, APIs, data model, components, bottlenecks, tradeoffs, evolution path
    - state what you are intentionally not solving yet; scope discipline is a positive signal, not a weakness

    Strong answer tip:

    - Interviewers usually prefer a clearly scoped and well-defended design over an overbuilt design that never established its assumptions.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/system-design-fundamentals/#system-design">🚀 See Full Deep Dive</a>


---

<div id="functional-vs-nonfunctional-requirements"></div>

## How do you separate functional vs non-functional requirements?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">requirements</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    System design interviews reward structured thinking: clarify the problem, narrow scope intelligently, and make tradeoffs explicit before diving into components.

    In interviews, cover:

    - separate functional requirements from scale, latency, availability, compliance, and cost constraints because architecture follows those boundaries
    - time-box assumptions and rough estimations so the discussion stays grounded rather than hand-wavy
    - define the first viable version of the system before exploring advanced optimizations or multi-region complexity
    - use a repeatable structure—requirements, APIs, data model, components, bottlenecks, tradeoffs, evolution path
    - state what you are intentionally not solving yet; scope discipline is a positive signal, not a weakness

    Strong answer tip:

    - Interviewers usually prefer a clearly scoped and well-defended design over an overbuilt design that never established its assumptions.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/requirements-and-scope/#functional-vs-nonfunctional-requirements">🚀 See Full Deep Dive</a>


---

<div id="scope-definition"></div>

## How do you define scope for a system design round?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">requirements</span>
  <span class="question-badge question-badge--tag">planning</span>
</div>

??? question "View Answer"

    System design interviews reward structured thinking: clarify the problem, narrow scope intelligently, and make tradeoffs explicit before diving into components.

    In interviews, cover:

    - separate functional requirements from scale, latency, availability, compliance, and cost constraints because architecture follows those boundaries
    - time-box assumptions and rough estimations so the discussion stays grounded rather than hand-wavy
    - define the first viable version of the system before exploring advanced optimizations or multi-region complexity
    - use a repeatable structure—requirements, APIs, data model, components, bottlenecks, tradeoffs, evolution path
    - state what you are intentionally not solving yet; scope discipline is a positive signal, not a weakness

    Strong answer tip:

    - Interviewers usually prefer a clearly scoped and well-defended design over an overbuilt design that never established its assumptions.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/requirements-and-scope/#scope-definition">🚀 See Full Deep Dive</a>


---

<div id="estimations"></div>

## How do you do quick capacity estimations?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">capacity</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    System design interviews reward structured thinking: clarify the problem, narrow scope intelligently, and make tradeoffs explicit before diving into components.

    In interviews, cover:

    - separate functional requirements from scale, latency, availability, compliance, and cost constraints because architecture follows those boundaries
    - time-box assumptions and rough estimations so the discussion stays grounded rather than hand-wavy
    - define the first viable version of the system before exploring advanced optimizations or multi-region complexity
    - use a repeatable structure—requirements, APIs, data model, components, bottlenecks, tradeoffs, evolution path
    - state what you are intentionally not solving yet; scope discipline is a positive signal, not a weakness

    Strong answer tip:

    - Interviewers usually prefer a clearly scoped and well-defended design over an overbuilt design that never established its assumptions.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/scalability-and-capacity-planning/#estimations">🚀 See Full Deep Dive</a>


---

<div id="high-level-components"></div>

## How do you structure high-level components?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">components</span>
</div>

??? question "View Answer"

    Component and boundary design is about minimizing coupling while preserving ownership clarity, deployability, and operational simplicity.

    In interviews, cover:

    - start with capabilities and change boundaries, not with a default “microservices everywhere” assumption
    - define interfaces around business actions and data contracts so teams can evolve independently
    - introduce BFF or edge-specific services when client needs diverge enough that a generic backend becomes a coordination bottleneck
    - watch for boundaries that look clean on diagrams but create chatty synchronous dependencies at runtime
    - for migrations, use strangler-style replacement when you need to route traffic gradually and prove the new path safely

    Strong answer tip:

    - A strong answer balances conceptual purity with operational cost: every boundary has coordination overhead.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/high-level-architecture/#high-level-components">🚀 See Full Deep Dive</a>


---

<div id="service-boundaries"></div>

## How do you define service boundaries?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">microservices</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    Component and boundary design is about minimizing coupling while preserving ownership clarity, deployability, and operational simplicity.

    In interviews, cover:

    - start with capabilities and change boundaries, not with a default “microservices everywhere” assumption
    - define interfaces around business actions and data contracts so teams can evolve independently
    - introduce BFF or edge-specific services when client needs diverge enough that a generic backend becomes a coordination bottleneck
    - watch for boundaries that look clean on diagrams but create chatty synchronous dependencies at runtime
    - for migrations, use strangler-style replacement when you need to route traffic gradually and prove the new path safely

    Strong answer tip:

    - A strong answer balances conceptual purity with operational cost: every boundary has coordination overhead.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/high-level-architecture/#service-boundaries">🚀 See Full Deep Dive</a>


---

<div id="data-modeling"></div>

## How do you approach data modeling in system design?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">data</span>
  <span class="question-badge question-badge--tag">modeling</span>
</div>

??? question "View Answer"

    Data design should reflect access patterns, consistency needs, and evolution pressure rather than ideological preference for one storage model.

    In interviews, cover:

    - model the dominant queries first because schema shape and storage choice should serve real read/write behavior
    - choose SQL when joins, transactions, and strong relational constraints matter; choose NoSQL when scale patterns or flexibility outweigh that rigor
    - treat indexes as read-optimization structures that also add write cost, storage cost, and operational complexity
    - plan schema evolution with backward compatibility, dual writes or readers, and safe rollout sequencing
    - explicitly discuss how the workload mix changes the architecture—for example, read-heavy systems often value caching and indexing more than strict write throughput

    Strong answer tip:

    - Interviewers like designs that clearly tie storage choices to query patterns, not “SQL for consistency, NoSQL for scale” clichés.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/data-modeling-and-storage/#data-modeling">🚀 See Full Deep Dive</a>


---

<div id="sql-vs-nosql"></div>

## When do you choose SQL vs NoSQL?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">databases</span>
  <span class="question-badge question-badge--tag">tradeoffs</span>
</div>

??? question "View Answer"

    Data design should reflect access patterns, consistency needs, and evolution pressure rather than ideological preference for one storage model.

    In interviews, cover:

    - model the dominant queries first because schema shape and storage choice should serve real read/write behavior
    - choose SQL when joins, transactions, and strong relational constraints matter; choose NoSQL when scale patterns or flexibility outweigh that rigor
    - treat indexes as read-optimization structures that also add write cost, storage cost, and operational complexity
    - plan schema evolution with backward compatibility, dual writes or readers, and safe rollout sequencing
    - explicitly discuss how the workload mix changes the architecture—for example, read-heavy systems often value caching and indexing more than strict write throughput

    Strong answer tip:

    - Interviewers like designs that clearly tie storage choices to query patterns, not “SQL for consistency, NoSQL for scale” clichés.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/data-modeling-and-storage/#sql-vs-nosql">🚀 See Full Deep Dive</a>


---

<div id="indexing-strategy"></div>

## How do indexes affect read and write performance?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">database</span>
  <span class="question-badge question-badge--tag">indexing</span>
</div>

??? question "View Answer"

    Data design should reflect access patterns, consistency needs, and evolution pressure rather than ideological preference for one storage model.

    In interviews, cover:

    - model the dominant queries first because schema shape and storage choice should serve real read/write behavior
    - choose SQL when joins, transactions, and strong relational constraints matter; choose NoSQL when scale patterns or flexibility outweigh that rigor
    - treat indexes as read-optimization structures that also add write cost, storage cost, and operational complexity
    - plan schema evolution with backward compatibility, dual writes or readers, and safe rollout sequencing
    - explicitly discuss how the workload mix changes the architecture—for example, read-heavy systems often value caching and indexing more than strict write throughput

    Strong answer tip:

    - Interviewers like designs that clearly tie storage choices to query patterns, not “SQL for consistency, NoSQL for scale” clichés.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/search-and-indexing/#indexing-strategy">🚀 See Full Deep Dive</a>


---

<div id="consistency-models"></div>

## What consistency models should you discuss in interviews?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">consistency</span>
  <span class="question-badge question-badge--tag">distributed-systems</span>
</div>

??? question "View Answer"

    Consistency decisions should be framed around user-visible correctness and failure handling, not abstract distributed-systems vocabulary alone.

    In interviews, cover:

    - name which operations require strong guarantees and which can tolerate eventual convergence or asynchronous repair
    - use transactions where the boundary is small and synchronous correctness is critical; use sagas where work spans services and compensation is acceptable
    - build idempotency into APIs and consumers so retries do not create duplicate side effects under failure
    - explain CAP pragmatically: partitions force tradeoffs, so the real question is which user guarantee you preserve when the network misbehaves
    - for eventually consistent systems such as search or analytics, define freshness expectations and user messaging explicitly

    Strong answer tip:

    - The strongest answers connect consistency to user experience—for example, payments and inventory feel different from search rankings or analytics counters.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/consistency-and-transactions/#consistency-models">🚀 See Full Deep Dive</a>


---

<div id="transactions-and-sagas"></div>

## When should you use transactions vs sagas?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">transactions</span>
  <span class="question-badge question-badge--tag">saga</span>
</div>

??? question "View Answer"

    Consistency decisions should be framed around user-visible correctness and failure handling, not abstract distributed-systems vocabulary alone.

    In interviews, cover:

    - name which operations require strong guarantees and which can tolerate eventual convergence or asynchronous repair
    - use transactions where the boundary is small and synchronous correctness is critical; use sagas where work spans services and compensation is acceptable
    - build idempotency into APIs and consumers so retries do not create duplicate side effects under failure
    - explain CAP pragmatically: partitions force tradeoffs, so the real question is which user guarantee you preserve when the network misbehaves
    - for eventually consistent systems such as search or analytics, define freshness expectations and user messaging explicitly

    Strong answer tip:

    - The strongest answers connect consistency to user experience—for example, payments and inventory feel different from search rankings or analytics counters.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/consistency-and-transactions/#transactions-and-sagas">🚀 See Full Deep Dive</a>


---

<div id="horizontal-scaling"></div>

## How do you scale a system horizontally?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">scalability</span>
  <span class="question-badge question-badge--tag">backend</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/scalability-and-capacity-planning/#horizontal-scaling">🚀 See Full Deep Dive</a>


---

<div id="load-balancing"></div>

## How do load balancers fit into architecture design?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/high-level-architecture/#load-balancing">🚀 See Full Deep Dive</a>


---

<div id="cache-aside"></div>

## What is cache-aside and when is it useful?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">caching</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/caching-strategies/#cache-aside">🚀 See Full Deep Dive</a>


---

<div id="cache-invalidation"></div>

## Why is cache invalidation hard?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">caching</span>
  <span class="question-badge question-badge--tag">consistency</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/caching-strategies/#cache-invalidation">🚀 See Full Deep Dive</a>


---

<div id="message-queues"></div>

## When do you add a message queue?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">queues</span>
  <span class="question-badge question-badge--tag">async</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/queueing-and-async-processing/#message-queues">🚀 See Full Deep Dive</a>


---

<div id="event-driven-design"></div>

## What are event-driven architecture tradeoffs?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">events</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/queueing-and-async-processing/#event-driven-design">🚀 See Full Deep Dive</a>


---

<div id="api-gateway"></div>

## What role does an API gateway play?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">api</span>
  <span class="question-badge question-badge--tag">gateway</span>
</div>

??? question "View Answer"

    External interface design should balance client simplicity, backward compatibility, security boundaries, and operational evolvability.

    In interviews, cover:

    - API gateways are useful for auth, routing, throttling, and cross-cutting concerns, but they should not become opaque monoliths of business logic
    - choose REST where broad interoperability and caching matter; choose gRPC where low-latency internal contracts and typed schemas provide leverage
    - design versioning and deprecation paths early so clients are never forced into emergency upgrades
    - separate authentication from authorization in both system boundaries and failure reasoning
    - for multi-tenant systems, isolate data, compute, quotas, and observability strongly enough that one tenant cannot degrade or inspect another

    Strong answer tip:

    - Interviewers like when you mention not only the happy path but also abuse resistance, key rotation, and backward compatibility.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/api-design-and-gateways/#api-gateway">🚀 See Full Deep Dive</a>


---

<div id="rest-vs-grpc-design"></div>

## How do you choose REST vs gRPC for internal APIs?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">api</span>
  <span class="question-badge question-badge--tag">grpc</span>
</div>

??? question "View Answer"

    External interface design should balance client simplicity, backward compatibility, security boundaries, and operational evolvability.

    In interviews, cover:

    - API gateways are useful for auth, routing, throttling, and cross-cutting concerns, but they should not become opaque monoliths of business logic
    - choose REST where broad interoperability and caching matter; choose gRPC where low-latency internal contracts and typed schemas provide leverage
    - design versioning and deprecation paths early so clients are never forced into emergency upgrades
    - separate authentication from authorization in both system boundaries and failure reasoning
    - for multi-tenant systems, isolate data, compute, quotas, and observability strongly enough that one tenant cannot degrade or inspect another

    Strong answer tip:

    - Interviewers like when you mention not only the happy path but also abuse resistance, key rotation, and backward compatibility.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/api-design-and-gateways/#rest-vs-grpc-design">🚀 See Full Deep Dive</a>


---

<div id="versioning-strategy"></div>

## How do you version APIs safely?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">api</span>
  <span class="question-badge question-badge--tag">versioning</span>
</div>

??? question "View Answer"

    External interface design should balance client simplicity, backward compatibility, security boundaries, and operational evolvability.

    In interviews, cover:

    - API gateways are useful for auth, routing, throttling, and cross-cutting concerns, but they should not become opaque monoliths of business logic
    - choose REST where broad interoperability and caching matter; choose gRPC where low-latency internal contracts and typed schemas provide leverage
    - design versioning and deprecation paths early so clients are never forced into emergency upgrades
    - separate authentication from authorization in both system boundaries and failure reasoning
    - for multi-tenant systems, isolate data, compute, quotas, and observability strongly enough that one tenant cannot degrade or inspect another

    Strong answer tip:

    - Interviewers like when you mention not only the happy path but also abuse resistance, key rotation, and backward compatibility.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/api-design-and-gateways/#versioning-strategy">🚀 See Full Deep Dive</a>


---

<div id="authn-vs-authz"></div>

## How do you model authentication vs authorization?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">auth</span>
</div>

??? question "View Answer"

    External interface design should balance client simplicity, backward compatibility, security boundaries, and operational evolvability.

    In interviews, cover:

    - API gateways are useful for auth, routing, throttling, and cross-cutting concerns, but they should not become opaque monoliths of business logic
    - choose REST where broad interoperability and caching matter; choose gRPC where low-latency internal contracts and typed schemas provide leverage
    - design versioning and deprecation paths early so clients are never forced into emergency upgrades
    - separate authentication from authorization in both system boundaries and failure reasoning
    - for multi-tenant systems, isolate data, compute, quotas, and observability strongly enough that one tenant cannot degrade or inspect another

    Strong answer tip:

    - Interviewers like when you mention not only the happy path but also abuse resistance, key rotation, and backward compatibility.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/security-and-compliance/#authn-vs-authz">🚀 See Full Deep Dive</a>


---

<div id="security-hardening"></div>

## What security hardening do you mention in interviews?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">security</span>
  <span class="question-badge question-badge--tag">production</span>
</div>

??? question "View Answer"

    External interface design should balance client simplicity, backward compatibility, security boundaries, and operational evolvability.

    In interviews, cover:

    - API gateways are useful for auth, routing, throttling, and cross-cutting concerns, but they should not become opaque monoliths of business logic
    - choose REST where broad interoperability and caching matter; choose gRPC where low-latency internal contracts and typed schemas provide leverage
    - design versioning and deprecation paths early so clients are never forced into emergency upgrades
    - separate authentication from authorization in both system boundaries and failure reasoning
    - for multi-tenant systems, isolate data, compute, quotas, and observability strongly enough that one tenant cannot degrade or inspect another

    Strong answer tip:

    - Interviewers like when you mention not only the happy path but also abuse resistance, key rotation, and backward compatibility.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/security-and-compliance/#security-hardening">🚀 See Full Deep Dive</a>


---

<div id="slos-and-slas"></div>

## How do SLOs/SLAs shape architecture decisions?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">observability</span>
  <span class="question-badge question-badge--tag">slo</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/observability-and-slos/#slos-and-slas">🚀 See Full Deep Dive</a>


---

<div id="logging-metrics-tracing"></div>

## Why are logs, metrics, and traces all needed?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">observability</span>
  <span class="question-badge question-badge--tag">monitoring</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/observability-and-slos/#logging-metrics-tracing">🚀 See Full Deep Dive</a>


---

<div id="circuit-breaker"></div>

## What is a circuit breaker and why use it?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">resilience</span>
  <span class="question-badge question-badge--tag">reliability</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/resilience-and-failure-handling/#circuit-breaker">🚀 See Full Deep Dive</a>


---

<div id="bulkheads-and-timeouts"></div>

## How do timeouts, retries, and bulkheads work together?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">resilience</span>
  <span class="question-badge question-badge--tag">timeouts</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/resilience-and-failure-handling/#bulkheads-and-timeouts">🚀 See Full Deep Dive</a>


---

<div id="idempotency"></div>

## Why is idempotency important in distributed systems?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">reliability</span>
  <span class="question-badge question-badge--tag">api</span>
</div>

??? question "View Answer"

    Consistency decisions should be framed around user-visible correctness and failure handling, not abstract distributed-systems vocabulary alone.

    In interviews, cover:

    - name which operations require strong guarantees and which can tolerate eventual convergence or asynchronous repair
    - use transactions where the boundary is small and synchronous correctness is critical; use sagas where work spans services and compensation is acceptable
    - build idempotency into APIs and consumers so retries do not create duplicate side effects under failure
    - explain CAP pragmatically: partitions force tradeoffs, so the real question is which user guarantee you preserve when the network misbehaves
    - for eventually consistent systems such as search or analytics, define freshness expectations and user messaging explicitly

    Strong answer tip:

    - The strongest answers connect consistency to user experience—for example, payments and inventory feel different from search rankings or analytics counters.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/resilience-and-failure-handling/#idempotency">🚀 See Full Deep Dive</a>


---

<div id="multi-region"></div>

## When do you move to multi-region architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">multi-region</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/multi-region-and-disaster-recovery/#multi-region">🚀 See Full Deep Dive</a>


---

<div id="disaster-recovery-rpo-rto"></div>

## How do RPO and RTO influence disaster recovery design?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">dr</span>
  <span class="question-badge question-badge--tag">reliability</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/multi-region-and-disaster-recovery/#disaster-recovery-rpo-rto">🚀 See Full Deep Dive</a>


---

<div id="cost-vs-latency"></div>

## How do you balance cost vs latency?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">cost</span>
  <span class="question-badge question-badge--tag">tradeoffs</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/cost-optimization/#cost-vs-latency">🚀 See Full Deep Dive</a>


---

<div id="capacity-headroom"></div>

## How much capacity headroom should a production system keep?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">capacity</span>
  <span class="question-badge question-badge--tag">operations</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/cost-optimization/#capacity-headroom">🚀 See Full Deep Dive</a>


---

<div id="bff-pattern"></div>

## What is Backend-for-Frontend (BFF) and when should Android use it?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">bff</span>
  <span class="question-badge question-badge--tag">mobile</span>
</div>

??? question "View Answer"

    Component and boundary design is about minimizing coupling while preserving ownership clarity, deployability, and operational simplicity.

    In interviews, cover:

    - start with capabilities and change boundaries, not with a default “microservices everywhere” assumption
    - define interfaces around business actions and data contracts so teams can evolve independently
    - introduce BFF or edge-specific services when client needs diverge enough that a generic backend becomes a coordination bottleneck
    - watch for boundaries that look clean on diagrams but create chatty synchronous dependencies at runtime
    - for migrations, use strangler-style replacement when you need to route traffic gradually and prove the new path safely

    Strong answer tip:

    - A strong answer balances conceptual purity with operational cost: every boundary has coordination overhead.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/mobile-backend-for-frontend/#bff-pattern">🚀 See Full Deep Dive</a>


---

<div id="edge-caching-mobile"></div>

## How does edge caching improve mobile user experience?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">cdn</span>
  <span class="question-badge question-badge--tag">mobile</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/mobile-backend-for-frontend/#edge-caching-mobile">🚀 See Full Deep Dive</a>


---

<div id="realtime-chat-design"></div>

## How would you design a real-time chat backend?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">realtime</span>
  <span class="question-badge question-badge--tag">websocket</span>
</div>

??? question "View Answer"

    Workload-specific designs are strongest when you identify the primary pressure—freshness, throughput, tail latency, ordering, or cost—and shape the architecture around it.

    In interviews, cover:

    - real-time chat emphasizes low-latency fanout, presence, ordering expectations, and offline reconciliation
    - search systems usually trade strict consistency for fast indexed reads and controlled ingestion pipelines
    - analytics pipelines optimize for high write volume, schema evolution, and downstream aggregation rather than per-event transactional guarantees
    - batch versus stream is rarely a philosophical choice; it depends on freshness needs, operational complexity, and cost tolerance
    - explicitly call out where client experience and backend architecture meet, especially for mobile offline behavior and tail-latency sensitivity

    Strong answer tip:

    - Interviewers respond well when example systems are used to demonstrate principles, not just recite component names.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/real-time-systems/#realtime-chat-design">🚀 See Full Deep Dive</a>


---

<div id="fanout-problem"></div>

## How do you handle fan-out at scale?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">realtime</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/real-time-systems/#fanout-problem">🚀 See Full Deep Dive</a>


---

<div id="search-architecture"></div>

## How do you design search for low-latency queries?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">search</span>
  <span class="question-badge question-badge--tag">indexing</span>
</div>

??? question "View Answer"

    Workload-specific designs are strongest when you identify the primary pressure—freshness, throughput, tail latency, ordering, or cost—and shape the architecture around it.

    In interviews, cover:

    - real-time chat emphasizes low-latency fanout, presence, ordering expectations, and offline reconciliation
    - search systems usually trade strict consistency for fast indexed reads and controlled ingestion pipelines
    - analytics pipelines optimize for high write volume, schema evolution, and downstream aggregation rather than per-event transactional guarantees
    - batch versus stream is rarely a philosophical choice; it depends on freshness needs, operational complexity, and cost tolerance
    - explicitly call out where client experience and backend architecture meet, especially for mobile offline behavior and tail-latency sensitivity

    Strong answer tip:

    - Interviewers respond well when example systems are used to demonstrate principles, not just recite component names.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/search-and-indexing/#search-architecture">🚀 See Full Deep Dive</a>


---

<div id="eventual-consistency-search"></div>

## Why is search often eventually consistent?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">search</span>
  <span class="question-badge question-badge--tag">consistency</span>
</div>

??? question "View Answer"

    Consistency decisions should be framed around user-visible correctness and failure handling, not abstract distributed-systems vocabulary alone.

    In interviews, cover:

    - name which operations require strong guarantees and which can tolerate eventual convergence or asynchronous repair
    - use transactions where the boundary is small and synchronous correctness is critical; use sagas where work spans services and compensation is acceptable
    - build idempotency into APIs and consumers so retries do not create duplicate side effects under failure
    - explain CAP pragmatically: partitions force tradeoffs, so the real question is which user guarantee you preserve when the network misbehaves
    - for eventually consistent systems such as search or analytics, define freshness expectations and user messaging explicitly

    Strong answer tip:

    - The strongest answers connect consistency to user experience—for example, payments and inventory feel different from search rankings or analytics counters.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/search-and-indexing/#eventual-consistency-search">🚀 See Full Deep Dive</a>


---

<div id="analytics-pipeline"></div>

## How do you design analytics ingestion pipelines?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">analytics</span>
  <span class="question-badge question-badge--tag">data-pipeline</span>
</div>

??? question "View Answer"

    Workload-specific designs are strongest when you identify the primary pressure—freshness, throughput, tail latency, ordering, or cost—and shape the architecture around it.

    In interviews, cover:

    - real-time chat emphasizes low-latency fanout, presence, ordering expectations, and offline reconciliation
    - search systems usually trade strict consistency for fast indexed reads and controlled ingestion pipelines
    - analytics pipelines optimize for high write volume, schema evolution, and downstream aggregation rather than per-event transactional guarantees
    - batch versus stream is rarely a philosophical choice; it depends on freshness needs, operational complexity, and cost tolerance
    - explicitly call out where client experience and backend architecture meet, especially for mobile offline behavior and tail-latency sensitivity

    Strong answer tip:

    - Interviewers respond well when example systems are used to demonstrate principles, not just recite component names.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/analytics-pipeline-design/#analytics-pipeline">🚀 See Full Deep Dive</a>


---

<div id="batch-vs-stream"></div>

## When do you choose batch vs stream processing?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">analytics</span>
  <span class="question-badge question-badge--tag">streaming</span>
</div>

??? question "View Answer"

    Workload-specific designs are strongest when you identify the primary pressure—freshness, throughput, tail latency, ordering, or cost—and shape the architecture around it.

    In interviews, cover:

    - real-time chat emphasizes low-latency fanout, presence, ordering expectations, and offline reconciliation
    - search systems usually trade strict consistency for fast indexed reads and controlled ingestion pipelines
    - analytics pipelines optimize for high write volume, schema evolution, and downstream aggregation rather than per-event transactional guarantees
    - batch versus stream is rarely a philosophical choice; it depends on freshness needs, operational complexity, and cost tolerance
    - explicitly call out where client experience and backend architecture meet, especially for mobile offline behavior and tail-latency sensitivity

    Strong answer tip:

    - Interviewers respond well when example systems are used to demonstrate principles, not just recite component names.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/analytics-pipeline-design/#batch-vs-stream">🚀 See Full Deep Dive</a>


---

<div id="migration-strangler"></div>

## What is the strangler pattern for migrations?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">migration</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    Component and boundary design is about minimizing coupling while preserving ownership clarity, deployability, and operational simplicity.

    In interviews, cover:

    - start with capabilities and change boundaries, not with a default “microservices everywhere” assumption
    - define interfaces around business actions and data contracts so teams can evolve independently
    - introduce BFF or edge-specific services when client needs diverge enough that a generic backend becomes a coordination bottleneck
    - watch for boundaries that look clean on diagrams but create chatty synchronous dependencies at runtime
    - for migrations, use strangler-style replacement when you need to route traffic gradually and prove the new path safely

    Strong answer tip:

    - A strong answer balances conceptual purity with operational cost: every boundary has coordination overhead.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/migration-and-evolution-strategies/#migration-strangler">🚀 See Full Deep Dive</a>


---

<div id="schema-evolution"></div>

## How do you manage schema evolution safely?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">schema</span>
  <span class="question-badge question-badge--tag">migration</span>
</div>

??? question "View Answer"

    Data design should reflect access patterns, consistency needs, and evolution pressure rather than ideological preference for one storage model.

    In interviews, cover:

    - model the dominant queries first because schema shape and storage choice should serve real read/write behavior
    - choose SQL when joins, transactions, and strong relational constraints matter; choose NoSQL when scale patterns or flexibility outweigh that rigor
    - treat indexes as read-optimization structures that also add write cost, storage cost, and operational complexity
    - plan schema evolution with backward compatibility, dual writes or readers, and safe rollout sequencing
    - explicitly discuss how the workload mix changes the architecture—for example, read-heavy systems often value caching and indexing more than strict write throughput

    Strong answer tip:

    - Interviewers like designs that clearly tie storage choices to query patterns, not “SQL for consistency, NoSQL for scale” clichés.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/migration-and-evolution-strategies/#schema-evolution">🚀 See Full Deep Dive</a>


---

<div id="tradeoff-framework"></div>

## How do you present tradeoffs clearly in interviews?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">tradeoffs</span>
  <span class="question-badge question-badge--tag">interview</span>
</div>

??? question "View Answer"

    System design interviews reward structured thinking: clarify the problem, narrow scope intelligently, and make tradeoffs explicit before diving into components.

    In interviews, cover:

    - separate functional requirements from scale, latency, availability, compliance, and cost constraints because architecture follows those boundaries
    - time-box assumptions and rough estimations so the discussion stays grounded rather than hand-wavy
    - define the first viable version of the system before exploring advanced optimizations or multi-region complexity
    - use a repeatable structure—requirements, APIs, data model, components, bottlenecks, tradeoffs, evolution path
    - state what you are intentionally not solving yet; scope discipline is a positive signal, not a weakness

    Strong answer tip:

    - Interviewers usually prefer a clearly scoped and well-defended design over an overbuilt design that never established its assumptions.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/tradeoffs-and-decision-frameworks/#tradeoff-framework">🚀 See Full Deep Dive</a>


---

<div id="cap-theorem-practical"></div>

## How do you explain CAP theorem pragmatically?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">distributed-systems</span>
  <span class="question-badge question-badge--tag">cap</span>
</div>

??? question "View Answer"

    Consistency decisions should be framed around user-visible correctness and failure handling, not abstract distributed-systems vocabulary alone.

    In interviews, cover:

    - name which operations require strong guarantees and which can tolerate eventual convergence or asynchronous repair
    - use transactions where the boundary is small and synchronous correctness is critical; use sagas where work spans services and compensation is acceptable
    - build idempotency into APIs and consumers so retries do not create duplicate side effects under failure
    - explain CAP pragmatically: partitions force tradeoffs, so the real question is which user guarantee you preserve when the network misbehaves
    - for eventually consistent systems such as search or analytics, define freshness expectations and user messaging explicitly

    Strong answer tip:

    - The strongest answers connect consistency to user experience—for example, payments and inventory feel different from search rankings or analytics counters.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/tradeoffs-and-decision-frameworks/#cap-theorem-practical">🚀 See Full Deep Dive</a>


---

<div id="read-heavy-vs-write-heavy"></div>

## How does workload shape architecture choices?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">capacity</span>
  <span class="question-badge question-badge--tag">databases</span>
</div>

??? question "View Answer"

    Data design should reflect access patterns, consistency needs, and evolution pressure rather than ideological preference for one storage model.

    In interviews, cover:

    - model the dominant queries first because schema shape and storage choice should serve real read/write behavior
    - choose SQL when joins, transactions, and strong relational constraints matter; choose NoSQL when scale patterns or flexibility outweigh that rigor
    - treat indexes as read-optimization structures that also add write cost, storage cost, and operational complexity
    - plan schema evolution with backward compatibility, dual writes or readers, and safe rollout sequencing
    - explicitly discuss how the workload mix changes the architecture—for example, read-heavy systems often value caching and indexing more than strict write throughput

    Strong answer tip:

    - Interviewers like designs that clearly tie storage choices to query patterns, not “SQL for consistency, NoSQL for scale” clichés.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/tradeoffs-and-decision-frameworks/#read-heavy-vs-write-heavy">🚀 See Full Deep Dive</a>


---

<div id="availability-vs-consistency"></div>

## How do you choose availability vs consistency?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">consistency</span>
  <span class="question-badge question-badge--tag">availability</span>
</div>

??? question "View Answer"

    Consistency decisions should be framed around user-visible correctness and failure handling, not abstract distributed-systems vocabulary alone.

    In interviews, cover:

    - name which operations require strong guarantees and which can tolerate eventual convergence or asynchronous repair
    - use transactions where the boundary is small and synchronous correctness is critical; use sagas where work spans services and compensation is acceptable
    - build idempotency into APIs and consumers so retries do not create duplicate side effects under failure
    - explain CAP pragmatically: partitions force tradeoffs, so the real question is which user guarantee you preserve when the network misbehaves
    - for eventually consistent systems such as search or analytics, define freshness expectations and user messaging explicitly

    Strong answer tip:

    - The strongest answers connect consistency to user experience—for example, payments and inventory feel different from search rankings or analytics counters.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/tradeoffs-and-decision-frameworks/#availability-vs-consistency">🚀 See Full Deep Dive</a>


---

<div id="backpressure-in-systems"></div>

## What is backpressure in distributed systems?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">backpressure</span>
  <span class="question-badge question-badge--tag">queues</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/queueing-and-async-processing/#backpressure-in-systems">🚀 See Full Deep Dive</a>


---

<div id="rate-limiting"></div>

## How do you design rate limiting?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">rate-limiting</span>
  <span class="question-badge question-badge--tag">api</span>
</div>

??? question "View Answer"

    Scalability mechanisms should be introduced when a measured bottleneck justifies their complexity, not simply because they appear in distributed-systems diagrams.

    In interviews, cover:

    - horizontal scaling, load balancing, caches, and queues each solve different constraints; combine them only where the bottleneck warrants it
    - cache-aside is often simplest operationally, but cache invalidation, TTL policy, and partial-staleness behavior need explicit design
    - queues and event-driven flows improve decoupling and absorption of bursts, but they also add retries, ordering, deduplication, and visibility concerns
    - fanout and backpressure problems should be addressed with batching, quotas, async processing, and admission control rather than infinite scale assumptions
    - rate limiting should protect both fairness and downstream stability, with clear client behavior when limits are hit

    Strong answer tip:

    - A good scalability answer explains not just what mechanism you add, but what new failure modes it introduces.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/api-design-and-gateways/#rate-limiting">🚀 See Full Deep Dive</a>


---

<div id="tenant-isolation"></div>

## How do you design multi-tenant isolation?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">multi-tenant</span>
  <span class="question-badge question-badge--tag">security</span>
</div>

??? question "View Answer"

    External interface design should balance client simplicity, backward compatibility, security boundaries, and operational evolvability.

    In interviews, cover:

    - API gateways are useful for auth, routing, throttling, and cross-cutting concerns, but they should not become opaque monoliths of business logic
    - choose REST where broad interoperability and caching matter; choose gRPC where low-latency internal contracts and typed schemas provide leverage
    - design versioning and deprecation paths early so clients are never forced into emergency upgrades
    - separate authentication from authorization in both system boundaries and failure reasoning
    - for multi-tenant systems, isolate data, compute, quotas, and observability strongly enough that one tenant cannot degrade or inspect another

    Strong answer tip:

    - Interviewers like when you mention not only the happy path but also abuse resistance, key rotation, and backward compatibility.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/security-and-compliance/#tenant-isolation">🚀 See Full Deep Dive</a>


---

<div id="data-retention"></div>

## How do retention policies affect architecture?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">compliance</span>
  <span class="question-badge question-badge--tag">data</span>
</div>

??? question "View Answer"

    Operational architecture should make reliability, observability, and recovery explicit design dimensions rather than afterthoughts.

    In interviews, cover:

    - use SLOs to decide how much redundancy, latency headroom, and alerting sophistication the system actually needs
    - logs, metrics, and traces answer different questions, so mature observability designs use all three intentionally
    - timeouts, retries, circuit breakers, and bulkheads should be tuned together because the wrong combination amplifies incidents
    - multi-region and disaster recovery decisions should be tied to RPO/RTO goals and justified by business impact, not prestige
    - cost, headroom, and retention policies are architectural constraints: they shape data flow, storage choices, and safety margins

    Strong answer tip:

    - A strong answer names the recovery objective and the operational tradeoff, not just “we would use multi-region for reliability.”

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/security-and-compliance/#data-retention">🚀 See Full Deep Dive</a>


---

<div id="design-round-structure"></div>

## What is a strong structure for solving design rounds?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">interview</span>
  <span class="question-badge question-badge--tag">communication</span>
</div>

??? question "View Answer"

    System design interviews reward structured thinking: clarify the problem, narrow scope intelligently, and make tradeoffs explicit before diving into components.

    In interviews, cover:

    - separate functional requirements from scale, latency, availability, compliance, and cost constraints because architecture follows those boundaries
    - time-box assumptions and rough estimations so the discussion stays grounded rather than hand-wavy
    - define the first viable version of the system before exploring advanced optimizations or multi-region complexity
    - use a repeatable structure—requirements, APIs, data model, components, bottlenecks, tradeoffs, evolution path
    - state what you are intentionally not solving yet; scope discipline is a positive signal, not a weakness

    Strong answer tip:

    - Interviewers usually prefer a clearly scoped and well-defended design over an overbuilt design that never established its assumptions.

    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/system-design-fundamentals/#design-round-structure">🚀 See Full Deep Dive</a>


---

<div id="design-a-push-notification-system-end-to-end-with-privacy-and-delivery"></div>

## Design a push notification system end-to-end with privacy and delivery correctness

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">push-notifications</span>
  <span class="question-badge question-badge--tag">fcm</span>
  <span class="question-badge question-badge--tag">privacy</span>
  <span class="question-badge question-badge--tag">reliability</span>
</div>

??? question "View Answer"

    A production push notification system must balance reliability (at-least-once delivery), privacy (minimal payload exposure), and user control (preferences, opt-out).
    In interviews, cover:
    - architecture: notification service → message queue (Kafka/SQS) → sender worker pool → FCM/APNs; decouple sending from triggering to handle burst traffic
    - privacy: send data-only notifications (notification ID only); the app calls a secured endpoint to fetch notification content with authentication — payload never traverses FCM in plaintext
    - delivery guarantees: FCM provides at-least-once delivery with TTL; for critical alerts (payment received), implement server-side read receipts and retry logic if no acknowledgement within TTL window
    - user preferences: maintain per-user, per-notification-type opt-in/out preferences server-side; never rely solely on client settings which can be stale
    - silent notifications for data sync: use FCM data messages with a low priority budget; do not exceed system-imposed limits (20 high-priority messages per hour per device on Android 13+)
    Strong answer tip:
    - discuss notification deduplication: if a notification for order #123 is generated twice (retry), the device must not show two toasts; use a deterministic notification ID (hash of entity type + entity ID)


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/system-design-fundamentals/#design-a-push-notification-system-end-to-end-with-privacy-and-delivery">🚀 See Full Deep Dive</a>


---

<div id="design-app-modularization-for-a-large-compose-app-with-100-screens"></div>

## Design app modularization for a large Compose app with 100+ screens

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">modularization</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">compose</span>
  <span class="question-badge question-badge--tag">gradle</span>
</div>

??? question "View Answer"

    Modularizing a large Compose app requires a layered module graph that prevents circular dependencies, enables parallel builds, and gives feature teams independent release velocity.
    In interviews, cover:
    - module types: :core:ui (design system, shared composables), :core:data (repositories, Room), :core:domain (use cases, business logic), :feature:X (each feature as an independent module with its own ViewModel/Screen)
    - dependency direction: feature → domain → data; feature → core:ui; never data → feature (avoids cycles); enforce with Gradle module-specific dependency constraints or Lint rules
    - navigation: central nav graph in a :navigation module that references feature entry points by route string — features do not know about each other; use NavigationBuilder extension functions
    - build impact: modules with separate compilation units allow Gradle to compile changed modules in parallel; features with stable interfaces benefit from build caching
    - dynamic delivery: large features (AR, video editor) as Play Feature Delivery modules — only installed when needed
    Strong answer tip:
    - identify the top 3 most-changed modules in your repo history; these should be the smallest and most isolated modules in your graph — changes to them should not trigger recompilation of the entire dependency tree


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/system-design-fundamentals/#design-app-modularization-for-a-large-compose-app-with-100-screens">🚀 See Full Deep Dive</a>


---

<div id="design-api-versioning-and-backward-compatibility-strategy-for-mobile-r"></div>

## Design API versioning and backward compatibility strategy for mobile releases

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--advanced">advanced</span>
  <span class="question-badge question-badge--tag">system-design</span>
  <span class="question-badge question-badge--tag">api-design</span>
  <span class="question-badge question-badge--tag">versioning</span>
  <span class="question-badge question-badge--tag">backward-compatibility</span>
  <span class="question-badge question-badge--tag">mobile</span>
</div>

??? question "View Answer"

    Mobile apps have a long tail of versions in the wild — API versioning must ensure old clients continue working while new clients get new capabilities.
    In interviews, cover:
    - version header approach: clients send X-App-Version or Accept: application/vnd.example.v2+json; the server routes to the appropriate handler; simpler than URL versioning for mobile where the client is always known
    - additive-only changes: add new fields, never remove or rename; use Kotlin's @JsonClass(generateAdapter=true) or kotlinx.serialization with ignoreUnknownKeys=true so old clients skip new fields
    - deprecation policy: mark an API path/field as deprecated and support it for M major app versions (e.g. 3 versions = ~6 months); track client version distribution to know when usage of old paths is zero
    - sunset header: return Deprecation: true and Sunset: <date> headers from deprecated endpoints; client-side analytics detect these and alert engineers
    - feature flags + minimum version: gate backend features behind a minimum app version check; use RemoteConfig or a server-side capability negotiation endpoint
    Strong answer tip:
    - the most common mistake is breaking changes deployed as a same-version update; always treat any response schema change as potentially breaking and design for forward compatibility (client parses only what it knows)


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/system-design-fundamentals/#design-api-versioning-and-backward-compatibility-strategy-for-mobile-r">🚀 See Full Deep Dive</a>

