# Conversion Tracking and Value (Google Ads side)

> Knowledge as of 2026-10. Deep implementation (GTM, server-side tagging, CRM pipelines, CMP setup, code) belongs to the measurement agent. This module covers what the google-ads agent must check, decide and request inside Google Ads. Several 2026 changes (Data Manager API migration for uploads, consent signal changes on 2026-06-15, enhanced conversions settings merge) are partly from trade press and labeled.

## 1. The conversion data contract

Smart Bidding, AI Max, PMax and Demand Gen optimize to whatever you mark as primary. A wrong primary conversion is the single most expensive mistake in Google Ads.

Rules:
1. Primary conversions = the business outcome or its closest high-volume proxy (purchase, qualified lead, booked call, trial that activates). Everything else is secondary.
2. One conversion per business event. No double counting from GA4 import plus Google tag for the same purchase.
3. Values reflect business value (revenue, or better, gross profit; lead values by stage).
4. Every conversion action has an owner, a definition and a deduplication key, recorded in `ads-master/MEASUREMENT.md`.

## 2. Goals and actions in Google Ads

| Concept | What it is | Check |
|---|---|---|
| Conversion action | One tracked event (purchase, lead, call) | Status Active or recording, correct source, last conversion recent |
| Category | Purchase, Submit lead form, Qualified lead, Converted lead, Phone call lead, Book appointment, Sign-up, Page view, Add to cart, Begin checkout, etc. | Correct category, because goals group actions by category |
| Primary vs secondary | Primary actions are used in the Conversions column and for bidding; secondary appear in All conversions only | Only business outcomes are primary |
| Account-default goals | Goals used by all campaigns unless overridden | Default goals = the main outcome |
| Campaign-specific goals | Override defaults per campaign | Use for campaigns that must optimize to a different outcome (supply vs demand side) |
| Custom goals | Bundle of actions for a campaign | Use sparingly |
| Conversion value rules | Adjust values by location, device, audience (incl. new customers, loyalty segments) | Document every rule; they change bidding |
| Counting | One (leads) vs Every (purchases) | Leads: One. Purchases: Every |
| Click-through window | 1 to 90 days | Match the sales cycle; 30 days default for most, 90 for long B2B cycles |
| Engaged-view and view-through windows | Video and display | Keep short; report separately |
| Attribution model | Data-driven (default) or last click. First click, linear, time decay and position-based were removed in 2023 [Official, 2023] | Use data-driven unless volume is too low to model |
| Include in "Conversions" | Derived from primary status | Must match intent |

## 3. Tag and data sources

| Source | Strength | Watch out |
|---|---|---|
| Google tag (gtag.js) or GTM Google Ads conversion tag | Native, supports enhanced conversions, fast | Must fire once per event with transaction ID |
| GA4 key event import | Easy, consistent with analytics | Delayed, attribution differences, do not use alongside a native tag for the same event as primary |
| Offline conversion import (OCI) with GCLID, GBRAID, WBRAID | Ties CRM outcomes to clicks | Capture click IDs on landing, store them in the CRM, upload within the window (up to 90 days after the click) |
| Enhanced conversions for leads | Matches hashed email or phone from the lead form to later CRM outcomes | Requires the same identifiers captured at form submit |
| Enhanced conversions for web | Sends hashed first-party data with the online conversion to recover unobserved conversions | Requires consent and correct data fields |
| Call conversions | Calls from ads, calls to a forwarding number on site, imported calls | Set a minimum duration that predicts a real lead |
| Store visits and store sales | Modeled or matched store outcomes | Directional, validate with geo tests |
| App conversions | Firebase, MMPs, SKAdNetwork, on-device measurement | Keep event definitions stable |

## 4. Enhanced conversions

- Enhanced conversions for web and for leads: in 2026 Google merged the settings into a single on and off control in the conversions settings [Official help article "Updates to your enhanced conversions settings", 2026; verify UI].
- Google cites an average gain of about 11% more Search conversions from enhanced conversions in 2026 materials [Official claim via trade press, 2026-09; not independently verified].
- Check: Diagnostics tab shows enhanced conversions status without errors, match rate and coverage acceptable, customer data terms accepted.

## 5. Offline conversion import (lead gen and B2B)

Recommended stage design:
| Stage | Conversion action category | Primary? | Value |
|---|---|---|---|
| Lead submitted (online) | Submit lead form | Secondary once OCI is stable (primary at launch if no OCI) | Expected value = average deal value x lead-to-sale rate |
| Qualified lead (MQL or SQL) | Qualified lead | Primary when 30+ per month | Expected value at this stage |
| Opportunity or proposal | Converted lead (or custom) | Secondary or primary for value-based bidding | Expected value |
| Closed won | Converted lead | Primary for value-based bidding at Scale tier, secondary otherwise | Actual deal value or gross profit |

Rules:
- Upload at least daily, ideally within 24 hours of the stage change. Uploads more than 7 days after the conversion are reported to be ignored by data-driven attribution [Unverified, trade press 2026-09].
- Use conversion adjustments (retractions, restatements) for refunds and disqualified leads.
- In 2026, Google moved offline conversion and enhanced conversions for leads uploads toward the Data Manager API. Trade press reports that from 2026-06-15 these uploads are handled through the Data Manager API rather than the Google Ads API conversion upload service [Contested: confirm the exact scope in the Google Ads API release notes before building or fixing an integration]. Hand off integration work to measurement.
- Google Ads API v22 was sunset on 2026-10-07 [Official, Google Ads Developer Blog]. Any upload script on v22 has stopped. Check integrations.

## 6. Google Data Manager

- Data Manager in Google Ads (Tools, Data manager) is the hub to connect first-party data sources (CRM, CDP, cloud storage, Shopify, HubSpot, Salesforce and others) for Customer Match and conversions. [Official, 2025]
- In 2026-09 Data Manager was extended to Google Analytics and Display and Video 360, and a Data Strength Uplift metric was added to Google Ads estimating conversions recovered by first-party data setup [Official via trade press, 2026-09-10].
- Customer Match gained IP addresses and interaction timestamps as signals through Data Manager, with matching restricted for EEA, UK and Switzerland users [Unverified, trade press 2026-10].

## 7. Consent mode v2 and privacy signals

- Consent mode v2 with ad_user_data and ad_personalization is required for advertisers serving EEA users to keep measurement, remarketing and Customer Match features [Official, effective 2024-03].
- Advanced consent mode (tags load and send cookieless pings when consent is denied) enables conversion modeling. Basic mode (tags blocked until consent) gives less modeling.
- June 2026: trade press reports that from 2026-06-15 ad_storage becomes the deciding signal for advertising data from linked accounts, Google signals is narrowed to GA4 reporting, and calls from visitors who deny ad_storage may not be linked to the ad click [Unverified, vendor sources 2026-06]. Ask measurement to verify and annotate.
- Never disable consent to recover conversions.

## 8. Google tag gateway for advertisers

- Serves Google tags through your own domain (first-party serving) via a CDN or load balancer integration, improving tag resilience. Launched in 2025 with one-click setups for some CDNs [Official, 2025].
- The google-ads agent checks whether it is in place and requests it from measurement when signal loss is suspected.

## 9. Conversion value rules and values

| Value approach | When |
|---|---|
| Static value per lead | Starter lead gen, before OCI |
| Dynamic transaction value (revenue) | Ecommerce baseline |
| Profit value (gross profit or contribution) | Ecommerce with variable margins (pass via server-side or adjusted values; hand off to measurement) |
| Stage-based expected value | Lead gen with OCI |
| Conversion value rules | Adjust by geo, device, audience (new customers, loyalty members) when you have evidence those segments are worth more |
| New customer value | Through the NCA goal, not a value rule |

Rule: a value rule must be based on data (for example, LTV by region from the CRM) and documented with its source. Arbitrary multipliers corrupt tROAS.

## 10. Audit checks inside Google Ads

1. Goals page: list primary actions per goal. Flag any micro conversion (page view, scroll, add to cart, begin checkout, engaged session) set as primary.
2. Duplicates: same event from GA4 import and Google tag both primary. Flag.
3. Status: any primary action "Inactive", "No recent conversions" or "Unverified". Flag critical.
4. Counting: leads counted Every. Flag.
5. Windows: click-through window shorter than the typical time to convert. Flag.
6. Values: purchase actions with default value only; lead actions without values when lead quality varies.
7. Enhanced conversions: off, or errors in diagnostics.
8. Consent mode: EEA traffic without consent mode v2 signals.
9. OCI: uploads stale (last upload older than 3 days), high error rate, wrong timezone format, still on a sunset API version.
10. Trend: daily conversions for 90 days, look for breaks and spikes (GAQL Q7 by date).
11. Reconciliation: Google Ads purchases vs backend orders by day; ratio stable within 0.8 to 1.2 of its usual level. Ask measurement for the backend number.
12. Data exclusions present for any known outage.

## 11. Tracking incident procedure

1. Detect: conversions drop more than 50% day over day with stable clicks, or spike above 2x. (Anomaly script in the GAQL module.)
2. Confirm: check Diagnostics for the conversion action, the site (thank you page, tag firing), recent releases (journal), consent banner changes.
3. Contain: do not change bids or budgets on the faulty data. If the outage lasts more than a day, draft a data exclusion for the affected dates and campaigns.
4. Hand off: write a journal entry tagged alert and request measurement to fix.
5. Recover: after the fix, verify 3 days of normal data, then remove the hold on optimization. Record the incident in `ads-master/MEASUREMENT.md` through the measurement agent.

## 12. What to hand off to measurement

| Need | Brief |
|---|---|
| Tag fix, GTM changes, server-side tagging | Conversion action names, expected trigger, evidence of the break |
| OCI or Data Manager pipeline | CRM, stages, click ID capture status, required upload frequency |
| Profit values | Margin source, product level or order level, refresh |
| Consent mode | Regions served, CMP, current consent state signals |
| Reconciliation | Date range, Google Ads numbers, backend numbers needed |
