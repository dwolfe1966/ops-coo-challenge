# Risk Policy — Ops COO 009

Brief version: **2026-07**

## Objective
Reduce executive review to exceptional decisions while preventing irreversible, high-cost, or externally damaging actions from auto-executing.

## Decision fields
Every automation item must carry:
- `external_action`: none / draft / execute
- `customer_or_candidate_facing`: yes/no
- `legal_or_contractual`: yes/no
- `sensitive_or_client_data`: yes/no
- `financial_exposure`: low / medium / high
- `reversibility`: easy / costly / irreversible
- `confidence`: 0–1
- `source_freshness_days`
- `entity_state_validated`: yes/no
- `owner`
- `evidence_link`
- `dedupe_key`
- `completion_evidence`

## RED — executive / designated senior approver
Any one of:
1. Legal/contractual change.
2. Sensitive/client data leaves the system.
3. High-value client relationship risk.
4. Irreversible or costly external action.
5. Confirmed automation failure with external impact.
6. Financial exposure above an executive-set threshold.

Examples: Q-11, Q-15, Q-08, Q-16.

**Action:** block execution by default. Named operator assembles evidence + recommended action. Executive approves only the decision, not the entire workflow.

## YELLOW — operator review
Any one of:
1. External communication with moderate reputational/commercial risk.
2. Confidence below threshold.
3. Entity/context conflict.
4. Missing or conflicting state/completion evidence.
5. Potential duplicate.
6. Time-sensitive revenue/customer signal requiring judgment.

Examples: Q-01, Q-02, Q-04, Q-13, Q-17, Q-18.

**Action:** operator must approve/edit/reject within SLA.

## GREEN — auto-execute or batch-review
All of:
1. Reversible.
2. Low financial/reputational risk.
3. No legal or sensitive-data implications.
4. Entity state validated.
5. No duplicate detected.
6. Confidence at/above threshold.
7. Owner and audit trail exist.

Examples: internal recommendations, low-risk planning drafts, batched market alerts.

## Auto-approved item that should not have passed
1. **Detect:** monitor complaints, bounced/edited actions, post-send validation, anomaly rules, and random audits.
2. **Contain:** pause the affected automation class, not the whole company.
3. **Recover:** execute customer/recipient correction if needed.
4. **Preserve:** retain input, model output, policy decision, tool/action log and approver state.
5. **Diagnose:** classify as bad data, model error, stale state, policy error, or integration failure.
6. **Patch:** add deterministic guardrail where possible.
7. **Replay:** test the failed case plus adjacent cases before re-enabling.
8. **Escalate policy only if needed:** repeated failures can move an action class from green → yellow/red.

## Working principle
**Automation earns autonomy by measured reliability and bounded downside.** Review burden should fall as evidence improves, not rise as output volume rises.
