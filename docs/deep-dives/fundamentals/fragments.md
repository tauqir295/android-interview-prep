---
hide:
  - toc
---

!!! abstract ""

    <a id="back-to-questions" href="/android-interview-prep/generated/fundamentals/">← Back to Fundamentals</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;

  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/fundamentals/${hash}`);
      return;
    }

    const referrer = document.referrer || "";
    if (referrer.includes("/android-interview-prep/generated/")) {
      link.setAttribute("href", referrer);
    }
  } catch (_) {
    // Keep default fundamentals link if URL parsing fails.
  }
})();
</script>

# Fragments Deep Dive

## Overview

Fragments are reusable UI components within an Activity. They have their own lifecycle, manage their own UI, and can be dynamically added, removed, and replaced. Understanding Fragment lifecycle and architecture is essential for modern Android development.

---

## Fragment Lifecycle

### Lifecycle Methods (Complete Sequence)

```
onCreate()
  ↓
onCreateView() [RETURN Layout]
  ↓
onViewCreated() [View tree ready]
  ↓
onStart()
  ↓
onResume()
  ↓
[USER INTERACTION]
  ↓
onPause()
  ↓
onStop()
  ↓
onDestroyView()
  ↓
onDestroy()
  ↓
onDetach()
```

### Key Lifecycle Methods

**onCreate()**
- Fragment instance created (UI not yet created)
- Safe to access arguments
- Don't access views here yet

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    val userId = arguments?.getInt("user_id") ?: 0
    viewModel.loadUser(userId)
}
```

**onCreateView()**
- Called to create fragment's UI view hierarchy
- **MUST return the root View of hierarchy**
- First time to inflate layout

```kotlin
override fun onCreateView(
    inflater: LayoutInflater,
    container: ViewGroup?,
    savedInstanceState: Bundle?
): View {
    return inflater.inflate(R.layout.fragment_main, container, false)
    // Return inflated view, container is Activity's container
}
```

**onViewCreated()**
- Called after onCreateView() returns
- View hierarchy now fully created
- **Safe to access views here**
- Modern Kotlin Synthetics or View Binding

```kotlin
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    super.onViewCreated(view, savedInstanceState)
    
    binding = FragmentMainBinding.bind(view)
    
    binding.button.setOnClickListener {
        // Handle click
    }
    
    viewModel.data.observe(viewLifecycleOwner) { data ->
        updateUI(data)
    }
}
```

**onStart()**
- Fragment visible to user
- Navigate to onResume() → onStop() → back to onStart()

**onResume()**
- Fragment interactive (has focus)
- All animations should be at full speed

**onPause()**
- Fragment losing focus
- Stop animations, pause playback
- Quick return required

**onStop()**
- Fragment no longer visible
- Safe for state saving

**onDestroyView()**
- View hierarchy being destroyed
- **Null out your view binding/references here**

```kotlin
override fun onDestroyView() {
    // Must null out binding to avoid memory leaks
    binding = null
    super.onDestroyView()
}
```

**onDestroy()**
- Fragment instance being destroyed
- Clean up observers, resources

**onDetach()**
- Fragment being removed from Activity
- Last lifecycle method

---

## Fragment vs Activity

### Comparison Table

| Feature | Activity | Fragment |
|---------|----------|----------|
| Creation | Entry point in manifest | No manifest entry needed |
| Lifecycle | Owns full lifecycle | Dependent on host Activity |
| Standalone | Can exist alone | Must be hosted in Activity |
| Window | Has own window | Shares Activity's window |
| Navigation | Full screen transitions | Can update partial UI |
| Back button | Handled by system | Controlled by FragmentManager |
| Memory | Heavier | Lighter, reusable |

### When to Use Each

**Use Activity for:**
- App entry points
- Full-screen distinct sections
- Navigation between major app sections

**Use Fragment for:**
- Reusable UI components
- Modular screens
- Tabbed interfaces
- Master-detail layouts
- Swap UI without changing Activity

### Architecture Pattern

```
MainActivity (Activity - container)
  ├─ Fragment A (reusable component)
  ├─ Fragment B (reusable component)
  └─ Fragment C (reusable component)

All fragments share MainActivity's window
Can be swapped independently
```

---

## Fragment Communication

### Pattern 1: Shared ViewModel (BEST PRACTICE)

```kotlin
// Shared ViewModel
class UserViewModel : ViewModel() {
    val selectedUser = MutableLiveData<User>()
}

// Fragment A (Master)
class UserListFragment : Fragment() {
    private val viewModel: UserViewModel by activityViewModels()
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding.list.setOnItemClickListener { user ->
            viewModel.selectedUser.value = user  // Notify others
        }
    }
}

// Fragment B (Detail)
class UserDetailFragment : Fragment() {
    private val viewModel: UserViewModel by activityViewModels()
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        viewModel.selectedUser.observe(viewLifecycleOwner) { user ->
            displayUserDetails(user)
        }
    }
}
```

**Why this works:**
- ViewModel shared across fragments (owned by Activity)
- Survives fragment replacement
- Survives configuration changes
- LiveData observers automatically lifecycle-aware

### Pattern 2: Interface Callback (Legacy)

```kotlin
interface UserSelectionListener {
    fun onUserSelected(user: User)
}

class UserListFragment : Fragment() {
    lateinit var listener: UserSelectionListener
    
    override fun onAttach(context: Context) {
        super.onAttach(context)
        listener = context as? UserSelectionListener
            ?: throw RuntimeException("Must implement UserSelectionListener")
    }
    
    private fun onUserClicked(user: User) {
        listener.onUserSelected(user)
    }
}

class MainActivity : AppCompatActivity(), UserSelectionListener {
    override fun onUserSelected(user: User) {
        val detailFragment = UserDetailFragment.newInstance(user)
        supportFragmentManager.beginTransaction()
            .replace(R.id.detail_container, detailFragment)
            .commit()
    }
}
```

**Downside:** Verbose, tightly couples to Activity

### Pattern 3: Bundle Arguments (Static Data)

```kotlin
class UserDetailFragment : Fragment() {
    companion object {
        private const val ARG_USER_ID = "user_id"
        
        fun newInstance(userId: Int) = UserDetailFragment().apply {
            arguments = Bundle().apply {
                putInt(ARG_USER_ID, userId)
            }
        }
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val userId = arguments?.getInt(ARG_USER_ID) ?: 0
        viewModel.loadUser(userId)
    }
}

// Usage
val fragment = UserDetailFragment.newInstance(123)
```

**Use for:** Initial data passing only, not ongoing communication

---

## Fragment Back Stack

### How It Works

```kotlin
fragmentManager.beginTransaction()
    .replace(R.id.container, newFragment)
    .addToBackStack(null)
    .commit()

// Stack state:
// TOP: [NewFragment]
// [PreviousFragment]
```

### With Named Back Stack Entry

```kotlin
fragmentManager.beginTransaction()
    .replace(R.id.container, newFragment)
    .addToBackStack("detail_screen")
    .commit()

// Pop by name
fragmentManager.popBackStackImmediate("detail_screen",
    FragmentManager.POP_BACK_STACK_INCLUSIVE)
```

### Back Button Behavior

```kotlin
// Back pressed
// System calls: fragmentManager.popBackStack()

// Stack pops:
// [PreviousFragment] → TOP
// [CurrentFragment] removed
```

### Manual Back Stack Control

```kotlin
// Go back specifically
fragmentManager.popBackStack()

// Check if can go back
if (fragmentManager.backStackEntryCount > 0) {
    fragmentManager.popBackStack()
}

// Clear entire back stack
fragmentManager.popBackStack(null, FragmentManager.POP_BACK_STACK_INCLUSIVE)
```

### Animation with Back Stack

```kotlin
fragmentManager.beginTransaction()
    .setCustomAnimations(
        R.anim.slide_in,
        R.anim.fade_out,
        R.anim.fade_in,
        R.anim.slide_out
    )
    .replace(R.id.container, newFragment)
    .addToBackStack(null)
    .commit()
```

---

## Best Practices

### 1. Always Use Fragment Factory for Arguments

```kotlin
// ✅ CORRECT
class UserDetailFragment : Fragment() {
    companion object {
        fun newInstance(userId: Int) = UserDetailFragment().apply {
            arguments = Bundle().apply { putInt("user_id", userId) }
        }
    }
}

// Use
val fragment = UserDetailFragment.newInstance(123)

// ❌ WRONG - Args lost on process death
class UserDetailFragment : Fragment(userId: Int) {}
```

### 2. Always Clean Up View References

```kotlin
override fun onDestroyView() {
    binding = null  // Prevent memory leaks
    super.onDestroyView()
}
```

### 3. Use Lifecycle-Aware Observers

```kotlin
// ✅ CORRECT - automatically handles lifecycle
viewModel.data.observe(viewLifecycleOwner) { data ->
    updateUI(data)
}

// ❌ WRONG - can cause memory leaks
viewModel.data.observe(this) { data ->  // 'this' is Fragment lifecycle
    updateUI(data)
}
```

### 4. Use Appropriate ViewManager for Different Scenarios

```kotlin
// Replace (swap fragments)
fragmentManager.beginTransaction()
    .replace(R.id.container, newFragment)
    .addToBackStack(null)
    .commit()

// Add (stack fragments)
fragmentManager.beginTransaction()
    .add(R.id.container, newFragment)
    .addToBackStack(null)
    .commit()

// Hide/Show (don't destroy)
fragmentManager.beginTransaction()
    .hide(currentFragment)
    .show(newFragment)
    .commit()
```

---

## Common Pitfalls

### Pitfall 1: Accessing Views Before onViewCreated()

```kotlin
// ❌ WRONG - binding is null
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding.button.text = "Hi"  // NullPointerException
}

// ✅ CORRECT
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    super.onViewCreated(view, savedInstanceState)
    binding.button.text = "Hi"  // Safe
}
```

### Pitfall 2: Creating Fragments with Constructor Arguments

```kotlin
// ❌ WRONG - args lost on process death
class UserFragment(userId: Int) : Fragment() {
    // userId lost if process killed
}

// ✅ CORRECT
class UserFragment : Fragment() {
    companion object {
        fun newInstance(userId: Int) = UserFragment().apply {
            arguments = Bundle().apply { putInt("user_id", userId) }
        }
    }
}
```

### Pitfall 3: Retaining Fragment Lifecycle

```kotlin
// ❌ DEPRECATED - don't use this anymore
setRetainInstance(true)

// ✅ USE ViewModel INSTEAD
class MyVM : ViewModel() {
    // Survives configuration changes automatically
}
```

---

## Key Takeaways

✅ Fragments are reusable UI components within Activities

✅ Fragment lifecycle includes onCreateView() for UI creation

✅ Always use onViewCreated() to access views

✅ Use ViewModel for fragment communication (best practice)

✅ Always add onDestroyView() { binding = null } to prevent leaks

✅ Use viewLifecycleOwner for lifecycle-aware observers

✅ Always use factory companion object for safe arguments

✅ Fragment back stack managed by FragmentManager

