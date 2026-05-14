# Deep Dive Mapping & Architecture

## Overview

This document maps all fundamentals questions to their corresponding deep dives. The design ensures question answer concise while detailed content lives in dedicated markdown files.

---

## Deep Dive Files to Create

### 1. Activity Lifecycle
**File:** `docs/deep-dives/fundamentals/activity-lifecycle.md`

**Questions pointing to this deep dive (6):**
- `activity-lifecycle-overview`: What is the Activity Lifecycle?
- `onstart-vs-onresume`: What's the difference between onStart() and onResume()?
- `onsaved-instance-state`: What is savedInstanceState and when is it called?
- `onconfig-change`: What happens during configuration changes (rotation)?
- `process-death-handling`: How does Android handle process death?
- `lifecycle-callbacks-order`: What is the exact order of lifecycle callbacks?

**Recommended Sections:**
- Overview
- Core Lifecycle Methods (detailed breakdown)
- Lifecycle Transitions (all scenarios)
- savedInstanceState Flow
- Configuration Changes Deep Dive
- Process Death & Recovery
- Multi-App Scenarios
- Advanced: Thread Safety & Timing
- Production Patterns: Lifecycle awareness
- Interview Questions & Traps

---

### 2. Intents
**File:** `docs/deep-dives/fundamentals/intents.md`

**Questions pointing to this deep dive (5):**
- `intent-explicit-implicit`: What's the difference between explicit and implicit intents?
- `intent-filters`: How do intent filters work?
- `intent-resolution`: How does intent resolution work?
- `intent-flags`: What are common intent flags and their purposes?
- `pending-intent`: What is a PendingIntent and when should you use it?

**Recommended Sections:**
- Intent Internals
- Explicit vs Implicit (detailed architecture)
- Intent Resolution Flow (step-by-step)
- Intent Filters (manifest parsing)
- Common Flags (all combinations)
- PendingIntent Internals
- Cross-App Communication
- Intent Matching Algorithm
- Security Considerations
- Interview Traps (e.g., ACTION_SEND vs ACTION_SEND_MULTIPLE)

---

### 3. Fragments
**File:** `docs/deep-dives/fundamentals/fragments.md`

**Questions pointing to this deep dive (5):**
- `fragment-lifecycle`: What is the Fragment lifecycle?
- `fragment-vs-activity`: What are the differences between Fragments and Activities?
- `fragment-communication`: How do fragments communicate with each other?
- `fragment-back-stack`: How does fragment back stack work?
- `fragment-arguments`: What's the best way to pass data to a Fragment?

**Recommended Sections:**
- Fragment Lifecycle (detailed callbacks)
- Lifecycle vs Activity (comparison)
- Fragment State Persistence
- Communication Patterns (all approaches)
- Back Stack Management
- Fragment Manager Internals
- Retained Fragments
- Fragment Factory Pattern
- Common Pitfalls (arguments reconstruction)
- Production Patterns: Master-Detail, Tabbed UI

---

### 4. Context
**File:** `docs/deep-dives/fundamentals/context.md`

**Questions pointing to this deep dive (4):**
- `context-what-is`: What is Context and what are its types?
- `context-memory-leaks`: How can Context cause memory leaks?
- `application-context-vs-activity-context`: When should you use Application Context vs Activity Context?
- `context-lifecycle-awareness`: Why is it important to match Context lifetime with usage?

**Recommended Sections:**
- Context Architecture & Types
- Context Hierarchy
- Application Context (single instance, lifecycle)
- Activity Context (tied to Activity)
- Memory Leak Mechanisms
- ServiceContext, BroadcastReceiverContext
- Context Operations (createPackageContext, etc)
- Best Practices Matrix
- Debugging Context Issues
- Senior-Level: Custom Context Wrapper

---

### 5. Memory Leaks
**File:** `docs/deep-dives/fundamentals/memory-leaks.md`

**Questions pointing to this deep dive (4):**
- `memory-leak-what-is`: What is a memory leak in Android?
- `memory-detection`: How do you detect memory leaks?
- `common-leak-patterns`: What are common memory leak patterns in Android?
- `memory-leak-fixes`: What are best practices to prevent memory leaks?

**Recommended Sections:**
- Memory Management Basics
- Garbage Collector Internals
- Leak Mechanisms (GC roots, reference chains)
- Detection Tools (LeakCanary, Profiler, Logcat)
- Common Patterns (Static refs, Inner classes, Listeners, Handlers)
- Prevention Strategies
- WeakReference vs SoftReference
- Debugging Heap Dumps
- Production Monitoring
- Code Examples: Before & After

---

### 6. ANR & Performance
**File:** `docs/deep-dives/fundamentals/anr-and-performance.md`

**Questions pointing to this deep dive (4):**
- `anr-what-is`: What is an ANR (Application Not Responding)?
- `preventing-anr`: How do you prevent ANRs?
- `main-thread-vs-background`: Why shouldn't you do network/I/O on main thread?
- `jank-dropped-frames`: What's jank and how do you measure it?

**Recommended Sections:**
- Main Thread Responsibilities
- ANR Thresholds (Activity vs Service vs Broadcast)
- ANR Triggers & Prevention
- Threading Models (Thread, Runnable, Coroutines)
- Rendering Pipeline (60fps/120fps)
- Jank Root Causes
- Profiling Tools (GPU Rendering, Profiler, FrameMetrics)
- Frame Budget (16.67ms per frame)
- Performance Monitoring
- Production Optimization: Lazy loading, Prefetching

---

### 7. Looper & Handler
**File:** `docs/deep-dives/fundamentals/looper-and-handler.md`

**Questions pointing to this deep dive (4):**
- `looper-what-is`: What is Looper and how does it work?
- `handler-what-is`: What is Handler and how does it relate to Looper?
- `handler-thread`: What is HandlerThread and when should you use it?
- `handler-memory-leak`: How can Handler cause memory leaks?

**Recommended Sections:**
- Thread Message Queue Architecture
- Looper Implementation (message processing, blocking)
- Handler Architecture (thread-safety, dispatching)
- HandlerThread (simplified Looper setup)
- Message Types (Runnable vs Message)
- Delayed Messages & Timing
- Handler Memory Leaks (reference chains)
- Weak References in Handlers
- Coroutines Alternative
- Production Patterns: Custom Handlers

---

### 8. Services
**File:** `docs/deep-dives/fundamentals/services.md`

**Questions pointing to this deep dive (4):**
- `service-what-is`: What is a Service in Android?
- `service-vs-thread`: What's the difference between Service and Thread?
- `bound-service`: What is a bound service and how do you use it?
- `intent-service`: What is IntentService and when should you use it?

**Recommended Sections:**
- Service Lifecycle
- Started Services (startService, stopService)
- Bound Services (bindService, AIDL)
- Foreground Services (notifications, requirements)
- Service vs Thread (process priority, longevity)
- LocalService Pattern (in-process IPC)
- Binder Deep Dive (for bound services)
- Background Execution Restrictions (Android 8.0+)
- WorkManager (modern alternative)
- Production Patterns: Music player, Sync service

---

### 9. Broadcast Receivers
**File:** `docs/deep-dives/fundamentals/broadcast-receivers.md`

**Questions pointing to this deep dive (3):**
- `broadcast-receiver`: What is a Broadcast Receiver?
- `broadcast-permissions`: How do you register broadcast receivers securely?
- `ordered-vs-sticky-broadcast`: What are ordered and sticky broadcasts?

**Recommended Sections:**
- Broadcast Architecture
- Static vs Dynamic Registration
- Intent Filtering for Broadcasts
- System Broadcasts (common ones)
- Broadcast Lifecycle (onReceive timing)
- Ordered Broadcasts (priority, abort)
- Security: Permissions, exported receivers
- Battery Optimization (Android 8.0+ restrictions)
- LocalBroadcastManager (deprecated, why)
- EventBus as Alternative

---

### 10. Permissions
**File:** `docs/deep-dives/fundamentals/permissions.md`

**Questions pointing to this deep dive (3):**
- `permissions-model`: What is the Android permission model?
- `runtime-permissions`: How do you implement runtime permissions?
- `permission-groups`: What are permission groups and how do they work?

**Recommended Sections:**
- Permission Model Evolution (Pre-M vs M+)
- Permission Categories (Normal, Dangerous, Signature, Custom)
- Runtime Permissions Flow
- Permission Groups & Behavior
- Manifest Declaration
- Requesting Permissions (ActivityCompat vs Activity Result)
- Handling Denials Gracefully
- Scoped Storage (Android 10+)
- Privacy Considerations
- Best Practices: Ask When Used, Explain Why

---

### 11. AndroidManifest
**File:** `docs/deep-dives/fundamentals/androidmanifest.md`

**Questions pointing to this deep dive (2):**
- `manifest-what-is`: What is AndroidManifest.xml and what does it contain?
- `manifest-intent-filters`: How do you declare intent filters in manifest?

**Recommended Sections:**
- Manifest Structure & Sections
- Component Declarations
- Permission Declarations
- Intent Filters Deep Dive
- Feature Declarations
- Application Attributes (debuggable, hardwareAccelerated, etc)
- Manifest Merging (build system)
- APK Deep Links
- Backup Agent Declaration
- Version Management

---

### 12. Binder IPC
**File:** `docs/deep-dives/fundamentals/binder-ipc.md`

**Questions pointing to this deep dive (1):**
- `binder-ipc`: What is Binder and how does IPC work in Android?

**Recommended Sections:**
- Binder Architecture (kernel driver)
- IPC Mechanism (parcel, data marshalling)
- Service Manager
- AIDL (Android Interface Definition Language)
- Binder Thread Pool
- Reference Counting
- Transaction Protocol
- Performance Characteristics
- Security (uid/pid tracking)
- System Services (LocationManager example)

---

### 13. Zygote Process Creation
**File:** `docs/deep-dives/fundamentals/zygote-process-creation.md`

**Questions pointing to this deep dive (1):**
- `zygote-process-creation`: What is Zygote and how does it create app processes?

**Recommended Sections:**
- Zygote Purpose & Design
- Process Forking (Copy-on-Write)
- Framework Preloading
- Application Thread
- App Process Initialization
- Zygote64 vs Zygote32
- Multiple Zygotes (Android 12+)
- Sandbox Isolation
- Security Model

---

### 14. ART vs Dalvik
**File:** `docs/deep-dives/fundamentals/art-vs-dalvik.md`

**Questions pointing to this deep dive (1):**
- `art-vs-dalvik`: What is the difference between ART and Dalvik?

**Recommended Sections:**
- Dalvik Runtime (JIT compilation)
- ART Runtime (AOT compilation)
- Compilation strategies
- Performance Characteristics
- Memory Usage Patterns
- Battery Impact
- Hybrid Compilation (modern Android)
- Implications for App Development
- Debugging Differences
- Migration from Dalvik

---

### 15. App Startup Flow
**File:** `docs/deep-dives/fundamentals/app-startup-flow.md`

**Questions pointing to this deep dive (1):**
- `app-startup-flow`: What happens when you launch an app?

**Recommended Sections:**
- Cold/Warm/Hot Start Definitions
- Complete Startup Sequence
- Application.onCreate() Role
- Activity Initialization
- Layout Inflation & Measurement
- First Frame Rendering
- Startup Time Metrics (Perfetto, traces)
- Optimization Strategies
- Startup Profiler Usage
- Splash Screens & Perceived Performance

---

### 16. RecyclerView Efficiency
**File:** `docs/deep-dives/fundamentals/recyclerview-efficiency.md`

**Questions pointing to this deep dive (1):**
- `recyclerview-efficiency`: Why is RecyclerView more efficient than ListView?

**Recommended Sections:**
- ListView Architecture & Limitations
- RecyclerView Architecture
- View Recycling Mechanism
- ViewHolder Pattern
- RecyclePool Implementation
- LayoutManager Role
- ItemAnimator
- DiffUtil for Efficient Updates
- Performance Optimization Techniques
- Common Mistakes & Fixes

---

### 17. Rendering Pipeline
**File:** `docs/deep-dives/fundamentals/rendering-pipeline.md`

**Questions pointing to this deep dive (1):**
- `rendering-pipeline`: How does Android render UI frames?

**Recommended Sections:**
- Frame Rendering Stages (Measure, Layout, Draw)
- View Tree Traversal
- Hardware Acceleration
- Canvas & RenderThread
- Vsync Synchronization
- Frame Timing Budget
- Overdraw & Optimization
- Layer Types & Implications
- GPU Profiling Tools
- Compose Rendering (alternative)

---

### 18. Storage Types
**File:** `docs/deep-dives/fundamentals/storage-types.md`

**Questions pointing to this deep dive (1):**
- `storage-types`: What are the different storage options in Android?

**Recommended Sections:**
- SharedPreferences (encryption, thread-safety)
- Internal Storage (security model)
- External Storage & Scoped Storage
- SQLite Databases (Room framework)
- Content Providers (interface, URI structure)
- FileProvider (secure file sharing)
- Cache Directories
- Backup & Restore
- Data Security Best Practices

---

### 19. Task & Back Stack
**File:** `docs/deep-dives/fundamentals/task-and-backstack.md`

**Questions pointing to this deep dive (1):**
- `task-and-backstack`: What is a Task and back stack in Android?

**Recommended Sections:**
- Task Concept & Lifecycle
- Back Stack LIFO Structure
- Task ID & Affinity
- Activities Across Apps in Tasks
- Intent Flags (NEW_TASK, CLEAR_TOP, SINGLE_TOP)
- Navigation Component Integration
- Recents Screen Management
- Deep Links & Task Stack
- Handling Deep Links Correctly

---

### 20. Process Death & Lifecycle
**File:** `docs/deep-dives/fundamentals/process-death-lifecycle.md`

**Questions pointing to this deep dive (1):**
- `process-death-lifecycle`: What happens to app state when process is killed?

**Recommended Sections:**
- Process Lifecycle in Android
- Low Memory Killer (LMK) Behavior
- savedInstanceState Timing
- State Preservation Strategies
- ViewModel Scoping
- Room Database Persistence
- SharedPreferences Atomicity
- Process Death Recovery
- Testing Process Death
- Crash vs Kill Difference

---

### 21. Multitasking & Window Focus
**File:** `docs/deep-dives/fundamentals/multitasking-window-focus.md`

**Questions pointing to this deep dive (1):**
- `multitasking-window-focus`: How does multitasking affect activity lifecycle?

**Recommended Sections:**
- Split Screen Multitasking
- Picture-in-Picture (PiP)
- App Switching Behavior
- Focus & Lifecycle Interaction
- Foreground vs Background
- Window Manager Role
- Multi-Window Layout
- Lifecycle During Transitions
- State Preservation in Multitasking
- PiP Implementation Example

---

## Question Distribution Summary

| Topic | Questions | Shared Questions % |
|-------|-----------|-------------------|
| Activity Lifecycle | 6 | 1 deep dive |
| Intents | 5 | 1 deep dive |
| Fragments | 5 | 1 deep dive |
| Context | 4 | 1 deep dive |
| Memory Leaks | 4 | 1 deep dive |
| ANR & Performance | 4 | 1 deep dive |
| Looper & Handler | 4 | 1 deep dive |
| Services | 4 | 1 deep dive |
| Broadcast Receivers | 3 | 1 deep dive |
| Permissions | 3 | 1 deep dive |
| AndroidManifest | 2 | 1 deep dive |
| Binder IPC | 1 | 1 deep dive |
| Zygote | 1 | 1 deep dive |
| ART vs Dalvik | 1 | 1 deep dive |
| App Startup | 1 | 1 deep dive |
| RecyclerView | 1 | 1 deep dive |
| Rendering | 1 | 1 deep dive |
| Storage | 1 | 1 deep dive |
| Task & Back Stack | 1 | 1 deep dive |
| Process Death | 1 | 1 deep dive |
| Multitasking | 1 | 1 deep dive |
| **TOTAL** | **54** | **21 deep dives** |

---

## Design Principles Used

✅ **Concise YAML Answers**
- All answers ~20-25 lines maximum
- Bullet points for quick scanning
- Interview-ready format

✅ **Shared Deep Dives**
- Multiple questions → single deep dive
- Avoids concept duplication
- Scalable architecture

✅ **Progressive Difficulty**
- **Beginner** (16): Basic concepts
- **Intermediate** (28): Practical applications
- **Advanced** (6): Internals & edge cases

✅ **Tag Organization**
- Functional grouping: android, lifecycle, threading, etc
- Enables filtering by topic
- Cross-references for discovery

✅ **Interview Focus**
- Real questions asked in Android interviews
- Covers both breadth and depth
- Includes common traps & edge cases

---

## Next Steps

1. ✅ Generate `fundamentals.yaml` (DONE)
2. ⏳ Create 21 deep dive markdown files
3. ⏳ Generate `docs/generated/fundamentals.md` from YAML
4. ⏳ Test generation script
5. ⏳ Validate deep dive links

---

## File Structure

```
docs/deep-dives/fundamentals/
├── activity-lifecycle.md
├── intents.md
├── fragments.md
├── context.md
├── memory-leaks.md
├── anr-and-performance.md
├── looper-and-handler.md
├── services.md
├── broadcast-receivers.md
├── permissions.md
├── androidmanifest.md
├── binder-ipc.md
├── zygote-process-creation.md
├── art-vs-dalvik.md
├── app-startup-flow.md
├── recyclerview-efficiency.md
├── rendering-pipeline.md
├── storage-types.md
├── task-and-backstack.md
├── process-death-lifecycle.md
└── multitasking-window-focus.md
```

---

## Notes

- All deep dive URLs in YAML follow format: `/docs/deep-dives/fundamentals/{topic}.md`
- Deep dives should be comprehensive yet focused (2000-4000 words ideal)
- Each deep dive starts with overview section for quick reading
- Code examples should be in Kotlin when possible
- Diagrams recommended for complex concepts (Mermaid format)
- Senior-level sections for interview discussions


