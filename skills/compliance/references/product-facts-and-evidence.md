# Product Facts and Evidence

> Knowledge as of 2026-10. Every customer facing statement about a product traces to a verified row in `ads-master/brand/PRODUCT_FACTS.md`. This module defines what counts as evidence, how to record it, how long it lasts, and the substantiation standards by claim type and market. It applies documented standards; when the standard for a claim type is unclear, the claim is NEEDS HUMAN OR LEGAL REVIEW.

## 1. Principles

1. Substantiate before publishing. The EU (UCPD Art 6 and 7, Art 12 lets courts require the trader to prove factual claims), the UK (CAP Code rule 3.7: hold documentary evidence before distribution), the US (FTC Policy Statement on Substantiation: a reasonable basis before the claim is made) and Turkey (Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği: the advertiser bears the burden of proof) all put the burden on the advertiser. [Official, canonical texts]
2. Evidence must match the claim exactly: same product (formula, size, version), same population, same condition of use, same market.
3. A fact without an owner, a source date and an expiry is unverified.
4. The words allowed in copy are recorded with the fact. Paraphrases that change meaning ("helps" to "guarantees") need their own approval.
5. Numbers decay. Ratings, customer counts, rankings, prices, delivery times and stock claims need short expiry dates.

## 2. PRODUCT_FACTS.md columns and how to fill them

| Column | What goes in | Example |
|--------|-------------|---------|
| Fact | Fact ID plus the plain fact | `F-003 Protein 14 g per 100 g; energy 400 kcal per 100 g` |
| Exact wording allowed | Public wording the fact supports | `14 g protein per 100 g`; `Source of protein` (if threshold met) |
| Applies to | Products, SKUs, sizes, markets | `Bar Original 60 g, all EU and TR` |
| Evidence | Document type, ID, location | `Lab report LR-2026-014 (accredited lab, ISO 17025), drive/evidence/LR-2026-014.pdf` |
| Source date | Date of the evidence (YYYY-MM-DD) | `2026-03-01` |
| Expiry or review date | When it must be re-checked (YYYY-MM-DD) | `2027-03-01` |
| Owner | Named person responsible | `Jane Doe (QA)` |
| Status | verified, pending, expired | `verified` |

Rules:
- Use one row per fact per product variant. Recipe changes create new rows; old rows move to expired.
- Store the evidence file outside the public site, with access for the legal reviewer. Never paste personal data from reviews or tests into the table.
- The checker flags facts that are not verified, have no evidence, are expired (BLOCK) or expire within 30 days (REVIEW): `claims_check.py --facts ads-master/brand/PRODUCT_FACTS.md --facts-only`.

## 3. Evidence types and default expiry

| Fact type | Acceptable evidence | Default review interval | Notes |
|-----------|--------------------|-------------------------|-------|
| Nutrition values | Accredited lab analysis or validated calculation from recipe plus ingredient specs (FIC 1169/2011 Art 31(4) allows declared values from analysis, calculation or established data) | 12 months or on recipe change | Tolerances: EU Commission guidance on tolerances (2012) |
| Ingredient statements (vegan, gluten-free, no added sugar) | Recipe sign-off, supplier declarations, certificates, gluten test (below 20 mg/kg for gluten-free) | 12 months, on supplier change | Supplier change is the common failure |
| Certifications (organic, Fairtrade, B Corp, ISO, Halal) | Certificate with number, scope, validity | Certificate expiry | Check the certificate covers the product and site |
| Health or nutrition claim eligibility | Regulation reference plus the fact that meets the condition of use | When the regulation or recipe changes | See food-and-nutrition-claims.md |
| Efficacy (cosmetics, devices, apps) | Study protocol and report on the product or same formula; population and endpoints matching the claim | 24 months or on reformulation | EU 655/2013 Annex criterion 3 |
| Performance numbers ("2x faster", "saves 3 hours") | Test report with method, sample, date, competitor or baseline version | 6 to 12 months | Re-run after major versions |
| Rankings and awards ("#1", "Best of 2026") | Third-party source, scope, date, category | Until the award year ends; rankings 3 months | State the source and year in copy |
| Ratings and review counts | Platform export (date, average, count, source) | 30 days | Show source near the rating |
| Customer counts, usage stats | Internal analytics export with definition | 90 days | Define "customer" (paying, active) |
| Prices and reference prices | Price history export per channel | Per promotion | See pricing-promotions-and-consumer-law.md |
| Delivery, stock, availability | Live system rules | Per campaign | Wrong delivery promises are a top complaint source |
| Origin ("Made in X") | Bill of materials, production records | 12 months | US: FTC Made in USA rule needs "all or virtually all" |
| Environmental facts | LCA, recycled content certificate, carbon accounting, third-party verification | 12 months | See environmental-claims.md |
| Testimonials and endorsements | Signed consent, proof of genuine use, disclosure of connection, typicality data | Contract term | See reviews-endorsements-and-influencers.md |
| AI capability claims | Test on representative data, error rates, scope | Each model change | FTC AI washing cases 2024 to 2026 |

## 4. Substantiation standards by claim type

| Claim type | Standard | Source |
|-----------|----------|--------|
| Objective product attribute | Documentary evidence that the attribute is true for the product as sold | CAP 3.7; UCPD Art 6; FTC substantiation policy |
| Establishment claim ("clinically proven", "tests show") | The level of proof the claim states: a test that actually establishes it | FTC substantiation doctrine; CAP 3.7 |
| Health benefit (US) | Competent and reliable scientific evidence; for most health claims, well designed randomized controlled trials on the product or an essentially equivalent formula | FTC Health Products Compliance Guidance (2022-12) [Official] |
| Health claim on food (EU, UK, TR) | Only authorised wording with its conditions; the trader's own study is not enough | Reg 1924/2006 Art 10 and 13; TR 2023 health claim regulation |
| Cosmetic claims (EU, TR, UK) | Six common criteria: legal compliance, truthfulness, evidential support, honesty, fairness, informed decision-making | Reg (EU) 655/2013 [Official] |
| Comparative claims | Like for like, material, relevant, verifiable, representative features; competitor not denigrated | Directive 2006/114 Art 4; CAP 3.33 to 3.44 |
| Environmental claims | Specific, accurate, whole life cycle where relevant, verified; EU generic claims banned from 2026-09-27 | Directive 2024/825; CMA Green Claims Code; TR 2026 amendment |
| Superlatives and rankings | Objective comparison with current market data, or clearly subjective puffery | Directive 2006/114; German case law on Alleinstellungswerbung |
| AI performance | Testing on data representative of the advertised use; accuracy numbers from that test | FTC Workado order (2025-04) [Official] |

Puffery: subjective, non measurable praise ("delicious", "beautifully made") is generally not a claim. It becomes a claim when paired with numbers, comparisons, rankings or technical terms. When in doubt, treat it as a claim.

## 5. Implied claims and visuals

Reviewers judge the net impression, not only the literal words.

| Element | Implied claim | Check |
|---------|---------------|-------|
| Before and after photos | Typical result in the shown time | Typicality data; platform policy (Meta changed rules 2026-07-22, see platform-ad-policies.md); EU and TR health claim limits |
| Lab coats, stethoscopes, pharmacy logos | Medical endorsement | TR supplement ads ban health professional imagery; EU Art 12(c) for foods |
| Green leaves, globes, recycling arrows | Environmental benefit | Treated as environmental claims in the EU (Directive 2024/825 covers images) and TR |
| Award badges and stars | Ranking or rating | Source and date |
| Product shown larger or with more content than supplied | Quantity | Show actual pack contents |
| AI generated people using the product | Genuine experience | Never as customers or experts; see ai-disclosure-and-synthetic-media.md |
| Crossed out price | Genuine prior price | Price history rule for the market |
| Countdown timer | Real deadline | Server enforced end time |

## 6. Number hygiene

- Every number in copy has a fact ID in the review file.
- Percentages need the base ("30% less sugar than our 2025 recipe", not "30% less sugar").
- Averages need the population ("average customer saved 2 hours per week, survey of 412 customers, 2026-08").
- Rounding must not inflate (4.46 stars is "4.4" or "4.5" only if the platform rounds that way; never "4.5+").
- Time-bound numbers carry the date ("10,000 customers as of 2026-09").

## 7. Fact intake interview (cold start)

Ask the human for, per hero product:
1. Full ingredient or component list and the recipe or spec version.
2. Nutrition table or technical sheet with the evidence source.
3. Certifications with numbers and expiry dates.
4. Studies or tests used in marketing so far, with the reports.
5. The 10 claims used most in current ads and pages, and where each came from.
6. Ratings sources and current values.
7. Markets sold to and languages used.
8. Any past regulator letter, platform rejection or competitor challenge.

Record answers as PRODUCT_FACTS rows with status pending until evidence is seen.

## 8. Worked examples

**Example A: protein bar, EU.** Fact F-003: 14 g protein and 400 kcal per 100 g. Energy from protein = 14 x 4 kcal = 56 kcal, which is 14% of 400 kcal. "Source of protein" (at least 12%) is allowed; "High protein" (at least 20%) is not. Verdict for "High protein bar": APPROVED WITH EDITS, change to "Source of protein", rule FOOD-EU-02.

**Example B: SaaS, US and UK.** Claim "Cuts reporting time by 70%". Evidence: one customer case study. A single case does not support a general claim. Verdict: NEEDS HUMAN OR LEGAL REVIEW, or APPROVED WITH EDITS to "Acme cut reporting time by 70% (Acme case study, 2026)" if the customer consented and results are labelled as not typical with typical results disclosed (FTC Endorsement Guides, 16 CFR 255.2).

**Example C: rating badge, all markets.** "Rated 4.8/5" with PRODUCT_FACTS F-009 pending and no evidence. Verdict: BLOCKED until the review platform export is recorded; then APPROVED WITH EDITS adding source and date ("4.8/5 on Trustpilot, 1,203 reviews, Oct 2026").

## 9. Evidence red flags

- Evidence predates a reformulation.
- Study on an ingredient, claim about the product.
- Study population differs (athletes vs general public; men only vs all).
- In vitro or animal data used for human benefit claims.
- Survey with leading questions or a sample of employees.
- "Internal data" without a definition or export.
- Supplier marketing brochure as the only source.
- Certificate scope covers another site or product line.
