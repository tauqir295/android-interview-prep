---
hide:
  - toc
---

## Zygote ART and App Startup Deep Dive

## Overview

Android startup performance combines process forking via Zygote and runtime
execution strategy in ART (AOT + JIT + profile-guided optimization).

## Why Zygote exists

Zygote preloads common framework classes/resources once, then forks apps.
Copy-on-write allows sharing clean pages until mutation.

Benefits:

- faster process creation
- reduced duplicated memory
- lower startup initialization cost

## ART execution strategy

ART balances install cost and run-time speed with:

- baseline profile guided compile
- JIT for runtime hotspots
- selective AOT artifacts

## Startup hidden costs

- class verification and linking at first touch
- heavy static initializers
- deep dependency graph pull-in

Move expensive setup off critical first-frame path when possible.

## Baseline profiles

Profiles mark methods that should be precompiled for startup and key journeys.
Stale profiles regress first-run performance after feature changes.

## Measurement

Track:

- cold/warm/hot startup times
- first frame and first interaction latency
- class loading and initialization events in trace

## Interview guidance

Good answers discuss both memory and startup speed. Great answers include an
operational loop: generate profile, ship, measure, refresh.
