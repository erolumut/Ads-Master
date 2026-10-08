# Logs

- `actions.jsonl`: one line per write attempt seen by the Ads Master hooks (time, tool, gate, decision, short summary). Never contains secrets.
- `session-reports/YYYY-MM-DD_HHMM.md`: what a substantial session requested, changed, which approvals it used and what remains open.

Keep logs in git if your team wants an audit trail; they hold no customer data.
