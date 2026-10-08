# Conversion Tracking and Value (Google Ads side)

> Knowledge as of 2026-10. Deep implementation (GTM, server-side tagging, CRM pipelines, CMP setup, code) belongs to the measurement agent. This module covers what the google-ads agent must check, decide and request inside Google Ads. The 2026 changes in this module (Data Manager API for offline uploads, consent signal changes on 2026-06-15, enhanced conversions settings merge, Customer Match IP matching) were re-verified against Google help and developer pages on 2026-10-08 and are labeled with their source.

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

Call recording: for US and Canada accounts that had never chosen a call recording setting, Google switched call recording to "Yes" on 2026-07-01; recordings feed AI lead scoring of calls, with call duration as a fallback signal [Practitioner reports citing Google's notice, 2026-05 to 2026-07]. Confirm the setting is a deliberate choice in every account (account settings, Call recording) and that the business's call disclosure covers it.

## 4. Enhanced conversions

- Enhanced conversions for web and for leads: since 2026-06 one account-level setting covers both, and Google deduplicates data arriving from the tag, Data Manager and API integrations at the same time (multiple sources allowed from 2026-04). Accounts that had accepted the customer data terms were moved automatically [Official, Google Ads Help "Updates to your enhanced conversions settings", 2026].
- Google cites an average gain of 11% more Search conversions from enhanced conversions compared with standard conversion imports [Official claim, repeated in Google's 2026-09 Data Strength materials; not independently verified].
- In 2026-09 the Conversions menu was reorganized: Summary and Leads moved above Conversions, an "All conversions" view was added and Settings was renamed "Conversion settings" [Practitioner report, Search Engine Roundtable 2026-09]. Update any written UI paths.
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
- Upload at least daily, ideally within 24 hours of the stage change. Several 2026-09 trade reports say uploads arriving more than 7 days after the conversion still appear in reports but are ignored by data-driven attribution [Unverified: not found in Google documentation this edition]. Google's Data Manager guidance asks for uploads within 24 hours of the tag event for best results [Official, Data Manager API docs].
- Use conversion adjustments (retractions, restatements) for refunds and disqualified leads.
- Data Manager API is now the path for offline uploads [Official, Google Ads Developer Blog 2026-05-15 and Google Ads API docs]:
  - From 2026-06-15 the Google Ads API `ConversionUploadService.UploadClickConversions` method (offline click conversions, including enhanced conversions for leads) accepts only developer tokens that already uploaded offline click conversions before the cutoff. New integrations get `CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE`. Google calls the allowlisted access transitional and has published no end date for it.
  - New builds must use the Data Manager API (no developer token, project-based quotas, optional encryption, IP and session attributes available to all users). Existing pipelines should plan a migration rather than wait.
  - Customer Match uploads followed the same pattern earlier: from 2026-04-01 tokens with no Customer Match requests between 2025-10-01 and 2026-03-31 lost Google Ads API access to OfflineUserDataJobService and UserDataService [Official, Google Ads API deprecations page]. A March 2027 deadline for data partners is reported but not confirmed [Unverified, PPC Land 2026].
  - Silent failure risk: a pipeline that does not handle the allowlist error stops sending conversions without an alert. Check the upload history (Goals, Uploads) and diagnostics weekly.
  - Hand off integration work to measurement.
- Google Ads API v22 was sunset on 2026-10-07 [Official, Google Ads Developer Blog]. Any upload script on v22 has stopped. Check integrations.

## 6. Google Data Manager

- Data Manager in Google Ads (Tools, Data manager) is the hub to connect first-party data sources (CRM, CDP, cloud storage, Shopify, HubSpot, Salesforce and others) for Customer Match and conversions. [Official, 2025]
- In 2026-09 Data Manager was extended to Google Analytics and Display and Video 360, and a Data Strength Uplift metric was added to Google Ads estimating conversions recovered by first-party data setup [Official via trade press, 2026-09-10].
- Customer Match accepts IP addresses (unhashed IPv4 or IPv6) with optional first and last interaction timestamps, through file upload, Data Manager and the Data Manager API (v1.7, 2026-05). IP matching is not supported for users in the EEA, UK or Switzerland, so exclude those users' IPs. Google expects match rate gains from these signals from 2026-10 [Official, Data Manager Help and Google Ads Developer Blog, 2026-05 to 2026-09].
- Multi-source conversions: uploaded conversion events can fill gaps in tag-based conversions for the same action (same transaction ID). Allowlist only; uploaded conversions that create new conversions are reported but not used for bidding during a 14-day trial period of the action [Official, Data Manager API docs, 2026; beta reported 2026-09-21].

## 7. Consent mode v2 and privacy signals

- Consent mode v2 with ad_user_data and ad_personalization is required for advertisers serving EEA users to keep measurement, remarketing and Customer Match features [Official, effective 2024-03].
- Advanced consent mode (tags load and send cookieless pings when consent is denied) enables conversion modeling. Basic mode (tags blocked until consent) gives less modeling.
- Since 2026-06-15, consent mode (ad_storage) is the single control for advertising data collected by the Google tag, including data a linked Google Analytics property shares with Google Ads. Google signals now only controls whether Analytics data is joined with signed-in user data for Analytics reporting. ad_personalization will alone decide personalization use on a date Google has not announced [Official, Analytics Help "Updates to Google Analytics data controls", 2026-04].
- Practical effects to check with measurement: GA4-based remarketing lists only include users who granted ad_storage, and calls from visitors who denied ad_storage may not be linked to the ad click [Practitioner and vendor reports, 2026-06]. Compare list sizes and call conversions before and after 2026-06-15 and annotate the journal.
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
