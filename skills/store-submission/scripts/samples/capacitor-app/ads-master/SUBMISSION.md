# Submission Dossier: Daily Puzzle 1.4.0 (212)

> Filled fixture for submission_check.py tests, built from references/submission-dossier-template.md. Every value is invented for the test.

## 1. Submission

- Store: both
- App name: Daily Puzzle
- Bundle ID and package name: app.example.puzzle (iOS), app.example.puzzle (Android)
- Version and build: 1.4.0 (212)
- Submission type: update
- Planned submission date: 2026-10-20
- Built with: Xcode 26, iOS 26 SDK; targetSdk 36; Capacitor 8.5.3
- What changed since the last approved version: avatar photo, puzzle clubs near you
- Previous rejection to answer: none
- Person who presses submit (G3): Product owner

## 2. Review access (Apple 2.1, Google Play App access)

- Features behind sign in: yes
- Demo account username: review@puzzle.example
- Demo account password stored in: password manager entry "App Review demo account"
- Demo account never expires: yes
- Expired subscription demo account: lapsed@puzzle.example (same password manager folder)
- Extra account types: none
- One time codes or two factor sign in: none
- Demo mode instead of an account: no
- Backend live during review: yes
- Server side feature flags for review: none
- Region or hardware needs: none

## 3. Accounts, privacy and support

- Account creation: yes
- Account deletion path in app: Settings > Account > Delete account
- Account deletion web link: https://puzzle.example/account/delete
- Deletion time told to the user: immediately, with a confirmation screen
- Sign in with Apple: offered next to Google sign in
- Social logins offered: Google
- Privacy policy URL: https://puzzle.example/privacy
- Privacy policy link in app: Settings > Privacy policy
- Terms of use URL: https://puzzle.example/terms
- Support URL: https://puzzle.example/support
- Contact for App Review: Review contact, review@puzzle.example, +31 20 000 0000
- Tracking (ATT): no
- Third party AI sharing: none
- User generated content controls: n/a

## 4. Money

- In-app purchases: yes
- Auto-renewable subscriptions: yes
- Restore purchases path: Paywall > Restore purchases, and Settings > Restore purchases
- Paywall disclosures checked: yes
- In-app purchases attached to this version: yes
- Paid random items: no
- Odds shown before purchase at: n/a
- Virtual currency shows real money price: n/a
- External purchase links: none
- Web purchases honoured in the app: no
- Contains ads: no
- Paywall and pricing copy compliance verdict: compliance output 2026-10-14

## 5. Platform forms

- Age rating questionnaire answered: yes, 2026-10-14, 4+ on Apple, PEGI 3 on Google Play
- Social media question answered: yes, no social media capability
- IARC questionnaire answered: yes, 2026-10-14
- Export compliance answered: yes, ITSAppUsesNonExemptEncryption NO
- EU DSA trader status: trader verified 2026-03-02
- App Privacy answers match the SDK data map: yes, 2026-10-14
- Data safety form matches the SDK data map: yes, 2026-10-14
- Content rights: we own all content
- Regulated documents attached: none
- Screenshots uploaded: iPhone 1206 x 2622, iPad 2064 x 2752, Play phone and tablet
- Medical device status: not a medical device

## 8. Review notes (paste into App Store Connect, App Review Information, Notes)

> Guidance lines are not pasted.

```text
Daily Puzzle is a daily logic puzzle for adults: one new puzzle every day, solved alone or compared with friends.
Sign in with the demo account in the App Review Information fields. It never expires and the backend is live.
How to test: 1. Sign in. 2. Tap Play to solve today's puzzle. 3. Open Profile and tap the avatar to take a photo.
4. Open Clubs to see puzzle clubs near you (location is asked only on this screen).
Purchases: the Plus subscription is on the paywall from Profile > Plus. Restore purchases is on the paywall and in Settings.
The second demo account in the notes field has an expired subscription so you can review the full purchase flow.
Account deletion: Settings > Account > Delete account.
```

## 9. SDK data map

| SDK and version | Purpose | Data collected | Linked to the user | Used for tracking | Shared with third parties | Apple privacy manifest in the SDK | Data safety category |
|-----------------|---------|----------------|--------------------|-------------------|---------------------------|-----------------------------------|----------------------|
| Capacitor 8.5.3 | runtime | none | no | no | no | yes | none |
| Firebase Authentication 12 | sign in | email, user id | yes | no | no | yes | personal info, app activity |

## 11. Accepted warnings and approval

- Approved to submit by: Product owner, 2026-10-19
