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

# Intents Deep Dive

## Overview

Intents are Android's primary mechanism for inter-component communication. An Intent encapsulates the "request" to perform some action, and can be used to start Activities, Services, or deliver Broadcasts. They're fundamental to Android's loose coupling philosophy.

---

## Intent Architecture

### Intent Structure

```kotlin
data class Intent(
    action: String = ACTION_MAIN,
    uri: Uri? = null,
    pkg: String? = null,
    cls: ComponentName? = null,
    extras: Bundle = Bundle(),
    flags: Int = 0,
    categories: Set<String> = emptySet(),
    type: String? = null,  // MIME type
    selector: Intent? = null  // For intent forwarding
)
```

### Core Intent Properties

**Action:** What operation to perform
```
ACTION_MAIN       - App entry point
ACTION_VIEW       - Display data
ACTION_SEND       - Send data
ACTION_CALL       - Initiate phone call
ACTION_SETTINGS   - Open system settings
```

**Category:** Hints about the component
```
CATEGORY_LAUNCHER    - Launchable icon
CATEGORY_DEFAULT     - Default handler
CATEGORY_BROWSABLE   - Can be invoked by browser
```

**Data:** URI and MIME type
```
scheme://host:port/path?query#fragment
content://contacts/people/1
https://example.com/page
file:///path/to/file
```

**Component:** Explicit target (optional for implicit)
```kotlin
ComponentName(packageName, className)
```

**Extras:** Bundle of additional data
```kotlin
intent.putExtra("key", value)
intent.putParcelableArrayListExtra("items", items)
```

**Flags:** Special handling instructions
```
FLAG_ACTIVITY_NEW_TASK
FLAG_ACTIVITY_CLEAR_TOP
FLAG_ACTIVITY_SINGLE_TOP
```

---

## Explicit vs Implicit Intents

### Explicit Intent
**You specify the exact component to start**

```kotlin
// Explicit - you know exactly what to start
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("item_id", 123)
startActivity(intent)
```

**Characteristics:**
- Package name + Class name known
- Guaranteed to reach target (or fail if not found)
- Direct app-to-app communication
- Used for internal app navigation
- Fastest resolution

**Internal app example:**
```kotlin
// From MainActivity to SettingsActivity
Intent(this, SettingsActivity::class.java).apply {
    putExtra("tab", "display")
    startActivity(this)
}
```

### Implicit Intent
**You describe what you want, system finds handler**

```kotlin
// Implicit - system decides who handles it
val intent = Intent(Intent.ACTION_VIEW).apply {
    data = Uri.parse("https://example.com")
}
startActivity(intent)

// System: "Who can handle VIEW action with https URI?" → Browser
```

**Characteristics:**
- Describe desired action + data
- System matches against installed app intent filters
- May show chooser if multiple matches
- Used for cross-app communication
- System decides implementation
- Decouples apps

**Cross-app examples:**
```kotlin
// Open browser
Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com"))

// Send email
Intent(Intent.ACTION_SEND).apply {
    putExtra(Intent.EXTRA_EMAIL, arrayOf("user@example.com"))
    putExtra(Intent.EXTRA_SUBJECT, "Hello")
    putExtra(Intent.EXTRA_TEXT, "Message body")
    type = "message/rfc822"
}

// Share to any app that accepts text
Intent(Intent.ACTION_SEND).apply {
    putExtra(Intent.EXTRA_TEXT, "Check this out!")
    type = "text/plain"
}
```

---

## Intent Filters

### Declaration in Manifest

```xml
<activity android:name=".MainActivity">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <action android:name="android.intent.action.VIEW" />
        
        <category android:name="android.intent.category.LAUNCHER" />
        <category android:name="android.intent.category.DEFAULT" />
        
        <data
            android:scheme="https"
            android:host="example.com"
            android:pathPattern="/products/.*"
            android:mimeType="application/pdf"
        />
    </intent-filter>
</activity>
```

### Matching Algorithm

For implicit intent to match, ALL of these must pass:

1. **Action Match (exactly)**
   - Intent action must match one declared action
   - If intent has no action: matches any filter with action

2. **Category Match (all must match)**
   - All intent categories must be in filter
   - `CATEGORY_DEFAULT` added automatically if not specified
   - Filter `CATEGORY_DEFAULT` is implicit requirement

3. **Data Match**
   - Intent URI + MIME type must match
   - Both scheme AND host must match
   - MIME type wildcard: `text/*`, `*/*`

**Example matching:**

```xml
<!-- Filter -->
<filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <data android:scheme="https" android:host="example.com" />
</filter>

<!-- ✅ MATCHES -->
Intent(Intent.ACTION_VIEW).apply {
    data = Uri.parse("https://example.com/page")
}

<!-- ❌ DOESN'T MATCH: wrong scheme -->
Intent(Intent.ACTION_VIEW).apply {
    data = Uri.parse("http://example.com/page")  // http not https
}

<!-- ❌ DOESN'T MATCH: wrong action -->
Intent(Intent.ACTION_SEND).apply {
    data = Uri.parse("https://example.com/page")
}
```

---

## Intent Resolution

### Resolution Process (Step-by-Step)

**1. Find all installed apps with components declaring intent filters for this action/data**

```
Query: "Which apps can handle VIEW + https://maps.example.com?"

Result:
- Google Maps (can handle location URLs)
- Google Chrome (can handle https)
- Safari (can handle https)
```

**2. Filter by Action**
- Intent action must match exactly one declared action
- Empty intent action matches any filter with action

**3. Filter by Category**
- All intent categories must exist in filter
- `CATEGORY_DEFAULT` special handling

**4. Filter by Data**
- Scheme, host, port, path, MIME type
- Must satisfy all specified constraints

**5. Result**
- No matches → ActivityNotFoundException
- One match → Start that activity
- Multiple matches → Show chooser dialog

### Resolution Code

```kotlin
// Implicit intent
val intent = Intent(Intent.ACTION_VIEW)
intent.data = Uri.parse("https://example.com/page")

// Android internally:
val resolveInfoList = packageManager.queryIntentActivities(intent, 0)
// Returns all activities that can handle this intent

if (resolveInfoList.isEmpty()) {
    // No handler found
    throw ActivityNotFoundException()
}

if (resolveInfoList.size == 1) {
    // Only one handler, start it
    startActivity(intent)
}

if (resolveInfoList.size > 1) {
    // Multiple handlers, show chooser
    val chooser = Intent.createChooser(intent, "Open with")
    startActivity(chooser)
}
```

---

## Intent Flags: Complete Reference

### Task/Back Stack Flags

**FLAG_ACTIVITY_NEW_TASK**
```kotlin
startActivity(Intent(this, BrowserActivity::class.java).apply {
    flags = Intent.FLAG_ACTIVITY_NEW_TASK
})
// Starts activity in a NEW task (new root in back stack)
// Used when starting from non-Activity context (Service, Broadcast)

// Without: Exception!
// Service can't start activity without FLAG_ACTIVITY_NEW_TASK
```

**FLAG_ACTIVITY_SINGLE_TOP**
```
Before:  [A] [B] [C] ← top
Intent to C with FLAG_ACTIVITY_SINGLE_TOP

After:   [A] [B] [C] (C.onNewIntent() called instead of onCreate)
// Prevents duplicate at top of stack
```

**FLAG_ACTIVITY_CLEAR_TOP**
```
Before:  [A] [B] [C] [D] ← top
Intent to B with FLAG_ACTIVITY_CLEAR_TOP

After:   [A] [B] ← top
// C and D removed, B comes to top (or recreated if not running)
```

**FLAG_ACTIVITY_CLEAR_TASK**
```
Before:  TaskX: [A] [B] [C]
Intent to new activity with FLAG_ACTIVITY_CLEAR_TASK

After:   TaskX: [NewActivity] ← top
// Previous task cleared entirely
// New activity becomes sole member of task
```

**FLAG_ACTIVITY_TASK_ON_HOME**
```kotlin
// Activity can be started from home screen
// Placed on home task if no existing task
```

### Visibility/Reset Flags

**FLAG_ACTIVITY_NO_HISTORY**
```
// Activity won't appear in recents
// Won't appear in back button history
// Back button skips it
```

**FLAG_ACTIVITY_PREVIOUS_IS_TOP**
```
// For internal use by system
// Previous activity should be treated as top
```

---

## PendingIntent

### What It Is
**Wrapped Intent to be executed later by another app with your permissions**

```kotlin
// Normal Intent
val intent = Intent(this, MainActivity::class.java)
startActivity(intent)

// PendingIntent
val pendingIntent = PendingIntent.getActivity(
    this,
    requestCode = 0,
    intent = Intent(this, MainActivity::class.java),
    flags = PendingIntent.FLAG_IMMUTABLE
)
// Can be passed to notification, alarm, widget, etc
// They execute it later
```

### Why Needed

**Problem:** System components don't have access to your Activity

```
Notification system: "User tapped notification"
Notification: "I have a PendingIntent from earlier"
Notification: "Execute this PendingIntent"
System: Runs it as if from your app
```

### Common Uses

**1. Notifications**
```kotlin
val pendingIntent = PendingIntent.getActivity(
    context,
    0,
    Intent(context, DetailActivity::class.java),
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
)

NotificationCompat.Builder(context)
    .setContentIntent(pendingIntent)
    .build()
```

**2. Alarms**
```kotlin
val pendingIntent = PendingIntent.getBroadcast(
    context,
    alarmID,
    Intent(context, AlarmReceiver::class.java),
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
)

alarmManager.setAndAllowWhileIdle(
    AlarmManager.RTC_WAKEUP,
    triggerTime,
    pendingIntent
)
```

**3. Widget Buttons**
```kotlin
val pendingIntent = PendingIntent.getService(
    context,
    0,
    Intent(context, MyService::class.java),
    PendingIntent.FLAG_IMMUTABLE
)

remoteViews.setOnClickPendingIntent(R.id.button, pendingIntent)
```

### Types

```kotlin
// Start Activity
PendingIntent.getActivity(context, id, intent, flags)

// Start Service
PendingIntent.getService(context, id, intent, flags)

// Send Broadcast
PendingIntent.getBroadcast(context, id, intent, flags)

// Send Foreground Service Intent (Android 12+)
PendingIntent.getForegroundService(context, id, intent, flags)
```

### Flags: Critical Security

**FLAG_IMMUTABLE (Android 12+ required)**
```kotlin
// Cannot be modified by caller
// Safer, recommended for all new code
PendingIntent.getActivity(
    context, 0, intent,
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
)
```

**FLAG_MUTABLE (Deprecated, avoid)**
```kotlin
// Can be modified by anyone who receives it
// Security risk
// Only use if absolutely necessary
```

**FLAG_UPDATE_CURRENT**
```kotlin
// Reuse existing PendingIntent if exists
// Update extras if provided
```

**FLAG_CANCEL_CURRENT**
```kotlin
// Cancel existing PendingIntent
// Create new one
```

---

## Intent Data Extras

### Passing Data

**With Intent**
```kotlin
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("user_id", 123)
intent.putExtra("user_name", "Alice")
intent.putExtra("user", userObject)  // Must be Parcelable/Serializable

startActivity(intent)

// Receiving
val userId = intent.getIntExtra("user_id", -1)
val userName = intent.getStringExtra("user_name")
val user = intent.getParcelableExtra<UserData>("user")
```

**Size Limitation**
- Bundle size ~500KB but depends on device
- Large data should use shared database/file instead

**Best Practice**
```kotlin
// Instead of passing large objects directly
intent.putExtra("item_id", 123)

// In receiving activity
val itemId = intent.getIntExtra("item_id", -1)
val item = viewModel.loadItem(itemId)  // Fetch from repository
```

---

##  Common Interview Questions

**Q: Can you pass ArrayList to Intent?**
A: Yes, if objects are Parcelable:
```kotlin
val list = arrayListOf(item1, item2)
intent.putParcelableArrayListExtra("items", list as ArrayList)
```

**Q: What's the difference between ACTION_SEND and ACTION_SEND_MULTIPLE?**
A: ACTION_SEND for single item, ACTION_SEND_MULTIPLE for multiple items

**Q: Why use createChooser()?**
A: Shows chooser even if one handler exists, allows "Always" selection

**Q: When is DATA filter applied?**
A: Only if Intent specifies data (setData/setDataAndType)

**Q: Why use FLAG_ACTIVITY_CLEAR_TOP?**
A: Prevents duplicates in back stack, useful for deep links

---

## Key Takeaways

✅ Explicit = known target, fast, internal navigation

✅ Implicit = describe action, system decides, cross-app

✅ Intent Filters declare what implicit intents are handled

✅ Resolution matches Action → Categories → Data

✅ Flags control back stack behavior

✅ PendingIntent = deferred execution with your permissions

✅ Always use FLAG_IMMUTABLE for PendingIntent (Android 12+)

