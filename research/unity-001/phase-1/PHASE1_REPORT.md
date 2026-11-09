# UNITY-001 — Phase 1 source freeze: executed audit

**Date:** 9 November 2026  
**Phase disposition:** **PASS for the bounded priority-source provenance freeze; UNRESOLVED for fresh independent mathematical replay, complete compiler import and physical theory.**  
**Deliverables:** [full lockfile](sources.lock.json) · [717-record source-equation ledger](source-equations.csv) · [extraction receipt](extraction-validation.json) · [conventions](conventions.md) · [provenance](provenance-ledger.md) · [replay evidence](replay-receipts/README.md).

## 1. Precisely what was frozen

Four priority repositories were pinned by their full 40-character Git commits; their recursive Git trees enumerate **209 file objects** with content-addressed Git blob hashes and sizes. The source-lock JSON records every tracked file path, not just a small citation list.

| Priority source | Pinned commit | Git blobs |
|---|---|---:|
| [Geometry](https://github.com/enuminous/Geometry/commit/285b95551ca11c487eb6c0c13f8dde86b702df71) | `285b95551ca11c487eb6c0c13f8dde86b702df71` | 15 |
| [Information-Tensor](https://github.com/enuminous/Information-Tensor/commit/b02b04897743d34cdb846e9fac2518cd8faa4399) | `b02b04897743d34cdb846e9fac2518cd8faa4399` | 66 |
| [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian/commit/83f9d2ec03e055c6cd09aa6359189161ad1571f6) | `83f9d2ec03e055c6cd09aa6359189161ad1571f6` | 122 |
| [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction/commit/aa569b13a594735774c7b643d44aebff4d5ad17c) | `aa569b13a594735774c7b643d44aebff4d5ad17c` | 6 |
| **Priority total** | **4 repository commits** | **209** |

This metadata pin is an immutable Git object inventory, **not** a claim that all 209 files have been mathematically audited or independently downloaded and SHA-256 verified.

## 2. Original upstream source chain — resolved for the four checked files

The archived sources were compared directly against their original upstream repositories at pinned commits:

| Upstream repository at exact commit | Source checked | Git blob identity |
|---|---|---|
| [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/commit/6e85c9e558652f5033c55d70f33077eff7a9fd89) | `canonical/equations.json` | **MATCH** `5e68eec5...` |
| [Monolithic_102_EFMW](https://github.com/enuminous/Monolithic_102_EFMW/commit/4129cc6e86396b6752433c80a78439662b441836) | `CANONICAL_102.md` | **MATCH** `a328e4ce...` |
| [FieldSpace](https://github.com/enuminous/FieldSpace/commit/4f994c45c319b44eaa43133280a7671e768da87c) | `fieldspace_master_action.md` | **MATCH** `337339a4...` |
| Same FieldSpace commit | `EFMW_165_field_equations.txt` | **MATCH** `ac6313fe...` |

**Result: 4/4 checked original-upstream blob IDs exactly match the archived source blobs.** These are checks of identical Git content, not external scientific validation.

## 3. Complete corpus transcription audit

The [source-equations.csv](source-equations.csv) ledger contains **717 line- or entry-addressed records**: 585 historical FieldSpace statements, 102 canonical ME entries, and 30 representative pinned mathematical source-line pointers (Geometry, Information-Tensor, WITD-002, C1, and the classical Standard Model).

- **585/585** rows in EFMW-Lagrangian `audit/equations.csv` have `source` strings identical to the specified `source_line` in the pinned original FieldSpace text. Zero transcription mismatches.
- **102/102** original catalogue formula blocks in the upstream canonical JSON and 102-section Markdown representation match **exactly when full multiline blocks are compared**. A naïve first-line-only comparison matches 98, with ME-065, ME-071, ME-073 and ME-102 spanning multiple lines. Those four are **resolved as textual identity**, not as physical proofs.
- Original `source` and audit `candidate_equation` occupy **different CSV columns** and never inherit each other's PASS.
- The 585 audit rows retain original literal classifications: **360 FAIL_SIGN, 88 FAIL_NEUTRAL_SCALAR_CURRENT, 2 UNDERDEFINED_CURRENT, 45 UNDERDEFINED_STRESS, 90 INDEX_REPAIR_REQUIRED**. These are source-vs-candidate audit classifications, not failures newly executed by this Phase 1.

The 30 additional entries preserve a verbatim **source line pointer**. A multiline equation/theorem requires its surrounding pinned file for complete mathematical context; a single line in the CSV is not represented as a full formal proof.

## 4. Physical and convention boundaries

- **Geometry**: `Geometry.lean` defines `totalSource = ordinary + κ * info` as a 4×4 component-array model and proves conditional identities. It does **not** construct tensor covariance, a complete Einstein–matter solution, or a measurable nonzero (kappa_I).
- **Information-Tensor**: the laboratory uses a fixed ((-+++)) Minkowski background, dimensionless normalized dynamics and explicitly authored memory/coherence closures. `R_ab` labels a residual, not Ricci curvature; WITD-002 contains energy-accounting results with retained numerical FAIL gates.
- **EFMW-Lagrangian C1**: proposed effective action, ((-+++)), frozen 165-triplet candidate; literally unmatched signs, gauge currents and gravitational stress terms are not silently normalized.
- **Standard-Model-Reduction**: classical Standard Model reference using ((+---)) and convention `Q=T3+Y`. The compact formula is a notation-level reconstruction, not a validated 39-strata or parameter-free theory.
- Source repository rights: Information-Tensor and EFMW-Lagrangian explicitly grant no new open-source redistribution license. These Phase 1 artifacts publish metadata and short pinned textual references, **not** entire upstream source files.

## 5. Reproduction and independent verification status

Head-matched existing GitHub Actions verification was observed for [Geometry](https://github.com/enuminous/Geometry/actions/runs/41696922044), [Information-Tensor](https://github.com/enuminous/Information-Tensor/actions/runs/42056702958) and [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian/actions/runs/40945020199). These are **existing upstream CI success reports**, not runs initiated by this Phase 1. Standard-Model-Reduction's [head-matched workflow](https://github.com/enuminous/Standard-Model-Reduction/actions/runs/40601622971) only deploys GitHub Pages; it does not independently run its SymPy verification script.

This execution environment has Python and Node, but lacks `lean` and `lake`, and cannot clone GitHub over the network. **No new independent clean Lean, Node, or SymPy replay has been claimed.** Complete instructions and honest execution distinctions are in [replay-receipts/README.md](replay-receipts/README.md). [verify_lock.py](verify_lock.py) is a local-verification utility to rerun the file-hash audit when the repositories are available; its first execution on the pinned full trees remains pending.

## 6. Phase gate outcomes

| Gate | Result | Scope |
|---|---|---|
| P1-A four priority commit pins | **PASS** | 4/4 full Git commits |
| P1-B tracked file object hashes | **PASS (Git metadata)** | 209/209 tree entries, nontruncated |
| P1-C canonical and FieldSpace original upstream head/source checks | **PASS** | Three additional upstream commits, 4/4 blob identities |
| P1-D historical FieldSpace source text fidelity | **PASS** | 585/585 exact source-line comparisons |
| P1-E canonical 102 textual archive fidelity | **PASS** | 102/102 complete formula-block matches |
| P1-F equation extraction ledger | **PASS (source fidelity)** | 717 records; not a type-checked physical corpus |
| P1-G exact existing toolchain and commands identified | **PASS (documentation)** | Lean 4.28; Mathlib pins, Node, SymPy requirements |
| P1-H fresh independent kernel / numerical / symbolic replay | **UNRESOLVED** | No fresh end-to-end execution in this environment |
| P1-I all 22 ontology sectors typed and cross-coupled | **UNRESOLVED** | This belongs to later phases; no assumption of Unity |

**Phase 1 narrow conclusion:** priority-source provenance and archived expression identity are reproducibly identified. This is a successful foundational source freeze, **not** completion of a master physical theory. The broader `ob_pin_sources` for *all* ontology sectors should remain open or explicitly scoped as “four priority sources pinned,” rather than being promoted to a blanket all-source PASS.

## 7. Next research gate

Using the pinned manifests, independently run `verify_lock.py` on clean Git clones, capture raw outputs of all specified toolchains, then start **Phase 2** with typed, versioned expression imports. Preserve the original source and candidate action as competing claims and require explicit convention bridges for metric signature, residual-vs-Ricci notation, scalar sign and gauge-current definitions.

**Original program:** [UNITY-001 Action Plan](../../../UNITY-001-Pathway-to-Physical-Unification-Action-Plan-2026-11-08.md) · [Unity Appendix](../../moc-001/UNITY_APPENDIX.md) · [Observe Unity](https://enuminous.github.io/Observatory/).

**Physical UNITY status: UNRESOLVED.**
