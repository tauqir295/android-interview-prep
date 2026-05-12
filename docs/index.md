# 📱 Android Interview Prep (2026 Edition)

Welcome to the ultimate preparation guide for Android Developers. This resource is designed to take you from **Junior** to **Senior/Staff** level by covering everything from core fundamentals to complex system design and CI/CD pipelines.

---

## 🚀 Navigation Roadmap

### [📱 Fundamentals](./fundamentals.md)
Master the core building blocks of the Android OS. 
* **Lifecycle:** Deep dives into Activity and Fragment states.
* **Components:** Services, Broadcast Receivers, and Content Providers.
* **Manifest & Context:** Understanding the app's blueprint and memory-safe context usage.

### [🧠 Kotlin](./kotlin.md)
Modern Android is Kotlin-first. We cover language internals and idiomatic usage.
* **Core:** Null safety, Extension functions, and Higher-order functions.
* **Advanced:** Inline functions, Reified types, and Sealed Class hierarchies.
* **Asynchronous:** Coroutines and Flow (StateFlow/SharedFlow).

### [🛠️ Jetpack Compose](./compose.md)
The declarative UI standard for Android.
* **State:** `remember`, `rememberSaveable`, and State Hoisting.
* **Internals:** Recomposition cycles and stability.
* **Effects:** Managing side effects with `LaunchedEffect` and `DisposableEffect`.

### [🏗️ Architecture](./architecture.md)
Design patterns that define professional, scalable apps.
* **Patterns:** MVVM, MVI, and Clean Architecture.
* **DI:** Hilt, Dagger2, and Koin.
* **Scalability:** Modularization strategies and the Repository pattern.

### [⚡ Concurrency](./concurrency.md)
Efficient background processing.
* **Coroutines:** Dispatchers, Scopes, and Structured Concurrency.
* **Flow vs LiveData:** Migration strategies and use cases.
* **Threading:** Handlers, Loopers, and the Main Thread.

### [🌐 Networking & Offline](./networking-db.md)
Data persistence and API communication.
* **Networking:** Retrofit, OkHttp, and Interceptors.
* **Database:** Room, Migrations, and Relationships.
* **Strategy:** [Offline-First Architecture](./offline-first.md) and data synchronization.

### [🚀 Performance & Vitals](./performance-debug.md)
Building "buttery smooth" experiences.
* **Optimization:** Memory leaks (LeakCanary), ANRs, and App Startup time.
* **Metrics:** [App Vitals](./app-vitals.md) and Play Console performance tracking.
* **Debugging:** Profilers, Logcat, and StrictMode.

### [⚙️ CI/CD & Release](./cicd-pipelines.md)
The "DevOps" of Android.
* **Pipelines:** GitHub Actions and automated workflows.
* **Management:** [Release Strategies](./release-management.md), App Bundles, and Gradual Rollouts.

### [🏗️ System Design](./system-design.md)
Senior-level discussions on building complex systems.
* Designing Image Loaders (Glide/Coil).
* Real-time Chat and Feed systems.
* Analytics and Logging SDKs.

### [🎓 Advanced & Security](./advanced.md)
Going deep into the OS.
* **Internals:** [AOSP basics](./aosp-internals.md) and Binder IPC.
* **Security:** [Keystore, ProGuard, and R8](./security.md).
* **Form Factors:** [Foldables and Tablets](./foldables.md).

---

## 🎯 Goal of This Project
This project aims to create a practical Android interview preparation resource with:
- **Interview-Focused Answers:** Not just documentation, but how to explain it to an interviewer.
- **2026 Standards:** Focused on Compose, KMP, and On-device AI.
- **Real Examples:** Code snippets that actually work in production.

## 🚧 Upcoming Content
- [ ] RecyclerView Performance Deep Dive
- [ ] On-Device AI (Gemini Nano) Integration
- [ ] Staff-Level Behavioral Interview Guide
- [ ] Mock System Design Interviews

---

!!! tip "Contribute"
    This is a public project! If you find a bug or want to add a question, feel free to open a Pull Request.