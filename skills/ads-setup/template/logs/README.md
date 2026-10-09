# Logs

- `actions.jsonl`: one line per write attempt seen by the Ads Master hooks (time, tool, gate, decision, short summary). Never contains secrets.
- `session-reports/YYYY-MM-DD_HHMM.md`: what a substantial session requested, changed, which approvals it used and what remains open.
- `alerts.csv`: the open alert queue from the daily report, one row per rule and entity (`rule,entity,alert_from,last_seen,status,ack_by,note`). Conditions that persist update `last_seen`; they never add a second row.

Keep logs in git if your team wants an audit trail; they hold no customer data.
