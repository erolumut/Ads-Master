# Compliance Playbooks

> Knowledge as of 2026-10. Step by step plays for the situations the compliance agent meets most. Each play states the trigger, inputs, steps, outputs and handoffs. All plays respect `ads-master/GUARDRAILS.md`: the agent drafts, reviews and recommends; it never publishes, pauses, edits live assets or contacts regulators, platforms or customers.

## Play 1: Onboarding the registry (new project or cold start)

Trigger: `ads-setup` just ran, or `brand/CLAIMS.md` and `brand/PRODUCT_FACTS.md` are empty.
Time box: one session.

1. Read PROJECT_BRIEF.md (markets, languages, products, section 8 constraints), BRAND.md and the current site.
2. Classify the vertical risk level (SKILL adaptation matrix) and list markets.
3. Harvest current claims: crawl or read the homepage, top 10 PDPs or landing pages, the top 20 live ads (exports or MCP reads), the welcome email flow and feed titles. Run `claims_check.py` on everything.
4. Build a claims inventory: every distinct claim with where it appears.
5. Run the fact intake interview ([Product facts](product-facts-and-evidence.md) section 7) and add PRODUCT_FACTS rows as pending.
6. Draft CLAIMS.md: Approved only where evidence and a rule exist; everything else Needs review; seed Blocked rows for the vertical and markets ([Workflow](review-workflow-and-registry.md) section 5.4).
7. List live problems as an incident candidate list (published BLOCKED claims are a stop condition).
8. Output `outputs/compliance/YYYY-MM-DD_compliance_registry-baseline.md` with the inventory, proposed registry, live issues ranked by risk, and evidence requests to the human.
9. Journal entry for all agents: "Registry baseline ready; use only Approved rows".

## Play 2: Launch gate for a campaign

Trigger: a channel agent, creative-strategy, cro or lifecycle-crm asks for approval before a G3 publish.

1. Collect the full package: every ad variant (all headlines and descriptions for RSAs and PMax asset groups), video scripts and final cuts with captions, landing pages, emails, feed promotions, targeting summary (age, geography, special ad category).
2. Run the screen per market.
3. Line review with verdicts ([Workflow](review-workflow-and-registry.md) section 3).
4. Check the landing page carries the same claims, prices, disclosures and terms.
5. Check platform eligibility for the category (certifications, permissions, special ad categories).
6. Write `_claims-review.md` and, if platform rules dominate, `_policy-check.md`.
7. Verdict summary to the requester: the asset IDs cleared, the edits required, the items waiting on humans.
8. Append to the review log.
Quality bar: no line without a verdict; every non trivial verdict cites a rule ID and source.

## Play 3: Fast lane for creative batches

Trigger: weekly creative batch from creative-strategy or video-studio (20 to 100 variants).

1. Ask for the batch as a single text export (ID, platform, market, copy, on screen text, voiceover).
2. Run `claims_check.py --format md` over the export.
3. Variants using only Approved wording and no flags: APPROVED in bulk (state the registry date).
4. Review flagged lines individually; group identical issues.
5. Video: check disclosure frames (first seconds for creator content, AI labels, legal supers readable for long enough).
6. Return a table of variant IDs with verdicts; recurring issues become registry rows.

## Play 4: Disapproval or account restriction recovery

Trigger: ads disapproved, limited, or an account warning or suspension.

1. Get the exact policy name, the affected assets and the date (Google GAQL in [Platform policies](platform-ad-policies.md) section 3; Meta Account Quality; TikTok ad review; Microsoft editorial status).
2. Read the live policy text and the changelog for recent changes.
3. Decide: true violation, ambiguous, or wrong flag.
4. True violation: rewrite (asset and landing page), add the pattern to CLAIMS.md Blocked, and sweep all other live assets for the same pattern.
5. Wrong flag: draft the appeal text with evidence (certificate, licence, page screenshot) for the channel agent.
6. Account level warning or suspension: stop condition. Journal immediately; the channel agent stops launches; the human decides on appeals.
7. Track in the review log; three similar rejections in 30 days require a registry update.

## Play 5: Incident: a prohibited or unverified claim is live

Trigger: the sweep, a human, a customer complaint, a competitor or a platform finds a BLOCKED claim or an expired fact in live copy. This is a stop condition in INCIDENTS.md.

1. Confirm with evidence (screenshot, URL, ad ID, date, markets, spend or sends affected).
2. Classify severity: high (health, finance, children, safety, gambling, alcohol in a ban market, environmental in the EU or TR, fake reviews) or medium (pricing, superlatives, missing disclosures).
3. Alert the human with the recommendation: pause the affected ads, revert the page or stop the flow. The human approves the pause (G3); the channel or site agent executes.
4. Preserve evidence for counsel.
5. Find every other place the claim appears (ads, PDPs, feeds, emails, social posts, AI search pages, marketplaces).
6. Draft the compliant replacement and the registry change.
7. Append an incident row to INCIDENTS.md and a journal entry; prevention rule (new Blocked row, new checklist item).
8. If a regulator letter or legal threat exists: route to the human and counsel only; the agent does not respond.

## Play 6: Regulatory change sweep

Trigger: a rule in the Freshness protocol changes or a dated rule starts (examples: EU environmental claims from 2026-09-27; Turkey 10 day price rule and influencer labels from 2026-08-01; EU withdrawal button from 2026-06-19; CCD2 from 2026-11-20; EU AI Act Art 50(2) grace ends 2026-12-02; UK subscription regime January 2027).

1. Summarise the change with source and date; list affected markets, channels and asset types.
2. Write the new rule rows into the relevant pack proposal (knowledge files change only with approval) and the project registry (Blocked or Needs review rows).
3. Sweep live assets with the screen plus a targeted manual check (images and names for environmental claims, price history for reductions, creator posts for labels).
4. Produce a fix list per owner agent with deadlines before the start date.
5. Journal entry `YYYY-MM-DD_HHMM_compliance_rule-change-<topic>.md`.

## Play 7: New market entry

1. Read [Country notes](country-notes.md); if the market is missing, run its new market intake.
2. Translate the registry: approved claims do not travel automatically; each needs the market's basis (EU authorised claims cover the EU only; TR needs TİTCK list; US needs FTC level substantiation).
3. Local labels: influencer label words, AI disclosure language, price reduction look-back, mandatory warnings.
4. Consent: local channel consent rules and registries (İYS in Turkey).
5. Platform category availability in that country (alcohol, gambling, finance lists).
6. Output: market rule card in `outputs/compliance/YYYY-MM-DD_compliance_market-<code>.md` and registry rows with the market code.

## Play 8: New product launch dossier

1. Collect specs, recipe or formula, certificates, test reports, pricing and markets.
2. Classify the product (food, supplement, cosmetic, device, software, service).
3. Draft the facts table and the claim menu: claims it qualifies for per market (for food, compute every Annex threshold from the nutrition table), claims it must not make, and claims needing studies.
4. Human approves; CLAIMS.md Approved rows created before creative briefs start.
5. Brief creative-strategy with the claim menu.

## Play 9: Sale event (Black Friday, Ramadan, 11.11, summer sales)

1. 30 days before (EU) or 10 days before (TR): freeze reference prices and export price history per channel and SKU; offer-strategy owns prices.
2. Review every discount claim against the history (PRICE-EU-01, PRICE-TR-01, PRICE-UK-01, PRICE-US-01).
3. Timers and stock claims tied to real end times and inventory.
4. "Free" gifts and free shipping thresholds stated with conditions.
5. Feeds: sale_price and promotion annotations match site prices (commerce-feeds).
6. Emails and SMS: consent status and quiet hours.
7. Post event: archive price evidence with the review log.

## Play 10: Influencer and creator program setup

1. Market label table ([Reviews and influencers](reviews-endorsements-and-influencers.md) section 3) into the creator brief.
2. Contract clauses (section 4 of that module).
3. Pre-approval of scripts for regulated claims; spot checks of live posts weekly.
4. Registration and permit checks (NL CvdM, UAE Advertiser Permit, Saudi Mawthooq).
5. Spark Ads or partnership ads: the paid version needs the same disclosure plus platform ad labels.

## Play 11: Competitor challenge or regulator inquiry received

1. Do not reply. Log it, preserve the asset and evidence, and alert the human.
2. Assemble the substantiation file for the challenged claim (facts, studies, approvals, review log rows).
3. Recommend whether to pause the claim pending counsel's view.
4. After the outcome: update CLAIMS.md and memory (if the decision is a confirmed pattern).

## Play 12: Monthly registry review (heartbeat)

1. `claims_check.py --facts ... --facts-only` for expired and expiring facts.
2. Sweep live assets (Play 3 style) and compare with last month.
3. Freshness checks for markets and platforms in use.
4. Needs review backlog: chase owners; close stale rows.
5. Output `YYYY-MM-DD_compliance_registry-review.md` for the ads-review monthly cycle.
