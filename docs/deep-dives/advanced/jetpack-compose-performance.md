# Jetpack Compose Performance Deep Dive

**Question ID**: advanced-23  
**Difficulty**: Senior  
**Tags**: compose, performance, architecture

## Core Concept

Jetpack Compose uses smart recomposition to minimize UI updates. When state changes, Compose reruns only affected composables; careful state management prevents cascading recomposes across the entire tree.

## Key Areas Covered

### State Stability & Recomposition
- **Stable types**: Immutable data classes with proper `equals()` skip recomposition if reference unchanged
- **Unstable types**: Mutable objects (lists, maps) always recompose even if content identical
- **Compiler warnings**: Use `@Stable` annotation to hint compiler about immutable semantics
- **Example**: `data class User(val id: Int, val name: String)` is stable; recompose only if User reference changes

### Recomposition Scope
- **Fine-grained**: Changes to `State<T>` only recompose downward from that state holder
- **Not whole tree**: Changing bottom-level state doesn't recompose entire screen
- **Performance implication**: Lift state as low as possible to minimize recomposition scope

### Remember & DerivedStateOf
- **remember { }**: Caches computed value across recompositions; cleared when composable leaves composition
- **derivedStateOf { }**: Skips recomposing child if result unchanged, even if dependent states changed
- **Use case**: Expensive calculation (filtering, sorting) wrapped in `derivedStateOf` prevents wasted work
- **Memory**: Each remembered value consumes memory; balance against recomposition cost

### Key Optimization
- **key { }**: Forces recomposition only when key changes, ignoring implicit dependencies
- **Use case**: LazyColumn item composition keys prevent accidental recomposition on scroll
- **Risk**: Incorrect keys can hide data changes (state updates but UI doesn't reflect)

### Compose Metrics & Profiling
- **Compose Compiler Metrics**: Generate report of which composables are skippable (stable)
- **Android Profiler**: Trace Compose frame composition time
- **Macrobenchmark**: Measure real app recomposition cost under production load

## Real-World Patterns

### Pattern: Expensive LazyColumn Item
```kotlin
// Problem: Complex item layout recomposes on every scroll
LazyColumn {
  items(100) { index ->
    ExpensiveItemCard(data = items[index])  // Recomposes if LazyColumn parent recomposes
  }
}

// Fix: Stabilize data and use content key
LazyColumn {
  items(items, key = { it.id }) { item ->
    ExpensiveItemCard(data = item)  // Recomposes only if item reference changes
  }
}
```

### Pattern: Over-Lifting State
```kotlin
// Problem: State at top-level, changes recompose entire screen
var selectedTab by remember { mutableStateOf(0) }
// Entire screen recomposes when selectedTab changes

// Better: Lift state only as high as needed
TabRow(selectedTab = selectedTab, onTabSelected = { selectedTab = it })
TabContent(selectedTab = selectedTab)  // Only these recompose
```

### Pattern: DerivedStateOf for Filtering
```kotlin
// Problem: Filtering inside composable body recomposes child on every parent recomposition
val filteredList = items.filter { it.matches(query) }

// Better: Cache filtered result
val filteredList = remember(items, query) {
  items.filter { it.matches(query) }
}

// Even better: Skip child recompose if filter result unchanged
val filteredList by remember { derivedStateOf { items.filter { it.matches(query) } } }
```

## Tradeoffs

| Factor | Fine-Grained State | Lifted State |
|--------|------------------|--------------|
| Recomposition Scope | Narrow (fast) | Broad (slow) |
| State Management | Complex | Simple |
| Code Clarity | Hard to follow | Easy to follow |
| Performance | Better (avoids unnecessary recomposes) | Worse (cascading recomposes) |

## Interview Signals

### Strong answers include:
- Understanding state stability and immutability requirements
- Knowing `remember` caches values across recompositions, not across app restarts
- Aware of `derivedStateOf` optimization for caching derived values
- Can explain why incorrect `key` breaks data updates
- Understanding recomposition scope and why state positioning matters

### Weak answers:
- Treating all state changes as triggering full recomposition
- Not understanding `remember` lifecycle (cleared when composable leaves composition)
- Confusing `remember` with SharedPreferences or persistent storage
- Unaware of stable/unstable type implications

## Common Mistakes

- **Calling remember without dependencies**: Captures stale variables
- **Using mutable objects in state**: `remember { mutableListOf() }` changes mean object mutated, not state change
- **Wrong key usage**: `key(randomValue)` forces recomposition every call (defeats purpose)
- **Expensive operations in remember**: Long computation blocks composition thread

## Related Deep Dives

- [Custom View Rendering](./custom-view-rendering-and-invalidation.md) - Comparison to traditional View invalidation
- [Choreographer & Animation](./choreographer-and-animation-timing.md) - Compose animation recomposition behavior
- [Reactive Programming](./reactive-programming-and-rxjava.md) - Feeding observable streams into Compose state

