# Playbooks

> Step by step plays for launch, import and diverge, optimize, scale, recover, peak season and B2B. Each play lists entry criteria, steps, approvals and exit criteria. All live changes require human approval.

## Play 1. New account launch from Google (days 0 to 30)

Entry: Google Ads live with at least 30 days of data; no Microsoft account or a dormant one.

| Day | Step | Owner | Approval |
|-----|------|-------|----------|
| 0 | Confirm intake facts; create account with correct time zone and currency; MFA for all users | microsoft-ads, human | Human creates billing |
| 0 | UET tag, goals, consent mode spec; hand off install to measurement | measurement | Human for site change |
| 1 | Import Center from Google: Search and Shopping or PMax only, campaigns paused | microsoft-ads | Human approves import |
| 1 | Post-import fix list (15 items) | microsoft-ads | Included in import approval |
| 2 | Merchant Center store and feed (ecommerce) | commerce-feeds | Human |
| 3 | Verify test click: MSCLKID, UET event, goal records | microsoft-ads, measurement | None |
| 3 | Enable campaigns at 10% to 20% of Google budget (or forecast) | human | Required |
| 7 | First search term and publisher pass; negatives | microsoft-ads | Human approves list |
| 14 | Reset manual bids from Microsoft CPC data; device adjustments if clear | microsoft-ads | Required |
| 21 | Second search term pass; asset performance; add multimedia ads | microsoft-ads | Required |
| 30 | Review: CPA vs target, conversions per campaign; move eligible campaigns to conversion bidding; decide scheduled import scope | microsoft-ads | Required |

Exit: 30 day report with CPA vs Google on matched keywords, list of divergence decisions, schedule for import.

## Play 2. Import and diverge (running accounts)

Entry: scheduled import exists and Microsoft has 60+ days of data.
1. Run the parity report (see [Optimization](optimization-and-diagnostics.md) section 3).
2. List keywords and campaigns where CPA ratio is outside 0.8 to 1.2 for 2 months.
3. Decide divergence per the tree in [Setup and import](account-setup-and-google-import.md) section 8.
4. Change import options so diverged fields are never overwritten.
5. Apply Microsoft only levers: LinkedIn layers (B2B), age and gender adjustments, partner exclusions, device adjustments.
6. Journal entry for google-ads with the new import scope.
Exit: import options documented; divergence list in memory once results confirm.

## Play 3. Weekly optimize (steady state)
Follow the weekly routine in [Optimization](optimization-and-diagnostics.md) section 1. Deliverable: `YYYY-MM-DD_microsoft-ads_weekly-optimization.md` with the change list. Escalate to a diagnostic tree when any campaign is 25%+ off target for 7 days.

## Play 4. Scale (profitable and budget limited)

Entry: CPA or ROAS at or better than target for 4+ weeks and IS lost to budget over 15% on core campaigns.
1. Raise budget 15% to 20% per week on campaigns with marginal CPA under target.
2. Add AI Max as an experiment on the top campaign.
3. Add broad match versions of top exact keywords under conversion bidding (or rely on AI Max, not both at once).
4. Launch or expand PMax with NCA (ecommerce) after an uplift test plan.
5. Add Audience campaigns: remarketing first, then in-market or LinkedIn company lists.
6. Move low volume campaigns into a portfolio; consider cross-account portfolios for multi account setups.
7. Re-check partners and audience share after each scale step.
Stop rule: if marginal CPA exceeds target by 20% for 2 weeks after a step, revert the last step.

## Play 5. Recover (performance collapse)

Entry: CPA 30%+ over target for 7 days or conversions down 50%.
1. Freeze changes. No new optimizations until diagnosis is complete.
2. Run diagnostic trees 4.1 to 4.3 in [Optimization](optimization-and-diagnostics.md).
3. Check change history and import history for the start date.
4. If tracking: hand off to measurement as P1; do not change bids while data is broken. Consider switching smart bidding campaigns to Maximize clicks with a cap or Enhanced CPC only if broken tracking will last more than 7 days.
5. If market: auction insights, competitor ads; adjust targets to margin reality.
6. If traffic quality: partner and audience exclusions; consider partners off.
7. Write a journal entry with root cause and fix; add a memory entry if the pattern repeats.

## Play 6. Peak season (ecommerce Q4, or the project's peak)

| When | Action |
|------|--------|
| 6 to 8 weeks before | Feed audit, Product explorer review, promotions in supplemental feed, asset refresh, budget plan with daily curve |
| 4 weeks before | Remarketing lists sized; customer match uploaded; NCA lists refreshed |
| 2 weeks before | Seasonality adjustments drafted for promo days only; Ad Preview Hub checks for new creatives |
| Event days | Pacing checks twice daily; disapproval watch; budget headroom |
| After event | Remove seasonality adjustment; review results; log learnings |

Microsoft published holiday planning guidance in 2026-09 covering feeds, measurement and AI visibility [Official, 2026-09].

## Play 7. B2B pipeline on Microsoft

Entry: B2B SaaS or high ticket lead gen with CRM.
1. Measurement: MSCLKID to CRM, offline goals for SQL and Closed won with values; HubSpot integration if on HubSpot (check availability).
2. Search: problem, category, competitor and brand campaigns; job seeker and student negatives.
3. LinkedIn layers: industry and job function Bid only; company list of target accounts (up to 10,000).
4. Audience campaign: company list plus job function, case study creative.
5. Bid to SQL once 30 SQLs per 30 days (pooled portfolio if needed); otherwise Enhanced CPC with LinkedIn bid adjustments.
6. Report monthly: pipeline and revenue from Microsoft by campaign and by target account.
7. Coordinate with linkedin-ads so target account messaging aligns.
Note: LinkedIn profile data excludes EEA, UK and Swiss users [Official, 2026-09]; use this play mainly for North America and other supported markets.

## Play 8. Starter tier (under $3k per month)
1. Import brand and top 2 to 3 non-brand campaigns only.
2. Enhanced CPC or Maximize clicks with a CPC cap until 15+ conversions per month.
3. Partners on, Audience Network off, location "People in".
4. Weekly 30 minute routine: search terms, publisher check every 2 weeks, budget pacing.
5. Monthly: one experiment at most.
6. Do not launch PMax without a feed and 30+ conversions per month across the account.

## Play 9. Copilot readiness sprint (2 weeks)

Entry: stakeholders ask about Copilot ads, or the account wants more AI surface coverage.
1. Explain the placement model: no Copilot campaign type; eligibility comes from Search, Shopping, AI Max and PMax.
2. Asset sweep: logos, business name, images, 15 headline RSAs, multimedia ads in every core ad group.
3. Feed sweep (ecommerce): titles, descriptions, attributes that answer conversational questions; hand off gaps to commerce-feeds.
4. Query coverage: enable broad match under conversion bidding or run AI Max as an experiment on profitable campaigns, because Copilot queries are longer and conversational.
5. Reporting check: look for a Copilot segment in network or ad distribution reports; document what exists.
6. Pilots: ask the account team about Showroom ads, dynamic filters and brand agents eligibility; never commit budget to a pilot without a written measurement plan.
7. Deliverable: `YYYY-MM-DD_microsoft-ads_copilot-readiness.md` with checklist status and the stakeholder message.

## Play 10. Europe consent compliance recovery

Entry: policy notice citing consent, conversions dropped for EEA, UK or Swiss traffic, or remarketing lists stopped growing.
1. Run the consent verification test (asc=D before consent, asc=G after) on 3 key pages.
2. Check load order: UET must load before the CMP with default denied; the CMP must not block UET entirely.
3. Hand off implementation to measurement with exact findings and the Microsoft FAQ link.
4. While fixing, freeze target changes on European campaigns; note expected under reporting.
5. After fix, confirm list growth and conversion recording for 7 days; check whether modeled conversions appear on goals.
6. Journal the root cause; add a memory entry if a CMP vendor or GTM setup caused it.

## Play 11. Lead gen quality fix
Entry: CPA on form fills looks fine but sales says leads are poor.
1. Pull CRM: Microsoft leads by stage and reason lost for 90 days.
2. Identify junk patterns: search terms, partners, devices, hours, LinkedIn segments.
3. Add negatives, exclusions and form friction where sales agrees (qualifying question, business email).
4. Switch the bidding goal to qualified lead (offline import) once volume allows.
5. Measure cost per SQL monthly; report to growth-orchestrator.
