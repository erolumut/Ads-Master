# Audiences and Signals

> Knowledge as of 2026-10. In 2026 Meta targeting is mostly done by three things: hard controls, creative, and conversion signal. Audience inputs are hints. This module covers what still matters and how to feed the system better data.

## 1. The 2026 targeting model

| Layer | What you control | Strength |
|-------|------------------|----------|
| Hard controls | Location, minimum age, language, excluded custom audiences, account-level controls, special ad category limits | Absolute |
| Creative | Who the ad is retrieved for (Andromeda), based on visual, copy, persona, format | Very high |
| Conversion signal | Which people the ranking models learn to find (events, values, CRM stages) | Very high |
| Audience suggestions | Custom audiences, lookalikes, interests, age and gender ranges inside Advantage+ audience | Low after the learning period |
| Value rules | Price adjustments by segment | Medium, for known value differences |

Implication: audience research shifts from "which interests" to "which personas and motivators should our creative speak to" (hand off to `creative-strategy`) and "which signal should we optimize for" (this module and measurement).

## 2. Advantage+ audience versus original audience options

| Option | When | Notes |
|--------|------|-------|
| Advantage+ audience with no suggestions | Accounts with conversion history; default | Fastest learning; controls still apply |
| Advantage+ audience with suggestions | New accounts or new products, niche B2B, local | Suggestions prioritized first, then expansion |
| Original audience options with broad (only location, age, gender) | Testing, legal constraints | Same reach as Advantage+ in most cases, less automation |
| Original audience options with detailed targeting and Advantage detailed targeting | Rarely; very niche offers where expansion wastes spend in tests | Advantage detailed targeting expands anyway when it predicts better results for conversion goals |
| Original audience options with custom audience, no expansion | Retention offers, existing customer upsell, event attendees | The only true "retargeting only" setup |

Detailed targeting changes to know: sensitive detailed targeting options were removed in 2022; detailed targeting exclusions were removed for new ad sets from 2024-07-29 and stopped delivering in existing ad sets from early 2025 (2025-01-31 per Meta's notice) [Official, 2024-07]; Meta continues to merge low-use interest options. Do not build strategies on specific interest IDs; they may disappear.

## 3. Custom audiences

| Source | Max retention | Use |
|--------|--------------|-----|
| Website (dataset events, URL rules) | 180 days | Exclusions (purchasers), retention, audience segments |
| App activity | 180 days | App re-engagement, exclusions |
| Customer list | Static, refresh via API or integration | Existing customer segment, exclusions, value-based lookalikes |
| Engagement: video, Instagram account, Facebook Page, lead form, Instant Experience, events, shopping, Marketplace | Up to 365 days for most, 730 days for some [verify per source] | Engaged audience segment, warm suggestions |
| Offline / CRM events (via Conversions API) | 180 days | Store buyers, closed deals, high LTV segments |

Customer list hygiene:
- Normalize then hash with SHA-256: email lowercased and trimmed, phone in E.164 digits without plus, first and last name lowercased, country as two-letter ISO code, zip without spaces. Meta hashes in the UI; via API you must hash.
- Include as many identifiers as possible (email, phone, name, city, zip, country, external ID). Match rate typically rises with more keys.
- Refresh existing customer lists at least weekly for audience segments and exclusions.
- Check legal basis (GDPR, KVKK, CCPA). Only upload customers who gave valid consent for this use. Coordinate with `measurement` on consent.

## 4. Lookalikes

Lookalike audiences (1% to 10% of a country) still exist. In Advantage+ audience they are suggestions. Their main remaining uses:
- Seed suggestions for new accounts without conversion history.
- Value-based lookalikes from customer lists with LTV values for markets where Advantage+ is not yet learning well.
- Original audience setups when a test requires a defined audience.
Do not run a ladder of lookalike ad sets (1%, 2 to 3%, 3 to 5%) in 2026; it fragments signal.

## 5. Audience segments (account settings)

Define once per ad account:
- Engaged audience: website visitors (30 to 180 days), social engagers (Instagram and Facebook, 90 to 365 days), lead form openers, video viewers (ThruPlay or 75%).
- Existing customers: customer list (all purchasers or closed won), purchase events 180 days, app purchasers, offline buyers.

Then use: segment breakdown in reporting, new customer controls in Sales campaigns (see bidding module), and incremental planning (high existing customer share usually means lower incrementality).

## 6. Exclusions

| Exclusion | When | How |
|-----------|------|-----|
| Recent purchasers | Single purchase products, high-ticket, lead gen (current leads) | Custom audience exclusion (hard control) |
| Current customers | Pure acquisition budgets | Customer list exclusion, refreshed weekly |
| Employees | Always | Account-level employee exclusions or list |
| Existing leads in CRM | Lead gen | Customer list of open leads, refresh daily or weekly |
| Converters in the last 7 to 30 days from retargeting | Retention campaigns | Event-based custom audience |
Do not exclude engaged audiences from acquisition campaigns: warm people are part of the acquisition path. Track their share with audience segments instead.

## 7. Retargeting in 2026

Advantage+ campaigns already reach engaged people. Separate retargeting campaigns are justified when:
- Consideration cycle is long (high ticket, B2B, education) and you need different creative (proof, objections, offers) for engaged people.
- Catalog-based retargeting (viewed or added to cart) with product-level ads.
- Messaging re-engagement (people who messaged in the last 30 to 90 days) with sponsored messages or click to message.
- Retention offers (replenishment, cross-sell) to customers.
Keep retargeting at 5 to 15% of spend unless data proves incrementality; retargeting is the most over-credited spend in platform reporting. Validate with a holdout (see measurement module).

## 8. Signal engineering (the highest leverage audience work)

| Signal | Implementation | Why it matters |
|--------|---------------|----------------|
| Purchase value with gross profit option | Send revenue as value; consider a profit-based custom value event for value optimization after `measurement` approval | Optimization chases what you send |
| Lead quality stages | Conversions API for CRM (lead_id or external IDs, stages such as Qualified, SQL, Won) | Enables conversion leads optimization and quality value rules |
| Predicted LTV | Send an early value proxy (subscription plan, basket composition, predicted LTV score) as value | Shortens feedback loop for subscriptions and apps |
| Offline / store sales | Conversions API with action_source physical_store | Website and in-store optimization, omnichannel measurement |
| Messaging outcomes | Conversions API for business messaging (lead submitted, purchase in chat) | Lets click to message optimize beyond conversations |
| Customer lists | Weekly CRM sync | Audience segments, exclusions, new customer controls |
| Event quality | EMQ, deduplication, coverage | Better matching equals better delivery |

Event selection ladder (choose the deepest with enough volume, at least about 50 per week per ad set):
```
Ecommerce:  Purchase (value) > Initiate checkout > Add to cart > Landing page view
Lead gen:   Closed won > SQL > Qualified lead (CRM) > Lead (form submit) > Landing page view
SaaS:       Paid conversion > Trial activated (product event) > Start trial > Lead
App:        Purchase or subscribe (value) > Key activation event > Install
Local:      Booked appointment > Qualified call (60s+) > Call or conversation > Lead
```
Never optimize for an event that is cheap to fake or trivially triggered (page views, "Contact" button clicks) unless it is a temporary bridge with a dated exit plan.

## 9. Privacy environment that changes signal

| Change | Date | Effect | Label |
|--------|------|--------|-------|
| Apple ATT | 2021 | iOS app signal loss; AEM and SKAdNetwork | [Official, 2021] |
| Health and wellness data restrictions | 2025-01 onward | Lower funnel events and URL details blocked for classified health advertisers | [Official, 2025] see policy module |
| EU political, electoral and social issue ads stopped | 2025-10 | Meta stopped these ads in the EU under the TTPA regulation | [Official, 2025-07 announcement] |
| Meta AI chat interactions used for ad personalization | 2025-12-16 | Conversations with Meta AI inform ad and content personalization, excluding sensitive topics; not applied in EU, UK, South Korea initially; no user opt-out reported | [Official, 2025-10 announcement] |
| EU less personalized ads choice | 2026-01 | EU users can choose a less personalized ads experience; smaller addressable signal pool in EU; Meta describes the option as less relevant and effective in SEC filings | [Official, 2025-12 EC statement; 2026 10-Q] |
| Attribution window changes | 2026-01 and 2026-03 | Reporting differences; see measurement module | [Official, 2026] |
| Apple iOS privacy updates (link tracking protection, fingerprinting protection) | 2023 onward, iOS 26 expansion reported | Click IDs (fbclid) stripped in more contexts; reliance on Conversions API and first-party IDs grows | [Unverified, scope varies] |

What to do about signal loss:
1. Conversions API with high EMQ (email, phone, external_id, fbp, fbc, IP, user agent).
2. Persist fbclid as fbc in a first-party cookie or server session where consent allows; capture email early (quiz, account, newsletter) to raise match.
3. Send CRM and offline outcomes.
4. In the EU, expect higher CPMs or lower match in less personalized ads users; judge EU campaigns on blended outcomes.

## 10. B2B and niche audiences

Meta has no firmographic targeting comparable to LinkedIn. What works:
- Creative that self-selects the buyer (job title, problem language, industry visuals) so retrieval finds them.
- Customer list suggestions and lookalikes of closed won accounts.
- Optimizing to CRM-qualified events, not raw leads.
- Higher intent instant forms with qualifying questions, or website forms with enrichment.
- Hand off account-based programs to `linkedin-ads`; use Meta for retargeting and reach into the same buying committees.

## 11. Local and geo

- Use radius or postal code targeting with "People living in or recently in this location" by default.
- Minimum radius for special ad categories is 15 miles (about 24 km) [Official, long-standing].
- Too small a radius (under about 5 km in low density areas) starves delivery; widen and let creative mention the area.
- Multi-location businesses: one campaign with location-specific ads (dynamic location ads where available) beats one campaign per location at small budgets.
