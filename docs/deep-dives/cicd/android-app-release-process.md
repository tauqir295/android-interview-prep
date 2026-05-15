---
hide:
  - toc
---

!!! abstract ""
    <a id="back-to-questions" href="/android-interview-prep/generated/cicd/">← Back to CI/CD & Release</a>

<script>
(function () {
  const link = document.getElementById("back-to-questions");
  if (!link) return;
  try {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      link.setAttribute("href", `/android-interview-prep/generated/cicd/${hash}`);
      return;
    }
    const referrer = document.referrer || "";
    if (referrer.includes("/android-interview-prep/generated/")) {
      link.setAttribute("href", referrer);
    }
  } catch (_) {
    // Keep default generated page link if URL parsing fails.
  }
})();
</script>

## Android App Release Process — Complete Deep Dive

## Overview

Shipping an Android app to production involves six distinct phases, each with hard prerequisites before the next can start:

```
Code Freeze
    │
    ▼
1. Build Configuration & Product Flavors
    │
    ▼
2. Code Shrinking, Obfuscation & Optimisation (R8 / ProGuard)
    │
    ▼
3. App Signing (keystore → apksigner)
    │
    ▼
4. Artifact Generation (APK / AAB)
    │
    ▼
5. Distribution Channel (Play Store / Custom Store / Direct APK)
    │
    ▼
6. Post-Release Monitoring & Rollback
```

Cross-cutting concerns — **security hardening, certificate pinning, RASP** — apply from step 2 onward.
→ See the [RASP and Runtime Self-Protection deep dive](/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/) for implementation detail.

---

## 1. Build Configuration

### 1.1 Build Types

```groovy
// build.gradle (app module)
android {
    buildTypes {
        debug {
            applicationIdSuffix ".debug"
            versionNameSuffix "-debug"
            debuggable true          // MUST be false in release
            minifyEnabled false
            signingConfig signingConfigs.debug
        }
        release {
            debuggable false         // Never ship a debuggable APK
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'),
                          'proguard-rules.pro'
            signingConfig signingConfigs.release
        }
    }
}
```

| Property | Debug | Release |
|---|---|---|
| `debuggable` | `true` | **`false`** |
| `minifyEnabled` | `false` | `true` |
| `shrinkResources` | `false` | `true` |
| Stack traces | Readable | Require mapping file |
| NetworkSecurityConfig | Can allow cleartext | Must block cleartext |

### 1.2 Product Flavors

Use flavors to ship variants (free/paid, region-specific, staging/prod backend):

```groovy
android {
    flavorDimensions "tier", "environment"

    productFlavors {
        free {
            dimension "tier"
            applicationIdSuffix ".free"
        }
        paid {
            dimension "tier"
        }
        staging {
            dimension "environment"
            buildConfigField "String", "API_BASE", '"https://staging.api.example.com"'
            versionNameSuffix "-staging"
        }
        production {
            dimension "environment"
            buildConfigField "String", "API_BASE", '"https://api.example.com"'
        }
    }
}
```

This produces `freeProductionRelease`, `paidProductionRelease`, etc. Only `*Release` variants go to the store.

### 1.3 Version Management

```groovy
// Use a single source of truth — never hardcode in two places
def versionMajor = 3
def versionMinor = 2
def versionPatch = 1

android {
    defaultConfig {
        // versionCode must increase monotonically with every store upload
        versionCode versionMajor * 10000 + versionMinor * 100 + versionPatch
        versionName "${versionMajor}.${versionMinor}.${versionPatch}"
    }
}
```

In CI, tie `versionCode` to the build number so it auto-increments:

```groovy
versionCode = System.getenv("BUILD_NUMBER")?.toInteger() ?: 1
```

---

## 2. Code Shrinking, Obfuscation & Optimisation (R8 / ProGuard)

### 2.1 R8 vs ProGuard

| | R8 (recommended) | ProGuard |
|---|---|---|
| Integrated with AGP | ✅ Since AGP 3.4 | Requires separate classpath |
| Desugaring | Built in | Separate step |
| Optimisation passes | Treeshaking + inlining + class merging | Shrink only |
| Kotlin metadata | Aware | Not aware |
| Speed | Faster | Slower |

R8 is the default; never re-enable ProGuard unless you have a specific reason.

### 2.2 R8 Configuration

```proguard
# ─── Keep entry points ──────────────────────────────────────────
# Activities, Services, Receivers and Providers registered in the manifest
-keep public class * extends android.app.Activity
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep public class * extends android.content.ContentProvider

# Application class
-keep public class com.example.app.MyApplication { *; }

# ─── Kotlin / Coroutines ────────────────────────────────────────
-keepnames class kotlinx.coroutines.internal.MainDispatcherFactory {}
-keepnames class kotlinx.coroutines.CoroutineExceptionHandler {}

# ─── Serialisation (Gson / Moshi / kotlinx.serialization) ──────
# Gson: keep data class fields used in fromJson/toJson
-keepclassmembers class com.example.app.model.** {
    <fields>;
}
# Moshi: keep generated adapters
-keep class com.example.app.model.**JsonAdapter { *; }

# kotlinx.serialization
-keepattributes *Annotation*, InnerClasses
-dontnote kotlinx.serialization.AnnotationsKt
-keepclassmembers @kotlinx.serialization.Serializable class ** {
    *** Companion;
    kotlinx.serialization.KSerializer serializer(...);
}

# ─── Retrofit / OkHttp ──────────────────────────────────────────
-dontwarn okhttp3.**
-dontwarn okio.**
-keep class retrofit2.** { *; }
-keepattributes Signature
-keepattributes Exceptions

# ─── Room ───────────────────────────────────────────────────────
-keep class * extends androidx.room.RoomDatabase
-keep @androidx.room.Entity class *
-keep @androidx.room.Dao interface *

# ─── Navigation safe-args ───────────────────────────────────────
-keep class * extends androidx.navigation.NavArgs { *; }

# ─── Crash reporting (Firebase Crashlytics) ─────────────────────
-keepattributes SourceFile, LineNumberTable
# Re-map stack traces with the upload-crashlytics-mapping-file Gradle task

# ─── Security: obfuscate detection logic names (RASP) ───────────
-keepnames class com.example.security.** { *; }

# ─── Debug: preserve source lines in crash reports ──────────────
-keepattributes SourceFile, LineNumberTable
-renamesourcefileattribute SourceFile
```

### 2.3 Mapping File — Critical for Crash Reports

R8 generates `build/outputs/mapping/release/mapping.txt`. You **must** store it alongside each release:

```bash
# Upload to Firebase Crashlytics automatically (AGP plugin)
# app/build.gradle
plugins {
    id 'com.google.firebase.crashlytics'
}

# Or upload manually with the CLI:
firebase crashlytics:mappingfile:upload \
  --app=1:1234567890:android:abc123 \
  app/build/outputs/mapping/release/mapping.txt
```

Never delete old mapping files — you may need to deobfuscate a crash from six months ago.

```bash
# Manually retrace a stack trace
java -jar retrace.jar \
  mapping.txt \
  obfuscated-stacktrace.txt
```

### 2.4 Resource Shrinking

```groovy
release {
    minifyEnabled true   // code shrink must be on for resource shrink
    shrinkResources true
}
```

Animated vector drawables and dynamically referenced resources may be stripped incorrectly. Add keep rules:

```xml
<!-- res/raw/keep.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools"
    tools:keep="@layout/activity_*, @drawable/ic_launcher*"
    tools:discard="@layout/unused_*" />
```

### 2.5 Verifying Shrink Results

```bash
# Generate an APK analysis report
./gradlew assembleRelease

# Inspect with Android Studio APK Analyzer, or CLI:
$ANDROID_SDK/build-tools/34.0.0/aapt2 dump --file resources.arsc app-release.apk

# Check the raw size breakdown:
./gradlew :app:bundleRelease
# then open the .aab in Android Studio → Analyze APK
```

---

## 3. App Signing

### 3.1 Why Signing Matters

Android uses signing to:

- Prove two APKs come from the same author (allowing upgrades)
- Enable `android:sharedUserId` between your own apps
- Gate Play Store updates (a different key = treated as new app)
- Bind `KeyStore`-backed hardware keys to the signing cert (important for RASP)

### 3.2 Generating a Keystore

```bash
# Generate a 4096-bit RSA keystore valid 10 000 days (~27 years)
keytool -genkeypair \
  -keystore release.keystore \
  -alias my-release-key \
  -keyalg RSA \
  -keysize 4096 \
  -validity 10000 \
  -storepass YOUR_STORE_PASSWORD \
  -keypass YOUR_KEY_PASSWORD \
  -dname "CN=Example Corp, OU=Android, O=Example Corp Ltd, L=London, S=England, C=GB"

# Verify the keystore content
keytool -list -v -keystore release.keystore -storepass YOUR_STORE_PASSWORD
```

⚠️ **The keystore is irreplaceable.** Back it up in at least two geographically separate secure locations (HSM, encrypted cloud vault). Losing it means you can never ship an update to existing installs.

### 3.3 Signing Configuration in Gradle

```groovy
// NEVER commit passwords to source control. Read from environment or ~/.gradle/gradle.properties
android {
    signingConfigs {
        release {
            storeFile     file(System.getenv("KEYSTORE_PATH") ?: "release.keystore")
            storePassword System.getenv("KEYSTORE_PASS")
            keyAlias      System.getenv("KEY_ALIAS")
            keyPassword   System.getenv("KEY_PASS")
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
        }
    }
}
```

In CI (GitHub Actions example):

```yaml
# .github/workflows/release.yml
- name: Decode keystore
  run: |
    echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 -d > release.keystore

- name: Build signed release AAB
  env:
    KEYSTORE_PATH: release.keystore
    KEYSTORE_PASS: ${{ secrets.KEYSTORE_PASS }}
    KEY_ALIAS:     ${{ secrets.KEY_ALIAS }}
    KEY_PASS:      ${{ secrets.KEY_PASS }}
  run: ./gradlew :app:bundleRelease
```

### 3.4 APK vs AAB Signing

```bash
# Sign an APK manually with apksigner (preferred over jarsigner)
$ANDROID_SDK/build-tools/34.0.0/apksigner sign \
  --ks release.keystore \
  --ks-pass env:KEYSTORE_PASS \
  --key-pass env:KEY_PASS \
  --ks-key-alias my-release-key \
  --out app-release-signed.apk \
  app-release-unsigned.apk

# Verify the signature
$ANDROID_SDK/build-tools/34.0.0/apksigner verify --verbose app-release-signed.apk

# For AAB, Gradle handles signing automatically when signingConfig is set
./gradlew :app:bundleRelease
```

### 3.5 Google Play App Signing (Recommended for Play Store)

With **Play App Signing**, Google re-signs your AAB with a Google-managed **app signing key** before delivery:

```
Your upload key (you keep it)
       ↓
   Upload AAB to Play Console
       ↓
  Google re-signs with App Signing Key (Google manages, HSM-backed)
       ↓
   APK delivered to devices signed with App Signing Key
```

**Benefits:**
- If you lose your upload key, you can request a new one without losing the app
- Devices always get a signature consistent with the Google-managed key
- Play Console → Setup → App Signing → opt in per app

---

## 4. Artifact Generation

### 4.1 APK vs Android App Bundle (AAB)

| | APK | AAB |
|---|---|---|
| Format | Ready-to-install binary | Build artefact; Google produces APKs |
| Play Store upload | Legacy (still supported) | Required for new apps since Aug 2021 |
| Native libraries | All ABIs bundled | Per-device split |
| Resources | All densities bundled | Per-device split |
| Typical size saving | — | 15–30 % smaller download |
| Sideloading | ✅ Direct | ❌ Not directly installable |

```bash
# Build a release APK
./gradlew :app:assembleRelease
# Output: app/build/outputs/apk/release/app-release.apk

# Build a release AAB (for Play Store)
./gradlew :app:bundleRelease
# Output: app/build/outputs/bundle/release/app-release.aab
```

### 4.2 Pre-Upload Checks

```bash
# 1. Verify signing certificate hash matches what Play Console expects
$ANDROID_SDK/build-tools/34.0.0/apksigner verify \
  --print-certs app-release.apk

# 2. Check versionCode is higher than current Play Store track
# (Play Console rejects uploads with same or lower versionCode)

# 3. Run lint on the release variant
./gradlew :app:lintRelease

# 4. Run baseline profile generation (optional but improves startup)
./gradlew :app:generateBaselineProfile
```

---

## 5. Google Play Store Release Process

### 5.1 One-Time Developer Account Cost

| Account Type | Fee | Who |
|---|---|---|
| **Individual developer** | **USD $25** (one-time, non-refundable) | Personal apps, freelancers |
| **Organisation / company** | **USD $25** (one-time) | Requires D-U-N-S number for verification |

Payment is processed at [play.google.com/console/signup](https://play.google.com/console/signup). The account supports unlimited apps after payment.

> **Note:** Google also charges a **15% service fee** on the first $1M USD in annual revenue per developer, and **30%** above $1M. Subscriptions after the first year drop to 15%.

### 5.2 Step-by-Step Play Console Release

```
1. Create app in Play Console
   └─ App name, default language, app or game, free or paid

2. Fill Store Listing
   ├─ Short description (80 chars)
   ├─ Full description (4 000 chars)
   ├─ Screenshots: phone, 7" tablet, 10" tablet (mandatory)
   ├─ Feature graphic: 1024×500 px
   └─ App icon: 512×512 px (no alpha, no rounded corners — Play rounds them)

3. Content Rating (IARC questionnaire)
   └─ Takes ~10 min; required before first release

4. Target Audience & Content
   └─ Set age group; affects data safety section requirements

5. Data Safety Section
   ├─ Declare every data type your app collects
   ├─ State whether it is shared with third parties
   └─ Link to your privacy policy URL

6. Upload AAB / APK
   └─ Play Console → Production → Create new release → Upload AAB

7. Choose Release Track
   ├─ Internal testing  (up to 100 testers, available in minutes)
   ├─ Closed testing    (alpha; named tester group)
   ├─ Open testing      (beta; opt-in public)
   └─ Production        (full rollout or staged)

8. Staged Rollout (production)
   ├─ Release to 1% → observe crash rate → 5% → 10% → 20% → 50% → 100%
   └─ Halt rollout button available at any stage

9. Review & Publish
   └─ New apps: typically 1–3 business days for first review
      Updates: usually a few hours to 1 business day
```

### 5.3 Release Tracks in Detail

```
Internal Testing ──► Closed Testing ──► Open Testing ──► Production
  (instant)           (hours)           (hours–1day)     (1–3 days first time)
     │                    │                  │                  │
     │              Named groups        Opt-in public      Staged rollout
     │              (max 2000)          (no limit)         (1%–100%)
     └──────────────────────────────────────────────────────────►
                     Promote release between tracks
```

### 5.4 Pre-Launch Report

After upload, Play Console automatically runs your app on Firebase Test Lab devices:

- Crawls the app for crashes, ANRs and accessibility issues
- Reports appear under **Android vitals → Pre-launch report**
- Check this before promoting to production

### 5.5 Android Vitals Thresholds

Google penalises apps that exceed bad-behaviour thresholds:

| Metric | Bad behaviour threshold |
|---|---|
| Crash rate | > 1.09 % daily sessions with crash |
| ANR rate | > 0.47 % daily sessions with ANR |
| Excessive wakeups | > 10/hr on a doze device |
| Excessive background wifi scans | > 4/hr in background |

Exceeding these can result in lowered search ranking or Play Store removal notices.

### 5.6 Automating Play Store Uploads

**Option A: Fastlane Supply**

```ruby
# Fastfile
lane :deploy do
  gradle(task: "bundle", build_type: "Release")
  supply(
    track: "internal",
    aab: "app/build/outputs/bundle/release/app-release.aab",
    json_key: "path/to/play-store-service-account.json",
    skip_upload_apk: true,
    skip_upload_metadata: false,
    skip_upload_screenshots: false
  )
end
```

**Option B: Gradle Play Publisher plugin**

```groovy
// build.gradle
plugins {
    id 'com.github.triplet.play' version '3.9.1'
}

play {
    serviceAccountCredentials.set(file("play-service-account.json"))
    defaultToAppBundles.set(true)
    track.set("internal")
    releaseStatus.set(com.github.triplet.gradle.androidpublisher.ReleaseStatus.DRAFT)
}
```

```bash
# Upload AAB to internal track
./gradlew publishReleaseBundle

# Promote internal → production at staged rollout
./gradlew promoteReleaseArtifact \
  --from-track internal \
  --promote-track production \
  --user-fraction 0.1   # 10% rollout
```

**Option C: GitHub Actions with Fastlane**

```yaml
# .github/workflows/release.yml
name: Release to Play Store

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 17

      - name: Decode keystore
        run: echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 -d > release.keystore

      - name: Decode Play Store service account
        run: echo "${{ secrets.PLAY_SA_JSON_BASE64 }}" | base64 -d > play-sa.json

      - name: Build & Upload
        env:
          KEYSTORE_PATH:  release.keystore
          KEYSTORE_PASS:  ${{ secrets.KEYSTORE_PASS }}
          KEY_ALIAS:      ${{ secrets.KEY_ALIAS }}
          KEY_PASS:       ${{ secrets.KEY_PASS }}
        run: bundle exec fastlane deploy
```

---

## 6. Releasing on a Custom / Alternative App Store

### 6.1 When to Use a Custom Distribution Channel

| Scenario | Recommended approach |
|---|---|
| Enterprise internal app (employees only) | Android Enterprise / MDM, or direct APK (no store) |
| China market (no Google Play) | Huawei AppGallery, Xiaomi GetApps, OPPO App Market, etc. |
| Open-source / privacy-focused apps | F-Droid |
| Gaming / Amazon ecosystem | Amazon Appstore |
| OEM pre-install | OEM partnership program |
| Beta / dog-food builds | Firebase App Distribution |

### 6.2 Direct APK Distribution (Sideloading)

```bash
# Build a signed release APK (not AAB — AAB is not directly installable)
./gradlew :app:assembleRelease

# Verify signature before distributing
$ANDROID_SDK/build-tools/34.0.0/apksigner verify \
  --verbose \
  --print-certs \
  app/build/outputs/apk/release/app-release.apk
```

**On the target device:**
- Settings → Security → Install unknown apps → enable for the source (browser, Files app, MDM)
- `adb install app-release.apk` for direct device installs

**Security considerations for sideloaded APKs:**

- No vetting by a store; users bear the risk
- Use Play Integrity's `requestIntegrityToken` to verify on your backend that the binary hash matches what you shipped
- Consider restricting certain features when `appRecognitionVerdict != PLAY_RECOGNIZED`

### 6.3 Amazon Appstore

```
1. Create developer account at developer.amazon.com
   └─ Free to register; Amazon takes 30% of revenue (20% for qualifying small developers)

2. Build a signed APK (Amazon does not accept AAB — convert your build)
   ./gradlew assembleRelease

3. Submit via Amazon Developer Console
   ├─ Upload APK
   ├─ Fill store listing (similar to Play Console)
   ├─ Set binary files tab: list supported device types
   └─ Amazon reviews typically take 1–5 business days

4. Amazon-specific adaptations:
   ├─ Replace Google Play Billing with Amazon In-App Purchasing SDK
   ├─ Replace Firebase Cloud Messaging with Amazon Device Messaging (ADM)
   └─ Replace Play Integrity with Amazon Device Messaging attestation
```

### 6.4 F-Droid (Open Source)

```
1. App source must be fully open source (FOSS)
   └─ No proprietary dependencies, no ad SDKs, no tracking

2. Submit via fdroid.org/contribute/
   └─ Add a metadata YAML file to the fdroiddata repository

3. F-Droid builds your app from source — you do not upload an APK
   └─ Their reproducible build server signs the APK with their key

4. Metadata file format:
   # metadata/com.example.app.yml
   Categories:
     - Productivity
   License: Apache-2.0
   SourceCode: https://github.com/example/app
   IssueTracker: https://github.com/example/app/issues
   Changelog: https://github.com/example/app/blob/HEAD/CHANGELOG.md
   AutoName: My App
   Description: |
     A great open-source app.
   RepoType: git
   Repo: https://github.com/example/app
   Builds:
     - versionName: '3.2.1'
       versionCode: 30201
       commit: v3.2.1
       subdir: app
       gradle:
         - yes
```

### 6.5 Huawei AppGallery (China / HMS)

```
1. Register at developer.huawei.com/consumer/en/appgallery/
   └─ Free account; 30% revenue share

2. Replace GMS APIs with HMS equivalents:
   ├─ FCM → Huawei Push Kit
   ├─ Google Maps → Huawei Map Kit
   ├─ Play Auth → Huawei Account Kit
   └─ Play Billing → Huawei IAP

3. Use flavor-based dependency injection to ship both GMS and HMS variants:
```

```groovy
// build.gradle
flavorDimensions "distribution"
productFlavors {
    gms {
        dimension "distribution"
        // Google Play Services dependencies
    }
    hms {
        dimension "distribution"
        // Huawei Mobile Services dependencies
    }
}
```

```kotlin
// Abstraction layer for push notifications
interface PushProvider {
    fun registerToken(callback: (String) -> Unit)
}

// src/gms/
class GmsPushProvider : PushProvider {
    override fun registerToken(callback: (String) -> Unit) {
        FirebaseMessaging.getInstance().token.addOnSuccessListener {
            callback(it)
        }
    }
}

// src/hms/
class HmsPushProvider : PushProvider {
    override fun registerToken(callback: (String) -> Unit) {
        HmsInstanceId.getInstance(context).getToken(APP_ID, "HCM").let {
            callback(it)
        }
    }
}
```

### 6.6 Firebase App Distribution (Beta / Internal)

```bash
# Via Fastlane
lane :beta do
  gradle(task: "assemble", build_type: "Release")
  firebase_app_distribution(
    app: "1:1234567890:android:abc123",
    testers: "qa@example.com, pm@example.com",
    release_notes: "Build #{ENV['BUILD_NUMBER']} — #{last_git_commit[:message]}",
    firebase_cli_token: ENV["FIREBASE_TOKEN"],
    groups: "qa-team, product-team"
  )
end

# Via Gradle plugin
plugins {
    id 'com.google.firebase.appdistribution' version '5.0.0'
}

firebaseAppDistribution {
    appId "1:1234567890:android:abc123"
    serviceCredentialsFile "firebase-service-account.json"
    releaseNotes "Internal build"
    testers "qa@example.com"
    groups "qa-team"
}
```

### 6.7 Android Enterprise / MDM (Internal Enterprise Apps)

```
For enterprise-only distribution (employees), skip the store entirely:

1. Build signed APK
2. Upload to your EMM/MDM console:
   - Google Workspace (Managed Google Play) → private app listing
   - Microsoft Intune
   - VMware Workspace ONE
   - Jamf

3. For Managed Google Play (private channel):
   - No $25 fee required
   - App is invisible to public
   - Push silently to managed devices
   - Supports all Play Console release tracks for internal enterprise

4. For raw MDM (non-Play):
   - Sign APK with your enterprise key
   - Upload to MDM server
   - MDM pushes install command to enrolled devices
   - Device policy can mandate only MDM-sourced APKs
```

---

## 7. Library Release Process

### 7.1 JCenter (Deprecated — Historical Context)

JCenter (hosted by JFrog/Bintray) was the dominant Android library registry until **May 1, 2021**, when JFrog shut it down. Libraries still hosted there are archived and read-only.

**Migration path:** any library previously on JCenter should be migrated to **Maven Central** or **Google Maven**. Do not publish new libraries to JCenter.

### 7.2 Google Maven Repository (`google()`)

Google Maven (`https://maven.google.com`) hosts **first-party Google and AndroidX libraries only**. You cannot publish third-party libraries here unless you are a Google partner. It is added automatically in AGP projects:

```groovy
repositories {
    google()       // → https://maven.google.com
    mavenCentral() // → https://repo.maven.apache.org/maven2
}
```

### 7.3 Maven Central (Standard for Open-Source Android Libraries)

Maven Central (operated by Sonatype) is the de-facto standard for open-source JVM/Android library publication.

#### Step-by-Step: Publishing to Maven Central

```
1. Register a namespace on central.sonatype.com
   ├─ Create account at central.sonatype.com
   ├─ Register group ID namespace (matches your domain reversed):
   │    com.github.yourusername  ← for GitHub-based projects
   │    io.yourcompany           ← requires domain verification (DNS TXT record)
   └─ Claim takes 1–3 business days

2. Generate GPG signing key (required for Central)
   # Generate 4096-bit RSA key
   gpg --gen-key
   gpg --list-keys  # note your KEY_ID

   # Upload public key to key servers
   gpg --keyserver keyserver.ubuntu.com --send-keys YOUR_KEY_ID
   gpg --keyserver keys.openpgp.org --send-keys YOUR_KEY_ID

   # Export secret key for CI
   gpg --export-secret-keys --armor YOUR_KEY_ID > signing-key.gpg

3. Configure your library's build.gradle
4. Publish
```

#### Library `build.gradle` Configuration

```groovy
// library/build.gradle
plugins {
    id 'com.android.library'
    id 'kotlin-android'
    id 'maven-publish'
    id 'signing'
}

group    = 'io.example'
version  = '1.2.3'

android {
    publishing {
        singleVariant('release') {
            withSourcesJar()
            withJavadocJar()
        }
    }
}

afterEvaluate {
    publishing {
        publications {
            release(MavenPublication) {
                from components.release

                groupId    = 'io.example'
                artifactId = 'my-library'
                version    = '1.2.3'

                pom {
                    name        = 'My Library'
                    description = 'A well-crafted Android Library'
                    url         = 'https://github.com/example/my-library'

                    licenses {
                        license {
                            name = 'The Apache License, Version 2.0'
                            url  = 'http://www.apache.org/licenses/LICENSE-2.0.txt'
                        }
                    }
                    developers {
                        developer {
                            id    = 'johndoe'
                            name  = 'John Doe'
                            email = 'john@example.io'
                        }
                    }
                    scm {
                        connection          = 'scm:git:https://github.com/example/my-library.git'
                        developerConnection = 'scm:git:ssh://github.com/example/my-library.git'
                        url                 = 'https://github.com/example/my-library'
                    }
                }
            }
        }

        repositories {
            maven {
                name = "SonatypeCentral"
                url  = uri("https://central.sonatype.com/api/v1/publisher/upload")
                credentials {
                    username = findProperty("sonatypeUsername") ?: System.getenv("SONATYPE_USERNAME")
                    password = findProperty("sonatypePassword") ?: System.getenv("SONATYPE_PASSWORD")
                }
            }
        }
    }

    signing {
        def signingKey     = findProperty("signingKey")     ?: System.getenv("SIGNING_KEY")
        def signingKeyId   = findProperty("signingKeyId")   ?: System.getenv("SIGNING_KEY_ID")
        def signingPasswd  = findProperty("signingPassword") ?: System.getenv("SIGNING_PASSWORD")
        useInMemoryPgpKeys(signingKeyId, signingKey, signingPasswd)
        sign publishing.publications.release
    }
}
```

#### Publishing Commands

```bash
# Publish to local Maven repository for local testing first
./gradlew publishToMavenLocal
# Verify at ~/.m2/repository/io/example/my-library/1.2.3/

# Consume locally in another project:
# settings.gradle
repositories {
    mavenLocal()
    mavenCentral()
}

# Publish to Maven Central staging
./gradlew publishReleasePublicationToSonatypeCentralRepository

# Promote staging → release in Sonatype Central portal
# At central.sonatype.com → Deployments → select → Publish
```

#### `~/.gradle/gradle.properties` (local secrets — never commit)

```properties
sonatypeUsername=your-sonatype-token-username
sonatypePassword=your-sonatype-token-password
signingKeyId=ABCD1234
signingKey=-----BEGIN PGP PRIVATE KEY BLOCK-----\n...
signingPassword=your-gpg-passphrase
```

### 7.4 Automating Library Release with GitHub Actions

```yaml
# .github/workflows/publish-library.yml
name: Publish Library to Maven Central

on:
  release:
    types: [ published ]   # Trigger on GitHub release creation

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 17

      - name: Publish to Maven Central
        env:
          SONATYPE_USERNAME:  ${{ secrets.SONATYPE_USERNAME }}
          SONATYPE_PASSWORD:  ${{ secrets.SONATYPE_PASSWORD }}
          SIGNING_KEY_ID:     ${{ secrets.SIGNING_KEY_ID }}
          SIGNING_KEY:        ${{ secrets.SIGNING_KEY }}
          SIGNING_PASSWORD:   ${{ secrets.SIGNING_PASSWORD }}
        run: |
          ./gradlew :library:publishReleasePublicationToSonatypeCentralRepository \
            -Pversion=${{ github.event.release.tag_name }}
```

### 7.5 JitPack (Lightweight Alternative for GitHub Projects)

JitPack builds directly from a GitHub (or GitLab) release tag — no Sonatype account or GPG key needed.

```groovy
// Consumer's settings.gradle
dependencyResolutionManagement {
    repositories {
        maven { url 'https://jitpack.io' }
    }
}

// Consumer's build.gradle — uses GitHub username/repo:tag format
dependencies {
    implementation 'com.github.YourUsername:my-library:v1.2.3'
}
```

**To publish:**
1. Push a git tag (`v1.2.3`) to GitHub
2. Go to `jitpack.io/#YourUsername/my-library`
3. Click "Get it" — JitPack builds and caches the artifact on first request

**Trade-offs vs Maven Central:**

| | JitPack | Maven Central |
|---|---|---|
| Setup effort | Minutes | Hours–Days |
| GPG signing | Not required | Mandatory |
| Availability | Depends on JitPack SLA | Highly available mirrored CDN |
| Discoverability | Low (not in default repos) | High (default in most JVM projects) |
| Suitable for | Prototypes, small OSS projects | Production, widely-adopted libs |

### 7.6 Library Versioning — Semantic Versioning

Always follow **SemVer** (`MAJOR.MINOR.PATCH`):

| Increment | When |
|---|---|
| `MAJOR` | Breaking API change; consumers must update call-sites |
| `MINOR` | New functionality, backward-compatible |
| `PATCH` | Bug fixes, no API change |
| `-alpha`, `-beta`, `-rc` | Pre-release suffixes; not promoted to consumers by default |

```groovy
// version.gradle — single source of truth for a multi-module library
ext {
    libraryVersion = "2.1.0"

    // Exposed as BOM (Bill of Materials) so consumers pin one version:
    // implementation platform('io.example:my-library-bom:2.1.0')
}
```

**BOM publication (multi-module libraries like OkHttp, Retrofit):**

```groovy
// bom/build.gradle
plugins {
    id 'java-platform'
    id 'maven-publish'
}

javaPlatform {
    allowDependencies()
}

dependencies {
    constraints {
        api "io.example:my-library-core:${libraryVersion}"
        api "io.example:my-library-retrofit:${libraryVersion}"
        api "io.example:my-library-room:${libraryVersion}"
    }
}
```

---

## 8. Security Hardening During Release

The release phase is the last line of defence before shipping to users. Apply these on every release build:

| Check | Tool / Mechanism |
|---|---|
| ProGuard/R8 obfuscation on | `minifyEnabled true` in release buildType |
| No `debuggable` flag | Lint rule `DebugConfiguration` |
| Certificate pinning active | `network_security_config.xml` + OkHttp pinner |
| RASP checks enabled | `RaspOrchestrator.initialize()` in Application.onCreate |
| No secrets in binary | `BuildConfig` fields + R8 string obfuscation |
| Play App Signing enrolled | Play Console → App Signing |
| Mapping file archived | Firebase Crashlytics or internal artefact store |

→ For full implementation detail on RASP, certificate pinning and keystore-backed key storage, see the [App Security deep dive](/android-interview-prep/deep-dives/security/rasp-and-runtime-self-protection/).

---

## 9. Post-Release Monitoring

### 9.1 Key Metrics to Watch in the First 24 Hours

```
Release pushed to 1%
       │
       ├── Crash rate          (Firebase Crashlytics, Play Console Android Vitals)
       ├── ANR rate            (Play Console → Android Vitals → ANRs)
       ├── Crash-free sessions (Crashlytics dashboard)
       ├── P90 / P99 startup time (Firebase Performance)
       ├── User reviews delta  (Play Console → Reviews)
       └── Revenue / conversion (Play Console → Statistics)
```

### 9.2 Automated Rollback

```bash
# Halt a staged rollout via Gradle Play Publisher:
./gradlew promoteReleaseArtifact \
  --promote-track production \
  --release-status halted

# Or via Play Console UI:
# Production → Releases → three-dot menu → Halt rollout
```

Set up crash-rate alerts in Firebase Crashlytics:
- Dashboard → Alerts → Create alert → Crash-free users drops below 99.5 %

---

## Senior-Level Insights

- **Never ship a `debuggable` APK.** Android's debuggable flag disables SELinux enforcement for your process and allows any app to attach a debugger. Check this with Lint rule `DebugConfiguration` and fail the CI pipeline if it triggers on a release build.
- **Treat the keystore like a root CA private key.** Loss is irreversible for Play Store deployment. Store in an HSM-backed vault (e.g. AWS CloudHSM, HashiCorp Vault), never in the source repository.
- **The AAB format reduces install size but requires Play App Signing.** For sideloaded enterprise distribution, you still need a signed APK — maintain both build tasks in your CI pipeline.
- **Staged rollouts are risk mitigation, not optional.** Always start production rollouts at 1–5 %, monitor Android Vitals for 24 h, then increase. A bad release caught at 1 % affects thousands of users instead of millions.
- **Library authors: breaking changes should bump MAJOR version immediately.** Never release a breaking change as a MINOR bump — consumers who auto-update on `+` version ranges will break silently.
- **Maven Central POM metadata is not cosmetic.** Sonatype will reject publications missing SCM, license, and developer entries. Set these up correctly from the first release.
- **ProGuard mapping files are forensic evidence.** Archive every mapping file in a content-addressed store tied to `versionCode`. You may need to deobfuscate a stack trace from a user running a build that is 18 months old.

