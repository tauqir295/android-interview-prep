# Choreographer & Animation Timing Deep Dive

**Question ID**: advanced-25  
**Difficulty**: Intermediate  
**Tags**: animation, rendering, performance

## Core Concept

Choreographer is a callback-based orchestrator that syncs animations and view updates to the display refresh rate (typically 60Hz = 16.67ms per frame). By aligning work with vsync, Choreographer prevents jank and enables smooth motion.

## Key Areas Covered

### Vsync Synchronization
- **Vsync pulse**: Display hardware signals every 16.67ms (60Hz) that it's ready for new frame
- **Choreographer.postFrameCallback()**: Queued at next vsync; guaranteed execution before frame deadline
- **All callbacks fire together**: Batched before rendering, preserving 60fps
- **Predictable timing**: Developers can count on callback timing relative to display refresh

### Three Callback Types
- **Input callbacks**: Touch events dispatched first (highest priority)
- **Animation callbacks**: PropertyAnimator, ValueAnimator update values
- **Traversal callbacks**: measure/layout/draw happens last
- **Ordering matters**: Input doesn't wait for animation to complete

### Frame Pacing
- **Frame budget**: 16.67ms total (1000ms / 60fps) to do all work
- **Exceeding budget**: If frame takes 18ms, vsync deadline missed → frame dropped → visible stutter
- **Frame pipelining**: RenderThread can work on frame N while main thread prepares N+1 (hides some latency)
- **Example**: If main thread takes 12ms and RT takes 15ms, only 12ms visible latency (overlapped)

### Interpolation & Motion
- **Animation value**: `value = startValue + (endValue - startValue) * interpolator.getInterpolation(elapsed / duration)`
- **Linear interpolator**: Constant velocity (smooth motion)
- **Ease-in/Ease-out**: Acceleration/deceleration (feels natural)
- **Overshoot**: Bounce past target then settle (playful, bouncy)
- **Interpolation cost**: Negligible (usually < 1ms per frame)

### Testing & Verification
- **Perfetto**: Profiler showing vsync boundaries and frame drop detection
- **Choreographer.FrameCallback**: Manual vsync callbacks for testing
- **Expected result**: Every callback fires, frames don't drop

## Real-World Patterns

### Pattern: PropertyAnimator vs Handler Loop
```kotlin
// Problem: Manual Handler loop has no vsync awareness
Handler().post(object : Runnable {
  override fun run() {
    view.translationX += 5
    handler.postDelayed(this, 16)  // Hopes to hit 16ms, might miss
  }
})

// Better: PropertyAnimator syncs to vsync
ObjectAnimator.ofFloat(view, "translationX", 0f, 100f).apply {
  duration = 500
  interpolator = LinearInterpolator()
  start()  // Internally uses Choreographer
}
```

### Pattern: Choreographer for Custom Animation
```kotlin
Choreographer.getInstance().postFrameCallback(object : Choreographer.FrameCallback {
  override fun doFrame(frameTimeNanos: Long) {
    val elapsedMs = (frameTimeNanos - startTimeNanos) / 1_000_000
    val progress = (elapsedMs / 500f).coerceIn(0f, 1f)  // 500ms duration
    view.alpha = startAlpha + (endAlpha - startAlpha) * progress
    
    if (progress < 1f) {
      Choreographer.getInstance().postFrameCallback(this)  // Schedule next frame
    }
  }
})
```

### Pattern: Animation Jank from Slow Main Thread
```
Frame 1 (0ms): Choreographer callback fires
  Main thread busy with GC pause (20ms)
  Can't render frame 1, deadline missed
Frame 2 (16.67ms): Vsync pulse, frame 1 finally renders (late)
  Frame 1 displayed 16.67ms late → visible jank
```

## Tradeoffs

| Factor | Tight Animation Loop | Sparse Updates |
|--------|------------------|-----------------|
| Smoothness | Smooth (60fps) | Choppy (fewer frames) |
| CPU Cost | Higher (callback per frame) | Lower (fewer callbacks) |
| Battery | More drain | Less drain |
| Use Case | UI animations | Progress bars (low frequency) |

## Interview Signals

### Strong answers include:
- Understanding vsync pulse and why Choreographer syncs to it
- Knowing PropertyAnimator internally uses Choreographer (advantage over Handler loop)
- Aware that frame pipelining hides latency between main thread and RenderThread
- Can explain why custom Handler loops miss vsync vs Choreographer
- Understanding interpolation and how it affects perceived motion

### Weak answers:
- Thinking animation just needs to occur every 16ms (doesn't understand vsync synchronization)
- Not knowing Choreographer exists or its benefit
- Confusing animation frame callbacks with UI layout traversal callbacks
- Unaware that slow main thread blocks animation (jank)

## Common Mistakes

- **No interpolation**: Jumpy motion instead of smooth easing
- **Expensive callback work**: Callback does network I/O → blocks frame → jank
- **Missing vsync**: Custom timer without Choreographer attachment misses sync windows
- **Forgetting to unpost callback**: Callback posted every frame but never cancelled → memory leak

## Performance Debug Approach

1. **Perfetto**: Record trace, look for vsync drop (red X in timeline)
2. **Frame Time**: Android Profiler → GPU Rendering shows per-frame cost
3. **Method Profiler**: If animation slow, profile which method takes time
4. **Systrace**: "Choreographer" events show when callbacks fire relative to vsync

## Related Deep Dives

- [RenderThread & GPU Pipeline](./renderthread-and-gpu-pipeline.md) - Frame pipelining and RenderThread latency
- [Custom View Rendering](./custom-view-rendering-and-invalidation.md) - invalidate() interaction with Choreographer
- [Jetpack Compose Performance](./jetpack-compose-performance.md) - Compose animations vs traditional animations

