# Playbooks: launch, optimize, scale, recover, migrate, peak season

> Step-by-step plays. Each play ends in a deliverable saved to `ads-master/outputs/commerce-feeds/` and a change list the human approves before anything goes live. Knowledge as of 2026-10.

## Play 1. Launch Merchant Center from zero (new store or first Shopping program)

Preconditions: store live with real products, checkout working, policy pages published.

1. Intake: platform, countries, currencies, catalog size, GTIN availability, shipping and return rules, stores (local), budget tier.
2. Site readiness: run the misrepresentation checklist in [diagnostics](diagnostics-and-disapprovals.md) section 3.1. Fix before creating the account.
3. Create Merchant Center: business info, website verify and claim, shipping and returns per country, tax where required.
4. Choose input: platform app as primary (Shopify, WooCommerce, BigCommerce) or feed file; add a supplemental source (Sheets) for overrides from day one.
5. Map attributes: brand, GTIN (barcode), MPN, Google fields (metafields on Shopify), product type, item group IDs, apparel attributes.
6. Run `feed_qa.py` on an export before first sync; fix errors.
7. Sync; wait for review (typically several business days for a new account [Practitioner consensus]).
8. Enable free listings and conversion tracking for free listings.
9. Link Google Ads; hand off to google-ads with the label plan.
10. Day 7 and day 14: review item issues, fix, document.
Deliverable: launch report with item counts, approval rate, open issues, next steps.

## Play 2. Title and attribute optimization program

1. Rank SKUs by revenue and click potential (`product_view.click_potential_rank`) and pick the top 20 percent plus zombies with search demand.
2. Gather queries (Google Ads search terms and search term insights, Search Console, site search).
3. Build templates per product type ([product data optimization](product-data-optimization.md) section 2).
4. Fill missing attributes in the source (material, size, color, compatibility).
5. Generate titles; QA (length, duplicates, banned words, unsupported claims).
6. Design the experiment (SKU split) and append to EXPERIMENTS.md.
7. Ship via supplemental source to the test cohort after approval.
8. Read out after 2 to 4 weeks with difference in differences; roll out winners; record in memory if confirmed.
Deliverable: title spec, change file, experiment readout.

## Play 3. Custom label rollout for profit-based bidding

1. Get unit costs (COGS) and contribution margin inputs from the human or ERP; get the last 60 days product performance.
2. Define the slot plan and thresholds with google-ads and meta-ads (journal request).
3. Run `label_builder.py`; review distribution (no tier above 60 percent of SKUs, no empty tier unless expected).
4. Publish to a supplemental source after approval.
5. Hand off: google-ads restructures listing groups or campaigns; meta-ads builds product sets.
6. Weekly refresh with hysteresis; monthly review of thresholds.
Deliverable: label spec, first label file, handoff briefs.

## Play 4. Scale to new channels (Microsoft, Meta, TikTok, Pinterest)

1. Confirm the master feed passes the audit at grade B or better.
2. Pick channels from the rollout table in [Microsoft, Pinterest and other catalogs](microsoft-pinterest-and-other-catalogs.md) section 5.
3. For each: create catalog or store, verify domain, connect source (native app or feed tool transform), map IDs to the cross-channel scheme.
4. Align pixels (measurement) before campaigns.
5. Build product sets or product groups mirroring Google labels.
6. QA counts and errors per channel at day 3 and day 10.
Deliverable: channel launch checklist with counts and issues per channel.

## Play 5. AI commerce readiness (ChatGPT, Google AI Mode and UCP, Copilot, Perplexity)

1. Fix the basics: identifiers, price parity, policies, structured data, crawl access (agent access policy decided by the human).
2. Platform toggles: Shopify AI channels and Catalog sharing; Copilot Checkout opt-in or opt-out; document the decision.
3. Non-Shopify: apply at chatgpt.com/merchants with SKU count and feed readiness; build the OpenAI-format feed from the master; prepare SFTP delivery.
4. Google: enrich conversational attributes (Q&A, related products, variant options, documents, video); request UCP early access if the human wants checkout in AI Mode and engineering capacity exists.
5. Perplexity: join the merchant program; check PayPal integration if using PayPal.
6. Measurement: AI assistant channel grouping; order source tags for in-chat checkouts.
7. Paid: hand off product feed ads in ChatGPT to chatgpt-ads with the feed location and refresh method.
Deliverable: AI commerce readiness memo with scores (see [ChatGPT module](chatgpt-shopping-and-agentic-commerce.md) section 9) and decisions needed.

## Play 6. Recover from a mass disapproval or a data source failure

1. Quantify: items affected, revenue share, destinations.
2. Check the data source history: fetch failure, credential expiry, file truncated, platform app disconnected, API quota.
3. Restore the last good feed (keep a copy of the last good file) or reconnect the app.
4. If a rule caused it, revert the rule (from the exported rule log).
5. Re-run QA; confirm item counts recover over 24 to 72 hours.
6. Post-incident journal entry: cause, detection time, fix, prevention (alert added).

## Play 7. Recover from account suspension (misrepresentation or other policy)

Follow [diagnostics](diagnostics-and-disapprovals.md) section 3.1. Add:
- Day 0: alert human and growth-orchestrator with revenue at risk; pause plans that depend on Shopping.
- Day 0 to 3: full site and data audit, fix list, human approves site changes.
- Day 3 to 5: request review once.
- If rejected: second audit focusing on less obvious triggers; consider an expert review; never open a new account to bypass.
- Meanwhile: shift budget to channels not affected (growth-orchestrator decides).

## Play 8. Migration plays

### 8.1 Content API to Merchant API (deadline passed 2026-08-18)
1. Inventory every integration that wrote to Merchant Center (custom code, scripts, older plugins, feed tools).
2. For each: confirm it now uses Merchant API (ask the vendor for the date they switched) or replace it.
3. Custom code: move to `productInputs` writes into a named data source, read `products` for status, handle base64url IDs, `version_number`, 30-day refresh, Notifications sub-API.
4. Google Ads scripts reading Merchant Center: update to the Merchant API service in scripts.
5. Validate item counts and statuses before and after.

### 8.2 Replatforming (for example custom to Shopify)
1. Export old IDs, titles, labels and performance.
2. Decide: keep old IDs (map them in the new feed via supplemental source or feed tool) or accept new IDs (performance history resets).
3. Keep the old feed live until the new one is approved; then switch primary sources with a short overlap and no duplicate IDs.
4. Redirect old product URLs to new ones; update `link` in the same release.
5. Watch Shopping performance for 4 weeks; hand off to google-ads to expect a learning period.

## Play 9. Peak season (Black Friday, Cyber Monday, holiday, local events)

| When | Action |
|------|--------|
| 8 weeks before | Audit at grade B or better; fix Critical and High items |
| 6 weeks | Promotions calendar; submit promotions early; seasonal custom label values set |
| 4 weeks | Stock forecasts into low stock labels; price competitiveness review; image refresh for top SKUs |
| 2 weeks | Feed change freeze except fixes; increase refresh frequency for price and stock; alerts tightened (feed age over 1 hour) |
| Event days | Monitor disapprovals and mismatches every few hours; sale price effective dates verified |
| 1 week after | Remove seasonal labels and expired promotions; post-mortem in journal |

## Play 10. Zombie SKU revival test
1. Identify zombies (eligible, under 50 impressions in 30 days) with real demand (best sellers report, site search, Keyword Planner).
2. Fix data first (title, GTIN, image, price competitiveness).
3. Hand off to google-ads: isolate zombies in their own campaign or asset group for 4 to 6 weeks with a modest budget and lower target.
4. Graduate SKUs that convert to the main structure; exclude or discontinue proven losers (human decides on catalog).
Deliverable: zombie analysis, test design in EXPERIMENTS.md, readout.

## Play 11. Monthly feed health report
Sections: data used; item counts per channel; approval rate trend; top issues; parity rate; zombie rate; label distribution; title program progress; AI surface status; next month plan; handoffs requested. Save as `YYYY-MM-DD_commerce-feeds_monthly-report.md`.

## Play 12. Weekly feed operations routine (30 to 60 minutes)
1. Pull status: item counts per channel, disapprovals by reason, account issues, data source history (Merchant API or exports).
2. Compare to last week's journal entry; flag any metric outside thresholds in [feed tools](feed-tools-and-automation.md) section 3.
3. Fix or ticket the top 5 issues by revenue at risk.
4. Run `feed_qa.py` on the latest export; run `pdp_parity.py` on 50 SKUs (top revenue plus random).
5. Refresh labels (Play 3 routine) and post the tier move summary.
6. Check freshness sources for platform changes (Merchant Center announcements, OpenAI merchants page, UCP repo, Shopify changelog).
7. Write the weekly journal entry: metrics, changes shipped, issues open, handoffs requested.
