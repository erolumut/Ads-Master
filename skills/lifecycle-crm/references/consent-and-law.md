# Consent and Law for Lifecycle Messaging

Rules for email, SMS, WhatsApp, push, tracking pixels and subscriptions by jurisdiction, as of October 2026. This is operational guidance, not legal advice: route every new consent text, new market and edge case to `compliance` and, where needed, counsel. When rules conflict, apply the strictest rule for the recipient's location.

## 1. Consent record standard (every channel)

Store for every profile and channel:

| Field | Example | Why |
|-------|---------|-----|
| Channel | email, sms, whatsapp, push | Consent is per channel |
| Status | subscribed, unsubscribed, never_subscribed, suppressed | |
| Timestamp (UTC) | 2026-10-08T12:31:09Z | Proof and expiry logic |
| Source | footer_form, checkout_checkbox, popup_v3, pos, import_2026_05 | Source quality and audits |
| Method | single_opt_in, double_opt_in, soft_opt_in, keyword | |
| Consent text version | sms_consent_v4 | Proof of what was shown |
| IP or device (where lawful) | | Proof for web capture |
| Jurisdiction | US-CA, DE, FR, TR, GB | Rules to apply |
| Registry sync | iys_synced_at (Turkey) | Turkey legal validity |
| Withdrawal | timestamp, method | Must be honored across systems |

Never import a list as subscribed without its consent evidence. Never re-subscribe suppressed profiles. Klaviyo's API exposes consent and suppression per channel, plus bulk subscribe, suppress and data privacy deletion jobs [Official, Klaviyo API revision 2026-07-15].

## 2. Email

### 2.1 European Union (GDPR plus ePrivacy Directive Article 13)

- Default: prior opt-in consent for marketing email to individuals (freely given, specific, informed, unambiguous; unticked box; records kept; withdrawal as easy as giving).
- Soft opt-in (Article 13(2)): existing customers whose contact details were obtained in the context of a sale may receive marketing for the seller's own similar products or services if they were given a clear, free opportunity to object at collection and in every message. National implementations differ (for example Germany UWG section 7(3) adds conditions; some member states treat B2B differently) [Official, Directive 2002/58/EC; national laws].
- Double opt-in: not mandated by the Directive, but German courts expect proof of consent, so double opt-in is the de facto standard in Germany and recommended across the EU for web capture [Practitioner consensus].
- Every message: sender identity, valid opt-out, no disguised sender.
- Status of reform (October 2026): the ePrivacy Regulation proposal was withdrawn (published 2025-10-06). The Digital Omnibus proposal (2025-11-19) would move personal data cookie consent into the GDPR (Article 88a) and add browser signals and single click reject; reports of the Council compromise of 2026-06-22 say it deleted Article 88a; nothing adopted [Secondary, Osborne Clarke, Freshfields 2025 to 2026; Contested]. Plan on current rules.

### 2.2 France: email tracking pixels (CNIL)

- CNIL recommendation on tracking pixels in emails (Délibération 2026-042) adopted 2026-03-12, published 2026-04-14 [Official, CNIL].
- Consent required for individual open tracking used to measure or optimize campaigns, personalize content, or change frequency or channel.
- Exempt (no consent) only: security and authentication uses, and individual open measurement strictly for deliverability (keep only the date of last known open, to the day, overwritten), for emails the recipient requested.
- Aggregate campaign level open rates without identifying individuals are widely read as outside consent if anonymization is effective; readings differ [Contested].
- Scope follows the recipient's location in France, regardless of sender location; B2B is not automatically exempt.
- Transition: existing contacts could be informed of their right to object by 2026-07-14; contacts collected from 2026-04-14 needed compliant consent from day one; opt-out from tracking must be separate from unsubscribe [Official and law firm summaries, 2026].
- Italy's Garante is reported to be on a similar track with consent deadlines in 2026 (including 2026-10-29) [Unverified].

Implementation: flag French recipients; either collect a separate tracking consent or disable individual open tracking for them (ESP setting or separate sending configuration); base their segments on clicks, orders and site activity; document the decision in DECISIONS.md.

### 2.3 United Kingdom (UK GDPR plus PECR as amended by the Data (Use and Access) Act 2025)

- PECR regulation 22: consent for marketing email to individuals, or the soft opt-in for existing customers (similar products and services, opt-out at collection and in every message).
- From 2026-02-05: PECR fines up to £17.5 million or 4% of global turnover (whichever is higher) for conduct after that date (previous cap £500,000) [Official, ICO statement 2026-02].
- Charity soft opt-in: charities may email supporters who expressed interest in or supported their purposes, for contact details collected from 2026-02-05, with opt-out at collection and in every message; ICO guidance published 2026-04-28, updated in May [Official, ICO; law firm summaries 2026].
- Some analytics and site personalization cookies moved to exceptions with opt-out under DUAA [Secondary, 2026].

### 2.4 United States (CAN-SPAM)

- Opt-out model for commercial email: no deceptive headers or subject lines, identify as an ad (unless prior affirmative consent), valid physical postal address, a working opt-out honored within 10 business days and functional for at least 30 days after send, no charging or extra steps to opt out, responsibility extends to vendors sending on your behalf [Official, FTC CAN-SPAM compliance guide].
- Civil penalties are inflation adjusted annually, above $50,000 per violating email [Official, FTC; verify current figure].
- Mailbox provider rules (one click unsubscribe, opt-in practice) are stricter than the law and decide deliverability.

### 2.5 Canada (CASL)

- Express consent, or implied consent: existing business relationship for 2 years after a purchase or 6 months after an inquiry. Identification and unsubscribe (honored within 10 business days) required. Administrative penalties up to CAD 10 million per violation for organizations [Official, CRTC].

### 2.6 Turkey (Law 6563, Regulation on Commercial Communication and Commercial Electronic Messages, İYS, KVKK)

| Rule | Detail |
|------|--------|
| Prior consent | Required for commercial electronic messages (SMS, email, calls, WhatsApp and other messages) to consumers [Official, Law 6563] |
| İYS registration | Consents obtained outside İYS must be registered in İYS within 3 business days or they are invalid; messages may only go to recipients whose consent is in İYS [Official, Regulation and İYS] |
| Confirmation of electronic consent | When consent is obtained electronically outside İYS, a confirmation with an opt-out option is sent to the recipient within 24 hours [Official, Regulation amendment] |
| Traders and craftsmen (tacir, esnaf) | Prior consent not required, but their addresses must be registered in İYS and checked for refusal before sending; after refusal, messages need consent [Official] |
| Opt-out | Every message includes an accessible opt-out (customer service number, SMS number or opt-out URL, or the İYS channel); stop sending within 3 business days of refusal; report refusals to İYS within 3 business days [Official] |
| Separate consents (KVKK) | KVKK Board principle decision 2025/1072 (2025-06-10, Official Gazette 2025-06-26): membership agreement approval, consent to personal data processing and commercial message permission are separate acts; do not collect them with a single SMS verification code; commercial message consent must not be a condition of the product or service; information notice and explicit consent are separate [Official, KVKK] |
| Fines (2026) | Per the 2025-12-25 Official Gazette (No. 33118) update: unconsented or non compliant messages 2,859 TL to 14,309 TL, up to ten times higher when sent in one batch to many recipients; other obligations (promotion conditions, refusal handling) 5,723 TL to 42,930 TL [Official, via law firm summaries; refusal fine band Contested] |
| Integrators | Integrators uploading consent to İYS are subject to authorization by the Ministry of Trade [Secondary; effective date Unverified] |

Implementation: connect the ESP or CDP to İYS (directly or via an integrator) for consent upload and refusal sync in both directions; check İYS status before every marketing send; keep separate checkboxes for KVKK explicit consent and commercial messages; in checkout, ask for message permission after the order is confirmed, not as part of OTP verification.

## 3. SMS and calls

### 3.1 United States (TCPA, FCC rules, state laws)

| Topic | Status (2026-10-08) |
|-------|---------------------|
| Consent for marketing texts | Prior express written consent for telemarketing texts sent with an autodialer or prerecorded content, with clear and conspicuous disclosure; consent cannot be a condition of purchase [Official, 47 CFR 64.1200] |
| One-to-one consent rule | Vacated by the Eleventh Circuit on 2025-01-24 (Insurance Marketing Coalition v. FCC); FCC formally removed it (2025-09) [Official] |
| Opt-out (revocation) rules | Since 2025-04-11: consumers may revoke by any reasonable means; honor within a reasonable time, max 10 business days; one confirmation text allowed. The "revoke all" provision (revocation applies to all robocalls and robotexts) was delayed to 2027-01-31, then narrowed by an FCC order adopted 2026-09-30: revocation in response to an informational message can be limited to that informational category, marketing opt-outs still stop all marketing, and callers may designate an exclusive FCC approved opt-out method; effective 30 days after Federal Register publication (not confirmed as of 2026-10-08); a further notice proposes shorter timeframes [Official, FCC; law firm alerts 2026-10] |
| Quiet hours | 8:00 to 21:00 called party local time for telephone solicitations (47 CFR 64.1200(c)(1)); plaintiffs apply it to texts even with consent; courts are split; an industry petition asks the FCC to confirm consented texts are outside quiet hours claims, no ruling yet [Official; secondary 2025 to 2026] |
| Statutory damages | $500 per violation, up to $1,500 if willful or knowing [Official, 47 U.S.C. 227] |
| Agency deference | After McLaughlin Chiropractic v. McKesson (US Supreme Court, 2025-06), district courts are not bound by FCC interpretations of the TCPA, adding uncertainty [Official, court ruling; secondary analysis] |
| State laws | Florida (FTSA: 8:00 to 20:00, max 3 messages per 24 hours on the same subject, private right of action), Oklahoma (similar), Maryland, Washington, Texas (text messages added to telephone solicitation rules from 2025-09-01, registration questions) carry private rights of action with $500 to $10,000 per violation ranges cited [Secondary, 2026; Unverified details per state] |
| Carrier rules | CTIA guidelines and 10DLC registration; carriers can block or suspend independently of law |

Compliant SMS consent disclosure (US, adapt with compliance):
```
By submitting, you agree to receive recurring automated marketing text messages from <Brand> at the number provided. Consent is not a condition of purchase. Msg frequency varies. Msg & data rates may apply. Reply HELP for help or STOP to cancel. See Terms <link> and Privacy <link>.
```

### 3.2 EU and UK

SMS marketing follows the same consent and soft opt-in rules as email (ePrivacy and PECR "electronic mail" covers SMS). Sender ID registration rules vary by country (for example alphanumeric sender registration in some markets).

### 3.3 Turkey

SMS is a commercial electronic message: İYS consent and the rules in 2.6 apply. Operators check İYS before delivering commercial SMS [Practitioner consensus].

## 4. WhatsApp

- Platform policy requires opt-in to receive WhatsApp messages from the business, clear identity, and honoring opt-outs; marketing templates paused to US numbers since 2025-04-01 [Official, Meta; secondary 2026].
- Law still applies on top: GDPR or PECR consent rules (WhatsApp marketing is electronic marketing), İYS in Turkey, LGPD in Brazil.
- General purpose AI assistants are barred from the WhatsApp Business API from 2026-01-15; task specific bots allowed ([SMS, WhatsApp and push](sms-whatsapp-and-push.md) section 4.2).

## 5. Push notifications

Push permission is an OS level consent, not a legal marketing consent. Under ePrivacy and PECR, push marketing to individuals is generally treated like other electronic marketing in practice when it promotes products; keep a marketing preference toggle in the app and respect it [Practitioner consensus; confirm with compliance].

## 6. Subscriptions and auto renewal

See [Replenishment and subscriptions](replenishment-and-subscriptions.md) section 6. Summary: no federal click to cancel rule (vacated 2025-07-08; ANPRM 2026-03-13), ROSCA enforcement continues, California ARL (from 2025-07-01) is the practical US standard, EU and UK require easy online termination.

## 7. Reviews and incentives

- US FTC rule on consumer reviews and testimonials (final August 2024, effective October 2024): no fake reviews, no review suppression, no incentives conditioned on positive sentiment; disclose material connections [Official, FTC 2024].
- UK DMCC Act: fake reviews and concealed incentivized reviews banned from 2025-04-06; CMA can fine directly [Official, UK 2025].
- EU Omnibus Directive: if a trader publishes reviews, disclose whether and how it checks they come from real purchasers [Official, Directive 2019/2161].

## 8. Data protection operations

- Lawful basis for profiling and segmentation: consent or legitimate interest with an assessment (EU, UK); KVKK explicit consent where required in Turkey.
- Data minimization: ask only for zero party data you will use; avoid special category data.
- Deletion: process deletion requests across ESP, SMS tool, CDP, warehouse and ad platform audiences; Klaviyo offers a data privacy deletion job endpoint [Official, Klaviyo API].
- Processors: DPAs with ESPs; data residency (EU hosting where needed: Klaviyo, Braze and others offer EU data centers on some plans) [Official, vendor docs; verify plan].
- Ad platform uploads of customer lists need a lawful basis and must exclude people who objected ([Lifecycle and paid media](lifecycle-and-paid-media.md)).

## 9. Pre-send compliance checklist (G3 gate)

- [ ] Audience includes only profiles with valid consent for this channel and jurisdiction (or valid soft opt-in) and excludes suppressed, unsubscribed and global control profiles
- [ ] Turkey recipients: İYS status checked at send time
- [ ] France recipients: no individual open tracking without tracking consent
- [ ] US SMS: express written consent records; send window inside quiet hours for each recipient's time zone; state rules checked
- [ ] Sender identity, physical address (CAN-SPAM), unsubscribe link and one click header present; SMS STOP language; WhatsApp opt-out path
- [ ] Offer terms clear (Turkey requires promotion conditions to be stated; EU prior price rule for discounts)
- [ ] Claims only from CLAIMS.md (approved); compliance sign off ID recorded
- [ ] Change request approved by the human listed in GUARDRAILS.md for customer messaging
