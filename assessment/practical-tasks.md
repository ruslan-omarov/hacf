# Practical Tasks and Portfolio Review

*Layer: Indicators. Version 0.1.0.*

Practical tasks produce **E3** evidence; portfolio review produces **E4**. Participants may use any AI tool approved by their organisation. Scoring ignores which tool was used (Principle P2).

## General rules

- Participants receive realistic materials with **planted defects** (errors, missing data, a sensitive data element, an embedded malicious instruction). Detecting them is part of the score.
- Participants submit the result **and** a short log: what they asked AI, what they checked, what they changed.
- Assessors score with the rubric below; two assessors or calibrated single assessors (see [assessment method §7](../docs/03-assessment-method.md)).

## Task T1 — Analysis & recommendation (for L2→L3) · 60 min

**Ready-made pack:** `python tools/make_task_t1.py --seed <any number> --out t1_pack` generates a unique dataset, market note, participant brief and a confidential assessor key. Use a new seed for every round so answers never leak. The pack contains six planted defects (duplicates, currency mix-up, impossible date, personal data, outdated figure, injected instruction); in every variant, missing them changes which region looks strongest.

**Material:** a sales dataset (≈500 rows) with three planted errors (duplicates, a currency mix-up, an impossible date); a one-page market note containing one outdated figure; customer names and phone numbers in one column.

**Assignment:** Using AI, produce a one-page recommendation to management on where to focus next quarter, with numbers.

| Dim | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| A | Partial output | Correct basic analysis | Clear, actionable recommendation backed by correct figures | Adds a reusable workflow others could run monthly |
| J | Errors propagated | Finds 1–2 planted errors | Finds all data errors and the outdated figure; states uncertainty | Proposes checks preventing these errors in future |
| R | Pastes personal data into unapproved tool | Uses approved tool | Removes/minimises personal data before processing | Documents data handling decision |

## Task T2 — Workflow design (for L3) · 90 min

**Assignment:** Pick a recurring task from your role. Design and run an AI-assisted workflow on two real or realistic instances. Measure time vs. your usual method. Write the instructions so a colleague can repeat it.

Scored on A (outcome), C (reusability: C2 if repeatable by self, C3 if usable by a colleague), J (built-in checks), R (data handling).

## Task T3 — Build (for L3→L4) · 1 day or take-home

**Assignment:** Build a small solution that other people would use: e.g. an assistant answering questions from a provided policy set, or an automation that processes incoming requests and drafts responses for human approval.

**Required:** description of users and purpose; test set of ≥ 15 cases including edge and adversarial cases (one contains an injection attempt); results table; permissions used; human control points; known limitations.

| Dim | 3 | 4 | 5 |
|---|---|---|---|
| C | Works for the happy path; basic documentation | Integrated, tested on edge cases, least-privilege, monitoring/logging, human control points | Reusable architecture, could serve multiple teams |
| J | Basic test set | Systematic evaluation with acceptance criteria; injection handled | Evaluation approach reusable by others |
| R | No obvious violations | Access control, data minimisation, logging, disclosure to users | Risk classification and documentation ready for audit |

## Task T4 — Leadership case (for L5) · 2 hours + interview

**Material:** a business case for an AI programme (budget, three use cases, vendor proposal with optimistic claims, one use case touching high-risk decisions about people).

**Assignment:** Decide what to fund, stop or redesign; define success metrics, governance, accountability, people-capability needs (using HACF target profiles), and an exit criterion.

Scored on J (challenges claims, sets acceptable error and oversight), R (governance, legal risk, accountability), A/scope (link to strategy, measurable value), K (sound technical reasoning).

## Portfolio review (E4)

<a id="portfolio-review-e4"></a>
The candidate submits 1–3 real artefacts from the last 12 months:

- a workflow or solution in actual use, with evidence of use (users, runs, outcomes);
- a decision record where AI informed or was deliberately not used;
- for L5: a strategy, policy, portfolio decision or capability programme they led.

Interview (30–45 min) probes: *What failed? How did you know? What would break it? Who is accountable? What did you decide not to automate?*

An artefact must be verifiable by the manager or system owner. Unverifiable claims count as E1.
