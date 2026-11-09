# Phase 1 — Prior CI and replay receipts

These are **repository-hosted prior CI runs**, observed by GitHub API at the exact frozen commit, not newly executed local verification by UNITY-001.

| Repo | Head-matched historical run | CI outcome | What it establishes / does not |
|---|---|---|---|
| Geometry | [Lean Geometry Audit, run 41696922044](https://github.com/enuminous/Geometry/actions/runs/41696922044) | GitHub reported completed SUCCESS | Repo's Lean build and specific theorem/witness audit, not GR covariance or physical κ detection |
| Information-Tensor | [Reproducibility checks, run 42056702958](https://github.com/enuminous/Information-Tensor/actions/runs/42056702958) | GitHub reported completed SUCCESS | JS/Node tests and explicit retained negative physical-model gates, not a physical experiment |
| EFMW-Lagrangian | [Verify candidate and Lean certificates, run 40945020199](https://github.com/enuminous/EFMW-Lagrangian/actions/runs/40945020199) · [continuum run 40945020112](https://github.com/enuminous/EFMW-Lagrangian/actions/runs/40945020112) | GitHub reported completed SUCCESS | Bounded polynomial/candidate formal checks, not literal equivalence of 585 equations or physical truth |
| Standard-Model-Reduction | [Publish dashboard, run 40601622971](https://github.com/enuminous/Standard-Model-Reduction/actions/runs/40601622971) | GitHub reported completed SUCCESS | **Deployment only**: workflow does not run `verify_standard_model_reduction.py` |

## Locked environment and reproduction commands

| Source | Version / dependency | Command or protocol | New replay |
|---|---|---|---|
| Geometry | Lean v4.28.0; Mathlib4 `8f9d9cff6bd728b17a24e163c9402775d9e6a365` from `lakefile.toml` | `bash check.sh` (`lake update`, `lake build Geometry`, `lake env lean Axioms.lean`, witness executable, `python3 sanity.py`) | NOT RUN HERE |
| Information-Tensor | Node ≥20, CI Node 24 / Python 3.12; no published Lean toolchain | `npm test`, `npm run verify`, `node research/witd-002/replay.cjs` | NOT RUN HERE |
| EFMW-Lagrangian | Lean v4.28.0; top-level no Mathlib; continuum Mathlib4 `8f9d9cff6bd728b17a24e163c9402775d9e6a365` | `python3 scripts/verify.py --clean` and continuum workflow | NOT RUN HERE |
| Standard-Model-Reduction | Python ≥3.10 and SymPy (exact version unpinned in this repo) | `python3 verify_standard_model_reduction.py` | NOT RUN HERE |

**Execution environment observation:** the authoring environment in this session has Python 3.13.5 and Node v22; `lean` / `lake` were absent, and direct network Git clones were unavailable due to DNS resolution. No failed clone is mislabeled a source-content error. Fresh Lean reproduction is **UNRESOLVED**.

## Historical, not new verification

- Geometry's `PROOF_RECEIPT.md` says Lean was unverified *at authoring*; later head-matched successful Actions runs exist. Keep both dates and methods separate.
- EFMW-Lagrangian's committed `verification/build_status.json` records a 2026-10-14 explicit-path launcher run. Its status must not be conflated with the Oct 29 GitHub-hosted standard-launcher CI result.
- Information-Tensor WITD-002 explicitly retains **11 numerical PASS and two numerical FAIL gate groups**. A successful CI workflow checks that those reported failures are faithfully reproduced; it does not turn them into successful physics.
- Standard-Model-Reduction stores 16 symbolic-check outputs, but head-matched Actions only publishes its website; an independent fresh SymPy run remains to do.

**Scientific conclusion:** source provenance and head-matched CI observed; independent fresh rebuild and physical validation are **not established**.
