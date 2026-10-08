# Measurement Audit Checklist (scored)

Run the whole checklist for a full audit; run sections for targeted audits. Mark each item Pass, Fail, Partial (half points) or N/A. Record evidence (screenshot, query, file and line) for every Fail.

Severity weights: Critical 10, High 6, Medium 3, Low 1.

## A. Strategy and definitions

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| A1 | MEASUREMENT.md lists every conversion with definition, trigger, dedup key, value rule, primary or secondary per platform | Shared truth across agents | Read file | Critical | Write the measurement plan |
| A2 | Source of truth named for revenue and lead quality | Reconciliation target | MEASUREMENT.md | High | Name system and owner |
| A3 | KPI tree with North Star and guardrails | Prevents optimizing the wrong metric | MEASUREMENT.md, STRATEGY.md | Medium | Draft with growth-orchestrator |
| A4 | Optimization event per platform is the deepest event with enough volume | Bidding quality | Platform settings vs volumes | High | Move up or down the ladder |
| A5 | Monthly reconciliation exists and is recent (under 45 days) | Detects drift | Outputs folder | High | Start monthly reconciliation |

## B. GA4

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| B1 | One GA4 configuration per page (no double tagging) | Duplicate events | Network tab, Tag Assistant | Critical | Remove duplicate |
| B2 | Purchase or lead events carry transaction_id or lead ID, value, currency | Dedup and revenue | DebugView, BigQuery | Critical | Add parameters |
| B3 | Duplicate transaction rate under 1% | Inflated revenue | BigQuery query | High | Once-only guard |
| B4 | Capture rate vs backend within expected band by region (track trend) | Data completeness | Reconciliation | Critical | Server-side purchase, fix tags |
| B5 | Event data retention 14 months (or 360 maximum) | Analysis depth | Admin | Medium | Change setting |
| B6 | Internal and developer traffic filters Active | Clean data | Admin > Data filters | Low | Activate |
| B7 | Unwanted referrals include payment and SSO domains | Credit theft | Referral report | High | Add domains |
| B8 | Cross-domain configured for all journey domains | Session breaks | Tag settings, _gl on links | High | Configure domains |
| B9 | Key events limited to outcomes and documented proxies | Clean imports | Admin | Medium | Remove noise |
| B10 | Google Ads link active with auto-tagging on | Attribution and audiences | Admin, Google Ads settings | High | Link and enable |
| B11 | BigQuery export on (Growth tier and above) | Raw data, no retention limit | Admin | High | Link now |
| B12 | Unassigned under 5% of sessions | Channel accuracy | Traffic acquisition | Medium | Fix UTMs, MP session_id |
| B13 | No PII in page_location, page_title or parameters | Policy and law | BigQuery regex search for @ and phone patterns | Critical | Redact at source |
| B14 | Custom channel group with AI assistants and paid AI channels | AI traffic visibility | Admin | Low | Create group |
| B15 | SPA page views counted once per route change | Funnel accuracy | DebugView on navigation | High | Pick one method |
| B16 | Currency and timezone match backend | Reconciliation | Admin | Medium | Align |

## C. Tag management and server-side

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| C1 | Single tag manager path (no hard-coded duplicates of GTM tags) | Duplicates | Code search, network | High | Consolidate |
| C2 | GTM publish rights limited, versions named with notes | Change control | GTM Admin, versions | Medium | Restrict, document |
| C3 | Triggers use data layer events for conversions, not URL or click guesses | Reliability | GTM triggers | High | Data layer contract |
| C4 | Ecommerce object cleared before pushes | Stale items | Code, preview | Medium | Push ecommerce null |
| C5 | Google tag gateway or sGTM first-party serving evaluated (Growth and above) | Resilience | Network, GTM gateway status | Medium | Enable gateway |
| C6 | sGTM (if used) on same-origin path or IP-aligned domain; min instances set; monitoring | Cookie life, uptime | DNS, Cloud Run settings, logs | High | Reconfigure |
| C7 | Unused tags and vendors removed in the last 6 months | Speed and leakage | Tag inventory | Low | Clean up |
| C8 | Purchases (or leads) also sent server-side for paid platforms | Browser loss | Platform event sources | High | Add CAPI |

## D. Consent and privacy

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| D1 | Consent default fires before any tag in opt-in regions | Legal and modeling | Tag Assistant consent tab, gcs parameter | Critical | Consent Initialization |
| D2 | CMP updates consent on choice and on page load for returning users | Data loss or violations | Preview, network | Critical | Fix CMP integration |
| D3 | All four consent mode v2 parameters sent (ad_user_data, ad_personalization included) | Google EU consent policy | gcd parameter, GA4 consent settings | High | Update CMP template |
| D4 | Non-Google ad tags blocked or consent API used when denied | Violations | Reject all test | Critical | Additional consent checks |
| D5 | Server events respect stored consent | Violations | Code review | Critical | Consent flag in pipeline |
| D6 | Reject as easy as accept on first layer (EEA, UK, TR) | Enforcement risk | Visual check | High | CMP config |
| D7 | CMP writes TCF v2.3 strings if TCF is used | Strings created without disclosedVendors are invalid since 2026-03-01 | __tcfapi output | High | Update CMP |
| D8 | US: GPC honored, "Do not sell or share" link, LDU or restricted processing for opted-out users | State laws | GPC test | High | CMP US mode |
| D9 | No sensitive category data sent to ad platforms | Policy and law | Event and URL review | Critical | Remove, neutral names |
| D10 | Cross-border transfer mechanism documented for Turkey (KVKK) and EU vendors | Fines | Transfer register | Medium | Legal review flag |

## E. Platform conversion APIs

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| E1 | Meta pixel and CAPI share event_id; dedup visible in Events Manager | Double counting | Events Manager | Critical | Shared event_id |
| E2 | Meta Purchase EMQ 6 or higher | Match and optimization | Events Manager | High | Add em, ph, external_id, fbc, fbp |
| E3 | Google enhanced conversions active without diagnostics errors | Recovered conversions | Google Ads Diagnostics | High | Code method |
| E4 | TikTok Events API live with dedup (if TikTok active) | Completeness | Events Manager | High | Add server events |
| E5 | LinkedIn CAPI or CRM sync for B2B (if LinkedIn active) | Pipeline optimization | Campaign Manager conversions | Medium | Add CAPI |
| E6 | Microsoft UET with consent mode and enhanced conversions (if active) | Completeness, EEA rules | UET Tag Helper | Medium | Configure |
| E7 | ChatGPT Ads pixel and CAPI with oppref capture (if active) | Conversion campaigns need events | Ads Manager event quality | Medium | Configure |
| E8 | Hashing and normalization correct per platform | Match rates | Code review, test events | High | Shared normalizer |
| E9 | Access tokens stored in secrets, rotated, owned by a system user | Security, continuity | Repo scan, platform settings | High | Move to secret store |
| E10 | Only one sender per platform (no app plus custom duplicate) | Double counting | Event source breakdown | High | Remove duplicate |

## F. Offline and CRM

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| F1 | Click IDs captured into CRM on 90% or more of paid leads | Closed loop | CRM report | Critical (lead gen) | Capture script, hidden fields |
| F2 | Qualified stage conversions uploaded at least daily | Bid on quality | Upload logs | High | Connector or pipeline |
| F3 | Google uploads on Data Manager (or allowlisted legacy) after 2026-06-15 | Uploads silently failing | Upload history, error codes | Critical | Migrate |
| F4 | Stage values set from current close rates | Value bidding | MEASUREMENT.md | Medium | Recalculate |
| F5 | Refunds and cancellations adjusted (Google) or excluded | Inflated values | Adjustment logs | Medium | Adjustment uploads |
| F6 | Calls tracked and qualified calls imported (local services) | Missing conversions | Call tracking | High | Add call tracking |

## G. Values

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| G1 | One value convention (tax and shipping treatment) across platforms | Comparability | Tag configs | Medium | Align |
| G2 | Profit values used where margins vary by over 15 points | Profit optimization | Margin data | Medium | Server-side profit |
| G3 | No margin or COGS exposed in browser | Competitive leak | View source, data layer | High | Move server-side |
| G4 | New customer flag sent where acquisition goals are used | NCA bidding | Tag payload | Medium | Backend flag |

## H. UTM and channels

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| H1 | UTM vocabulary documented and lowercase | Clean channels | Hygiene query | Medium | Governance sheet |
| H2 | Dynamic parameters set on every paid platform | Campaign level analysis | Platform settings | Medium | Templates |
| H3 | No UTMs on internal links | Self-attribution | Crawl, query | Medium | Remove |
| H4 | Redirects preserve query strings | Lost attribution | Test final URLs | High | Fix rules |

## I. Attribution settings

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| I1 | Attribution settings per platform recorded in MEASUREMENT.md | Interpretation | File vs platforms | Medium | Record |
| I2 | Dashboards and connectors updated for Meta 2026 changes (no 7d or 28d view queries; engage-through split) | Silent empty data | Connector config | High | Update |
| I3 | One primary conversion per goal per campaign in Google Ads | Double optimization | Conversion actions | High | Set secondary |
| I4 | Platform to backend ratios tracked monthly | Drift detection | Reports | Medium | Add to monthly |

## J. Incrementality and MMM

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| J1 | Largest channel has an incrementality read in the last 12 months (Growth and above) | Calibration | EXPERIMENTS.md | High | Plan test |
| J2 | Tests have power analysis and pre-registered stop rules | Valid results | Test docs | Medium | Template |
| J3 | Incrementality factors recorded and used in reporting | Decision quality | MEASUREMENT.md, dashboards | Medium | Add |
| J4 | MMM readiness assessed (Scale and above) | Allocation | Output file | Low | Assess |

## K. Reporting and monitoring

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| K1 | Daily automated checks (zero, spike, duplicates, capture drift, loads) | Fast detection | Scheduled queries, alerts | High | Build |
| K2 | MER, aMER, nCAC reported weekly from backend | Blended truth | Reports | High | Build |
| K3 | Annotations for tracking and attribution changes | Trend interpretation | GA4 annotations, journal | Low | Add |
| K4 | Dashboard definitions documented | Shared math | Dashboard footer | Low | Document |

## L. Apps (if applicable)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| L1 | MMP or Firebase installed with consent handling | Attribution | SDK config | Critical | Install |
| L2 | SKAN or AdAttributionKit conversion value schema documented and current | iOS optimization | Schema doc | High | Design schema |
| L3 | Server-side store notifications feed revenue truth | Revenue accuracy | Backend | Medium | Add |
| L4 | MMP vs store reconciliation monthly | Drift | Report | Medium | Add |

## Scoring rubric

```
Score = (sum of weights for Pass + half of weights for Partial) / (sum of weights for applicable items) x 100
```

| Score | Grade | Meaning |
|-------|-------|---------|
| 90 to 100 | A | Trustworthy; focus on calibration and value |
| 75 to 89 | B | Usable with known gaps; fix Highs this month |
| 60 to 74 | C | Directional only; fix before scaling spend |
| 40 to 59 | D | Unreliable; freeze big budget changes |
| Under 40 | F | Broken; foundation play first |

Caps: any Critical Fail caps the grade at C regardless of score; three or more Critical Fails cap it at D. Report the score, grade, caps applied, top 5 fixes by impact x confidence x ease, and the estimated revenue or spend at risk for each Critical.

Audit report structure: Summary, Data used, Score and grade by section, Findings table (ID, status, evidence, severity, fix, owner, effort), Change list, Test plan, MEASUREMENT.md draft update, Handoffs requested.
