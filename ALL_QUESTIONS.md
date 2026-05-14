# Complete Question List - Android Interview Prep
Generated: 205 interview questions across 81 deep dive topics
---
## Fundamentals Questions
## Activity Lifecycle (6 questions -> 1 deep dive)
1. `activity-lifecycle-overview` - What is the Activity Lifecycle?
2. `onstart-vs-onresume` - What's the difference between onStart() and onResume()?
3. `onsaved-instance-state` - What is savedInstanceState and when is it called?
4. `onconfig-change` - What happens during configuration changes (rotation)?
5. `process-death-handling` - How does Android handle process death?
6. `lifecycle-callbacks-order` - What is the exact order of lifecycle callbacks?
## Intents (5 questions -> 1 deep dive)
7. `intent-explicit-implicit` - What's the difference between explicit and implicit intents?
8. `intent-filters` - How do intent filters work?
9. `intent-resolution` - How does intent resolution work?
10. `intent-flags` - What are common intent flags and their purposes?
11. `pending-intent` - What is a PendingIntent and when should you use it?
## Fragments (5 questions -> 1 deep dive)
12. `fragment-lifecycle` - What is the Fragment lifecycle?
13. `fragment-vs-activity` - What are the differences between Fragments and Activities?
14. `fragment-communication` - How do fragments communicate with each other?
15. `fragment-back-stack` - How does fragment back stack work?
16. `fragment-arguments` - What's the best way to pass data to a Fragment?
## Context (4 questions -> 1 deep dive)
17. `context-what-is` - What is Context and what are its types?
18. `context-memory-leaks` - How can Context cause memory leaks?
19. `application-context-vs-activity-context` - When should you use Application Context vs Activity Context?
20. `context-lifecycle-awareness` - Why is it important to match Context lifetime with usage?
## Memory Leaks (4 questions -> 1 deep dive)
21. `memory-leak-what-is` - What is a memory leak in Android?
22. `memory-detection` - How do you detect memory leaks?
23. `common-leak-patterns` - What are common memory leak patterns in Android?
24. `memory-leak-fixes` - What are best practices to prevent memory leaks?
## Anr And Performance (4 questions -> 1 deep dive)
25. `anr-what-is` - What is an ANR (Application Not Responding)?
26. `preventing-anr` - How do you prevent ANRs?
27. `main-thread-vs-background` - Why shouldn't you do network/I/O on main thread?
28. `jank-dropped-frames` - What's jank and how do you measure it?
## Looper And Handler (4 questions -> 1 deep dive)
29. `looper-what-is` - What is Looper and how does it work?
30. `handler-what-is` - What is Handler and how does it relate to Looper?
31. `handler-thread` - What is HandlerThread and when should you use it?
32. `handler-memory-leak` - How can Handler cause memory leaks?
## Services (4 questions -> 1 deep dive)
33. `service-what-is` - What is a Service in Android?
34. `service-vs-thread` - What's the difference between Service and Thread?
35. `bound-service` - What is a bound service and how do you use it?
36. `intent-service` - What is IntentService and when should you use it?
## Broadcast Receivers (3 questions -> 1 deep dive)
37. `broadcast-receiver` - What is a Broadcast Receiver?
38. `broadcast-permissions` - How do you register broadcast receivers securely?
39. `ordered-vs-sticky-broadcast` - What are ordered and sticky broadcasts?
## Permissions (3 questions -> 1 deep dive)
40. `permissions-model` - What is the Android permission model?
41. `runtime-permissions` - How do you implement runtime permissions?
42. `permission-groups` - What are permission groups and how do they work?
## Androidmanifest (2 questions -> 1 deep dive)
43. `manifest-what-is` - What is AndroidManifest.xml and what does it contain?
44. `manifest-intent-filters` - How do you declare intent filters in manifest?
## Binder Ipc (1 questions -> 1 deep dive)
45. `binder-ipc` - What is Binder and how does IPC work in Android?
## Zygote Process Creation (1 questions -> 1 deep dive)
46. `zygote-process-creation` - What is Zygote and how does it create app processes?
## Art Vs Dalvik (1 questions -> 1 deep dive)
47. `art-vs-dalvik` - What is the difference between ART and Dalvik?
## App Startup Flow (1 questions -> 1 deep dive)
48. `app-startup-flow` - What happens when you launch an app?
## Recyclerview Efficiency (1 questions -> 1 deep dive)
49. `recyclerview-efficiency` - Why is RecyclerView more efficient than ListView?
## Rendering Pipeline (1 questions -> 1 deep dive)
50. `rendering-pipeline` - How does Android render UI frames?
## Storage Types (1 questions -> 1 deep dive)
51. `storage-types` - What are the different storage options in Android?
## Task And Backstack (1 questions -> 1 deep dive)
52. `task-and-backstack` - What is a Task and back stack in Android?
## Process Death Lifecycle (1 questions -> 1 deep dive)
53. `process-death-lifecycle` - What happens to app state when process is killed?
## Multitasking Window Focus (1 questions -> 1 deep dive)
54. `multitasking-window-focus` - How does multitasking affect activity lifecycle?

---

## Kotlin Questions
## Kotlin Basics (2 questions -> 1 deep dive)
55. `kotlin-language-features` - What makes Kotlin a good language for Android development?
56. `val-vs-var` - What is the difference between val and var in Kotlin?
## Data Classes And Generated Code (2 questions -> 1 deep dive)
57. `data-classes` - What is a data class in Kotlin?
58. `data-class-generated-members` - What methods does Kotlin generate for a data class?
## Object And Companion Objects (3 questions -> 1 deep dive)
59. `object-keyword` - What does the object keyword do in Kotlin?
60. `companion-objects` - What is a companion object in Kotlin?
61. `object-declaration-vs-object-expression` - What is the difference between an object declaration and an object expression?
## Sealed Classes And Enums (3 questions -> 1 deep dive)
62. `sealed-classes` - What is a sealed class in Kotlin?
63. `sealed-vs-enum` - When should you use a sealed class instead of an enum?
64. `enum-class-use-cases` - What are enum classes useful for in Kotlin?
## Delegation And Delegated Properties (3 questions -> 1 deep dive)
65. `class-delegation` - What is delegation in Kotlin?
66. `delegated-properties` - What are delegated properties in Kotlin?
67. `lazy-delegation` - How does lazy initialization work in Kotlin?
## Extension Functions (2 questions -> 1 deep dive)
68. `extension-functions` - What are extension functions in Kotlin?
69. `extension-function-resolution` - How are extension functions resolved in Kotlin?
## Scope Functions (2 questions -> 1 deep dive)
70. `scope-functions` - What are Kotlin scope functions?
71. `let-vs-run-vs-apply-vs-also` - What is the difference between let, run, apply, also, and with?
## Higher Order Functions And Lambdas (2 questions -> 1 deep dive)
72. `higher-order-functions` - What is a higher-order function in Kotlin?
73. `lambdas-with-receiver` - What is a lambda with receiver in Kotlin?
## Inline Functions (3 questions -> 1 deep dive)
74. `inline-functions` - What is an inline function in Kotlin?
75. `crossinline-vs-noinline` - What are crossinline and noinline in Kotlin?
76. `inline-performance-considerations` - When do inline functions help or hurt performance?
## Reified Generics (1 questions -> 1 deep dive)
77. `reified-generics` - What are reified type parameters in Kotlin?
## Null Safety And Smart Casts (3 questions -> 1 deep dive)
78. `null-safety` - How does null safety work in Kotlin?
79. `safe-call-elvis-not-null` - What are the safe call, Elvis operator, and not-null assertion in Kotlin?
80. `smart-casts` - What are smart casts in Kotlin?
## Generics And Variance (3 questions -> 1 deep dive)
81. `generics-in-kotlin` - How do generics work in Kotlin?
82. `variance-in-out` - What do in and out mean in Kotlin variance?
83. `star-projection` - What is a star projection in Kotlin?
## Collections And Sequences (3 questions -> 1 deep dive)
84. `collections-api` - What is important about Kotlin's collections API in interviews?
85. `immutable-vs-mutable-collections` - What is the difference between read-only and mutable collections in Kotlin?
86. `sequences-vs-collections` - When should you use Sequence instead of a regular collection chain?
## Coroutines Foundations (3 questions -> 1 deep dive)
87. `coroutines-what-are` - What are Kotlin Coroutines?
88. `suspend-functions` - What is a suspend function in Kotlin?
89. `continuation-and-cps` - How do suspend functions work internally in Kotlin?
## Dispatchers And Coroutine Scope (2 questions -> 1 deep dive)
90. `dispatchers` - What are Dispatchers in Kotlin Coroutines?
91. `coroutine-scope` - What is CoroutineScope and why does it matter?
## Structured Concurrency And Jobs (4 questions -> 1 deep dive)
92. `structured-concurrency` - What is structured concurrency in Kotlin?
93. `job-vs-supervisorjob` - What is the difference between Job and SupervisorJob?
94. `async-vs-launch` - What is the difference between launch and async in coroutines?
95. `job-hierarchy` - How does coroutine job hierarchy work?
## Cancellation And Exception Handling (2 questions -> 1 deep dive)
96. `coroutine-cancellation` - How does cancellation work in Kotlin Coroutines?
97. `coroutine-exception-handling` - How are exceptions handled in Kotlin Coroutines?
## Flow Fundamentals (2 questions -> 1 deep dive)
98. `flow-what-is` - What is Flow in Kotlin?
99. `cold-vs-hot-flow` - What is the difference between cold and hot streams in Kotlin?
## Stateflow Sharedflow And Channels (3 questions -> 1 deep dive)
100. `stateflow-vs-sharedflow` - What is the difference between StateFlow and SharedFlow?
101. `channels-vs-sharedflow` - When should you use a Channel instead of SharedFlow?
102. `mutex-in-kotlin` - What is Mutex in Kotlin Coroutines and when should you use it?
## Jvm Interop And Bytecode (3 questions -> 1 deep dive)
103. `kotlin-jvm-interoperability` - How does Kotlin interoperate with Java on the JVM?
104. `kotlin-bytecode-basics` - What should you know about Kotlin bytecode for interviews?
105. `suspend-state-machine` - How are coroutines compiled into a state machine?

---

## Compose Questions
## Compose Basics And Composable Contract (4 questions -> 1 deep dive)
106. `compose-declarative-ui` - What makes Jetpack Compose a declarative UI toolkit?
107. `composable-function` - What is a composable function?
108. `composable-lifecycle` - How should you think about composable lifecycle compared to Activity lifecycle?
109. `previews-in-compose` - What are Compose previews and their limitations?
## State And Remember (3 questions -> 1 deep dive)
110. `mutable-state-in-compose` - What is `MutableState` in Compose?
111. `remember-vs-rememberSaveable` - What is the difference between `remember` and `rememberSaveable`?
112. `remember-key-parameter` - Why do keys matter in `remember`?
## State Hoisting And Udf (4 questions -> 1 deep dive)
113. `state-hoisting` - What is state hoisting in Compose?
114. `unidirectional-data-flow-compose` - How does unidirectional data flow apply in Compose UI architecture?
115. `ui-state-modeling-compose` - How should UI state be modeled for complex Compose screens?
116. `event-handling-compose` - What are best practices for event handling in Compose?
## Recomposition And Skip Optimization (6 questions -> 1 deep dive)
117. `recomposition-definition` - What is recomposition in Jetpack Compose?
118. `what-triggers-recomposition` - What triggers recomposition?
119. `smart-recomposition` - What is smart recomposition?
120. `skip-optimization` - What is skip optimization in Compose?
121. `unstable-parameter-recomposition` - Why do unstable parameters often cause extra recomposition?
122. `prevent-unnecessary-recomposition` - How do you reduce unnecessary recomposition in production apps?
## Snapshot System And Observation (2 questions -> 1 deep dive)
123. `snapshot-system` - What is the Compose snapshot system?
124. `snapshot-state-read-write` - How are state reads and writes observed by Compose runtime?
## Side Effects Overview (3 questions -> 1 deep dive)
125. `side-effects-overview` - Why does Compose provide side-effect APIs?
126. `sideeffect-usage` - When should `SideEffect` be used?
127. `produceState-usage` - What problem does `produceState` solve?
## Effects Coroutines And Lifecycle (3 questions -> 1 deep dive)
128. `launchedeffect-usage` - How does `LaunchedEffect` work and when should you use it?
129. `disposableeffect-usage` - When do you use `DisposableEffect`?
130. `rememberCoroutineScope-usage` - What is `rememberCoroutineScope` used for?
## Derived State And Remember Updated State (2 questions -> 1 deep dive)
131. `derivedStateOf-purpose` - What is `derivedStateOf` and when does it help?
132. `rememberUpdatedState-purpose` - Why is `rememberUpdatedState` important in long-lived effects?
## Compositionlocal And Context Propagation (1 questions -> 1 deep dive)
133. `compositionlocal-purpose` - What is `CompositionLocal` and when should it be used?
## Flow Integration With Compose (3 questions -> 1 deep dive)
134. `stateflow-with-compose` - How do you integrate `StateFlow` with Compose UI?
135. `collectAsState-vs-collectAsStateWithLifecycle` - `collectAsState` vs `collectAsStateWithLifecycle` - what is the difference?
136. `snapshotFlow-usage` - What is `snapshotFlow` and when would you use it?
## Stability And Compose Compiler (3 questions -> 1 deep dive)
137. `stability-in-compose` - What does stability mean in Compose?
138. `stable-vs-immutable` - What is the difference between `@Stable` and `@Immutable`?
139. `compose-compiler-role` - What is the role of the Compose compiler?
## Slot Table And Runtime Internals (1 questions -> 1 deep dive)
140. `slot-table-purpose` - What is the Slot Table in Compose runtime?
## Composer Applier And Runtime Phases (2 questions -> 1 deep dive)
141. `composer-and-applier` - What are `Composer` and `Applier` in Compose internals?
142. `compose-runtime-phases` - What are the major runtime phases in Compose frame updates?
## Modifier Chain And Node Graph (1 questions -> 1 deep dive)
143. `modifier-chain-order` - Why does modifier order matter in Compose?
## Layout Measure Draw Pipeline (2 questions -> 1 deep dive)
144. `custom-layout-basics` - What should you know before writing custom layouts in Compose?
145. `measure-layout-draw-phases` - Explain measure, layout, and draw phases in Compose.
## Lazy Layouts And List Performance (2 questions -> 1 deep dive)
146. `lazycolumn-performance` - How do you optimize `LazyColumn` performance?
147. `keys-in-lazycolumn` - Why are keys important in `LazyColumn` items?
## Navigation In Compose (2 questions -> 1 deep dive)
148. `navigation-compose-basics` - What are core principles of navigation in Compose?
149. `navigation-single-source-of-truth` - How do you keep navigation maintainable at scale in Compose apps?
## Theming And Material3 (1 questions -> 1 deep dive)
150. `theming-material3-compose` - How does theming work in Compose with Material 3?
## Animation In Compose (1 questions -> 1 deep dive)
151. `animations-compose` - What animation APIs should you discuss in Compose interviews?
## Testing Interop And Performance (4 questions -> 1 deep dive)
152. `compose-testing-strategy` - What is a strong testing strategy for Compose UI?
153. `semantics-and-test-tags` - How do semantics and test tags help Compose testing?
154. `androidview-interop` - When and how should you use `AndroidView` interop?
155. `compose-performance-checklist` - What is your practical Compose performance checklist?

---

## Architecture Questions
## Mvvm And Viewmodel (3 questions -> 1 deep dive)
156. `mvvm-basics` - What is MVVM in Android architecture?
157. `viewmodel-role` - What is the role of a ViewModel in scalable Android apps?
158. `savedstatehandle-usage` - When should you use SavedStateHandle in architecture design?
## Mvi And Udf (3 questions -> 1 deep dive)
159. `mvi-what-is` - What is MVI architecture?
160. `mvi-vs-mvvm` - MVVM vs MVI - how do you choose?
161. `udf-principles` - What are the key principles of Unidirectional Data Flow?
## Clean Architecture Layering (3 questions -> 1 deep dive)
162. `clean-architecture-overview` - What is Clean Architecture in Android?
163. `layer-dependency-rule` - What is the dependency rule in layered architecture?
164. `dependency-inversion-android` - How does dependency inversion apply to Android app architecture?
## Repository Pattern And Data Sources (3 questions -> 1 deep dive)
165. `repository-pattern-purpose` - Why use the Repository pattern?
166. `repository-single-source-truth` - How does a repository support a Single Source of Truth model?
167. `multiple-data-sources-orchestration` - How should repositories orchestrate network, cache, and database sources?
## Use Cases And Domain Layer (3 questions -> 1 deep dive)
168. `use-case-purpose` - What problem do use cases solve in architecture?
169. `use-case-granularity` - How granular should use cases be?
170. `domain-layer-when-to-add` - When is a dedicated domain layer worth adding?
## Dependency Injection Strategies (3 questions -> 1 deep dive)
171. `dependency-injection-what-why` - Why is dependency injection important in Android architecture?
172. `constructor-injection-vs-field-injection` - Constructor injection vs field injection - which is preferred?
173. `di-scope-management` - How do DI scopes affect memory and lifecycle behavior?
## Hilt In Production (2 questions -> 1 deep dive)
174. `hilt-benefits` - What architectural advantages does Hilt provide?
175. `hilt-component-lifetimes` - What Hilt component lifetimes should senior engineers know?
## Dagger And Component Graph (3 questions -> 1 deep dive)
176. `dagger-vs-hilt` - Dagger vs Hilt - what is the architectural tradeoff?
177. `dagger-component-subcomponent` - What should you understand about Dagger components and subcomponents?
178. `dagger-performance-tradeoffs` - What are Dagger/Hilt build and runtime tradeoffs at scale?
## Service Locator And Anti Patterns (2 questions -> 1 deep dive)
179. `service-locator-what-is` - What is a Service Locator pattern?
180. `service-locator-vs-di` - Service Locator vs DI - why does this matter in interviews?
## Modularization Strategies (3 questions -> 1 deep dive)
181. `modularization-why` - Why modularize Android apps?
182. `multi-module-architecture-shapes` - What multi-module structures are common in Android?
183. `api-vs-implementation-modules` - How do API vs implementation module boundaries improve architecture?
## Feature Modules And Boundaries (3 questions -> 1 deep dive)
184. `feature-module-boundaries` - What defines a good feature module boundary?
185. `dynamic-feature-modules-when` - When should you use dynamic feature modules?
186. `dependency-direction-between-modules` - How should dependency direction work between feature modules?
## State Management And Ssot (3 questions -> 1 deep dive)
187. `state-management-android-architecture` - What is a strong state management approach in Android architecture?
188. `single-source-of-truth` - What does Single Source of Truth mean in practice?
189. `immutable-ui-state-models` - Why model UI state as immutable data classes?
## Offline First And Sync (3 questions -> 1 deep dive)
190. `offline-first-principles` - What is offline-first architecture?
191. `sync-strategies-pull-push` - Push, pull, and hybrid sync strategies - when to use each?
192. `conflict-resolution-sync` - How should architecture handle sync conflicts?
## Caching And Pagination Architecture (2 questions -> 1 deep dive)
193. `caching-strategies` - What caching strategies are common in Android architecture?
194. `pagination-architecture` - What does a robust pagination architecture look like?
## Reactive Architecture With Flows (2 questions -> 1 deep dive)
195. `stateflow-architecture` - How does StateFlow fit Android architecture design?
196. `event-handling-one-off-events` - How should one-off events be handled in reactive architecture?
## Ui State And Event Modeling (3 questions -> 1 deep dive)
197. `error-handling-architecture` - What is a good error handling architecture for Android apps?
198. `retry-strategies-architecture` - How do retry strategies fit architecture decisions?
199. `ui-state-modeling-architecture` - How should complex UI state be modeled architecturally?
## Navigation And Deep Link Architecture (2 questions -> 1 deep dive)
200. `navigation-architecture` - What are key principles of navigation architecture?
201. `deep-link-architecture` - How should deep links be designed in modular Android apps?
## Testing Architecture And Testability (1 questions -> 1 deep dive)
202. `architecture-testability` - How do you design Android architecture for high testability?
## Scalability And Team Topologies (1 questions -> 1 deep dive)
203. `scaling-architecture-for-team` - How does architecture impact team scalability?
## Production Tradeoffs And Decision Making (2 questions -> 1 deep dive)
204. `architecture-governance` - What is architecture governance in large Android codebases?
205. `production-architecture-tradeoffs` - How should senior engineers discuss architecture tradeoffs in interviews?

---
## Statistics
- **Total Questions:** 205
- **Total Deep Dives:** 81
- **Fundamentals:** 54 questions
- **Kotlin:** 51 questions
- **Compose:** 50 questions
- **Architecture:** 50 questions
- **Beginner:** 32 questions
- **Intermediate:** 108 questions
- **Advanced:** 17 questions
- **Senior:** 41 questions
- **Staff:** 7 questions

## By Category Difficulty
### Fundamentals
- Beginner: 14
- Intermediate: 37
- Advanced: 3

### Kotlin
- Beginner: 9
- Intermediate: 28
- Advanced: 14

### Compose
- Beginner: 4
- Intermediate: 26
- Senior: 17
- Staff: 3

### Architecture
- Beginner: 5
- Intermediate: 17
- Senior: 24
- Staff: 4

## Quick Tags Reference
- **architecture:** 61 questions
- **android:** 56 questions
- **kotlin:** 51 questions
- **compose:** 50 questions
- **state:** 19 questions
- **performance:** 17 questions
- **lifecycle:** 16 questions
- **coroutines:** 15 questions
- **runtime:** 11 questions
- **compiler:** 8 questions
- **recomposition:** 7 questions
- **side-effects:** 7 questions
- **di:** 7 questions
- **fundamentals:** 6 questions
- **intents:** 6 questions
- **memory:** 6 questions
- **ui:** 6 questions
- **modularization:** 6 questions
- **fragments:** 5 questions
- **threading:** 5 questions
- **data:** 5 questions
- **navigation:** 5 questions
- **flow:** 5 questions
- **scalability:** 5 questions
- **ipc:** 4 questions
- **context:** 4 questions
- **rendering:** 4 questions
- **service:** 4 questions
- **inline:** 4 questions
- **generics:** 4 questions
---
**Next Step:** Regenerate docs and validate navigation for Fundamentals, Kotlin, Compose, Architecture sections.
