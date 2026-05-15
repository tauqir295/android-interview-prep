# 📱 Android Interview Prep (2026 Edition)

Welcome to the ultimate preparation guide for Android Developers. This resource is designed to take you from **Junior** to **Senior/Staff** level by covering everything from core fundamentals to complex system design and CI/CD pipelines.

---

## 🚀 Navigation Roadmap

### [📱 Fundamentals](./generated/fundamentals.md)
Master the core building blocks of the Android OS. 
* **Lifecycle:** Deep dives into Activity and Fragment states.
* **Components:** Services, Broadcast Receivers, and Content Providers.
* **Manifest & Context:** Understanding the app's blueprint and memory-safe context usage.

### [🧠 Kotlin](./generated/kotlin.md)
Modern Android is Kotlin-first. We cover language internals and idiomatic usage.
* **Core:** Null safety, Extension functions, and Higher-order functions.
* **Advanced:** Inline functions, Reified types, and Sealed Class hierarchies.
* **Asynchronous:** Coroutines and Flow (StateFlow/SharedFlow).

### [🛠️ Jetpack Compose](./generated/compose.md)
The declarative UI standard for Android.
* **State:** `remember`, `rememberSaveable`, and State Hoisting.
* **Internals:** Recomposition cycles and stability.
* **Effects:** Managing side effects with `LaunchedEffect` and `DisposableEffect`.

### [🏗️ Architecture](./generated/architecture.md)
Design patterns that define professional, scalable apps.
* **Patterns:** MVVM, MVI, and Clean Architecture.
* **DI:** Hilt, Dagger2, and Koin.
* **Scalability:** Modularization strategies and the Repository pattern.

### [⚡ Concurrency](./generated/concurrency.md)
Efficient background processing.
* **Coroutines:** Dispatchers, Scopes, and Structured Concurrency.
* **Flow vs LiveData:** Migration strategies and use cases.
* **Threading:** Handlers, Loopers, and the Main Thread.

### [🌐 Networking & Offline](./generated/networking.md)
Data persistence and API communication.
* **Networking:** Retrofit, OkHttp, and Interceptors.
* **Database:** Room, Migrations, and Relationships.
* **Strategy:** Offline-First Architecture and data synchronization.

### [🔐 App Security](./generated/security.md)
Production-grade Android hardening and abuse prevention.
* **Threat Modeling:** Attack surface mapping and risk prioritization.
* **App Hardening:** Manifest, exported component, and WebView security.
* **Data Protection:** Keystore usage, local encryption, and secret handling.
* **Runtime Defense:** Network security config, integrity signals, and release hardening.

### [🚀 Performance & Vitals](./generated/performance.md)
Building "buttery smooth" experiences.
* **Optimization:** Memory leaks (LeakCanary), ANRs, and App Startup time.
* **Metrics:** Play Console performance tracking and vitals.
* **Debugging:** Profilers, Logcat, and StrictMode.

### [⚙️ CI/CD & Release](./generated/cicd.md)
The "DevOps" of Android.
* **Pipelines:** GitHub Actions and automated workflows.
* **Management:** Release strategies, App Bundles, and Gradual Rollouts.

### [🏗️ System Design](./generated/system-design.md)
Senior-level discussions on building complex systems.
* Designing Image Loaders (Glide/Coil).
* Real-time Chat and Feed systems.
* Analytics and Logging SDKs.

### [🧪 Testing](./generated/testing.md)
Comprehensive testing strategies from unit to system tests.
* **Strategy:** Test pyramid, risk-based testing, and CI/CD integration.
* **Unit & Integration:** ViewModels, repositories, and use cases.
* **UI & E2E:** Compose testing, Espresso, and release gates.
* **Advanced:** Flaky test diagnostics, performance benchmarks, and mutation testing.

### [🎓 Advanced Internals](./generated/advanced.md)
Going deep into the OS.
* **Internals:** AOSP basics and Binder IPC.
* **Form Factors:** Foldables and Tablets.

### [🤖 Future Tech](./generated/future-tech.md)
Emerging technologies shaping Android's future.
* **AI & ML:** On-device inference, edge AI, and federated learning.
* **Form Factors:** Foldables, large screens, wearables, and XR/AR/VR.
* **Platforms:** KMP, ambient computing, and multimodal interfaces.
* **Strategy:** Future-proofing and emerging product experimentation.

### [💬 Behavioral & Soft Skills](./generated/behavioral.md)
Answering the "why you" and "how you work" questions.
* **Interview Prep:** STAR method, story selection, and anti-patterns.
* **Execution:** Ownership, accountability, prioritization, and tradeoffs.
* **Leadership:** Mentorship, conflict resolution, and cross-functional collaboration.
* **At Scale:** Staff-level behavioral signals, ethical decision-making, and impact.

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