# HACF Tools

Reference implementation of the [assessment method](../docs/03-assessment-method.md). Python 3.11+ (tested in CI on 3.11 and 3.13), standard library only. License: MIT.

Two scripts:

- `hacf_assess.py` — raw instrument results (self-assessment, scenario answers, task and artefact rubric scores) → dimension scores and evidence level, following [scoring-rules.md](../assessment/scoring-rules.md).
- `hacf_score.py` — dimension scores → levels, flags, gaps and the enterprise report.

## Quick start

```bash
cd tools
python hacf_assess.py sample/raw_results.json --out people_from_raw.csv
python hacf_score.py people_from_raw.csv --roles sample/role_profiles.json --results results.csv

# or score an existing table of dimension scores
python hacf_score.py sample/people.csv \
  --roles sample/role_profiles.json \
  --out report.md --results results.csv
```

- `report.md` — enterprise report: HACF Index, level distribution, department heat map (groups < 5 suppressed), gaps vs. role targets, rule-based recommendations. See [sample/report.md](sample/report.md).
- `results.csv` — per-person level, profile, flags, gaps to next level and to role target.

Without `--out`/`--results`, results are printed to the console.

## Input format

| Column | Required | Values |
|---|---|---|
| id | yes | any identifier (use pseudonyms) |
| department | yes | free text |
| role | no | must match a key in the role profiles JSON to compute coverage |
| K, A, C, J, R | yes | integers 0–5 |
| evidence | yes | E1–E5 |
| scope | no (default Self) | Self, Team, Organisation, Ecosystem |

The sample data in `sample/people.csv` is **synthetic**.

## Tests

```bash
python -m unittest discover tests
```
(from the repository root)
