# Forms, Lead Capture and Booking Flows

> Optimize for qualified pipeline, not form fills. A form change that raises leads 40% and drops SQL rate 50% loses money. Every form decision is judged on cost per qualified lead or cost per opportunity from the CRM (see `ads-master/MEASUREMENT.md`).

## 1. Field audit (do this first)

For each field, fill this table. Remove or defer any field without a "yes" in the first three columns.

| Field | Used to route? | Used to qualify? | Legally required? | Can be enriched or asked later? | Decision |
|-------|---------------|------------------|-------------------|--------------------------------|----------|
| First name | | | | | keep |
| Last name | | | | yes (later) | defer |
| Work email | yes | yes (domain) | | | keep |
| Phone | yes (sales calls) | | | | test optional vs required |
| Company | | yes | | yes (enrichment from email domain) | remove |
| Company size | yes | yes | | yes (enrichment) | keep as select if routing needs it |
| Job title | | yes | | yes (enrichment) | remove or make optional |
| Message | | | | yes | optional, placeholder with example |

Evidence on field count:
- Baymard: most checkouts need only 8 form fields (12 to 14 form elements), while the average checkout had 11.3 fields in 2024 (11.8 in 2021, 12.7 in 2019) [Study, 2024].
- Removing a field often lifts completion, but removing a qualifying field can lower lead quality; that trade-off is the decision, not the field count alone [Practitioner consensus].
- Classic anecdote: Expedia reported removing an optional "Company" field that confused users was worth about $12M per year (2010) [Unverified, widely cited anecdote].

## 2. Single step vs multi-step

Use multi-step when the form has 5 or more fields, needs qualification questions, or benefits from personalization of the next step. Keep single step for 1 to 4 fields.

Multi-step rules:
1. Step 1 is the easiest, most engaging question (a choice with icons: "What do you need help with?"). Do not ask for contact data first.
2. Contact details last, after the visitor has invested.
3. Show progress ("Step 2 of 4") and keep steps to 2 to 5.
4. One topic per step. Auto-advance on single-choice questions.
5. Allow back without losing data. Persist entries in session storage.
6. Capture partial leads only with clear consent and only if the privacy policy covers it (GDPR: be careful; often not allowed without consent).
7. Track every step as an event (section 6).

Evidence: multi-step forms often outperform long single forms in practitioner case studies, but published results are mostly vendor case studies without controls [Contested]. Test it.

## 3. Qualification vs volume

| Goal | Tactic | Watch |
|------|--------|-------|
| More volume, sales team has capacity | Fewer fields, optional phone, instant booking | SQL rate, sales acceptance |
| Higher quality, sales team overloaded | Add qualifying select (budget, timeline, company size), route small leads to self-serve | Lead volume drop, cost per SQL |
| Both | Multi-step with routing: qualified leads get a calendar, others get a resource or self-serve path | Routing accuracy |

Feed quality back to ad platforms: offline conversion import or CRM-based conversion events so bidding optimizes for qualified leads (owned by `measurement` and channel agents). Without this, platform algorithms optimize for form fills of any quality.

## 4. Form UX rules (checklist)

- [ ] Single column layout.
- [ ] Visible labels above fields. Placeholder text is not a label.
- [ ] Correct input types and attributes for mobile keyboards and autofill:

| Field | type | autocomplete | inputmode |
|-------|------|--------------|-----------|
| Email | `email` | `email` | |
| Phone | `tel` | `tel` | |
| First name | `text` | `given-name` | |
| Last name | `text` | `family-name` | |
| Company | `text` | `organization` | |
| Job title | `text` | `organization-title` | |
| Postal code | `text` | `postal-code` | `numeric` only where codes are numeric |
| Street | `text` | `address-line1` | |
| City | `text` | `address-level2` | |
| Card number | `text` | `cc-number` | `numeric` |
| One-time code | `text` | `one-time-code` | `numeric` |

- [ ] Inline validation on blur, not on every keystroke. Error message says how to fix it, next to the field, in text (not color alone).
- [ ] Do not clear fields on error.
- [ ] Phone: accept any format, normalize server side; default country from geo; do not force a format mask that rejects valid input.
- [ ] Mark optional fields "(optional)" rather than marking required ones with asterisks only.
- [ ] Button copy states the outcome ("Get my quote"); disable double submit; show a loading state.
- [ ] No CAPTCHA puzzles. Use a honeypot field, time-to-submit check and an invisible challenge (for example Cloudflare Turnstile).
- [ ] Privacy line under the button: what happens next, response time, no spam promise.
- [ ] Marketing consent checkbox unticked by default where GDPR or similar applies.
- [ ] Tap targets at least 44 x 44 px (WCAG 2.2 minimum is 24 x 24 CSS px).
- [ ] Success state: tell them what happens next and when; offer the next step (book a time, download, watch video).

## 5. Native lead forms vs website forms

| Option | Strength | Weakness | Judge on |
|--------|----------|----------|----------|
| Meta Instant Forms (More volume) | Lowest friction, prefilled | Lowest intent, accidental submits | Contact rate, SQL rate |
| Meta Instant Forms (Higher intent) | Review step adds friction that filters | Lower volume | Cost per SQL |
| Google Lead Form assets | Prefilled from Google account | Limited questions, quality varies | Cost per SQL |
| LinkedIn Lead Gen Forms | Prefilled professional data, high B2B completion | Quality varies by offer | Cost per opportunity |
| TikTok instant forms | Volume | Quality often low for high ticket | Contact rate |
| Website form | Full control, richer context, better quality signals | More friction | Cost per SQL |

Always connect native forms to the CRM in real time (native integrations or Zapier type tools) and call fast. Speed to lead: the Harvard Business Review study of 2,241 US companies found firms contacting leads within an hour were nearly 7 times as likely to qualify them as those waiting longer (2011) [Study, 2011].

## 6. Form analytics

### 6.1 Metrics
| Metric | Formula | Healthy signal |
|--------|---------|----------------|
| Form view rate | form views / page sessions | Low means form is below the fold or hidden |
| Start rate | form starts / form views | Low means intimidating form or weak offer |
| Completion rate | submits / starts | Low means friction inside the form |
| Field drop-off | sessions whose last interaction was field X / starts | Identifies the killer field |
| Field correction rate | refills or errors on field X / interactions with X | Validation or label problem |
| Time per field | median seconds | Long time means confusing question |
| Lead to SQL rate | SQLs / leads (from CRM) | The real quality metric |

### 6.2 Tools
Zuko (form analytics), Contentsquare (Hotjar) form analysis, Clarity recordings filtered by form page, PostHog, or custom events into GA4. GA4 enhanced measurement `form_start` and `form_submit` miss many forms; implement custom events.

### 6.3 Field-level tracking snippet (dataLayer, framework agnostic)
```html
<script>
(function () {
  var form = document.querySelector('form[data-track-form]');
  if (!form) return;
  var formId = form.getAttribute('data-track-form');
  var started = false, lastField = null;
  window.dataLayer = window.dataLayer || [];
  form.addEventListener('focusin', function (e) {
    if (!e.target.name) return;
    if (!started) { started = true; dataLayer.push({event: 'form_start_custom', form_id: formId}); }
    lastField = e.target.name;
  });
  form.addEventListener('change', function (e) {
    if (!e.target.name) return;
    dataLayer.push({event: 'form_field_complete', form_id: formId, field_name: e.target.name});
  });
  form.addEventListener('invalid', function (e) {
    dataLayer.push({event: 'form_field_error', form_id: formId, field_name: e.target.name});
  }, true);
  form.addEventListener('submit', function () {
    dataLayer.push({event: 'form_submit_attempt', form_id: formId});
  });
  window.addEventListener('pagehide', function () {
    if (started && lastField) dataLayer.push({event: 'form_abandon', form_id: formId, last_field: lastField});
  });
})();
</script>
```
Never push field values (personal data) to analytics. Fire the conversion only on server-confirmed success (thank you state or `generate_lead` after a 200 response), not on submit attempt. Coordinate event names with the `measurement` agent.

## 7. Booking flows and B2B demo pages

### 7.1 Demo page anatomy
1. Headline: outcome of the demo, not "Request a demo" ("See how teams like yours cut month-end close to 3 days").
2. What happens in the demo (3 bullets: tailored walkthrough, answers on pricing, 30 minutes).
3. Short form (work email, company size, one qualifier). Enrich the rest.
4. Instant scheduling on submit for qualified leads (Chili Piper, HubSpot Meetings, Calendly Routing, SavvyCal, Default). Show the calendar on the thank you state, not an email later.
5. Proof next to the form: logos from the same industry, one quantified case study, G2 or Capterra rating.
6. Alternatives for not-ready visitors: interactive product tour, pricing page, recorded demo.

### 7.2 Booking flow rules
- Show next available slots in the visitor's time zone. Fewer, sooner slots beat a full month view [Practitioner consensus].
- Confirm by email and calendar invite immediately; send reminders (24 h and 1 h). SMS reminders where consent allows.
- Track: demo booked, demo held, show rate, opportunity created. Optimize for held demos.
- Unqualified leads: route to self-serve or a resource, do not leave them with "we will be in touch".

### 7.3 Local services
- Click to call in the hero and sticky; track calls with dynamic number insertion (CallRail or similar); calls often outnumber forms.
- Quote form: service type, postcode, preferred time, name, phone. 5 fields.
- Show response time promise and working hours. Offer online booking where the business can honor it.
- Instant price estimate or range increases form starts for price-sensitive services [Practitioner consensus].

## 8. Lead magnets and gated content
- Gate only content worth an email to the target segment (templates, benchmarks, tools). Ungate thought leadership.
- One-field gate (email) for top of funnel; enrich the rest.
- Deliver instantly on the thank you page and by email.
- Track lead magnet to SQL rate; many lead magnets produce leads that never buy.

## 9. Spam and validation
- Honeypot field hidden with CSS (not `type=hidden`), rejected server side if filled.
- Minimum time to submit (for example 3 seconds).
- Invisible challenge (Turnstile, reCAPTCHA v3) with server verification.
- Email validation: syntax plus MX check server side; optional real-time verification for paid lead gen.
- Block disposable domains for B2B trials if abuse appears.
- Spam leads inflate CPL math and train ad algorithms on junk. Exclude spam before sending conversions to platforms.

## 10. Consent and compliance on forms
- GDPR and UK GDPR: separate marketing consent from the request; unticked; link privacy policy; state purpose.
- US TCPA for calls and texts: consent language for automated calls or texts. The FCC one-to-one consent rule was vacated by a federal court in January 2025 [Unverified, verify], but express written consent rules still apply. Get legal review for lead gen in insurance, finance, solar, home services.
- Health data: HIPAA in the US; do not pass form contents or health conditions to ad pixels.
- Accessibility: labels, error identification, keyboard operation (see [Audit checklist](audit-checklist.md) section K).

## 11. Form test ideas (ranked by typical impact) [Practitioner consensus]
1. Offer and CTA framing ("Get my free quote in 60 seconds" vs "Contact us").
2. Remove or defer non-routing fields.
3. Multi-step with an engaging first question.
4. Instant booking on submit.
5. Phone optional vs required (watch contact rate).
6. Form position (above the fold vs after proof) on mobile.
7. Social proof and privacy line next to the button.
8. Native lead form vs website form (judge on SQL cost).

## 12. Form spec template
```
# Form spec: <form name> | Page: | Goal (lead, booking, quote):
Fields: name | type | autocomplete | required | validation | purpose (route/qualify/legal)
Steps (if multi-step): step -> fields -> progress label
Routing rules: condition -> destination (calendar, nurture, sales rep)
Success state copy and next step:
Events: form_view, form_start_custom, form_field_complete, form_field_error, form_submit_attempt, generate_lead (server confirmed)
CRM mapping: field -> CRM property; source and UTM fields captured as hidden inputs
Consent text:
Spam protection:
QA: devices, in-app browsers, CRM receipt, conversion fires once
```
