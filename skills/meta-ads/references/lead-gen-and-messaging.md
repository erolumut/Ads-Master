# Lead Generation and Messaging

> Knowledge as of 2026-10. Lead gen on Meta fails on quality, not volume. Optimize to what sales accepts, and feed CRM outcomes back to Meta.

## 1. Choose the lead path

| Path | Conversion location | Best for | Quality risk | Speed to lead |
|------|--------------------|----------|-------------|---------------|
| Instant forms | Instant forms | Local services, B2C high volume, mobile-first audiences | High with "More volume" forms | Needs instant CRM sync |
| Website forms | Website | B2B, high consideration, when site qualifies better | Lower; higher CPL | Normal |
| Click to message | Messenger, Instagram Direct, WhatsApp | Markets where chat is the norm (Turkey, LATAM, MENA, South and Southeast Asia), local services, ecommerce with consultative sale | Medium; needs fast response | Must respond within minutes |
| Calls | Calls | Urgent local services (plumbing, legal, towing) | Low to medium | Staffed hours required |
| Hybrid | Website and instant forms or messaging where offered | Testing paths | n/a | n/a |

## 2. Instant form setup

Form types [Official]:
| Type | Behavior | Use |
|------|----------|-----|
| More volume | Short, prefilled, fast submit | Only when sales can call fast and lead value is low |
| Higher intent | Adds a review step where the person confirms details before submitting | Default for most businesses |
| Rich creative | Adds visual intro section about the business | Brand-heavy or new categories |

Form build checklist:
1. Intro: who it is for and what happens next (sets expectations, reduces junk).
2. Questions: prefilled contact fields (email, phone, name) plus 1 to 3 custom qualifying questions (budget, timeline, location, use case). Use multiple choice for routing; conditional logic for branching.
3. Avoid all-prefill forms for high-value services; one short-answer question reduces accidental submissions.
4. Privacy policy link and any required consents (marketing consent checkboxes, KVKK or GDPR language).
5. Completion screen: clear next step, call button or website link, calendar link for B2B.
6. Hidden fields for campaign, ad set and ad IDs where available, or rely on lead_id with ad attribution in the CRM sync.
7. Connect the CRM: native integrations (Salesforce, HubSpot, Zoho, and others in Leads Center or via partners like Zapier or LeadsBridge). Test with the Lead Ads Testing Tool. Sync must be near real time.

Response time standard: call or message instant form leads within 5 minutes during business hours [Practitioner consensus]; quality "problems" are often follow-up problems.

## 3. Conversion leads optimization

What it does: optimizes delivery toward leads likely to reach a deeper CRM stage rather than raw form submits [Official].
Setup:
1. Integrate CRM with Meta via Conversions API for CRM (lead_id from Meta captured in the CRM; or hashed email and phone).
2. Map lead stages in Events Manager (for example: Lead > Marketing qualified > Sales qualified > Won). Choose the optimization stage.
3. Send stage updates at least daily; reported eligibility thresholds include roughly 200+ leads per month and a stage conversion rate between about 1% and 40% [Unverified, verify current Help Center requirements].
4. Create the Leads campaign with performance goal "Maximize number of conversion leads".
5. Expect CPL to rise and cost per qualified lead to fall. Judge on cost per SQL and close rate after 2 to 4 weeks.

If the account cannot meet thresholds: optimize to leads, but send quality stages anyway (they improve learning and enable value rules), and use higher intent forms.

## 4. Lead quality playbook

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Fake or unreachable contacts | More volume form, incentives, Audience Network | Higher intent form, add a short-answer question, phone verification where available, placement value rule down on Audience Network |
| Leads from wrong geo | Location type, broad geo | Location control strict, ask location in form |
| Low intent ("just browsing") | Creative promises free or easy outcome | Qualify in copy (price anchor, who it is not for), add budget or timeline question |
| Sales says leads are cold | Slow follow-up | Fix speed to lead first; measure time to first contact |
| CPL fine, close rate falling | Optimization on raw leads | Conversion leads optimization, cost per SQL target |
| Duplicates | Retargeting, repeat submits | Exclude existing leads list, dedupe in CRM |

Lead quality KPIs to report weekly: CPL, contact rate, qualification rate (MQL or SQL %), cost per SQL, close rate, cost per customer, time to first contact. Pull from CRM; label source.

## 5. Website lead gen

- Fire Lead on the thank-you state (not on button click) via Pixel and CAPI with event_id dedup.
- Send downstream stages (Qualified, SQL, Won) as custom events via CAPI with the same identifiers (email, phone, external_id) so Meta can match.
- Use value on stages (expected value = deal value x stage-to-close probability) to enable value optimization later.
- For B2B, enrich and filter (block free email domains only if sales confirms they never convert).

## 6. Click to message ads

Destinations: Messenger, Instagram Direct, WhatsApp, or multiple (Meta chooses).
| Setting | Recommendation |
|---------|----------------|
| Performance goal | Maximize conversations to start; switch to leads or purchases through messaging once business messaging events are sent via Conversions API |
| Message template | Greeting plus 3 to 5 ice breaker questions that pre-qualify ("Price for 2 people?", "Book for this week") |
| Automation | Instant reply, FAQ automation, or a business AI agent where available; human handoff within business hours |
| Hours | If chats are not staffed 24/7, set expectations in the greeting and use ad scheduling with lifetime budget only if after-hours leads are wasted |
| Tracking | Label chats (lead, qualified, booked, purchase) in the inbox or CRM; send those events back via Conversions API for business messaging |

WhatsApp specifics:
- WhatsApp Business Platform moved to per-message pricing on 2025-07-01 [Official, 2025]. Conversations started from click to WhatsApp ads have a free entry point window (72 hours historically), during which business messages are free [Official, long-standing]; a 7-day free window for click to WhatsApp ads was reported in September 2026 [Unverified, 2026-09]. Verify current pricing before forecasting.
- Use the WhatsApp Business app for small teams, the WhatsApp Business Platform (Cloud API via a BSP) for scale and CRM integration.
- Opt-in rules apply for marketing messages after the chat window; respect local consent law (KVKK in Turkey, GDPR in EU).

Messaging KPIs: cost per conversation, reply rate within 5 minutes, qualified conversation rate, cost per qualified conversation, conversion to booking or sale, revenue per conversation.

## 7. WhatsApp Status ads and Promoted Channels

| Date | Event | Label |
|------|-------|-------|
| 2025-06-16 | Meta announced ads in Status, Promoted Channels and channel subscriptions in the WhatsApp Updates tab; ads never shown in personal chats | [Official, 2025-06] |
| 2025-09 | Click to message ads in Status reported | [Unverified, 2025-09] |
| 2026-02 | Promoted Channels and ads in Status reported rolling out globally after limited tests | [Official, 2026-02] via trade press |
| EU | Irish DPC indicated no WhatsApp ads in the EU until 2026; EU rollout lags | [Official, 2025] via Silicon Republic |
| 2026-08 | WhatsApp campaign management and Status placement inside Ads Manager reported | [Unverified, 2026-08] |

Targeting for Status ads uses city or country, language, channels followed and ad interactions; Meta states phone numbers are not shared with advertisers [Official, 2025-06]. Practical use: include WhatsApp Status inside Advantage+ placements where available; judge by placement breakdown with breakdown-effect caution; for chat-led markets build creative that sends people into WhatsApp chats.

## 8. Calls ads

- Objective Leads or Sales with Calls conversion location; set call hours.
- Optimize to calls, or to quality calls (calls above a duration) where offered [Unverified availability].
- Track calls with a call tracking provider and send qualified calls back via Conversions API.

## 9. Templates

Local service lead campaign (Growth tier):
```
Campaign: TR-IST_LEADS_ADV+_LEAD_HV_20261015
  Ad set: Advantage+ audience, controls: Istanbul +25 km, 25+; placements Advantage+; value rule: Audience Network minus 50%
  Form: Higher intent; questions: district (multiple choice), service type, timeline (this week / this month / later); completion: call button
  Ads: 5 concepts (before/after where policy allows, team intro, price transparency, reviews, guarantee)
  CRM: native sync to CRM, stages New > Contacted > Qualified > Booked > Won; daily CAPI sync
  Exit to conversion leads optimization when Qualified stage reaches volume requirements
```

B2B SaaS lead campaign (Growth tier):
```
Campaign: US_LEADS_MANUAL_SQL_CPRGOAL_20261015
  Conversion location: Website; event: CompleteRegistration (trial) until SQL volume allows, then custom SQL event via CAPI
  Audience: Advantage+ audience with customer list suggestions; exclude current customers and open opportunities
  Creative: problem-led demos, customer proof, founder POV; job-title callouts in the first line
  Measurement: CRM stage events with value; weekly cost per SQL review
```

## 10. Handoffs

- CRM integration and CAPI for CRM implementation: `measurement`.
- Form and landing page conversion rate work: `cro`.
- Messaging scripts, hooks and creative concepts: `creative-strategy`.
- B2B account-based reach on LinkedIn: `linkedin-ads`.
