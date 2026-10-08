# SMS, RCS, WhatsApp, Push and In-App

Channel rules, costs, consent, timing, copy patterns and the 2025 to 2026 changes for messaging channels. Sending any message is G3. Push and in-app inside a native app are co-owned with `mobile-app-growth` (they own the app SDK, permission prompts and app store context; you own the lifecycle logic and copy).

## 1. Channel selection

| Channel | Best for | Cost model | Consent bar | Avoid when |
|---------|----------|-----------|-------------|-----------|
| Email | Everything; long content; low cost per send | ESP plan by profiles; near zero marginal | Opt-in (or soft opt-in where legal) | Never avoid; it is the base |
| SMS (US 10DLC, toll-free, short code) | High intent and time sensitive: checkout abandonment, back in stock, drops, delivery issues, VIP early access | Per message (ESP fee plus carrier pass-through fees, rising in 2026) | US: prior express written consent for marketing texts sent with automated systems; plus state rules | Low margin products where message cost exceeds incremental margin; markets where WhatsApp dominates |
| RCS | Branded, rich messages in the default messaging app (verified sender, images, buttons) | Per message, by type and destination | Same as SMS | Audiences on devices or carriers without RCS support (fallback to SMS) |
| WhatsApp | Markets where it is the default messenger (EU outside Nordics, UK, Turkey, LATAM, India, MENA, Southeast Asia); conversational commerce; order updates | Per delivered template message by category and country (since 2025-07-01) | Opt-in specific to WhatsApp messages from the business; Turkey: İYS | US marketing (marketing templates to US numbers paused since 2025-04-01) |
| Push (app) | Engaged app users; behavioral triggers | Free per send (SDK, ESP plan) | OS permission (iOS prompt; Android 13+ runtime permission) | Users without app; over sending (uninstalls) |
| Web push | Browser subscribers; content and drops | Low | Browser permission | Low value without strong content cadence |
| In-app messages | Onboarding, feature adoption, offers in session | Plan | None beyond terms; respect consent for tracking | Interrupting core tasks |

Channel cascade rule: email first for low urgency; escalate to SMS or WhatsApp only if not engaged within a window (for example 4 to 24 hours) and only for high intent steps. Never send the same message on three channels at once.

## 2. SMS in the United States

### 2.1 Registration and costs (October 2026)

- Since 2025-02-01 US carriers block A2P traffic on unregistered 10 digit long codes; register brand and campaign with The Campaign Registry (TCR) through your ESP or CPaaS [Secondary, 2026]. Content that drifts from the registered use case can be suspended after approval.
- TCR brand registration fee rose from $4.00 to $4.50 on 2025-08-01; standard vetting about $41.50 [Secondary, 2026; verify with provider].
- Carrier pass-through fees rose through 2026: T-Mobile updated A2P fees 2026-01-19; AT&T raised SMS by $0.0005 and MMS by $0.0015 per message from 2026-04-01; Verizon set registered 10DLC SMS at $0.0045 (2026-05-01) and then $0.0050 per outbound SMS across 10DLC, toll-free and short code from 2026-10-01 (RCS rich MT also $0.0050); further increases by other networks were reported for 2026-11-01 [Secondary, Telgorithm and Tychron carrier notices, 2026; verify on the provider rate card].
- Toll-free verification: new submissions need business registration number, issuing country and entity type (from 2026-01-01, or 2026-02-17 at some providers); one provider reports live privacy policy and terms URLs required from 2026-09-15 [Secondary, 2026; Unverified for the September item].

Budget every SMS program with fully loaded cost per message (ESP fee plus carrier fees plus MMS premium). MMS costs several times SMS; use it only where images lift results in a test.

### 2.2 Consent and opt-in mechanics (summary; law in [Consent and law](consent-and-law.md))

- Marketing texts: prior express written consent with clear disclosure (brand, recurring automated marketing messages, consent not a condition of purchase, message frequency, "Msg and data rates may apply", HELP and STOP instructions, link to terms and privacy).
- The FCC one-to-one consent rule was vacated (2025-01-24) and formally removed (2025-09); consent still must be specific to the seller [Official, court ruling and FCC 2025].
- Double opt-in by reply ("Reply Y to confirm") is common practice and proves consent; Klaviyo, Postscript and Attentive support it [Practitioner consensus].
- Opt-out: honor STOP and reasonable alternatives (for example "unsubscribe", "cancel", "end", "quit") within a reasonable time, at most 10 business days under FCC rules in force since 2025-04-11; a single confirmation text is allowed [Official, FCC 2024 order]. The September 2026 FCC order narrows the "revoke all" scope and lets callers designate an exclusive opt-out method; effective 30 days after Federal Register publication [Official, FCC 2026-09-30; publication unconfirmed as of 2026-10-08].
- Quiet hours: federal 8:00 to 21:00 recipient local time for telephone solicitations; Florida and Oklahoma 8:00 to 20:00 and other state limits (for example frequency caps per 24 hours in Florida) [Official, statutes]. Quiet hours class actions remain active (hundreds of filings and demand letters by late 2025, mostly from one firm per a trade group count; courts split on whether consent defeats quiet hour claims) [Secondary, 2025 to 2026]. Default send window: 10:00 to 20:00 local.

### 2.3 Content rules

- Identify the brand at the start of each message.
- No SHAFT content (sex, hate, alcohol, firearms, tobacco) without proper age gating and carrier approved use cases; cannabis and CBD are restricted [Official, CTIA guidelines].
- Link domains: branded, consistent; public shorteners trigger carrier filters [Practitioner consensus].
- Keep messages under one segment (160 GSM characters, 70 if Unicode or emoji) when cost matters; emoji switch encoding.

### 2.4 iOS 26 "Screen unknown senders"

iOS 26 (September 2025) can move texts from numbers the user has not saved or replied to into a separate Unknown Senders folder with badge only notifications; the setting is off by default in most markets (reported on by default in Brazil, China and India); time sensitive codes appear in the main inbox for one hour [Secondary, Omnisend, Braze, Sinch 2025]. Impact is unmeasured: Apple publishes no adoption rate and Postscript reports no meaningful engagement impact at scale [Contested, vendors 2025 to 2026].

Actions: get recipients to reply (two way welcome: "Reply with your skin type"), offer a contact card (vCard) in the welcome, send useful utility texts (shipping updates) from the same number, and compare click rates of replied vs not replied subscribers in your own data.

### 2.5 SMS frequency and benchmarks

- Typical DTC cadence: 2 to 6 campaigns per month plus flows, higher in peak [Practitioner consensus].
- Omnisend 2025 data (321 million SMS): campaigns 12.39% click through and 0.12% conversion; automated SMS 20.34% click through, 0.77% conversion, $0.74 per send vs $0.15 for campaigns [Study, vendor, 2026]. Click metrics vary by month (3.47% January to 23.92% December in campaigns).
- Vendor claims (Postscript 34x return on SMS spend; Attentive RCS lifts) are self reported [Unverified].

## 3. RCS

- RCS Business Messaging shows verified brand name and logo, rich cards, carousels and suggested reply buttons in the default messaging app; iPhones support RCS since iOS 18 where carriers enable it [Official, Apple and GSMA; carrier support varies].
- Klaviyo lists RCS in the US, UK, France, Germany, Italy, Spain, Sweden, Norway, Denmark, Austria, Poland and Mexico [Official, Klaviyo product page 2026].
- Attentive launched Visibility AI (2026-05-20) to choose between RCS and an existing SMS thread using inbox visibility signals, plus auto upgrade of SMS and MMS to RCS; it reports 45% higher click through, 37% higher conversion and 36% higher revenue per send for RCS vs SMS (early adopter data) [Unverified, vendor 2026-05].
- Iterable added native RCS in its 2026-09-24 Fall release; Braze Conversational Agents cover RCS (beta) [Official, 2026].

Rule: run RCS as an A/B test against SMS on the same consented audience; read revenue per message after fully loaded cost.

## 4. WhatsApp Business Platform

### 4.1 Pricing (verify in WhatsApp Manager before budgeting)

| Date | Change |
|------|--------|
| 2025-04-01 | Delivery of marketing template messages to US phone numbers paused; still paused as of mid 2026 with no lift date (error 131049 on blocked sends) [Secondary, Braze 2026-07 and others] |
| 2025-07-01 | Per message pricing replaced conversation pricing: charges per delivered template by category (marketing, utility, authentication) and recipient country; utility templates inside an open customer service window were free; volume tiers for utility and authentication [Official, Meta developer docs] |
| 2026-08-01 | Meta Business Agent messages billed by tokens [Official, Meta docs via secondary] |
| 2026-10-01 | Per message charges extend to free form service replies inside the 24 hour customer service window after the first 1,000 free service messages per business phone number per month; utility templates in an open window become paid; marketing and authentication pricing unchanged by this step; some country marketing rates rose (Kuwait, Mexico, Morocco, Saudi Arabia, UAE and regional groups) [Official, Meta developer docs; YCloud 2026; rollout not independently confirmed] |
| 2026 | Marketing Messages API for WhatsApp: optional max price per marketing message delivery (beta) [Official, Meta docs; status Unverified] |

Free entry point: conversations started from click to WhatsApp ads (or Facebook Page CTA) open a free 72 hour window [Official, Meta; verify current terms].

Klaviyo bills WhatsApp from the same mobile credit pool as SMS with country dependent credit rates; Klaviyo WhatsApp is for non US destinations [Secondary, 2026]. Braze, Iterable (native WhatsApp in Fall 2026 release), Customer.io (WhatsApp and LINE since April 2026), Bloomreach, Insider, Infobip, Twilio and specialist tools (Charles, Chatarmin and others) also send WhatsApp.

### 4.2 Policies

- Opt-in: obtain opt-in that states the business will send messages on WhatsApp; keep a record. Marketing must respect opt-outs immediately [Official, WhatsApp Business Messaging Policy].
- Templates: business initiated messages outside the 24 hour window must be pre-approved templates in the right category; miscategorized marketing as utility is a policy risk.
- Frequency capping: WhatsApp may limit how many marketing templates a person receives from all businesses in a period; third parties cite about 2 per recipient per 24 hours, but Meta does not publish the number [Unverified]. Blocked sends return error 131049.
- Quality rating and messaging limits depend on blocks and reports; low quality reduces throughput.
- AI chatbots: from 2026-01-15 (2025-10-15 for new accounts) the WhatsApp Business Solution terms bar general purpose AI assistants; task specific business bots (customer service, order inquiries, appointments, product questions) remain allowed. Brazil's competition regulator suspended the policy for +55 numbers and a per message AI provider fee applies there; EU and Italy reviews were ongoing [Official, Meta terms; TechCrunch 2025-10 and 2026-01; status after April 2026 Unverified]. Klaviyo Customer Agent, Braze Conversational Agents and Postscript style shopping assistants are task specific; confirm with the provider.
- Turkey: WhatsApp marketing messages are commercial electronic messages; consent must be registered in İYS before sending [Practitioner consensus; see [Consent and law](consent-and-law.md)].

### 4.3 WhatsApp flow patterns

| Use | Template category | Notes |
|-----|------------------|-------|
| Order confirmation, shipping, delivery | Utility | Strong channel adoption driver; keep promotional content out |
| Cart or checkout abandonment | Marketing | Only with WhatsApp marketing opt-in; counts toward frequency caps |
| Back in stock, price drop | Marketing | Good fit; real time |
| Product questions and assisted selling | Service (user initiated) | Free form inside 24 hour window; now charged beyond the free tier from 2026-10-01 |
| Winback | Marketing | Test against email; cost per message matters |

## 5. Push and in-app (handoff with mobile-app-growth)

- Permission: iOS requires an explicit prompt (provisional authorization delivers quietly to Notification Center); Android 13+ requires runtime permission. Use a pre-permission explainer screen tied to value ("Get notified when your order ships") before the OS prompt [Official, Apple and Android docs; practitioner consensus]. mobile-app-growth owns prompt placement and tests.
- Push cadence: behavior triggered pushes (cart, price drop, back in stock, content the user followed) outperform broadcasts; cap broadcasts and monitor uninstall and opt-out rates [Practitioner consensus]. Omnisend reports 22.9% click to conversion for automated pushes (2025 data, click to conversion, not conversion rate) [Study, vendor 2026].
- In-app messages: onboarding checklists, feature discovery, offers in session; never block core tasks; frequency cap per session.
- ESP support: Klaviyo push (campaigns API supports push since 2025-01-15 revision; push tokens API since 2025-04-15) [Official, Klaviyo API changelog]; Braze, Iterable, Customer.io, OneSignal, Airship are push native.
- Web push: Safari supports web push for home screen web apps on iOS 16.4 and later [Official, Apple WebKit]; value depends on content cadence.

## 6. Copy patterns

SMS welcome (US, after opt-in; fill only with approved facts):
```
<Brand>: You're in! Here's your <promised incentive>: <CODE> (expires <date>). Reply with your <zero party question> so we can send what fits. Msg freq varies. Msg&data rates may apply. Reply HELP for help, STOP to opt out.
```

SMS checkout abandonment:
```
<Brand>: Still thinking it over? Your cart is saved: <link>. Questions? Just reply. STOP to opt out
```

WhatsApp back in stock (marketing template):
```
Hi {{1}}, good news: {{2}} is back in stock in your size. Tap below to grab it before it goes. [Button: Shop now]
```

Push (back in stock):
```
Title: Back in stock: {{product}}
Body: Your size is available again. Tap to check out.
```

Every message: brand identified, one action, opt-out per channel rules, no claims outside CLAIMS.md, compliance review before activation.

## 7. Messaging channel audit questions

- Is consent captured per channel with timestamp, source, method and jurisdiction, and synced to the ESP and (Turkey) İYS?
- Are SMS quiet hours enforced by recipient time zone?
- Is fully loaded cost per message known and is revenue per message read against it?
- Are STOP and opt-out keywords honored within the required time and across systems?
- Are WhatsApp templates categorized correctly, and is the quality rating healthy?
- Is the US audience excluded from WhatsApp marketing templates while the pause lasts?
- Is the cascade logic preventing duplicate messages across email, SMS, WhatsApp and push?
