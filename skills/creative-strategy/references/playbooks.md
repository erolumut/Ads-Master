# Creative Playbooks

> Step by step plays for launch, optimize, scale and recover. Each play lists trigger, steps, outputs, success metric and handoffs. All launches, pauses and setting changes are drafted as a change list for human approval; channel agents implement.

## Play 1. Cold start creative launch (new account or new product)

**Trigger:** no ads running, or no ad history for this product.

1. Intake minimum facts (SKILL.md Intake). If `ads-master/` is missing, suggest `ads-setup`.
2. Research sprint light (4 to 6 hours): reviews (own or competitor), Reddit, search queries, ad libraries.
3. Build 2 to 3 personas and the persona by awareness grid.
4. Write 6 to 10 concept cards; select 3 to 6 that are maximally different (persona, angle, format).
5. Produce cheaply: founder or staff phone video, 1 to 2 UGC creators, 2 to 3 statics. One execution per concept, 3 hooks each where video.
6. Name ads per convention. Compliance checklist.
7. Test plan: Starter: in-situ in one broad campaign; Growth: testing lane. Judge on hook and CTR in week 1, CPA over weeks 2 to 4.
8. Week 2 to 4: kill bottom concepts, iterate the top 1 to 2 (hooks), add 2 new concepts.

**Outputs:** VOC bank, concept slate, briefs, test plan, EXPERIMENTS.md rows.
**Success:** at least 1 concept at or under target CPA with directional evidence by week 4 to 6.
**Handoffs:** channel agent (launch structure), `measurement` (tracking check before launch), `cro` (LP message match).

## Play 2. Weekly creative sprint (steady state)

**Trigger:** every week.

| Day | Activity |
|-----|----------|
| Monday | Pull exports (last 7, 30 days). Concept rollup. Fatigue watch. Decide kill, iterate, scale. |
| Tuesday | Next slate: new concepts (share per production mix rule) and iterations; write briefs. |
| Wednesday to Thursday | Production and QA (creative, compliance, naming). |
| Thursday | Change list to human; channel agents launch after approval. |
| Friday | Journal entry: winners, learnings, fatigue alerts. Update EXPERIMENTS.md. |

**Success:** steady launches at the tier cadence; share of spend on creative under 30 days old stays above 20%; hit rate stable or rising.

## Play 3. Scale a winner

**Trigger:** a concept reaches "confident winner" on the evidence ladder.

1. Record the winner: why it works (persona, angle, hook, proof, format), evidence, dates.
2. Graduate to the scaling ad set (existing post ID on Meta, Spark post on TikTok).
3. Iteration ladder rungs 1 to 3 (hooks, first frames, bodies): 5 to 8 variants.
4. Extend: format translation (static, carousel), 2 new creators on the same script, length cuts.
5. Expand: 2 adjacent new concepts (same angle, new persona; or same persona, new angle).
6. Port to other channels (Play 6).
7. Monitor fatigue weekly; plan the successor before the half-life ends.

**Success:** winner concept family (original plus iterations plus adjacent) keeps CPA within target as spend rises.
**Handoffs:** `meta-ads` or `tiktok-ads` (budget scaling is theirs), `growth-orchestrator` (if scaling needs more budget).

## Play 4. Recover from fatigue or a performance drop

**Trigger:** CPA up 20%+ week over week for 2 weeks, or fatigue indicators firing on top spenders.

1. Rule out non-creative causes first: tracking (`measurement`), site or stock changes (`cro`), auction or seasonality (CPM across all ads), budget jumps, policy issues.
2. Fatigue diagnosis per ad (leading indicators table). Identify which concepts carry the decline.
3. Immediate (this week): launch prepared iterations (new hooks) on fatigued winners; propose pausing only clearly fatigued ads after replacements are live.
4. Next 2 weeks: 3 to 6 new concepts focused on uncovered personas and awareness levels.
5. If the decline is broad and not creative: escalate to `growth-orchestrator`.

**Success:** CPA returns within 10% of target within 3 to 4 weeks.

## Play 5. Low diversity rescue (Meta)

**Trigger:** Creative diversity rating Low, or one concept above 60% of spend with new ads starved.

1. Run the diagnostic in the diversity module (section 9).
2. Freeze iterations into the affected ad set for 2 sprints.
3. Produce 6 to 12 new concepts chosen for distance: new personas, new visual worlds, new formats, new talent.
4. Propose removing near-duplicates with weak results (change list).
5. Use the testing lane or Creative Testing tool to force reads.
6. Re-check the rating and spend distribution after 2 and 4 weeks.

**Success:** number of concepts with at least 5% of spend increases; rating improves; blended CPA stable or better.

## Play 6. Port winners to a new channel

**Trigger:** winner on one channel; another channel active or planned.

| From to | Translation |
|---------|-------------|
| Meta to TikTok | Re-shoot or re-edit native: creator to camera, faster cuts, TikTok text styles, sound on, trending or original audio, no polished brand intro; Spark Ads via creator |
| Meta or TikTok to YouTube Shorts | 9:16 kept, add brand early (ABCD), clear CTA; captions |
| Meta or TikTok to YouTube in-stream and Demand Gen | 16:9 and 1:1 versions, brand in first 5 seconds, spoken CTA, end card |
| Any to LinkedIn | Reframe for role and business outcome, add numbers, captions, consider document version and Thought Leader Ads |
| Any to Google RSA and PMax | Winning angle and proof become headline categories; winning statics become image assets |
| Any to ChatGPT ads | Angle becomes a direct answer to an intent cluster; plain factual copy |

**Success:** ported concept within 20% of the channel's target CPA within 4 weeks.
**Handoffs:** the destination channel agent with assets, names and test plan.

## Play 7. Google assets refresh (RSA, PMax, Demand Gen)

**Trigger:** monthly, or asset report shows many low performing assets, or new winning angles on social.

1. Export asset reports (RSA, PMax asset groups, Demand Gen).
2. Replace bottom performers with new headlines from winning social angles and VOC categories (copywriting module section 8).
3. Supply real video in 16:9, 1:1, 9:16 so Google does not rely on auto-generated video; supply 4:5 and 1.91:1 images.
4. Review any AI generated or customized text for claims and brand voice.
5. Hand the asset list to `google-ads`.

## Play 8. B2B LinkedIn creative launch

1. Mine 10+ sales calls and G2 reviews; map pains by buying committee role.
2. Concepts per role: user (ease demo), manager (team outcome case study), executive (cost or risk), technical (security, integration).
3. Formats: founder or expert Thought Leader Ads, document ads with one insight per page, short captioned videos, single image with a specific number.
4. Test on leading indicators (CTR, cost per lead), then judge on SQL and pipeline over 30 to 90 days.
5. Hand off to `linkedin-ads`.

## Play 9. ChatGPT ads copy launch

1. Pull intent clusters from search query mining and `ai-search-optimization` prompt data.
2. For each cluster: one plain answer style message with proof and a specific fit statement.
3. Verify format and policies with `chatgpt-ads`.
4. Test 2 to 3 messages per cluster; judge on conversion quality.

## Play 10. Creator program launch

1. Define the roster gap (personas, ages, settings, styles missing).
2. Source 10 candidates; vet; trial 3 to 5 with a proven script plus a new concept each.
3. Contract with the rights checklist; set up partnership ad permissions or Spark codes.
4. Track by creator token; promote top performers to retainer after 2 videos.

## Play 11. AI production pilot

1. Pick 2 winning concepts with real assets.
2. Use AI for 3 background worlds each, image to video versions, and voiceover localization for one market.
3. QA checklist; flags in ad names.
4. Test AI-assisted executions vs human-shot executions within the same concepts.
5. Decide where AI earns a place in the pipeline; write to memory only with 2+ concept agreement.

## Play 12. Peak season plan (for example Black Friday and Cyber Monday)

| Weeks before peak | Creative action |
|-------------------|-----------------|
| 8 to 6 | Identify evergreen winners; research gift and seasonal angles; book creators |
| 6 to 4 | Produce offer versions of winners (offer cards, offer hooks), gift angle concepts, new statics |
| 4 to 2 | Test new seasonal concepts at modest spend; pre-approve all offer creative |
| 2 to 0 | Launch offer creative on schedule; refresh hooks only; avoid untested concepts in the peak window |
| Peak | Daily fatigue scan on top spenders; prepared iterations ready |
| After | Return to evergreen concepts; retire dated offer creative |

## Play 13. New market localization

1. Check market rules (compliance module), language, cultural fit with a native reviewer.
2. Start with top 3 to 5 winning concepts; localize scripts (not literal translation) and on-screen text.
3. Prefer local creators for UGC; AI dubbing and avatars for explainers only, with disclosure where required.
4. Research the local VOC (local reviews, forums) for 1 to 2 new local concepts.
5. Test like a new account (Play 1) with the localized winners as the first slate.
