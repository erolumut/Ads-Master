# Rejections and Appeals

> Knowledge as of 2026-10. Apple's rules for replies, appeals, expedited review and Bug Fix Submissions were read at the source on 2026-10-12 to 2026-10-15 (App Review Guidelines "After You Submit" [Official, 2026-06]; App Review help pages [Official, 2026-10]). Google Play's appeal details come from search results of Play Console Help [Reported, 2026-10]. Every reply, appeal and expedite request is drafted by `store-submission` and sent by the human (G3). A rejection, removal or policy warning is a stop condition in `ads-master/INCIDENTS.md`.

## 1. Read the rejection before doing anything

1. Save the exact message, the guideline numbers cited, any screenshots or attachments, the submission id and the date to the journal (`YYYY-MM-DD_HHMM_store-submission_rejection-<app>.md`).
2. Look for the Bug Fix Submissions line at the top of an Apple message: "Bug Fix Submissions: The issues we've identified below are eligible to be resolved on your next update." [Official, 2026-10]. If it is there, read section 4 before resubmitting.
3. Split the message into issues. One message can cite several guidelines; each issue gets its own row.
4. Classify each issue:

| Class | Signs | Response |
|-------|-------|----------|
| Information missing | "We were unable to sign in", "we could not locate the in-app purchase", "please provide documentation" | Reply with the information or fix the demo account; resubmit only if the build must change |
| Metadata fix | 2.3.x, screenshots, name, other platforms, pricing words | Fix in App Store Connect; app-store-optimization drafts, compliance verdict |
| Binary fix | Crash, placeholder, purpose string, missing restore, missing deletion, missing Sign in with Apple, privacy manifest | App team fix; new build; dossier and script rerun |
| Business model | 3.1.1 external purchase, 3.1.2 subscription value, 4.3 spam | Decision with mobile-app-growth, game-monetization and the human |
| Misunderstanding | The reviewer describes the app incorrectly or missed a feature | Reply with steps and screenshots; appeal only if the reply does not resolve it |
| Policy dispute | The app follows the guideline as written and the reviewer reads it differently | Reply first, then an appeal citing the guideline point by point |

5. Write the root cause: why did the dossier and the script not catch it? Every rejection adds a check to the dossier template, the audit or the script (through a journal proposal to update the skill).

## 2. Options after an Apple rejection

| Option | When | Rules | Evidence |
|--------|------|-------|----------|
| Reply in App Store Connect | Questions, clarifications, extra information | Use App Store Connect to talk to App Review directly | [Official, 2026-06] |
| Fix and resubmit | The reviewer is right | Answer every cited issue in one build; describe the change in the notes (template F in [Review notes](review-notes-and-demo-accounts.md)) | [Practitioner consensus] |
| Bug Fix Submission | An update to an approved app, rejected with no legal or safety issue, with the eligibility line in the message | Section 4 | [Official, 2026-10] |
| Appeal to the App Review Board | You believe the app follows the guidelines and the reply did not resolve it, or treatment was unfair | Section 5 | [Official, 2026-10] |
| Expedited review | Critical bug fix or an event the app is directly tied to; only for submissions already sent | Section 6 | [Official, 2026-10] |
| App Review appointment | Unclear guideline reading for a future version | 30 minute video appointment | [Official, 2026-10] |
| Suggest a guideline change | The rule itself is unclear | Contact form | [Official, 2026-06] |

Never: resubmit the same build without a change hoping for another reviewer, create a new bundle or account to escape a rejection, hide a feature from the reviewer with a flag, or argue in the notes. Repeated rejections for the same guideline and attempts to manipulate review make later reviews take longer [Official, 2026-06].

## 3. Reply templates (Apple)

### Information provided

```text
Thank you for the review. The information is now in App Review Information:
- Demo account: <username> (password in the Password field). It never expires and the back end is live.
- <Expired subscription account: second account in the Notes.>
- To reach <feature>: 1. <step> 2. <step>.
No build change was needed, so we have not resubmitted the binary. Please let us know if anything else is missing.
```

### Clarification of a misunderstanding

```text
Thank you for the review under Guideline <number>. We think the app may have been seen differently from how it works:
- <Fact 1, with the screen and path.>
- <Fact 2.>
Screenshots of these screens are attached. If this does not address the concern, could you tell us which part of the guideline the app does not meet?
```

### Fix described

```text
We fixed the issue under Guideline <number> in build <build>:
- <What changed, where.>
To verify: 1. <step> 2. <step>.
```

Rules: one reply per issue thread, facts and steps only, attach screenshots of the exact screens, no promises about future builds, no blame. `compliance` reads any reply that makes a claim about the product or the law.

### 3.1 Reply to a 2.3.1(a) hidden features rejection

```text
Thank you for the review. The flagged item was <key name>, a remote configuration value used only by our Android build to <purpose>. The iOS app never read it. We have removed the key from the configuration the iOS app receives and removed <code, if any>; the app now behaves identically for every user. Reviewers can test the subscription with the sandbox and the demo account in App Review Information. The complete list of remote configuration keys the iOS app receives is: <list with one line each>. We are happy to share more detail.
```

Facts only, no argument. Resubmit only after the key is gone from what the iOS app actually fetches.

### 3.2 Account safety

Reports of terminated developer accounts and removed apps rise in waves [Reported, 2026-10, practitioner posts]. What keeps an account safe is the same discipline as a clean review:
1. One honest app per account: no hidden features, no switching the app's purpose after approval, no review detection (section 3.1, checklist section 6.1).
2. No ties to terminated accounts: shared payment details, devices, bank accounts or team members with a banned account are reported as a cause of linked terminations [Reported, 2026-10]; buying or borrowing accounts is out.
3. No copycat or template apps across accounts, no fake reviews or rating manipulation, no misleading metadata (2.3, 4.3, 5.6).
4. Answer Apple's messages in App Store Connect promptly, and keep the legal entity, contact details and agreements current.
5. If a termination notice arrives: do not open a new account; read the notice, gather the facts, and appeal through the stated channel with the human and counsel deciding (G4).

## 4. Bug Fix Submissions (Apple)

| Rule | Evidence |
|------|----------|
| Available only for updates to apps already approved for the App Store or alternative distribution | [Official, 2026-10] |
| The rejected update must introduce no legal or safety concerns | [Official, 2026-10] |
| The eligibility line appears at the top of the rejection message | [Official, 2026-10] |
| Reply to the message saying you want this submission approved and will fix the issues in the next update; do not resubmit, which starts a new review | [Official, 2026-10] |
| App Review replies to confirm and approve | [Official, 2026-10] |
| Every deferred issue must be fixed in the next update; App Review verifies each one | [Official, 2026-10] |
| An issue deferred once cannot be deferred again | [Official, 2026-10] |

Use it when the update fixes something users suffer from today. Log the deferred issues as a FAIL list in the next dossier so they cannot be forgotten.

## 5. Appeals to the App Review Board (Apple)

| Rule | Evidence |
|------|----------|
| Before appealing, reply to the rejection, removal or termination message in App Store Connect with clarification; appeal if that does not resolve it | [Official, 2026-10] |
| Appeal when the app was rejected or removed but follows the Guidelines and the License Agreement, when the account faces termination but complies, or when treatment seemed unfair or biased | [Official, 2026-10] |
| Do not appeal to reinstate an already terminated account, to get a status update or to request expedited review | [Official, 2026-10] |
| One appeal per rejected or removed app; if several guidelines are cited, address them all in that one appeal | [Official, 2026-10] |
| The form takes appeals for up to five rejected or removed apps | [Official, 2026-10] |
| Cite the specific guideline and explain point by point how the app meets it; add relevant information; leave out anything not relevant | [Official, 2026-10] |
| Do not appeal requests for information or documentation; do not appeal after you fixed and resubmitted | [Official, 2026-10] |
| The board messages in App Store Connect, may ask for more information or a call; a complete appeal does not guarantee a reversal | [Official, 2026-10] |

Appeal template:

```text
App: <name> (<Apple ID>), version <version> (<build>), submission <id>, rejected <date> under Guideline <number(s)>.
We replied in App Store Connect on <date> with <summary>; the issue remains.
Guideline <number> says: "<short quote>".
How the app meets it:
1. <Requirement part 1>: <how the app meets it; screen and path; screenshot attached>.
2. <Requirement part 2>: <same>.
<Second guideline cited, if any, handled the same way.>
Relevant context: <only what bears on the decision>.
```

Apple's own example of a complete appeal: the app was rejected under 2.1 for incomplete information, and the appeal points out that the demo account and setup steps are in App Review Information, with screenshots of the feature working [Official, 2026-10]. An incomplete appeal says the app is important to the business and asks for another look [Official, 2026-10].

## 6. Expedited review (Apple)

| Rule | Evidence |
|------|----------|
| Only submissions already sent to App Review can be expedited | [Official, 2026-10] |
| The app must be review ready: notes complete, demo account or demo mode | [Official, 2026-10] |
| Reserve it for genuine urgency; abuse can lead Apple to reject future requests | [Official, 2026-10] and [Official, 2026-06] |
| Critical bug fix: include the steps to reproduce the bug on the current version in the Notes | [Official, 2026-10] |
| Event: include the event, its date and the app's association with it in the Notes; schedule the release ahead where possible | [Official, 2026-10] |
| Granted subject to availability and demand; not guaranteed | [Official, 2026-10] |

Ads Master rule: an expedite request is G3 and is used for incidents (a crash or payment bug live for users, a security issue) or a dated event the app is part of. A marketing launch date is not an emergency; plan buffer instead.

## 7. Common rejections and fixes

| Cited | Usual cause | Fix | Prevented by |
|-------|-------------|-----|--------------|
| 2.1 (completeness) | Crash on the reviewer's device, placeholder screens, broken support or privacy link, back end off | Test on current iOS on device; open every URL on the day | Release QA; dossier section 6 |
| 2.1 (information) | Demo account expired or behind a code; no expired subscription account; paywall not found | Fix the account; add steps | Demo account checklist |
| 2.1(b) | Product not attached to the version or not visible | Attach in App Store Connect; explain hidden products | Payments checklist |
| 2.3.1(a) | Hidden features: review detection or a reviewer bypass, often a remote config key shared with Android | Remove the key and the code path, split config per platform, give reviewers a real account or a granted entitlement; reply with what was removed and offer the full key list | [Apple review checklist](apple-review-checklist.md) section 6.1 |
| 2.3.3, 2.3.4 | Splash or marketing art as screenshots; rendered trailer as a preview | Real UI captures; screen recorded previews | ASO workflow |
| 2.3.10 | "Get it on Google Play" badge or Android device in assets or in the web view | Remove from assets and the wrapped site | Wrapper checklist |
| 3.1.1 | Web checkout or a "buy on our website" link outside the US storefront; license key unlock | In-app purchase; link out only where allowed | Payments checklist |
| 3.1.2 | Billed amount not the most prominent price; trial terms missing; no Restore; no Terms link | Paywall checklist | Payments checklist |
| 4.2 | Wrapper looks like the website | Native value list; notes that show it | Wrapper checklist |
| 4.3 | Near identical app or template reskin | Real differences, or one app with variants | Portfolio check |
| 4.8 | Google or Facebook login without an equivalent | Add Sign in with Apple, or document the exception | `submission_check.py` |
| 5.1.1(i) | Privacy policy missing in the app or not covering SDK sharing | Link in settings; policy rewrite with compliance | Dossier section 3 |
| 5.1.1(ii) | Vague purpose string | Specific sentence per resource | `submission_check.py` |
| 5.1.1(v) | No in-app account deletion; deactivation only; guest accounts not deletable | Full deletion flow | Dossier section 3 |
| 5.1.2(i) | Tracking without ATT, rewards for allowing tracking, AI sharing without consent | Fix the flow; consent screen | Privacy checklist |
| Upload error for a missing required reason API | Privacy manifest without a category the code or an SDK uses (often reported as ITMS-91053) | Add the category with the right reason; update the SDK | `submission_check.py`; error code [Practitioner consensus] |

## 8. Google Play rejections and appeals

| Item | Detail | Evidence |
|------|--------|----------|
| Where | Policy status in Play Console and the email; each issue names the policy | [Reported, 2026-10] |
| Fix first | Most rejections are fixed by a new release with the change, or by correcting a declaration | [Practitioner consensus] |
| Appeal | Google offers an appeal form per policy issue | [Official] (mobile-app-growth module) |
| Termination appeal window | 180 days | [Reported, 2026-10] |
| Ban evasion | A new developer account during an appeal or suspension is treated as ban evasion | [Reported, 2026-10] |
| Repeated violations | Can lead to account termination | [Reported, 2026-10] |

Play appeal template:

```text
App: <name> (<package>), version code <code>, issue <policy name> on <date>.
What the policy requires: <one line>.
What the app does: <facts with paths; screenshots or a short video attached>.
What we changed, if anything: <change and release>.
We ask for <reinstatement, approval, or a specific explanation of what still does not comply>.
```

## 9. Logging and KPIs

Append one row per submission and per outcome to `ads-master/data/store_submissions.csv`:

`submitted_at, store, app, version, build, submission_type, outcome, guidelines_cited, repeat_of_previous (yes or no), reply_or_appeal, resolved_at, live_at, build_uploaded_at, notes_file`

- First pass approval rate = submissions approved with no rejection / submissions, per store, rolling 90 days.
- Days from build to live = `live_at` minus `build_uploaded_at`, median per store.
- Rejections by guideline = count per guideline per quarter.
- Repeat rejections = rejections citing a guideline already cited for the same app in the last 12 months; target zero. Each one gets a root cause note and a prevention change.
