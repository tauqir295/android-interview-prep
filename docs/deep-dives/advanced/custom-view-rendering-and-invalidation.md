# Custom View Rendering & Invalidation Deep Dive

**Question ID**: advanced-24  
**Difficulty**: Intermediate  
**Tags**: rendering, performance, custom-views

## Core Concept

Custom views follow a three-phase rendering pipeline: measure (size negotiation), layout (position children), draw (render to canvas). Each phase has performance implications; invalidation triggers recalculation but can cascade inefficiently if not managed.

## Key Areas Covered

### Measure Phase
- **Constraints**: Parent offers width/height specs (exact, at-most, unspecified) and child returns size
- **Two-pass negotiation**: Parent measures children, child reports size, parent adjusts
- **MeasureSpec**: Encodes mode (EXACTLY, AT_MOST, UNSPECIFIED) + size value
- **Expensive**: Measuring unspecified children in loop → O(n²) layouts
- **Example**: Parent wraps RecyclerView with height UNSPECIFIED → causes child to measure all items

### Layout Phase
- **Positioning**: Parent calls child.layout(l, t, r, b) with actual bounds; child positions own children
- **Coordinates**: Relative to parent (0,0 is parent's top-left)
- **Recursive**: Parent layouts children, children layout grandchildren
- **Linear complexity**: Well-designed layout tree is O(n) per layout pass

### Draw Phase
- **Canvas operations**: drawRect(), drawText(), drawBitmap() rendered to framebuffer
- **Occluded areas still drawn**: If View A overlaps B, B's draw() still called (waste)
- **Clipping**: Canvas.clipRect() prevents drawing outside bounds (optimization)
- **Double buffering**: Off-screen canvas used to avoid flicker (hardware-accelerated by default)

### Invalidation Cascade
- **invalidate()**: Queues layout + draw pass; runs asynchronously
- **requestLayout()**: Queues only layout pass (don't redraw if size unchanged)
- **Systemic risk**: Calling invalidate() in onDraw() creates recursive loop (ANR)
- **Throttling**: Use Choreographer.postFrameCallback() to batch invalidations

## Real-World Patterns

### Pattern: Nested View Measurement Explosion
```kotlin
// Problem: VerticalLayout with height WRAP_CONTENT containing HorizontalScroll
// HorizontalScroll has width UNSPECIFIED
// Each item in scroll measured repeatedly during parent's layout

@Suppress("DEBUG_METRICS_REQUIRED")
val spec = MeasureSpec.makeMeasureSpec(width, MeasureSpec.EXACTLY)  // Prevents re-measurement
```

### Pattern: Expensive onDraw with Invalidation
```kotlin
// Problem: onDraw() calls invalidate() → triggers recursion
override fun onDraw(canvas: Canvas) {
  // Draw something expensive
  invalidate()  // WRONG: causes infinite loop
}

// Better: Use Choreographer for throttling
override fun onDraw(canvas: Canvas) {
  // Draw
  choreographer.postFrameCallback(object : Choreographer.FrameCallback {
    override fun doFrame(frameTimeNanos: Long) {
      invalidate()  // Schedule next frame, not recursive
    }
  })
}
```

### Pattern: Nested RecyclerView Jank
```
Parent RecyclerView measure → child RecyclerView with height UNSPECIFIED
Child forced to measure ALL items in scroll (potentially 1000+)
Result: Scroll jank, 100-200ms layout pass

Fix: Set child RecyclerView height explicitly (not WRAP_CONTENT)
```

## Tradeoffs

| Factor | Precise Measurement | Caching |
|--------|------------------|---------|
| Memory | Less (measure on-demand) | More (cached sums) |
| CPU | More (repeated calculation) | Less (lookup) |
| Layout Time | Slower | Faster |
| Code Complexity | Simple | Complex |

## Interview Signals

### Strong answers include:
- Understanding two-pass measure negotiation (constraint offering, size reporting)
- Knowing O(n²) measurement explosion in nested containers
- Aware of invalidate() vs requestLayout() distinction
- Can explain how Choreographer prevents recursive invalidation
- Understanding that occluded views still draw (no automatic optimization)

### Weak answers:
- Treating measure, layout, draw as blacks boxes without understanding their purpose
- Not knowing about measurement constraint modes
- Unaware of O(n²) pitfalls in nested scrollable layouts
- Blanking on how to fix nested RecyclerView jank

## Common Mistakes

- **WRAP_CONTENT in nested scroll**: Forces expensive measurement
- **No clipping**: Drawing off-screen content wastes GPU cycles
- **Calling invalidate() in onDraw()**: Causes recursive loop
- **Ignoring layout pass**: Only redrawing without relayouting when size needs change

## Performance Debug Approach

1. **Layout Inspector**: Visualize view hierarchy and measure times
2. **Android Profiler**: GPU Rendering → "Measure/Layout" bar shows cost
3. **Systrace**: "Inflater" events show initialization; "Choreographer" shows frame deadlines
4. **Profile**: Identify which views take longest to measure/layout

## Related Deep Dives

- [RenderThread & GPU Pipeline](./renderthread-and-gpu-pipeline.md) - Hardware acceleration of canvas drawing
- [Choreographer & Animation](./choreographer-and-animation-timing.md) - Frame callbacks and invalidation throttling
- [Jetpack Compose Performance](./jetpack-compose-performance.md) - How Compose avoids layout cascade with state

