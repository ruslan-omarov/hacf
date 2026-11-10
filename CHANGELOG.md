# Changelog

All notable changes to HACF are documented here. Versioning follows the [three-layer model](docs/08-versioning-and-longevity.md): MAJOR = Core, MINOR = Indicators, PATCH = Examples.

## [0.1.0] — 2026-11-10 — Public Draft

### Added
- Core: ten design principles; six levels (L0–L5) with interaction modes and scope of impact; five dimensions (K, A, C, J, R); gate-based level assignment; evidence levels E1–E5 with level caps; flags (RISK-J, RISK-R, UNTAPPED, CEILING, EVIDENCE-CAP, PROVISIONAL).
- Indicators: 0–5 descriptors for each dimension; reference question bank; four practical tasks and portfolio review; enterprise metrics and engagement model.
- Examples: target role profiles; regulatory mapping (EU AI Act Art. 4, Kazakhstan AI Law, ISO/IEC 42001); crosswalk to DigComp 3.0, SFIA and others.
- Tools: reference scoring script (`tools/hacf_score.py`), machine-readable spec, synthetic sample data, unit tests.
- White paper, report templates, governance and contribution rules.

### Known limitations
- Gate thresholds and descriptors are not yet empirically validated.
