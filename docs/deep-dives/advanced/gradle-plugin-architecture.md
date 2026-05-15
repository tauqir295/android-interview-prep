# Gradle Plugin Architecture Deep Dive

**Question ID**: advanced-28  
**Difficulty**: Senior  
**Tags**: build, gradle, performance

## Core Concept

Gradle plugins extend the build system with custom tasks. Incremental tasks minimize work by processing only changed inputs; build caching skips unchanged tasks entirely. Both require precise @Input/@Output declarations.

## Key Areas Covered

### Custom Task Design
- **extend DefaultTask**: Define @Input properties (e.g., sourceDir) and @Output (e.g., outputDir)
- **Gradle introspection**: Gradle reads @Input/@Output to determine if task needs rerunning
- **No explicit dependencies**: Gradle builds dependency graph automatically from @Input/@Output
- **Task properties**: File, String, Int, boolean annotated correctly for Gradle's analysis

### Incremental Tasks
- **Full task**: Input changes → entire task reruns (slow for large inputs)
- **Incremental task**: Input changes → only changed files processed (10-100x faster)
- **Example**: Only 1 source file changed → only that file recompiled (not whole project)
- **Cost**: Requires stateful processing (tracking which files processed)
- **Memory**: Incremental state persisted between builds (requires cleanup)

### Build Caching
- **Local cache**: Recent task outputs stored locally; cache miss → rebuild
- **Remote cache**: CI task outputs uploaded; developer machines download (skip local recompilation)
- **Cache key**: Hash of inputs; if inputs identical, output trusted from cache
- **Risk**: Incorrect cache key can silently hide bugs (changing input not detected)
- **Example**: Task reading system time without declaring it as @Input → mistaken cache hit when time changes

### Dependency Declaration
- **Explicit @Input/@Output**: Gradle can reason about task schedules
- **Missing declarations**: Gradle assumes dependencies Unknown, forces full rebuild to be safe
- **Gradle task analysis**: Visualization shows which tasks depend on which, identifies bottlenecks

### Real-World Scale Issues
- **500 modules × 30s compile**: 250 minutes full build
- **With parallelization**: 4 machines × 30s = ~30m (8x speedup)
- **With incremental**: Change 1 file → rebuild only that module (1m instead of 30m)
- **Combined**: 100x speedup possible (with perfect task isolation)

## Real-World Patterns

### Pattern: Custom Annotation Processor Task
```kotlin
@CacheableTask  // Enable build cache
abstract class AnnotationProcessorTask : DefaultTask() {
  @InputFiles
  @PathSensitive(PathSensitivity.RELATIVE)
  abstract fun getSourceFiles(): FileCollection  // Changed files → cache miss
  
  @OutputDirectory
  abstract fun getOutputDir(): DirectoryProperty  // Generated code
  
  @TaskAction
  fun process() {
    val sourceFiles = getSourceFiles().files
    sourceFiles.forEach { file ->
      // Process only changed files, not all
      generateCode(file, getOutputDir())
    }
  }
}
```

### Pattern: Missing @Input Causes Cache Miss
```kotlin
// Problem: Task reads system time; no @Input declared
@TaskAction
fun build() {
  val buildTime = System.currentTimeMillis()  // WRONG: not in @Input
  writeMetadata(buildTime)  // Cache key doesn't change
}

// Result: Cache hit even though buildTime changed (stale output)

// Better: Declare time as input
@Input
abstract fun getBuildTime(): Property<Long>  // Gradle includes in cache key
```

### Pattern: Incremental vs Full Rebuild
```
Scenario 1: Change 100 source files
  Full recompile: 30s
  Incremental (100 files): 1s (99% faster)

Scenario 2: Change 1 annotation processor rule
  Both full + incremental: regenerate all code (can't be incremental)
  Cost is same; incremental doesn't help
```

## Tradeoffs

| Factor | Fine-Grained @Input/@Output | Coarse-Grained |
|--------|----------------------|------------|
| Cache Hit Rate | High (precise key) | Low (changes missed) |
| Code Complexity | Complex | Simple |
| Build Speed | Faster | Slower |
| Maintenance | Fragile (easy wrong) | Robust |

## Interview Signals

### Strong answers include:
- Understanding @Input/@Output declaration is how Gradle determines cache validity
- Knowing incremental tasks require state tracking but give massive speedup
- Aware of cache key sensitivity (missing @Input hides changes)
- Can explain why 500 module project is slow (full build) but fast with incremental (1 file change)
- Understanding remote cache benefit (CI precompiles, developers download)

### Weak answers:
- Thinking Gradle caching is automatic (requires correct @Input/@Output)
- Not knowing incremental tasks only reprocess changed files
- Unaware of cache key misses (wrong hash, stale output)
- Missing understanding of parallel execution with 500+ modules

## Common Mistakes

- **Including mutable properties as @Input**: Timestamp, random value → cache key changes every build (always rebuilds)
- **Forgetting to declare @OutputDirectory**: Gradle doesn't know where task outputs go
- **Mixing tasks in single process**: Task A's output becomes task B's input → need explicit `dependsOn`
- **Assuming remote cache**: Must configure (build cache plugin + remote server)

## Performance Debug Approach

1. **gradle build --profile**: Generates HTML timeline showing per-task times
2. **gradle tasks --profile**: Shows task dependency graph
3. **Build scan (Gradle Enterprise)**: Cloud dashboard of build times, bottlenecks
4. **Trace**: `gradle build --trace-task-graph` shows execution order

## Configuration Cache
- **Gradle 7.0+**: Project configuration only evaluated once (cached)
- **Requirement**: Tasks can't read project properties at task action time (must be @Input)
- **Benefit**: Configuration cache + build cache + parallel = best performance

## Related Deep Dives

- [Dependency Injection at Scale](./dependency-injection-at-scale.md) - Dagger annotation processor as custom task
- [Modularization at Scale](./modularization-at-scale.md) - Task parallelization with modular projects
- [Data Serialization](./data-serialization-tradeoffs.md) - Protobuf code generation task example

