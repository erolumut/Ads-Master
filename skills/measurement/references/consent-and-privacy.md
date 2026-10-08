# Consent and Privacy

Consent design decides how much data you may collect and how much of it platforms can use. This module covers consent mode v2, CMPs, IAB TCF, and the legal regimes that most often affect paid media tracking: GDPR and ePrivacy, DMA, the EU Digital Omnibus proposal, UK PECR and the Data (Use and Access) Act, US state laws and Turkey's KVKK.

This is operational guidance, not legal advice. State the rule, the source, the date and the uncertainty, and escalate interpretation to the human and their counsel.

## 1. Consent mode v2 (Google)

### Parameters

| Parameter | Controls | Required for |
|-----------|----------|--------------|
| ad_storage | Advertising cookies (read and write) | Ads measurement cookies |
| analytics_storage | Analytics cookies | GA4 cookies |
| ad_user_data | Sending user data to Google for advertising | Enhanced conversions, Customer Match, offline uploads for EEA users |
| ad_personalization | Personalized advertising (remarketing) | Remarketing audiences |
| functionality_storage, personalization_storage, security_storage | Non-ad storage | Optional, CMP categories |

Google's EU user consent policy requires advertisers using Google measurement and personalization for EEA users to pass consent signals (ad_user_data and ad_personalization added in 2024 in response to the DMA) [Official, 2024]. Without valid signals, remarketing and some measurement features degrade for EEA traffic.

### Basic versus advanced

| | Basic | Advanced |
|-|-------|----------|
| Tag behavior before consent | Google tags blocked until the user interacts with the banner | Google tags load with defaults denied and send cookieless pings |
| Data when denied | None | Cookieless pings (no cookies, no client ID) |
| Modeling | General (not advertiser specific) conversion modeling in Google Ads | Advertiser specific modeling in Google Ads and GA4 behavioral modeling when thresholds are met |
| Legal posture | Lower data collection before consent | Some DPAs and counsel question pings before consent [Contested] |
| Choose when | Counsel requires no network calls before consent | Counsel accepts cookieless pings; you need modeling |

Google Ads conversion modeling eligibility has been described as at least 700 ad clicks over 7 days per country and domain grouping [Official, verify current help page]. GA4 behavioral modeling thresholds are in [GA4](ga4-setup-and-audit.md).

### Implementation rules

1. The default command must run before any Google tag and before GTM loads tags. In GTM use a CMP template on the Consent Initialization (All Pages) trigger. In code, put the default in the head before the GTM or gtag snippet.
2. Use region-specific defaults: denied in opt-in regions (EEA, UK, Switzerland, Turkey), and a policy decision elsewhere (US states are opt-out regimes; default granted with GPC and "Do not sell or share" honored is common [Practitioner consensus]).
3. `wait_for_update` (milliseconds) gives an async CMP time to send the update; 500 is typical.
4. The CMP must call `gtag('consent', 'update', {...})` on load for returning users and on every choice.
5. Optional: `ads_data_redaction` (redacts ad click identifiers when ad_storage denied) and `url_passthrough` (passes click IDs through URLs when cookies are denied). Check legal posture before url_passthrough.
6. Verify in network requests: the `gcs` parameter (for example G100 both denied, G111 both granted) and the `gcd` parameter carry consent state; GTM Tag Assistant has a Consent tab.

```html
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  // Opt-in regions: EEA, UK, Switzerland, Turkey
  gtag('consent', 'default', {
    ad_storage: 'denied', analytics_storage: 'denied',
    ad_user_data: 'denied', ad_personalization: 'denied',
    wait_for_update: 500,
    region: ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','IS','LI','NO','GB','CH','TR']
  });
  // Everywhere else (policy decision; US opt-out handled by CMP and GPC)
  gtag('consent', 'default', {
    ad_storage: 'granted', analytics_storage: 'granted',
    ad_user_data: 'granted', ad_personalization: 'granted'
  });
  gtag('set', 'ads_data_redaction', true);
</script>
<!-- CMP script here, then GTM snippet -->
```

## 2. Consent for non-Google platforms

| Platform | Consent mechanism | Recommended pattern |
|----------|-------------------|---------------------|
| Meta pixel | `fbq('consent', 'revoke')` before `fbq('init')`, then `fbq('consent', 'grant')` on consent | Or block the pixel via GTM additional consent (ad_storage) |
| Meta CAPI | Send only when you have a lawful basis for ad data; for US state opt-outs use `data_processing_options: ['LDU']` (Limited Data Use) with country and state codes per Meta docs | Carry consent flag from browser to server |
| TikTok pixel | `ttq.holdConsent()`, then `ttq.grantConsent()` or `ttq.revokeConsent()` | Or GTM consent check |
| Microsoft UET | UET consent mode: `uetq.push('consent', 'default', {ad_storage: 'denied'})` then update; Microsoft enforces consent signals for EEA, UK and Swiss traffic from 2025-05-05 [Official, 2025-03; same date in the microsoft-ads skill] | Map CMP ad category to ad_storage |
| LinkedIn Insight Tag, Pinterest, Snap, Reddit, ChatGPT Ads pixel | Check each vendor's current consent API (the ChatGPT Ads pixel exposes a consent call according to community API notes [Unverified]); otherwise load only after consent | GTM "Require additional consent" with ad_storage |
| Server events (all CAPIs, offline uploads) | Google Ads API and Data Manager API accept consent fields (ad user data, ad personalization) for EEA users [Official, verify field names] | Never send server events the browser consent would have blocked |

## 3. CMPs

Choose a CMP that is: Google certified (Google CMP Partner Program, required for publishers using Google ad products in EEA, UK and Switzerland, and the easiest path to consent mode v2), TCF v2.3 compatible if you use TCF, GPP capable if you serve US states, and supports region rules, Shopify Customer Privacy API or WordPress integration as needed.

Common choices: Cookiebot and Usercentrics (same group), OneTrust, Didomi, CookieYes, iubenda, Complianz (WordPress), Axeptio, Sourcepoint, consentmanager.net, Termly, Osano, TrustArc, Ketch, Pandectes and Consentmo (Shopify apps), Shopify's own banner. Check the current certified list on Google's CMP partner page before recommending.

CMP configuration checks:
1. Reject is as easy as accept on the first layer (EDPB cookie banner taskforce report 2023; CNIL and other DPA enforcement) [Official, 2023].
2. No pre-ticked boxes, no consent walls for analytics (except lawful pay-or-consent models, contested).
3. Categories map to consent mode parameters correctly (marketing -> ad_storage, ad_user_data, ad_personalization; statistics -> analytics_storage).
4. Returning visitors: consent update fires on page load before tags need it.
5. Logs: consent records retained for proof.
6. Banner language matches site language.
7. Re-consent cycle (commonly 6 to 12 months) and on vendor list changes.

## 4. IAB TCF

| Version | Status |
|---------|--------|
| TCF v2.2 | Released 2023; removed legitimate interest for advertising and content personalization purposes |
| TCF v2.3 | Adds the mandatory disclosedVendors segment. Transition ended 2026-02-28; from 2026-03-01 TC strings created without the segment are invalid, older strings stay valid until renewed [Official, IAB Europe]. Google requires v2.3 for TC strings generated on or after 2026-03-01; non-compliant ad requests may fall back to Limited Ads [Official, Google Ad Manager Help] |

For advertisers: TCF matters mostly if your CMP is a TCF CMP and your vendors read the TC string. Google tags can read TCF signals (Google's vendor ID is 755) when TCF support is enabled; otherwise map CMP choices to consent mode explicitly. Confirm the CMP writes v2.3 strings (inspect `__tcfapi('getTCData', ...)` output or CMP dashboard).

US: IAB Global Privacy Platform (GPP) carries US state signals (US National and state sections). Use a CMP that writes GPP strings if your vendors consume them.

## 5. EU: GDPR, ePrivacy, DMA, Digital Omnibus

- ePrivacy Directive Article 5(3): storing or reading information on a device needs consent unless strictly necessary. Applies to cookies, local storage, pixels, fingerprinting. National laws implement it (for example France, Germany TDDDG, Italy, Spain).
- GDPR: lawful basis for processing personal data (consent for ad tracking in practice), transparency, data minimization, processor contracts (DPAs), international transfers (EU-US Data Privacy Framework since July 2023; check vendor certification).
- DMA: Google, Meta and others are gatekeepers; requires consent for combining personal data across services. Google responded with the consent mode v2 signals; the European Commission fined Meta EUR 200 million in April 2025 over its pay or consent model [Official, 2025-04].
- Digital Omnibus (proposed November 2025): would move personal data cookie rules into a new GDPR Article 88a and add Article 88b requiring sites to honor machine-readable browser or OS consent signals. As of 2026-10-08 it is a proposal: the Council has no agreed mandate (the 2026-06-26 Coreper vote was cancelled; the 2026-10-07 vote was postponed to 2026-10-11 under pressure from France and Germany), Council texts dropped Article 88b, the September Irish Presidency text keeps cookie consent in the ePrivacy framework rather than moving it into the GDPR and shortens the re-ask period after refusal from 6 to 4 months, and Parliament has no position after 1,750+ committee amendments. Final adoption of the data provisions is not expected before late 2026 at the earliest [Press, 2026-06 to 2026-10; Contested on final shape]. Do not confuse it with the AI omnibus, which is already law (Regulation (EU) 2026/1744, in force 2026-07-27; AI Act Article 50 disclosure duties apply from 2026-08-02) [Official, 2026-07]. Action: keep current ePrivacy consent practice; monitor.

## 6. United Kingdom

- PECR governs cookies; UK GDPR governs personal data.
- Data (Use and Access) Act 2025 received Royal Assent in June 2025. Its PECR changes (new Schedule A1 exceptions, including statistical purposes, and PECR fines raised to UK GDPR levels) commenced on 2026-02-05 under the Commencement No. 6 Regulations 2026; the ICO published final guidance on storage and access technologies on 2026-04-29 [Official, 2026-02 and 2026-04].
- The statistical exception applies only when the sole purpose is statistics about how the service is used (not identifying or tracking people), with clear information and a free, simple way to object. Analytics tags that also feed advertising, or third-party analytics vendors that reuse the data for their own purposes, do not qualify. Default: UK analytics may run without consent only after counsel confirms the tool and configuration meet these conditions; otherwise keep it behind consent. Advertising cookies stay consent based.
- The ICO announced a review of cookie compliance on the most visited UK websites in 2025 [Official, 2025].

## 7. United States

| Area | Rule of thumb |
|------|---------------|
| Comprehensive state laws | Around 19 states in force by January 2026 (including California, Virginia, Colorado, Connecticut, Utah, Texas, Oregon, Montana, Iowa, Delaware, Nebraska, New Hampshire, New Jersey, Tennessee, Minnesota, Maryland, and from 2026-01-01 Indiana, Kentucky, Rhode Island) [Practitioner consensus; verify with an up-to-date tracker] |
| Targeted advertising | Opt-out rights for "sale", "sharing" (California) and "targeted advertising"; sharing pixel data with ad platforms is often treated as sale or sharing |
| Universal opt-out | Many states require honoring opt-out preference signals such as Global Privacy Control (GPC). Default policy: treat GPC as an opt-out of sale, sharing and targeted advertising in every US state |
| Sensitive data | Opt-in consent for sensitive data in most states; Maryland's law (in force October 2025) bans the sale of sensitive data and has strict minimization [verify] |
| California | CPPA regulations on automated decision-making, risk assessments and cybersecurity audits took effect 2026-01-01 (ADMT obligations from 2027, first cybersecurity audit certifications from 2028-04-01; ADMT start date reported as January or April 2027) [Official, CPPA 2025-09]; AB 566 (California Opt Me Out Act, signed 2025-10-08) requires browsers to offer an opt-out preference signal from 2027-01-01 [Official, 2025-10] |
| Health | Washington My Health My Data Act (2024) covers broad "consumer health data"; HHS OCR guidance on tracking technologies for HIPAA entities (partly vacated by a federal court in June 2024 for unauthenticated pages); FTC Health Breach Notification Rule actions against health apps sharing data with ad platforms |
| Litigation risk | Class actions under the California Invasion of Privacy Act (pixels, session replay, chat) and the Video Privacy Protection Act (video pages plus pixels) |

Implementation: CMP with US mode (notice plus "Your privacy choices" link, GPC detection), Meta LDU for California and other states as Meta supports, Google restricted data processing (`gtag('set', 'restricted_data_processing', true)` for opted-out users), TikTok and others blocked for opted-out users.

## 8. Turkey: KVKK (Law No. 6698)

| Topic | Rule | Source label |
|-------|------|--------------|
| Cookies | The KVKK cookie guideline (2022) expects explicit consent for non-essential cookies such as analytics and advertising, with separate consent, no pre-ticked boxes | [Official, 2022; verify current guideline] |
| Cross-border transfer reform | Law No. 7499 (Official Gazette 2024-03-12) rewrote Article 9; new regime in force 2024-06-01; explicit consent as a general transfer basis tolerated only until 2024-09-01 | [Official, 2024] |
| Transfer tiers | Adequacy decision, appropriate safeguards (standard contracts, binding corporate rules, undertakings with Board permission), or limited occasional derogations (explicit consent among them, only for non-regular transfers) | [Official, 2024] |
| Implementing regulation | 2024-07-10 (Official Gazette 32598); Board standard contract templates adopted 2024-06-04 (decision 2024/959), four modules (C2C, C2P, P2P, P2C) | [Official, 2024] |
| Standard contracts | Use the Board text without changes, Turkish text prevails, notify the Authority within 5 business days after signatures (online notification module since 2024-10-25, KEP, or by hand); re-notify on amendment or termination | [Official, 2024] |
| Guidance | Cross-border transfer guideline published January 2025; July 2026 announcement on signatures by authorized persons, signing the Turkish text and notarized translations | [Official via law firm summaries, 2025 to 2026] |
| Adequacy | The Authority stated on 2026-08-17 that no adequacy decision has been made | [Secondary citing kvkk.gov.tr, 2026-08] |
| Fines 2026 | Failure to notify a standard contract: TRY 90,308 to 1,806,177; data security failures TRY 256,357 to 17,092,242; transparency (information) duty TRY 85,437 to 1,709,200. Amounts revalued every January (2026 rate 25.49%, Official Gazette 2025-11-27), applying to violations from 2026-01-01 | [Secondary, multiple law firms 2026; verify Article 18 table] |

What this means for tracking in Turkey:
1. Treat Turkey as an opt-in region for analytics and ad cookies (default denied, explicit consent).
2. Tags and CAPIs that send personal data to platforms abroad (Google, Meta, TikTok, Microsoft, LinkedIn, OpenAI) are cross-border transfers. Systematic transfers need an Article 9 safeguard; relying on explicit consent alone for regular transfers is no longer the standard path after 2024-09-01 [Contested in practice: many sites still rely on consent; escalate].
3. Check whether each vendor offers a KVKK standard contract or other safeguard; if a vendor does not, flag the risk to the human and counsel. Do not claim compliance.
4. Host sGTM in a region and with a processor documented in the VERBIS registration and privacy notice where required.
5. Keep a transfer register: vendor, data categories, mechanism, notification date.

## 9. Sensitive categories and platform policies

- Meta restricts data sharing for health and wellness and some financial advertisers (2025 changes limited lower funnel optimization and blocked some URL and parameter data for these categories) [Official, 2025; verify current scope in Meta Business Help Center].
- Google personalized advertising policy bans targeting on sensitive categories and remarketing on sensitive pages; GA4 bans sending PII.
- Never send diagnosis, condition, medication, financial distress or similar values in event names, URLs, parameters or custom data to any ad platform. Use neutral event names (lead, purchase) and server-side filtering.
- For HIPAA covered entities and health advertisers in the US: no third-party pixels on authenticated pages or condition-specific pages without legal review; prefer server-side with a BAA-capable vendor.

## 10. Consent QA checklist

| # | Test | Pass |
|---|------|------|
| 1 | Fresh session in an opt-in region, before interacting with banner | Only strictly necessary requests; Google pings show gcs=G100 (advanced) or no Google requests (basic); no Meta, TikTok, LinkedIn requests |
| 2 | Accept all | Consent update fires; tags fire on the same page view; gcs=G111 |
| 3 | Reject all | No ad cookies set; non-Google ad tags never fire; server events not sent for this user |
| 4 | Partial (analytics only) | GA4 cookies set, ad tags blocked |
| 5 | Returning visitor who accepted | Update fires before page_view |
| 6 | US visitor with GPC on | Sale and sharing opted out; restricted data processing or LDU applied; ad tags limited per policy |
| 7 | Checkout and thank you page (Shopify sandbox, other domains) | Consent state respected there too |
| 8 | Server-side events | Consent flag present on every server event; denied events dropped or sent only as permitted |
| 9 | CMP logs | Consent records stored with timestamp and version |
| 10 | GA4 Admin consent settings | Signals detected for ads measurement and personalization |
