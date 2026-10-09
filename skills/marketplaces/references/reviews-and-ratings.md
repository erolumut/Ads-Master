# Reviews and Ratings

> Knowledge as of 2026-10. Reviews decide conversion, ad efficiency and AI assistant answers. Review manipulation is the fastest path to suspension and, since 2024 to 2026, to regulatory fines. Only compliant programs are allowed in this system.

## 1. Two different things

| Type | What | Where | Owner |
|------|------|-------|-------|
| Product reviews and ratings | Customer opinion of the product (stars, text, photos) | Product page, shared across sellers of the same product | Product quality and listing accuracy |
| Seller feedback or seller score | Customer opinion of the seller's service | Seller profile, featured offer and buybox inputs | Operations (delivery, service, returns) |

Fix product reviews with product and listing changes; fix seller feedback with operations.

## 2. Legal and policy boundaries

| Rule | Scope | Label |
|------|-------|-------|
| Amazon Community Guidelines and selling policies: no incentives for reviews, no review gating (asking only satisfied customers), no reviews from family, employees or competitors' attacks, no review manipulation via variation merging, no requests to change or remove reviews | All Amazon stores | [Official, prior knowledge] |
| US FTC Rule on the use of consumer reviews and testimonials: bans fake reviews, buying positive or negative reviews, insider reviews without disclosure, review suppression; civil penalties | US, in force from 2024-10-21 | [Official, 2024-08, prior knowledge] |
| EU Omnibus Directive (Unfair Commercial Practices): fake reviews and misrepresenting reviews blacklisted; traders must say whether and how they check reviews are genuine | EU, since 2022-05-28 | [Official, prior knowledge] |
| Turkey Commercial Advertising Regulation amendment: defines consumer reviews and sets rules for their display | Turkey, from 2026-08-01 | [Official Gazette 2026-07-01, via secondary] |
| UK DMCC Act: fake reviews on the banned practices list | UK, from 2025-04-06 | [Official, prior knowledge] |

Never in this system: free products in exchange for reviews outside an official program, rebates after review, inserts that ask for 5 star reviews, inserts that offer gifts for reviews, contacting buyers to remove negative reviews, review clubs, buying accounts, "review swaps", or merging unrelated variations to borrow ratings.

## 3. Compliant programs

### 3.1 Amazon Vine
| Item | Detail | Label |
|------|--------|-------|
| Eligibility | Brand Registry brand owners; FBA offers in new condition; fewer than 30 reviews on the parent ASIN; buyable with an image and description; not adult products [Official, prior knowledge] | |
| Units | Up to 30 units per parent ASIN | [Secondary, 2026] |
| Enrollment fee (US) | Tiers per parent ASIN since 2023-10-19: 1 to 2 units USD 0, 3 to 10 units USD 75, 11 to 30 units USD 200 | [Secondary quoting Official rate card] |
| 2026 change | One source reports USD 0 for products under USD 100 from March 2026 | [Unverified] |
| Billing | Billed after 30 days if at least one Vine review exists, otherwise at first review | [Secondary quoting Official, Contested timing] |
| Other costs | Free units, FBA fees on each Vine order | |
| Reviews | Vine reviews are labeled; reviewers are free to be negative | |

When to use Vine: new ASINs with fewer than 10 reviews, in a product you are confident in. Do not use Vine to "test" an unproven product: honest negative reviews early hurt for a long time.

Vine sizing: enroll enough units to reach about 10 to 20 reviews (claim and review rates vary) [Practitioner consensus]. Cost per review example: a USD 12 product with 30 units enrolled costs about USD 710 in total, about USD 24 per review if all 30 review [Secondary example].

### 3.2 Request a Review (Amazon)
- Button in Order Details or via the Solicitations API; sends a standardized Amazon message asking for a product review and seller feedback; allowed 5 to 30 days after delivery; once per order [Official, prior knowledge].
- Automate through the Solicitations API in your own tool or a reviewed third-party tool. It is G3 (customer contact) to switch on; the human approves once for the program, and the setting is logged.
- Do not send separate review request messages through Buyer-Seller Messaging beyond what policy allows.

### 3.3 Other marketplaces
| Marketplace | Mechanism | Note |
|-------------|-----------|------|
| bol | Customers rate products and partners after purchase; bol sends requests | Partner rating shown as a score out of 10 [Practitioner consensus] |
| Trendyol | Product reviews and seller score; review requests by platform | Seller score inputs include reviews, returns, complaints, cargo [Practitioner consensus] |
| Hepsiburada | Product reviews and store score | Same logic |
| Allegro | Seller ratings (recommendation) and product reviews | Super Seller status depends on ratings [Practitioner consensus] |
| Walmart | Walmart Spark Reviewer program (similar to Vine) | Check eligibility [Unverified] |
| Etsy | Reviews after delivery | Shop rating visible |

## 4. Rating thresholds that matter in practice

| Rating | Effect | Action |
|--------|--------|--------|
| Under 3.5 stars | Conversion and ads suffer strongly; many operators stop ads [Practitioner consensus] | Pause ads (decision rule 6), fix product, consider relaunch only with a real product change |
| 3.5 to 3.9 | Visible friction; competitive disadvantage | Root cause analysis, listing expectation fixes |
| 4.0 to 4.2 | Acceptable in many categories | Improve top complaint themes |
| 4.3 and higher | Target for hero products | Maintain velocity |
| Under 10 ratings | Low trust in competitive categories | Vine, Request a Review, time |

Benchmarks are category dependent. Compare against the median rating of the top 10 results for your main keyword.

## 5. Negative review loop (weekly)

1. Export new 1 to 3 star reviews (product) and negative seller feedback.
2. Tag each by theme: product defect, expectation mismatch (listing), size or fit, damage in transit, wrong item, delivery, customer service.
3. Route: defect and quality to the product team (journal entry); expectation mismatch to listing fix ([Listing optimization](listing-optimization.md)); transit damage to packaging and fulfillment; delivery and service to operations.
4. Seller feedback that violates policy (for example product review in seller feedback, obscene language, personal information) can be submitted for removal through the official process. Product reviews can be reported only if they violate Community Guidelines. Never pressure customers.
5. Public responses: Amazon removed public comments on reviews years ago for most cases; bol, Trendyol and Hepsiburada allow seller answers in some flows. Answer factually, never argue, never reveal order data.
6. Track monthly: share of reviews by theme, rating trend, return reasons. The same themes appear in AI review summaries ("Customers say") that shoppers and Alexa for Shopping see.

## 6. Review velocity planning for launches

```
Target: 15 or more ratings at 4.3+ within 60 days on a new hero ASIN (category dependent)
Inputs: Vine units, organic orders per week, review rate (own history; often a low single digit percentage of orders) [Practitioner consensus]
Plan:
  Week 0: Vine enrolled with 10 to 30 units
  Weeks 1 to 8: Request a Review on every eligible order (automated after approval)
  Ads: launch ads at a level that produces enough orders for the rating target
Stop: if the average rating after 10 ratings is under 3.8, stop scaling and investigate
```

## 7. Ratings and ads

- Ads on low rated products waste money: CTR and CVR fall, CPC paid per click stays.
- Sponsored Brands and display creatives that show ratings perform better with 4 stars or more [Practitioner consensus].
- Use review themes as ad copy angles only with `compliance` approval and when backed by PRODUCT_FACTS.md.

## 8. Audit items

| Check | Pass |
|-------|------|
| No review incentives anywhere (inserts, emails, social, packaging) | Confirmed by inspection |
| Vine used only for eligible, confident products | Yes |
| Request a Review automated with approval logged | Yes |
| Negative review themes reported monthly to product team | Yes |
| Hero products at 4.3 stars or higher | Yes, or a fix plan |
| Seller feedback above 95% positive (Amazon) and seller scores at target on other marketplaces | Yes |
| No variation merging of unrelated products | Yes |
