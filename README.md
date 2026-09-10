# AI-Native COO Operating System — Single Grain Ops COO 009

Candidate work product for **Beat Claude / Ops COO 009**  
Brief version: **2026-07**

This repo is an inspectable operating artifact, not a generic strategy memo. It turns the challenge fixture into:
1. a ranked 48-hour triage board,
2. an executable green/yellow/red risk policy,
3. an automation portfolio audit with explicit merges/kills,
4. a low-bureaucracy operating cadence,
5. evidence and AI-usage disclosures.

## Start here
- [`triage_board.csv`](triage_board.csv)
- [`risk_policy.md`](risk_policy.md)
- [`automation_portfolio.md`](automation_portfolio.md)
- [`operating_cadence.md`](operating_cadence.md)
- [`evidence_log.md`](evidence_log.md)
- [`ai_usage.md`](ai_usage.md)
- [`submission_draft.md`](submission_draft.md)

## Fixture
Local reference copy: `fixture_review_queue_snapshot.csv`  
SHA-256: `2de9268f03c7764bc85d3447336ba211938a3b506933af4ea80844a4a3034c78`

Verify from a fresh checkout of the public challenge with:
```bash
shasum -a 256 challenges/ops-coo-009/fixtures/review_queue_snapshot.csv
```

## Core operating thesis
AI should increase action throughput without increasing executive review load.

**signal → validation/dedupe → risk tier → owner/action → completion evidence → measured outcome → policy/model update**

The executive only handles high-downside decisions and changes to policy thresholds.

## Three fixture observations I would not act on at face value
- **Q-09** duplicates Q-01; two alerts do not mean two customer-risk events.
- **Q-13** says `done`, but there is no CRM evidence of an email/call; status is not completion evidence.
- **Q-14** recommends work for a churned client; automation output is invalid if customer state is stale.

Additional planted-risk signals include Q-08, Q-16, Q-17, and Q-18.

## Publication note
This repo contains only public challenge data, synthetic/anonymized artifacts, and candidate-owned material. Do not commit confidential data from prior employers or clients.
