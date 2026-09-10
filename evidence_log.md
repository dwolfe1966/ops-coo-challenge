# Evidence Log

Brief version: **2026-07**

## Challenge-derived evidence
| Claim | Evidence tier | Source / verification |
|---|---:|---|
| Triage ordering and risk classification use all 18 current fixture rows | Tier 2 | `triage_board.csv` |
| Current fixture SHA-256 | Tier 3 | `2de9268f03c7764bc85d3447336ba211938a3b506933af4ea80844a4a3034c78` computed from local fixture copy; verify against source checkout with `shasum -a 256 challenges/ops-coo-009/fixtures/review_queue_snapshot.csv` |
| Risk policy is operational and inspectable | Tier 2 | `risk_policy.md` |
| Portfolio audit includes keep/improve/merge/kill decisions | Tier 2 | `automation_portfolio.md` |
| Operating cadence is inspectable | Tier 2 | `operating_cadence.md` |

## Personal operating claims to use in written answer
These are **candidate-supplied claims** and should only be labeled at the highest tier for which checkable proof can actually be provided.

| Claim | Number label | Proposed evidence tier | Proof to attach if available |
|---|---|---:|---|
| NewCo/MyLife revenue increased 235% over six months to cash-flow break-even | Observed | Tier 4 if before/after records can be shown safely; otherwise Tier 0 | Sanitized financial/operating record or independent confirmation |
| Propel platform processed >5B impressions/day | Observed | Tier 3–5 only if checkable source exists | Public/company source, architecture record, or independent confirmation |
| ML bidding system improved advertiser ROAS ~37% | Observed | Tier 4–5 only if checkable source exists | Sanitized before/after analysis or independent confirmation |
| Customer retention improved 500% | Observed | Tier 4–5 only if checkable source exists | Sanitized cohort analysis or independent confirmation |

**Rule:** do not label a personal claim Tier 2–5 unless the reviewer has something concrete to inspect.
