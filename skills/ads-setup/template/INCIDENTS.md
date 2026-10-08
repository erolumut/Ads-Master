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

## Incident log
| Date | Condition | Impact | Root cause | Fix | Prevention | Owner |
|------|-----------|--------|-----------|-----|-----------|-------|
| | | | | | | |
