# AI-Native COO Operating System — Single Grain Ops COO 009

Candidate work product for **Beat Claude / Ops COO 009**  
Brief version: **2026-07**

This repo is an inspectable operating artifact for the Single Grain COO/GM challenge. It converts the supplied queue fixture into a concrete operating system: triage, risk policy, decision rights, portfolio rationalization, cadence, evidence, and AI-use disclosure.

## Start here
1. [`FINAL_SUBMISSION.md`](FINAL_SUBMISSION.md) — concise written response
2. [`triage_board.csv`](triage_board.csv) — all 18 queue items ranked, classified, owned, and actioned
3. [`risk_policy.md`](risk_policy.md) — executable green/yellow/red policy
4. [`decision_tree.md`](decision_tree.md) — rendered decision flow
5. [`automation_portfolio.md`](automation_portfolio.md) — KEEP / IMPROVE / MERGE / KILL decisions
6. [`operating_cadence.md`](operating_cadence.md) — daily / weekly / monthly management cadence
7. [`evidence_log.md`](evidence_log.md) — proof tiers and source labels
8. [`ai_usage.md`](ai_usage.md) — AI disclosure and known weak spots

## Core operating thesis
AI should increase action throughput **without increasing executive review load**.

**signal → validation/dedupe → risk tier → owner/action → completion evidence → measured outcome → policy/model update**

Automation earns autonomy through measured reliability and bounded downside. Executive attention is reserved for high-downside decisions, policy-threshold changes, and material cross-functional tradeoffs.

## Fixture integrity
Reference fixture: [`fixture_review_queue_snapshot.csv`](fixture_review_queue_snapshot.csv)  
SHA-256: `2de9268f03c7764bc85d3447336ba211938a3b506933af4ea80844a4a3034c78`

Verify from a fresh checkout of the public challenge with:
```bash
shasum -a 256 challenges/ops-coo-009/fixtures/review_queue_snapshot.csv
```

## Seeded issues explicitly caught
Examples include:
- **Q-08** — auto-send used the wrong company name: automation-control failure, not just copy quality.
- **Q-09** — duplicate of Q-01: duplicate alerts are not independent evidence.
- **Q-13** — marked done with no CRM evidence: status is not completion.
- **Q-14** — recommendations for a churned client: stale entity state invalidates the action.
- **Q-16** — client performance numbers sourced from a screenshot: provenance/confidentiality risk.
- **Q-17** — 9 of 14 prospects duplicate another batch: upstream dedupe failure.
- **Q-18** — two candidates now work at client companies: relationship context must be revalidated before outreach.

## Publication / confidentiality
This repository should contain only public challenge data, synthetic or anonymized artifacts, and candidate-owned material. No confidential employer or customer data belongs here.

`submission_draft.md` is retained as working history; `FINAL_SUBMISSION.md` is the current submission version.
