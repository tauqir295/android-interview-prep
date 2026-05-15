# Complete Question List - Android Interview Prep
Generated: 727 interview questions across 301 deep dive topics
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
## Activity Lifecycle And State (3 questions -> 1 deep dive)
55. `explain-android-i18n-correctness-plurals-gender-neutral-text-number-fo` - Explain Android i18n correctness - plurals, gender-neutral text, number formatting, and locale handling
56. `explain-rtl-layout-support-bidirectional-text-icon-direction-and-meani` - Explain RTL layout support - bidirectional text, icon direction, and meaning preservation
57. `explain-accessibility-at-scale-audit-strategy-semantics-coverage-and-k` - Explain accessibility at scale - audit strategy, semantics coverage, and keyboard/D-pad navigation

---

## Kotlin Questions
## Kotlin Basics (12 questions -> 1 deep dive)
58. `kotlin-language-features` - What makes Kotlin a good language for Android development?
59. `val-vs-var` - What is the difference between val and var in Kotlin?
60. `explain-the-kotlin-type-system-nullable-vs-non-nullable-platform-types` - Explain the Kotlin type system - nullable vs non-nullable, platform types, and Nothing
61. `explain-kotlin-generics-variance-out-in-and-star-projections` - Explain Kotlin generics variance - out, in, and star-projections
62. `explain-kotlin-inline-functions-and-reified-type-parameters-capabiliti` - Explain Kotlin inline functions and reified type parameters - capabilities and costs
63. `explain-kotlin-extension-functions-dispatch-rules-and-common-pitfalls` - Explain Kotlin extension functions - dispatch rules and common pitfalls
64. `explain-kotlin-object-declarations-companion-objects-and-singleton-ini` - Explain Kotlin object declarations, companion objects, and singleton initialization order
65. `explain-kotlin-delegation-and-property-delegates-by-lazy-observable-an` - Explain Kotlin delegation and property delegates - by, lazy, observable, and custom delegates
66. `explain-kotlin-value-classes-inline-classes-runtime-representation-box` - Explain Kotlin value classes (inline classes) - runtime representation, boxing, and Android use cases
67. `explain-kotlin-jvm-interop-sam-conversions-default-methods-and-jvmover` - Explain Kotlin JVM interop - SAM conversions, default methods, and @JvmOverloads
68. `discuss-kotlin-performance-traps-sequences-vs-collections-allocation-a` - Discuss Kotlin performance traps - sequences vs collections, allocation, and persistent data structures
69. `explain-reflection-and-kclass-on-android-costs-risks-and-alternatives` - Explain reflection and KClass on Android - costs, risks, and alternatives
## Data Classes And Generated Code (2 questions -> 1 deep dive)
70. `data-classes` - What is a data class in Kotlin?
71. `data-class-generated-members` - What methods does Kotlin generate for a data class?
## Object And Companion Objects (3 questions -> 1 deep dive)
72. `object-keyword` - What does the object keyword do in Kotlin?
73. `companion-objects` - What is a companion object in Kotlin?
74. `object-declaration-vs-object-expression` - What is the difference between an object declaration and an object expression?
## Sealed Classes And Enums (3 questions -> 1 deep dive)
75. `sealed-classes` - What is a sealed class in Kotlin?
76. `sealed-vs-enum` - When should you use a sealed class instead of an enum?
77. `enum-class-use-cases` - What are enum classes useful for in Kotlin?
## Delegation And Delegated Properties (3 questions -> 1 deep dive)
78. `class-delegation` - What is delegation in Kotlin?
79. `delegated-properties` - What are delegated properties in Kotlin?
80. `lazy-delegation` - How does lazy initialization work in Kotlin?
## Extension Functions (2 questions -> 1 deep dive)
81. `extension-functions` - What are extension functions in Kotlin?
82. `extension-function-resolution` - How are extension functions resolved in Kotlin?
## Scope Functions (2 questions -> 1 deep dive)
83. `scope-functions` - What are Kotlin scope functions?
84. `let-vs-run-vs-apply-vs-also` - What is the difference between let, run, apply, also, and with?
## Higher Order Functions And Lambdas (2 questions -> 1 deep dive)
85. `higher-order-functions` - What is a higher-order function in Kotlin?
86. `lambdas-with-receiver` - What is a lambda with receiver in Kotlin?
## Inline Functions (3 questions -> 1 deep dive)
87. `inline-functions` - What is an inline function in Kotlin?
88. `crossinline-vs-noinline` - What are crossinline and noinline in Kotlin?
89. `inline-performance-considerations` - When do inline functions help or hurt performance?
## Reified Generics (1 questions -> 1 deep dive)
90. `reified-generics` - What are reified type parameters in Kotlin?
## Null Safety And Smart Casts (3 questions -> 1 deep dive)
91. `null-safety` - How does null safety work in Kotlin?
92. `safe-call-elvis-not-null` - What are the safe call, Elvis operator, and not-null assertion in Kotlin?
93. `smart-casts` - What are smart casts in Kotlin?
## Generics And Variance (3 questions -> 1 deep dive)
94. `generics-in-kotlin` - How do generics work in Kotlin?
95. `variance-in-out` - What do in and out mean in Kotlin variance?
96. `star-projection` - What is a star projection in Kotlin?
## Collections And Sequences (3 questions -> 1 deep dive)
97. `collections-api` - What is important about Kotlin's collections API in interviews?
98. `immutable-vs-mutable-collections` - What is the difference between read-only and mutable collections in Kotlin?
99. `sequences-vs-collections` - When should you use Sequence instead of a regular collection chain?
## Coroutines Foundations (3 questions -> 1 deep dive)
100. `coroutines-what-are` - What are Kotlin Coroutines?
101. `suspend-functions` - What is a suspend function in Kotlin?
102. `continuation-and-cps` - How do suspend functions work internally in Kotlin?
## Dispatchers And Coroutine Scope (2 questions -> 1 deep dive)
103. `dispatchers` - What are Dispatchers in Kotlin Coroutines?
104. `coroutine-scope` - What is CoroutineScope and why does it matter?
## Structured Concurrency And Jobs (4 questions -> 1 deep dive)
105. `structured-concurrency` - What is structured concurrency in Kotlin?
106. `job-vs-supervisorjob` - What is the difference between Job and SupervisorJob?
107. `async-vs-launch` - What is the difference between launch and async in coroutines?
108. `job-hierarchy` - How does coroutine job hierarchy work?
## Cancellation And Exception Handling (2 questions -> 1 deep dive)
109. `coroutine-cancellation` - How does cancellation work in Kotlin Coroutines?
110. `coroutine-exception-handling` - How are exceptions handled in Kotlin Coroutines?
## Flow Fundamentals (2 questions -> 1 deep dive)
111. `flow-what-is` - What is Flow in Kotlin?
112. `cold-vs-hot-flow` - What is the difference between cold and hot streams in Kotlin?
## Stateflow Sharedflow And Channels (3 questions -> 1 deep dive)
113. `stateflow-vs-sharedflow` - What is the difference between StateFlow and SharedFlow?
114. `channels-vs-sharedflow` - When should you use a Channel instead of SharedFlow?
115. `mutex-in-kotlin` - What is Mutex in Kotlin Coroutines and when should you use it?
## Jvm Interop And Bytecode (3 questions -> 1 deep dive)
116. `kotlin-jvm-interoperability` - How does Kotlin interoperate with Java on the JVM?
117. `kotlin-bytecode-basics` - What should you know about Kotlin bytecode for interviews?
118. `suspend-state-machine` - How are coroutines compiled into a state machine?

---

## Compose Questions
## Compose Basics And Composable Contract (15 questions -> 1 deep dive)
119. `compose-declarative-ui` - What makes Jetpack Compose a declarative UI toolkit?
120. `composable-function` - What is a composable function?
121. `composable-lifecycle` - How should you think about composable lifecycle compared to Activity lifecycle?
122. `previews-in-compose` - What are Compose previews and their limitations?
123. `compare-remembercoroutinescope-launchedeffect-and-viewmodel-scope-when` - Compare rememberCoroutineScope, LaunchedEffect, and ViewModel scope — when to use each
124. `how-do-you-model-one-off-events-in-compose-navigation-snackbar-and-toa` - How do you model one-off events in Compose — navigation, snackbar, and toast correctly
125. `explain-derivedstateof-and-how-to-avoid-unnecessary-recompositions` - Explain derivedStateOf and how to avoid unnecessary recompositions
126. `explain-compose-accessibility-and-semantics-correctness-for-talkback-a` - Explain Compose accessibility and semantics correctness for TalkBack and focus order
127. `debug-snackbar-toast-or-navigation-event-triggers-twice-in-compose` - Debug - snackbar, toast, or navigation event triggers twice in Compose
128. `debug-launchedeffect-re-runs-unexpectedly-on-recomposition` - Debug - LaunchedEffect re-runs unexpectedly on recomposition
129. `debug-list-item-state-jumps-between-rows-in-lazycolumn` - Debug - list item state jumps between rows in LazyColumn
130. `debug-excessive-recompositions-while-typing-in-a-textfield` - Debug - excessive recompositions while typing in a TextField
131. `debug-and-fix-slow-scrolling-and-jank-in-compose-lazy-lists` - Debug and fix slow scrolling and jank in Compose lazy lists
132. `explain-paging-3-integration-with-compose-and-correct-invalidation-con` - Explain Paging 3 integration with Compose and correct invalidation control
133. `explain-compose-modifier-chains-ordering-performance-cost-and-correctn` - Explain Compose Modifier chains - ordering, performance cost, and correctness
## State And Remember (3 questions -> 1 deep dive)
134. `mutable-state-in-compose` - What is `MutableState` in Compose?
135. `remember-vs-rememberSaveable` - What is the difference between `remember` and `rememberSaveable`?
136. `remember-key-parameter` - Why do keys matter in `remember`?
## State Hoisting And Udf (4 questions -> 1 deep dive)
137. `state-hoisting` - What is state hoisting in Compose?
138. `unidirectional-data-flow-compose` - How does unidirectional data flow apply in Compose UI architecture?
139. `ui-state-modeling-compose` - How should UI state be modeled for complex Compose screens?
140. `event-handling-compose` - What are best practices for event handling in Compose?
## Recomposition And Skip Optimization (6 questions -> 1 deep dive)
141. `recomposition-definition` - What is recomposition in Jetpack Compose?
142. `what-triggers-recomposition` - What triggers recomposition?
143. `smart-recomposition` - What is smart recomposition?
144. `skip-optimization` - What is skip optimization in Compose?
145. `unstable-parameter-recomposition` - Why do unstable parameters often cause extra recomposition?
146. `prevent-unnecessary-recomposition` - How do you reduce unnecessary recomposition in production apps?
## Snapshot System And Observation (2 questions -> 1 deep dive)
147. `snapshot-system` - What is the Compose snapshot system?
148. `snapshot-state-read-write` - How are state reads and writes observed by Compose runtime?
## Side Effects Overview (3 questions -> 1 deep dive)
149. `side-effects-overview` - Why does Compose provide side-effect APIs?
150. `sideeffect-usage` - When should `SideEffect` be used?
151. `produceState-usage` - What problem does `produceState` solve?
## Effects Coroutines And Lifecycle (3 questions -> 1 deep dive)
152. `launchedeffect-usage` - How does `LaunchedEffect` work and when should you use it?
153. `disposableeffect-usage` - When do you use `DisposableEffect`?
154. `rememberCoroutineScope-usage` - What is `rememberCoroutineScope` used for?
## Derived State And Remember Updated State (2 questions -> 1 deep dive)
155. `derivedStateOf-purpose` - What is `derivedStateOf` and when does it help?
156. `rememberUpdatedState-purpose` - Why is `rememberUpdatedState` important in long-lived effects?
## Compositionlocal And Context Propagation (1 questions -> 1 deep dive)
157. `compositionlocal-purpose` - What is `CompositionLocal` and when should it be used?
## Flow Integration With Compose (3 questions -> 1 deep dive)
158. `stateflow-with-compose` - How do you integrate `StateFlow` with Compose UI?
159. `collectAsState-vs-collectAsStateWithLifecycle` - `collectAsState` vs `collectAsStateWithLifecycle` - what is the difference?
160. `snapshotFlow-usage` - What is `snapshotFlow` and when would you use it?
## Stability And Compose Compiler (3 questions -> 1 deep dive)
161. `stability-in-compose` - What does stability mean in Compose?
162. `stable-vs-immutable` - What is the difference between `@Stable` and `@Immutable`?
163. `compose-compiler-role` - What is the role of the Compose compiler?
## Slot Table And Runtime Internals (1 questions -> 1 deep dive)
164. `slot-table-purpose` - What is the Slot Table in Compose runtime?
## Composer Applier And Runtime Phases (2 questions -> 1 deep dive)
165. `composer-and-applier` - What are `Composer` and `Applier` in Compose internals?
166. `compose-runtime-phases` - What are the major runtime phases in Compose frame updates?
## Modifier Chain And Node Graph (1 questions -> 1 deep dive)
167. `modifier-chain-order` - Why does modifier order matter in Compose?
## Layout Measure Draw Pipeline (2 questions -> 1 deep dive)
168. `custom-layout-basics` - What should you know before writing custom layouts in Compose?
169. `measure-layout-draw-phases` - Explain measure, layout, and draw phases in Compose.
## Lazy Layouts And List Performance (2 questions -> 1 deep dive)
170. `lazycolumn-performance` - How do you optimize `LazyColumn` performance?
171. `keys-in-lazycolumn` - Why are keys important in `LazyColumn` items?
## Navigation In Compose (2 questions -> 1 deep dive)
172. `navigation-compose-basics` - What are core principles of navigation in Compose?
173. `navigation-single-source-of-truth` - How do you keep navigation maintainable at scale in Compose apps?
## Theming And Material3 (1 questions -> 1 deep dive)
174. `theming-material3-compose` - How does theming work in Compose with Material 3?
## Animation In Compose (1 questions -> 1 deep dive)
175. `animations-compose` - What animation APIs should you discuss in Compose interviews?
## Testing Interop And Performance (4 questions -> 1 deep dive)
176. `compose-testing-strategy` - What is a strong testing strategy for Compose UI?
177. `semantics-and-test-tags` - How do semantics and test tags help Compose testing?
178. `androidview-interop` - When and how should you use `AndroidView` interop?
179. `compose-performance-checklist` - What is your practical Compose performance checklist?

---

## Concurrency Questions
## Coroutine Internals (4 questions -> 1 deep dive)
180. `structured-concurrency` - What is structured concurrency?
181. `suspend-functions` - What is a suspend function?
182. `continuation-and-cps` - What is a Continuation in Kotlin coroutines?
183. `coroutine-state-machine` - How does coroutine suspension work internally?
## Threads Vs Coroutines (1 questions -> 1 deep dive)
184. `threads-vs-coroutines` - What is the difference between threads and coroutines?
## Threads Dispatchers Context (2 questions -> 1 deep dive)
185. `dispatchers-overview` - What are Dispatchers in Kotlin Coroutines?
186. `withcontext-purpose` - What does `withContext` do and why is it important?
## Structured Scope And Jobs (4 questions -> 1 deep dive)
187. `coroutine-scope` - What is `CoroutineScope` and why does it matter?
188. `job-hierarchy` - How does coroutine job hierarchy work?
189. `supervisorjob` - What is the difference between `Job` and `SupervisorJob`?
190. `supervisorScope` - What does `supervisorScope` do?
## Cancellation Exception Supervision (4 questions -> 1 deep dive)
191. `coroutine-cancellation` - How does coroutine cancellation work?
192. `cooperative-cancellation` - What is cooperative cancellation?
193. `coroutine-exception-handling` - How are exceptions handled in coroutines?
194. `coroutineexceptionhandler` - What is `CoroutineExceptionHandler` used for?
## Launch Async Parallelism (3 questions -> 1 deep dive)
195. `launch-vs-async` - What is the difference between `launch` and `async`?
196. `lazy-async` - What is lazy async?
197. `parallelism-limit` - How do you limit coroutine parallelism?
## Scheduler Thread Pools (2 questions -> 1 deep dive)
198. `thread-pools` - What are coroutine thread pools?
199. `thread-starvation` - What is thread starvation in concurrency?
## Parallelism And Scheduling (1 questions -> 1 deep dive)
200. `limited-parallelism` - What is `limitedParallelism` in coroutines?
## Flow Fundamentals (10 questions -> 1 deep dive)
201. `flow-what-is` - What is Flow in Kotlin?
202. `cold-vs-hot-flow` - What is the difference between cold and hot flows?
203. `backpressure` - What is backpressure in Flow?
204. `explain-coroutine-exception-handling-try-catch-coroutineexceptionhandl` - Explain coroutine exception handling - try/catch, CoroutineExceptionHandler, and SupervisorJob
205. `compare-channels-vs-flow-vs-sharedflow-how-to-choose-the-right-primiti` - Compare Channels vs Flow vs SharedFlow — how to choose the right primitive
206. `explain-cancellation-cooperation-in-coroutines-where-it-works-and-wher` - Explain cancellation cooperation in coroutines — where it works and where it does not
207. `how-do-withtimeout-and-withtimeoutornull-work-and-what-are-the-ux-corr` - How do withTimeout and withTimeoutOrNull work, and what are the UX correctness traps?
208. `explain-dispatchers-main-immediate-and-re-entrancy-hazards-in-coroutin` - Explain Dispatchers.Main.immediate and re-entrancy hazards in coroutines
209. `explain-state-vs-event-modeling-and-the-singleliveevent-replacement-pa` - Explain state vs event modeling and the SingleLiveEvent replacement pattern
210. `explain-callbackflow-correctness-awaitclose-cancellation-and-leak-prev` - Explain callbackFlow correctness - awaitClose, cancellation, and leak prevention
## Flow Operators And Backpressure (3 questions -> 1 deep dive)
211. `collectLatest` - When should you use `collectLatest`?
212. `flatMapLatest` - When should you use `flatMapLatest`?
213. `buffering-conflation` - What is buffering and conflation in Flow?
## Stateflow Sharedflow And Channels (2 questions -> 1 deep dive)
214. `stateflow-vs-sharedflow` - What is the difference between StateFlow and SharedFlow?
215. `channels-vs-sharedflow` - When should you use a Channel instead of SharedFlow?
## Flow Sharing And Hot Streams (2 questions -> 1 deep dive)
216. `statein-sharein` - What are `stateIn` and `shareIn` used for?
217. `one-off-events-with-sharedflow` - How do you model one-off events with SharedFlow?
## Callbackflow And Channelflow (3 questions -> 1 deep dive)
218. `callbackflow` - What is `callbackFlow`?
219. `channelflow` - What is `channelFlow`?
220. `flow-callback-interop` - How do you bridge callbacks into Flow safely?
## Synchronization And Mutex (4 questions -> 1 deep dive)
221. `mutex` - What is `Mutex` in Kotlin coroutines?
222. `synchronization-strategies` - What are common synchronization strategies in concurrent code?
223. `shared-mutable-state` - Why is shared mutable state dangerous?
224. `atomic-operations` - What are atomic operations used for?
## Thread Confinement And Race Conditions (3 questions -> 1 deep dive)
225. `thread-confinement` - What is thread confinement?
226. `race-conditions` - What is a race condition?
227. `deadlocks` - What is a deadlock?
## Coroutine Testing And Virtual Time (3 questions -> 1 deep dive)
228. `coroutine-testing` - How do you test coroutines?
229. `virtual-time-testing` - How does virtual time testing work?
230. `test-dispatchers` - Why use test dispatchers for coroutine tests?
## Coroutine Debugging And Observability (2 questions -> 1 deep dive)
231. `coroutine-debugging` - How do you debug coroutines in production?
232. `trace-and-observability` - How should you observe coroutine and Flow behavior?
## Android Lifecycle And Flow Collection (1 questions -> 1 deep dive)
233. `repeatOnLifecycle-flow-collection` - How should Flow be collected with Android lifecycle?
## Android Lifecycle And Main Safety (2 questions -> 1 deep dive)
234. `main-safety` - What does main-safety mean?
235. `anr-and-main-thread` - Why do blocking calls on the main thread cause ANRs?
## Production Concurrency Patterns And Tuning (1 questions -> 1 deep dive)
236. `concurrency-performance-optimization` - How do you optimize concurrency performance in production?

---

## Architecture Questions
## Mvvm And Viewmodel (3 questions -> 1 deep dive)
237. `mvvm-basics` - What is MVVM in Android architecture?
238. `viewmodel-role` - What is the role of a ViewModel in scalable Android apps?
239. `savedstatehandle-usage` - When should you use SavedStateHandle in architecture design?
## Mvi And Udf (3 questions -> 1 deep dive)
240. `mvi-what-is` - What is MVI architecture?
241. `mvi-vs-mvvm` - MVVM vs MVI - how do you choose?
242. `udf-principles` - What are the key principles of Unidirectional Data Flow?
## Clean Architecture Layering (8 questions -> 1 deep dive)
243. `clean-architecture-overview` - What is Clean Architecture in Android?
244. `layer-dependency-rule` - What is the dependency rule in layered architecture?
245. `dependency-inversion-android` - How does dependency inversion apply to Android app architecture?
246. `compare-datastore-vs-sharedpreferences-consistency-migration-and-threa` - Compare DataStore vs SharedPreferences - consistency, migration, and threading model
247. `explain-room-flow-invalidation-correctness-problems-and-avoiding-over-` - Explain Room + Flow invalidation - correctness problems and avoiding over-collection
248. `explain-room-transactions-wal-mode-and-concurrency-correctness-under-l` - Explain Room transactions, WAL mode, and concurrency correctness under load
249. `explain-sync-engine-design-idempotency-deduplication-and-at-least-once` - Explain sync engine design - idempotency, deduplication, and at-least-once semantics
250. `explain-deletes-and-tombstones-in-offline-sync-preventing-resurrected-` - Explain deletes and tombstones in offline sync - preventing resurrected data
## Repository Pattern And Data Sources (3 questions -> 1 deep dive)
251. `repository-pattern-purpose` - Why use the Repository pattern?
252. `repository-single-source-truth` - How does a repository support a Single Source of Truth model?
253. `multiple-data-sources-orchestration` - How should repositories orchestrate network, cache, and database sources?
## Use Cases And Domain Layer (3 questions -> 1 deep dive)
254. `use-case-purpose` - What problem do use cases solve in architecture?
255. `use-case-granularity` - How granular should use cases be?
256. `domain-layer-when-to-add` - When is a dedicated domain layer worth adding?
## Dependency Injection Strategies (3 questions -> 1 deep dive)
257. `dependency-injection-what-why` - Why is dependency injection important in Android architecture?
258. `constructor-injection-vs-field-injection` - Constructor injection vs field injection - which is preferred?
259. `di-scope-management` - How do DI scopes affect memory and lifecycle behavior?
## Hilt In Production (2 questions -> 1 deep dive)
260. `hilt-benefits` - What architectural advantages does Hilt provide?
261. `hilt-component-lifetimes` - What Hilt component lifetimes should senior engineers know?
## Dagger And Component Graph (3 questions -> 1 deep dive)
262. `dagger-vs-hilt` - Dagger vs Hilt - what is the architectural tradeoff?
263. `dagger-component-subcomponent` - What should you understand about Dagger components and subcomponents?
264. `dagger-performance-tradeoffs` - What are Dagger/Hilt build and runtime tradeoffs at scale?
## Service Locator And Anti Patterns (2 questions -> 1 deep dive)
265. `service-locator-what-is` - What is a Service Locator pattern?
266. `service-locator-vs-di` - Service Locator vs DI - why does this matter in interviews?
## Modularization Strategies (3 questions -> 1 deep dive)
267. `modularization-why` - Why modularize Android apps?
268. `multi-module-architecture-shapes` - What multi-module structures are common in Android?
269. `api-vs-implementation-modules` - How do API vs implementation module boundaries improve architecture?
## Feature Modules And Boundaries (3 questions -> 1 deep dive)
270. `feature-module-boundaries` - What defines a good feature module boundary?
271. `dynamic-feature-modules-when` - When should you use dynamic feature modules?
272. `dependency-direction-between-modules` - How should dependency direction work between feature modules?
## State Management And Ssot (3 questions -> 1 deep dive)
273. `state-management-android-architecture` - What is a strong state management approach in Android architecture?
274. `single-source-of-truth` - What does Single Source of Truth mean in practice?
275. `immutable-ui-state-models` - Why model UI state as immutable data classes?
## Offline First And Sync (3 questions -> 1 deep dive)
276. `offline-first-principles` - What is offline-first architecture?
277. `sync-strategies-pull-push` - Push, pull, and hybrid sync strategies - when to use each?
278. `conflict-resolution-sync` - How should architecture handle sync conflicts?
## Caching And Pagination Architecture (2 questions -> 1 deep dive)
279. `caching-strategies` - What caching strategies are common in Android architecture?
280. `pagination-architecture` - What does a robust pagination architecture look like?
## Reactive Architecture With Flows (2 questions -> 1 deep dive)
281. `stateflow-architecture` - How does StateFlow fit Android architecture design?
282. `event-handling-one-off-events` - How should one-off events be handled in reactive architecture?
## Ui State And Event Modeling (3 questions -> 1 deep dive)
283. `error-handling-architecture` - What is a good error handling architecture for Android apps?
284. `retry-strategies-architecture` - How do retry strategies fit architecture decisions?
285. `ui-state-modeling-architecture` - How should complex UI state be modeled architecturally?
## Navigation And Deep Link Architecture (2 questions -> 1 deep dive)
286. `navigation-architecture` - What are key principles of navigation architecture?
287. `deep-link-architecture` - How should deep links be designed in modular Android apps?
## Testing Architecture And Testability (1 questions -> 1 deep dive)
288. `architecture-testability` - How do you design Android architecture for high testability?
## Scalability And Team Topologies (1 questions -> 1 deep dive)
289. `scaling-architecture-for-team` - How does architecture impact team scalability?
## Production Tradeoffs And Decision Making (2 questions -> 1 deep dive)
290. `architecture-governance` - What is architecture governance in large Android codebases?
291. `production-architecture-tradeoffs` - How should senior engineers discuss architecture tradeoffs in interviews?

---

## Networking Questions
## Retrofit Fundamentals (2 questions -> 1 deep dive)
292. `retrofit-fundamentals` - What is Retrofit?
293. `coroutines-retrofit` - How does Retrofit work with Kotlin Coroutines?
## Serialization Strategies (2 questions -> 1 deep dive)
294. `retrofit-converters` - How do Retrofit converters work?
295. `json-serialization` - What are differences between Gson, Moshi, and Kotlin Serialization?
## Okhttp Internals (2 questions -> 1 deep dive)
296. `okhttp-interceptors` - What is an OkHttp Interceptor?
297. `okhttp-connection-pooling` - How does OkHttp connection pooling work?
## Rest Api Principles (2 questions -> 1 deep dive)
298. `rest-principles` - What are REST API principles?
299. `http-methods` - When should you use HTTP PUT vs PATCH?
## Authentication Security (2 questions -> 1 deep dive)
300. `authentication` - How should you implement authentication in mobile apps?
301. `https-tls` - What is HTTPS and TLS?
## Certificate Pinning (1 questions -> 1 deep dive)
302. `certificate-pinning` - What is certificate pinning?
## Retry Exponential Backoff (2 questions -> 1 deep dive)
303. `retry-strategies` - How should you implement retry logic?
304. `exponential-backoff` - What is exponential backoff?
## Pagination Architecture (2 questions -> 1 deep dive)
305. `pagination` - How does pagination work in REST APIs?
306. `paging-3` - What is Paging 3 library?
## Caching Strategies (2 questions -> 1 deep dive)
307. `http-caching` - How does HTTP caching work?
308. `etags-conditional` - What are ETags and conditional requests?
## Offline First Architecture (2 questions -> 1 deep dive)
309. `offline-first` - What is offline-first architecture?
310. `sync-engine` - How do you implement a sync engine?
## Conflict Resolution (1 questions -> 1 deep dive)
311. `conflict-resolution` - How should you handle sync conflicts?
## Websockets Streaming (2 questions -> 1 deep dive)
312. `websockets` - What are WebSockets?
313. `streaming-downloads` - How do you handle streaming and large file downloads?
## Error Handling Resilience (2 questions -> 1 deep dive)
314. `network-error-handling` - How should you handle network errors?
315. `resiliency-patterns` - What are network resiliency patterns?
## Compression Optimization (2 questions -> 1 deep dive)
316. `compression` - How does request/response compression work?
317. `battery-optimization` - How do you optimize for battery usage in networking?
## Graphql Advanced (2 questions -> 1 deep dive)
318. `graphql-rest` - What are differences between GraphQL and REST?
319. `grpc-basics` - What is gRPC?
## Network Monitoring Debugging (1 questions -> 1 deep dive)
320. `network-monitoring` - How do you monitor and debug network traffic?
## Rate Limiting Idempotency (3 questions -> 1 deep dive)
321. `rate-limiting` - How do you handle rate limiting?
322. `idempotency` - What is idempotency in APIs?
323. `request-cancellation` - How do you cancel network requests?
## Multipart Uploads (1 questions -> 1 deep dive)
324. `multipart-uploads` - How do you implement multipart file uploads?
## Api Versioning Scalability (2 questions -> 1 deep dive)
325. `api-versioning` - How should you version your APIs?
326. `scalability-cdn` - What is CDN and when to use it?
## Production Networking Patterns (3 questions -> 1 deep dive)
327. `network-security-config` - What is Network Security Configuration?
328. `timeouts` - How should you configure network timeouts?
329. `performance-monitoring` - How do you monitor API performance?

---

## Security Questions
## Threat Modeling And Attack Surface (2 questions -> 1 deep dive)
330. `security-threat-modeling` - How do you threat model an Android app before release?
331. `security-third-party-sdk-risk` - How do you audit and manage the security risk introduced by third-party SDKs?
## Manifest And Component Hardening (3 questions -> 1 deep dive)
332. `security-manifest-hardening` - What manifest hardening checks do you always enforce?
333. `security-exported-components` - How do you secure exported Activities, Services, and Receivers?
334. `security-deep-link-security` - How do you prevent insecure deep link and intent URI handling?
## Data Protection And Keystore (3 questions -> 1 deep dive)
335. `security-data-at-rest` - How do you protect sensitive data at rest on Android?
336. `security-keystore` - When do you use Android Keystore, and what are the common pitfalls?
337. `security-biometric-auth` - How do you implement biometric authentication securely in Android?
## Network Security And Api Abuse (2 questions -> 1 deep dive)
338. `security-network-config` - How do you use Network Security Config in production apps?
339. `security-cert-pinning` - When is certificate pinning worth the operational cost?
## Webview And Client Side Hardening (2 questions -> 1 deep dive)
340. `security-webview-hardening` - What are your WebView hardening defaults?
341. `security-input-validation` - How do you defend against injection and input-based attacks in Android?
## Release Hardening And Runtime Integrity (4 questions -> 1 deep dive)
342. `security-secret-management` - How do you keep API keys and secrets out of the APK?
343. `security-r8-obfuscation` - What does R8/ProGuard protect, and what does it not protect?
344. `security-play-integrity` - How do you use Play Integrity API without locking out legitimate users?
345. `security-logging-pii` - How do you prevent sensitive data leaks through logs and analytics?
## Rasp And Runtime Self Protection (20 questions -> 1 deep dive)
346. `security-rasp-overview` - What is RASP and how does it apply to Android app security?
347. `security-root-detection` - How do you detect rooted or compromised devices at runtime?
348. `security-hook-detection` - How do you detect Frida, Xposed, or LSPosed hooks at runtime?
349. `security-debugger-detection` - How do you detect debugger attachment and reverse-engineering tools at runtime?
350. `security-anti-tamper` - How do you implement APK integrity and anti-tamper checks?
351. `security-emulator-detection` - How do you detect emulated environments for abuse prevention?
352. `security-rasp-response-strategy` - What response strategies should a RASP system use when a threat is detected?
353. `security-dynamic-code-loading` - How do you control dynamic code loading to prevent code injection attacks?
354. `explain-android-security-basics-intents-exported-components-pendingint` - Explain Android security basics - intents, exported components, PendingIntent mutability, and deep link risks
355. `explain-font-scaling-and-dynamic-type-designing-for-1-0-to-2-0-scale-f` - Explain font scaling and dynamic type - designing for 1.0× to 2.0× scale factors without layout breaking
356. `explain-token-handling-access-tokens-vs-refresh-tokens-rotation-and-se` - Explain token handling - access tokens vs refresh tokens, rotation, and secure logout
357. `explain-sensitive-ui-input-security-pins-otps-keyboard-suggestions-aut` - Explain sensitive UI input security - PINs, OTPs, keyboard suggestions, autofill, and screenshots
358. `explain-clipboard-security-risks-otp-interception-clipboard-snooping-a` - Explain clipboard security risks - OTP interception, clipboard snooping, and safe UX patterns
359. `explain-account-takeover-ato-defenses-layered-approach-for-consumer-mo` - Explain account takeover (ATO) defenses - layered approach for consumer mobile apps
360. `explain-passkeys-and-fido2-for-consumer-android-apps-implementation-an` - Explain Passkeys and FIDO2 for consumer Android apps - implementation and UX tradeoffs
361. `explain-session-fixation-and-session-hijacking-protections-in-android-` - Explain session fixation and session hijacking protections in Android apps
362. `explain-push-messaging-security-fcm-token-management-spoofing-and-priv` - Explain push messaging security - FCM token management, spoofing, and privacy
363. `explain-device-compromise-handling-root-and-hook-detection-as-security` - Explain device compromise handling - root and hook detection as security risk signals
364. `explain-secure-high-risk-action-policies-payments-profile-changes-and-` - Explain secure high-risk action policies - payments, profile changes, and step-up authentication
365. `explain-abuse-response-readiness-detection-throttling-and-incident-res` - Explain abuse response readiness - detection, throttling, and incident response for consumer apps

---

## Performance Questions
## Performance Metrics (3 questions -> 1 deep dive)
366. `android-performance-fundamentals` - What are the main performance metrics in Android?
367. `explain-r8-and-proguard-reflection-and-serialization-pitfalls-in-andro` - Explain R8 and ProGuard reflection and serialization pitfalls in Android apps
368. `explain-baseline-profiles-macrobenchmark-and-operationalizing-startup-` - Explain Baseline Profiles, Macrobenchmark, and operationalizing startup performance
## Jank And Frame Drops (1 questions -> 1 deep dive)
369. `jank-and-ui-drops` - What causes jank and how do you fix it?
## Memory Leaks (1 questions -> 1 deep dive)
370. `memory-leaks` - What is a memory leak and how do you find them?
## Memory Management (3 questions -> 1 deep dive)
371. `garbage-collection` - How does garbage collection work in Android?
372. `memory-pressure` - How do you handle memory pressure?
373. `graphics-memory` - How much memory do graphics consume?
## Battery Optimization (1 questions -> 1 deep dive)
374. `battery-optimization` - How do you optimize battery usage?
## Rendering Pipeline (1 questions -> 1 deep dive)
375. `rendering-pipeline` - What is Android rendering pipeline?
## Rendering Optimization (1 questions -> 1 deep dive)
376. `overdraw` - What is overdraw and how do you detect it?
## App Startup (1 questions -> 1 deep dive)
377. `app-startup-time` - How do you reduce app startup time?
## Memory Profiling (1 questions -> 1 deep dive)
378. `memory-profiling` - How do you profile memory usage?
## Cpu Profiling (1 questions -> 1 deep dive)
379. `cpu-profiling` - How do you profile CPU usage?
## Layout Optimization (1 questions -> 1 deep dive)
380. `layout-inflation` - How does layout inflation work?
## Anr Prevention (1 questions -> 1 deep dive)
381. `anr-prevention` - What causes ANR and how do you prevent it?
## Bitmap Optimization (1 questions -> 1 deep dive)
382. `bitmap-optimization` - How do you optimize bitmap memory usage?
## Database Optimization (1 questions -> 1 deep dive)
383. `database-performance` - How do you optimize database queries?
## Network Optimization (1 questions -> 1 deep dive)
384. `network-performance` - How do you optimize network requests?
## Allocation Optimization (2 questions -> 1 deep dive)
385. `string-formatting` - What's the performance impact of string formatting?
386. `object-pooling` - What is object pooling?
## Reflection Optimization (1 questions -> 1 deep dive)
387. `reflection-performance` - What's the performance cost of reflection?
## Recyclerview Optimization (1 questions -> 1 deep dive)
388. `view-recycling` - How does RecyclerView recycling work?
## Initialization Patterns (1 questions -> 1 deep dive)
389. `lazy-initialization` - What is lazy initialization?
## Profiling Tools (3 questions -> 1 deep dive)
390. `perfetto-tracing` - What is Perfetto and how do you use it?
391. `systrace-analysis` - How do you use systrace?
392. `benchmark-tools` - Differences between profiling tools?
## Frame Stability (1 questions -> 1 deep dive)
393. `frame-rate-stability` - How do you ensure stable frame rates?
## Startup Optimization (1 questions -> 1 deep dive)
394. `cold-start-optimization` - What causes slow cold starts?
## Caching Strategies (1 questions -> 1 deep dive)
395. `warm-cache` - How do you keep a warm cache?
## Compose Performance (1 questions -> 1 deep dive)
396. `composition-performance` - How does Compose performance differ from Views?
## Graphics Optimization (1 questions -> 1 deep dive)
397. `shader-compilation` - What is shader compilation?
## Battery Profiling (1 questions -> 1 deep dive)
398. `power-consumption-profiling` - How do you profile power consumption?
## Monitoring Implementation (1 questions -> 1 deep dive)
399. `custom-performance-monitoring` - How do implement custom monitoring?
## Performance Testing (1 questions -> 1 deep dive)
400. `performance-testing` - How do you write performance tests?
## Ux Perception (1 questions -> 1 deep dive)
401. `responsiveness-perception` - Perceived responsiveness vs actual performance?
## Performance Strategy (1 questions -> 1 deep dive)
402. `performance-budgets` - What is a performance budget?
## Gpu Optimization (1 questions -> 1 deep dive)
403. `gpu-rendering-cost` - What is the cost of GPU rendering?
## System Internals (1 questions -> 1 deep dive)
404. `kernel-linux-performance` - How does Linux kernel impact performance?
## Compilation Optimization (1 questions -> 1 deep dive)
405. `ahead-of-time-compilation` - What is AoT compilation?

---

## Cicd Questions
## Ci Cd Fundamentals (3 questions -> 1 deep dive)
406. `cicd-01` - How do you approach ci cd fundamentals in production Android systems
407. `cicd-21` - How do you approach ci cd fundamentals in production Android systems
408. `cicd-41` - How do you approach ci cd fundamentals in production Android systems
## Pipeline Architecture And Orchestration (3 questions -> 1 deep dive)
409. `cicd-02` - How do you approach pipeline architecture and orchestration in production Android systems
410. `cicd-22` - How do you approach pipeline architecture and orchestration in production Android systems
411. `cicd-42` - How do you approach pipeline architecture and orchestration in production Android systems
## Android Build Optimization (3 questions -> 1 deep dive)
412. `cicd-03` - How do you approach android build optimization in production Android systems
413. `cicd-23` - How do you approach android build optimization in production Android systems
414. `cicd-43` - How do you approach android build optimization in production Android systems
## Test Strategy In Pipelines (3 questions -> 1 deep dive)
415. `cicd-04` - How do you approach test strategy in pipelines in production Android systems
416. `cicd-24` - How do you approach test strategy in pipelines in production Android systems
417. `cicd-44` - How do you approach test strategy in pipelines in production Android systems
## Branching And Release Workflows (3 questions -> 1 deep dive)
418. `cicd-05` - How do you approach branching and release workflows in production Android systems
419. `cicd-25` - How do you approach branching and release workflows in production Android systems
420. `cicd-45` - How do you approach branching and release workflows in production Android systems
## Artifact Management And Versioning (3 questions -> 1 deep dive)
421. `cicd-06` - How do you approach artifact management and versioning in production Android systems
422. `cicd-26` - How do you approach artifact management and versioning in production Android systems
423. `cicd-46` - How do you approach artifact management and versioning in production Android systems
## Secrets Signing And Key Management (3 questions -> 1 deep dive)
424. `cicd-07` - How do you approach secrets signing and key management in production Android systems
425. `cicd-27` - How do you approach secrets signing and key management in production Android systems
426. `cicd-47` - How do you approach secrets signing and key management in production Android systems
## Static Analysis And Quality Gates (3 questions -> 1 deep dive)
427. `cicd-08` - How do you approach static analysis and quality gates in production Android systems
428. `cicd-28` - How do you approach static analysis and quality gates in production Android systems
429. `cicd-48` - How do you approach static analysis and quality gates in production Android systems
## Dependency Security And Supply Chain (3 questions -> 1 deep dive)
430. `cicd-09` - How do you approach dependency security and supply chain in production Android systems
431. `cicd-29` - How do you approach dependency security and supply chain in production Android systems
432. `cicd-49` - How do you approach dependency security and supply chain in production Android systems
## Infrastructure As Code For Ci (3 questions -> 1 deep dive)
433. `cicd-10` - How do you approach infrastructure as code for ci in production Android systems
434. `cicd-30` - How do you approach infrastructure as code for ci in production Android systems
435. `cicd-50` - How do you approach infrastructure as code for ci in production Android systems
## Runner Strategy And Scaling (2 questions -> 1 deep dive)
436. `cicd-11` - How do you approach runner strategy and scaling in production Android systems
437. `cicd-31` - How do you approach runner strategy and scaling in production Android systems
## Caching And Incremental Builds (2 questions -> 1 deep dive)
438. `cicd-12` - How do you approach caching and incremental builds in production Android systems
439. `cicd-32` - How do you approach caching and incremental builds in production Android systems
## Deployment Strategies And Rollouts (2 questions -> 1 deep dive)
440. `cicd-13` - How do you approach deployment strategies and rollouts in production Android systems
441. `cicd-33` - How do you approach deployment strategies and rollouts in production Android systems
## Feature Flags And Kill Switches (2 questions -> 1 deep dive)
442. `cicd-14` - How do you approach feature flags and kill switches in production Android systems
443. `cicd-34` - How do you approach feature flags and kill switches in production Android systems
## Play Store Release Automation (2 questions -> 1 deep dive)
444. `cicd-15` - How do you approach play store release automation in production Android systems
445. `cicd-35` - How do you approach play store release automation in production Android systems
## Monitoring Release Health (2 questions -> 1 deep dive)
446. `cicd-16` - How do you approach monitoring release health in production Android systems
447. `cicd-36` - How do you approach monitoring release health in production Android systems
## Rollback And Incident Response (2 questions -> 1 deep dive)
448. `cicd-17` - How do you approach rollback and incident response in production Android systems
449. `cicd-37` - How do you approach rollback and incident response in production Android systems
## Compliance Auditability And Governance (2 questions -> 1 deep dive)
450. `cicd-18` - How do you approach compliance auditability and governance in production Android systems
451. `cicd-38` - How do you approach compliance auditability and governance in production Android systems
## Cost Optimization In Ci Cd (2 questions -> 1 deep dive)
452. `cicd-19` - How do you approach cost optimization in ci cd in production Android systems
453. `cicd-39` - How do you approach cost optimization in ci cd in production Android systems
## Staff Level Devex And Platform Strategy (2 questions -> 1 deep dive)
454. `cicd-20` - How do you approach staff level devex and platform strategy in production Android systems
455. `cicd-40` - How do you approach staff level devex and platform strategy in production Android systems
## Android App Release Process (3 questions -> 1 deep dive)
456. `cicd-51` - Walk through the complete Android app release process end to end
457. `cicd-52` - Explain how to publish an Android library to Maven Central and JitPack
458. `explain-gradle-build-performance-kapt-vs-ksp-configuration-cache-and-m` - Explain Gradle build performance - KAPT vs KSP, configuration cache, and modularization impact

---

## Advanced Questions
## Android Runtime Internals (1 questions -> 1 deep dive)
459. `advanced-01` - Explain the Android Runtime (ART) internals and how to optimize it in production
## Binder And Ipc At Scale (1 questions -> 1 deep dive)
460. `advanced-02` - Discuss Binder IPC design choices and scaling challenges in system_server
## Zygote Art And Startup (1 questions -> 1 deep dive)
461. `advanced-03` - Explain Zygote's role in app startup and memory efficiency via Copy-on-Write
## Renderthread And Gpu Pipeline (1 questions -> 1 deep dive)
462. `advanced-04` - Walk through frame pipelining, triple buffering, and jank diagnosis on RenderThread
## Memory Model And Gc Tuning (1 questions -> 1 deep dive)
463. `advanced-05` - What factors influence GC tuning decisions in ART and how do you measure them
## Aosp Framework Layering (1 questions -> 1 deep dive)
464. `advanced-06` - Describe the AOSP layered architecture from kernel through apps and its constraints
## System Services And Lifecycle (1 questions -> 1 deep dive)
465. `advanced-07` - Explain how system services enforce lifecycle and manage resource contention across apps
## Input Window And Surfaceflinger (1 questions -> 1 deep dive)
466. `advanced-08` - Discuss input dispatch routing and SurfaceFlinger composition; when do deadlocks occur
## Android Security Model (1 questions -> 1 deep dive)
467. `advanced-09` - Explain Android's defense-in-depth security layers and how privilege escalation exploits work
## Sepolicy And Sandboxing (1 questions -> 1 deep dive)
468. `advanced-10` - What is SEPolicy Type Enforcement and how do you debug sandboxing violations in production
## Native Interop And Ndk (1 questions -> 1 deep dive)
469. `advanced-11` - When should you use NDK and how do you measure performance gains vs complexity costs
## Jni Performance And Safety (1 questions -> 1 deep dive)
470. `advanced-12` - Explain JNI reference management, critical sections, and their GC interaction
## Power Management Doze And Jobs (1 questions -> 1 deep dive)
471. `advanced-13` - Design a background sync strategy balancing battery life, data freshness, and reliability
## Storage Stack And Filesystems (1 questions -> 1 deep dive)
472. `advanced-14` - Discuss scoped storage constraints and tradeoffs when migrating legacy apps
## Network Stack And Connectivity (1 questions -> 1 deep dive)
473. `advanced-15` - Analyze connection pooling, DNS caching, and radio state transitions for battery optimization
## Boot Flow And Init (1 questions -> 1 deep dive)
474. `advanced-16` - Explain the Android boot sequence and init.rc scripting language with failure modes
## Instrumentation Tracing And Profiler Internals (1 questions -> 1 deep dive)
475. `advanced-17` - Compare systrace, Perfetto, and method tracing; when would you use each one
## Multithreading And Scheduler Behavior (1 questions -> 1 deep dive)
476. `advanced-18` - Explain the CFS scheduler and Android thread priority model; when does starvation occur
## Modularization At Scale (1 questions -> 1 deep dive)
477. `advanced-19` - Design a modular app architecture; why is the dependency graph acyclic and what breaks
## Advanced Tradeoffs And Interview Strategy (2 questions -> 1 deep dive)
478. `advanced-20` - When facing an architectural decision, what factors matter most and how do you measure
479. `explain-android-background-restrictions-doze-app-standby-and-backgroun` - Explain Android background restrictions - Doze, App Standby, and background start limits
## Reactive Programming And Rxjava (1 questions -> 1 deep dive)
480. `advanced-21` - Design a reactive architecture using RxJava; explain backpressure and operator fusion
## Dependency Injection At Scale (1 questions -> 1 deep dive)
481. `advanced-22` - Architect dependency injection at scale using Dagger/Hilt; when do circular deps occur
## Jetpack Compose Performance (1 questions -> 1 deep dive)
482. `advanced-23` - Explain Jetpack Compose recomposition triggers and how to prevent excessive redraws
## Custom View Rendering And Invalidation (1 questions -> 1 deep dive)
483. `advanced-24` - Walk through custom view measurement, layout, and drawing phases; how do invalidations cascade
## Choreographer And Animation Timing (1 questions -> 1 deep dive)
484. `advanced-25` - Explain Choreographer frame pacing callbacks and how animations sync to display vsync
## Room Database Query Optimization (1 questions -> 1 deep dive)
485. `advanced-26` - Design a Room database strategy avoiding N+1 queries and slow index misses
## Workmanager And Background Execution (1 questions -> 1 deep dive)
486. `advanced-27` - Compare WorkManager, periodic JobScheduler, and foreground services; which guarantees work executes
## Gradle Plugin Architecture (1 questions -> 1 deep dive)
487. `advanced-28` - Design a Gradle plugin architecture; explain incremental tasks and caching for build performance
## Data Serialization Tradeoffs (1 questions -> 1 deep dive)
488. `advanced-29` - Compare Protobuf vs JSON serialization; when do you use each and what are evolution risks
## Firebase Offline Sync And Conflicts (1 questions -> 1 deep dive)
489. `advanced-30` - Architect Firebase offline sync; explain conflict resolution when device and cloud both write

---

## Aosp Questions
## Binder Ipc And Threading (4 questions -> 1 deep dive)
490. `aosp-01` - Explain Binder IPC transaction lifecycle from client stub to server thread
491. `aosp-02` - How do Binder thread pools affect system service throughput and latency
492. `aosp-03` - What is a Binder death recipient and when should you use it
493. `aosp-04` - How do you debug slow Binder calls in production traces
## Ams And Process Lifecycle (4 questions -> 1 deep dive)
494. `aosp-05` - Walk through ActivityManagerService process state transitions
495. `aosp-06` - How does AMS decide what to kill under memory pressure
496. `aosp-07` - What are common AMS lifecycle race conditions and mitigations
497. `aosp-08` - How do background execution limits change AMS behavior across API levels
## Windowmanager Surfaceflinger Render Pipeline (4 questions -> 1 deep dive)
498. `aosp-09` - Explain frame production pipeline from app render to SurfaceFlinger composition
499. `aosp-10` - How do WindowManager and InputDispatcher coordinate focus and input routing
500. `aosp-11` - What causes jank in SurfaceFlinger pipeline and how do you isolate it
501. `aosp-12` - How do buffer queue and triple buffering trade latency for smoothness
## Zygote Art And App Startup (4 questions -> 1 deep dive)
502. `aosp-13` - Why does Android use Zygote and copy-on-write process forking
503. `aosp-14` - Explain ART startup path and dex optimization modes in modern Android
504. `aosp-15` - What startup costs are hidden in class loading and static initialization
505. `aosp-16` - How do Baseline Profiles interact with ART and app startup performance
## Boot Init And System Server (4 questions -> 1 deep dive)
506. `aosp-17` - Walk through Android boot flow from bootloader to launcher ready
507. `aosp-18` - What is system_server and why is it the most critical process
508. `aosp-19` - How do init rc scripts influence security and boot reliability
509. `aosp-20` - How do watchdog mechanisms protect Android from system service hangs
## Security Selinux And Sandboxing (4 questions -> 1 deep dive)
510. `aosp-21` - Explain Android sandbox model and SELinux role in defense in depth
511. `aosp-22` - How do you debug SELinux denials without weakening policy
512. `aosp-23` - What are common privilege escalation paths in Android service architecture
513. `aosp-24` - How do runtime permissions map to framework and kernel enforcement
## Memory Gc And Scheduler Behavior (4 questions -> 1 deep dive)
514. `aosp-25` - How does ART garbage collection interact with UI jank and latency
515. `aosp-26` - Explain Linux CFS scheduling effects on Android thread priorities
516. `aosp-27` - What thread priority anti-patterns commonly break Android performance
517. `aosp-28` - How do you measure and reduce context-switch overhead in heavy IPC flows
## Power Background Execution And Jobs (4 questions -> 1 deep dive)
518. `aosp-29` - Explain Doze internals and maintenance windows for deferred work
519. `aosp-30` - How do App Standby Buckets and quotas impact background job reliability
520. `aosp-31` - WorkManager vs JobScheduler vs ForegroundService at framework level
521. `aosp-32` - How do wakelock anti-patterns cause battery and thermal regressions

---

## Future Tech Questions
## Mobile Ai Foundations (3 questions -> 1 deep dive)
522. `future-tech-01` - How do you approach mobile ai foundations in production Android systems
523. `future-tech-21` - How do you approach mobile ai foundations in production Android systems
524. `future-tech-41` - How do you approach mobile ai foundations in production Android systems
## On Device Ml Inference (3 questions -> 1 deep dive)
525. `future-tech-02` - How do you approach on device ml inference in production Android systems
526. `future-tech-22` - How do you approach on device ml inference in production Android systems
527. `future-tech-42` - How do you approach on device ml inference in production Android systems
## Edge Ai Privacy And Governance (3 questions -> 1 deep dive)
528. `future-tech-03` - How do you approach edge ai privacy and governance in production Android systems
529. `future-tech-23` - How do you approach edge ai privacy and governance in production Android systems
530. `future-tech-43` - How do you approach edge ai privacy and governance in production Android systems
## Ai Assisted Development Workflows (3 questions -> 1 deep dive)
531. `future-tech-04` - How do you approach ai assisted development workflows in production Android systems
532. `future-tech-24` - How do you approach ai assisted development workflows in production Android systems
533. `future-tech-44` - How do you approach ai assisted development workflows in production Android systems
## Agentic Mobile Experiences (3 questions -> 1 deep dive)
534. `future-tech-05` - How do you approach agentic mobile experiences in production Android systems
535. `future-tech-25` - How do you approach agentic mobile experiences in production Android systems
536. `future-tech-45` - How do you approach agentic mobile experiences in production Android systems
## Foldables And Adaptive Ui (3 questions -> 1 deep dive)
537. `future-tech-06` - How do you approach foldables and adaptive ui in production Android systems
538. `future-tech-26` - How do you approach foldables and adaptive ui in production Android systems
539. `future-tech-46` - How do you approach foldables and adaptive ui in production Android systems
## Large Screen And Multi Window Strategy (3 questions -> 1 deep dive)
540. `future-tech-07` - How do you approach large screen and multi window strategy in production Android systems
541. `future-tech-27` - How do you approach large screen and multi window strategy in production Android systems
542. `future-tech-47` - How do you approach large screen and multi window strategy in production Android systems
## Wearables And Health Tech (3 questions -> 1 deep dive)
543. `future-tech-08` - How do you approach wearables and health tech in production Android systems
544. `future-tech-28` - How do you approach wearables and health tech in production Android systems
545. `future-tech-48` - How do you approach wearables and health tech in production Android systems
## Xr Ar Vr Mobile Platforms (3 questions -> 1 deep dive)
546. `future-tech-09` - How do you approach xr ar vr mobile platforms in production Android systems
547. `future-tech-29` - How do you approach xr ar vr mobile platforms in production Android systems
548. `future-tech-49` - How do you approach xr ar vr mobile platforms in production Android systems
## Ambient Computing And Context Awareness (3 questions -> 1 deep dive)
549. `future-tech-10` - How do you approach ambient computing and context awareness in production Android systems
550. `future-tech-30` - How do you approach ambient computing and context awareness in production Android systems
551. `future-tech-50` - How do you approach ambient computing and context awareness in production Android systems
## Multimodal Interfaces Voice Vision (2 questions -> 1 deep dive)
552. `future-tech-11` - How do you approach multimodal interfaces voice vision in production Android systems
553. `future-tech-31` - How do you approach multimodal interfaces voice vision in production Android systems
## Offline Intelligence Patterns (2 questions -> 1 deep dive)
554. `future-tech-12` - How do you approach offline intelligence patterns in production Android systems
555. `future-tech-32` - How do you approach offline intelligence patterns in production Android systems
## Federated Learning And Personalization (2 questions -> 1 deep dive)
556. `future-tech-13` - How do you approach federated learning and personalization in production Android systems
557. `future-tech-33` - How do you approach federated learning and personalization in production Android systems
## Kmp And Cross Platform Architecture (2 questions -> 1 deep dive)
558. `future-tech-14` - How do you approach kmp and cross platform architecture in production Android systems
559. `future-tech-34` - How do you approach kmp and cross platform architecture in production Android systems
## Modern Android Hardware Acceleration (2 questions -> 1 deep dive)
560. `future-tech-15` - How do you approach modern android hardware acceleration in production Android systems
561. `future-tech-35` - How do you approach modern android hardware acceleration in production Android systems
## Energy Efficient Ai On Mobile (2 questions -> 1 deep dive)
562. `future-tech-16` - How do you approach energy efficient ai on mobile in production Android systems
563. `future-tech-36` - How do you approach energy efficient ai on mobile in production Android systems
## Mobile Security For Ai Features (2 questions -> 1 deep dive)
564. `future-tech-17` - How do you approach mobile security for ai features in production Android systems
565. `future-tech-37` - How do you approach mobile security for ai features in production Android systems
## Future Networking 5G Edge (2 questions -> 1 deep dive)
566. `future-tech-18` - How do you approach future networking 5g edge in production Android systems
567. `future-tech-38` - How do you approach future networking 5g edge in production Android systems
## Emerging Product Strategy And Experimentation (2 questions -> 1 deep dive)
568. `future-tech-19` - How do you approach emerging product strategy and experimentation in production Android systems
569. `future-tech-39` - How do you approach emerging product strategy and experimentation in production Android systems
## Future Tech Tradeoffs And Interview Strategy (2 questions -> 1 deep dive)
570. `future-tech-20` - How do you approach future tech tradeoffs and interview strategy in production Android systems
571. `future-tech-40` - How do you approach future tech tradeoffs and interview strategy in production Android systems

---

## System Design Questions
## System Design Fundamentals (5 questions -> 1 deep dive)
572. `system-design` - What is Android system design in interviews?
573. `design-round-structure` - What is a strong structure for solving design rounds?
574. `design-a-push-notification-system-end-to-end-with-privacy-and-delivery` - Design a push notification system end-to-end with privacy and delivery correctness
575. `design-app-modularization-for-a-large-compose-app-with-100-screens` - Design app modularization for a large Compose app with 100+ screens
576. `design-api-versioning-and-backward-compatibility-strategy-for-mobile-r` - Design API versioning and backward compatibility strategy for mobile releases
## Requirements And Scope (2 questions -> 1 deep dive)
577. `functional-vs-nonfunctional-requirements` - How do you separate functional vs non-functional requirements?
578. `scope-definition` - How do you define scope for a system design round?
## Scalability And Capacity Planning (2 questions -> 1 deep dive)
579. `estimations` - How do you do quick capacity estimations?
580. `horizontal-scaling` - How do you scale a system horizontally?
## High Level Architecture (3 questions -> 1 deep dive)
581. `high-level-components` - How do you structure high-level components?
582. `service-boundaries` - How do you define service boundaries?
583. `load-balancing` - How do load balancers fit into architecture design?
## Data Modeling And Storage (2 questions -> 1 deep dive)
584. `data-modeling` - How do you approach data modeling in system design?
585. `sql-vs-nosql` - When do you choose SQL vs NoSQL?
## Search And Indexing (3 questions -> 1 deep dive)
586. `indexing-strategy` - How do indexes affect read and write performance?
587. `search-architecture` - How do you design search for low-latency queries?
588. `eventual-consistency-search` - Why is search often eventually consistent?
## Consistency And Transactions (2 questions -> 1 deep dive)
589. `consistency-models` - What consistency models should you discuss in interviews?
590. `transactions-and-sagas` - When should you use transactions vs sagas?
## Caching Strategies (2 questions -> 1 deep dive)
591. `cache-aside` - What is cache-aside and when is it useful?
592. `cache-invalidation` - Why is cache invalidation hard?
## Queueing And Async Processing (3 questions -> 1 deep dive)
593. `message-queues` - When do you add a message queue?
594. `event-driven-design` - What are event-driven architecture tradeoffs?
595. `backpressure-in-systems` - What is backpressure in distributed systems?
## Api Design And Gateways (4 questions -> 1 deep dive)
596. `api-gateway` - What role does an API gateway play?
597. `rest-vs-grpc-design` - How do you choose REST vs gRPC for internal APIs?
598. `versioning-strategy` - How do you version APIs safely?
599. `rate-limiting` - How do you design rate limiting?
## Security And Compliance (4 questions -> 1 deep dive)
600. `authn-vs-authz` - How do you model authentication vs authorization?
601. `security-hardening` - What security hardening do you mention in interviews?
602. `tenant-isolation` - How do you design multi-tenant isolation?
603. `data-retention` - How do retention policies affect architecture?
## Observability And Slos (2 questions -> 1 deep dive)
604. `slos-and-slas` - How do SLOs/SLAs shape architecture decisions?
605. `logging-metrics-tracing` - Why are logs, metrics, and traces all needed?
## Resilience And Failure Handling (3 questions -> 1 deep dive)
606. `circuit-breaker` - What is a circuit breaker and why use it?
607. `bulkheads-and-timeouts` - How do timeouts, retries, and bulkheads work together?
608. `idempotency` - Why is idempotency important in distributed systems?
## Multi Region And Disaster Recovery (2 questions -> 1 deep dive)
609. `multi-region` - When do you move to multi-region architecture?
610. `disaster-recovery-rpo-rto` - How do RPO and RTO influence disaster recovery design?
## Cost Optimization (2 questions -> 1 deep dive)
611. `cost-vs-latency` - How do you balance cost vs latency?
612. `capacity-headroom` - How much capacity headroom should a production system keep?
## Mobile Backend For Frontend (2 questions -> 1 deep dive)
613. `bff-pattern` - What is Backend-for-Frontend (BFF) and when should Android use it?
614. `edge-caching-mobile` - How does edge caching improve mobile user experience?
## Real Time Systems (2 questions -> 1 deep dive)
615. `realtime-chat-design` - How would you design a real-time chat backend?
616. `fanout-problem` - How do you handle fan-out at scale?
## Analytics Pipeline Design (2 questions -> 1 deep dive)
617. `analytics-pipeline` - How do you design analytics ingestion pipelines?
618. `batch-vs-stream` - When do you choose batch vs stream processing?
## Migration And Evolution Strategies (2 questions -> 1 deep dive)
619. `migration-strangler` - What is the strangler pattern for migrations?
620. `schema-evolution` - How do you manage schema evolution safely?
## Tradeoffs And Decision Frameworks (4 questions -> 1 deep dive)
621. `tradeoff-framework` - How do you present tradeoffs clearly in interviews?
622. `cap-theorem-practical` - How do you explain CAP theorem pragmatically?
623. `read-heavy-vs-write-heavy` - How does workload shape architecture choices?
624. `availability-vs-consistency` - How do you choose availability vs consistency?

---

## Testing Questions
## Testing Fundamentals (2 questions -> 1 deep dive)
625. `testing-strategy` - How do you define an Android testing strategy?
626. `qa-dev-collaboration` - How should QA and dev collaborate on automation?
## Test Pyramid And Strategy (4 questions -> 1 deep dive)
627. `test-pyramid` - What is the test pyramid and why does it matter?
628. `unit-vs-integration` - What is the difference between unit and integration tests?
629. `hermetic-tests` - What are hermetic tests and why are they valuable?
630. `risk-based-testing` - What is risk-based testing?
## Unit Testing Viewmodel (3 questions -> 1 deep dive)
631. `viewmodel-unit-tests` - How do you unit test a ViewModel?
632. `usecase-tests` - How should use cases be tested?
633. `clock-abstraction` - How does clock abstraction improve test reliability?
## Repository And Data Layer Testing (2 questions -> 1 deep dive)
634. `repository-tests` - How do you test repository logic with multiple data sources?
635. `datasource-tests` - How do you test remote and local data sources?
## Integration Testing (1 questions -> 1 deep dive)
636. `integration-boundary` - When should you add integration tests?
## Ui Testing With Compose (2 questions -> 1 deep dive)
637. `compose-ui-tests` - How do Compose UI tests differ from View UI tests?
638. `semantics-testing` - Why are semantics important in Compose tests?
## Espresso And Ui Automation (3 questions -> 1 deep dive)
639. `espresso-basics` - When do you still use Espresso?
640. `idling-resources` - What are idling resources and when are they needed?
641. `android-test-runner` - How do you structure instrumentation test modules?
## Mocking Fakes And Stubs (3 questions -> 1 deep dive)
642. `mocks-vs-fakes` - When should you use mocks vs fakes?
643. `stub-vs-spy` - What is the difference between stubs and spies?
644. `test-data-builders` - Why use test data builders?
## Coroutine And Flow Testing (3 questions -> 1 deep dive)
645. `coroutine-test` - How do you test coroutines deterministically?
646. `virtual-time` - Why is virtual time important for async tests?
647. `flow-test-patterns` - How do you test Flow emissions?
## Stateflow Sharedflow Testing (2 questions -> 1 deep dive)
648. `stateflow-testing` - How do you test StateFlow UI state?
649. `sharedflow-events-testing` - How do you test one-off SharedFlow events?
## Network Testing And Mockwebserver (1 questions -> 1 deep dive)
650. `mockwebserver` - Why use MockWebServer for networking tests?
## Contract Testing (3 questions -> 1 deep dive)
651. `api-contract-tests` - How do you keep API tests resilient to server changes?
652. `consumer-contract` - What is consumer-driven contract testing?
653. `contract-mocks` - How do contracts reduce mock drift?
## Database Testing Room (2 questions -> 1 deep dive)
654. `room-inmemory-tests` - How do you test Room with in-memory databases?
655. `migration-tests` - Why are Room migration tests critical?
## Testability And Architecture (3 questions -> 1 deep dive)
656. `testable-architecture` - What makes Android architecture testable?
657. `dependency-injection-testing` - How does DI improve testability?
658. `test-maintenance-cost` - How do you manage long-term test maintenance cost?
## Flaky Test Diagnostics (3 questions -> 1 deep dive)
659. `flaky-tests` - What causes flaky tests?
660. `stabilize-ui-tests` - How do you stabilize flaky UI tests?
661. `retry-in-tests` - Should flaky tests be fixed with retries?
## Performance And Benchmark Testing (2 questions -> 1 deep dive)
662. `benchmark-tests` - When should you add benchmark tests?
663. `macrobenchmark` - What does Macrobenchmark validate?
## Snapshot And Golden Testing (2 questions -> 1 deep dive)
664. `golden-tests` - What are snapshot or golden tests?
665. `visual-regression` - How do visual regression tests fit release safety?
## E2E Testing And Release Gates (2 questions -> 1 deep dive)
666. `e2e-tests` - What are good use cases for end-to-end tests?
667. `release-gates` - How should tests gate production releases?
## Ci Cd Test Pipelines (3 questions -> 1 deep dive)
668. `ci-pipeline` - How do you design a fast CI test pipeline?
669. `sharding-tests` - When should you shard test suites?
670. `test-environments` - How do you manage test environments across teams?
## Test Metrics And Quality Governance (4 questions -> 1 deep dive)
671. `test-reporting` - What metrics should test reports include?
672. `quality-gates` - How do quality gates prevent regressions?
673. `mutation-testing` - Where does mutation testing fit in Android?
674. `postmortem-regression-tests` - How do you turn incidents into regression tests?

---

## Behavioral Questions
## Behavioral Fundamentals (4 questions -> 1 deep dive)
675. `behavioral-interviews` - What do interviewers evaluate in behavioral rounds?
676. `walk-through-driving-a-major-view-to-compose-migration-without-stoppin` - Walk through driving a major View-to-Compose migration without stopping feature delivery
677. `describe-mentoring-engineers-and-raising-the-bar-on-compose-code-quali` - Describe mentoring engineers and raising the bar on Compose code quality at scale
678. `walk-through-making-a-technical-decision-under-uncertainty-build-vs-bu` - Walk through making a technical decision under uncertainty - build vs buy, library choice
## Interview Story Frameworks (2 questions -> 1 deep dive)
679. `star-method` - How should you use STAR effectively?
680. `story-selection` - How do you select strong interview stories quickly?
## Ownership And Accountability (2 questions -> 1 deep dive)
681. `ownership-example` - How do you present a strong ownership story?
682. `accountability-vs-ownership` - What is the difference between accountability and ownership?
## Conflict Resolution (2 questions -> 1 deep dive)
683. `handling-conflict` - How do you discuss conflict with a teammate?
684. `disagree-and-commit` - How do you answer "tell me about a disagreement"?
## Stakeholder Management (2 questions -> 1 deep dive)
685. `stakeholder-alignment` - How do you align engineering and product stakeholders?
686. `influence-roadmap` - How do you influence roadmap decisions?
## Prioritization And Tradeoffs (3 questions -> 1 deep dive)
687. `tradeoff-prioritization` - How do you prioritize under tight deadlines?
688. `saying-no` - How do you say no to low-impact requests?
689. `tradeoff-communication` - How do you communicate tradeoffs to non-technical stakeholders?
## Mentorship And Team Growth (3 questions -> 1 deep dive)
690. `mentoring-juniors` - How do you describe mentoring junior engineers?
691. `growing-senior-engineers` - How do you grow senior engineers on your team?
692. `dealing-with-low-performer` - How do you support a struggling teammate?
## Leadership Without Authority (2 questions -> 1 deep dive)
693. `lead-without-authority` - How do you lead without formal authority?
694. `driving-adoption` - How do you drive adoption of technical standards?
## Incident Management And Postmortems (3 questions -> 1 deep dive)
695. `incident-response-story` - How do you explain your role during a production incident?
696. `blameless-postmortem` - What makes a postmortem blameless and actionable?
697. `production-accountability` - How do you show accountability after production issues?
## Delivery And Execution (2 questions -> 1 deep dive)
698. `execution-under-pressure` - How do you deliver under pressure without burnout?
699. `missed-deadline` - How do you answer questions about missing deadlines?
## Decision Making Under Ambiguity (3 questions -> 1 deep dive)
700. `ambiguity` - How do you make decisions under ambiguity?
701. `insufficient-data-decisions` - How do you decide with incomplete data?
702. `unpopular-decision` - How do you defend an unpopular decision?
## Feedback Culture (3 questions -> 1 deep dive)
703. `giving-feedback` - How do you give difficult feedback?
704. `receiving-feedback` - How do you respond to critical feedback?
705. `upward-feedback` - How do you give respectful upward feedback?
## Cross Functional Collaboration (3 questions -> 1 deep dive)
706. `cross-functional-collab` - How do you collaborate with design and QA?
707. `product-engineering-partnership` - How do you build trust with product managers?
708. `partner-with-ops` - How do you partner with SRE/ops teams effectively?
## Career Growth And Self Reflection (3 questions -> 1 deep dive)
709. `career-growth-plan` - How do you discuss your growth plan?
710. `failure-story` - How do you tell a failure story well?
711. `self-awareness` - How do you demonstrate self-awareness in interviews?
## Managing Up (3 questions -> 1 deep dive)
712. `manage-up` - How do you manage up effectively?
713. `escalation` - When and how should you escalate issues?
714. `expectation-alignment-manager` - How do you align expectations with your manager?
## Staff Level Behavioral Signals (3 questions -> 1 deep dive)
715. `staff-scope` - What behavioral signals are expected at staff level?
716. `org-impact` - How do you show organization-level impact?
717. `staff-cross-team-conflict` - How do staff engineers resolve cross-team conflict?
## Ethical Decision Making (3 questions -> 1 deep dive)
718. `ethical-tradeoff` - How do you handle ethical tradeoffs in product decisions?
719. `privacy-vs-growth` - How do you discuss privacy vs growth tension?
720. `ethical-escalation` - When should ethical concerns be escalated?
## Remote And Distributed Teams (3 questions -> 1 deep dive)
721. `remote-collaboration` - How do you maintain alignment in remote teams?
722. `async-communication` - What does strong async communication look like?
723. `remote-trust-building` - How do you build trust in distributed teams?
## Behavioral Anti Patterns (2 questions -> 1 deep dive)
724. `behavioral-red-flags` - What behavioral anti-patterns hurt candidates?
725. `blame-language` - Why is blame language risky in interviews?
## Communication And Clarity (2 questions -> 1 deep dive)
726. `clarity-structure` - How do you keep answers concise and structured?
727. `executive-summary` - How do you open answers with an executive summary?

---
## Statistics
- **Total Questions:** 727
- **Total Deep Dives:** 301
- **Fundamentals:** 57 questions
- **Kotlin:** 61 questions
- **Compose:** 61 questions
- **Concurrency:** 57 questions
- **Architecture:** 55 questions
- **Networking:** 38 questions
- **Security:** 36 questions
- **Performance:** 40 questions
- **Cicd:** 53 questions
- **Advanced:** 31 questions
- **Aosp:** 32 questions
- **Future Tech:** 50 questions
- **System Design:** 53 questions
- **Testing:** 50 questions
- **Behavioral:** 53 questions
- **Beginner:** 78 questions
- **Intermediate:** 356 questions
- **Advanced:** 96 questions
- **Senior:** 171 questions
- **Staff:** 26 questions

## By Category Difficulty
### Fundamentals
- Beginner: 14
- Intermediate: 40
- Advanced: 3

### Kotlin
- Beginner: 9
- Intermediate: 35
- Advanced: 17

### Compose
- Beginner: 4
- Intermediate: 35
- Advanced: 2
- Senior: 17
- Staff: 3

### Concurrency
- Beginner: 5
- Intermediate: 25
- Advanced: 1
- Senior: 26

### Architecture
- Beginner: 5
- Intermediate: 21
- Advanced: 1
- Senior: 24
- Staff: 4

### Networking
- Beginner: 4
- Intermediate: 30
- Advanced: 4

### Security
- Intermediate: 23
- Advanced: 7
- Senior: 6

### Performance
- Beginner: 4
- Intermediate: 23
- Advanced: 13

### Cicd
- Beginner: 10
- Intermediate: 23
- Advanced: 10
- Senior: 10

### Advanced
- Beginner: 4
- Intermediate: 14
- Advanced: 4
- Senior: 9

### Aosp
- Intermediate: 3
- Advanced: 20
- Senior: 9

### Future Tech
- Beginner: 10
- Intermediate: 20
- Advanced: 10
- Senior: 10

### System Design
- Beginner: 2
- Intermediate: 16
- Advanced: 3
- Senior: 23
- Staff: 9

### Testing
- Beginner: 2
- Intermediate: 26
- Senior: 18
- Staff: 4

### Behavioral
- Beginner: 5
- Intermediate: 22
- Advanced: 1
- Senior: 19
- Staff: 6

## Quick Tags Reference
- **android:** 82 questions
- **architecture:** 80 questions
- **kotlin:** 73 questions
- **compose:** 68 questions
- **performance:** 67 questions
- **testing:** 57 questions
- **coroutines:** 55 questions
- **release:** 53 questions
- **system-design:** 53 questions
- **behavioral:** 53 questions
- **cicd:** 52 questions
- **future-tech:** 50 questions
- **innovation:** 50 questions
- **security:** 49 questions
- **networking:** 36 questions
- **aosp:** 33 questions
- **advanced:** 31 questions
- **state:** 26 questions
- **internals:** 25 questions
- **flow:** 25 questions
- **concurrency:** 21 questions
- **lifecycle:** 19 questions
- **optimization:** 18 questions
- **memory:** 16 questions
- **threading:** 15 questions
- **runtime:** 14 questions
- **communication:** 13 questions
- **scalability:** 13 questions
- **debugging:** 12 questions
- **rendering:** 11 questions
---
**Next Step:** Regenerate docs and validate navigation for Fundamentals, Kotlin, Compose, Concurrency, Architecture, Networking, Security, Performance, Cicd, Advanced, Aosp, Future Tech, System Design, Testing, Behavioral sections.
