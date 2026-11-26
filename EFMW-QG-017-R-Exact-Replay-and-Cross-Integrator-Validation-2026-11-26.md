# QG-017-R — Exact replay and new-seed cross-integrator test

26 November 2026 · Monolithic LLC · EFMW exploratory computational research

## Scope and status

PASS_BOUNDED: the previously published QG-017 classical, homogeneous Bianchi I Einstein–scalar experiment is reproducible in the same software environment. A new-seed, cross-integrator extension also passes the selected checks. This is not independent scientific replication, a quantum gravity simulation, or evidence that general relativity emerges from EFMW.

The original QG-017 source is pinned at https://github.com/enuminous/Quantum-Gravity/tree/65b9b1a812bf72963bd7d8f3364c40115a040d3d/QG-017 . The original paper is https://github.com/enuminous/papers/blob/63bf061ef767764253343ac1efd7c4f214be0651/EFMW-QG-017-Reciprocal-Einstein-Matter-Dynamics-2026-11-26.md . Neither original was modified.

## Exact replay

Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, `OPENBLAS_NUM_THREADS=1 python run.py`. All eleven original manifest entries verified before replay. The original `run.py`, `results.json`, and `primary_trajectories.npz` Git blob hashes are `c2fa05496e505f7bd762ed6249f611887cbd9832`, `6ec7d6a2bd22e7f33f0640317c0b46920891a6e3`, and `cfdcf9c61a70e99f631092d9420fb2b597d0a446`. The replay results JSON and binary trajectory archive were byte-identical. All 11 original assertions passed: 24 complete cases, 48 ablations, 7272 primary samples, 384 off-shell checks, 24 canonical comparisons, 24 lapse comparisons, eight RK4 refinements, 36 extended stress runs. No extended solver failure in this replay; the original initial failed attempt is retained in QG-017.

## New-seed extension

Holdout.py (filename `holdout.py`) uses seeds 100–111, replacing original seeds 0–3, and otherwise retains the published initial-condition generator, three potentials (massless, quadratic, quartic), two expansion signs, and primary comparison windows. For 72 distinct initial states, solve the complete model with DOP853 and Radau, compare with the canonical formulation, and run both matched coupling-removal controls. Each evolution uses 101 sampled time points. Integrator tolerances: rtol=2e-12, atol=2e-13. Six programmed acceptance checks, declared in the script before execution, require constraint, work, shear, cross-solver, canonical errors below 1e-8, and every ablation's maximum relative constraint residual above 1e-3. The extension is exploratory, not externally preregistered or independent.

| Diagnostic | Result |
|---|---:|
| Complete cases | 72 |
| Ablation cases | 144 |
| Primary sampled states | 21816 |
| Additional Radau sampled states | 7272 |
| DOP853 max relative constraint residual | 1.0522239061056852e-11 |
| Radau max relative constraint residual | 1.0655774554864076e-12 |
| Max scaled pressure-work residual | 3.3237031163097276e-12 |
| Max absolute shear momentum residual | 9.463679839782912e-13 |
| Max scaled cross-solver difference | 4.6579321449643895e-12 |
| Max scaled canonical difference | 1.512578891098665e-11 |
| Matter-to-geometry removal: min/max residual | .011038779343368157 / .9352490275240833 |
| Geometry-to-matter removal: min/max residual | .009161204949321254 / .9999999777856846 |
| Ablations detected | 144/144 |
| Programmed checks | 6/6 |

The full case-level diagnostics are in `holdout_results.json`. The two integrators share the same right-hand-side equations; agreement checks integration error, not independent derivation of the physical laws. Canonical comparison uses the published separate Hamiltonian formulation. Additional seeds vary initial conditions within the original distribution, not the broader model assumptions. No new empirical validation, spatial dynamics or quantum corrections are tested.

## Replay instructions

Copy the original `run.py` from the pinned QG-017 commit into this directory, or use the exact included source. Install the versions in `requirements.txt`. Run `OPENBLAS_NUM_THREADS=1 python run.py` and `OPENBLAS_NUM_THREADS=1 python holdout.py`. The first command generates the original JSON and binary trajectories; the second generates all extension diagnostics. Compare against the pinned original or local archive. The extension does not store all additional trajectories, only case-level diagnostics, but the source regenerates them. The archive manifest covers the packaged originals and new evidence, not an arbitrary future replay's byte serialization.

## Research interpretation

The classical reciprocal feedback and constraint preservation survive this additional within-model challenge. Both directions of coupling are necessary for the tested full-model constraint identity. Independent implementation by an external researcher, new matter models, generic inhomogeneous 3+1 geometry and quantum backreaction remain distinct obligations. The series has already progressed through QG-018 (https://github.com/enuminous/Quantum-Gravity/tree/ec7b038e6233554f251d2e0abddd674dfaaa1095/QG-018). QG-019 is the next new physics investigation.

## Published replay package

All eleven artifacts were checked against the local Git blob hashes: https://github.com/enuminous/Quantum-Gravity/tree/f7c5786091817a8525440b713f6b723cbcb12acc/QG-017-R . The original QG-017 remains unchanged.
