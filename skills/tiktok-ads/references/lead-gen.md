# Lead Generation on TikTok

> Knowledge as of 2026-10. TikTok produces cheap leads. The job is to make them qualified leads. Judge every lead campaign on CRM stages, never on form fills alone. Agentic Leads (announced 2026-10-05) and Auto-selection for Lead Generation (Q3 2026) are new and rolling out; confirm availability.

## 1. Destination options

| Destination | How it works | Strength | Weakness | Use for |
|-------------|-------------|----------|----------|---------|
| Instant Form (in-app form) | Pre-filled form opens inside TikTok | Lowest CPL, no page load | Lowest intent, typo and fake data risk | High-volume B2C (insurance quotes, education, home services) with fast follow-up |
| Website form | Ad sends traffic to a landing page form tracked by pixel and Events API | Higher intent, full control of qualification | Higher CPL, page speed matters | B2B SaaS, high-ticket services |
| Direct messages (TikTok DM) | Users start a conversation with the business account | Conversational qualification | Needs staffing or automation | Local services, consultations |
| Instant messaging apps (WhatsApp, Messenger, LINE, Zalo where available) | Click to messaging app | Familiar channel in some regions | Market availability varies [Unverified] | LATAM, SEA, MENA markets |
| Agentic Leads | AI lead agent in TikTok DM and on advertiser websites that captures and qualifies leads through AI-guided conversations | Automated qualification | New; rollout and markets [Contested] | Test cell only, with human review of transcripts [Official, 2026-10] |

Smart+ Lead Generation exists in the upgraded Smart+ flow; Custom Selection controls let you add, exclude or use automated recommendations [Official, 2026]. Auto-selection for Lead Generation was previewed in Q3 2026 [Official, 2026-07].

## 2. Instant Form design for quality

| Setting | Recommendation | Why |
|---------|---------------|-----|
| Intro | State who it is for and what happens next ("A licensed advisor will call within 1 business day") | Filters low intent |
| Questions | 2 to 4 qualifying multiple-choice questions (budget, timeline, service area, role or company size) | Adds friction that removes tire kickers; multiple choice avoids junk text |
| Pre-filled fields | Name, phone, email are pre-filled where available; require phone for call-based sales | Contactability |
| Confirmation or review step | Enable a review or confirmation screen if the form builder offers it [Unverified per account] | Cuts accidental submissions |
| Privacy policy | Required link | Policy compliance |
| Thank-you screen | Set expectations and offer a next step (book a time, visit website) | Improves contact rate |
| Disqualifying answers | Use conditional logic or tag leads by answers in CRM | Route and suppress |

Run a volume form and a qualifying form as two ads in the same ad group for 14 days. Judge by cost per qualified lead (CPQL), not CPL.

## 3. Getting leads out of TikTok fast

| Method | Setup | Latency | Notes |
|--------|-------|---------|-------|
| Leads Center download | Manual CSV from Ads Manager | Hours to days | Starter only; leads go cold |
| Native CRM integrations | HubSpot, Salesforce and others via Ads Manager integrations [Unverified current list] | Minutes | Preferred |
| Connectors (Zapier, LeadsBridge, Make) | Webhook to CRM or sheet | Minutes | Monitor failures daily |
| Marketing API lead retrieval | Developer pulls leads via API | Minutes | Enterprise; see tools-api-mcp.md |

Speed-to-lead rule: call or message within 5 minutes during business hours. Leads contacted after 24 hours lose most of their value [Practitioner consensus]. Daypart lead campaigns to staffed hours if follow-up is phone-based.

## 4. Closing the loop: optimize for qualified leads

1. Capture the TikTok lead ID (Instant Form) or the click ID / ttclid and hashed email and phone (website forms) into the CRM.
2. Define stages in `ads-master/MEASUREMENT.md`: Lead -> Contacted -> Qualified (MQL/SQL) -> Opportunity -> Won, with values.
3. Send CRM stage events back to TikTok via Events API (CRM or offline event set) with the lead ID or hashed identifiers and event time. Name and mapping per TikTok's CRM event documentation [Unverified current event names].
4. Once a deeper stage reaches about 50 events per week (account or campaign), test optimizing to it in a new ad group or Smart+ campaign.
5. Report CPL, contact rate, qualification rate, CPQL, cost per opportunity and cost per won deal weekly.

Hand the CRM pipeline and Events API mapping to the measurement agent; this agent defines which stage to optimize toward.

## 5. Lead quality diagnostics

| Symptom | Likely cause | Checks | Fix |
|---------|-------------|--------|-----|
| Many fake or junk leads | Instant Form too easy, incentive too generic, TikTok Ad Network placement | Placement breakdown, field patterns, duplicate rate | Add qualifying questions, remove off-platform placements, change offer to non-generic |
| Low contact rate | Wrong numbers, slow follow-up | Time to first contact, number validation | Require phone, SMS verification step via CRM, speed-to-lead |
| Leads too young or out of area | Age and geo not enforced | Audience controls, location settings | Enforce age floor and geo in Smart+ audience controls |
| CPL fine, SQL rate collapsing | Creative attracting curiosity, not intent | Creative-level CRM join | Callout hooks, price anchoring in creative, qualifying copy |
| Duplicate leads | Same users submitting repeatedly | Duplicate rate by phone and email | Exclude lead audiences of last 30 days, CRM dedup |

## 6. Creative for lead gen
- Lead with the qualifier: "Homeowners in [City] with south-facing roofs..."
- Show the person who will call or the service in action; humans beat graphics.
- State price ranges or minimums where possible ("Plans from $X"); it removes unqualified leads.
- For B2B, call out the role and the job ("If you run payroll for 50+ employees..."). TikTok has no firmographic targeting; creative is the filter.
- Use Spark Ads from a founder or expert account for trust.

## 7. Structure by tier

| Tier | Structure | Bid | Optimization |
|------|-----------|-----|-------------|
| Starter | 1 campaign, 1 ad group, broad + geo + age floor, Instant Form with 2 questions | Maximum Delivery | Leads |
| Growth | Smart+ Lead Generation or 1 manual campaign with 2 to 3 ad groups (form types or offers), CRM integration live | Maximum Delivery, then Cost Cap at 1.1x trailing CPL | Leads, testing deeper CRM event |
| Scale | Smart+ Lead Generation scaling + manual testing; CRM events optimization; per-region campaigns if sales capacity differs | Cost Cap on CPQL-calibrated targets | Qualified lead event |
| Enterprise | Per market and product line, offline conversions, lift tests on qualified pipeline | Cost Cap or value-based where lead values exist | Value or qualified stage |

Scaling note: TikTok's Smart+ Lead Generation guidance is to raise budgets by no more than 50% per day [Official].

## 8. Compliance for lead gen
- Financial services, insurance, credit, education, employment and housing have restricted or special rules in many markets. Verify the ad policy for the vertical and market before launch (see policy-and-account-health.md).
- Consent text on forms must match data use (marketing calls, SMS). In the US, TCPA consent language for calls and texts is a legal matter; route to the human.
- Do not ask for sensitive data (health conditions, financial account numbers) in Instant Forms.

## 9. Lead gen weekly report template

```
| Campaign | Spend | Leads | CPL | Contacted % | Qualified % | CPQL | Opps | Cost/Opp | Won | Cost/Won | Notes |
Lead source split: Instant Form vs website vs DM vs Agentic Leads
Creative ranking by CPQL (not CPL)
Follow-up SLA: median minutes to first contact
Decisions proposed for approval
```

## 10. Lead values for value-based optimization and reporting

```
Lead value = P(qualified | lead) x P(won | qualified) x average contribution per won deal
```

Worked example (home services): 40% of leads qualify, 25% of qualified leads close, average job contribution $1,200. Lead value = 0.40 x 0.25 x 1,200 = $120. Target CPL at a 3:1 return on lead value = $40. Recompute monthly from CRM, by campaign where volume allows, and send stage values with CRM events so the platform can learn which leads are worth more.

## 11. CRM stage to TikTok event mapping (draft for the measurement agent)

| CRM stage | When it fires | Event sent via Events API | Value | Use |
|-----------|--------------|---------------------------|-------|-----|
| Lead created | Form submitted | Lead / SubmitForm (from TikTok form or website) | Lead value or none | Volume baseline |
| Contacted | First two-way contact | Custom CRM event "Contacted" [Unverified naming in TikTok CRM event set] | none | Contact rate |
| Qualified (MQL or SQL) | Sales accepts | CRM event "Qualified lead" | Stage value | Optimization target once 50+ per week |
| Opportunity | Proposal sent | CRM event "Opportunity" | Stage value | Reporting |
| Won | Closed won | CRM event "Won" or Purchase | Deal value | Reporting, value signal |

Pass the TikTok lead ID (Instant Form) or hashed email and phone plus event time. Send events within 24 to 48 hours of the stage change; late events lose optimization value.

## 12. Instant Form copy templates

Home services:
```
Intro headline: Free roof inspection for [City] homeowners
Intro text: Takes 30 seconds. A local specialist calls you within 1 business day.
Q1 Are you the homeowner? (Yes / No)
Q2 When do you want the work done? (Within 30 days / 1 to 3 months / Just researching)
Q3 Roof age? (Under 10 years / 10 to 20 years / Over 20 years / Not sure)
Thank-you: We will call from [number]. Want to pick a time now? [Book a time]
```

Education:
```
Intro headline: Get the [Program] syllabus and fees
Q1 Highest completed education (options)
Q2 When would you start? (Next intake / Within 6 months / Later)
Q3 Preferred study mode (Online / On campus)
```

B2B SaaS (website form preferred; Instant Form variant):
```
Q1 Team size (1 to 10 / 11 to 50 / 51 to 200 / 200+)
Q2 Your role (Owner / Manager / Individual contributor / Other)
Q3 Current tool (options incl. "None")
```

Disqualifying answers ("Just researching", "No" to homeowner) should route to nurture, not sales, and should not be sent back as qualified events.

## 13. Agentic Leads and Auto-selection test plan
1. Confirm availability with the rep or in Ads Manager; record eligibility in memory.
2. Run as a separate ad group or campaign at 10% to 20% of lead budget, same creative, same geo.
3. Review 50 conversation transcripts per week for accuracy, policy compliance and tone; stop if the agent makes claims outside BRAND.md.
4. Compare CPQL and cost per opportunity over 28 days against the control.
5. Log the test in EXPERIMENTS.md with a stop rule (CPQL above 1.3x control after 21 days).
