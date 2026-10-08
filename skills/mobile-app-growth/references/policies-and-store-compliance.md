# Policies and Store Compliance for App Growth

> Knowledge as of 2026-10. This module lists the rules that most often block growth work. It is not legal advice; route claims, consumer law and privacy questions to the compliance agent. App Review Guidelines and Google Play policies change several times a year (Apple updates on 2025-05-01, 2025-06-09, 2025-11-13, 2026-02-06, 2026-06-08; Google policy updates monthly). Read the current text before any submission plan.

## 1. Apple App Review Guidelines that affect growth

| Guideline | What it means for growth work | Evidence |
|-----------|-------------------------------|----------|
| 1.2 User generated content | Apps with UGC need filtering, reporting and blocking; random or anonymous chat apps fall under 1.2 (2026-02) | [Official, 2026-02] |
| 1.2.1(a) Creator content | Creator apps need an age restriction mechanism (2025-11) | [Official, 2025-11] |
| 2.3 Accurate metadata | Screenshots must show the app in use (2.3.3); no irrelevant keywords, competitor names or pricing terms in metadata (2.3.7); metadata must match the app | [Official] |
| 3.1.1 In-App Purchase | Digital goods and features unlocked in the app use IAP, except where 3.1.1(a) and regional rules allow other routes | [Official] |
| 3.1.1(a) and 3.1.3 (US storefront) | No prohibition on buttons, external links or other calls to action to web purchases on the US storefront; no entitlement needed; alternative payment processing inside the app still not allowed (updated 2025-05-01) | [Official, 2025-05] |
| 3.1.2 Subscriptions | Clear description of what the user gets, price, period and renewal; the billed amount must be clear and prominent; subscriptions must provide ongoing value | [Official] |
| 3.1.3(a) Reader apps | Reader apps may link to an external account management site with the entitlement in markets outside the US rules | [Official] |
| 3.2.1(viii) Financial apps | Lending and financial services apps need licensing and must be submitted by the institution or an approved developer (clarified 2025-06) | [Official, 2025-06] |
| 4.7 Mini apps, HTML5 and JavaScript games, chatbots | Covered by 4.7 since 2025-11; Mini Apps Partner Program at 15% commission requires Declared Age Range API and Advanced Commerce API | [Official, 2025-11] |
| 4.8 Login services | Offer an equivalent privacy focused login (for example Sign in with Apple) when third party login is offered | [Official] |
| 5.1.1 Data collection | Purpose strings, data minimization, in-app account deletion for apps with account creation (5.1.1(v)); do not force consent for unnecessary data | [Official] |
| 5.1.2 Data use and sharing | Tracking requires ATT permission; disclose sharing personal data with third party AI (5.1.2(i), 2025-11) | [Official, 2025-11] |
| 5.6.1 App Store reviews | Use the provided API to request reviews; no custom review prompts | [Official] |
| 5.6.3 Discovery fraud | No manipulation of charts, search, reviews or referrals (no bought installs, review farms, incentivized rank boosting) | [Official] |

Other Apple requirements:
- Age ratings: new tiers 13+, 16+, 18+ plus 4+ and 9+; questions had to be answered by 2026-01-31 [Official, 2025-07]. From 2026-09 the questionnaire requires a declaration of social media capabilities (apps with them get at least 13+ unless features are disabled for under 13s with the Declared Age Range API) [Official, 2026-07].
- Age assurance laws: Texas SB2420 in effect for new Texas Apple Accounts from 2026-06-04 using the Declared Age Range API, Significant Change API and a revocation server notification (after a court injunction paused it in 2025-12) [Official, 2026-06]; age requirements for Brazil, Australia, Singapore, Utah and Louisiana with Declared Age Range API updates (beta 2026-02) [Official, 2026-02]; Australia social media under 16 account ban from 2025-12-10 [Official, 2025-12]. Hand legal interpretation to compliance.
- Privacy: privacy nutrition labels, privacy manifests and required reason API declarations (enforced from 2024-05-01) [Official].
- EU: trader status required under the Digital Services Act; apps without it were removed from the EU App Store from 2025-02-17 [Official, 2025-02].
- Regulated medical devices: new qualifying apps in the EEA, UK and US must declare regulated medical device status; existing apps must declare by early 2027 or lose the ability to update [Official, 2026-03].
- Gambling in Brazil: a valid SPA license is required; answering yes to gambling sets the Brazil rating to A18 [Official, 2026-05].
- SDK minimums: uploads need the iOS 26 SDK from 2026-04-28 and the iOS 27 SDK from April 2027 [Official].
- New device: iPhone Duo screenshots required for submissions from April 2027 [Official, 2026-10].
- China storefront commission 25% and 12% from 2026-03-15 [Official].

## 2. Google Play policies that affect growth

| Policy | What it means | Evidence |
|--------|---------------|----------|
| Metadata policy | No ranking or performance claims, price or promotion words, emoji or repeated special characters in title, icon or developer name; no misleading or irrelevant keywords | [Official] |
| Store listing and promotion | No fake or incentivized ratings and reviews, no misleading ads for the app, no deceptive install tactics | [Official] |
| Payments | Digital goods through Play Billing, or alternative billing and external links under the US, UK and EEA programs | [Official, 2025-12 to 2026-06] |
| Subscriptions | Clear offer terms: trial length, price after trial, frequency, cancellation; no misleading free trial claims | [Official] |
| User data and Data safety section | Accurate declarations of collection, sharing and security; mismatches are enforcement triggers | [Official] |
| Advertising ID | Apps targeting Android 13+ must declare AD_ID permission to use it; Families apps restricted | [Official] |
| Families | Child directed apps follow Families policy and certified ad SDK rules | [Official] |
| Financial services and personal loans | Disclosures and licensing; stricter rules in several countries | [Official] |
| Health apps declaration | Health apps must complete the declaration | [Official] |
| Generative AI apps | Must prevent and allow reporting of restricted content | [Official] |
| Account deletion | Apps with accounts must offer in-app and web account deletion | [Official] |
| Target API | API 36 for new apps and updates since 2026-08-31 (extension to 2026-11-01) | [Official, 2026] |
| Developer verification | Required for installs on certified devices in Brazil, Indonesia, Singapore and Thailand from 2026-09-30; global 2027 | [Official, 2026] |
| Android vitals | Bad behavior thresholds can reduce visibility | [Official] |

## 3. Ad platform rules for app promotion

| Platform | Watch for |
|----------|-----------|
| Google Ads App campaigns | Misrepresentation (fake gameplay, fake system messages), unreliable claims, destination requirements (deep links must work), Families and personalized ads restrictions |
| Meta | Prohibited and restricted content by category (dating, financial, health, gambling), personal attributes language ("Are you depressed?"), misleading claims, before and after rules |
| TikTok | Category restrictions by market, misleading claims, AIGC labeling |
| Apple Ads | Ads use App Store metadata and approved assets; trademark complaints process for keyword bidding; ads are not shown to children and personalized ads are restricted for minors [Official, verify current Apple Ads policy] |
| Ad networks | Network specific creative rules (no fake close buttons, playable content must match the app) |

## 4. Consumer protection themes (hand to compliance)

- Subscriptions and auto renewal: disclose terms before payment, confirm after, easy cancellation. US state automatic renewal laws apply; the FTC Negative Option ("click to cancel") rule was vacated in 2025 [Practitioner consensus, verify status with compliance].
- Fake reviews: the US FTC rule (effective 2024-10) bans buying or selling fake reviews and suppressing negative reviews [Official].
- Price reductions: EU and Turkey reference price rules apply to "was" prices in ads and store promotional text (EU 30 days, Turkey 10 days per the compliance package).
- Dark patterns in paywalls and cancellation: regulators in the EU (DSA, consumer law) and US target them; avoid confirmshaming, hidden close buttons and pre-checked upsells.
- Data and consent: GDPR, ePrivacy, KVKK and US state privacy laws govern SDK data collection independent of ATT.

## 5. Pre-submission checklist for growth changes

- [ ] Metadata and screenshots reviewed against 2.3 (Apple) and the Metadata policy (Google).
- [ ] Every claim in screenshots, CPPs, in-app events, promotional text and ads exists in brand/CLAIMS.md as approved.
- [ ] Paywall shows billed amount, period, trial terms, restore, terms and privacy links.
- [ ] External purchase links only on storefronts where they are allowed, with the right program enrollment (Google) and current fee assumptions.
- [ ] ATT prompt and pre-prompt follow 5.1.1 and 5.1.2; EU alternative prompt copy ready for iOS 27.2.
- [ ] Age rating answers current, including the social media capability question.
- [ ] Privacy labels and Data safety section updated for new SDKs (MMP, paywall, analytics).
- [ ] Deep links tested on the QA matrix.
- [ ] Category specific requirements (finance licensing, health declaration, medical device status, gambling licenses) checked.
- [ ] Submission scheduled outside holiday review slowdowns; Apple and Google review times vary.

## 6. When the app is rejected or a policy strike arrives

1. Read the exact guideline or policy cited and the reviewer message; save it to the journal.
2. Classify: metadata fix, binary fix, business model issue, or misunderstanding.
3. Fix the minimal thing; reply in Resolution Center (Apple) or the Play Console policy inbox with evidence.
4. Appeal only with a clear argument; Apple offers an App Review Board appeal; Google offers an appeal form per policy issue.
5. Never create a new developer account, rename the app or use another bundle to evade enforcement. That escalates to account termination.
6. Log the incident and the fix in INCIDENTS.md and update this skill through the journal if the rule changed.

## 7. Category quick rules (route details to compliance)

| Category | Store rules to check | Ad platform rules to check |
|----------|----------------------|----------------------------|
| Finance, lending, trading, crypto | Apple 3.2.1(viii) licensing and submitting entity; Google Financial services policy (personal loan disclosures, country specific rules) | Google financial services verification by country, Meta special ad category rules where applicable (credit in some markets), TikTok financial restrictions |
| Health, fitness, medical | Medical device declaration (EEA, UK, US) [Official, 2026-03]; health claims in metadata; Google Health apps declaration | Personal health attribute language bans (Meta), health claim restrictions by market |
| Dating and social | 1.2 UGC rules, random chat apps (2026-02), social media capability age question (2026-09), Australia under 16 rules | Dating ads approvals on Google and Meta, age targeting minimums |
| Gambling and real money games | Licenses per market (Brazil SPA license from 2026-05), age rating 17+ or 18+ | Platform certification per country, strict geo targeting |
| Kids and families | Kids Category rules (Apple), Families policy (Google), no third party analytics or ads without compliance | Child directed ad restrictions, no personalized ads |
| VPN, security, cleaner utilities | Accurate functionality claims, no fake system warnings | Misrepresentation and fake alert bans |
| AI apps and chatbots | 4.7 coverage for chatbots, 5.1.2(i) third party AI data sharing disclosure, age rating considers AI features | AI disclosure rules for synthetic media (EU AI Act transparency from 2026-08-02) |

## 8. Age assurance and minors: status table (as of 2026-10)

| Jurisdiction | Requirement | Platform tooling | Evidence |
|--------------|-------------|------------------|----------|
| Texas (SB2420) | Age assurance and parental consent for app distribution; in effect for new Texas Apple Accounts from 2026-06-04 after a 2025-12 injunction pause | Declared Age Range API, Significant Change API, revocation notifications | [Official, 2026-06] |
| Utah, Louisiana | App store age requirements | Declared Age Range API updates (beta 2026-02) | [Official, 2026-02] |
| Australia | Social media platforms must prevent under 16 accounts (from 2025-12-10); age rating 15+ replaced by 16+ (2026-06-18) | Declared Age Range API | [Official, 2025-12 and 2026-05] |
| Brazil, Singapore | Age requirements for apps | Declared Age Range API | [Official, 2026-02] |
| South Korea | GRAC rating overrides; two descriptors move from All to 12+ from 2026-10 | App Store Connect age rating settings | [Official, 2026-08] |
| Vietnam | Region specific ratings 00+, 12+, 16+, 18+; games need a license | App Store Connect | [Official, 2026-05] |

Implications for growth: age gates change funnel conversion and audience eligibility; plan onboarding and paid targeting around them and never target minors with restricted categories.

## 9. SDK and privacy declaration map

| SDK type | Apple privacy label and manifest | Google Data safety |
|----------|----------------------------------|--------------------|
| MMP (AppsFlyer, Adjust, Branch, Singular, Kochava) | Device ID, usage data, purchases; tracking domains declared; ATT gating for IDFA | Device or other IDs, app activity, purchase history; shared with third parties |
| Ad network and mediation SDKs | Tracking, advertising data; tracking domains | Advertising, device IDs, shared |
| Paywall and subscription SDKs (RevenueCat, Superwall, Adapty) | Purchases, identifiers linked to user if accounts exist | Purchase history |
| Analytics (Firebase, Amplitude, Mixpanel) | Usage data, diagnostics | App activity, diagnostics |
| Crash reporting | Diagnostics | Crash logs |

Re-check declarations every time an SDK is added, removed or updated; mismatches are a common rejection and enforcement trigger [Practitioner consensus].

## 10. Review timing and expedites

- Plan submissions with buffer: review times vary by season and by account history; avoid shipping critical growth changes in the final days before holidays [Practitioner consensus].
- Apple offers expedited review requests for critical fixes; use them sparingly and only for real incidents [Official].
- Google Play reviews can take longer for new developer accounts and for sensitive categories [Practitioner consensus].
