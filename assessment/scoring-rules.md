# Scoring Rules — from instruments to dimension scores

*Layer: Indicators. Version 0.1.0. Reference implementation: [`tools/hacf_assess.py`](../tools/hacf_assess.py).*

These rules make scoring **deterministic**: two assessors with the same raw results must get the same profile. Assessor judgment enters only through rubric scores on practical tasks and artefacts, which are themselves anchored (see [assessor guide](../docs/10-assessor-guide.md)).

## Step 1 — Score each instrument per dimension

| Instrument | Evidence | Dimensions it can score | Rule |
|---|---|---|---|
| Self-assessment §A | E1 | K, A, C, J, R | Mean of the three items per dimension (0–4) → 0–0.5 = **0**; 0.6–1.4 = **1**; 1.5–2.4 = **2**; 2.5–3.2 = **3**; 3.3–4.0 = **4** |
| Scenario check §B | E2 | K, J, R only | Items may count for two dimensions (e.g. B12 → J and R). Share correct per dimension → 0–39 % = **1**; 40–69 % = **2**; ≥ 70 % = **3**. Never above 3. A dimension needs ≥ 3 items to be scored |
| Practical task T1–T4 | E3 | dimensions in the task rubric | Rubric score as given by the assessor (0–5) |
| Artefact / portfolio review | E4 | any | Rubric score (0–5) confirmed by a second assessor or the system owner |
| Sustained outcome | E5 | A (and scope) | Rubric score with ≥ 3 months of documented outcome |

## Step 2 — Combine into the final dimension score

For each dimension, take the score from the **strongest evidence that covers that dimension** (E5 > E4 > E3 > E2 > E1). If two instruments at the same evidence level disagree, take the **lower** score (conservative rule).

The self-assessment counts only for dimensions that no objective instrument covered. Each such dimension is listed as *self-reported* in the report.

## Step 3 — Overall evidence level

The overall evidence level is the **lowest** evidence level among the dimensions that the level's gates require — with one exception: **K evidenced by a scenario check (E2) satisfies any evidence requirement**, because a knowledge check is the appropriate instrument for knowledge. A, C, J and R must be evidenced at the level the gates require (E3 for L3, E4 for L4–L5).

Example: a person whose A, C, J, R come from a practical task (E3) but whose K comes only from self-assessment (E1) has overall evidence E1 — K must be checked by the scenario check before even L2 can be confirmed. If K comes from the scenario check (E2), the overall evidence is E3 and L3 can be reported.

This prevents one strong instrument from "lifting" dimensions it never measured.

## Step 4 — Level and flags

Apply the gates and flags in [docs/03-assessment-method.md](../docs/03-assessment-method.md).

## Worked example

See [docs/examples/worked-example.md](../docs/examples/worked-example.md).
