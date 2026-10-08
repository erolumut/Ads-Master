# Guardrails

> The safety policy for this project. Humans own this file. The machine readable copy is `guardrails.json` (the hooks enforce it). Keep both in sync. Full model: Ads Master `docs/GUARDRAILS_MODEL.md`.

## Automation stage
Current stage: **1 (Read only)**

| Stage | Name | Agents may |
|-------|------|------------|
| 1 | Read only | Read, analyze, draft files locally |
| 2 | Platform drafts | Also create PAUSED entities, unpublished themes, previews (with confirmation) |
| 3 | Automated reports and QA | Also scheduled daily and weekly runs |
| 4 | Controlled writes | Also execute approved G3 changes in session |
| 5 | Limited automatic actions | Also the auto actions listed below, within caps |

Raise the stage only after the current one has run cleanly for several weeks. Record the change in `DECISIONS.md`.

## Gates
| Gate | Covers | Handling here |
|------|--------|---------------|
| G0 Read | Reports, exports, code, APIs | Automatic |
| G1 Draft | Local files, branches, briefs, renders on disk | Automatic |
| G2 Prepare | PAUSED entities, unpublished theme, previews, creative uploads, draft discounts | Stage 2+, confirmation |
| G3 Commit | Activate, budgets, bids, prices, discounts, shipping, publish, send to customers, live feeds | Human approval every time |
| G4 Forbidden | Delete, billing, ownership, permissions, budgets above the hard cap | Never by an agent |

## Money caps
| Cap | Value | Currency |
|-----|-------|----------|
| Max daily budget per campaign | | |
| Max daily spend per account | | |
| Max budget increase per change (percent) | 0 | |
| Max monthly ceiling (approved, not mandatory) | | |

## Approvers
| Area | Person | How they approve |
|------|--------|------------------|
| Media spend and activation | | |
| Prices, discounts, shipping | | |
| Site publishing | | |
| Claims and legal review | | |
| Customer messaging (email, SMS, push) | | |

## Auto actions (stage 5 only)
None. Example of what could be allowed later: "Pause an ad set when purchase events drop to zero for 6 hours while spend continues."

## Stock guard
Do not increase budgets or launch ads for a product or bundle with less than ____ days of stock cover. Pause or shift creative when the advertised item is sold out.

## Secrets and data
Secrets live in `.env` (git ignored) or a secret manager. `.env.example` holds placeholders only. Agents use aggregated data; no customer names, emails, phones or addresses unless a task requires it and the approver agrees.
