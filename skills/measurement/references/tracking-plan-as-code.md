# Tracking Plan as Code

> A tracking plan in a spreadsheet drifts the day after launch. A tracking plan in the repo, checked by a script, does not. This module turns the event spec into a machine readable allowlist that code, tag manager and server senders are checked against.

Pattern origin: privacy first analytics layers built in practice (allowlisted event catalog with a pure ingest gate) plus two way docs and code parity checks. Generalized here for GA4, server-side tagging and platform conversion APIs. [Practitioner consensus]

## 1. Why

| Problem without it | What the allowlist fixes |
|--------------------|--------------------------|
| Events renamed in code, conversions silently stop | Undeclared event names fail the check before release |
| PII leaks into GA4 or CAPI parameters (email in a URL, name in a custom dimension) | Only declared, typed properties pass; free text is banned by default |
| Catalog lists events nothing emits | Two way check: orphan catalog rows fail too |
| Every agent defines "purchase" differently | One file, referenced by `METRICS.md` and `MEASUREMENT.md` |

## 2. The file

Store it at `ads-master/tracking-plan.json` (project state) or in the codebase next to the analytics module. Shape:

```json
{
  "version": 3,
  "pii_policy": "no raw email, phone, name, address or free text in any parameter; user ids are hashed",
  "events": {
    "purchase": {
      "owner": "measurement",
      "destinations": ["ga4", "meta_capi", "google_ec"],
      "conversion": true,
      "dedup_key": "transaction_id",
      "props": {
        "transaction_id": {"type": "id"},
        "value": {"type": "num", "min": 0, "max": 100000},
        "currency": {"type": "enum", "values": ["EUR", "USD", "TRY", "GBP"]},
        "new_customer": {"type": "bool"},
        "items_count": {"type": "num", "min": 1, "max": 500}
      }
    },
    "generate_lead": {
      "owner": "measurement",
      "destinations": ["ga4", "meta_capi", "linkedin_capi"],
      "conversion": true,
      "dedup_key": "lead_id",
      "props": {
        "lead_id": {"type": "id"},
        "form": {"type": "enum", "values": ["contact", "demo", "quote"]}
      }
    }
  }
}
```

Property types: `id` (opaque, no spaces, max 64 chars), `num` (with `min` and `max`), `bool`, `enum` (closed list), `route` (a path pattern like `/products/[handle]`, never a raw URL with a query string). There is deliberately no free `string` type. Add one only with a written reason in `DECISIONS.md`.

## 3. Rules the plan enforces

1. Anything not declared is dropped at ingest (first-party collection) or fails the check (third party tags). Declare first, ship second.
2. URLs are folded to route patterns before they leave the site. Query strings carry PII more often than any other field.
3. User identifiers are hashed (SHA-256, normalized per the platform's spec) before any CAPI call, and never stored raw in analytics.
4. Internal, demo, QA and bot traffic is flagged at ingest and excluded from reported numbers, not deleted.
5. Every conversion event names a `dedup_key` shared by the browser and server sends.
6. The server clock is the source of truth for event time; client time is kept only to correct skew.
7. Changing an event name or a conversion definition needs a `DECISIONS.md` entry and a note to every channel agent whose bidding uses it (learning resets).

## 4. The checks

`scripts/tracking_plan_check.py` (in this skill) runs two checks with the stdlib only:

| Mode | What it does | Exit |
|------|--------------|------|
| `--plan tracking-plan.json --payloads sample.jsonl` | Validates captured payloads (one JSON event per line, from a debug export, sGTM preview or a test run) against the plan: unknown events, undeclared props, type and range errors, PII patterns (email, phone, raw URLs with query) | 0 pass, 1 fail, 2 could not run |
| `--plan tracking-plan.json --code src/` | Greps the codebase for emitted event names (`gtag('event', 'x'`, `dataLayer.push({event: 'x'`, `track('x'`, `fbq('track', 'x'`, `ttq.track('x'`) and compares both ways: emitted but undeclared, declared but never emitted | 0, 1, 2 |

The code scan is a grep, so it reports what it cannot cover (dynamic event names, tag manager only events). Treat those as manual review items, never as passes.

Run it: before every release that touches tracking (site-engineer launch QA), in the monthly measurement health audit, and after a tag manager publish (with a fresh payload sample).

## 5. Rollout

1. Draft the plan from the current GA4 events report and platform event managers (read only, G0).
2. Run the code scan; reconcile the differences with the developer.
3. Capture a payload sample on staging; fix failures.
4. Add the check to the release checklist (site-engineer) and, if the project uses git hooks or CI, as a validate-only step.
5. Start in warn mode for two weeks, then make failures blocking.

## 6. Hand offs

| Situation | To |
|-----------|----|
| Check fails on a release branch | site-engineer (block release until fixed) |
| A conversion definition changes | every active channel agent, growth-orchestrator |
| PII found in a live payload | compliance, and log in `INCIDENTS.md` |
