#!/usr/bin/env python3
"""HACF assessment tool: raw instrument results -> dimension scores -> CSV for hacf_score.py.

Implements assessment/scoring-rules.md deterministically.

Usage:
    python hacf_assess.py sample/raw_results.json --out people.csv
    python hacf_score.py people.csv --roles sample/role_profiles.json --out report.md

Input: a JSON list of participants, each with any of
    "self":      {"A1": 0-4, ..., "A15": 0-4}
    "scenario":  {"B1": "a".."d", ...}
    "tasks":     [{"name": "T1", "evidence": "E3", "scores": {"A": 3, "J": 2, "R": 3}}]
    "artefacts": [{"name": "...", "evidence": "E4" or "E5", "scores": {...}}]
plus "id", "department", "role", "scope".

Standard library only. License: MIT (see LICENSE-CODE).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIMS = ["K", "A", "C", "J", "R"]
EV_RANK = {"E1": 1, "E2": 2, "E3": 3, "E4": 4, "E5": 5}
SELF_ITEMS = {"K": ["A1", "A2", "A3"], "A": ["A4", "A5", "A6"], "C": ["A7", "A8", "A9"],
              "J": ["A10", "A11", "A12"], "R": ["A13", "A14", "A15"]}
MIN_SCENARIO_ITEMS = 3


def self_score(mean: float) -> int:
    if mean <= 0.5:
        return 0
    if mean < 1.5:
        return 1
    if mean < 2.5:
        return 2
    if mean < 3.3:
        return 3
    return 4


def scenario_scores(answers: dict, key: dict) -> dict:
    tally = {d: [0, 0] for d in DIMS}
    for item, spec in key.items():
        if item.startswith("_") or item not in answers:
            continue
        ok = str(answers[item]).strip().lower() == spec["answer"]
        for d in spec["dims"]:
            tally[d][0] += ok
            tally[d][1] += 1
    out = {}
    for d, (right, total) in tally.items():
        if total >= MIN_SCENARIO_ITEMS:
            share = right / total
            out[d] = 1 if share < 0.4 else 2 if share < 0.7 else 3
    return out


def combine(person: dict, key: dict) -> tuple[dict, dict]:
    """Return (scores, evidence_per_dim). Strongest evidence wins; ties -> lower score."""
    candidates = {d: [] for d in DIMS}  # (rank, score)
    if person.get("self"):
        s = person["self"]
        for d, items in SELF_ITEMS.items():
            vals = [s[i] for i in items if i in s]
            if vals:
                candidates[d].append((1, self_score(sum(vals) / len(vals))))
    if person.get("scenario"):
        for d, v in scenario_scores(person["scenario"], key).items():
            candidates[d].append((2, v))
    for block in person.get("tasks", []) + person.get("artefacts", []):
        rank = EV_RANK[block["evidence"]]
        for d, v in block["scores"].items():
            if d not in DIMS or not 0 <= int(v) <= 5:
                sys.exit(f"{person.get('id')}: invalid score {d}={v}")
            candidates[d].append((rank, int(v)))
    scores, ev = {}, {}
    for d in DIMS:
        if not candidates[d]:
            scores[d], ev[d] = 0, 1
            continue
        top = max(r for r, _ in candidates[d])
        scores[d] = min(v for r, v in candidates[d] if r == top)
        ev[d] = top
    return scores, ev


def effective(dim: str, rank: int) -> int:
    """Knowledge is what a scenario check (E2) measures, so E2 fully evidences K."""
    return 5 if dim == "K" and rank >= 2 else rank


def overall_evidence(scores: dict, ev: dict, spec: dict, scope: str) -> str:
    caps = {int(k[1]): v["max_level"] for k, v in spec["evidence_levels"].items()}
    scopes = spec["scopes"]
    for lvl in sorted(spec["levels"], key=lambda l: -l["level"]):
        gates = lvl["gates"]
        if not all(scores[d] >= v for d, v in gates.items()):
            continue
        if scopes.index(scope) < scopes.index(lvl["min_scope"]):
            continue
        e = min((effective(d, ev[d]) for d in gates), default=max(ev.values()))
        if caps[e] >= lvl["level"]:
            return f"E{e}"
    return f"E{min(ev.values())}"


def main(argv=None):
    p = argparse.ArgumentParser(description="HACF: raw results -> dimension scores")
    p.add_argument("raw", type=Path)
    p.add_argument("--key", type=Path, default=ROOT / "assessment" / "scenario-key.json")
    p.add_argument("--spec", type=Path, default=ROOT / "assessment" / "hacf-spec.json")
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args(argv)
    key = json.loads(a.key.read_text(encoding="utf-8"))
    spec = json.loads(a.spec.read_text(encoding="utf-8"))
    people = json.loads(a.raw.read_text(encoding="utf-8"))
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "department", "role", *DIMS, "evidence", "scope", "self_reported"])
        for person in people:
            scope = person.get("scope", "Self")
            scores, ev = combine(person, key)
            e = overall_evidence(scores, ev, spec, scope)
            self_rep = " ".join(d for d in DIMS if ev[d] == 1)
            w.writerow([person["id"], person.get("department", "-"), person.get("role", ""),
                        *[scores[d] for d in DIMS], e, scope, self_rep])
    print(f"Wrote {len(people)} participants to {a.out}")


if __name__ == "__main__":
    main()
