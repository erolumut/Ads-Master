# Review Workflow and Claims Registry

> Knowledge as of 2026-10. This module defines how the compliance agent reviews customer facing material, how it maintains `ads-master/brand/CLAIMS.md`, and how it logs decisions. It applies documented rules and cites them. It is not legal advice and never invents a legal basis. Anything it cannot place under a documented rule is NEEDS HUMAN OR LEGAL REVIEW.

## 1. What goes through the gate

Every customer facing word, image, number and offer, before it is published or sent:

| Asset type | Examples | Typical owner agent | Extra checks |
|-----------|----------|---------------------|--------------|
| Paid ads | RSAs, PMax assets, Meta and TikTok ads, LinkedIn, Microsoft, ChatGPT ad cards | channel agents, creative-strategy | Platform policy pack, special categories, AI labels |
| Video and audio | UGC scripts, final cuts, voiceovers, avatars | video-studio, creative-strategy | On screen and spoken disclosure, synthetic performer rules |
| Landing and product pages | PDP copy, price display, badges, FAQ, comparison tables | cro, site-engineer, storefront-ux | Price reduction rule, drip pricing, accessibility handoff |
| Email, SMS, push, WhatsApp | Flows, campaigns, popups that collect consent | lifecycle-crm | Consent basis, İYS sync (TR), unsubscribe, sender identity |
| Feeds and listings | Merchant Center titles, Meta catalog, TikTok Shop, ChatGPT merchant feeds | commerce-feeds | Promotions, sale_price history, claims in titles |
| App store listings | App name, subtitle, screenshots, in-app purchase text | mobile-app-growth | Apple 2.3, Google Play metadata policy |
| Offers and promotions | Discounts, bundles, free gifts, subscriptions, trials | offer-strategy | Prior price, "free" rules, cancellation, renewal terms |
| Influencer and creator content | Briefs, scripts, captions, whitelisted posts | creative-strategy | Disclosure labels per country, material connection |
| Organic and AI search content | Blog, FAQ, structured data claims, llms facing pages | seo, ai-search-optimization | Same facts and claims as ads; no hidden claims in schema |

Internal documents (briefs, strategy) do not need the gate, but any claim drafted inside them is checked when it moves into an asset.

## 2. Verdicts (per line, per asset)

| Verdict | Meaning | When to use | What the requester does |
|---------|---------|-------------|-------------------------|
| APPROVED | Line may publish as written in the listed markets | Wording matches an Approved row in CLAIMS.md (or is a non claim) and every number traces to a verified fact; platform rules met | Publish after the normal G3 approval |
| APPROVED WITH EDITS | Line may publish only with the stated edit | A documented rule allows a compliant version (for example add "contains naturally occurring sugars", add prior price, add "#ad" upfront) | Apply the edit exactly; no further review if unchanged |
| NEEDS HUMAN OR LEGAL REVIEW | Do not publish yet | No documented rule covers it, evidence is missing, the rule is contested, the market is unfamiliar, or the claim is high risk (health, finance, comparative naming a competitor, environmental in the EU) | Human or counsel decides; outcome is written back to CLAIMS.md |
| BLOCKED | Do not publish in this form | A documented rule or the Blocked table prohibits it, or a fact is expired or false | Rewrite; a blocked line cannot be approved by the agent |

Rules for verdicts:
1. Every verdict other than a plain non claim cites a rule ID from the rule packs (for example `FOOD-EU-03`, `PRICE-TR-01`) and the underlying source (regulation article, platform policy name and date).
2. The agent never upgrades a NEEDS REVIEW item to APPROVED on its own judgment. Only a recorded human or legal decision does, and that decision becomes an Approved row.
3. When two markets differ, give the verdict per market (for example "APPROVED UK, BLOCKED EU").
4. Asset verdict = worst line verdict.
5. If the agent is unsure which rule applies, the verdict is NEEDS HUMAN OR LEGAL REVIEW. Never guess a legal basis.

## 3. Pre-publish review procedure

Time box: 10 to 30 minutes per asset batch; longer for a new market or regulated vertical.

1. **Intake.** Record asset IDs, channel, markets, languages, product(s), planned publish date, requester slug. Pull the asset text (copy, on screen text, voiceover transcript, captions, alt text, metadata, landing page URL).
2. **Load state.** Read `brand/CLAIMS.md`, `brand/PRODUCT_FACTS.md`, `PROJECT_BRIEF.md` section 8, `BRAND.md` claims section, `memory/compliance.md`, and the latest review log rows for the same product.
3. **Classify risk.** Use the vertical risk matrix in the SKILL (low, medium, high, prohibited-adjacent) and list the rule packs to apply: core consumer law for every asset; vertical pack; platform pack for each channel; country notes for each market.
4. **Run the screen.** `python3 <skill>/scripts/claims_check.py --claims ads-master/brand/CLAIMS.md --facts ads-master/brand/PRODUCT_FACTS.md --market <codes> <files>` (see section 8). The screen finds known patterns; it does not decide.
5. **Line by line review.** Split the asset into atomic claims (one statement each). For every claim:
   - Is it a claim at all (objective, could be true or false)? Puffery ("delicious", "you will love it") is usually not, but superlatives with numbers or rankings are.
   - Express claims and implied claims: what does the average consumer take away from the words plus the image plus the context (UCPD average consumer test; FTC net impression)? Images and before and after visuals are claims.
   - Match against CLAIMS.md: Approved (exact wording and conditions), Needs review, Blocked.
   - Match every number, rating, certification, origin and status (vegan, organic, gluten-free) to a verified PRODUCT_FACTS row that is not expired.
   - Apply the rule packs. Note the rule ID.
6. **Check the frame.** Disclosures (ad label, #ad, paid partnership, AI label), price display (total price, prior price, unit price), terms near the claim, landing page consistency (the page must support every ad claim), age gating and targeting constraints for the category.
7. **Decide verdicts** per line and per market. Write the edit for every APPROVED WITH EDITS.
8. **Write the output** `ads-master/outputs/compliance/YYYY-MM-DD_compliance_claims-review.md` (template in section 6). For platform specific checks use `_policy-check.md`.
9. **Update the registry proposal.** New compliant wording becomes a proposed Approved row; new risky wording becomes a Needs review or Blocked row. Present the diff to the human (brand files change only with approval).
10. **Append to the review log** (section 7) and write a journal entry if anything was BLOCKED in an asset that other agents are about to ship, or if a live asset is affected.
11. **Handoffs.** Price history problems to offer-strategy and commerce-feeds; page fixes to cro or site-engineer; creative rewrites to creative-strategy or video-studio; consent problems to lifecycle-crm and measurement; anything legal to the human.

## 4. Live asset sweep (monthly, or after any rule change)

1. Export live ad copy (platform exports or MCP reads), top 50 landing pages by traffic, active email flows, feed titles and promotions.
2. Run the screen on everything; diff against last month.
3. Check every PRODUCT_FACTS row with expiry inside 30 days, and every Approved claim whose basis references an expiring fact.
4. Check freshness items in the SKILL Freshness protocol for the markets and platforms in use.
5. Report: new findings, expired evidence in live copy (stop condition if a claim is now unverified), registry changes proposed.

## 5. CLAIMS.md: structure and rules

The template lives at `ads-master/brand/CLAIMS.md` with three tables. Keep the columns; the checker reads them by header name.

### 5.1 Approved
| Column | Rule |
|--------|------|
| Claim (exact wording) | The wording as it may appear. Variants need their own row. For a pattern use `/regex/` |
| Markets | Codes (EU, UK, US, TR, NL, DE, AE, SA) or `all`. EU rows cover member states |
| Legal basis or evidence | Required. Either a legal basis (for example "Reg (EU) 432/2012, vitamin C, immune function") or evidence (fact IDs, study reference). Never "common sense" |
| Conditions | Product scope, minimum amounts, mandatory accompanying text, footnotes, channels where allowed, expiry |
| Approved by | A named human (or "counsel: <firm>") |
| Date | YYYY-MM-DD of approval. Re-approve when the basis changes or expires |

### 5.2 Needs review (do not publish)
Wording that is wanted but not cleared. Each row names why, who reviews, and status (open, with counsel, rejected, approved). When the status becomes approved, move the row to Approved with the basis; when rejected, move it to Blocked with the reason.

### 5.3 Blocked
Words and patterns that must not appear. Reason must cite the rule (for example "UCPD Annex I no.4a generic environmental claim, EU from 2026-09-27"). Add market codes when the block is local.

### 5.4 Seed rows by vertical (propose on setup, human approves)
| Vertical | Blocked seeds | Needs review seeds |
|----------|---------------|--------------------|
| Food and drink | "X% fat free", "detox", disease words, "guilt-free" (brand policy) | "superfood", "boosts immunity", "natural" |
| Supplements | cure, treat, prevent + disease, weight amount and timeframe, "no side effects", doctor imagery (TR) | "clinically proven", "supports immunity" without the authorised wording |
| Cosmetics | "free from" banned substances, "chemical-free", "100% natural" without evidence | "hypoallergenic", "dermatologist recommended", "anti-aging" |
| Finance and crypto | "guaranteed returns", "risk-free", "can't lose", "get rich" | APR and "0%" offers, "no credit check" |
| Sustainability | "eco-friendly", "green", "climate neutral" (EU) | "recyclable", "sustainable", "plastic free" |
| Pricing | "lowest price ever" without data, fake "was" prices | "% off", "sale", "free" |

## 6. Output template: claims review

```markdown
# Claims review: <asset batch name>

Date: YYYY-MM-DD | Agent: compliance | Requester: <slug> | Markets: <codes> | Channels: <list>
Inputs: <files, URLs, export names and dates> | Registry version: CLAIMS.md as of YYYY-MM-DD
Screen: claims_check.py exit <0|1|2>, <n> block, <n> review (output attached in appendix)

## Verdict
Asset verdict per market: <EU: BLOCKED> <UK: APPROVED WITH EDITS> ...
One sentence on the main reason.

## Line review
| # | Asset / location | Text (exact) | Market | Verdict | Rule ID | Source | Edit or action |
|---|------------------|--------------|--------|---------|---------|--------|----------------|
| 1 | Ad A1 headline | "High protein snack" | EU | APPROVED WITH EDITS | FOOD-EU-02 | Reg 1924/2006 Annex (high protein: 20% energy) | Product is 14% energy: change to "Source of protein" |

## Facts used
| Fact ID | Fact | Evidence | Expiry | Status |

## Registry changes proposed (human approval needed)
- Add Approved: ...
- Add Blocked: ...

## Needs human or legal review
| Item | Question for the reviewer | Why the agent cannot decide | Deadline |

## Handoffs requested
- <slug>: <2 to 4 line brief>
```

## 7. Review log

Path: `ads-master/outputs/compliance/review-log.md`. Append only: add rows, never edit or delete rows. One row per reviewed asset batch. This is the audit trail the human can show a regulator or platform.

```markdown
| Date | Review file | Requester | Assets | Markets | Verdict | Block | Review | Decided by | Published? (filled later by requester) |
|------|-------------|-----------|--------|---------|---------|-------|--------|------------|----------------------------------------|
```

Retention: keep with the evidence files for at least as long as the claims run plus the limitation period counsel gives (often 3 to 6 years). [Practitioner consensus; confirm with counsel per market]

## 8. The checker script

`scripts/claims_check.py` (standard library only, Python 3.8+). Tested by `scripts/test_claims_check.py`.

| Command | Use |
|---------|-----|
| `python3 claims_check.py --claims ads-master/brand/CLAIMS.md --market EU,UK ad_copy.md` | Screen files for two markets |
| `... --text "Lose 5 kg in 2 weeks"` | Screen a line |
| `cat page.html \| python3 claims_check.py --claims ... --strip-html -` | Screen a fetched page |
| `... --facts ads-master/brand/PRODUCT_FACTS.md --facts-only` | List expired, expiring, pending or evidence-less facts |
| `... --format md` | Table for the review file appendix |
| `... --format json` | Machine readable for other agents |
| `... --fail-on block` | Use in CI so only BLOCK fails a build |
| `... --list-rules` | Print the built-in pattern pack |
| `... --no-builtin` | Only the project registry |

Exit codes: 0 clean, 1 review items, 2 blocked items, 3 input error. Where to find the script at runtime: the skill folder (`skills/compliance/scripts/` in this repo, `.claude/skills/compliance/scripts/` in a project install, or the plugin cache). If it cannot be run, apply the same patterns manually from `--list-rules` output saved in this module's appendix and say so in the review.

Limits: it matches words, not meaning. It cannot see images, implied claims, tone, targeting or missing disclosures. A clean run is never an approval.

## 9. Escalation rules (NEEDS HUMAN OR LEGAL REVIEW, always)

1. Any health, disease, medical, pharmaceutical, weight loss or supplement claim not already in Approved.
2. Any financial, credit, investment, crypto, insurance or gambling promotion.
3. Comparative claims naming a competitor, or "#1" style claims.
4. Environmental claims in the EU (from 2026-09-27) and Turkey (from 2026-08-01) not already approved.
5. Claims involving children, or ads that could reach minors in restricted categories.
6. Political, electoral or social issue content (EU: TTPA scope).
7. AI generated or altered people, voices or events presented realistically.
8. A market the registry has never covered, or a language the agent cannot verify.
9. Contested rules (marked [Contested] in the packs) and any rule marked [Unverified].
10. Anything a regulator, platform or competitor has already challenged.

## 10. Anti patterns

- Approving because "competitors say it": competitor ads are not a legal basis.
- Treating a platform approval as legal clearance: platform review is automated and does not check national law.
- Copying an authorised EU health claim but dropping its conditions of use.
- Fixing an ad but not the landing page, feed title or email that carries the same claim.
- Letting evidence expire while the claim runs (stop condition in INCIDENTS.md).
- Writing approvals into memory or journal instead of CLAIMS.md.
