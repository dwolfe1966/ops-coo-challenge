# AI Usage Disclosure

Tools used:
- ChatGPT / GPT-5.6 Sol for challenge analysis, drafting, red-teaming, and artifact generation.
- GitHub connector to retrieve the current 2026-07 brief, scoring guidance, and fixture.

AI helped with:
- Parsing the brief and fixture.
- Generating a first-pass queue classification and artifact structure.
- Stress-testing risk-tier rules and failure handling.
- Drafting documentation.

Personally decided / to be personally validated by David Wolfe:
- Final queue priority.
- Which actions are red/yellow/green.
- Which automations to keep, improve, merge, or kill.
- Operating cadence and executive decision boundaries.
- Which personal operating examples and metrics are accurate and supportable.
- Final written submission language.

Checks performed:
- Every fixture `item_id` is represented in `triage_board.csv`.
- Planted-looking issues are explicitly surfaced rather than taken at face value.
- The artifact separates external-action risk from internal recommendations.
- No confidential employer/customer data is included.

Known weak spots:
- Priority order is judgment-based and may change with contract value, customer economics, or missing context.
- Financial thresholds are intentionally not fabricated; the executive should set them from actual economics.
- Historical personal metrics require checkable evidence before claiming high evidence tiers.
