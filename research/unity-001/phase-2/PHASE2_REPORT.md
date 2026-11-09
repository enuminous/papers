# UNITY-001 — Phase 2: Source-Linked Mathematical Type Compilation

**Date:** 9 November 2026  
**Research:** Matthew Chenoweth Wright / Monolithic LLC; AI-assisted software and mathematical auditing  
**Scientific status:** **BOUNDED TYPE-CHECK PASS; COMPLETE MATHEMATICAL COMPILATION UNRESOLVED; PHYSICAL UNITY UNRESOLVED.**

**Previous stage:** [Phase 1 source freeze](../phase-1/PHASE1_REPORT.md) · [717-record original source ledger](../phase-1/source-equations.csv) · [four priority source commits and upstream copies](../phase-1/sources.lock.json)  
**Code and data:** [Conservative compiler](compile.py) · [typed registry](typed-registry.json) · [conflict register](conflicts.json) · [adversarial tests](test_compiler.py) · [machine-readable execution receipt](EXECUTION.json)  
**Executed CI:** [UNITY-001 Phase 2 typed compilation, GitHub Actions run 42619525163](https://github.com/enuminous/papers/actions/runs/42619525163) · [generated manifest artifact](https://github.com/enuminous/papers/actions/runs/42619525163/artifacts/13673897149)

## 1. Decision: typed subset, not wholesale ontology compilation

This phase introduces a restrictive standard-library Python compiler for **manually declared, source-linked expression ASTs**. It verifies reference linkage, original source-anchor preservation, identifier uniqueness, dependency-graph integrity, declared mathematical shapes and local dimension consistency. It does **not** automatically parse original Lean, natural-language physics, index-rich LaTeX, functional derivatives, or covariant PDEs.

The original 717 Phase 1 records remain complete and unchanged. Only nine have additionally authored typed interpretations. The other 708 are **UNCOMPILED / UNRESOLVED**, not failures or passes. The nine successful checks are not nine proved equations, and no physical EFMW-specific observation has been reported.

## 2. Executed Phase 2 results — exact denominator

| Metric | Executed result | Valid inference |
|---|---:|---|
| Frozen Phase 1 source records | **717** | Source provenance and original statements retained |
| Human-authored, source-linked typed AST interpretations | **9 / 717** | Declared shape/dimension and source anchor can be checked |
| Typed AST checks passed | **9 / 9 attempted** | Local type/source checks only; **not** original mathematical equivalence |
| Typed AST check failures | **0 / 9 attempted** | No error in this selected bounded sample |
| Records not compiled into typed AST | **708 / 717** | Remain UNRESOLVED |
| Open cross-ontology/conflict obligations | **8** | All retained UNRESOLVED |
| New derivations of mathematical equivalence | **0** | No claimed proof of source-to-AST equivalence |
| EFMW-specific physical PASS | **0** | No new measured or derived physical law certified |
| CI adversarial tests | **20 / 20 PASS** | Executed against Python 3.12 with GitHub Actions |

**Provenance of execution:** [Run 42619525163](https://github.com/enuminous/papers/actions/runs/42619525163) ran \`python3 -m unittest discover -s research/unity-001/phase-2 -p 'test_*.py' -v\` and \`python3 research/unity-001/phase-2/compile.py compile --out research/unity-001/phase-2/build/manifest.json\`. GitHub reports both commands succeeded; the machine-generated manifest is retained as a CI artifact, and the run log reports 9 typed PASS, 0 typed FAIL, 708 not compiled and eight conflicts.

**Historical baseline remains separate:** the original MOC-001 Observatory snapshot was **5/40** structural PASS, 4/22 illustrative dimensional equation checks, 0 EFMW-specific physical PASS. Those counts are not recomputed or replaced by this Phase 2.

## 3. Nine source-linked interpretations

| Source ledger ID | Namespace | Declared check | Explicit limitation |
|---|---|---|---|
| \`E002-Geometry\` | \`geometry_components\` | Source-component sum \`S=T+κI\` type compatibility | Arrays are not covariant tensors; κ not detected |
| \`E011-Information_Tensor\` | \`witd_lab\` | \`q_dot=p\` dimension and scalar shape | Lab state identity only |
| \`E013-Information_Tensor\` | \`witd_lab\` | \`m_dot=α(q-m)\` dimension | Authored relaxation law, conventional memory |
| \`E016-Information_Tensor\` | \`witd_lab\` | \`R_ab=βT_ab[m]\` rank-two shape | \`R_ab\` is **not Ricci curvature** |
| \`E017-Information_Tensor\` | \`witd_lab\` | \`I_ab=T_ab[q]+R_ab\` rank-two shape | No derived conserved gravitational stress |
| \`E023-EFMW_Lagrangian\` | \`c1_action\` | Declared scalar differential-term mass dimensions | \`□φ\` and \`∂U/∂φ\` treated as separately declared symbols, not parsed operators |
| \`E025-EFMW_Lagrangian\` | \`c1_action\` | Declared metric/stress tensor shape and mass dimensions | No metric variation or physical correspondence proven |
| \`E029-Standard_Model_Reduction\` | \`standard_model_classical\` | Tree-level \`m_h²=2λv²\` dimensional equality | No prediction of observed mass from first principles |
| \`E030-Standard_Model_Reduction\` | \`standard_model_classical\` | Hypercharge-anomaly expression dimensions | Does not by itself establish anomaly cancellation or novel parameters |

The type system intentionally forbids adding different tensor shapes or adding incompatible dimensions. It also rejects tensor multiplication without a specifically supplied contraction. Every expression belongs to a namespace with its own unit system: Geometry components, normalized \`Q/L\` field simulations, or natural mass dimensions. **No cross-namespace unit conversion or map is assumed.**

## 4. Conflict register: science left unresolved

The compiler preserves eight explicit conflicts/bridge gaps:

| Conflict | Open issue |
|---|---|
| C-P2-001 | Metric-signature mismatch: C1 \`(-+++)\` vs Standard Model reference \`(+---)\` |
| C-P2-002 | \`R_ab\` memory residual is not spacetime Ricci curvature |
| C-P2-003 | Historical scalar source sign vs C1 variational equation; the Phase 1 archive contains 360 \`FAIL_SIGN\` rows |
| C-P2-004 | Neutral real scalar currents not derived by C1; 88 prior \`FAIL_NEUTRAL_SCALAR_CURRENT\` rows |
| C-P2-005 | Information energy tensor not equated to full gravitational metric stress |
| C-P2-006 | 90 archived Bianchi statements require explicit index corrections |
| C-P2-007 | Component-level Geometry objects do not automatically have tensor-bundle/covariant structure |
| C-P2-008 | Classical SM notation compression does not establish the proposed parameter-free/39-strata theory |

The 585 archived historical source classifications are untouched, including 45 underdefined gravitational stresses and two underdefined gauge currents. These are **prior audit annotations**, not newly failed type checks. A type-system PASS on a manually translated equation cannot repair the original formula's sign, gauge, or geometric premises.

## 5. Implementation and adversarial review

The source-preserving compiler in [compile.py](compile.py) uses a small JSON abstract syntax tree with only:

\`\`\`text
symbol, number, add, sub, mul, neg, pow
\`\`\`

Each symbol declares a shape and integer dimensional-exponent vector. The implementation forbids unsupported AST operators, unknown symbols, malformed dimensions, excessive AST nesting, unbounded integer exponents, ambiguous contraction between non-scalar objects, missing source hashes, altered source anchors, duplicate typed IDs, missing dependency nodes and dependency cycles. The test suite also deliberately mutates one equation's right-hand dimensions and asserts that the checker records a **FAIL**, not a physical PASS.

Provenance is checked against the Phase 1 \`sources.lock.json\`: the record's original repository, exact commit, file path and Git blob ID must match a frozen source object. The original text must contain the manually specified source anchor. **This is a source-link check, not a formal proof that the human-authored AST equals the complete original expression.**

To reproduce:

\`\`\`bash
python3 -m unittest discover -s research/unity-001/phase-2 -p 'test_*.py' -v
python3 research/unity-001/phase-2/compile.py compile --out research/unity-001/phase-2/build/manifest.json
\`\`\`

No dependencies beyond Python 3.11+ are required. The [CI run](https://github.com/enuminous/papers/actions/runs/42619525163) used Python 3.12 and uploaded its output as the [typed-manifest artifact](https://github.com/enuminous/papers/actions/runs/42619525163/artifacts/13673897149).

## 6. Phase 2 gate disposition

| Gate | Disposition |
|---|---|
| P2-A frozen provenance references for selected expressions | **PASS, 9/9** |
| P2-B conservative AST shapes/dimensions | **PASS, 9/9 declared interpretations** |
| P2-C source preservation and 717-row inventory | **PASS, unchanged** |
| P2-D dependency/invalid-input adversarial guard | **PASS, 20/20 tests** |
| P2-E original source expression parser for all 717 | **UNRESOLVED, 708 uncompiled** |
| P2-F source-to-AST semantic equivalence proof | **UNRESOLVED, 0 equivalences certified** |
| P2-G cross-domain covariance, gauge/metric maps, Bianchi/stress consistency | **UNRESOLVED, 8 declared conflicts** |
| P2-H physical observation and independent replication | **UNRESOLVED, no physical claim** |

**Scientific result:** an executable, evidence-bounded bridge from a frozen heterogeneous-source ledger to nine checked, deliberately local type interpretations. This is substantive *infrastructure* progress, **not the completion of Phase 2 over all source equations or physical Unity**.

## 7. Next technical decision

Broaden parser coverage with explicitly versioned expression grammars and proof obligations rather than manually paraphrasing every physics equation. Priorities are: (1) full original Lean proposition and tensor-signature parsing; (2) explicit signature/curvature convention translation; (3) a matched, independent action-variation comparison against original source equations; and (4) one genuine cross-ontology correspondence map with counterexamples.

**Phase 3 must not receive a PASS from any present result.** The future target is a mathematical interface whose correspondence is demonstrated, not merely two equation ASTs whose dimensions agree.

**Public navigation:** [UNITY-001 execution plan](../../../UNITY-001-Pathway-to-Physical-Unification-Action-Plan-2026-11-08.md) · [MOC-001 Unity Appendix](../../moc-001/UNITY_APPENDIX.md) · [Observe Unity](https://enuminous.github.io/Observatory/).

*No upstream scientific repository was rewritten. Source statements, prior failures, and unresolved physical claims remain preserved.*
