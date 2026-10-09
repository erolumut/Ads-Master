# Commercial Pricing Report (template)

> The deliverable of every full engagement. Save as `ads-master/outputs/pricing-strategy/YYYY-MM-DD_pricing-strategy_commercial-pricing-report-<scope>.md`. Never overwrite; a revision is a new dated file. The structure follows the style of a senior consultant's DTC brief (the Amara pattern: retail shelf price vs DTC bundles, full cost per unit, competitor packs per unit, positioning, entry, hero and stock up bundles, delivery thresholds, launch economics, channel conflict, risks, decisions).

Writing rules:
- First page answers the question. A reader who stops after the summary knows the price, the ladder, the delivery policy, the margin and the top risk.
- Every number carries its source and date range, or the label "assumption" or "illustrative".
- Prices the customer sees are incl VAT. Margins are ex VAT. Say so in the header.
- FACTS, INTERPRETATION and RECOMMENDATION are visibly separated in every section that mixes them.
- No customer facing wording is final; claims and price displays go to `compliance`.

---

## Template

```markdown
# Commercial Pricing Report: <brand>, <scope (products, markets, channels)>

Date: YYYY-MM-DD | Author: pricing-strategy | Status: draft for decision
Prices incl VAT unless stated; margins and contribution ex VAT. Currency: <EUR/TRY/...>
Data used: <list with date ranges, e.g. order export 2025-10-01 to 2026-09-30; cost sheet v3 2026-09; shelf check AH 2026-10-04; competitor sites 2026-10-05>

## 0. Summary (the recommendation in 8 lines)
- Today: you sell <hero> at <X per unit> on DTC and the retailer shelves it at <Y per unit>.
- Market: competitors sell at <range per unit> (median <M>), most with free delivery above <Z range>.
- Position: <premium/parity/value> is defensible because <2 proofs>; weak on <1 or 2>.
- Cost: full cost <C per unit>; an order costs <F> to serve; single unit orders lose <L>.
- Recommendation: ladder <Entry N1 at P1>, <Hero N2 at P2>, <Stock up N3 at P3>; minimum basket <N or value>; free delivery from <threshold>.
- Margin: CM2 <a to b%> across rungs; blended CM2 per order <value> at the expected mix.
- Channel: DTC per unit sits <+/-x%> vs shelf at the hero rung; conflict risk <low/medium/high> because <reason>.
- Top risk and mitigation: <one line>. Decisions needed: <count>, see section 11.

## 1. Current state
FACTS
| SKU / pack | Channel | Price incl VAT | Units | Per unit | Per 100 g / serving | Delivery fee | Threshold | Promo last 90 days | Source, date |
Current CM2 by top 3 basket sizes (script output). Share of orders below the minimum viable basket: <x%>.
INTERPRETATION: what the current state means (leakage, mispriced rungs, delivery subsidy).

## 2. Market and competitors
FACTS: normalized benchmark table (see competitive-price-benchmarking.md section 6)
| Competitor | Product and pack | Channel | Price incl VAT | Units | Per unit | Per 100 g | Regular or promo | Delivery terms | Source, date |
Price index: ours vs median competitor, regular and effective. Promo frequency and depth of the top 3 competitors.
INTERPRETATION: where the market clusters, where the gaps are.

## 3. Positioning hypothesis
FACTS: strengths and weaknesses table with proof
| Attribute | Us | Competitor A | Competitor B | Proof and source |
Positioning map (two axes) as a table or chart description.
HYPOTHESIS: "We are <segment> for <customer> who value <attribute>. Defensible position: <premium/parity/value> at index <range> vs <reference set>."
Evidence for willingness to pay (if any) and its strength.

## 4. Cost basis
Input sheet with confidence grades (A to D).
Margin waterfall for each proposed rung (script output, unedited).
Minimum viable basket: <charged delivery> and <free delivery>.
Sensitivity: carrier +25%, COGS +20%, returns x2, mix shift one rung down.

## 5. Recommended price architecture and prices
| Rung | Pack | Price incl VAT | Per unit | Step vs rung below | CM2 per order | CM2 % | CM2 per unit | Role |
| Entry | | | | | | | | Trial, low commitment |
| Hero (default) | | | | | | | | Best value story, most orders |
| Stock up | | | | | | | | Lowest per unit, loyalty |
Price endings and rationale (charm vs round, see price-architecture-and-pack-sizes.md).
What not to sell and why (e.g. single units on DTC).
Expected order mix and blended CM2 per order (assumption, labeled).

## 6. Delivery and minimum basket
| Policy element | Recommendation | Economics | Competitor reference |
| Minimum order | | | |
| Delivery fee below threshold | | | |
| Free delivery threshold | | | |
| Formats (letterbox, box, express) | | | |
Dead zone analysis around the threshold. Display requirement handoff (CJEU C-62/25, unit price) to compliance.

## 7. Launch economics
List price is set above. Incentive options received from offer-strategy (or requested):
| Option | Customer sees | Cost per order | CM2 per order | Breakeven volume lift | Reference price effect | Channel effect |
| No incentive | | | | | | |
| Bonus product (e.g. +4 units) | | | | | | |
| % discount | | | | | | |
| Free delivery on first order | | | | | | |
Recommendation and duration. Volume needed to justify the launch spend (if growth-orchestrator supplied media plans).

## 8. Channel conflict
Corridor table
| Rung | DTC per unit | Retail shelf per unit | Marketplace per unit | Gap vs shelf | Brand CM per unit DTC vs retail |
Conflict assessment: what the retailer sees, likely reaction, how DTC is differentiated (exclusive packs, sizes, flavors, subscriptions).
Hard line: no instruction or pressure on reseller prices; recommended prices only as recommendations. Legal items routed to compliance.

## 9. Risks
| Risk | Likelihood | Impact | Early signal | Mitigation | Owner |
Always consider: retailer reaction, competitor promo response, cost inflation, carrier surcharge changes, cannibalization of the hero rung by stock up, legal display issues, stock and cash on large packs.

## 10. Validation plan
Test or monitoring design, primary metric, guardrails, review dates, kill criteria. EXPERIMENTS.md row IDs.

## 11. Decisions for the human
| # | Decision | Options | Recommendation | If you choose otherwise |
| 1 | Hero price | A / B / C | B | ... |
| 2 | Minimum order | ... | ... | ... |
| 3 | Free delivery threshold | ... | ... | ... |
| 4 | Launch incentive | ... | ... | ... |
| 5 | Channel stance with retailer | ... | ... | ... |

## 12. Change request (if approved)
G3 lines only: price changes, threshold changes, new SKUs live. Snapshot, proposed value, start time with time zone, rollback, approver. See ads-master/templates/CHANGE_REQUEST.md.

## Appendix
Assumptions register | Sources with dates | Script inputs JSON | Raw competitor captures (links or files in data/imports/)

## Handoffs requested
- <slug>: <2 to 4 line brief>
```

---

## Worked skeleton (illustrative, Amara pattern)

All numbers below are ILLUSTRATIVE, taken from the script demo in [Cost to serve](cost-to-serve-and-margin-waterfall.md). Competitor figures are placeholders that `market-intel` must replace. This skeleton shows the shape and reasoning, not a real brand's data.

Summary lines as they would read:
- Today: you sell the hero bar at EUR 2.79 per bar on DTC (single units) and the retailer shelves it at EUR 2.99 per bar (illustrative shelf check).
- Market: performance protein competitors sell 12 packs at EUR [A] to [B] per bar (illustrative placeholders, replace with `market-intel` data dated within 30 days); natural snack competitors at EUR [C] to [D]; most offer free delivery between EUR [E] and [F].
- Position: "modern transparent nutrition" between performance protein and natural snack: certified organic and vegan (proof: certificates in PRODUCT_FACTS.md), lower protein per bar than performance brands (weakness). Defensible index: parity to +10% vs natural snack median, below performance protein on price per gram of protein (so do not lead on protein).
- Cost: full cost EUR 0.85 per bar (illustrative); an order costs EUR 7 to 10 to serve depending on carrier format (packaging, pick, carrier, payment); single bar orders lose EUR 0.76 even with EUR 4.95 delivery charged.
- Recommendation: Entry 12 at EUR 32.95 (EUR 2.75 per bar), Hero 24 at EUR 59.95 (EUR 2.50), Stock up 48 at EUR 109.95 (EUR 2.29); optional 96 at EUR 199.95 for subscribers only; no single bars on DTC; free delivery from EUR 50 (the 24 pack qualifies).
- Margin: CM2 41.5% to 47.7% across rungs; CM2 per order EUR 14.43 to 48.07.
- Channel: hero rung sits 16.5% below shelf per bar; that is visible to the retailer's buyer. Mitigation: DTC sells only multi-packs and mixed boxes not stocked in retail, and the hero DTC per bar price stays within an agreed corridor of shelf minus 10 to 20% (brand's own decision, never imposed on the retailer).
- Risk: retailer reads DTC 24 pack as undercutting. Decisions needed: 5.

Launch economics framing (illustrative): a "+4 bars free on the 24 pack" bonus costs 4 x EUR 0.85 = EUR 3.40 landed per order and keeps the visible price and the reference price intact; a 15% discount on EUR 59.95 costs EUR 8.99 incl VAT (EUR 8.25 ex VAT) of revenue per order and creates a lower price that prior price rules will then reference. `offer-strategy` owns this choice; the report shows the economics side by side.

## Review checklist before sending

- [ ] Summary answers price, ladder, delivery, margin, channel and top risk.
- [ ] Illustrative or assumed numbers are labeled where they appear, not only in the appendix.
- [ ] Script output pasted unedited, inputs JSON attached.
- [ ] Competitor data dated within 30 days (7 days in Turkey) or flagged as stale.
- [ ] Decisions are numbered with options and consequences.
- [ ] Compliance, offer-strategy and channel handoffs listed.
- [ ] Banned style: no dashes as separators, no hype words.
