# B2B Nurture, Lead Scoring and Sales Handoff

Lifecycle for lead gen, B2B SaaS and local services: speed to lead, nurture tracks, scoring models, MQL definitions and SLAs, closed loop feedback, product led onboarding and the tools (HubSpot first). Paid lead generation itself belongs to the channel agents; offline conversion import belongs to `measurement`; ABM ads to `linkedin-ads`.

## 1. Funnel definitions (agree with sales; record in METRICS.md)

| Stage | Entry rule (example) | Owner | SLA |
|-------|---------------------|-------|-----|
| Lead | Any known contact with consent or legitimate interest basis | Marketing | Immediate auto response |
| MQL | Fit score A or B AND engagement threshold, or hand raiser (demo, pricing contact, quote request) | Marketing | Route within minutes |
| SAL (accepted) | Sales accepts within SLA | Sales | Accept or reject within 1 business day |
| SQL or opportunity | Qualified meeting held, budget and need confirmed | Sales | |
| Customer | Closed won | Sales or CS | |
| Recycled | Rejected or lost with reason | Marketing nurture | Re-score after 30 to 90 days |

Hand raisers (demo request, contact sales, quote) skip scoring and go straight to sales. Scoring is for everyone else.

## 2. Speed to lead (the biggest lever in lead gen)

- Instant confirmation email and, where consented, SMS with next step (booking link, what happens next, who will call).
- Routing: round robin or territory in the CRM; calendar booking inline for qualified forms (Chili Piper, HubSpot meetings, Calendly, Default) [Practitioner consensus].
- Local services: call or text back in minutes during business hours; out of hours auto reply with booking link.
- Measure median time to first human contact; report it weekly with lead to opportunity rate by response time band.

## 3. Lead scoring

### 3.1 Model structure

Two separate dimensions, then a combined grade:

| Dimension | Inputs | Decay |
|-----------|--------|-------|
| Fit | Firmographics (industry, size, region), role and seniority, tech stack, ICP match from closed won analysis | No time decay; changes when the record changes |
| Engagement | Pricing page views, demo page visits, webinar attendance, high intent content, email clicks (not opens), product usage (PLG), replies | Decay over 30 to 90 days |

HubSpot's current Lead Scoring tool (Marketing > Lead Scoring; Marketing Hub Professional and Enterprise) builds fit, engagement or combined scores for contacts, companies and deals, with a combined grid A1 to C3 (letter = fit, number = engagement). The legacy HubSpot Score property was retired: new legacy scores blocked from 2025-05-01 and existing ones stopped updating on 2025-08-31, with no automatic migration [Official, HubSpot announcement 2025-02; agency summaries 2025]. Audit any portal still using the legacy property in workflows, lists or reports.

### 3.2 Build from data, not opinion

1. Pull 12 to 24 months of closed won and closed lost (or SQL vs non SQL) leads.
2. For each attribute and behavior, compute conversion rate to opportunity vs the base rate (lift).
3. Assign points proportional to lift; cap any single behavior.
4. Choose the MQL threshold that balances volume and sales capacity (precision vs recall); review with sales.
5. Validate on a holdout period; re-calibrate quarterly.

```sql
-- Lift of a behavior on opportunity creation (example schema)
SELECT behavior,
       COUNT(DISTINCT lead_id) AS leads_with_behavior,
       AVG(CASE WHEN became_opportunity THEN 1 ELSE 0 END) AS opp_rate,
       AVG(CASE WHEN became_opportunity THEN 1 ELSE 0 END)
         / (SELECT AVG(CASE WHEN became_opportunity THEN 1 ELSE 0 END) FROM leads) AS lift
FROM lead_behaviors JOIN leads USING (lead_id)
WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 18 MONTH)
GROUP BY behavior
HAVING leads_with_behavior >= 30
ORDER BY lift DESC;
```

### 3.3 Negative signals

Competitors, students, job seekers (careers page), personal email domains (for enterprise products), unsubscribes, bounced, no fit region: subtract or disqualify.

## 4. Nurture tracks

| Track | Audience | Cadence | Content |
|-------|----------|---------|---------|
| New lead education | Leads below MQL, by persona | Weekly to biweekly for 6 to 8 weeks | Problem education, proof (case studies with approved facts), comparison guides, ROI calculators |
| Hand raiser no show or stalled | Demo booked but missed, or no reply | 3 to 5 touches over 2 weeks | Reschedule, short video, peer proof |
| Recycled | Rejected or closed lost (no budget, timing) | Monthly | New features, events, timing check in at the stated timing |
| Event and webinar | Registrants | Before and after | Reminder sequence; replay; next step |
| Customer onboarding and adoption | New customers | Milestone based | Setup, training, feature adoption (with CS) |
| Expansion | Customers with usage signals | Triggered | Upgrade paths, add ons |
| Renewal and churn risk | Contracts near renewal, usage drop | Triggered | Value recap, success plan |

Rules: one primary CTA per email; plain text style often outperforms heavy design in B2B [Practitioner consensus]; clicks and replies are engagement, opens are not (Apple MPP, security scanners in corporate mail clients click and open links automatically, so filter bot clicks by timing and user agent where the ESP allows).

## 5. Product led SaaS lifecycle

| Stage | Trigger | Message goal |
|-------|---------|-------------|
| Signup | Account created | One next step to the activation event (defined with product: for example "created first project and invited a teammate") |
| Not activated after 24 to 72 hours | Activation event missing | Remove the blocker (template, import help, video) |
| Activated | Activation event | Next value milestone |
| Trial ending | 7, 3, 1 days before | Value recap from their own usage, plan comparison, sales contact for larger accounts |
| Expired trial | Trial end without conversion | Extension offer tested, feedback |
| Paid | Conversion | Onboarding for paid features |
| Usage drop | Weekly active usage below threshold | Help, check in |

Tools: Customer.io, Braze, Iterable, Intercom, HubSpot, Userpilot or Appcues for in-product guides. Product usage events must flow from the product analytics or warehouse (Segment, RudderStack, Customer.io Data Pipelines).

## 6. Local services lifecycle

- Quote follow-up: same day, day 2, day 5, day 14 (reason codes from the CRM).
- Booking reminders: 48 and 2 hours before, with reschedule link (SMS consent).
- Post job: review request same day ([Loyalty, referral and reviews](loyalty-referral-and-reviews.md)), referral ask after positive review.
- Seasonal reminders: service intervals (HVAC, pest control, dental recall) timed from the last job date, the local equivalent of replenishment.

## 7. Closed loop with paid media and measurement

- Pass CRM stages (MQL, SQL, opportunity, closed won with value) back to ad platforms through offline conversion import or CRM integrations (owned by `measurement`; HubSpot and Salesforce native integrations exist for Google Ads, Meta and LinkedIn).
- Share lead quality by source and form with channel agents weekly (lead to SQL rate by campaign).
- Suppress customers and open opportunities from cold acquisition campaigns ([Lifecycle and paid media](lifecycle-and-paid-media.md)).
- ABM: share target account lists and engagement scores with `linkedin-ads`; nurture known contacts at those accounts with account specific content.

## 8. B2B deliverability notes

- Corporate recipients sit behind Microsoft 365 and Google Workspace filters plus secure email gateways that prefetch links; expect inflated clicks from scanners.
- Keep marketing nurture on a marketing subdomain, separate from sales one to one mail and transactional product mail.
- Cold outbound prospect lists (purchased contact data) are not lifecycle: they carry consent risk (GDPR, PECR, CASL) and deliverability risk; route any cold outreach question to `compliance` and keep it off the marketing domain.

## 9. Tools and AI (2026)

| Tool | Notes |
|------|------|
| HubSpot | Lead Scoring tool (fit, engagement, combined); Workflows; remote MCP server at mcp.hubspot.com GA 2026-04-13 with read and write on CRM objects, OAuth 2.1 with PKCE, respects user permissions; local Developer MCP server GA 2026-02-19; Breeze agents (renaming to Agent Hub and Agent Builder reported 2026-07) [Secondary, 2026; naming Unverified] |
| Salesforce (Marketing Cloud, Account Engagement) | Enterprise B2B; Agentforce features |
| Customer.io | PLG lifecycle; MCP v2 (2026-05-04) exposes Journeys UI API and Data Pipelines API with permission inheritance; admins can disable AI and MCP [Official, Customer.io 2026] |
| Braze, Iterable | B2C first but used for PLG at scale |
| Marketo (Adobe) | Enterprise B2B scoring and nurture |

## 10. B2B lifecycle audit questions

- Are MQL, SAL and SQL defined in writing with sales, with SLAs and rejection reasons?
- Is median time to first contact measured, and is it minutes rather than hours for hand raisers?
- Is the scoring model built from closed won data, with fit and engagement separated and engagement decaying?
- Is any workflow still using the retired HubSpot legacy score?
- Do CRM stages flow back to ad platforms (offline conversions) and is lead quality by source reported?
- Are customers and open opportunities suppressed from acquisition campaigns?
