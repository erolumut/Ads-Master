# Audiences and First-Party Data

> Knowledge as of 2026-10. Similar audiences were retired in 2023. In 2026 Demand Gen lookalikes became signals and Customer Match gained new identifiers through Data Manager. Verify eligibility rules in Google Ads Help (Customer Match policy) before uploading data.

## 1. Audience types and how they behave by campaign

| Audience type | Search | PMax | Demand Gen | Video | Notes |
|---|---|---|---|---|---|
| Your data segments (website visitors, app users, YouTube users) | Observation or targeting | Signal | Targeting | Targeting | Remarketing |
| Customer Match (emails, phones, addresses, and since 2026-09 IP addresses with interaction timestamps, not for EEA, UK or Swiss users [Official, 2026-09]) | Observation, targeting, exclusion | Signal, NCA customer definition | Targeting, lookalike seed or signal | Targeting | Highest value first-party asset |
| Custom segments (search terms, URLs, apps) | Observation | Signal | Targeting | Targeting | Build from converting queries and competitor URLs |
| Affinity, in-market, life events, detailed demographics | Observation | Signal | Targeting | Targeting | Weak signals alone |
| Lookalike segments | n/a | n/a | Signal (from 2026-03-15) [Practitioner report, 2026] | n/a | Narrow 2.5%, balanced 5%, broad 10% sizes |
| Optimized targeting | n/a | Built in | On by default in some formats | n/a | Expands beyond selected audiences |
| Audience signals | n/a | Starting point only | n/a | n/a | Not hard targeting |

Observation vs targeting in Search:
- Observation: ads show to everyone matching keywords; audience used for reporting and Smart Bidding signals. Default for most Search campaigns.
- Targeting: ads show only to the audience (RLSA style). Use for high-cost broad themes where only past visitors convert, or separate remarketing campaigns with looser keyword sets.
- Smart Bidding already uses audience signals in every auction. Manual audience bid adjustments are ignored by Smart Bidding (they still matter for Manual CPC).

## 2. Customer Match

Requirements and rules [Official, verify current policy]:
- Account in good standing, compliant with Google Ads policies and the Customer Match policy; accept the customer data terms.
- Full use (targeting, observation, manual bid adjustments, exclusions) requires 90 days of Google Ads history and more than 50,000 USD lifetime spend; other compliant advertisers can use Customer Match for observation and exclusions [Official, Customer Match policy].
- Upload only data collected with consent for this use; follow regional rules (EEA, UK, Switzerland have stricter rules and consent mode requirements).
- Minimum list size to serve: 100 active matched users in the last 30 days on Search, YouTube and Display (Google lowered the Search and YouTube floor from 1,000) [Practitioner report, Search Engine Roundtable citing Google Ads Help 7476585, 2025-12]. Active matched users are far fewer than uploaded rows; match rates of 30% to 70% are typical [Practitioner consensus].
- IP matching (2026-09): upload unhashed IP addresses with first and last interaction timestamps (a timestamp alone is an error; IP-only lists are allowed). Without timestamps Google matches the IP's latest known user, which is weaker on shared IPs. Exclude EEA, UK and Swiss users' IPs [Official, Data Manager Help "Prepare your data for import"; Google Ads Developer Blog 2026-05].
- Membership duration: set to match the use; refresh at least monthly, ideally automatically through Data Manager connectors.
- Uploading methods: Data Manager (connectors for CRM, cloud storage, Shopify, HubSpot, Salesforce and others), Google Ads UI file upload, Data Manager API (programmatic).

Lists every account should maintain:
| List | Use |
|---|---|
| All customers (last 540 days) | Exclusion for acquisition campaigns; NCA definition |
| High value customers (top 20% by LTV or margin) | PMax and Demand Gen signal; lookalike seed; value rules |
| Recent purchasers (last 30 days) | Exclusion from acquisition; cross-sell |
| Lapsed customers (no purchase in 180 days) | Retention campaigns |
| Leads not yet converted | Nurture with Demand Gen or YouTube |
| Disqualified leads or bad fit | Exclusion and negative signal |
| Target account contacts (B2B) | ABM style targeting and signals |
| Employees and partners | Exclusion |

Customer list labeling: from 2026-08-18 Google assigns a customer type automatically to eligible conversion-based customer lists you have not classified [Practitioner report, Search Engine Land 2026-06; not described on the Google help page found this edition]. Labels feed NCA, retention goals and loyalty pricing (a list labeled "Loyalty program members" gets member prices and shipping in Shopping ads). Classify every list yourself in Tools, Shared library, Audience manager, Your data segments.

## 3. PMax audience signals: what works

Ranked from strongest to weakest [Practitioner consensus]:
1. Customer Match high value customers and all purchasers.
2. Website converters (purchasers, qualified leads) from your data segments.
3. Custom segments from converting search terms (people who searched for X).
4. Custom segments from competitor URLs and apps.
5. In-market and life events relevant to the product.
6. Affinity.

Pattern: one signal per asset group combining 1 to 3 plus a custom segment matching the asset group theme. Signals matter most in the first weeks.

## 4. Demand Gen audiences

- Lookalikes: seed lists of at least about 100 matched users historically; narrow (2.5%), balanced (5%) and broad (10%) sizes. From 2026-03-15 lookalikes act as AI-powered audience signals instead of strict targeting [Practitioner report, 2026]. Expect broader delivery.
- Structure: separate ad groups for new customer audiences (lookalikes, custom segments) and remarketing; exclude converters from new customer groups.
- Optimized targeting: test on vs off when tracking is clean.
- B2B: Customer Match of target accounts and pipeline contacts, custom segments of competitor URLs and category search terms.

## 5. Remarketing in 2026

- Remarketing lists come from the Google tag, GA4 audiences (with Google signals and consent), YouTube engagement and app events.
- In the EEA, remarketing depends on consent mode signals (ad_personalization). Lists may be smaller than in other regions.
- Recency windows: 1 to 7 days for cart abandoners, 8 to 30 days for product viewers, 30 to 180 days for past customers for cross-sell.
- Frequency: cap in Display and Video. Exclude purchasers from acquisition and abandonment campaigns for at least the typical repurchase cycle.
- PMax already remarkets. Separate remarketing campaigns next to PMax often overlap. Prefer NCA goals and exclusions over parallel remarketing campaigns.

## 6. Exclusions every account needs

| Exclusion | Where | Why |
|---|---|---|
| Existing customers | Acquisition campaigns, NCA-only campaigns | Pay for new customers only |
| Recent converters | Lead gen campaigns | Avoid duplicate leads |
| Employees | All | Avoid internal clicks |
| Job seekers | Search negatives plus custom segment exclusions in Demand Gen | Common waste in B2B and services |
| Disqualified leads | Lead gen | Avoid paying twice for bad fit |

## 7. First-party data maturity ladder

| Level | What exists | Next step |
|---|---|---|
| 0 | Google tag only | Enhanced conversions for web, consent mode v2 |
| 1 | Enhanced conversions, GA4 audiences | Customer Match of all customers, refresh monthly |
| 2 | Customer Match automated via Data Manager | OCI with qualified stages, NCA goals |
| 3 | OCI daily, values by stage or profit | Value rules from LTV data, high value customer lists, journey aware bidding when available |
| 4 | Full CRM loop, profit values, incrementality tests | MMM calibration with Meridian, Data Strength Uplift tracking |

## 8. Audience diagnostics

| Symptom | Causes | Fix |
|---|---|---|
| Customer Match list too small to serve | Low match rate (only emails, old data), list under threshold | Add phone and address fields, normalize formats, combine lists |
| NCA campaigns still reporting many returning customers | Customer list stale or incomplete | Automate refresh, widen lookback |
| Demand Gen lookalike delivery broad after 2026-03 | Lookalikes now signals | Use exclusions, creative that self-selects, monitor CPA |
| Remarketing lists shrinking in EEA | Consent rates, ad_personalization denied | Measurement to review CMP and consent mode; plan for smaller pools |
| PMax ignores the signal | Signals are hints | Judge by results, not by audience reports; use asset group themes |

## 9. Customer Match upload checklist

| Step | Rule |
|---|---|
| Fields | Email, phone (E.164 format with country code), first name, last name, country, postal code; more fields raise match rates |
| Normalization | Lowercase and trim emails, remove spaces and symbols from phones, before hashing |
| Hashing | SHA-256 for uploads that require hashing; Data Manager connectors handle this automatically |
| Consent | Only customers who agreed to this use; respect deletion and opt-out requests on each refresh |
| Segmentation | Separate lists by purpose (exclusion, signal, retention) instead of one large list |
| Refresh | Automated daily or weekly through Data Manager; at minimum monthly |
| Naming | `CM_{purpose}_{source}_{lookback}`, for example CM_AllCustomers_Shopify_540d |
| Verification | Check match rate and size for Search and Display after upload (GAQL Q26) |

## 10. Audience strategy by business model

| Model | Signals and lists that matter | Exclusions |
|---|---|---|
| Ecommerce | Purchasers, high value customers, cart abandoners, product viewers | Recent purchasers from acquisition campaigns, employees |
| Lead gen | Qualified leads and customers from CRM, converters | Existing customers, disqualified leads, recent submitters |
| B2B SaaS | Target account contacts, opportunities, trial users, customers | Customers from acquisition, job seekers, students |
| Local services | Past customers for repeat service, website visitors | Out of area users (via location settings) |
| App | Active users, payers, lapsed users | Installed users from install campaigns |
| Marketplace | Buyers vs sellers lists kept separate | Each side excluded from the other side's campaigns |
