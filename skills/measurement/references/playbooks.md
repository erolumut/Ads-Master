# Measurement Playbooks

Step by step plays for the situations this agent meets most. Each play lists trigger, steps, outputs and done criteria. All live changes require human approval (see SKILL.md guardrails).

## P1. Foundation build (new project or no trusted tracking)

Trigger: cold start, new site, audit grade D or F.

1. Intake (SKILL.md) and codebase scan: framework, existing tags, CMP, order and lead handlers, CRM.
2. Write the measurement plan ([Strategy](measurement-strategy-and-kpi-tree.md) section 9): KPI tree, conversion definitions with dedup keys and values, consent design by region, platform matrix.
3. Consent: CMP choice, defaults by region, GTM template, test matrix ([Consent](consent-and-privacy.md) section 10).
4. Data layer contract ([Implementation recipes](implementation-recipes.md) recipe 0) and developer tickets.
5. GA4 property settings ([GA4](ga4-setup-and-audit.md) section 2), BigQuery export at Growth tier and above.
6. GTM container: Google tag, GA4 events, Google Ads conversion with enhanced conversions, Meta pixel with event_id, other active platforms.
7. Server events for purchases or leads on the top paid platform (native app, sGTM or sender module).
8. Click ID capture and CRM fields (lead gen).
9. QA: test orders or leads in each region and consent state; platform test tools; dedup checks.
10. Go live with approval; annotate; 7-day reconciliation.
11. Update MEASUREMENT.md draft; journal entry; hand off to channel agents with the new conversion actions and the date they became reliable.

Done when: audit grade C or better with no Critical fails in sections B, D, E; capture rate known by region; MEASUREMENT.md approved.

## P2. Site migration or replatform

Trigger: new theme, framework migration (for example to Next.js), domain change, checkout change.

1. Inventory current tracking (tags, events, parameters, conversion actions, audiences built on events, UTMs, redirects).
2. Map old to new events; keep names and IDs identical where possible.
3. Staging implementation with a separate GTM environment or property; QA script.
4. Redirect map preserves query strings; test paid final URLs.
5. Launch day: monitor real-time GA4, platform test events, sGTM logs every hour for the first 6 hours; compare orders to backend.
6. Day 1, 3, 7 reconciliation; fix gaps fast.
7. Tell channel agents the cutover time; advise Google Ads data exclusions for any broken window.

## P3. Shopify checkout extensibility and pixel migration

Trigger: Additional scripts or checkout.liquid tracking still present, Thank you page upgrade, duplicate or missing purchases after upgrade. Deadlines: Plus 2025-08-28, non-Plus 2026-08-26 (both passed) [Official, shopify.dev]. A conversion drop starting late August 2026 on a non-Plus store points here first.

1. List what Additional scripts and theme code did (GA4, Ads, Meta, TikTok, affiliates, surveys).
2. Replace with app pixels first (Google and YouTube, Facebook and Instagram with Maximum data sharing, TikTok), then custom pixels for the rest ([Implementation recipes](implementation-recipes.md) recipe 5).
3. Set each custom pixel's Customer privacy permission.
4. Remove old scripts and duplicate GA4 or Ads tags from theme.liquid.
5. Test orders with consent accepted and declined; check event_id parity with server events.
6. Reconcile purchases for 7 days; check post-purchase upsell pages if used.

## P4. CAPI rollout (any platform)

1. Choose route: native integration, sGTM template, CAPI Gateway or sender module.
2. Event spec: names, event_id rule, user data fields, values, consent behavior.
3. Add event_id to browser events first (no server yet) and verify.
4. Add server events with test codes; verify dedup and match quality.
5. Ship to production behind a flag; 7-day comparison of browser, server, platform and backend counts.
6. Monitor EMQ and success rate weekly; record in MEASUREMENT.md.

## P5. Lead gen offline loop

1. Define stages and values with sales ([Offline and CRM](offline-and-crm-conversions.md) section 4).
2. Click ID capture script and hidden fields; CRM fields; mapping to deals.
3. Fill rate check after 2 weeks (target 90% for Google leads).
4. Connector (Data Manager, HubSpot or Salesforce integrations) or pipeline; conversion actions created as secondary first.
5. Run 2 to 4 weeks as secondary; compare stage volumes per campaign.
6. With channel agents: switch primary to the qualified stage when volume allows; translate targets.
7. Weekly parity checks; quarterly value refresh.

## P6. Consent mode v2 rollout or fix (EEA, UK, CH, TR)

1. Test current state (gcs and gcd parameters, consent tab, reject all test).
2. Pick basic or advanced with the human and counsel.
3. Configure CMP template and region defaults; add non-Google tag consent checks.
4. Update server pipeline to carry consent.
5. QA matrix; go live with approval; annotate.
6. Watch modeling eligibility (GA4 and Google Ads) and capture rate by region for 4 weeks.

## P7. Tracking outage recovery (incident)

Trigger: zero conversions, sudden drop or spike, alert fired.

1. Confirm with backend that business did not actually change (orders, leads).
2. Time box the start: GA4 hourly, platform hourly or daily, GTM version history, deploy logs, CMP changes, platform announcements.
3. Identify cause (release, tag paused, consent, token, API change, checkout change). Check the Diagnostics table in SKILL.md.
4. Fix or roll back (approval needed). Verify with test conversions.
5. Impact estimate: missing or duplicated conversions by platform and day, method stated.
6. Data hygiene: advise channel agents on Google Ads data exclusions, Meta and TikTok expectations (learning disruption), whether to upload missed conversions (offline import for Google within windows; Meta CAPI within 7 days for website events).
7. Incident report and journal entry; prevention (monitoring rule, release checklist).

## P8. GA4 vs backend gap investigation

1. Quantify the gap by day, region, device, browser, payment method, landing page (BigQuery join on transaction_id).
2. Patterns: EEA only (consent), Safari or Firefox heavy (blockers, ITP), specific payment methods (redirect or confirmation page skipped), specific days (releases), mobile app webviews.
3. Fixes: server-side purchase (MP with client_id and session_id, or sGTM), confirmation page firing logic, unwanted referrals, cross-domain.
4. Document expected capture by segment in memory once confirmed by two reconciliations.

## P9. Attribution change shock (for example Meta January and March 2026)

1. Confirm change from official source; log date.
2. Check connectors and dashboards for empty or changed columns.
3. Rebaseline: compute the ratio of old to new definition on overlapping periods where possible; otherwise compare to backend trend.
4. Communicate: journal entry tagged alert; hand off to the channel agent with the new target translation.
5. Update MEASUREMENT.md attribution settings and annotate GA4 and dashboards.

## P10. First incrementality test

1. Pick channel by spend and uncertainty ([Incrementality](incrementality-testing.md) section 1).
2. Choose design based on volume and tools (platform lift if eligible, else geo).
3. Power analysis; budget and duration; stop rule; KPI from backend.
4. EXPERIMENTS.md row; approval; launch with channel agent (geo exclusions).
5. Monitor spend by geo and contamination weekly; no peeking decisions.
6. Readout with intervals; compute incrementality factor; decision; journal; MEASUREMENT.md update; hand off to growth-orchestrator.

## P11. MMM readiness and first model

1. Readiness checklist ([MMM](mmm.md) section 1); if not ready, list what to collect and when it will be ready.
2. Data build in BigQuery: weekly spend by channel role, KPI, controls.
3. Tool choice (Meridian for geo hierarchy and Google ecosystem, Robyn for fast many-model exploration, PyMC-Marketing for custom Bayesian work) or vendor.
4. Fit, validate, calibrate with test results.
5. Present response curves and mROI with intervals; propose capped reallocation and the next test.

## P12. Profit bidding rollout

1. Margin data source and refresh process (finance).
2. Choose method (sGTM lookup, backend sender, cart data plus COGS, adjustments) per [Value and profit](value-and-profit-optimization.md).
3. Simulate 90 days; compute target translation factors.
4. Run as secondary 2 to 4 weeks; then switch per platform with targets translated (approval).
5. Monitor CM3 for 4 weeks; roll back rule.

## P13. App measurement setup

1. MMP or Firebase choice; SDK with consent handling; ATT prompt plan.
2. Event taxonomy (install, registration, trial, purchase, subscription renewal) and revenue events with currency.
3. SKAdNetwork and AdAttributionKit conversion value schema mapped to early revenue or high value actions.
4. Network integrations (Google, Meta, TikTok, Apple Search Ads, ChatGPT Ads MMP integrations if relevant).
5. Server-side store notifications for revenue truth; reconciliation monthly.
6. Web-to-app paths: deep links, click ID pass-through.

## P14. Monthly measurement review

1. Freshness Protocol; log changes.
2. Reconciliation table; ratios vs last 3 months.
3. Data quality summary (alerts, incidents, MTTR).
4. Consent rates by region.
5. Offline loop health (fill rate, latency, match rate).
6. Test results and plan; MMM status.
7. Audit score delta for sections touched.
8. Deliverable `YYYY-MM-DD_measurement_monthly-review.md`; MEASUREMENT.md draft update; Handoffs requested.
