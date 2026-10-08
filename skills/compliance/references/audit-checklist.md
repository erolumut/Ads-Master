# Compliance Audit Checklist (scored)

> Knowledge as of 2026-10. Use for a full compliance audit of a project's live marketing (quarterly, at onboarding, before a new market, or after an incident). Record data sources and dates at the top of the output. Severity: Critical (legal or platform exposure now; fix before any new launch), High (fix this month), Medium (fix this quarter), Low (hygiene). Each item scores 2 (pass), 1 (partial) or 0 (fail).

## A. Registry and facts (weight 15%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| A1 | CLAIMS.md exists with Approved, Needs review, Blocked tables in use | Single source of allowed wording | Open file; rows dated and owned | Critical | Play 1 |
| A2 | Every Approved row has a legal basis or evidence and a named approver | No invented basis | Inspect rows | Critical | Move unsupported rows to Needs review |
| A3 | PRODUCT_FACTS rows have evidence, source date, owner, expiry, status | Expired facts in live copy are a stop condition | `claims_check.py --facts ... --facts-only` | High | Renew or retire facts |
| A4 | No expired or pending fact used in live copy | Unverified claims live | Cross-check sweep results with facts | Critical | Incident play |
| A5 | Review log exists and is append only | Audit trail for regulators and platforms | `outputs/compliance/review-log.md` | Medium | Create; backfill last 90 days |

## B. Live claims sweep (weight 20%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| B1 | No BLOCK findings in live ads, top pages, emails, feeds | Prohibited claims | Screen exports per market | Critical | Rewrite and pause |
| B2 | All REVIEW findings resolved to Approved rows or removed | Unreviewed claims | Diff screen output vs registry | High | Review backlog |
| B3 | Images, product names and badges reviewed (implied claims) | The checker cannot see images | Manual sample of 20 top assets | High | Replace visuals |
| B4 | Landing pages support every ad claim | Destination consistency and law | Pair top 20 ads with pages | High | Align |
| B5 | Old content swept for rules that started in 2026 (EU environmental 2026-09-27, TR 2026-08-01 rules) | Old posts still visible are still advertising | Site search and social history | High | Edit or unpublish |

## C. Vertical rules (weight 15%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| C1 | Food: every nutrition claim meets the Annex threshold for the product | Threshold breaches are binary | Compute from nutrition table | Critical | Correct claim |
| C2 | Food and supplements: health claims use authorised wording, conditions and Art 10(2) statements | Unauthorised health claims | Register lookup | Critical | Rewrite |
| C3 | No disease, weight amount or absolute safety claims | Highest enforcement risk | Screen plus manual | Critical | Remove |
| C4 | Cosmetics: free-from and hypoallergenic claims meet the technical document | Common EU finding | Inspect claims | High | Rewrite |
| C5 | Regulated categories (finance, crypto, gambling, alcohol, dating, political) have licences, permissions and mandatory wording per market | Platform bans and criminal exposure | Licence facts, platform status | Critical | Pause until fixed |
| C6 | UK less healthy food: no identifiable LHF products in paid online ads or pre 21:00 TV | In force 2026-01-05 | Product NPM scores and creative | High | Brand-only creative |

## D. Pricing and promotions (weight 15%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| D1 | Price reductions use the correct reference price (EU 30 days, TR 10 days per channel, UK genuine, US 16 CFR 233) | Most common consumer law finding | Price history export vs claims | Critical | Recompute |
| D2 | Headline prices include mandatory fees | CMA fines 2025 to 2026; EU CRD | Checkout walk-through | Critical | Fix display |
| D3 | Urgency and scarcity are true and system enforced | UCPD Annex I no.7; CMA cases | Test timers and stock badges | High | Remove or wire to data |
| D4 | "Free" offers meet conditions and state terms | UCPD no.20; FTC 16 CFR 251 | Inspect offers | Medium | Add terms |
| D5 | Subscriptions: terms near CTA, express consent, easy cancellation, EU withdrawal button (since 2026-06-19), DE cancellation button, US state ARLs | Large fines (Amazon USD 2.5 billion) | Test sign-up and cancel flows | Critical | Fix flows |
| D6 | Comparative and superlative claims documented and current | Competitor challenges | Comparison files | High | Update or remove |

## E. Reviews, endorsements and influencers (weight 10%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| E1 | No fake, AI generated, gated or sentiment conditioned reviews; no suppression | FTC rule, DMCC, UCPD, TR 2026 | Review program settings and history | Critical | Stop practice; disclose |
| E2 | Ratings and counts in ads have dated sources | Unverified numbers | Facts | High | Add source |
| E3 | Creator posts carry market correct labels in the first line or first screen | Low compliance in sweeps (about 1 in 5 consistent in EU 2024) | Sample 20 posts | High | Correct and brief |
| E4 | Creator registrations and permits where required (NL, UAE, SA) | Fines | Contract records | Medium | Obtain |
| E5 | "How we verify reviews" statement near reviews (EU) | UCPD Art 7(6) | Page check | Medium | Add |

## F. Environmental claims (weight 8%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| F1 | No generic environmental claims in EU (since 2026-09-27) or TR without basis | Blacklist | Screen plus images and names | Critical | Rewrite to specific |
| F2 | No offset based product neutrality claims in EU | Blacklist | Screen | Critical | Remove |
| F3 | No self made sustainability badges in EU | Blacklist | Visual check | High | Remove |
| F4 | Specific claims state scope, percentage, standard, evidence | Misleading omissions | Inspect | High | Edit |
| F5 | Future targets backed by public plan and independent verification | UCPD Art 6(2)(d) | Plan document | High | Remove or support |

## G. Platform policies (weight 7%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| G1 | Disapproval and limited ads below 2% of active ads; root causes logged | Account health | Platform reports, GAQL | High | Play 4 |
| G2 | Special ad categories declared (Meta) and verifications complete (Google financial services, gambling certifications) | Delivery blocks and suspensions | Account settings | Critical | Channel agent fixes |
| G3 | No personal attributes phrasing in Meta ads | Top Meta rejection | Screen | Medium | Rewrite |
| G4 | Political or social issue content not running in the EU | TTPA and platform exits | Review | High | Remove |
| G5 | App store metadata free of rankings, prices and "free" in titles (Play) and matching the app (Apple 2.3) | Store rejections | Listing check | Medium | Edit |

## H. AI and synthetic media (weight 5%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| H1 | No AI customers, testimonials, experts or real person replicas | Hard line in all markets | Creative registry AI flags | Critical | Remove |
| H2 | Realistic AI people or scenes disclosed (EU Art 50 since 2026-08-02, NY 396-b, TR Art 18/8, CA from 2027-01-01) | Fines and rejections | Sample assets | High | Add disclosure |
| H3 | Chatbots and voice agents disclose AI | EU Art 50(1) | Test | Medium | Add notice |
| H4 | AI capability claims substantiated | FTC AI washing cases | Evidence file | High | Test or remove |

## I. Privacy and consent in marketing (weight 4%)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| I1 | Consent wording per channel; unticked; not bundled | GDPR, PECR, KVKK 2025/1072 | Forms review | High | Edit forms |
| I2 | TR sends only to İYS consented recipients | Fines per message | İYS sync status | Critical | Sync before sends |
| I3 | US SMS consent language, STOP and HELP, quiet hours | TCPA class actions | Flow review | High | Edit |
| I4 | No health or sensitive inference in copy or audiences | MHMDA, MODPA, platform rules | Audience list review with measurement | Critical | Remove audiences |

## J. Accessibility of marketing pages (weight 1%, handoff driven)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| J1 | Claims, prices and terms available as text, readable by screen readers, sufficient contrast | EAA since 2025-06-28 | Automated scan plus manual | Medium | Handoff to cro and site-engineer |
| J2 | Videos captioned; disclosures both visual and audio where relevant | EAA, disclosure rules | Sample | Medium | Add captions |
| J3 | Accessibility statement for EU e-commerce | EAA Annex V | Footer | Low | Add |

## Scoring rubric

1. Score each item 0, 1 or 2. Section score = points earned / points possible.
2. Weighted total = sum of section score x weight (A 15, B 20, C 15, D 15, E 10, F 8, G 7, H 5, I 4, J 1).
3. Any Critical item at 0 caps the overall grade at "At risk" regardless of the total.

| Weighted total | Grade | Meaning |
|----------------|-------|---------|
| 90 to 100 and no Critical at 0 | Controlled | Registry driven, low exposure; monthly sweeps enough |
| 75 to 89 and no Critical at 0 | Managed | Gaps in documentation or older content; fix this quarter |
| 50 to 74, or one Critical at 1 | Exposed | Material legal or platform risk; fix list this month, gate all launches |
| Below 50, or any Critical at 0 | At risk | Stop condition review; pause affected assets with human approval; Play 5 |

## Output template

```markdown
# Compliance audit: <project>
Date: YYYY-MM-DD | Agent: compliance | Markets: <codes> | Data: <exports, crawls, dates>

## Verdict (three sentences)
## Score
| Section | Score | Weight | Weighted | Critical fails |
## Critical and high findings
| ID | Finding | Evidence | Rule ID and source | Fix | Owner | Deadline |
## Registry changes proposed
## Needs human or legal review
## Handoffs requested
## Appendix: checker output, sample list, full checklist results
```
