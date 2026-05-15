# Dependency Injection at Scale Deep Dive

**Question ID**: advanced-22  
**Difficulty**: Senior  
**Tags**: architecture, design-patterns, DI

## Core Concept

Dependency injection decouples components by inverting control—consumers declare dependencies rather than creating them. Dagger compiles a dependency graph at build-time, guaranteeing no circular dependencies can exist at runtime.

## Key Areas Covered

### Dependency Graph as DAG
- **Directed Acyclic Graph**: Dagger enforces no cycles (A→B→A fails at compile-time, not runtime)
- **Compile-time verification**: Errors before shipping (prevents runtime surprises)
- **Example cycle**: Service A @Provides B, Service B @Provides A → Dagger error
- **Prevention**: Detect cycles during build, force developer to refactor (introduce intermediary or break reference)

### Scopes & Lifetimes
- **@Singleton**: Single instance per application lifetime (caches permanently)
- **@ActivityScoped**: New instance per activity (tied to activity lifecycle)
- **@FragmentScoped**: New instance per fragment
- **Unscoped**: Creates new instance on every injection (stateless utilities)
- **Decision**: Choose scope to match object lifetime expectations

### Lazy vs Provider
- **Lazy<T>**: Delays creation until `.get()` called; instance created once then cached
- **Provider<T>**: Fresh instance on each `.get()` call; useful for factories
- **Memory vs initialization**: Lazy saves initialization time if object never used; Provider flexible for repeated needs

### Real-World Scale Issues
- **100+ modules → Dagger build overhead**: Full graph analysis takes seconds per compile
- **Solution strategies**:
  - Hierarchical graphs (separate Dagger instances per module)
  - Library modules (pre-compiled dependency graphs)
  - Lazy module loading (load graph only when needed)

### Hilt Auto-Wiring
- **Less boilerplate**: @HiltViewModel, @AndroidEntryPoint reduce setup
- **Trade-off**: Less explicit wiring makes debugging harder when app doesn't inject as expected
- **Hidden dependencies**: Auto-wiring can hide implicit assumptions about availability

## Real-World Patterns

### Pattern: Circular Dependency Detection
```kotlin
// This fails at compile-time:
@Module
class ServiceModule {
  @Provides
  fun provideA(b: B) = A(b)  // A needs B
  
  @Provides
  fun provideB(a: A) = B(a)  // B needs A
}

// Dagger error: Cycle detected at build-time
```

### Pattern: Scope Mismatch
```kotlin
// Problem: Activity-scoped dependency in singleton
@Provides
@Singleton
fun provideLongLivedService(activity: Activity) {
  // ERROR: Activity dies, singleton still holds reference → memory leak
}

// Fix: Inject activity-scoped dependency into activity-scoped service
@Provides
@ActivityScoped
fun provideActivityService(activity: Activity) { ... }
```

### Pattern: Module Hierarchy at Scale
```
:app (has Dagger Component)
├─ :feature:home (has separate Component, depends on :core Component)
├─ :feature:login (separate Component)
└─ :core (base Component, provides AppContext, Database, etc.)
```

## Tradeoffs

| Factor | Tight Graph | Loose Services |
|--------|-----------|-----------------|
| Build Time | Longer (full analysis) | Shorter (less coupling) |
| Runtime Errors | None (caught at compile) | Possible (missing bindings) |
| Flexibility | Less (strict contracts) | More (manual wiring) |
| Debugging | Explicit (graph visible) | Implicit (harder to trace) |

## Interview Signals

### Strong answers include:
- Understanding cycles fail at compile-time, not runtime (significant advantage)
- Knowing when to use Lazy vs Provider (trade memory for initialization cost)
- Aware of scope lifetime mismatches and memory leak patterns
- Can explain build-time cost and mitigation strategies

### Weak answers:
- Treating DI as just "injecting dependencies" without understanding graph structure
- Not knowing Dagger detects cycles early
- Confusing Lazy and Provider use cases

## Related Deep Dives

- [Gradle Plugin Architecture](./gradle-plugin-architecture.md) - Custom Gradle tasks for DI validation
- [Jetpack Compose Performance](./jetpack-compose-performance.md) - DI scoping in Compose ViewModels
- [Modularization at Scale](./modularization-at-scale.md) - Separating Dagger graphs per module

