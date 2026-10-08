# Email Deliverability

Mailbox provider requirements as of October 2026, DNS and header setup, thresholds, monitoring tools, inbox changes (Gmail, Apple, Outlook), warmup, list hygiene and a diagnostic table. Deliverability problems are stop conditions for campaign volume: fix before optimizing anything else.

## 1. Requirements by mailbox provider

### 1.1 Gmail (personal gmail.com and googlemail.com)

| Requirement | All senders | Bulk senders (close to 5,000 or more messages per day to personal Gmail accounts; status is permanent once reached) |
|-------------|-------------|------------------------------------------------------------------------|
| Authentication | SPF or DKIM | SPF and DKIM, plus DMARC (p=none minimum) with alignment of the From domain to SPF or DKIM |
| PTR and TLS | Valid forward and reverse DNS for sending IPs; TLS | Same |
| Format | RFC 5322; no impersonation of gmail.com in From | Same |
| Unsubscribe | Easy unsubscribe | One click unsubscribe (RFC 8058 headers) for marketing and subscribed messages, plus a visible unsubscribe link; honor within 2 days |
| Spam rate | Keep under 0.1% (Postmaster Tools); never reach 0.3% | Same; sustained 0.3% or higher causes rejections and makes mitigation ineligible |

Enforcement: requirements announced October 2023 and phased in from February 2024; from November 2025 Gmail moved from mostly temporary errors (4.7.x) to temporary and permanent rejections (5.7.x) for non compliant traffic [Official, Google sender guidelines FAQ; enforcement change reported by Valimail, Red Sift and Suped, 2025-11]. The rules did not change; enforcement did.

### 1.2 Yahoo and AOL

Same core rules as Gmail since February 2024: SPF, DKIM, DMARC (p=none minimum), one click unsubscribe for bulk mail (honored within 2 days), complaint rate under 0.3% (Yahoo calculates on mail delivered to the inbox and evaluates as a snapshot, so spikes can trigger throttling). Yahoo Sender Hub Insights shows complaint rate once you send at least about 100 messages per day; treat 0.1% as the working target [Official, Yahoo Sender Hub; secondary guides 2026]. Whether a 5,000 per day threshold applies to Yahoo is disputed; assume the rules apply at any volume [Contested].

### 1.3 Microsoft consumer domains (outlook.com, hotmail.com, live.com)

| Item | Status |
|------|--------|
| Scope | Senders of more than 5,000 messages per day to Microsoft consumer domains [Official, Microsoft Defender for Office 365 blog, announced 2025-04-02] |
| Required | SPF pass, DKIM pass, DMARC at p=none or stronger aligned with SPF or DKIM |
| Enforcement | From 2025-05-05 non compliant mail is rejected (not junked) with `550; 5.7.515 Access denied, sending domain [domain] does not meet the required authentication level` [Official, Microsoft; URIports and dmarcian 2025] |
| Recommended | Functional unsubscribe, list hygiene, valid From and Reply-To, compliant formatting [Official] |
| 2026 | Reports of tightening (PTR, p=none scrutiny) are not backed by a Microsoft document [Contested]; SNDS and postmaster site migration dates in 2026 conflict across sources [Unverified] |

Note: Microsoft 365 business tenants (B2B recipients) apply their own filtering (Defender policies) beyond these consumer rules.

### 1.4 Apple iCloud Mail

Apple's postmaster page lists requirements for bulk email and states non compliant mail will be rejected: send only to recipients who explicitly subscribed, provide an unsubscribe link that works immediately, SPF and DKIM, a published DMARC policy (no minimum policy level), ARC on forwarded mail, RFC 5321 and 5322 compliance, reverse DNS, consistent sending identity, separate marketing and transactional streams. Apple publishes no volume threshold, no complaint threshold and no postmaster dashboard; contact is icloudadmin@apple.com [Official, Apple Support 102322].

### 1.5 One configuration that satisfies all four

- Branded sending domain or subdomain (for example `mail.brand.com` or `news.brand.com`) authenticated in the ESP; no shared ESP domain in From.
- SPF including the ESP; under 10 DNS lookups.
- DKIM 2048 bit keys aligned with the From domain.
- DMARC record on the organizational domain: start `p=none` with `rua` reporting, move to `p=quarantine` then `p=reject` once all legitimate sources pass (also required for BIMI).
- RFC 8058 one click unsubscribe headers on every marketing message:
  ```
  List-Unsubscribe: <https://brand.example/unsub?t=TOKEN>, <mailto:unsub@brand.example?subject=unsub>
  List-Unsubscribe-Post: List-Unsubscribe=One-Click
  ```
  The header must be covered by the DKIM signature. Major ESPs add these automatically when unsubscribe links are present [Official, RFC 8058; ESP docs].
- Visible unsubscribe link in the body; processing within 2 days (Gmail, Yahoo) and 10 business days maximum (CAN-SPAM).
- Separate streams: transactional (receipts, shipping, password) on a different subdomain or IP pool from marketing.
- TLS for SMTP; valid PTR.

DMARC note: the IETF DMARC update (DMARCbis) was reportedly published in May 2026 as RFC 9989, 9990 and 9991; vendors say it does not change mailbox provider bulk sender requirements [Unverified, secondary 2026].

## 2. Thresholds to run by

| Metric | Healthy | Investigate | Stop and fix |
|--------|---------|-------------|-------------|
| Gmail spam rate (Postmaster v2) | Under 0.08% | 0.08% to 0.1% | Over 0.1% for 2+ days; never approach 0.3% [Official thresholds 0.1% and 0.3%; bands are practitioner consensus] |
| Yahoo complaint rate | Under 0.1% | 0.1% to 0.2% | Over 0.2% |
| Hard bounce per send | Under 0.3% | 0.3% to 0.5% | Over 0.5%: list source problem |
| Unsubscribe per campaign | Under 0.3% | 0.3% to 0.5% | Over 0.5% repeatedly: frequency or relevance problem |
| Click rate trend | Stable vs own baseline | Down 20% across all providers | Down 50% at one provider: placement issue |
| Authentication pass rate (DMARC reports) | Near 100% for ESP sources | Unknown sources appear | Legitimate source failing |

Bands other than the official 0.1% and 0.3% are [Practitioner consensus]; calibrate to the project's history.

## 3. Monitoring tools

| Tool | What | Notes |
|------|------|------|
| Google Postmaster Tools v2 | Compliance status dashboard (SPF, DKIM, DMARC, one click unsubscribe, spam rate, TLS), spam rate, delivery errors | v2 dashboards replace the legacy interface; the legacy web interface deprecation was postponed; the v1 API is being retired and v2 API dropped Domain and IP reputation [Official, Gmail Help 16594218]. Dates for v1 shutdown conflict across sources [Contested] |
| Yahoo Sender Hub (Insights) | Complaint rate, delivery data | Needs about 100 messages per day [Secondary, 2026] |
| Microsoft SNDS | IP level data for Outlook consumer | Migration to a new portal reported in 2026 with conflicting dates [Unverified] |
| DMARC aggregate report processor (dmarcian, Valimail, Red Sift, PowerDMARC, URIports, EasyDMARC) | Authentication sources and failures | Required before moving to p=reject |
| ESP deliverability dashboards | Bounces, complaints, unsub by provider | Klaviyo deliverability hub, Braze, Iterable |
| Seed list placement tests (Validity Everest, GlockApps, others) | Inbox vs spam on seed accounts | Directional; seeds do not have engagement history [Practitioner consensus] |
| Blocklist monitors (Spamhaus, others) | Listings | Act within hours if listed |

## 4. Inbox changes that affect lifecycle email (2025 to 2026)

| Change | Date | Impact | What to do |
|--------|------|--------|-----------|
| Gmail "Manage subscriptions" view | Rolled out 2025-07 | Lists subscriptions sorted by sender volume with one tap unsubscribe (Gmail sends the request) | Heavy senders are most exposed; cut volume to unengaged tiers; earn the frequency [Official, Google Workspace Updates 2025-07] |
| Gmail Promotions "Most relevant" sorting and "Top deals for you" card; Purchases view | Announced 2025-09-11, mobile personal accounts first | Engagement driven ordering of promotional mail; order and shipping emails consolidated | Engagement matters more than send time; keep transactional mail transactional; whether "most relevant" is default is unconfirmed [Official, Google blog 2025-09; Contested default] |
| Gemini in Gmail summaries | 2025 to 2026 | Post open summaries can paraphrase offers | Put offer, price and deadline in plain text near the top; avoid image only emails [Secondary, Klaviyo and Omnisend 2025 to 2026] |
| Apple Mail categories and Apple Intelligence summaries (iOS 18.2 and later) | 2024-12 onward | Promotions categorized; pre-open summaries can replace preheader text | Clear first sentence; consistent sender identity; BIMI helps brand recognition [Official, Apple; secondary analysis] |
| Apple MPP | Since 2021, still dominant | Opens inflated; Apple share of tracked opens about 62% (Litmus, July 2026) | Click and conversion based metrics and segments [Study, Litmus via secondary 2026-07] |
| CNIL tracking pixel recommendation (France) | Adopted 2026-03-12, published 2026-04-14, transition ended 2026-07-14 | Individual open tracking for campaign optimization needs consent for recipients in France | See [Consent and law](consent-and-law.md); disable individual open tracking for French recipients without consent |

## 5. BIMI

- Requires DMARC at enforcement (`p=quarantine` or `p=reject`, pct 100), SPF and DKIM passing, an SVG Tiny PS logo and a BIMI DNS record.
- Gmail shows the logo with either a Verified Mark Certificate (VMC, needs a registered trademark) or a Common Mark Certificate (CMC, needs at least 12 months of documented public logo use); only a VMC shows the blue verified checkmark [Official, Google; secondary 2026].
- Apple Mail shows BIMI logos with a VMC [Official, Apple; verify CMC support].
- A 2025 URIports analysis found 53.6% of published BIMI records had at least one error preventing display [Study, vendor 2025]; validate with a BIMI checker.
- Value: brand recognition and trust; no provider promises inbox placement from BIMI [Practitioner consensus].

## 6. Warmup (new domain, new ESP, new dedicated IP)

| Day | Audience | Daily volume guide (per major provider) |
|-----|----------|------------------------------------------|
| 1 to 3 | Clicked or purchased in last 30 days | A few thousand |
| 4 to 7 | Add 31 to 60 day engaged | Roughly double every 1 to 2 days if spam rate under 0.1% and no deferrals |
| 8 to 14 | Add 61 to 90 day engaged | Continue doubling |
| 15 to 30 | Add 91 to 180 day | Reach normal volume |
| Never | 180+ day unengaged | Sunset flow only |

Rules [Practitioner consensus]: keep flows running (high engagement helps); pause ramp on any 4.7.x deferrals or spam rate rise; never start a warmup with a purchased, scraped or very old list (do not send to those at all).

## 7. List hygiene

- Real time verification at capture for typos and disposable domains (with care: do not reject valid addresses).
- Double opt-in for high risk sources (co-registration is not allowed; sweepstakes and giveaways need double opt-in), and as the default in Germany and other markets where proof of consent is expected.
- Bot signups: honeypot fields, rate limits, CAPTCHA on suspicious traffic; watch for spikes of signups with no site activity.
- Suppress hard bounces immediately; suppress soft bounces after repeated failures.
- Role addresses (info@, admin@) only when they actually signed up.
- Sunset flow monthly ([Core flows](core-flows.md) section 9).
- Spam traps: recycled traps come from old, unengaged addresses; pristine traps from scraped or purchased lists. Engagement based sunsetting is the defense.

## 8. Content and sending practices

- Consistent From name and address; recognizable brand.
- Text and image balance with live text for offer and CTA; alt text on images.
- Avoid link shorteners and mismatched link domains; brand the click tracking domain.
- Preheader written, not default.
- Send in batches for very large sends (throttle by provider) to avoid spikes.
- Do not change everything at once (new domain, new template, new list) or you cannot diagnose.

## 9. Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| Bounces `550 5.7.515` at Outlook | Missing or failing SPF, DKIM or DMARC alignment | DMARC reports; ESP authentication status | Authenticate branded domain; align DKIM |
| Gmail 4.7.x deferrals or 5.7.x rejections citing sender guidelines | Missing one click unsubscribe, DMARC, alignment, or high spam rate | Postmaster v2 Compliance status | Fix the failing item; reduce volume to engaged tiers |
| Gmail spam rate spike after a campaign | Sent to old or unengaged segment, unexpected frequency, misleading subject, list import | Segment used; list source; unsub and complaint by segment | Revert to engaged tiers; sunset; review consent of imported lists |
| Clicks down at one provider only | Spam foldering at that provider | Seed test; provider dashboards | Engaged only sends for 1 to 2 weeks; check content and links |
| Opens up, clicks flat | Machine opens (MPP, scanners) | Apple Privacy open share | Switch KPIs to clicks and orders |
| Unsubscribes jump | Frequency increase, irrelevant content, Gmail Manage subscriptions | Unsub by tier and campaign type | Preference center, lower frequency for E2 and E3 |
| Hard bounces spike | Bad list source, form abuse, import | Source of new profiles | Remove source; verification; double opt-in |
| Blocklist listing | Spam traps, complaint spike, compromised form | Blocklist lookup; recent sources | Stop the source; request delisting after fix |
| Transactional emails delayed | Shared stream with marketing reputation | Stream separation | Separate subdomain or IP for transactional |

Any of the stop conditions above goes to `ads-master/INCIDENTS.md` with the data, and campaign volume pauses (except engaged tiers and high intent flows) until fixed.
