# Privacy in Marketing, Consent and Accessible Pages

> Knowledge as of 2026-10. Rule pack for consent to email, SMS, calls and messaging, cookie and pixel consent as it affects marketing copy and forms, health and sensitive data in ad targeting, children, and the accessibility of marketing pages under the European Accessibility Act. Tracking implementation (CMPs, consent mode, CAPI) belongs to measurement; flows and lists to lifecycle-crm; page builds to cro and site-engineer. This module checks the customer facing words, forms and audience rules.

## 1. Email, SMS and messaging consent by market

| Rule ID | Market | Rule | Source |
|---------|--------|------|--------|
| PRIV-EU-01 | EU | Electronic mail marketing (email, SMS, MMS) to natural persons needs prior consent; soft opt-in for existing customers: contact obtained in the context of a sale, marketing of own similar products, clear opt-out at collection and in every message. Member states differ for legal persons | ePrivacy Directive 2002/58/EC Art 13 [Official, canonical] |
| PRIV-EU-02 | EU | Consent must be freely given, specific, informed, unambiguous, by clear affirmative action, as easy to withdraw as to give; no pre-ticked boxes; keep proof. Right to object to direct marketing is absolute (GDPR Art 21(2) and (3)). Legitimate interest can cover some direct marketing (Recital 47; CJEU C-621/22 KNLTB, 2024-10-04: commercial interests can be legitimate) but never replaces ePrivacy consent for email or SMS | GDPR Art 4(11), 7, 21 [Official] |
| PRIV-DE-01 | Germany | Email advertising needs prior express consent (double opt-in is the evidence standard in practice); existing customer exception in UWG § 7(3); phone advertising to consumers needs prior express consent, documented and kept for 5 years (UWG § 7a since 2021-10-01) | UWG [Official, canonical] |
| PRIV-NL-01 | Netherlands | Opt-in for email to natural persons including sole traders (Telecommunicatiewet Art 11.7); telemarketing opt-in since 2021-07-01; ACM enforces | [Official, canonical] |
| PRIV-UK-01 | UK | PECR regulation 22 (consent or soft opt-in for email and SMS). Data (Use and Access) Act 2025 commencement 2026-02-05: PECR fines raised to the UK GDPR level (up to GBP 17.5 million or 4% of worldwide turnover); new cookie exemptions (Schedule A1: for example first-party analytics and functionality cookies with clear information and a simple right to object; advertising and tracking still need consent); charitable purposes soft opt-in for charities (not retrospective; ICO guidance 2026-04-28) | Clifford Chance 2026-02; Lewis Silkin 2026-05-08 [Official via secondary] |
| PRIV-US-01 | US email | CAN-SPAM: no opt-in required for commercial email, but no false or misleading headers, no deceptive subject lines, identify the message as an ad (unless prior affirmative consent), include a valid physical postal address, a clear opt-out that works for at least 30 days after sending and is honoured within 10 business days; the brand is liable for vendors. Civil penalties per email (USD 53,088 in the 2025 adjustment; check current) | FTC CAN-SPAM guide [Official] |
| PRIV-US-02 | US SMS and calls | TCPA: prior express written consent for marketing calls and texts using an autodialer or prerecorded voice; quiet hours (no calls before 08:00 or after 21:00 recipient local time); National Do Not Call Registry. The FCC one-to-one consent rule was vacated (11th Circuit, Insurance Marketing Coalition v. FCC, 2025-01-24) and formally removed (effective 2025-08-29): consent may name multiple sellers but must be clear and specific. Revocation: consumers may revoke by any reasonable means; a marketing opt-out applies to all future marketing from that caller. FCC Report and Order adopted 2026-09-30 (released 2026-10-01) narrows the "revoke all" rule for informational messages and lets businesses designate an exclusive opt-out method; effective 30 days after Federal Register publication (not confirmed as of 2026-10-08). State mini-TCPAs (Florida, Oklahoma, Maryland and others) add private rights of action | Pierce Atwood 2025-01; Goodwin 2025-09; Troutman 2026-10 [Official via secondary] |
| PRIV-TR-01 | Turkey | Commercial electronic messages (SMS, email, calls, WhatsApp) to consumers need prior consent (onay) under Law 6563 and the Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik; senders must register in İYS (İleti Yönetim Sistemi) and may not send to recipients without İYS consent; traders and craftsmen (tacir, esnaf) can be messaged on an opt-out basis but still through İYS; consent obtained via İYS needs a positive declaration and the contact address; greeting messages (holiday or birthday wishes) that build brand recognition count as commercial messages; since 2025-03-31 consent and rejection changes reportedly go only through official İYS integrators | iys.org.tr; law firm summaries [Official]; integrator rule [Unverified] |
| PRIV-TR-02 | Turkey | KVKK: processing personal data for marketing needs explicit consent (açık rıza) separate from the İYS commercial message consent and separate from the information notice (aydınlatma metni). KVKK principle decision 2025/1072 (2025-06-10, Official Gazette 2025-06-26): making a commercial message consent compulsory through an SMS verification code during a purchase or membership is invalid; membership, data processing and commercial message consents cannot be bundled in one SMS code; marketing consent may be asked separately after the transaction. A 2026/347 principle decision on separating explicit consent and information texts is reported | Gün + Partners 2025 [Official via secondary]; 2026/347 [Unverified] |
| PRIV-TR-03 | Turkey | Targeted advertising (from 2026-08-01): advertisers must give consumers direct and easily accessible information on the criteria used to show them an ad and how to change them; profiling based targeted ads are prohibited where the user is known or reasonably expected to be a child | Ticari Reklam Yönetmeliği Art 25/A as amended [Official via secondary] |
| PRIV-MENA-01 | UAE, Saudi Arabia | UAE PDPL (Federal Decree-Law 45/2021) and Saudi PDPL (in force 2023-09-14, enforcement from 2024-09-14) require consent or another basis for marketing and give opt-out rights; telecom regulators (TDRA, CST) regulate promotional SMS with sender registration | [Practitioner consensus; verify implementing rules] |

### 1.1 Consent wording checks (copy level)
1. The checkbox text names the channel(s) (email, SMS, WhatsApp, calls), the sender, the purpose (marketing) and that consent can be withdrawn at any time, with how.
2. Unticked by default; not a condition of purchase (EU, UK, TR KVKK 2025/1072).
3. Separate boxes for separate purposes (marketing vs profiling vs third party sharing).
4. US SMS: disclose message frequency, "Msg and data rates may apply", STOP and HELP instructions, link to terms and privacy (carrier and CTIA practice) [Practitioner consensus].
5. Every marketing email: sender identity, physical address (US), unsubscribe link that works without login.
6. Turkey: İYS registration line and that consent is recorded in İYS.
7. Popups that collect email: discount terms clear ("10% off your first order over 50 EUR, excludes sale items"), no pre-ticked boxes.

## 2. Cookies and pixels: what the copy must say

| Rule ID | Rule | Source |
|---------|------|--------|
| PRIV-COOKIE-01 | EU and UK: non essential cookies and similar technologies (ad pixels, server side identifiers tied to device storage) need prior consent; reject as easy as accept; no cookie walls in most authorities' view [Contested by country] | ePrivacy Art 5(3); CJEU Planet49 (2019); PECR as amended 2026 |
| PRIV-COOKIE-02 | Turkey: KVKK cookie guidance (2022): explicit consent for analytics and advertising cookies; rejecting as easy as accepting | KVKK guidance [Official] |
| PRIV-COOKIE-03 | Privacy notice names ad platforms receiving data (Meta, Google, TikTok, Microsoft, LinkedIn, OpenAI pixel and CAPI), purposes, transfers (KVKK Art 9 transfer mechanism since 2024-06-01) | See measurement module |

## 3. Sensitive data, health data and ad targeting

| Rule ID | Rule | Source |
|---------|------|--------|
| PRIV-SENS-01 | EU: health, religion, sexual orientation and other special category data need explicit consent (GDPR Art 9); online platforms may not present ads based on profiling using special category data (DSA Art 26(3)) or profiling based ads to minors (DSA Art 28(2)) | [Official] |
| PRIV-SENS-02 | US Washington My Health My Data Act (in force since 2024-03-31): consent to collect and share consumer health data, signed authorisation to sell, geofencing ban near health facilities, private right of action through the state consumer protection act. Litigation: Amazon Ads SDK case (filed 2025-02-10, pending as of 2026-05); Uncle Ike's cannabis retailer pixel suit (2025-11). No AG action announced as of 2026-05 | Benesch 2026; Hintze Law 2025-11 [Official via secondary] |
| PRIV-SENS-03 | US Maryland Online Data Privacy Act (in force 2025-10-01): bans the sale of sensitive data including consumer health data even with consent and limits processing to what is strictly necessary; treat health audience uploads and conversion sharing to ad platforms as prohibited for Maryland residents unless counsel says otherwise | [Practitioner reading via Benesch, Paubox 2026] |
| PRIV-SENS-04 | US: Connecticut bans geofencing within 1,750 feet of mental, reproductive or sexual health facilities; New York bans geofencing around health care facilities for ads; New York Health Information Privacy Act vetoed 2025-12, revised bill (A.10357/S.9269) pending | MoFo 2026-03-16 [Official via secondary] |
| PRIV-SENS-05 | US FTC: Health Breach Notification Rule (amended 2024) and cases on sharing health data with ad platforms (GoodRx USD 1.5 million penalty; BetterHelp USD 7.8 million refunds; Premom; Cerebral); HIPAA covered entities: tracking technology guidance partly vacated in 2024 but PHI rules still apply | [Official] |
| PRIV-SENS-06 | Platforms: Meta restricts health and wellness advertisers' data use (2025); Google personalized advertising policy bans targeting by health conditions and other sensitive categories; LinkedIn restricts health targeting; OpenAI does not serve ads in personal health or mental health conversations | Platform policies [Official] |

Copy implications: never say or imply "we know you have X" (also a Meta personal attributes breach); do not build retargeting audiences from symptom or condition pages; health funnels use contextual targeting and aggregated measurement.

## 4. Children and teens

| Rule ID | Rule | Source |
|---------|------|--------|
| PRIV-KIDS-01 | EU DSA Art 28: no profiling based ads to minors on online platforms; Commission guidelines on minors' protection (2025-07) | [Official] |
| PRIV-KIDS-02 | US COPPA (amended rule effective 2025, compliance 2026-04-22 for most changes [verify]): verifiable parental consent before collecting data from children under 13, including for targeted ads | FTC [Official; dates verify] |
| PRIV-KIDS-03 | UK: ICO Age Appropriate Design Code; CAP Code section 5 (children) | [Official] |
| PRIV-KIDS-04 | Turkey: child profiling targeted ads prohibited from 2026-08-01 (PRIV-TR-03) | [Official via secondary] |
| PRIV-KIDS-05 | Restricted categories (alcohol, gambling, HFSS in the UK, weight loss, supplements, cosmetic procedures, dating, crypto) never target or appeal to minors | Category packs |

## 5. Marketing form and flow review checklist

| # | Check | Fail verdict |
|---|-------|--------------|
| 1 | Consent checkbox per channel, unticked, purpose and withdrawal stated | BLOCKED (EU, UK, TR) |
| 2 | Marketing consent not bundled with purchase, account creation or SMS verification code (TR 2025/1072) | BLOCKED |
| 3 | İYS registration and sync confirmed for TR sends | BLOCKED until confirmed |
| 4 | US SMS: express written consent language, frequency, STOP and HELP, quiet hours rule | APPROVED WITH EDITS |
| 5 | Every email has unsubscribe and sender identity (plus postal address for US) | APPROVED WITH EDITS |
| 6 | No health or sensitive inference in copy or audience build | BLOCKED |
| 7 | Privacy notice lists ad platforms and pixels used | Handoff to measurement |
| 8 | Children: no profiling ads; age gates for restricted categories | BLOCKED |
| 9 | Targeted ad criteria information available to TR consumers (2026) | Handoff to channel agents and site-engineer |
| 10 | Chatbots disclose AI (EU Art 50(1)) | APPROVED WITH EDITS |

## 6. Accessibility basics for marketing pages (European Accessibility Act)

| Rule ID | Rule | Source |
|---------|------|--------|
| ACC-EU-01 | Directive (EU) 2019/882 applies from 2025-06-28 to e-commerce services, consumer banking, e-books, transport ticketing and other listed products and services sold to EU consumers, including by non-EU sellers. Websites and apps of these services must meet the WCAG principles (perceivable, operable, understandable, and compatible with assistive technologies); the harmonised standard EN 301 549 maps to WCAG 2.1 AA in practice | Directive 2019/882 [Official, canonical]; standard mapping [Practitioner consensus] |
| ACC-EU-02 | Microenterprise exemption only for service providers with fewer than 10 employees and annual turnover or balance sheet total of at most EUR 2 million; interpreted narrowly; document eligibility | Taylor Wessing 2025 [Official via secondary] |
| ACC-EU-03 | Service providers publish accessibility information (how the service meets the requirements), usually an accessibility statement | Annex V [Official, canonical] |
| ACC-EU-04 | Enforcement 2026: Netherlands ACM found 61% of about 100 of the largest Dutch online stores not accessible (2026-03; dialogue first, enforcement for laggards; inaccessible buttons and CAPTCHAs block purchases); Germany BFSG fines up to EUR 100,000 for listed breaches plus competitor warnings; France: two disability organisations sued Auchan, Carrefour, E.Leclerc and Picard (2025-11-12). No public authority fine on an e-commerce site confirmed as of 2026-10 | ACM 2026-03; Taylor Wessing 2026-06 [Official via secondary] |

Compliance agent checks on every landing page review (then hands fixes to cro and site-engineer):
1. Text alternatives on product images that carry claims (the claim in an image must also be in text).
2. Price, discount and subscription terms readable by screen readers (not only in images or strikethrough styling).
3. Video ads and page videos captioned; disclosures not only spoken or only visual.
4. Colour contrast of disclaimers and terms (small grey text on white often fails).
5. Consent banners and checkout keyboard operable; CAPTCHAs have accessible alternatives.
6. Accessibility statement linked in the footer for EU e-commerce.

## 7. Consent text templates (adapt with counsel)

```text
EN (EU/UK email and SMS):
[ ] Yes, send me news and offers from <Brand> by email and SMS. I can unsubscribe at any time via the link in each message or in my account. See our Privacy Notice.

DE (E-Mail):
[ ] Ja, ich möchte den Newsletter von <Brand> mit Angeboten per E-Mail erhalten. Die Einwilligung kann ich jederzeit über den Abmeldelink widerrufen. Datenschutzhinweise.
(Double opt-in confirmation email follows.)

TR (ticari elektronik ileti, separate from the KVKK explicit consent box):
[ ] <Marka> tarafından kampanya ve tanıtımlarla ilgili SMS ve e-posta ile ticari elektronik ileti gönderilmesine onay veriyorum. Onayımı dilediğim zaman geri alabilirim. Onayım İYS'ye kaydedilir.

US SMS (express written consent):
By checking this box, I agree to receive recurring automated marketing text messages from <Brand> at the number provided. Consent is not a condition of purchase. Msg frequency varies. Msg and data rates may apply. Reply STOP to cancel, HELP for help. Terms and Privacy: <links>.
```

## 8. Worked examples

| Situation | Market | Verdict | Rule | Fix |
|-----------|--------|---------|------|-----|
| Checkout box pre-ticked "Send me offers" | DE | BLOCKED | PRIV-EU-02, PRIV-DE-01 | Unticked box plus double opt-in |
| Account sign up SMS code that also activates marketing consent | TR | BLOCKED | PRIV-TR-02 | Separate marketing consent after the transaction; İYS record |
| SMS campaign at 22:30 recipient time | US | BLOCKED | PRIV-US-02 | Schedule 08:00 to 21:00 local |
| Email to past customers about similar products, opt-out offered at purchase and in every email | UK | APPROVED | PRIV-UK-01 soft opt-in | Keep evidence of the opt-out at collection |
| Lookalike audience seeded from users who visited a diabetes symptom page | US (WA, MD) | BLOCKED | PRIV-SENS-02, PRIV-SENS-03 | Contextual targeting only |
| Ad copy "Because you searched for anxiety help" | Meta, all | BLOCKED | PRIV-SENS-06, PLAT-META-01 | Remove the inference |
| Chatbot on the PDP answers as "Emma from our team" without AI notice | EU | APPROVED WITH EDITS | AI-EU-03 | "Emma (AI assistant)" and a human handover option |
| Price only in an image banner without text alternative | EU | APPROVED WITH EDITS | ACC-EU-01 | Add the price and terms as text |

## 9. Retention of consent evidence

Keep, per contact: timestamp, source (form, page URL, campaign), exact consent text version, IP or device signal where lawful, double opt-in confirmation (DE practice), İYS record ID (TR), and every opt-out. Keep the consent text versions in the repository so a regulator can see what the person agreed to. Measurement and lifecycle-crm hold the data; compliance checks the wording and the process.
