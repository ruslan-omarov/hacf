# 05 · Target Role Profiles

*Layer: Examples (non-normative starting points). Each organisation should adapt targets to its strategy, risk appetite and the autonomy of the AI systems in use.*

A target profile states the **minimum** dimension scores a role needs. It is a business decision, reviewed yearly.

Machine-readable version: [`tools/sample/role_profiles.json`](../tools/sample/role_profiles.json).

| Role family | Target level | K | A | C | J | R | Rationale |
|---|---|---|---|---|---|---|---|
| All employees (baseline) | L1 | 1 | – | – | 1 | 1 | Safe awareness for everyone exposed to AI features |
| Knowledge worker (general) | L2 | 2 | 2 | – | 2 | 2 | Daily productivity with verification |
| Customer-facing staff | L2 | 2 | 2 | – | 3 | 3 | Errors reach clients; confidentiality critical |
| Analyst / specialist | L3 | 2 | 3 | 2 | 3 | 3 | Complex work, repeatable workflows |
| Legal, compliance, audit | L3 | 3 | 3 | 1 | 4 | 4 | Verification and accountability dominate |
| HR professional | L3 | 2 | 3 | 2 | 3 | 4 | Personal data, fairness in people decisions |
| People manager | L2→L3 | 2 | 3 | 1 | 3 | 3 | Redesigns team work, oversees AI use |
| Software engineer | L3→L4 | 3 | 3 | 4 | 3 | 3 | Builds AI-enabled software |
| Automation / AI builder | L4 | 3 | 3 | 4 | 3 | 3 | Creates solutions others depend on |
| Operator of high-risk / autonomous AI | L3 | 3 | 3 | 1 | 4 | 4 | Human oversight is the core duty |
| IT / security lead | L4 | 4 | 3 | 3 | 4 | 4 | Platform, access, threats |
| Executive (C-level) | L5 | 3 | 3 | 1 | 4 | 4 | Strategy, governance (see note) |
| Chief AI / Digital Officer | L5 | 4 | 3 | 3 | 4 | 4 | Accountable for AI portfolio |

**Note on executives.** The L5 *gate* requires C≥3, but some executive roles only need to judge solutions, not build them. Organisations may therefore set an executive target as a profile (K3 A3 C1 J4 R4) without requiring the formal L5 level. Coverage is measured against the profile.

## Proportionality modifiers

Raise J and R targets by one point (max 5) when the role:

- works with AI systems classified as **high-risk** under applicable law;
- supervises AI that acts **autonomously** (sends, pays, decides, changes records);
- handles **special categories** of personal data, minors' data, or state secrets;
- produces **synthetic content** published under the organisation's name.
