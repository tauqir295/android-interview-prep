# Complete Question List - Android Fundamentals
Generated: 54 interview questions across 21 deep dive topics
---
## Activity Lifecycle (6 questions → 1 deep dive)
1. `activity-lifecycle-overview` - What is the Activity Lifecycle?
2. `onstart-vs-onresume` - What's the difference between onStart() and onResume()?
3. `onsaved-instance-state` - What is savedInstanceState and when is it called?
4. `onconfig-change` - What happens during configuration changes (rotation)?
5. `process-death-handling` - How does Android handle process death?
6. `lifecycle-callbacks-order` - What is the exact order of lifecycle callbacks?
## Intents (5 questions → 1 deep dive)
7. `intent-explicit-implicit` - What's the difference between explicit and implicit intents?
8. `intent-filters` - How do intent filters work?
9. `intent-resolution` - How does intent resolution work?
10. `intent-flags` - What are common intent flags and their purposes?
11. `pending-intent` - What is a PendingIntent and when should you use it?
## Fragments (5 questions → 1 deep dive)
12. `fragment-lifecycle` - What is the Fragment lifecycle?
13. `fragment-vs-activity` - What are the differences between Fragments and Activities?
14. `fragment-communication` - How do fragments communicate with each other?
15. `fragment-back-stack` - How does fragment back stack work?
16. `fragment-arguments` - What's the best way to pass data to a Fragment?
## Context (4 questions → 1 deep dive)
17. `context-what-is` - What is Context and what are its types?
18. `context-memory-leaks` - How can Context cause memory leaks?
19. `application-context-vs-activity-context` - When should you use Application Context vs Activity Context?
20. `context-lifecycle-awareness` - Why is it important to match Context lifetime with usage?
## Memory Leaks (4 questions → 1 deep dive)
21. `memory-leak-what-is` - What is a memory leak in Android?
22. `memory-detection` - How do you detect memory leaks?
23. `common-leak-patterns` - What are common memory leak patterns in Android?
24. `memory-leak-fixes` - What are best practices to prevent memory leaks?
## ANR & Performance (4 questions → 1 deep dive)
25. `anr-what-is` - What is an ANR (Application Not Responding)?
26. `preventing-anr` - How do you prevent ANRs?
27. `main-thread-vs-background` - Why shouldn't you do network/I/O on main thread?
28. `jank-dropped-frames` - What's jank and how do you measure it?
## Looper & Handler (4 questions → 1 deep dive)
29. `looper-what-is` - What is Looper and how does it work?
30. `handler-what-is` - What is Handler and how does it relate to Looper?
31. `handler-thread` - What is HandlerThread and when should you use it?
32. `handler-memory-leak` - How can Handler cause memory leaks?
## Services (4 questions → 1 deep dive)
33. `service-what-is` - What is a Service in Android?
34. `service-vs-thread` - What's the difference between Service and Thread?
35. `bound-service` - What is a bound service and how do you use it?
36. `intent-service` - What is IntentService and when should you use it?
## Broadcast Receivers (3 questions → 1 deep dive)
37. `broadcast-receiver` - What is a Broadcast Receiver?
38. `broadcast-permissions` - How do you register broadcast receivers securely?
39. `ordered-vs-sticky-broadcast` - What are ordered and sticky broadcasts?
## Permissions (3 questions → 1 deep dive)
40. `permissions-model` - What is the Android permission model?
41. `runtime-permissions` - How do you implement runtime permissions?
42. `permission-groups` - What are permission groups and how do they work?
## AndroidManifest (2 questions → 1 deep dive)
43. `manifest-what-is` - What is AndroidManifest.xml and what does it contain?
44. `manifest-intent-filters` - How do you declare intent filters in manifest?
## Binder IPC (1 question → 1 deep dive)
45. `binder-ipc` - What is Binder and how does IPC work in Android?
## Zygote (1 question → 1 deep dive)
46. `zygote-process-creation` - What is Zygote and how does it create app processes?
## ART vs Dalvik (1 question → 1 deep dive)
47. `art-vs-dalvik` - What is the difference between ART and Dalvik?
## App Startup (1 question → 1 deep dive)
48. `app-startup-flow` - What happens when you launch an app?
## RecyclerView (1 question → 1 deep dive)
49. `recyclerview-efficiency` - Why is RecyclerView more efficient than ListView?
## Rendering Pipeline (1 question → 1 deep dive)
50. `rendering-pipeline` - How does Android render UI frames?
## Storage (1 question → 1 deep dive)
51. `storage-types` - What are the different storage options in Android?
## Back Stack & Tasks (1 question → 1 deep dive)
52. `task-and-backstack` - What is a Task and back stack in Android?
## Process Death (1 question → 1 deep dive)
53. `process-death-lifecycle` - What happens to app state when process is killed?
## Multitasking (1 question → 1 deep dive)
54. `multitasking-window-focus` - How does multitasking affect activity lifecycle?
---
## Statistics
- **Total Questions:** 54
- **Total Deep Dives:** 21
- **Beginner:** 16 questions
- **Intermediate:** 32 questions
- **Advanced:** 6 questions
## By Difficulty
### Beginner (16)
activity-lifecycle-overview, onstart-vs-onresume, fragment-lifecycle, context-what-is, 
memory-leak-what-is, anr-what-is, service-what-is, broadcast-receiver, permissions-model, 
manifest-what-is, intent-explicit-implicit, fragment-vs-activity, service-vs-thread, 
storage-types, task-and-backstack, looper-what-is
### Intermediate (32)
onsaved-instance-state, onconfig-change, lifecycle-callbacks-order, intent-filters, 
intent-resolution, intent-flags, pending-intent, fragment-communication, fragment-back-stack, 
fragment-arguments, context-memory-leaks, application-context-vs-activity-context, 
context-lifecycle-awareness, memory-detection, common-leak-patterns, memory-leak-fixes, 
preventing-anr, main-thread-vs-background, jank-dropped-frames, handler-what-is, 
handler-thread, bound-service, intent-service, broadcast-permissions, ordered-vs-sticky-broadcast, 
runtime-permissions, permission-groups, manifest-intent-filters, binder-ipc, 
app-startup-flow, recyclerview-efficiency, rendering-pipeline
### Advanced (6)
process-death-handling, handler-memory-leak, art-vs-dalvik, zygote-process-creation, 
process-death-lifecycle, multitasking-window-focus
---
## Quick Tags Reference
### By Tag
- **android:** All 54 questions
- **lifecycle:** activity-lifecycle-overview, onstart-vs-onresume, onsaved-instance-state, 
  onconfig-change, lifecycle-callbacks-order, fragment-lifecycle, context-lifecycle-awareness, 
  process-death-lifecycle, multitasking-window-focus
- **threading:** looper-what-is, handler-what-is, handler-thread, handler-memory-leak, 
  main-thread-vs-background, service-vs-thread
- **memory:** context-memory-leaks, memory-leak-what-is, memory-detection, common-leak-patterns, 
  memory-leak-fixes, handler-memory-leak
- **performance:** anr-what-is, preventing-anr, jank-dropped-frames, rendering-pipeline, 
  recyclerview-efficiency
- **ipc:** intent-explicit-implicit, intent-filters, intent-resolution, intents, 
  binder-ipc, bound-service
---
**Next Step:** All 21 deep dive markdown files are in place. Regenerate docs and validate site navigation/build.
