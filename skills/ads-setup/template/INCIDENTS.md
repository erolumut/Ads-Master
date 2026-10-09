# Incidents

## Stop conditions
Any agent that detects one of these stops automated writes, alerts the human and follows the runbook.

| Condition | Typical detector |
|-----------|------------------|
| Spend above cap or pacing far above plan | Channel agents, daily report |
| Purchase or lead events stop, double, or fire to the wrong pixel or dataset | measurement |
| Checkout, cart or lead form broken; destination URL returns an error | site-engineer, cro |
| Wrong price, discount or shipping rule live | offer-strategy, site-engineer |
| Advertised product or bundle sold out or below stock cover | commerce-feeds, channel agents |
| Unverified or prohibited claim published | compliance |
| Credential suspected exposed | any agent |

## Runbook
1. Stop automated writes (set `automation_stage` to 1 in `guardrails.json` if needed).
2. Recommend pausing affected paid delivery; the human approves the pause.
3. Preserve evidence: screenshots, exports, `logs/actions.jsonl` lines.
4. Restore the last known good state (previous theme, previous budget or status, previous feed).
5. Explain the cause with evidence.
6. Confirm recovery with fresh data.
7. Add a prevention rule (guardrail, checklist item, alert) and log it in `DECISIONS.md`.

## Risk register (prevention before incidents)
Reviewed in every weekly review; a risk that fires becomes an incident row below. Keep the early warning measurable so the daily report or a script can watch it.

| Risk | Early warning (what we watch, threshold) | Ready response (who does what) | Owner | Last reviewed |
|------|------------------------------------------|--------------------------------|-------|---------------|
| Tracking breaks after a site or tag change | Backend orders vs platform conversions gap moves more than 20 percent day over day; `tracking_plan_check.py` fails | measurement diagnoses; site-engineer rolls back the release; channel agents hold budget changes | measurement | |
| Ad account restricted or ads mass disapproved | Disapproval count above normal; policy emails; delivery drops on all ad sets | compliance reviews the flagged copy; channel agent drafts the appeal; human submits | compliance | |
| Product feed suspended or mass disapproved | Merchant Center item approval rate drops more than 5 points; misrepresentation warning | commerce-feeds fixes the feed and price parity; site-engineer checks structured data | commerce-feeds | |
| Learning reset or volatility after a big change | Several edits on the same campaign within 7 days; budget change above the cap in GUARDRAILS.md | channel agent batches changes; growth-orchestrator approves one change window per week | growth-orchestrator | |
| Price or offer shown differently across channels | Price parity sample (ad, page, JSON-LD, feed, checkout) mismatch | pricing-strategy and offer-strategy correct the source; compliance checks the displayed price | pricing-strategy | |
| Advertised item goes out of stock | Stock cover of advertised items below 14 days | commerce-feeds excludes the item; channel agents shift budget; lifecycle-crm pauses flows that feature it | commerce-feeds | |
| Approved claim loses its evidence | Evidence expiry in CLAIMS.md within 30 days; `approved_copy.py verify` fails | compliance re-verifies or retires the claim; channel agents swap the copy | compliance | |
| Spend runs away on a new campaign or automation | Hourly pacing above 150 percent of plan; guard log shows repeated G3 asks | channel agent recommends a pause; human approves; automation stage drops to 1 | growth-orchestrator | |

## Incident log
| Date | Condition | Impact | Root cause | Fix | Prevention | Owner |
|------|-----------|--------|-----------|-----|-----------|-------|
| | | | | | | |
