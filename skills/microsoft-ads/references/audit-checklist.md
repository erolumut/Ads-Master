# Microsoft Advertising Audit Checklist (scored)

> How to use: mark each item Pass, Fail or N/A. Severity weights: Critical 10, High 5, Medium 3, Low 1. Score = sum of weights for Pass / sum of weights for applicable items x 100. State the data source and date range at the top of the audit. Save as `ads-master/outputs/microsoft-ads/YYYY-MM-DD_microsoft-ads_audit.md`.

## A. Measurement (run first; Critical failures stop the audit)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | UET tag fires on every page | Conversions, remarketing and bidding depend on it | UET Tag Helper on home, product or service, cart or form, thank you pages | Critical | Install via GTM or platform integration |
| A2 | Primary conversion goal recording in last 7 days | Bidding trains on it | Conversion goals page status and counts | Critical | Fix goal or event |
| A3 | Only true goals have "Include in conversions" on | Micro goals distort bidding | Goals list | High | Turn off for micro goals |
| A4 | Revenue values dynamic (ecommerce) or staged (lead gen) | Value bidding needs values | Goal settings, test purchase | High | Pass revenue_value or set stage values |
| A5 | UET consent mode for EEA, UK, Swiss traffic with default denied before CMP | Required since 2025-05-05; tracking and remarketing can be disabled | asc=D before consent, asc=G after | Critical (if such traffic exists) | Implement per [Measurement](measurement-uet-and-conversions.md) |
| A6 | MSCLKID auto-tagging on and captured in CRM (lead gen) | Offline import needs it | Test click, CRM field populated | High | Capture script, hidden field |
| A7 | Offline conversions uploaded at least weekly with 90%+ match | Qualified lead bidding | Upload history | High (lead gen) | Automate upload |
| A8 | Enhanced conversions considered and enabled where consent allows | Better matching | Goal setting | Medium | Enable per goal |
| A9 | Platform conversions reconcile with backend within 10% to 25% | Trust in numbers | Monthly comparison | High | Investigate duplicates or gaps |
| A10 | Attribution model and windows documented in MEASUREMENT.md | Changes shift reported results | MEASUREMENT.md | Medium | Document; coordinate DDA change |

## B. Account settings

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Time zone and currency match business reporting | Comparisons and pacing | Account settings | Medium | New account if wrong |
| B2 | MFA on all users; least privilege roles | Security | User list | High | Enforce |
| B3 | Billing healthy, alerts set | Serving stops on payment failure | Billing page | High | Update method, alert |
| B4 | Auto-apply recommendations off unless approved | Unapproved changes | Recommendations settings | High | Turn off |
| B5 | Shared negative and website exclusion lists exist | Waste control | Shared library | Medium | Create |
| B6 | Microsoft Places claimed (local) | Location assets | Places account | Medium (local) | Claim |
| B7 | Clarity linked | Diagnosis and CRO | Clarity settings | Low | Link |

## C. Import and sync

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Scheduled import scope documented | Prevents silent overwrite | Import schedule, journal | High | Document and restrict |
| C2 | Diverged fields excluded from scheduled import | Protects Microsoft changes | Import options | High | Set "do not update" equivalents |
| C3 | Post-import fix list applied (location intent, distribution, audience network, tracking) | Imported defaults leak spend | Settings per campaign | High | Apply list |
| C4 | No Google only parameters in tracking templates | Broken tracking | Tracking templates | Medium | Replace with Microsoft equivalents |

## D. Search campaigns

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Brand and non-brand separated | Budget and bidding clarity | Campaign list | High | Split |
| D2 | Location target "People in" (unless travel) | Spend outside market | Campaign location options | High | Change |
| D3 | Audience Network exposure deliberate on Search | Display style traffic in search | Settings, network segment | High | Opt out or adjust |
| D4 | Partner publishers reviewed in last 30 days | Partner waste | Publisher report and exclusions | Medium | Exclude failing domains |
| D5 | Search terms reviewed in last 14 days | Waste | Change history for negatives | High | Weekly routine |
| D6 | Wasted search term spend under 15% of non-brand | Efficiency | Search term report | High | Negatives, match types |
| D7 | Every ad group has an RSA with 15 headlines, 4 descriptions | Ad strength, eligibility | Ads report | Medium | Write assets |
| D8 | Sitelinks, callouts, snippets, images, logo on core campaigns | CTR, Copilot eligibility | Assets report | Medium | Add assets |
| D9 | Multimedia ads in core ad groups | Right rail and Copilot eligibility | Ads report | Low | Add |
| D10 | No disapproved assets older than 7 days | Lost eligibility | Asset status filter | Medium | Bulk edit, appeal |
| D11 | AI Max decision documented (on, off, experiment) | Expansion risk and upside | Campaign settings, journal | Medium | Decide and test |
| D12 | Quality score 5+ on top spend keywords | Cost and rank | Keyword report | Medium | Relevance and landing page |

## E. Performance Max and Shopping

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Merchant Center feed approval 95%+ | Shopping ceiling | Merchant Center, Product explorer | Critical (ecommerce) | commerce-feeds |
| E2 | Brand exclusions on PMax | Brand cannibalization | Campaign settings | High | Attach brand list |
| E3 | Negative keyword list linked to PMax | Waste | PMax negatives | High | Link list |
| E4 | No accidental product overlap between PMax and Shopping | Same auction competition since 2025-05 | Listing groups and product groups | Medium | Split by label |
| E5 | NCA settings match strategy and lists are fresh | New customer premium accuracy | Goal settings, list upload date | Medium | Refresh monthly |
| E6 | Landing page report reviewed monthly | Non commercial URL spend | Report | Medium | URL exclusions |
| E7 | Asset groups fully populated (images, logos, video) | Auto generated assets otherwise | Asset group | Medium | Add assets |
| E8 | Custom labels used for margin or priority splits | Profit control | Feed | Medium | Add labels |

## F. Audiences and targeting

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Remarketing lists exist and grow | Recovery and exclusions | Audience library sizes | Medium | Create lists |
| F2 | Converters excluded where appropriate | Waste | Combined lists | Medium | Exclude |
| F3 | B2B: LinkedIn industry and job function layers applied as Bid only | Unique B2B lever | Audience settings | High (B2B) | Add layers |
| F4 | B2B: company list for target accounts | ABM | Audience library | Medium (B2B) | Upload |
| F5 | Demographic and device adjustments based on 30+ days of data | Efficiency | Reports vs settings | Medium | Adjust |
| F6 | Audience campaign placements reviewed | Brand safety, waste | Placement report | Medium | Exclusions |

## G. Bidding and budgets

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Bid strategy matches conversion volume | Learning stability | Conversions per campaign vs strategy | High | Change strategy or pool |
| G2 | Targets set from Microsoft data | Different auction | Target vs trailing CPA or ROAS | High | Reset |
| G3 | Budget limited campaigns are profitable | Scale where it pays | IS lost to budget vs CPA | Medium | Reallocate |
| G4 | Bid adjustments not wasted on strategies that ignore them | Clarity | Strategy and adjustments | Low | Remove or restructure |
| G5 | Seasonality adjustments only for short events | Avoid distortion | Bid strategy settings | Low | Remove stale ones |
| G6 | Pacing within 0.9 to 1.1 of plan | Budget control | Pacing calc | Medium | Adjust budgets |

## H. Testing and governance

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | At least one experiment run per quarter (Growth and above) | Learning | Experiments page, EXPERIMENTS.md | Medium | Plan from backlog |
| H2 | Change history matches approved change lists | Governance | Change history vs journal | High | Investigate |
| H3 | API or script integrations on SOAP have a REST migration plan before 2027-01-31 | Breakage risk | Integration inventory | High (if applicable) | Plan migration |
| H4 | Policy disapprovals resolved within 7 days | Lost eligibility | Policy center | Medium | Fix or appeal |

## Scoring rubric

| Score | Grade | Meaning | Next step |
|-------|-------|---------|-----------|
| 90 to 100 | A | Well run; focus on scale tests | Scale playbook, experiments |
| 75 to 89 | B | Solid with gaps | Fix High items within 2 weeks |
| 60 to 74 | C | Material waste or risk | Fix Critical and High in order; re-audit in 30 days |
| under 60 | D | Unreliable | Freeze scaling; measurement and structure rebuild |

Override rule: any failed Critical item caps the grade at C regardless of score, and a failed A1, A2 or A5 caps it at D until fixed.

## Audit report template
```
# Microsoft Ads audit: <account>
Date: YYYY-MM-DD | Data: <files or connector>, <date range>
Score: <n>/100 (<grade>) | Critical fails: <list>
## Top 10 fixes (impact x confidence x ease)
| # | Item | Fix | Expected impact | Effort | Approval |
## Waste quantified
## Upside quantified
## Handoffs requested
## Next audit date
```
