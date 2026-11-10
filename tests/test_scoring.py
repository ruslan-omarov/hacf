"""Tests for the HACF reference scorer. Run: python -m unittest discover tests"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from hacf_score import Scorer  # noqa: E402
import hacf_assess  # noqa: E402

SPEC = json.loads((ROOT / "assessment" / "hacf-spec.json").read_text(encoding="utf-8"))


def run(K, A, C, J, R, ev="E4", scope="Self"):
    return Scorer(SPEC).score("x", "d", "", dict(K=K, A=A, C=C, J=J, R=R), ev, scope)


class TestLevels(unittest.TestCase):
    def test_l0(self):
        self.assertEqual(run(0, 0, 0, 0, 0).level, 0)

    def test_l1(self):
        self.assertEqual(run(1, 0, 0, 1, 1).level, 1)

    def test_l2(self):
        self.assertEqual(run(2, 2, 0, 2, 2).level, 2)

    def test_l3(self):
        self.assertEqual(run(2, 3, 2, 3, 3, "E3").level, 3)

    def test_l4_requires_team_scope(self):
        self.assertEqual(run(3, 3, 4, 3, 3, "E4", "Self").level, 3)
        self.assertEqual(run(3, 3, 4, 3, 3, "E4", "Team").level, 4)

    def test_l5(self):
        self.assertEqual(run(3, 3, 3, 4, 4, "E4", "Organisation").level, 5)

    def test_l5_does_not_require_builder_depth(self):
        self.assertEqual(run(3, 3, 2, 4, 4, "E4", "Organisation").level, 5)


class TestGatesNotAverages(unittest.TestCase):
    def test_power_user_at_risk(self):
        r = run(2, 5, 4, 1, 1, "E4", "Team")
        self.assertEqual(r.level, 1)
        self.assertIn("RISK-J", r.flags)
        self.assertIn("RISK-R", r.flags)


class TestEvidence(unittest.TestCase):
    def test_self_report_capped_at_l2(self):
        r = run(4, 4, 4, 4, 4, "E1", "Organisation")
        self.assertEqual(r.level, 2)
        self.assertIn("PROVISIONAL", r.flags)
        self.assertIn("EVIDENCE-CAP", r.flags)

    def test_practical_task_capped_at_l3(self):
        self.assertEqual(run(4, 4, 4, 4, 4, "E3", "Organisation").level, 3)


class TestFlags(unittest.TestCase):
    def test_untapped(self):
        self.assertIn("UNTAPPED", run(3, 1, 0, 2, 2).flags)

    def test_ceiling(self):
        r = run(2, 3, 1, 3, 3, "E3")
        self.assertEqual(r.level, 2)
        self.assertIn("CEILING", r.flags)
        self.assertEqual(r.next_gaps, {"C": 1})


class TestRoleProfilesConsistent(unittest.TestCase):
    """Every example role profile must produce its stated target level."""

    def test_profiles_match_gates(self):
        roles = json.loads((ROOT / "tools" / "sample" / "role_profiles.json").read_text(encoding="utf-8"))
        for name, p in roles.items():
            if name.startswith("_"):
                continue
            scores = {d: p.get(d, 0) for d in "KACJR"}
            level = Scorer(SPEC).score("x", "d", name, scores, "E4", p["scope"]).level
            self.assertEqual(level, p["target_level"], name)


class TestAssess(unittest.TestCase):
    KEY = json.loads((ROOT / "assessment" / "scenario-key.json").read_text(encoding="utf-8"))

    def test_self_mapping(self):
        self.assertEqual([hacf_assess.self_score(x) for x in (0.4, 1.0, 2.0, 3.0, 3.5)], [0, 1, 2, 3, 4])

    def test_strongest_evidence_wins_and_ties_take_lower(self):
        person = {"self": {"A4": 4, "A5": 4, "A6": 4},
                  "tasks": [{"evidence": "E3", "scores": {"A": 3}},
                            {"evidence": "E3", "scores": {"A": 2}}]}
        scores, ev = hacf_assess.combine(person, self.KEY)
        self.assertEqual((scores["A"], ev["A"]), (2, 3))

    def test_scenario_never_above_3(self):
        answers = {k: v["answer"] for k, v in self.KEY.items() if not k.startswith("_")}
        out = hacf_assess.scenario_scores(answers, self.KEY)
        self.assertEqual(out, {"K": 3, "J": 3, "R": 3})

    def test_sample_end_to_end(self):
        people = json.loads((ROOT / "tools" / "sample" / "raw_results.json").read_text(encoding="utf-8"))
        expected = {"A-017": 3, "S-104": 1, "X-001": 5}
        for p in people:
            scores, ev = hacf_assess.combine(p, self.KEY)
            e = hacf_assess.overall_evidence(scores, ev, SPEC, p["scope"])
            level = Scorer(SPEC).score(p["id"], "", "", scores, e, p["scope"]).level
            self.assertEqual(level, expected[p["id"]], p["id"])


if __name__ == "__main__":
    unittest.main()
