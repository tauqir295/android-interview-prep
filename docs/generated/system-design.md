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

    What is Android system design in interviews? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `architecture`


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

    How do you separate functional vs non-functional requirements? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `requirements`


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

    How do you define scope for a system design round? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `requirements`


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

    How do you do quick capacity estimations? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `capacity`


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

    How do you structure high-level components? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `architecture`


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

    How do you define service boundaries? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `microservices`


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

    How do you approach data modeling in system design? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `data`


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

    When do you choose SQL vs NoSQL? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `databases`


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

    How do indexes affect read and write performance? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `database`


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

    What consistency models should you discuss in interviews? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `consistency`


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

    When should you use transactions vs sagas? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `transactions`


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

    How do you scale a system horizontally? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `scalability`


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

    How do load balancers fit into architecture design? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `networking`


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

    What is cache-aside and when is it useful? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `caching`


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

    Why is cache invalidation hard? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `caching`


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

    When do you add a message queue? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `queues`


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

    What are event-driven architecture tradeoffs? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `events`


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

    What role does an API gateway play? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `api`


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

    How do you choose REST vs gRPC for internal APIs? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `api`


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

    How do you version APIs safely? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `api`


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

    How do you model authentication vs authorization? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `security`


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

    What security hardening do you mention in interviews? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `security`


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

    How do SLOs/SLAs shape architecture decisions? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `observability`


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

    Why are logs, metrics, and traces all needed? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `observability`


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

    What is a circuit breaker and why use it? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `resilience`


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

    How do timeouts, retries, and bulkheads work together? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `resilience`


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

    Why is idempotency important in distributed systems? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `reliability`


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

    When do you move to multi-region architecture? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `multi-region`


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

    How do RPO and RTO influence disaster recovery design? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `dr`


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

    How do you balance cost vs latency? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `cost`


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

    How much capacity headroom should a production system keep? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `capacity`


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

    What is Backend-for-Frontend (BFF) and when should Android use it? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `bff`


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

    How does edge caching improve mobile user experience? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `cdn`


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

    How would you design a real-time chat backend? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `realtime`


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

    How do you handle fan-out at scale? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `realtime`


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

    How do you design search for low-latency queries? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `search`


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

    Why is search often eventually consistent? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `search`


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

    How do you design analytics ingestion pipelines? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `analytics`


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

    When do you choose batch vs stream processing? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `analytics`


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

    What is the strangler pattern for migrations? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `migration`


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

    How do you manage schema evolution safely? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `schema`


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

    How do you present tradeoffs clearly in interviews? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `tradeoffs`


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

    How do you explain CAP theorem pragmatically? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `distributed-systems`


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

    How does workload shape architecture choices? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `capacity`


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

    How do you choose availability vs consistency? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `consistency`


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

    What is backpressure in distributed systems? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `backpressure`


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

    How do you design rate limiting? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `rate-limiting`


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

    How do you design multi-tenant isolation? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `multi-tenant`


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

    How do retention policies affect architecture? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `compliance`


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

    What is a strong structure for solving design rounds? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `system-design` choices to measurable outcomes in `interview`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/system-design/system-design-fundamentals/#design-round-structure">🚀 See Full Deep Dive</a>

