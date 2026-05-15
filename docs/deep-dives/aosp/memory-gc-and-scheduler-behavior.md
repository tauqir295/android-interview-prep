---
hide:
  - toc
---

## Memory GC and Scheduler Behavior Deep Dive

## Overview

User-perceived performance in Android is strongly affected by heap behavior,
GC events, scheduler decisions, and context-switch overhead.

## ART GC behavior

GC can impact frame timing through:

- pause windows
- concurrent mark/scan CPU usage
- allocation churn from UI and data pipelines

Reduce allocation pressure in hot paths before trying low-level tuning.

## Scheduler impact

Linux CFS plus cgroup and priority controls define CPU distribution. Misuse of
priorities can improve one path while starving others.

## Thread priority anti-patterns

- elevating background work close to UI priority
- long blocking calls on priority-sensitive threads
- lock inversion between mixed-priority workers

## Context-switch overhead

In IPC-heavy systems, excess process hops and synchronous chains increase
context-switch and wakeup overhead.

Mitigation:

- reduce unnecessary synchronous boundaries
- batch operations
- minimize binder nesting in critical paths

## Measurement strategy

Correlate:

- frame metrics
- GC event timings
- scheduler run queue pressure
- context-switch counts and tail latency

## Interview guidance

Strong answers connect allocator and scheduler behavior to concrete user-level
SLOs, not only microbenchmarks.
