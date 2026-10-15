# Apple Privacy and SDK Requirements

> Knowledge as of 2026-10. Read at the source on 2026-10-12 to 2026-10-15: App Review Guidelines 5.1 (last updated 2026-06-08, [Official, 2026-06]); privacy manifest, required reason API, protected resource and entitlement documentation, the third party SDK list, the account deletion page and the purpose string help page ([Official, 2026-10]); the ATT and Sign in with Apple news items ([Official, 2026-08] and [Official, 2026-09]). Capacitor facts come from the official plugin READMEs on the npm registry, versions named per row. This module tells you what App Review and App Store Connect check; consent law (GDPR, KVKK, COPPA) is owned by `compliance` and consent tooling by `measurement`.

## 1. The privacy stack App Review reads

| Layer | Where it lives | Rule | Checked by |
|-------|----------------|------|------------|
| Privacy policy | App Store Connect metadata and inside the app | Both places, easy to reach; the policy names the data collected, how and why, confirms third parties (analytics, ad networks, SDKs) give equal protection, and explains retention, deletion and how to revoke consent (5.1.1(i)) [Official, 2026-06] | Dossier; compliance reads the policy text |
| App Privacy answers | App Store Connect, App Privacy | Cover all data the app and its SDKs collect and match the live version [Official, 2026-10] (research pass) | SDK data map comparison (section 6) |
| Privacy manifest | `PrivacyInfo.xcprivacy` in the app and in each SDK bundle | Data collected, tracking domains, required reason APIs (section 2) [Official, 2026-10] | `submission_check.py`, Xcode privacy report |
| Purpose strings | `Info.plist` (or `INFOPLIST_KEY_` build settings) | One specific string per protected resource the app requests (section 4) [Official, 2026-10] | `submission_check.py` |
| Consent before collection | In the app | User or usage data needs consent even if anonymous; paid functionality never depends on granting data; an easy way to withdraw (5.1.1(ii)) [Official, 2026-06] | Release QA, compliance |
| Minimization | In the app | Ask only for data relevant to the core function; prefer out of process pickers and share sheets over full Photos or Contacts access (5.1.1(iii)) [Official, 2026-06] | Code review |
| No forced consent | In the app | No tricking or forcing; offer an alternative when the user declines (for example manual address entry instead of location) (5.1.1(iv)) [Official, 2026-06] | Release QA |
| Tracking | ATT framework | Explicit permission through ATT to track; no feature, content or reward may depend on enabling tracking, push or location (5.1.2(i)) [Official, 2026-06] | Section 7 |
| Third party AI | In the app | Disclose where personal data is shared with third parties, including third party AI, and obtain explicit permission before sharing (5.1.2(i)) [Official, 2026-06] | Section 10 |
| Account deletion | In the app | Section 8 | Dossier, release QA |

## 2. Privacy manifests

| Fact | Evidence |
|------|----------|
| The file is a property list named `PrivacyInfo.xcprivacy`, the required name for bundled manifests; in Xcode: File > New File > App Privacy | [Official, 2026-10] |
| Top level keys: `NSPrivacyTracking` (Boolean), `NSPrivacyTrackingDomains` (domains that engage in tracking; required when tracking is true), `NSPrivacyCollectedDataTypes`, `NSPrivacyAccessedAPITypes` | [Official, 2026-10] |
| If the user has not granted ATT permission, network requests to the declared tracking domains fail | [Official, 2026-10] |
| Add the manifest to the target's resources so Xcode includes it in the privacy report | [Official, 2026-10] |
| Each bundle with an executable or dynamic library that uses a required reason API carries its own manifest; an SDK cannot rely on the app's manifest | [Official, 2026-10] |
| SDKs on Apple's list must include a privacy manifest when a new app includes them or an update adds them; signatures are also required when they are binary dependencies; any version of a listed SDK and any SDK that repackages one is covered | [Official, 2026-10] |
| Xcode validates that a new version of a third party SDK was signed by the same developer | [Official, 2026-10] |
| The developer is responsible for all code an SDK brings into the app | [Official, 2026-10] |

Apple's list "SDKs that require a privacy manifest and signature" had 86 entries on 2026-10-12. The ones this repo meets most often: Capacitor, Cordova, Flutter, the Firebase modules (Core, Auth, Crashlytics, Firestore, Messaging, Remote Config, Installations and others), the Facebook SDK modules (FBSDKCoreKit, FBSDKLoginKit, FBSDKShareKit, FBAEMKit), GoogleSignIn, GoogleUtilities, GoogleDataTransport, OneSignal, Lottie, UnityFramework, Alamofire, SDWebImage, Kingfisher, RealmSwift, hermes (React Native), and Flutter plugins such as url_launcher, shared_preferences_ios, path_provider and share_plus [Official, 2026-10]. Re-read the list before each first submission; it changes without notice.

How to confirm a build: Xcode > Product > Archive > Generate Privacy Report reads every manifest in the app. A listed SDK with no manifest in the report means an outdated SDK version: update it before submission.

## 3. Required reason APIs

Since 2024-05-01, App Store Connect does not accept uploads that use a required reason API without an approved reason in the privacy manifest [Official, 2026-10]. Reasons must match the app's functionality as presented to users, and the APIs or derived data may never be used for tracking or fingerprinting [Official, 2026-10].

| Category (`NSPrivacyAccessedAPIType`) | Example APIs | Reasons most apps need |
|---------------------------------------|--------------|------------------------|
| `NSPrivacyAccessedAPICategoryUserDefaults` | `UserDefaults`, `NSUserDefaults` | `CA92.1` read and write data only the app itself can access; `1C8F.1` shared within the app's App Group |
| `NSPrivacyAccessedAPICategoryFileTimestamp` | `creationDate`, `modificationDate`, `fileModificationDate`, `contentModificationDateKey`, `creationDateKey`, `getattrlist`, `stat`, `fstat`, `lstat` | `C617.1` files inside the app container, app group or CloudKit container; `DDA9.1` timestamps shown to the user; `3B52.1` files the user granted access to |
| `NSPrivacyAccessedAPICategorySystemBootTime` | `systemUptime`, `mach_absolute_time()` | `35F9.1` elapsed time between in-app events and timers |
| `NSPrivacyAccessedAPICategoryDiskSpace` | `volumeAvailableCapacityKey`, `statfs`, `statvfs` and related keys | `E174.1` check there is space to write, or free space when low; `85F4.1` show disk space to the user |
| `NSPrivacyAccessedAPICategoryActiveKeyboards` | `activeInputModes` | `54BD.1` customized UI based on active keyboards; `3EC4.1` custom keyboard apps |

All codes [Official, 2026-10]. Reasons that only third party SDKs may declare (`0A2A.1`, `C56D.1`) are not for the app's own manifest.

Capacitor specifics, from the official plugin READMEs on npm (read 2026-10-12) [Official, 2026-10]:

| Package | What the app must do |
|---------|---------------------|
| `@capacitor/ios` 8.5.3 | Ships `PrivacyInfo.xcprivacy` files for the Capacitor and CapacitorCordova frameworks (both empty). The app still needs its own manifest for its own code and for plugins |
| `@capacitor/preferences` 8.0.1 | Add `NSPrivacyAccessedAPICategoryUserDefaults` with `CA92.1` to `PrivacyInfo.xcprivacy` in `ios/App` |
| `@capacitor/filesystem` 8.1.4 | Add `NSPrivacyAccessedAPICategoryFileTimestamp` with `C617.1` |
| `@capacitor/camera` 8.2.5 | Purpose strings `NSCameraUsageDescription`, `NSPhotoLibraryAddUsageDescription`, `NSPhotoLibraryUsageDescription` |
| `@capacitor/geolocation` 8.2.3 | `NSLocationWhenInUseUsageDescription` and `NSLocationAlwaysAndWhenInUseUsageDescription` (the second is required because a dependency can report background location; the same text may be used) |
| `@capacitor/barcode-scanner` 3.1.3 | `NSCameraUsageDescription` |
| `@capacitor/push-notifications` 8.1.3 | Enable the Push Notifications capability in Xcode |

`submission_check.py` knows these plugins and the five categories; other plugins and SDKs are read from their own documentation.

## 4. Purpose strings

Apple's guidance for 5.1.1(ii) [Official, 2026-10]:

| Do | Do not |
|----|--------|
| Name the specific feature or outcome the data makes possible | Restate the resource name ("To use location.") |
| Write a separate string for every protected resource requested | Hide behind a vague benefit or passive voice ("Your data will be used to provide a better experience.") |
| Give a concrete example of what the app does with the data | Fill the string with marketing copy or a feature list |
| One brief, complete sentence, active voice, sentence case, ending with a period | |
| Localize the strings for every supported localization and test each language | |

Apple's example of a clear string: "The app uses location data to determine the recommended route to your destination and provide turn-by-turn directions." [Official, 2026-10]. The app's name is shown by the system, so the string need not repeat it [Official, 2026-10].

The developer is responsible for strings SDKs need: if an SDK references a protected API the app has a reason to use, define the string; if not, remove the references from the binary [Official, 2026-10]. A required key that is missing either fails at runtime or at review: for ATT, the app crashes if it uses the framework without `NSUserTrackingUsageDescription` [Official, 2026-10]; for camera, location and photos the key "is required" when the app uses the APIs [Official, 2026-10].

Common keys (all from Apple's protected resources list [Official, 2026-10]):

| Feature | Key |
|---------|-----|
| Camera, including `getUserMedia` video in a web view and barcode scanning | `NSCameraUsageDescription` |
| Microphone, including `getUserMedia` audio and voice chat | `NSMicrophoneUsageDescription` |
| Photos read or picker with full access | `NSPhotoLibraryUsageDescription` (the system picker without full access needs none) |
| Save to photos only | `NSPhotoLibraryAddUsageDescription` |
| Location in the foreground, including `navigator.geolocation` in a web view | `NSLocationWhenInUseUsageDescription` |
| Location in the background | `NSLocationAlwaysAndWhenInUseUsageDescription` |
| Contacts | `NSContactsUsageDescription` |
| Calendars (iOS 17 and later) | `NSCalendarsFullAccessUsageDescription` or `NSCalendarsWriteOnlyAccessUsageDescription` |
| Tracking (ATT) | `NSUserTrackingUsageDescription`; in the EU a rich text variant `NSUserTrackingMarkdownUsageDescription` exists |
| Face ID | `NSFaceIDUsageDescription` |
| Bluetooth | `NSBluetoothAlwaysUsageDescription` |
| Local network (multiplayer discovery, casting) | `NSLocalNetworkUsageDescription` |
| Motion and fitness | `NSMotionUsageDescription` |
| Speech recognition | `NSSpeechRecognitionUsageDescription` |
| Game Center friends list | `NSGKFriendListUsageDescription` |

Timing: ask at the moment the feature needs it, after a sentence on screen that explains it, never on first launch for a feature the user has not reached [Practitioner consensus]. The ATT pre-prompt and its placement belong to `mobile-app-growth`; this agent checks that the prompt follows 5.1.2(i) and that nothing is withheld when the user declines.

## 5. Data minimization checks before submission

1. Every purpose string in the build maps to a feature the reviewer can reach; strings for unused resources are removed (the script reports them as INFO).
2. Photos use the system picker unless the feature needs the library; contacts use the contact picker unless the feature needs the store (5.1.1(iii)) [Official, 2026-06].
3. Registration asks only for what the core function needs; an app without significant account based features lets people use it without a login (5.1.1(v)) [Official, 2026-06].
4. Social network credentials can be revoked inside the app, and tokens are never stored off device (5.1.1(v)) [Official, 2026-06].

## 6. App Privacy answers matched to an SDK data map

App Privacy answers must cover every SDK's collection and match the version under review [Official, 2026-10] (research pass). Build the answers from the SDK data map in dossier section 9, never from memory.

1. List every SDK and version from `Podfile.lock`, `Package.resolved`, `package.json` (Capacitor plugins), `pubspec.lock` and Gradle files. Include SDKs pulled in by other SDKs.
2. For each SDK read its privacy manifest (`NSPrivacyCollectedDataTypes`), its privacy documentation and its configuration in the app (for example whether analytics collection or advertising identifiers are turned on).
3. Record per SDK: data types, linked to the user or not, used for tracking or not, purposes.
4. Generate the Xcode privacy report and compare: every data type in the report appears in the map.
5. Write the App Privacy answers from the map; save the date of the comparison in the dossier.
6. Hand the same map to the Google Play Data safety form ([Google Play declarations and data safety](google-play-declarations-and-data-safety.md)) so both stores tell the same story.
7. Repeat on every SDK addition, removal, major update or configuration change (ads turned on, crash reporting added). A changed SDK without a new comparison date is a FAIL in the audit.

Typical SDK rows (verify each SDK's current documentation; values vary by configuration) [Practitioner consensus]:

| SDK type | Data usually collected | Tracking |
|----------|------------------------|----------|
| Analytics (Firebase Analytics, Amplitude, Mixpanel) | Usage data, device identifiers, diagnostics | Only if combined with third party data or ads |
| Crash reporting (Crashlytics, Sentry) | Crash data, performance data, device identifiers | No |
| Ad mediation and networks (AdMob, AppLovin MAX) | Device identifiers, advertising data, coarse location, usage | Yes when IDFA is used |
| MMP (AppsFlyer, Adjust) | Device identifiers, purchases, usage | Yes with IDFA |
| Auth (Firebase Auth, Google Sign-In, Sign in with Apple) | Email, name, user ID | No |
| Payments and paywalls (StoreKit, RevenueCat) | Purchase history, user ID | No |
| Push (APNs direct, OneSignal, Firebase Messaging) | Device token, user ID, usage | Depends on the vendor's use |

## 7. App Tracking Transparency

| Rule | Evidence |
|------|----------|
| Tracking needs explicit permission through the ATT APIs | [Official, 2026-06] |
| No feature, content, use of the app or reward may require enabling tracking, push or location | [Official, 2026-06] |
| The purpose string is short and specific; the system shows the app name | [Official, 2026-10] |
| From iOS 27.2 and iPadOS 27.2 developers may use an alternative ATT system prompt in the EU; in Germany, France, Italy, Poland and Romania only the alternative prompt is available; when permission is needed does not change | [Official, 2026-09] |
| Requests to declared tracking domains fail without permission | [Official, 2026-10] |

Review checks: the prompt appears only where tracking starts; declining changes nothing for the user; no in-app copy offers a reward for allowing tracking; the App Privacy answers say "used to track you" for the data types involved. Copy for any pre-prompt goes through `compliance`.

## 8. Account deletion (5.1.1(v))

Apps that support account creation let people start account deletion inside the app [Official, 2026-06]. Apple's support page adds [Official, 2026-10]:

| Requirement | Detail |
|-------------|--------|
| Easy to find | Typically in account settings |
| Whole account | Delete the account record and associated personal data, including user generated content (photos, videos, text posts, reviews); only deactivating or disabling is insufficient; tell people what the law requires you to keep |
| Guest accounts | Automatically generated ("guest") accounts and their data can be deleted too |
| Sign in with Apple | Use the Sign in with Apple REST API to revoke user tokens; use server to server notifications; developers in the Republic of Korea provide a server to server notification endpoint when registering a new Services ID |
| Subscriptions | Tell the person billing continues through Apple and ask them to cancel first; link to subscription management (`showManageSubscriptions` on iOS 15 and later, or apps.apple.com/account/subscriptions); refunds through `beginRefundRequest` or Apple's support page; scheduling deletion for when the subscription ends is allowed only if immediate deletion is also offered |
| No support loops | Outside highly regulated industries, no phone call, email or chat support flow may be required |
| Timing | Manual or slower deletion is acceptable if the app says how long it takes and confirms when done; local law applies |
| Website step | If a website step is needed, link directly to the deletion page; sending people to the browser to sign in or register is not appropriate under Guideline 4, and deletion must still start in the app |
| Friction | Confirmation steps (reauthentication, a code) are allowed; making deletion unnecessarily difficult fails review |
| Everyone | Available to all users, not only those under CCPA or GDPR |

Review note line: "Account deletion: Settings > Account > Delete account. It deletes the account and its data immediately." The demo account must be able to see the button; App Review may test it, so give a second account if deletion would destroy the demo account (say so in the notes).

## 9. Sign in with Apple

| Item | Detail | Evidence |
|------|--------|----------|
| When it is needed | Guideline 4.8 ([Apple review checklist](apple-review-checklist.md) section 2) | [Official, 2026-06] |
| Entitlement | `com.apple.developer.applesignin`, added by enabling the Sign in with Apple capability in Xcode | [Official, 2026-10] |
| Token revocation on deletion | REST API, see section 8 | [Official, 2026-10] |
| Relay email domain | New private relay addresses use `private.icloud.com` instead of `privaterelay.appleid.com` (later in 2026); existing addresses keep working; account systems, email validation and allowlists must accept both | [Official, 2026-08] |
| Hide My Email | Stays on `icloud.com` | [Official, 2026-08] |

## 10. Third party AI and external services

1. Inventory every AI service the app sends personal data to (chat features, moderation, translation, image generation, support bots).
2. Before sharing, show what is sent and to whom, and get explicit permission (5.1.2(i)) [Official, 2026-06]; record the consent screen in the dossier.
3. List the AI service under external services in the review notes (Apple asks for external services such as data providers, authentication, payment processors and AI services) [Official, 2026-10].
4. Chatbots inside the app fall under 4.7 when they are software not embedded in the binary [Official, 2026-06]; the age rating should reflect what the AI can produce [Practitioner consensus].
5. `compliance` checks EU AI Act transparency duties for synthetic content.

## 11. Minors

| Rule | Evidence |
|------|----------|
| Apps for kids should not include third party analytics or advertising except as 1.3 allows; apps that collect personal information from a minor need a privacy policy and must follow children's privacy laws; the Kids Category parental gate is not the same as parental consent under those laws | [Official, 2026-06] |
| Outside the Kids Category, no name, subtitle, icon, screenshots or description may imply that children are the main audience | [Official, 2026-06] |
| Social media features disabled for under 13s need at least a Declared Age Range API check | [Official, 2026-10] |
| Texas SB 2420 applies to new Texas Apple Accounts from 2026-06-04; Brazil, Australia, Singapore, Utah and Louisiana age requirements have Declared Age Range API support (news 2026-02-24) | [Official, 2026-06] and [Official, 2026-02] |

Legal reading of minors rules belongs to `compliance`; this agent checks that the build, the age rating answers and the notes agree with the compliance verdict.

## 12. Pre-submission privacy checklist

- [ ] `submission_check.py` passes the purpose string and privacy manifest checks.
- [ ] Xcode privacy report generated for the archive; every listed SDK shows a manifest.
- [ ] SDK data map dated after the last SDK change; App Privacy answers re-compared.
- [ ] Privacy policy URL works in App Store Connect and inside the app; the policy matches the map.
- [ ] ATT: prompt only where tracking starts; no reward or gate; strings localized.
- [ ] Account deletion reachable from the demo account; subscription warning shown; Sign in with Apple tokens revoked server side.
- [ ] Third party AI disclosure and consent screen, if any, named in the notes.
- [ ] Kids, minors and age assurance answers match the compliance verdict.
