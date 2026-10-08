# Policy and Account Health

> Knowledge as of 2026-10. Policies change often and enforcement is automated. Read the current Meta Advertising Standards (transparency.meta.com/policies/ad-standards) before launching in a regulated category. This module is not legal advice; flag legal questions to the human.

## 1. Account health foundations

| Item | Standard | Why |
|------|----------|-----|
| Business portfolio (formerly Business Manager) | Owned by the company, at least 2 admins with 2FA, verified business | Recovery and stability; many features and higher limits require verification |
| Business verification | Completed with legal documents matching business name and domain | Required for some APIs, messaging, special categories, higher ad limits |
| Domain verification | Domains verified in the business portfolio | Link ownership, editing link previews, brand protection |
| Admin hygiene | Personal profiles of admins real, secure, 2FA, no shared logins | Hacked or fake profiles cause cascading restrictions |
| Partner access | Agencies via partner business access, not personal admin invites | Clean offboarding |
| System users | API access through system users with scoped tokens | Avoid personal token dependencies |
| Payment | Valid cards with sufficient limits or invoicing (credit line) for larger spend; backup payment method | Failed payments trigger restrictions and delivery stops |
| Account spending limit | Set as safety net | Protects against runaway automation |
| Account Quality / Business Support Home | Checked weekly | Early warning for restrictions |

## 2. Account restrictions and appeals

Common triggers:
- Unusual activity: new account with high spend quickly, many rejected ads, login from new locations, payment failures.
- Policy violations: repeated disapprovals in a short window, circumvention (cloaking, new accounts after a ban), misleading claims, prohibited products.
- Identity issues: admin profile restricted, failed verification.
- Payment disputes or chargebacks.

Appeal procedure:
1. Identify the restricted entity (person, ad account, business portfolio, Page, catalog, WhatsApp account) in Account Quality.
2. Read the cited policy. Fix the cause first (edit landing page, remove claims, update payment, complete verification).
3. Request review once, with a short factual explanation. Template:
```
Business: <legal name>, website <domain>, business portfolio ID <id>.
Restricted asset: <ad account ID>. Policy cited: <policy>.
What we sell and to whom: <one sentence>.
Changes made: <list with dates>.
Evidence: <licenses, verification, landing page URL>.
We request a review. Contact: <name, role, email>.
```
4. If denied and the business is legitimate, escalate through Meta support chat (available for many advertisers), a Meta partner rep, or Meta's agency partner channels. Keep a timeline in the journal.
5. Never create new accounts, profiles or portfolios to bypass a restriction. Circumvention converts a fixable restriction into a permanent ban.

Prevention checklist for new accounts: warm up spend gradually (no more than about 2 to 3x day over day in the first weeks), verify business before launch, start with clean, policy-safe creatives, avoid sudden mass ad launches from new profiles.

## 3. Special ad categories (SAC)

| Category | Covers | Key restrictions [Official, verify current] |
|----------|--------|------------------------------------------|
| Housing | Real estate listings, mortgage, home insurance, rentals | No age, gender, postal code targeting; minimum 15-mile (about 24 km) radius; limited detailed targeting; no lookalikes (special ad audiences restricted) |
| Employment | Job offers, internships, certification programs | Same as above |
| Financial products and services (expanded from "Credit" in January 2025 for US and other regions) | Credit cards, loans, insurance, investments, banking, financing offers | Same targeting limits as above; Meta expanded scope in 2025 [Official, 2025-01, verify geography] |
| Social issues, elections or politics | Ads about social issues, elections, political figures | Authorization ("Paid for by" disclaimer), Ad Library archiving; Meta stopped political, electoral and social issue ads in the EU from October 2025 under the TTPA regulation [Official, 2025-07 announcement] |

Operating rules:
- Declare the category at campaign level; misdeclaring leads to disapprovals and account risk.
- Creative carries more of the targeting load in SAC campaigns; use precise copy that self-selects the audience.
- Advantage+ audience and placements remain usable within SAC limits.

## 4. Restricted and prohibited content (high-frequency issues)

| Topic | Rule summary | Practical guidance |
|-------|-------------|--------------------|
| Personal attributes | Do not assert or imply personal characteristics (health, financial status, religion, ethnicity, sexual orientation, criminal record) | Avoid "Are you depressed?" or "Struggling with debt?"; write "For people who want..." |
| Health and wellness | Weight loss ads 18+, no before and after images that imply unrealistic results, no negative self-perception; prescription drugs and online pharmacies need certification (LegitScript in many markets) | Use outcome-neutral imagery, show product use instead |
| Supplements | No unsafe ingredients, no unproven claims | Claims substantiation in BRAND.md |
| Cosmetic procedures | 18+ targeting; no before and after in some regions | Check region rules |
| Financial services | Advertiser verification required in several countries (for example UK, Australia, India, Singapore, Taiwan, Thailand) [Official, verify list]; crypto requires written permission or regulator licenses | Verify before launch |
| Gambling, real money games | Written permission and licensing per country | Apply before campaign build |
| Alcohol | Country and age rules (often 18+ or 21+ by country); some countries prohibit | Minimum age control and location controls |
| Dating | Written permission | Apply first |
| Misleading claims, clickbait, engagement bait | Disapprovals and reduced delivery | Avoid fake buttons, exaggerated claims |
| Landing pages | Must match the ad, function, not cloak, not be under construction | QA every landing page before launch |
| AI-generated content | Disclosure requirements for some ads (social issue and political, and evolving rules for realistic synthetic people) | Label as required; keep source files |

## 5. Health and wellness data restrictions (2025)

[Official, 2025-01 onward] Meta classifies some advertisers' data sources (datasets, websites, apps) as health and wellness (and other restricted categories). Effects vary by tier:
| Tier (as quoted from Meta Help Center by third parties) | Effect |
|------|--------|
| Core setup | Custom parameters and URL paths after the domain are not shared |
| Restriction on certain standard events | Specific mid and lower funnel events (for example Purchase, AddToCart, Lead, Schedule) blocked from being shared or used for optimization |
| Full restrictions | All events blocked, in specific regions or globally |
Regional differences reported: EU health providers often fully restricted; US often limited to certain standard events [Unverified, 2025-04 Twigeo].

What to do:
1. Check Events Manager > dataset > Settings: data source category and data restrictions. Record the status in ads-master/MEASUREMENT.md.
2. If misclassified (for example generic apparel flagged as health), request review through Events Manager. Appeal times reported from days to months.
3. If correctly classified: optimize to the deepest allowed event (often landing page views or engagement-based events), lean on creative, use website and backend measurement (MER, holdouts) for truth, consider click to message or instant forms where allowed.
4. Do not rename restricted events to mimic Purchase. Practitioners disagree on whether some custom events are allowed; the safe default is to follow Meta's restriction and ask the human before any workaround [Contested].
5. Hand off measurement design to `measurement`.

## 6. Privacy and regional regulation

| Region | Item | Effect on operations |
|--------|------|---------------------|
| EU | DMA: Commission found the "subscription for no ads" model non-compliant in April 2025 (EUR 200 million fine); Meta committed to a less personalized ads choice rolled out from January 2026; the Commission said it will monitor implementation [Official, 2025-12 EC; Meta 10-Q 2026] | Some EU users see less personalized ads; expect lower relevance and potentially higher cost per result in EU; Meta calls the option "less relevant and effective" in SEC filings |
| EU | TTPA: no political, electoral or social issue ads from October 2025 [Official, 2025-07] | Issue-adjacent brands must avoid ads that could be classified as social issue ads in the EU |
| EU | DSA: Ad Library shows all EU ads with targeting and reach data | Competitors can see your EU targeting summary and reach |
| Global (excluding EU, UK, South Korea at launch) | Meta AI chat interactions used to personalize ads from 2025-12-16, excluding sensitive topics [Official, 2025-10 announcement] | More interest signal for ranking; nothing for advertisers to configure; disclose in privacy notices as counsel advises |
| US states | State privacy laws; Limited Data Use flag for California and other states where applicable | `measurement` configures LDU |
| Turkey | KVKK (personal data law) consent and cross-border transfer rules | CAPI and customer lists need a lawful basis and transfer compliance; consult counsel |

## 7. Turkey specific notes

- Location fees: Meta announced in March 2026 that from 2026-07-01 it charges a location fee on image and video ads (including click to WhatsApp ads and WhatsApp marketing messages) delivered to audiences in six countries with digital services taxes: Turkey 5%, Austria 5%, France, Italy and Spain 3%, United Kingdom 2%. The fee follows the audience's location, not the advertiser's, so a non-Turkish advertiser reaching Turkey pays it too. Example from Meta: 100 of delivery to Italy is billed 100 plus 3 location fee; applicable VAT is calculated on top of the total. Meta says the country list and rates may change [Official, 2026-03, via Reuters and Bloomberg Tax]. Add the fee to CPA and ROAS targets for Turkey (breakeven ROAS rises about 5%) and check Billing and payment settings for the current list.
- VAT: Meta calculates applicable VAT on top of ad delivery plus location fee [Official, 2026-03]. For Turkish businesses the treatment (20% standard rate, reverse charge or charged on invoice) depends on account tax settings and business registration; ensure the business tax ID is entered in billing so invoices are correct [Unverified local treatment, confirm with an accountant].
- Currency: Turkish lira accounts are exposed to FX moves; budgets set in TRY need monthly review. A USD or EUR ad account may be preferable for multi-market advertisers, subject to payment method and tax advice.
- Platform availability risk: Instagram was blocked in Turkey for about 9 days in August 2024 and Threads was suspended in Turkey in April 2024 due to a competition authority order [Official news, 2024; Threads current status Unverified]. Keep contingency plans (other channels, owned audiences).
- Advertising Board (Reklam Kurulu) rules on influencer marketing require clear disclosure of commercial content [Unverified details, 2021 guidance]; apply to partnership ads.
- Messaging-first market: click to WhatsApp and Instagram Direct often outperform website forms for local services and consultative sales [Practitioner consensus].

## 8. Brand safety and suitability

| Control | Use |
|---------|-----|
| Inventory filter (expanded, moderate, limited) | Moderate default; limited for sensitive brands |
| Block lists (Audience Network, in-stream, Instant Articles legacy) | Block known unsafe publishers |
| Publisher lists and delivery reports | Audit where ads ran on Audience Network and in-stream |
| Account-level placement controls | Hard block placements (the remaining true exclusion after ad set exclusions began disappearing on 2026-08-25) [Practitioner consensus, 2026-08] |
| Comment moderation | Hide keywords, moderation assist; required if "relevant comments" enhancement is on |
| Third-party verification partners | Integral Ad Science, DoubleVerify, Zefr for feed and Reels brand safety reporting |

## 9. Weekly account health checklist

1. Account Quality: no new restrictions, warnings, or rejected ads trends.
2. Disapprovals: fix or appeal within 24 hours; document patterns.
3. Payment: no failures; spending limit headroom above next 30 days of spend.
4. Business verification and domain verification still valid.
5. Admin list and partner access: remove departed people.
6. Data restrictions notices in Events Manager.
7. Policy updates in the Meta Business Help Center and Advertising Standards changelog.
