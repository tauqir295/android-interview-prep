---
hide:
  - toc
---

# Testing

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

<div id="testing-strategy"></div>

## How do you define an Android testing strategy?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">strategy</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    How do you define an Android testing strategy? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `strategy`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/testing-fundamentals/#testing-strategy">🚀 See Full Deep Dive</a>


---

<div id="test-pyramid"></div>

## What is the test pyramid and why does it matter?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">test-pyramid</span>
  <span class="question-badge question-badge--tag">quality</span>
</div>

??? question "View Answer"

    What is the test pyramid and why does it matter? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `test-pyramid`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/test-pyramid-and-strategy/#test-pyramid">🚀 See Full Deep Dive</a>


---

<div id="unit-vs-integration"></div>

## What is the difference between unit and integration tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--beginner">beginner</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">unit-testing</span>
  <span class="question-badge question-badge--tag">integration-testing</span>
</div>

??? question "View Answer"

    What is the difference between unit and integration tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `unit-testing`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/test-pyramid-and-strategy/#unit-vs-integration">🚀 See Full Deep Dive</a>


---

<div id="viewmodel-unit-tests"></div>

## How do you unit test a ViewModel?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">viewmodel</span>
  <span class="question-badge question-badge--tag">unit-testing</span>
</div>

??? question "View Answer"

    How do you unit test a ViewModel? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `viewmodel`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/unit-testing-viewmodel/#viewmodel-unit-tests">🚀 See Full Deep Dive</a>


---

<div id="usecase-tests"></div>

## How should use cases be tested?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">domain</span>
  <span class="question-badge question-badge--tag">unit-testing</span>
</div>

??? question "View Answer"

    How should use cases be tested? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `domain`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/unit-testing-viewmodel/#usecase-tests">🚀 See Full Deep Dive</a>


---

<div id="repository-tests"></div>

## How do you test repository logic with multiple data sources?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">repository</span>
  <span class="question-badge question-badge--tag">data-layer</span>
</div>

??? question "View Answer"

    How do you test repository logic with multiple data sources? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `repository`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/repository-and-data-layer-testing/#repository-tests">🚀 See Full Deep Dive</a>


---

<div id="datasource-tests"></div>

## How do you test remote and local data sources?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">data-layer</span>
  <span class="question-badge question-badge--tag">repository</span>
</div>

??? question "View Answer"

    How do you test remote and local data sources? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `data-layer`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/repository-and-data-layer-testing/#datasource-tests">🚀 See Full Deep Dive</a>


---

<div id="integration-boundary"></div>

## When should you add integration tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">integration-testing</span>
  <span class="question-badge question-badge--tag">strategy</span>
</div>

??? question "View Answer"

    When should you add integration tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `integration-testing`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/integration-testing/#integration-boundary">🚀 See Full Deep Dive</a>


---

<div id="compose-ui-tests"></div>

## How do Compose UI tests differ from View UI tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">compose</span>
  <span class="question-badge question-badge--tag">ui-testing</span>
</div>

??? question "View Answer"

    How do Compose UI tests differ from View UI tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `compose`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/ui-testing-with-compose/#compose-ui-tests">🚀 See Full Deep Dive</a>


---

<div id="semantics-testing"></div>

## Why are semantics important in Compose tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">compose</span>
  <span class="question-badge question-badge--tag">accessibility</span>
</div>

??? question "View Answer"

    Why are semantics important in Compose tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `compose`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/ui-testing-with-compose/#semantics-testing">🚀 See Full Deep Dive</a>


---

<div id="espresso-basics"></div>

## When do you still use Espresso?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">espresso</span>
  <span class="question-badge question-badge--tag">ui-testing</span>
</div>

??? question "View Answer"

    When do you still use Espresso? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `espresso`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/espresso-and-ui-automation/#espresso-basics">🚀 See Full Deep Dive</a>


---

<div id="idling-resources"></div>

## What are idling resources and when are they needed?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">espresso</span>
  <span class="question-badge question-badge--tag">synchronization</span>
</div>

??? question "View Answer"

    What are idling resources and when are they needed? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `espresso`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/espresso-and-ui-automation/#idling-resources">🚀 See Full Deep Dive</a>


---

<div id="mocks-vs-fakes"></div>

## When should you use mocks vs fakes?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">mocks</span>
  <span class="question-badge question-badge--tag">fakes</span>
</div>

??? question "View Answer"

    When should you use mocks vs fakes? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `mocks`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/mocking-fakes-and-stubs/#mocks-vs-fakes">🚀 See Full Deep Dive</a>


---

<div id="stub-vs-spy"></div>

## What is the difference between stubs and spies?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">mocks</span>
  <span class="question-badge question-badge--tag">unit-testing</span>
</div>

??? question "View Answer"

    What is the difference between stubs and spies? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `mocks`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/mocking-fakes-and-stubs/#stub-vs-spy">🚀 See Full Deep Dive</a>


---

<div id="coroutine-test"></div>

## How do you test coroutines deterministically?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">kotlin</span>
</div>

??? question "View Answer"

    How do you test coroutines deterministically? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `coroutines`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/coroutine-and-flow-testing/#coroutine-test">🚀 See Full Deep Dive</a>


---

<div id="virtual-time"></div>

## Why is virtual time important for async tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">coroutines</span>
  <span class="question-badge question-badge--tag">virtual-time</span>
</div>

??? question "View Answer"

    Why is virtual time important for async tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `coroutines`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/coroutine-and-flow-testing/#virtual-time">🚀 See Full Deep Dive</a>


---

<div id="flow-test-patterns"></div>

## How do you test Flow emissions?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">flow</span>
  <span class="question-badge question-badge--tag">coroutines</span>
</div>

??? question "View Answer"

    How do you test Flow emissions? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `flow`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/coroutine-and-flow-testing/#flow-test-patterns">🚀 See Full Deep Dive</a>


---

<div id="stateflow-testing"></div>

## How do you test StateFlow UI state?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">stateflow</span>
  <span class="question-badge question-badge--tag">ui-state</span>
</div>

??? question "View Answer"

    How do you test StateFlow UI state? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `stateflow`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/stateflow-sharedflow-testing/#stateflow-testing">🚀 See Full Deep Dive</a>


---

<div id="sharedflow-events-testing"></div>

## How do you test one-off SharedFlow events?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">sharedflow</span>
  <span class="question-badge question-badge--tag">events</span>
</div>

??? question "View Answer"

    How do you test one-off SharedFlow events? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `sharedflow`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/stateflow-sharedflow-testing/#sharedflow-events-testing">🚀 See Full Deep Dive</a>


---

<div id="mockwebserver"></div>

## Why use MockWebServer for networking tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">mockwebserver</span>
</div>

??? question "View Answer"

    Why use MockWebServer for networking tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `networking`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/network-testing-and-mockwebserver/#mockwebserver">🚀 See Full Deep Dive</a>


---

<div id="api-contract-tests"></div>

## How do you keep API tests resilient to server changes?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">networking</span>
  <span class="question-badge question-badge--tag">contract-testing</span>
</div>

??? question "View Answer"

    How do you keep API tests resilient to server changes? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `networking`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/contract-testing/#api-contract-tests">🚀 See Full Deep Dive</a>


---

<div id="room-inmemory-tests"></div>

## How do you test Room with in-memory databases?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">room</span>
  <span class="question-badge question-badge--tag">database</span>
</div>

??? question "View Answer"

    How do you test Room with in-memory databases? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `room`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/database-testing-room/#room-inmemory-tests">🚀 See Full Deep Dive</a>


---

<div id="migration-tests"></div>

## Why are Room migration tests critical?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">room</span>
  <span class="question-badge question-badge--tag">migration</span>
</div>

??? question "View Answer"

    Why are Room migration tests critical? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `room`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/database-testing-room/#migration-tests">🚀 See Full Deep Dive</a>


---

<div id="testable-architecture"></div>

## What makes Android architecture testable?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">architecture</span>
  <span class="question-badge question-badge--tag">design</span>
</div>

??? question "View Answer"

    What makes Android architecture testable? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `architecture`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/testability-and-architecture/#testable-architecture">🚀 See Full Deep Dive</a>


---

<div id="dependency-injection-testing"></div>

## How does DI improve testability?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">di</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    How does DI improve testability? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `di`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/testability-and-architecture/#dependency-injection-testing">🚀 See Full Deep Dive</a>


---

<div id="flaky-tests"></div>

## What causes flaky tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">flaky-tests</span>
  <span class="question-badge question-badge--tag">quality</span>
</div>

??? question "View Answer"

    What causes flaky tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `flaky-tests`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/flaky-test-diagnostics/#flaky-tests">🚀 See Full Deep Dive</a>


---

<div id="stabilize-ui-tests"></div>

## How do you stabilize flaky UI tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">ui-testing</span>
  <span class="question-badge question-badge--tag">flaky-tests</span>
</div>

??? question "View Answer"

    How do you stabilize flaky UI tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `ui-testing`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/flaky-test-diagnostics/#stabilize-ui-tests">🚀 See Full Deep Dive</a>


---

<div id="benchmark-tests"></div>

## When should you add benchmark tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">performance</span>
  <span class="question-badge question-badge--tag">benchmark</span>
</div>

??? question "View Answer"

    When should you add benchmark tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `performance`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/performance-and-benchmark-testing/#benchmark-tests">🚀 See Full Deep Dive</a>


---

<div id="macrobenchmark"></div>

## What does Macrobenchmark validate?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">macrobenchmark</span>
  <span class="question-badge question-badge--tag">performance</span>
</div>

??? question "View Answer"

    What does Macrobenchmark validate? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `macrobenchmark`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/performance-and-benchmark-testing/#macrobenchmark">🚀 See Full Deep Dive</a>


---

<div id="golden-tests"></div>

## What are snapshot or golden tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">snapshot</span>
  <span class="question-badge question-badge--tag">ui-testing</span>
</div>

??? question "View Answer"

    What are snapshot or golden tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `snapshot`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/snapshot-and-golden-testing/#golden-tests">🚀 See Full Deep Dive</a>


---

<div id="visual-regression"></div>

## How do visual regression tests fit release safety?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">snapshot</span>
  <span class="question-badge question-badge--tag">release</span>
</div>

??? question "View Answer"

    How do visual regression tests fit release safety? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `snapshot`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/snapshot-and-golden-testing/#visual-regression">🚀 See Full Deep Dive</a>


---

<div id="consumer-contract"></div>

## What is consumer-driven contract testing?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">contract-testing</span>
  <span class="question-badge question-badge--tag">api</span>
</div>

??? question "View Answer"

    What is consumer-driven contract testing? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `contract-testing`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/contract-testing/#consumer-contract">🚀 See Full Deep Dive</a>


---

<div id="e2e-tests"></div>

## What are good use cases for end-to-end tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">e2e</span>
  <span class="question-badge question-badge--tag">strategy</span>
</div>

??? question "View Answer"

    What are good use cases for end-to-end tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `e2e`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/e2e-testing-and-release-gates/#e2e-tests">🚀 See Full Deep Dive</a>


---

<div id="release-gates"></div>

## How should tests gate production releases?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">release</span>
  <span class="question-badge question-badge--tag">quality</span>
</div>

??? question "View Answer"

    How should tests gate production releases? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `release`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/e2e-testing-and-release-gates/#release-gates">🚀 See Full Deep Dive</a>


---

<div id="ci-pipeline"></div>

## How do you design a fast CI test pipeline?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">ci</span>
  <span class="question-badge question-badge--tag">automation</span>
</div>

??? question "View Answer"

    How do you design a fast CI test pipeline? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `ci`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/ci-cd-test-pipelines/#ci-pipeline">🚀 See Full Deep Dive</a>


---

<div id="sharding-tests"></div>

## When should you shard test suites?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">ci</span>
  <span class="question-badge question-badge--tag">scalability</span>
</div>

??? question "View Answer"

    When should you shard test suites? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `ci`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/ci-cd-test-pipelines/#sharding-tests">🚀 See Full Deep Dive</a>


---

<div id="test-reporting"></div>

## What metrics should test reports include?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">metrics</span>
  <span class="question-badge question-badge--tag">quality</span>
</div>

??? question "View Answer"

    What metrics should test reports include? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `metrics`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/test-metrics-and-quality-governance/#test-reporting">🚀 See Full Deep Dive</a>


---

<div id="quality-gates"></div>

## How do quality gates prevent regressions?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">quality</span>
  <span class="question-badge question-badge--tag">governance</span>
</div>

??? question "View Answer"

    How do quality gates prevent regressions? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `quality`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/test-metrics-and-quality-governance/#quality-gates">🚀 See Full Deep Dive</a>


---

<div id="mutation-testing"></div>

## Where does mutation testing fit in Android?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">mutation-testing</span>
  <span class="question-badge question-badge--tag">quality</span>
</div>

??? question "View Answer"

    Where does mutation testing fit in Android? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `mutation-testing`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/test-metrics-and-quality-governance/#mutation-testing">🚀 See Full Deep Dive</a>


---

<div id="hermetic-tests"></div>

## What are hermetic tests and why are they valuable?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">hermetic</span>
  <span class="question-badge question-badge--tag">reliability</span>
</div>

??? question "View Answer"

    What are hermetic tests and why are they valuable? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `hermetic`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/test-pyramid-and-strategy/#hermetic-tests">🚀 See Full Deep Dive</a>


---

<div id="test-data-builders"></div>

## Why use test data builders?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">unit-testing</span>
  <span class="question-badge question-badge--tag">maintainability</span>
</div>

??? question "View Answer"

    Why use test data builders? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `unit-testing`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/mocking-fakes-and-stubs/#test-data-builders">🚀 See Full Deep Dive</a>


---

<div id="clock-abstraction"></div>

## How does clock abstraction improve test reliability?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">time</span>
  <span class="question-badge question-badge--tag">architecture</span>
</div>

??? question "View Answer"

    How does clock abstraction improve test reliability? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `time`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/unit-testing-viewmodel/#clock-abstraction">🚀 See Full Deep Dive</a>


---

<div id="retry-in-tests"></div>

## Should flaky tests be fixed with retries?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">flaky-tests</span>
  <span class="question-badge question-badge--tag">ci</span>
</div>

??? question "View Answer"

    Should flaky tests be fixed with retries? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `flaky-tests`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/flaky-test-diagnostics/#retry-in-tests">🚀 See Full Deep Dive</a>


---

<div id="android-test-runner"></div>

## How do you structure instrumentation test modules?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">instrumentation</span>
  <span class="question-badge question-badge--tag">android</span>
</div>

??? question "View Answer"

    How do you structure instrumentation test modules? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `instrumentation`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/espresso-and-ui-automation/#android-test-runner">🚀 See Full Deep Dive</a>


---

<div id="test-environments"></div>

## How do you manage test environments across teams?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">environments</span>
  <span class="question-badge question-badge--tag">operations</span>
</div>

??? question "View Answer"

    How do you manage test environments across teams? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `environments`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/ci-cd-test-pipelines/#test-environments">🚀 See Full Deep Dive</a>


---

<div id="contract-mocks"></div>

## How do contracts reduce mock drift?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">contract-testing</span>
  <span class="question-badge question-badge--tag">mocks</span>
</div>

??? question "View Answer"

    How do contracts reduce mock drift? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `contract-testing`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/contract-testing/#contract-mocks">🚀 See Full Deep Dive</a>


---

<div id="qa-dev-collaboration"></div>

## How should QA and dev collaborate on automation?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">collaboration</span>
  <span class="question-badge question-badge--tag">process</span>
</div>

??? question "View Answer"

    How should QA and dev collaborate on automation? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `collaboration`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/testing-fundamentals/#qa-dev-collaboration">🚀 See Full Deep Dive</a>


---

<div id="risk-based-testing"></div>

## What is risk-based testing?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--intermediate">intermediate</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">strategy</span>
  <span class="question-badge question-badge--tag">risk</span>
</div>

??? question "View Answer"

    What is risk-based testing? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `strategy`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/test-pyramid-and-strategy/#risk-based-testing">🚀 See Full Deep Dive</a>


---

<div id="postmortem-regression-tests"></div>

## How do you turn incidents into regression tests?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--senior">senior</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">postmortem</span>
  <span class="question-badge question-badge--tag">quality</span>
</div>

??? question "View Answer"

    How do you turn incidents into regression tests? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `postmortem`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/test-metrics-and-quality-governance/#postmortem-regression-tests">🚀 See Full Deep Dive</a>


---

<div id="test-maintenance-cost"></div>

## How do you manage long-term test maintenance cost?

<div class="question-meta">
  <span class="question-badge question-badge--difficulty question-badge--staff">staff</span>
  <span class="question-badge question-badge--tag">testing</span>
  <span class="question-badge question-badge--tag">maintainability</span>
  <span class="question-badge question-badge--tag">strategy</span>
</div>

??? question "View Answer"

    How do you manage long-term test maintenance cost? is primarily about making clear, practical decisions.

    In interviews, cover:

    - definition in one sentence
    - when to use it and when not to
    - tradeoffs (latency, reliability, complexity, cost)
    - a production example from your team

    Strong answer tip:

    - connect `testing` choices to measurable outcomes in `maintainability`


    <a class="question-dive-link" href="/android-interview-prep/deep-dives/testing/testability-and-architecture/#test-maintenance-cost">🚀 See Full Deep Dive</a>

