---
hide:
  - toc
---

## WindowManager SurfaceFlinger Render Pipeline Deep Dive

## Overview

Android frame delivery is a pipeline from app rendering to compositor present.
Missing deadline at any stage causes jank.

## Main stages

1. UI thread computes state and records commands.
2. RenderThread submits GPU work.
3. Buffers move through BufferQueue.
4. SurfaceFlinger latches latest ready buffers.
5. Hardware Composer composes and presents.

## Input and focus

WindowManager + InputDispatcher define trusted routing:

- focused window gets key events
- touch dispatch depends on hit test and policy
- secure/obscured window checks protect against abuse

## Jank root-cause classes

- app-side: expensive measure/layout/draw work
- GPU-side: shader stalls, upload spikes
- compositor-side: late latch, layer complexity
- scheduler-side: thread preemption, frequency throttling

## Triple buffering tradeoff

- smoother frame throughput under jitter
- higher input-to-photon latency if queue is deep

Treat this as an explicit UX tradeoff with measurement.

## How to diagnose correctly

Use Perfetto FrameTimeline and graphics tracks to separate:

- app frame cost
- GPU completion delay
- SurfaceFlinger present delay

## Interview guidance

A strong answer names pipeline stages and metrics per stage, not only "jank due
to slow UI thread".
