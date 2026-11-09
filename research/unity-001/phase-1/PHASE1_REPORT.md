# UNITY-001 — Phase 1 source freeze: executed audit

**Date:** 2026-11-09  
**Status:** **PARTIAL PASS — 4/4 repository commit pins and 209/209 Git-tracked file object IDs recorded; full cross-repository original provenance and independent mathematical replay UNRESOLVED.**  
**Source lock:** [sources.lock.json](sources.lock.json) · [Equation ledger](source-equations.csv) · [Conventions](conventions.md) · [Replay evidence](replay-receipts/README.md).

## What was done

Retrieved four exact default-branch commit SHAs through the connected GitHub repository API; inspected recursive trees and pinned all file objects to their Git blob SHA. The machine-readable lock includes every tracked file in the four snapshots, but **only selected mathematical files were read in detail**. This is an immutable Git provenance capture, not a fresh source tarball, standalone SHA-256 receipt, or independent proof replay.

| Repository | Immutable commit | Files locked |
|---|---|---:|
| [Geometry](https://github.com/enuminous/Geometry/commit/285b95551ca11c487eb6c0c13f8dde86b702df71) | `285b95551ca11c487eb6c0c13f8dde86b702df71` | 15 |
| [Information-Tensor](https://github.com/enuminous/Information-Tensor/commit/b02b04897743d34cdb846e9fac2518cd8faa4399) | `b02b04897743d34cdb846e9fac2518cd8faa4399` | 66 |
| [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian/commit/83f9d2ec03e055c6cd09aa6359189161ad1571f6) | `83f9d2ec03e055c6cd09aa6359189161ad1571f6` | 122 |
| [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction/commit/aa569b13a594735774c7b643d44aebff4d5ad17c) | `aa569b13a594735774c7b643d44aebff4d5ad17c` | 6 |

**Exact total:** 209 git blobs. The original historical copies inside EFMW-Lagrangian and the 102-catalogue copy inside Information-Tensor are individually identifiable by file object IDs; their *outside* upstream source repository heads were not frozen in this four-repo scope.

## Content checks that were actually executed

- **EFMW-Lagrangian 165-triplet archive:** independently compared the `source` field of every one of **585** rows in `audit/equations.csv` against its declared `source_line` in `sources/EFMW_165_field_equations.txt` at the same pinned commit. **585/585 exact string matches**, zero transcription mismatches. This is an archival transcription check only: the audit's stated **360 FAIL_SIGN**, 88 **FAIL_NEUTRAL_SCALAR_CURRENT**, two **UNDERDEFINED_CURRENT**, 45 **UNDERDEFINED_STRESS**, and 90 **INDEX_REPAIR_REQUIRED** source issues are not erased by transcription fidelity.
- **102-equation catalogue cross-archive screen:** parsed the 102 entries from Information-Tensor `sources/canonical-equations.json` and the 102 numbered sections in the EFMW-Lagrangian `sources/Monolithic_CANONICAL_102.md`. **98/102** equal the first extracted formula line exactly; the remaining four IDs **ME-065, ME-071, ME-073, ME-102** have multiline or prose-inclusive definitions and require block-normalized comparison. No invented discrepancy or equivalence claim is made.
- **Geometry:** identified exact `Geometry.lean` declarations and the pinned Lean/Mathlib toolchain, along with the authoring receipt's disclaimer that a local Lean build was then unverified; later successful GitHub Actions builds for the pinned head are linked separately.
- **Information-Tensor:** inspected the `docs/THEORY.md` equations, distinguished standard scalar stress from new memory/coherence closures and recorded WITD–002's conditional energy-accounting model.
- **Standard-Model-Reduction:** inspected the original three-line classical Lagrangian, SymPy verification script and its recorded 16 checks. **The repository's pinned CI workflow only deploys Pages**, so a green workflow is not an independent execution of the symbolic verifier.

## Important convention and rights boundaries

- Geometry and EFMW-Lagrangian use `(-,+,+,+)` in their primary candidate calculations; Information-Tensor uses a fixed Minkowski `(-,+,+,+)) background but retains a historical EFMW `(+,-,-,-)` source wave operator; Standard-Model-Reduction uses `(+,-,-,-)`. **No signs have been reconciled or normalized as if already equivalent.**
- EFMW-Lagrangian C1 is a *proposed classical effective action*, not the demonstrated physical origin of the complete 102-equation corpus.
- Information-Tensor's residual label `R_ab=beta T_ab[m]` is expressly **not the Ricci tensor**, and full memory energy is not a covariantly conserved informational stress by declaration.
- Information-Tensor and EFMW-Lagrangian expressly do **not** grant an open-source redistribution license; Geometry and Standard-Model-Reduction have no root license file in the pinned snapshots. Publication of provenance links does not redistribute their contents or create license rights.

## Phase-1 decision table

| Gate | Outcome | Meaning |
|---|---|---|
| P1-A — four repository commit pins | **PASS** | 4 of 4 exact 40-character commits located |
| P1-B — four recursive Git blob trees | **PASS** | 209 objects inventoried, tree API not truncated |
| P1-C — primary source statement locating | **PASS (bounded)** | Exact file objects, line/equation IDs for selected originals |
| P1-D — 585 audit row original-source comparison | **PASS** | All 585 recorded `source_line` values match raw archived text |
| P1-E — cross-archive 102 formula normalization | **UNRESOLVED** | Four multiline entries require semantic-preserving comparison |
| P1-F — *external* original upstream commit provenance | **UNRESOLVED** | Canonical/FieldSpace source copies are pinned, parent repository revisions are not |
| P1-G — fresh independent Lean, Python, Node, SymPy replay | **UNRESOLVED** | Prior successful CI exists; new end-to-end rebuild not performed |
| P1-H — fully verified all-source extraction into master compiler | **UNRESOLVED** | Source equation ledger is a source-faithful inventory, not a typed master equation derivation |

**No Phase 2 compilation, Unity correspondence, or physical validation is claimed.** Preserve `ob_pin_sources` open for the wider multi-repository corpus even though this bounded four-repo Git-source lock succeeds.

## Next evidence action

Resolve the four multiline catalogue block comparisons; pin the original upstream canonical/FieldSpace source commits and confirm their source bytes; independently replay the pinned toolchains; import the selected records into MOC-001 using explicit namespaces while retaining unresolved sign/current/tensor conflicts. Nothing in the present evidence proves (kappa_I \ne 0) or a new fundamental interaction.

**Public observatory:** [Observe Unity](https://enuminous.github.io/Observatory/) · **Plan:** [UNITY-001 action plan](../../../UNITY-001-Pathway-to-Physical-Unification-Action-Plan-2026-11-08.md).
