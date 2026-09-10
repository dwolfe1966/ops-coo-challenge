from pathlib import Path
import csv

root = Path(__file__).resolve().parent
required = [
    'README.md',
    'triage_board.csv',
    'risk_policy.md',
    'automation_portfolio.md',
    'operating_cadence.md',
    'evidence_log.md',
    'ai_usage.md',
    'submission_draft.md',
]
missing = [x for x in required if not (root / x).exists()]
if missing:
    raise SystemExit('Missing: ' + ', '.join(missing))

rows = list(csv.DictReader(open(root / 'triage_board.csv')))
ids = [r['item_id'] for r in rows]
expected = {f'Q-{i:02d}' for i in range(1, 19)}
assert set(ids) == expected, set(ids) ^ expected
assert len(ids) == len(set(ids)) == 18
print('PASS: required files present; all 18 fixture ids classified exactly once.')
