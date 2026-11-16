# Physlib Maxwell — full Zoo audit

> Published in `enuminous/papers` on 16 November 2026 at Matthew Wright's instruction. [Evidence and full roster](research/physlib-maxwell-zoo-2026-11-16/README.md) · [Download the original replay bundle](research/physlib-maxwell-zoo-2026-11-16/Physlib-Full-Zoo-Audit-2026-11-16.zip) · [Publication record](research/physlib-maxwell-zoo-2026-11-16/PUBLICATION_NOTICE.md). The archived audit and its findings are preserved; this edition adds publication navigation.

**Audit date:** 16 November 2026. **Target verdict:** PASS within the four-theorem mathematical scope below. **Audit-tool release integrity:** FAIL, limited to a stale README checksum. **EFMW or physical validation:** not established.

This is an AI-assisted, uncommissioned audit prepared at Matthew Wright's request. It is a local replay and source review, not independent human certification, a blind experiment, or an endorsement by Physlib's maintainers. No upstream files were changed.

## What was audited

The target is [Physlib's three-dimensional Maxwell module at commit 892e8fc](https://github.com/leanprover-community/physlib/blob/892e8fcba8af5ec691ca7a8ad82ee5dbe3180b17/Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean), its four named theorems, their declaration dependencies and physical assumptions. The source inventory covers 1,765 tracked files; the textual import closure contains 124 local modules. The semantic review concentrates on the Maxwell chain, not every theorem in the repository.

The exact environment is Lean `v4.35.0` (compiler commit `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`) and Mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679`. All nine dependency revisions matched the unchanged lockfile. Full pins and final source checks are in `FINAL_INTEGRITY.json`.

## Main results

| Check | Result | Evidence and limit |
|---|---|---|
| Pinned source and dependency integrity | PASS | Frozen target bytes, nine revisions and tracked Git state match. |
| Maxwell module build | PASS | 3,704 Lake jobs, using downloaded upstream artifacts. |
| Fresh Maxwell source elaboration | PASS | Unmodified source checked with `weak.says.verify=true` and warnings as errors. Imported dependencies were cached. |
| Full default build | PASS | `lake build -KCI --iofail`: 5,168 jobs for Physlib and QuantumInfo. Cache-assisted; PhyslibAlpha was not locally rebuilt. |
| Four-theorem axiom audit | PASS | Only `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`, custom axiom or native-computation axiom. |
| Nonvacuity witness | PASS | A separate Lean proof constructs positive free-space parameters, zero potential/current, smoothness and `IsExtrema` together. |
| Checker controls | PASS after diagnostic-name correction | Valid proof accepted; public/private axioms, placeholder and native proof rejected; false arithmetic rejected. Original attempts retained. |
| Physlib native-dependency attribution | PASS | Local `pseudo_lint Physlib QuantumInfo` passed. Physlib already performs this kind of dependency checking. |
| Conventional SI dimensions | PASS, conditional interpretation | Five exact dimension equalities; separate bookkeeping, not proof that the Lean types enforce SI dimensions. |
| Zoo package static integrity | **FAIL** | `verify.py` stops on README.md. Exactly one of 80 manifest entries differs. |

The full default build primarily restored cached artifacts. It is not a claim that all Physlib and Mathlib sources were freshly compiled. The Maxwell source itself was re-elaborated locally. Axiom collection and declaration traversal operate in Lean's imported environment; this is not a separate implementation of Lean's trusted kernel.

## The four mathematical contracts

All four statements quantify over time and three-dimensional position and use electric and magnetic fields obtained from an electromagnetic potential. `FreeSpace` supplies positive real permittivity and permeability; its speed of light is defined as `1 / sqrt(ε₀ μ₀)`.

| Theorem | Essential hypotheses | Conclusion | Reachable constants / Physlib constants |
|---|---|---|---:|
| `gaussLawElectric` | Smooth potential and four-current; `IsExtrema` | `div E = ρ / ε₀` | 50,988 / 1,328 |
| `gaussLawMagnetic` | Smooth potential | `div B = 0` | 35,225 / 291 |
| `ampereLaw` | Smooth potential and four-current; `IsExtrema` | `curl B = μ₀ J + μ₀ ε₀ ∂t E` | 51,003 / 1,340 |
| `faradayLaw` | Smooth potential | `curl E = −∂t B` | 35,342 / 324 |

These counts describe overlapping declaration graphs, including types and proof values. They are not numbers of independent confirmations. Exact elaborated types and direct references are in `logs/target-axiom-audit-attempt2.log`; the structured Physlib declaration traces are in `PROOF_DEPENDENCIES.json`.

### Stationarity, circularity and totalized definitions

[`IsExtrema`](https://github.com/leanprover-community/physlib/blob/892e8fcba8af5ec691ca7a8ad82ee5dbe3180b17/Physlib/Electromagnetism/Dynamics/IsExtrema.lean) is defined by `gradLagrangian = 0`. This is stationarity, not a proof of a local minimum or maximum. The [Lagrangian](https://github.com/leanprover-community/physlib/blob/892e8fcba8af5ec691ca7a8ad82ee5dbe3180b17/Physlib/Electromagnetism/Dynamics/Lagrangian.lean) is independently defined from the electromagnetic kinetic term and current-potential coupling; the equivalence to the inhomogeneous Maxwell equations is proved. Assuming stationarity is therefore an explicit dynamical premise, not simply assuming the final three-dimensional equations under another name.

There is a subtle boundary in the [variational-gradient definition](https://github.com/leanprover-community/physlib/blob/892e8fcba8af5ec691ca7a8ad82ee5dbe3180b17/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean): it returns zero when no gradient exists. Reading `IsExtrema` alone as evidence of genuine stationary dynamics would therefore be unsafe without existence conditions. Here the smoothness assumptions support `lagrangian_hasVarGradientAt_gradLagrangian`, establishing that the required gradient exists. No fallback-based vacuity was found in these four results.

The variational framework works with a density/integrand and smooth compactly supported test variations. Its integral notation does not assert that a global action integral is finite, or that a minimizer exists. Those stronger interpretations are not established by this audit.

The local witness `ZeroWitness.lean` additionally proves that the joint hypotheses have an explicit model. Its final axiom list contains only the three allowed foundations. This rules out empty-premise vacuity for that witness; it does not establish existence for arbitrary prescribed currents or initial/boundary data.

### Scope that survives scrutiny

The fields use the conventional potential formulas `E = −grad φ − ∂t A` and `B = curl A`. The homogeneous laws follow from derivative identities and smoothness. The constants and signs in the four displayed equations agree with those definitions; the separate SI dimension check found no mismatch under its stated interpretation.

The module explicitly excludes integral formulations, boundary conditions and material constitutive laws. It does not prove arbitrary-field representability by a global smooth potential, solution existence/uniqueness, singular-source behavior, quantum electrodynamics, or experimental confirmation. These are limits, not failures of claims the module makes.

## Full Zoo accounting

The frozen [Zoo formalization](https://github.com/enuminous/Monolithic-Zoo-Lean4/tree/8b22841ffcf44e41451e7696335bf6a6ae8f222e) registers 46 core animals and separately records five extension decision models. This audit also examines standalone [PEGASUS](https://github.com/enuminous/Pegasus/tree/41d57615f16c43ea8858e35cd1250d44c3c7df97) and records an unresolved lookup for the previously named HUMMINGBIRD. That is **53 accounted-for names**, not an assertion of a newly canonical 53-animal registry.

| Final disposition | Count | Meaning |
|---|---:|---|
| PASS | 1 | ELEPHANT verified the bounded, explicitly supplied version lineage. This says nothing about Maxwell truth. |
| FAIL | 1 | CIRCUS retained the observed material integrity failure in the Zoo release. This is not a Physlib theorem failure. |
| UNRESOLVED | 7 | TURTLE, MAGPIE, WEASEL, MOLE, LYNX lack justified target measurements; PEGASUS lacks a Lean-proof bridge; HUMMINGBIRD lacks a located contract. |
| NOT_APPLICABLE | 44 | Fixed operations requiring forecasting, causal/intervention, recovery, queue, agent, ranking or explanation data that this theorem audit does not contain. |

`FULL_ROSTER.md`, `.csv` and `.json` contain every name, purpose, schema, transformation, criterion and reason. Three fixed operations ran on actual target/audit records: ELEPHANT, CIRCUS and PEGASUS. The remaining operations were not given invented data merely to obtain outputs. This is a full applicability and evidence audit, **not a claim that every animal's complete pipeline executed**.

ELEPHANT traced four first-parent source-change commits plus the pinned snapshot anchor, terminating at the origin with one active selected record. It does not represent the entire Git DAG. CIRCUS initially returned N/A for pending independent review, then returned FAIL after the checksum failure was added to the final ledger under its unchanged precedence rule. Both runs remain available. PEGASUS returned four UNRESOLVED obligations because its v0.1 closed registry cannot validate Lean certificates; the passing Lean replay is recorded separately.

HUMMINGBIRD was not found in the pinned registry or extension manifest, the exact repository lookup returned 404, scoped repository searches returned no match, and the EFMW navigation index did not supply it. This does not establish that no implementation exists elsewhere.

### Audit-tool verification

- The 46 selected Python adapters passed 22 test methods, including all 90 reference comparisons.
- The pinned Zoo rebuilt under Lean 4.19.0; its reference runner passed all 90 comparisons.
- Its strict axiom audit passed for 2,797 safe declarations, including 1,255 theorem declarations. Public/private axiom, placeholder and native-proof rejection controls passed.
- Five extension decision models reproduced 643 source-derived finite certificates. Generated complete-record certificates numbered 1,432; exact-threshold certificates numbered 2,100. Both generated certificate sets compiled with their axiom audits. Nightingale coverage is a stopping-rule projection, not a validation of its statistical pipeline.
- PEGASUS passed 26 tests and verified all 17 files in its recorded freeze.
- Zoo builds emitted a nonfatal unused `horizons` warning in Moth. The local Physlib linter executable emitted a nonfatal module-system advisory. Neither is presented as a failed theorem.

The Python adapter engine is pinned at `fd4ac30ffdbb44c78e7ea69e2424beaa9f3fdb93`. Its embedded formalization snapshot is older than the current Zoo pin. Fixture agreement and current Lean compilation do not prove full Python/Lean pipeline equivalence. The 17 rank adapters aggregate supplied columns; they do not extract features or train models.

### Reproducible negative finding: stale Zoo manifest

At Zoo commit `8b22841`, `python3 verify.py` fails with `AssertionError: README.md`.

| Entry | SHA-256 |
|---|---|
| Recorded README hash | `87da76c0068124e3f2447bfe68d81143e95be419b58707a3e191fd2ec378d6da` |
| Actual pinned README hash | `0242e33fa54fbfc36807fc4813e2a5411d10598f1b482436af5f31f428c25341` |

The README's latest commit is `8b22841` (navigation/menu changes); the manifest's latest commit is `509480e`. All other 79 entries match. This is a release-integrity defect, not evidence that the theorem code changed or a mathematical claim is false. `ZOO_README_MANIFEST.patch` prepares the one-line correction for review; it was not applied or published. The final CIRCUS gate treats the failed declared integrity check as material to endorsing the tool release.

## Evidence, novelty and open obligations

**Demonstrated locally:** the bounded replay, printed axiom dependencies, nonvacuity witness, supplied version-lineage operation, fixture/certificate outcomes, dimension bookkeeping and stale checksum.

**Supported but incomplete:** correspondence between the formal contracts and the intended smooth, free-space classical formulation. The source-to-physics interpretation still merits independent human review; this AI-assisted audit does not certify the authors' intent.

**Unresolved:** seven named Zoo applications/contracts; empirical performance of the Zoo; EFMW-specific physics; weaker regularity, arbitrary-source solution existence and extensions beyond the stated module scope.

**Rejected interpretations:** a green build proves EFMW; fixture success is physical evidence; independent animal names imply independent evidence; `IsExtrema` establishes a minimum/maximum; all 53 names passed or executed.

The four equations and their potential/variational derivation are standard classical electromagnetism. This implementation and its formal verification are software/formalization contributions. No novel EFMW physical prediction follows from this audit. Source, cached CI artifacts, local replay and this report form related evidence, not multiple independent physical replications.

## Next concrete actions

1. Review the README-only change and apply the prepared manifest patch in a separate Zoo maintenance change, then rerun its static integrity check. Keep this original failure record.
2. Have a human physicist/formalizer review the exact theorem types, the density-based variational semantics and the zero-gradient fallback boundary. Request a verdict on those specific contracts.
3. For EFMW, specify one additional equation with explicit fields, units, coupling and boundary assumptions. Use Physlib's Maxwell results as a standard baseline; prove a precise reduction/bridge before claiming new consequences. Then identify an observable difference and a falsification test. This audit alone supplies no EFMW confirmation.

## Replay and provenance

The bundle contains the frozen plan, per-animal ledger, complete local logs, exact harnesses, quarantined negative controls, proposed patch, dependency data and selected source snapshots with licenses. `AMENDMENTS.md` preserves failed setup/harness attempts and their corrections. The native rejection test's first diagnostic expectation used the Lean 4.19 axiom name; Lean 4.35 generated a `native_decide` axiom instead. It was rejected on both runs; only the diagnostic assertion required correction.

The upstream [CI run at the same commit](https://github.com/leanprover-community/physlib/actions/runs/43690036787) reports successful build and lint steps, including PhyslibAlpha. Those hosted results are archived separately and are not substituted for local execution. No external review, communication or publication occurred during this audit.
