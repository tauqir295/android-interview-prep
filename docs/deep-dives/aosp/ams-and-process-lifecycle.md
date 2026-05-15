---
hide:
  - toc
---

## AMS and Process Lifecycle Deep Dive

## Overview

`ActivityManagerService` (AMS) is the policy engine for process states, component
lifecycle coordination, and process importance tracking in Android.

## Process importance model

AMS continually recomputes process state and OOM adjustment from:

- visible activities
- foreground services
- bound service dependencies
- broadcasts/jobs currently executing

These values guide LMKD kill priority under pressure.

## Lifecycle orchestration

AMS coordinates transitions across activities, services, and receivers:

- start/resume/pause/stop callbacks
- process launch/attach handshake
- binding and unbinding service edges
- background execution constraints by API level

## Memory pressure interaction

LMKD uses pressure signals plus AMS importance:

- cached/background are first victims
- visible/foreground protected as long as possible
- repeated kill/restart loops indicate architecture issues

## Race conditions to watch

- callback returns after UI owner destroyed
- bind/unbind around configuration change
- async work outliving process importance downgrade

Mitigate with lifecycle-aware scopes and idempotent cleanup paths.

## API-level policy evolution

- API 26+ background service restrictions
- foreground service visibility requirements
- app standby buckets and quota behavior
- stricter start limits in newer platform versions

## Interview guidance

Strong answers connect AMS policy to product outcomes:

- startup speed
- background reliability
- ANR/kill incidence
- battery and quota compliance

