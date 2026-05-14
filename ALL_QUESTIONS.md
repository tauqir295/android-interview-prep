# Complete Question List - Android Interview Prep
Generated: 481 interview questions across 214 deep dive topics
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

## Concurrency Questions
## Coroutine Internals (4 questions -> 1 deep dive)
156. `structured-concurrency` - What is structured concurrency?
157. `suspend-functions` - What is a suspend function?
158. `continuation-and-cps` - What is a Continuation in Kotlin coroutines?
159. `coroutine-state-machine` - How does coroutine suspension work internally?
## Threads Vs Coroutines (1 questions -> 1 deep dive)
160. `threads-vs-coroutines` - What is the difference between threads and coroutines?
## Threads Dispatchers Context (2 questions -> 1 deep dive)
161. `dispatchers-overview` - What are Dispatchers in Kotlin Coroutines?
162. `withcontext-purpose` - What does `withContext` do and why is it important?
## Structured Scope And Jobs (4 questions -> 1 deep dive)
163. `coroutine-scope` - What is `CoroutineScope` and why does it matter?
164. `job-hierarchy` - How does coroutine job hierarchy work?
165. `supervisorjob` - What is the difference between `Job` and `SupervisorJob`?
166. `supervisorScope` - What does `supervisorScope` do?
## Cancellation Exception Supervision (4 questions -> 1 deep dive)
167. `coroutine-cancellation` - How does coroutine cancellation work?
168. `cooperative-cancellation` - What is cooperative cancellation?
169. `coroutine-exception-handling` - How are exceptions handled in coroutines?
170. `coroutineexceptionhandler` - What is `CoroutineExceptionHandler` used for?
## Launch Async Parallelism (3 questions -> 1 deep dive)
171. `launch-vs-async` - What is the difference between `launch` and `async`?
172. `lazy-async` - What is lazy async?
173. `parallelism-limit` - How do you limit coroutine parallelism?
## Scheduler Thread Pools (2 questions -> 1 deep dive)
174. `thread-pools` - What are coroutine thread pools?
175. `thread-starvation` - What is thread starvation in concurrency?
## Parallelism And Scheduling (1 questions -> 1 deep dive)
176. `limited-parallelism` - What is `limitedParallelism` in coroutines?
## Flow Fundamentals (3 questions -> 1 deep dive)
177. `flow-what-is` - What is Flow in Kotlin?
178. `cold-vs-hot-flow` - What is the difference between cold and hot flows?
179. `backpressure` - What is backpressure in Flow?
## Flow Operators And Backpressure (3 questions -> 1 deep dive)
180. `collectLatest` - When should you use `collectLatest`?
181. `flatMapLatest` - When should you use `flatMapLatest`?
182. `buffering-conflation` - What is buffering and conflation in Flow?
## Stateflow Sharedflow And Channels (2 questions -> 1 deep dive)
183. `stateflow-vs-sharedflow` - What is the difference between StateFlow and SharedFlow?
184. `channels-vs-sharedflow` - When should you use a Channel instead of SharedFlow?
## Flow Sharing And Hot Streams (2 questions -> 1 deep dive)
185. `statein-sharein` - What are `stateIn` and `shareIn` used for?
186. `one-off-events-with-sharedflow` - How do you model one-off events with SharedFlow?
## Callbackflow And Channelflow (3 questions -> 1 deep dive)
187. `callbackflow` - What is `callbackFlow`?
188. `channelflow` - What is `channelFlow`?
189. `flow-callback-interop` - How do you bridge callbacks into Flow safely?
## Synchronization And Mutex (4 questions -> 1 deep dive)
190. `mutex` - What is `Mutex` in Kotlin coroutines?
191. `synchronization-strategies` - What are common synchronization strategies in concurrent code?
192. `shared-mutable-state` - Why is shared mutable state dangerous?
193. `atomic-operations` - What are atomic operations used for?
## Thread Confinement And Race Conditions (3 questions -> 1 deep dive)
194. `thread-confinement` - What is thread confinement?
195. `race-conditions` - What is a race condition?
196. `deadlocks` - What is a deadlock?
## Coroutine Testing And Virtual Time (3 questions -> 1 deep dive)
197. `coroutine-testing` - How do you test coroutines?
198. `virtual-time-testing` - How does virtual time testing work?
199. `test-dispatchers` - Why use test dispatchers for coroutine tests?
## Coroutine Debugging And Observability (2 questions -> 1 deep dive)
200. `coroutine-debugging` - How do you debug coroutines in production?
201. `trace-and-observability` - How should you observe coroutine and Flow behavior?
## Android Lifecycle And Flow Collection (1 questions -> 1 deep dive)
202. `repeatOnLifecycle-flow-collection` - How should Flow be collected with Android lifecycle?
## Android Lifecycle And Main Safety (2 questions -> 1 deep dive)
203. `main-safety` - What does main-safety mean?
204. `anr-and-main-thread` - Why do blocking calls on the main thread cause ANRs?
## Production Concurrency Patterns And Tuning (1 questions -> 1 deep dive)
205. `concurrency-performance-optimization` - How do you optimize concurrency performance in production?

---

## Architecture Questions
## Mvvm And Viewmodel (3 questions -> 1 deep dive)
206. `mvvm-basics` - What is MVVM in Android architecture?
207. `viewmodel-role` - What is the role of a ViewModel in scalable Android apps?
208. `savedstatehandle-usage` - When should you use SavedStateHandle in architecture design?
## Mvi And Udf (3 questions -> 1 deep dive)
209. `mvi-what-is` - What is MVI architecture?
210. `mvi-vs-mvvm` - MVVM vs MVI - how do you choose?
211. `udf-principles` - What are the key principles of Unidirectional Data Flow?
## Clean Architecture Layering (3 questions -> 1 deep dive)
212. `clean-architecture-overview` - What is Clean Architecture in Android?
213. `layer-dependency-rule` - What is the dependency rule in layered architecture?
214. `dependency-inversion-android` - How does dependency inversion apply to Android app architecture?
## Repository Pattern And Data Sources (3 questions -> 1 deep dive)
215. `repository-pattern-purpose` - Why use the Repository pattern?
216. `repository-single-source-truth` - How does a repository support a Single Source of Truth model?
217. `multiple-data-sources-orchestration` - How should repositories orchestrate network, cache, and database sources?
## Use Cases And Domain Layer (3 questions -> 1 deep dive)
218. `use-case-purpose` - What problem do use cases solve in architecture?
219. `use-case-granularity` - How granular should use cases be?
220. `domain-layer-when-to-add` - When is a dedicated domain layer worth adding?
## Dependency Injection Strategies (3 questions -> 1 deep dive)
221. `dependency-injection-what-why` - Why is dependency injection important in Android architecture?
222. `constructor-injection-vs-field-injection` - Constructor injection vs field injection - which is preferred?
223. `di-scope-management` - How do DI scopes affect memory and lifecycle behavior?
## Hilt In Production (2 questions -> 1 deep dive)
224. `hilt-benefits` - What architectural advantages does Hilt provide?
225. `hilt-component-lifetimes` - What Hilt component lifetimes should senior engineers know?
## Dagger And Component Graph (3 questions -> 1 deep dive)
226. `dagger-vs-hilt` - Dagger vs Hilt - what is the architectural tradeoff?
227. `dagger-component-subcomponent` - What should you understand about Dagger components and subcomponents?
228. `dagger-performance-tradeoffs` - What are Dagger/Hilt build and runtime tradeoffs at scale?
## Service Locator And Anti Patterns (2 questions -> 1 deep dive)
229. `service-locator-what-is` - What is a Service Locator pattern?
230. `service-locator-vs-di` - Service Locator vs DI - why does this matter in interviews?
## Modularization Strategies (3 questions -> 1 deep dive)
231. `modularization-why` - Why modularize Android apps?
232. `multi-module-architecture-shapes` - What multi-module structures are common in Android?
233. `api-vs-implementation-modules` - How do API vs implementation module boundaries improve architecture?
## Feature Modules And Boundaries (3 questions -> 1 deep dive)
234. `feature-module-boundaries` - What defines a good feature module boundary?
235. `dynamic-feature-modules-when` - When should you use dynamic feature modules?
236. `dependency-direction-between-modules` - How should dependency direction work between feature modules?
## State Management And Ssot (3 questions -> 1 deep dive)
237. `state-management-android-architecture` - What is a strong state management approach in Android architecture?
238. `single-source-of-truth` - What does Single Source of Truth mean in practice?
239. `immutable-ui-state-models` - Why model UI state as immutable data classes?
## Offline First And Sync (3 questions -> 1 deep dive)
240. `offline-first-principles` - What is offline-first architecture?
241. `sync-strategies-pull-push` - Push, pull, and hybrid sync strategies - when to use each?
242. `conflict-resolution-sync` - How should architecture handle sync conflicts?
## Caching And Pagination Architecture (2 questions -> 1 deep dive)
243. `caching-strategies` - What caching strategies are common in Android architecture?
244. `pagination-architecture` - What does a robust pagination architecture look like?
## Reactive Architecture With Flows (2 questions -> 1 deep dive)
245. `stateflow-architecture` - How does StateFlow fit Android architecture design?
246. `event-handling-one-off-events` - How should one-off events be handled in reactive architecture?
## Ui State And Event Modeling (3 questions -> 1 deep dive)
247. `error-handling-architecture` - What is a good error handling architecture for Android apps?
248. `retry-strategies-architecture` - How do retry strategies fit architecture decisions?
249. `ui-state-modeling-architecture` - How should complex UI state be modeled architecturally?
## Navigation And Deep Link Architecture (2 questions -> 1 deep dive)
250. `navigation-architecture` - What are key principles of navigation architecture?
251. `deep-link-architecture` - How should deep links be designed in modular Android apps?
## Testing Architecture And Testability (1 questions -> 1 deep dive)
252. `architecture-testability` - How do you design Android architecture for high testability?
## Scalability And Team Topologies (1 questions -> 1 deep dive)
253. `scaling-architecture-for-team` - How does architecture impact team scalability?
## Production Tradeoffs And Decision Making (2 questions -> 1 deep dive)
254. `architecture-governance` - What is architecture governance in large Android codebases?
255. `production-architecture-tradeoffs` - How should senior engineers discuss architecture tradeoffs in interviews?

---

## Networking Questions
## Retrofit Fundamentals (2 questions -> 1 deep dive)
256. `retrofit-fundamentals` - What is Retrofit?
257. `coroutines-retrofit` - How does Retrofit work with Kotlin Coroutines?
## Serialization Strategies (2 questions -> 1 deep dive)
258. `retrofit-converters` - How do Retrofit converters work?
259. `json-serialization` - What are differences between Gson, Moshi, and Kotlin Serialization?
## Okhttp Internals (2 questions -> 1 deep dive)
260. `okhttp-interceptors` - What is an OkHttp Interceptor?
261. `okhttp-connection-pooling` - How does OkHttp connection pooling work?
## Rest Api Principles (2 questions -> 1 deep dive)
262. `rest-principles` - What are REST API principles?
263. `http-methods` - When should you use HTTP PUT vs PATCH?
## Authentication Security (2 questions -> 1 deep dive)
264. `authentication` - How should you implement authentication in mobile apps?
265. `https-tls` - What is HTTPS and TLS?
## Certificate Pinning (1 questions -> 1 deep dive)
266. `certificate-pinning` - What is certificate pinning?
## Retry Exponential Backoff (2 questions -> 1 deep dive)
267. `retry-strategies` - How should you implement retry logic?
268. `exponential-backoff` - What is exponential backoff?
## Pagination Architecture (2 questions -> 1 deep dive)
269. `pagination` - How does pagination work in REST APIs?
270. `paging-3` - What is Paging 3 library?
## Caching Strategies (2 questions -> 1 deep dive)
271. `http-caching` - How does HTTP caching work?
272. `etags-conditional` - What are ETags and conditional requests?
## Offline First Architecture (2 questions -> 1 deep dive)
273. `offline-first` - What is offline-first architecture?
274. `sync-engine` - How do you implement a sync engine?
## Conflict Resolution (1 questions -> 1 deep dive)
275. `conflict-resolution` - How should you handle sync conflicts?
## Websockets Streaming (2 questions -> 1 deep dive)
276. `websockets` - What are WebSockets?
277. `streaming-downloads` - How do you handle streaming and large file downloads?
## Error Handling Resilience (2 questions -> 1 deep dive)
278. `network-error-handling` - How should you handle network errors?
279. `resiliency-patterns` - What are network resiliency patterns?
## Compression Optimization (2 questions -> 1 deep dive)
280. `compression` - How does request/response compression work?
281. `battery-optimization` - How do you optimize for battery usage in networking?
## Graphql Advanced (2 questions -> 1 deep dive)
282. `graphql-rest` - What are differences between GraphQL and REST?
283. `grpc-basics` - What is gRPC?
## Network Monitoring Debugging (1 questions -> 1 deep dive)
284. `network-monitoring` - How do you monitor and debug network traffic?
## Rate Limiting Idempotency (3 questions -> 1 deep dive)
285. `rate-limiting` - How do you handle rate limiting?
286. `idempotency` - What is idempotency in APIs?
287. `request-cancellation` - How do you cancel network requests?
## Multipart Uploads (1 questions -> 1 deep dive)
288. `multipart-uploads` - How do you implement multipart file uploads?
## Api Versioning Scalability (2 questions -> 1 deep dive)
289. `api-versioning` - How should you version your APIs?
290. `scalability-cdn` - What is CDN and when to use it?
## Production Networking Patterns (3 questions -> 1 deep dive)
291. `network-security-config` - What is Network Security Configuration?
292. `timeouts` - How should you configure network timeouts?
293. `performance-monitoring` - How do you monitor API performance?

---

## Performance Questions
## Performance Metrics (1 questions -> 1 deep dive)
294. `android-performance-fundamentals` - What are the main performance metrics in Android?
## Jank And Frame Drops (1 questions -> 1 deep dive)
295. `jank-and-ui-drops` - What causes jank and how do you fix it?
## Memory Leaks (1 questions -> 1 deep dive)
296. `memory-leaks` - What is a memory leak and how do you find them?
## Memory Management (3 questions -> 1 deep dive)
297. `garbage-collection` - How does garbage collection work in Android?
298. `memory-pressure` - How do you handle memory pressure?
299. `graphics-memory` - How much memory do graphics consume?
## Battery Optimization (1 questions -> 1 deep dive)
300. `battery-optimization` - How do you optimize battery usage?
## Rendering Pipeline (1 questions -> 1 deep dive)
301. `rendering-pipeline` - What is Android rendering pipeline?
## Rendering Optimization (1 questions -> 1 deep dive)
302. `overdraw` - What is overdraw and how do you detect it?
## App Startup (1 questions -> 1 deep dive)
303. `app-startup-time` - How do you reduce app startup time?
## Memory Profiling (1 questions -> 1 deep dive)
304. `memory-profiling` - How do you profile memory usage?
## Cpu Profiling (1 questions -> 1 deep dive)
305. `cpu-profiling` - How do you profile CPU usage?
## Layout Optimization (1 questions -> 1 deep dive)
306. `layout-inflation` - How does layout inflation work?
## Anr Prevention (1 questions -> 1 deep dive)
307. `anr-prevention` - What causes ANR and how do you prevent it?
## Bitmap Optimization (1 questions -> 1 deep dive)
308. `bitmap-optimization` - How do you optimize bitmap memory usage?
## Database Optimization (1 questions -> 1 deep dive)
309. `database-performance` - How do you optimize database queries?
## Network Optimization (1 questions -> 1 deep dive)
310. `network-performance` - How do you optimize network requests?
## Allocation Optimization (2 questions -> 1 deep dive)
311. `string-formatting` - What's the performance impact of string formatting?
312. `object-pooling` - What is object pooling?
## Reflection Optimization (1 questions -> 1 deep dive)
313. `reflection-performance` - What's the performance cost of reflection?
## Recyclerview Optimization (1 questions -> 1 deep dive)
314. `view-recycling` - How does RecyclerView recycling work?
## Initialization Patterns (1 questions -> 1 deep dive)
315. `lazy-initialization` - What is lazy initialization?
## Profiling Tools (3 questions -> 1 deep dive)
316. `perfetto-tracing` - What is Perfetto and how do you use it?
317. `systrace-analysis` - How do you use systrace?
318. `benchmark-tools` - Differences between profiling tools?
## Frame Stability (1 questions -> 1 deep dive)
319. `frame-rate-stability` - How do you ensure stable frame rates?
## Startup Optimization (1 questions -> 1 deep dive)
320. `cold-start-optimization` - What causes slow cold starts?
## Caching Strategies (1 questions -> 1 deep dive)
321. `warm-cache` - How do you keep a warm cache?
## Compose Performance (1 questions -> 1 deep dive)
322. `composition-performance` - How does Compose performance differ from Views?
## Graphics Optimization (1 questions -> 1 deep dive)
323. `shader-compilation` - What is shader compilation?
## Battery Profiling (1 questions -> 1 deep dive)
324. `power-consumption-profiling` - How do you profile power consumption?
## Monitoring Implementation (1 questions -> 1 deep dive)
325. `custom-performance-monitoring` - How do implement custom monitoring?
## Performance Testing (1 questions -> 1 deep dive)
326. `performance-testing` - How do you write performance tests?
## Ux Perception (1 questions -> 1 deep dive)
327. `responsiveness-perception` - Perceived responsiveness vs actual performance?
## Performance Strategy (1 questions -> 1 deep dive)
328. `performance-budgets` - What is a performance budget?
## Gpu Optimization (1 questions -> 1 deep dive)
329. `gpu-rendering-cost` - What is the cost of GPU rendering?
## System Internals (1 questions -> 1 deep dive)
330. `kernel-linux-performance` - How does Linux kernel impact performance?
## Compilation Optimization (1 questions -> 1 deep dive)
331. `ahead-of-time-compilation` - What is AoT compilation?

---

## System Design Questions
## System Design Fundamentals (2 questions -> 1 deep dive)
332. `system-design` - What is Android system design in interviews?
333. `design-round-structure` - What is a strong structure for solving design rounds?
## Requirements And Scope (2 questions -> 1 deep dive)
334. `functional-vs-nonfunctional-requirements` - How do you separate functional vs non-functional requirements?
335. `scope-definition` - How do you define scope for a system design round?
## Scalability And Capacity Planning (2 questions -> 1 deep dive)
336. `estimations` - How do you do quick capacity estimations?
337. `horizontal-scaling` - How do you scale a system horizontally?
## High Level Architecture (3 questions -> 1 deep dive)
338. `high-level-components` - How do you structure high-level components?
339. `service-boundaries` - How do you define service boundaries?
340. `load-balancing` - How do load balancers fit into architecture design?
## Data Modeling And Storage (2 questions -> 1 deep dive)
341. `data-modeling` - How do you approach data modeling in system design?
342. `sql-vs-nosql` - When do you choose SQL vs NoSQL?
## Search And Indexing (3 questions -> 1 deep dive)
343. `indexing-strategy` - How do indexes affect read and write performance?
344. `search-architecture` - How do you design search for low-latency queries?
345. `eventual-consistency-search` - Why is search often eventually consistent?
## Consistency And Transactions (2 questions -> 1 deep dive)
346. `consistency-models` - What consistency models should you discuss in interviews?
347. `transactions-and-sagas` - When should you use transactions vs sagas?
## Caching Strategies (2 questions -> 1 deep dive)
348. `cache-aside` - What is cache-aside and when is it useful?
349. `cache-invalidation` - Why is cache invalidation hard?
## Queueing And Async Processing (3 questions -> 1 deep dive)
350. `message-queues` - When do you add a message queue?
351. `event-driven-design` - What are event-driven architecture tradeoffs?
352. `backpressure-in-systems` - What is backpressure in distributed systems?
## Api Design And Gateways (4 questions -> 1 deep dive)
353. `api-gateway` - What role does an API gateway play?
354. `rest-vs-grpc-design` - How do you choose REST vs gRPC for internal APIs?
355. `versioning-strategy` - How do you version APIs safely?
356. `rate-limiting` - How do you design rate limiting?
## Security And Compliance (4 questions -> 1 deep dive)
357. `authn-vs-authz` - How do you model authentication vs authorization?
358. `security-hardening` - What security hardening do you mention in interviews?
359. `tenant-isolation` - How do you design multi-tenant isolation?
360. `data-retention` - How do retention policies affect architecture?
## Observability And Slos (2 questions -> 1 deep dive)
361. `slos-and-slas` - How do SLOs/SLAs shape architecture decisions?
362. `logging-metrics-tracing` - Why are logs, metrics, and traces all needed?
## Resilience And Failure Handling (3 questions -> 1 deep dive)
363. `circuit-breaker` - What is a circuit breaker and why use it?
364. `bulkheads-and-timeouts` - How do timeouts, retries, and bulkheads work together?
365. `idempotency` - Why is idempotency important in distributed systems?
## Multi Region And Disaster Recovery (2 questions -> 1 deep dive)
366. `multi-region` - When do you move to multi-region architecture?
367. `disaster-recovery-rpo-rto` - How do RPO and RTO influence disaster recovery design?
## Cost Optimization (2 questions -> 1 deep dive)
368. `cost-vs-latency` - How do you balance cost vs latency?
369. `capacity-headroom` - How much capacity headroom should a production system keep?
## Mobile Backend For Frontend (2 questions -> 1 deep dive)
370. `bff-pattern` - What is Backend-for-Frontend (BFF) and when should Android use it?
371. `edge-caching-mobile` - How does edge caching improve mobile user experience?
## Real Time Systems (2 questions -> 1 deep dive)
372. `realtime-chat-design` - How would you design a real-time chat backend?
373. `fanout-problem` - How do you handle fan-out at scale?
## Analytics Pipeline Design (2 questions -> 1 deep dive)
374. `analytics-pipeline` - How do you design analytics ingestion pipelines?
375. `batch-vs-stream` - When do you choose batch vs stream processing?
## Migration And Evolution Strategies (2 questions -> 1 deep dive)
376. `migration-strangler` - What is the strangler pattern for migrations?
377. `schema-evolution` - How do you manage schema evolution safely?
## Tradeoffs And Decision Frameworks (4 questions -> 1 deep dive)
378. `tradeoff-framework` - How do you present tradeoffs clearly in interviews?
379. `cap-theorem-practical` - How do you explain CAP theorem pragmatically?
380. `read-heavy-vs-write-heavy` - How does workload shape architecture choices?
381. `availability-vs-consistency` - How do you choose availability vs consistency?

---

## Testing Questions
## Testing Fundamentals (2 questions -> 1 deep dive)
382. `testing-strategy` - How do you define an Android testing strategy?
383. `qa-dev-collaboration` - How should QA and dev collaborate on automation?
## Test Pyramid And Strategy (4 questions -> 1 deep dive)
384. `test-pyramid` - What is the test pyramid and why does it matter?
385. `unit-vs-integration` - What is the difference between unit and integration tests?
386. `hermetic-tests` - What are hermetic tests and why are they valuable?
387. `risk-based-testing` - What is risk-based testing?
## Unit Testing Viewmodel (3 questions -> 1 deep dive)
388. `viewmodel-unit-tests` - How do you unit test a ViewModel?
389. `usecase-tests` - How should use cases be tested?
390. `clock-abstraction` - How does clock abstraction improve test reliability?
## Repository And Data Layer Testing (2 questions -> 1 deep dive)
391. `repository-tests` - How do you test repository logic with multiple data sources?
392. `datasource-tests` - How do you test remote and local data sources?
## Integration Testing (1 questions -> 1 deep dive)
393. `integration-boundary` - When should you add integration tests?
## Ui Testing With Compose (2 questions -> 1 deep dive)
394. `compose-ui-tests` - How do Compose UI tests differ from View UI tests?
395. `semantics-testing` - Why are semantics important in Compose tests?
## Espresso And Ui Automation (3 questions -> 1 deep dive)
396. `espresso-basics` - When do you still use Espresso?
397. `idling-resources` - What are idling resources and when are they needed?
398. `android-test-runner` - How do you structure instrumentation test modules?
## Mocking Fakes And Stubs (3 questions -> 1 deep dive)
399. `mocks-vs-fakes` - When should you use mocks vs fakes?
400. `stub-vs-spy` - What is the difference between stubs and spies?
401. `test-data-builders` - Why use test data builders?
## Coroutine And Flow Testing (3 questions -> 1 deep dive)
402. `coroutine-test` - How do you test coroutines deterministically?
403. `virtual-time` - Why is virtual time important for async tests?
404. `flow-test-patterns` - How do you test Flow emissions?
## Stateflow Sharedflow Testing (2 questions -> 1 deep dive)
405. `stateflow-testing` - How do you test StateFlow UI state?
406. `sharedflow-events-testing` - How do you test one-off SharedFlow events?
## Network Testing And Mockwebserver (1 questions -> 1 deep dive)
407. `mockwebserver` - Why use MockWebServer for networking tests?
## Contract Testing (3 questions -> 1 deep dive)
408. `api-contract-tests` - How do you keep API tests resilient to server changes?
409. `consumer-contract` - What is consumer-driven contract testing?
410. `contract-mocks` - How do contracts reduce mock drift?
## Database Testing Room (2 questions -> 1 deep dive)
411. `room-inmemory-tests` - How do you test Room with in-memory databases?
412. `migration-tests` - Why are Room migration tests critical?
## Testability And Architecture (3 questions -> 1 deep dive)
413. `testable-architecture` - What makes Android architecture testable?
414. `dependency-injection-testing` - How does DI improve testability?
415. `test-maintenance-cost` - How do you manage long-term test maintenance cost?
## Flaky Test Diagnostics (3 questions -> 1 deep dive)
416. `flaky-tests` - What causes flaky tests?
417. `stabilize-ui-tests` - How do you stabilize flaky UI tests?
418. `retry-in-tests` - Should flaky tests be fixed with retries?
## Performance And Benchmark Testing (2 questions -> 1 deep dive)
419. `benchmark-tests` - When should you add benchmark tests?
420. `macrobenchmark` - What does Macrobenchmark validate?
## Snapshot And Golden Testing (2 questions -> 1 deep dive)
421. `golden-tests` - What are snapshot or golden tests?
422. `visual-regression` - How do visual regression tests fit release safety?
## E2E Testing And Release Gates (2 questions -> 1 deep dive)
423. `e2e-tests` - What are good use cases for end-to-end tests?
424. `release-gates` - How should tests gate production releases?
## Ci Cd Test Pipelines (3 questions -> 1 deep dive)
425. `ci-pipeline` - How do you design a fast CI test pipeline?
426. `sharding-tests` - When should you shard test suites?
427. `test-environments` - How do you manage test environments across teams?
## Test Metrics And Quality Governance (4 questions -> 1 deep dive)
428. `test-reporting` - What metrics should test reports include?
429. `quality-gates` - How do quality gates prevent regressions?
430. `mutation-testing` - Where does mutation testing fit in Android?
431. `postmortem-regression-tests` - How do you turn incidents into regression tests?

---

## Behavioral Questions
## Behavioral Fundamentals (1 questions -> 1 deep dive)
432. `behavioral-interviews` - What do interviewers evaluate in behavioral rounds?
## Interview Story Frameworks (2 questions -> 1 deep dive)
433. `star-method` - How should you use STAR effectively?
434. `story-selection` - How do you select strong interview stories quickly?
## Ownership And Accountability (2 questions -> 1 deep dive)
435. `ownership-example` - How do you present a strong ownership story?
436. `accountability-vs-ownership` - What is the difference between accountability and ownership?
## Conflict Resolution (2 questions -> 1 deep dive)
437. `handling-conflict` - How do you discuss conflict with a teammate?
438. `disagree-and-commit` - How do you answer "tell me about a disagreement"?
## Stakeholder Management (2 questions -> 1 deep dive)
439. `stakeholder-alignment` - How do you align engineering and product stakeholders?
440. `influence-roadmap` - How do you influence roadmap decisions?
## Prioritization And Tradeoffs (3 questions -> 1 deep dive)
441. `tradeoff-prioritization` - How do you prioritize under tight deadlines?
442. `saying-no` - How do you say no to low-impact requests?
443. `tradeoff-communication` - How do you communicate tradeoffs to non-technical stakeholders?
## Mentorship And Team Growth (3 questions -> 1 deep dive)
444. `mentoring-juniors` - How do you describe mentoring junior engineers?
445. `growing-senior-engineers` - How do you grow senior engineers on your team?
446. `dealing-with-low-performer` - How do you support a struggling teammate?
## Leadership Without Authority (2 questions -> 1 deep dive)
447. `lead-without-authority` - How do you lead without formal authority?
448. `driving-adoption` - How do you drive adoption of technical standards?
## Incident Management And Postmortems (3 questions -> 1 deep dive)
449. `incident-response-story` - How do you explain your role during a production incident?
450. `blameless-postmortem` - What makes a postmortem blameless and actionable?
451. `production-accountability` - How do you show accountability after production issues?
## Delivery And Execution (2 questions -> 1 deep dive)
452. `execution-under-pressure` - How do you deliver under pressure without burnout?
453. `missed-deadline` - How do you answer questions about missing deadlines?
## Decision Making Under Ambiguity (3 questions -> 1 deep dive)
454. `ambiguity` - How do you make decisions under ambiguity?
455. `insufficient-data-decisions` - How do you decide with incomplete data?
456. `unpopular-decision` - How do you defend an unpopular decision?
## Feedback Culture (3 questions -> 1 deep dive)
457. `giving-feedback` - How do you give difficult feedback?
458. `receiving-feedback` - How do you respond to critical feedback?
459. `upward-feedback` - How do you give respectful upward feedback?
## Cross Functional Collaboration (3 questions -> 1 deep dive)
460. `cross-functional-collab` - How do you collaborate with design and QA?
461. `product-engineering-partnership` - How do you build trust with product managers?
462. `partner-with-ops` - How do you partner with SRE/ops teams effectively?
## Career Growth And Self Reflection (3 questions -> 1 deep dive)
463. `career-growth-plan` - How do you discuss your growth plan?
464. `failure-story` - How do you tell a failure story well?
465. `self-awareness` - How do you demonstrate self-awareness in interviews?
## Managing Up (3 questions -> 1 deep dive)
466. `manage-up` - How do you manage up effectively?
467. `escalation` - When and how should you escalate issues?
468. `expectation-alignment-manager` - How do you align expectations with your manager?
## Staff Level Behavioral Signals (3 questions -> 1 deep dive)
469. `staff-scope` - What behavioral signals are expected at staff level?
470. `org-impact` - How do you show organization-level impact?
471. `staff-cross-team-conflict` - How do staff engineers resolve cross-team conflict?
## Ethical Decision Making (3 questions -> 1 deep dive)
472. `ethical-tradeoff` - How do you handle ethical tradeoffs in product decisions?
473. `privacy-vs-growth` - How do you discuss privacy vs growth tension?
474. `ethical-escalation` - When should ethical concerns be escalated?
## Remote And Distributed Teams (3 questions -> 1 deep dive)
475. `remote-collaboration` - How do you maintain alignment in remote teams?
476. `async-communication` - What does strong async communication look like?
477. `remote-trust-building` - How do you build trust in distributed teams?
## Behavioral Anti Patterns (2 questions -> 1 deep dive)
478. `behavioral-red-flags` - What behavioral anti-patterns hurt candidates?
479. `blame-language` - Why is blame language risky in interviews?
## Communication And Clarity (2 questions -> 1 deep dive)
480. `clarity-structure` - How do you keep answers concise and structured?
481. `executive-summary` - How do you open answers with an executive summary?

---
## Statistics
- **Total Questions:** 481
- **Total Deep Dives:** 214
- **Fundamentals:** 54 questions
- **Kotlin:** 51 questions
- **Compose:** 50 questions
- **Concurrency:** 50 questions
- **Architecture:** 50 questions
- **Networking:** 38 questions
- **Performance:** 38 questions
- **System Design:** 50 questions
- **Testing:** 50 questions
- **Behavioral:** 50 questions
- **Beginner:** 54 questions
- **Intermediate:** 240 questions
- **Advanced:** 34 questions
- **Senior:** 127 questions
- **Staff:** 26 questions

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

### Concurrency
- Beginner: 5
- Intermediate: 19
- Senior: 26

### Architecture
- Beginner: 5
- Intermediate: 17
- Senior: 24
- Staff: 4

### Networking
- Beginner: 4
- Intermediate: 30
- Advanced: 4

### Performance
- Beginner: 4
- Intermediate: 21
- Advanced: 13

### System Design
- Beginner: 2
- Intermediate: 16
- Senior: 23
- Staff: 9

### Testing
- Beginner: 2
- Intermediate: 26
- Senior: 18
- Staff: 4

### Behavioral
- Beginner: 5
- Intermediate: 20
- Senior: 19
- Staff: 6

## Quick Tags Reference
- **architecture:** 75 questions
- **android:** 67 questions
- **testing:** 57 questions
- **kotlin:** 56 questions
- **compose:** 53 questions
- **performance:** 52 questions
- **system-design:** 50 questions
- **behavioral:** 50 questions
- **coroutines:** 47 questions
- **networking:** 34 questions
- **state:** 23 questions
- **flow:** 21 questions
- **concurrency:** 19 questions
- **optimization:** 18 questions
- **lifecycle:** 17 questions
- **threading:** 14 questions
- **runtime:** 14 questions
- **communication:** 13 questions
- **memory:** 13 questions
- **scalability:** 13 questions
- **security:** 9 questions
- **compiler:** 9 questions
- **resilience:** 9 questions
- **rendering:** 8 questions
- **ui:** 8 questions
- **di:** 8 questions
- **data:** 7 questions
- **api:** 7 questions
- **recomposition:** 7 questions
- **events:** 7 questions
---
**Next Step:** Regenerate docs and validate navigation for Fundamentals, Kotlin, Compose, Concurrency, Architecture, Networking, Performance, System Design, Testing, Behavioral sections.
