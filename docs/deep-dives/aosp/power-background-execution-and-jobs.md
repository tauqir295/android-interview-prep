---
hide:
  - toc
---

## Power Background Execution and Jobs Deep Dive

## Overview

Modern Android background work is policy-driven. Doze, standby buckets, quota
systems, and foreground-service rules shape when and how work executes.

## Doze model

Doze defers background activity during device idle and opens periodic
maintenance windows for batched execution.

## App Standby Buckets

Apps are bucketed by engagement level. Bucket impacts:

- job frequency
- alarm quotas
- network execution opportunities

## API choice matrix

- WorkManager: durable deferred work with constraints
- JobScheduler: scheduler primitive under modern APIs
- ForegroundService: immediate, user-visible ongoing work

## Wakelock discipline

Common battery regressions:

- missing release on failure path
- long-held wakelocks during retries
- overlapping alarms and wakelocks

Use timeout defaults, ownership logging, and release assertions in tests.

## Reliability design

Given quotas and idle policy, design for eventual completion:

- idempotent work units
- retry with backoff
- explicit stale-data tolerances
- user-facing messaging for delayed operations

## Interview guidance

A strong answer links policy constraints to product SLA decisions and shows
tradeoff awareness between immediacy, battery, and compliance.
