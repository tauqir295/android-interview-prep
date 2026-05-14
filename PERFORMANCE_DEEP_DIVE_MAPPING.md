# Performance Deep Dive Mapping
This document maps Performance section questions to shared deep-dive topics.
## Architecture Overview
The Performance section contains:
- **Total Questions:** 50
- **Total Deep Dives:** 20
- **Strategy:** multiple questions per deep dive
## Recommended Deep Dive Files
1. `performance-metrics.md` - Metrics, measurement, profiling basics
2. `jank-and-frame-drops.md` - Frame rendering, jank detection/fixes
3. `memory-leaks.md` - Detection, prevention, debugging
4. `memory-management.md` - GC, memory pressure, optimization
5. `battery-optimization.md` - Battery drain sources, optimization
6. `rendering-pipeline.md` - Android rendering process, GPU
7. `rendering-optimization.md` - Overdraw, GPU optimization
8. `app-startup.md` - Cold/warm/hot start optimization
9. `memory-profiling.md` - Memory Profiler, heap dumps, tools
10. `cpu-profiling.md` - CPU profiling methods and tools
11. `layout-optimization.md` - Layout inflation, layout complexity
12. `anr-prevention.md` - ANR causes and prevention
13. `bitmap-optimization.md` - Bitmap memory, compression
14. `database-optimization.md` - Query optimization, indexing
15. `network-optimization.md` - Network requests, caching
16. `allocation-optimization.md` - String allocation, object pooling
17. `reflection-optimization.md` - Reflection performance cost
18. `recyclerview-optimization.md` - View recycling, performance
19. `initialization-patterns.md` - Lazy init, dependency injection
20. `profiling-tools.md` - Perfetto, systrace, Android Profiler
## Question-to-Deep Dive Mapping
| Questions | Deep Dive |
|-----------|-----------|
| android-performance-fundamentals | performance-metrics |
| jank-and-ui-drops | jank-and-frame-drops |
| memory-leaks | memory-leaks |
| garbage-collection, memory-pressure, graphics-memory | memory-management |
| battery-optimization | battery-optimization |
| rendering-pipeline | rendering-pipeline |
| overdraw | rendering-optimization |
| app-startup-time, cold-start-optimization | app-startup |
| memory-profiling | memory-profiling |
| cpu-profiling | cpu-profiling |
| layout-inflation | layout-optimization |
| anr-prevention | anr-prevention |
| bitmap-optimization | bitmap-optimization |
| database-performance | database-optimization |
| network-performance | network-optimization |
| string-formatting, object-pooling | allocation-optimization |
| reflection-performance | reflection-optimization |
| view-recycling | recyclerview-optimization |
| lazy-initialization | initialization-patterns |
| perfetto-tracing, frame-rate-stability, systrace-analysis, custom-performance-monitoring, performance-testing, benchmark-tools, power-consumption-profiling | profiling-tools |
| warm-cache, composition-performance, shader-compilation, gpu-rendering-cost, kernel-linux-performance, ahead-of-time-compilation, responsiveness-perception, performance-budgets | misc-advanced-topics |
---
Generated September 2026
