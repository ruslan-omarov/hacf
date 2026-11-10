# Worked Example — from raw answers to a development plan

*Layer: Examples. Data is fictional and included in `tools/sample/raw_results.json`.*

## Participant A-017 · Financial analyst

**Instruments:** self-assessment (E1), scenario check (E2), practical tasks T1 and T2 (E3).

### Step 1 — instrument scores

| Dim | Self (E1) | Scenario (E2) | T1 (E3) | T2 (E3) |
|---|---|---|---|---|
| K | mean 2.7 → 3 | 4/4 correct → 3 | – | – |
| A | 3.3 → 4 | – | 3 | 3 |
| C | 1.7 → 2 | – | – | 2 |
| J | 2.3 → 2 | 6/7 correct → 3 | 3 | 3 |
| R | 3.0 → 3 | 5/6 correct → 3 | 3 | 3 |

### Step 2 — final scores (strongest evidence wins; ties → lower)

K3 (E2) · A3 (E3) · C2 (E3) · J3 (E3) · R3 (E3). Note that her self-rating of A4 is not used: the practical tasks show A3.

### Step 3 — evidence and level

K is evidenced by the scenario check, which suffices for K; A, C, J, R are at E3. Overall evidence **E3**, so up to L3 can be reported. Gates for L3 (K2 A3 C2 J3 R3) are all met.

```
HACF L3 [K3 · A3 · C2 · J3 · R3]  evidence: E3  scope: Self
```

**Flags:** `CEILING` toward L4 (only C is below the L4 gate, by 2 points; scope also needs to reach Team).
**Role target (Analyst):** met.

### Development plan

1. **C → 3:** turn her monthly variance workflow into a shared assistant used by two colleagues; document tests. (8 weeks)
2. **Scope → Team:** present the workflow at the finance team meeting; measure colleagues' time saved.
3. Re-assess with artefact review (E4) in 6 months; candidate for the Builder track.

## Participant S-104 · Sales

Self-assessment suggests a confident user (A 4, J 3, R 3). The practical task tells a different story: strong output (A4) but the planted currency mix-up passed unnoticed (J1) and the customer phone list was pasted into an unapproved tool (R1). The scenario check confirms the gap: K1 (1 of 4 correct), J1 (1 of 7) and R1 (1 of 6).

```
HACF L1 [K1 · A4 · C2 · J1 · R1]  evidence: E3  scope: Self   flags: RISK-J RISK-R
```

C2 comes only from self-assessment and is marked *self-reported*.

**Interpretation:** a productive but risky user — exactly the profile that averages hide. **Action:** verification and data-handling training before the next tool rollout; re-check J and R with a new practical task in 6–8 weeks.

## Participant X-001 · Executive

Scenario check perfect (K, J, R at 3); leadership case T4 (E3); portfolio decision record reviewed with the CFO (E4): K3 A3 C2 J4 R4, scope Organisation.

```
HACF L5 [K3 · A3 · C2 · J4 · R4]  evidence: E4  scope: Organisation
```

Meets the Executive role profile.
