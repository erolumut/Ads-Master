# Submission Dossier: <app name> <version (build)>

> Template source for `ads-master/SUBMISSION.md`, the dossier `store-submission` builds before every App Store or Google Play submission. Knowledge as of 2026-10. Copy this file, fill every `<...>` value, then run `python3 -I <skill>/scripts/submission_check.py <project> --dossier ads-master/SUBMISSION.md` (add `--policy ads-master/data/monetization-policy.json` for games). A FAIL blocks the submission; a WARN needs a named person to accept it in section 11. Pressing submit is a G3 human action.
>
> Rules for this file: one dossier per submission. Archive the previous one as `ads-master/outputs/store-submission/YYYY-MM-DD_store-submission_dossier-<version>.md` before you overwrite it. Never write a password, token, private key, `.p8` file content or service account JSON here: name the password manager entry instead. Facts come from the build, the consoles and `ads-master/brand/PRODUCT_FACTS.md`; nothing is guessed.
>
> The checker reads lines shaped `- Key: value`. Keep the key text exactly as written; write the answer after the colon. Answers that start with `yes`, `no` or `n/a` are read as such. Anything in angle brackets counts as unfilled.

## 1. Submission

- Store: <apple, google or both>
- App name: <exactly as in App Store Connect and Play Console>
- Bundle ID and package name: <com.example.app (iOS), com.example.app (Android)>
- Version and build: <for example 1.4.0 (212)>
- Submission type: <first submission, update, or resubmission after rejection>
- Planned submission date: <YYYY-MM-DD>
- Built with: <Xcode and iOS SDK version; Android targetSdk; Capacitor, Bubblewrap or engine version>
- What changed since the last approved version: <one line per user visible change, or first version>
- Previous rejection to answer: <submission id, guideline and date, or none>
- Person who presses submit (G3): <name>

## 2. Review access (Apple 2.1, Google Play App access)

> App Review needs full access. Credentials that expire or change before the review starts can get the build rejected. If the app has account types (player and admin, two players for multiplayer), list each one. If a one time code is needed, give the reviewer a way past it in the notes; otherwise Apple may need a call, which takes days.

- Features behind sign in: <yes or no>
- Demo account username: <reviewer login, for example review@yourdomain.example, or n/a>
- Demo account password stored in: <password manager entry name; never the password itself>
- Demo account never expires: <yes>
- Expired subscription demo account: <username of an account whose subscription has lapsed, or n/a without auto-renewable subscriptions>
- Extra account types: <second player, admin, teacher, or none>
- One time codes or two factor sign in: <how the reviewer gets past them, or none>
- Demo mode instead of an account: <no, or yes with the date Apple approved it>
- Backend live during review: <yes, or n/a when the app has no backend>
- Server side feature flags for review: <none, or which flags and that they match production>
- Remote config keys read by hand: <yes: date, and no review detection, bypass or other platform only keys>
- Region or hardware needs: <none, or what the reviewer needs and how it is provided>
- Walk-through video attached: <yes: file name, build number and date recorded; Apple only>
- AI features: <none, or what the AI does, which service, and where the app asks before sending personal data>

## 3. Accounts, privacy and support

> Guest accounts that the app creates on its own count as account creation: they need a deletion path too. Deactivation alone is not deletion.

- Account creation: <yes or no>
- Account deletion path in app: <for example Settings > Account > Delete account, or n/a>
- Account deletion web link: <https URL where people can request deletion without the app (Google Play), or n/a>
- Deletion time told to the user: <for example immediately, or within 30 days with a confirmation email>
- Sign in with Apple: <offered, or not required because (name the Guideline 4.8 exception)>
- Social logins offered: <Google, Facebook, other, or none>
- Privacy policy URL: <https URL>
- Privacy policy link in app: <where in the app, for example Settings > Privacy>
- Terms of use URL: <https URL; required with auto-renewable subscriptions, or n/a>
- Support URL: <https URL with real contact information>
- Contact for App Review: <name, email, phone with +country code>
- Tracking (ATT): <no, or yes with the screen where the prompt appears>
- Third party AI sharing: <none, or provider, data sent, and the consent screen>
- User generated content controls: <filter, report, block and published contact, or n/a>

## 4. Money

> Restore is needed for restorable purchases (non consumables, subscriptions, season passes). An app that sells only consumables may answer n/a and say so.

- In-app purchases: <yes or no>
- Auto-renewable subscriptions: <yes or no>
- Restore purchases path: <where the Restore or Sign in button is, or n/a when every product is a consumable>
- Paywall disclosures checked: <yes: name, duration, content, full renewal price as the most prominent price, trial length and price after, Restore, Terms and Privacy links>
- In-app purchases attached to this version: <yes, all products Ready to Submit and added to the version, or n/a>
- Paid random items: <yes or no>
- Odds shown before purchase at: <screen and route, or n/a>
- Virtual currency shows real money price: <yes, or n/a>
- External purchase links: <none, or storefronts, entitlement or program, and the screen>
- Web purchases honoured in the app: <no, or yes and the same items are also sold as in-app purchases (Guideline 3.1.3(b))>
- Contains ads: <yes or no>
- Paywall and pricing copy compliance verdict: <journal entry or output file from compliance>

## 5. Platform forms

- Age rating questionnaire answered: <yes, date, resulting rating per store>
- Social media question answered: <yes, and the capability answer (Apple, required since 2026-09)>
- IARC questionnaire answered: <yes, date and ratings (Google Play), or n/a>
- Export compliance answered: <yes: ITSAppUsesNonExemptEncryption NO, or YES with documentation code>
- EU DSA trader status: <trader verified, or non trader declared, with date>
- App Privacy answers match the SDK data map: <yes, date of the last comparison>
- Data safety form matches the SDK data map: <yes, date of the last comparison, or n/a>
- Content rights: <we own or license all content; documents attached for third party content>
- Regulated documents attached: <none, or licenses and clearances by storefront>
- Screenshots uploaded: <iPhone with Dynamic Island 1179 x 2556 or 1206 x 2622; iPad 13 inch 2064 x 2752 or 2048 x 2732 when the app runs on iPad; Play phone and tablet>
- Medical device status: <not a medical device, or declared status>

## 6. Design and content

- Native value beyond the website: <for wrappers: the native features a reviewer can see, or n/a for a native app>
- HTML5 mini games or mini apps inside the app: <no, or yes with the Guideline 4.7 controls>
- Placeholder content removed: <yes>
- All links work: <yes, checked on date>
- iPad layout usable: <yes, or n/a when the app is iPhone only>
- Kids Category or Families: <no, or which program and its rules checked>

## 7. Google Play only

- Developer account type: <personal created after 2023-11-13, older personal, or organization>
- Closed test: <12 or more testers opted in for the last 14 continuous days, finished YYYY-MM-DD, or not required>
- Target API level: <36>
- Play Billing Library version: <8 or later, or n/a>
- App signing: <Play App Signing enrolled, upload key fingerprint recorded>
- Digital Asset Links verified: <yes for TWA with the app signing fingerprint, or n/a>
- Permissions declared in Play Console: <none needed, or which declaration forms are filled>
- Android vitals last 28 days: <user perceived crash rate and ANR rate, or new app>
- Developer verification: <done, or not yet required for this account and market>

## 8. Review notes (paste into App Store Connect, App Review Information, Notes)

> Up to 4,000 bytes. Plain sentences, numbered steps. Say what the app is, who it is for, how to sign in, what to tap, where purchases and their Restore button are, where account deletion is, and what native features a wrapper offers. Use the templates in review-notes-and-demo-accounts.md. Write the text between the two fence lines; the guidance lines starting with the quote mark are not pasted.

```text
<What the app is and who it is for, in two sentences.>
<How to sign in: use the demo account in the App Review Information fields; it never expires and the backend is live.>
<How to test: 1. ... 2. ... 3. ...>
<Purchases: where the paywall is, which products, where Restore is.>
<Account deletion: the path in the app.>
<AI: "The app has no AI features." or what the AI does and which service.>
<Walk-through: "A walk-through video of this build is attached.">
<Anything that is hard to find, regional differences, or hardware needs.>
```

## 9. SDK data map

> One row per SDK in the build (from Podfile.lock, Package.resolved, package.json, Gradle). App Privacy answers and the Data safety form are written from this table, and a new SDK means a new row and a new comparison date. The checker does not read this table; the human and `store-submission` compare it with the consoles.

| SDK and version | Purpose | Data collected | Linked to the user | Used for tracking | Shared with third parties | Apple privacy manifest in the SDK | Data safety category |
|-----------------|---------|----------------|--------------------|-------------------|---------------------------|-----------------------------------|----------------------|
| <name 1.2.3> | <analytics, ads, crash, payments, auth, push> | <identifiers, usage, purchases, diagnostics> | <yes or no> | <yes or no> | <yes or no, with whom> | <yes, no, not on Apple's list> | <category> |

## 10. Checks run

- submission_check.py result: <exit code and date; paste the FAIL and WARN lines below if any>
- Store text compliance verdict: <journal entry or output file>
- Release QA by site-engineer: <for wrappers and web backed apps: result and date>
- Tested on devices: <device models and OS versions>
- TestFlight or internal test build: <build number and date, or n/a>

## 11. Accepted warnings and approval

> Each WARN that stays open is written here with the reason and the person who accepts it. A FAIL is never accepted here; it is fixed.

| Warning | Why it is acceptable | Accepted by | Date |
|---------|----------------------|-------------|------|
| <WARN line> | <reason> | <name> | <YYYY-MM-DD> |

- Approved to submit by: <name and date (G3)>
- Submitted at: <timestamp, filled after the human submits>
- Review outcome: <approved, rejected with guideline, or pending>
