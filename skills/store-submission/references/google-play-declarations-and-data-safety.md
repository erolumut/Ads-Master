# Google Play Declarations and Data Safety

> Knowledge as of 2026-10. The Data safety rule ("declare all collection and sharing, including SDKs; a mismatch triggers enforcement") was read on developer.android.com in the 2026-10-12 research pass [Official, 2026-10]. Most form details live in Play Console Help on support.google.com, which this environment could not open: those rows carry [Reported, 2026-10] or [Unverified] and the live Play Console wins. Consent law and copy verdicts belong to `compliance`; tag and SDK configuration to `measurement` and the app team.

## 1. The forms and what drives each answer

| Form (Play Console > Policy > App content) | What drives the answer | Source of truth in the workspace | Evidence |
|---------------------------------------------|------------------------|----------------------------------|----------|
| Privacy policy | A live URL; the policy matches the Data safety answers | Dossier section 3 | [Reported, 2026-10] |
| App access | Whether features sit behind sign in; instructions and credentials for reviewers | Dossier section 2 | [Unverified] (form name from long standing console use; confirm) |
| Ads | Any ad SDK or ad display in the app, including mediation and rewarded ads | Policy `storeDeclarations.containsAds` for games; SDK data map | [Reported, 2026-10] |
| Content rating | IARC questionnaire answers (violence, gambling and simulated gambling, user interaction, purchases, loot boxes) | Dossier section 5; compliance verdict | [Reported, 2026-10] |
| Target audience and content | Age groups the app targets; triggers the Families policy when children are included | Product brief; compliance verdict | [Reported, 2026-10] |
| Data safety | Every data type collected or shared by the app and its SDKs, purposes, security practices, deletion | SDK data map (dossier section 9) | [Official, 2026-10] |
| Account deletion | In-app path plus a web link entered in Data safety | Dossier section 3 | [Reported, 2026-10] |
| Government, financial features, health | Declarations when the app falls in the category | Product brief | [Reported, 2026-10]; health declaration [Official] (mobile-app-growth module) |
| Permission declarations | Sensitive permissions (exact alarm, foreground service types, broad media, call log, SMS, background location) | AndroidManifest.xml | [Official, 2026-10] |

## 2. Data safety from the SDK data map

The same map that feeds Apple's App Privacy answers ([Apple privacy and SDK requirements](apple-privacy-and-sdk-requirements.md) section 6) feeds Data safety. Steps:

1. List every Android dependency from Gradle (including transitive ones that collect data, such as ad mediation adapters).
2. For each SDK, read the vendor's Data safety guidance page (most large SDKs publish one) and the app's configuration of it.
3. Record per data type: collected or not, shared or not, processed ephemerally or not, required or optional, purposes.
4. Answer the security questions: data encrypted in transit; whether users can request deletion.
5. Write the form from the map; record the date in the dossier.
6. Compare with Apple's answers: the same SDK should not be "collected for analytics" on one store and absent on the other.
7. Repeat on every SDK change. A Data safety mismatch with the SDKs in the build is among the most reported causes of rejection and enforcement [Reported, 2026-10].

Data type groups and purposes as they appear in the form (confirm the current wording in the console) [Unverified]:

| Data type groups | Purposes |
|------------------|----------|
| Location; personal info; financial info; health and fitness; messages; photos and videos; audio files; files and docs; calendar; contacts; app activity; web browsing; app info and performance; device or other IDs | App functionality; analytics; developer communications; advertising or marketing; fraud prevention, security and compliance; personalization; account management |

Concept map between the stores (for writing both from one map) [Practitioner consensus]:

| Apple App Privacy | Google Play Data safety |
|-------------------|-------------------------|
| Data collected (by the app or partners) | Data collected |
| Data used to track you | Data shared (for advertising) plus the advertising purpose |
| Data linked to you | No direct equivalent; reflected in personal info and IDs |
| Purposes (analytics, app functionality, third party advertising and others) | Purposes (same idea, different names) |
| Not asked | Security practices (encryption in transit, deletion requests) |

## 3. Account deletion on Google Play

| Rule | Evidence |
|------|----------|
| Apps that let users create an account offer deletion inside the app and a web link where users can request deletion without reinstalling | [Reported, 2026-10] |
| The web link is entered in the Data safety form | [Reported, 2026-10] |
| Deactivation or a temporary disable does not count as deletion | [Reported, 2026-10] |
| Apple's in-app requirement is [Official]; building one flow that meets both stores is the default | [Official, 2026-10] (Apple) |

Web link page checklist: reachable without the app, identifies the app by name, explains what is deleted and what is kept (and why), lets the user request deletion of the account and data (or of data only), gives a time frame and a confirmation. `site-engineer` builds it; `compliance` reviews the retention wording.

## 4. Ads, audience and families

| Topic | Rule | Evidence |
|-------|------|----------|
| Contains ads | Declare yes when the app shows ads, including rewarded and house ads served through an ad SDK | [Reported, 2026-10] (scope of house ads [Unverified]) |
| Advertising ID | `AD_ID` permission for apps targeting Android 13 or later that use it | [Official] (mobile-app-growth module) |
| Child directed apps | Families policy; certified ad SDKs only | [Official, 2026-10] (research pass) |
| Anonymous chat | Since 2026-08-26 anonymous chat apps may not target children | [Official, 2026-10] (research pass) |
| Loot boxes | Odds before purchase, in close proximity to the purchase | [Reported, 2026-10] |
| Kids may play | If children may play the game, the audience form and Families rules apply | [Reported, 2026-10] |

For games with a `monetization-policy.json`, run `submission_check.py --policy`: it fails when the dossier's "Contains ads", "In-app purchases", "Auto-renewable subscriptions" or "Paid random items" answer disagrees with `storeDeclarations` and the catalog. The Play forms are then written from the dossier.

## 5. Content rating (IARC)

| Step | Detail |
|------|--------|
| 1 | Answer the questionnaire from the build, not the plan: violence, fear, sexual content, language, controlled substances, gambling and simulated gambling, user interaction (chat, UGC), sharing location, digital purchases, paid random items [Reported, 2026-10] |
| 2 | Use the same facts as the Apple age rating answers; the resulting ratings may differ by region and authority |
| 3 | Record the ratings per region in the dossier |
| 4 | Re-answer when a feature changes an answer (chat added, loot boxes added, ads added) |
| 5 | PEGI: new games with paid random items default to PEGI 16 from 2026-06-01 [Reported, 2026-10] |

A wrong rating answer is a policy violation, not a cosmetic error [Practitioner consensus]: route any doubt to `compliance` before submitting.

## 6. Subscriptions on Google Play

| Rule | Evidence |
|------|----------|
| Disclose the offer: terms, price, billing frequency, auto renewal and how a trial converts, without extra steps | [Reported, 2026-10] |
| Explain how to manage and cancel; online cancellation is easy | [Reported, 2026-10] |
| Cancellation keeps access until the end of the paid period | [Official, 2026-10] |
| Support restore and resubscribe | [Official, 2026-10] |
| A free trial charges the full price at its end; people who already used a trial lose trial eligibility | [Official, 2026-10] |

## 7. Permissions and their declarations

Remove what the app does not need first; declare what remains.

| Permission | Declaration or alternative | Evidence |
|------------|---------------------------|----------|
| Exact alarms | `USE_EXACT_ALARM` only for alarm or calendar apps | [Official, 2026-10] |
| Foreground services (Android 14+) | Service types in the manifest and the Play Console declaration; `specialUse` with a justification | [Official, 2026-10] |
| Photos and videos | Photo picker | [Official, 2026-10] |
| Contacts, location | Contact picker; location button | [Official, 2026-10] |
| Call log | Not for verification uses from 2027-01-27 | [Official, 2026-10] |
| Any other sensitive permission (background location, SMS, all files access) | Read its Play policy page before the submission; the 2026-10 research pass did not cover them | [Unverified] |

Some declaration forms ask for a short video or description of the feature [Unverified]; record what was sent in the dossier.

## 8. Mismatch triggers and fixes

| Trigger | Typical cause | Fix |
|---------|---------------|-----|
| Data safety mismatch | New SDK or SDK update; ads turned on; crash reporting added | Update the map, the form and the privacy policy together |
| Privacy policy unreachable | Moved page, a 404, a login wall, a PDF that does not load | Stable public URL; check on the submission day |
| Account deletion missing | Accounts added in an update without deletion; no web link | Ship deletion and the web link before the update that adds accounts |
| Permission rejected | Broad permission for a narrow use | Use the picker or narrow API; remove the permission |
| Ads declaration wrong | Rewarded ads added by a new placement | Policy file and dossier updated in the same change |
| Content rating changed by Google | Answers did not match observed content | Re-answer with `compliance`; never argue against observed content |

## 9. Pre-submission declarations checklist

- [ ] SDK data map dated after the last dependency change; Data safety and App Privacy written from it.
- [ ] Privacy policy URL live, public, consistent with both forms.
- [ ] Account deletion: in-app path and web link; the link entered in Data safety.
- [ ] Ads, in-app purchases, subscriptions and random items answered the same in the dossier, the policy file and both stores.
- [ ] IARC answers match Apple's age rating facts; ratings recorded.
- [ ] Target audience and Families decisions match the compliance verdict.
- [ ] Every sensitive permission removed or declared.
- [ ] App access instructions and the demo account ready when sign in is required.
