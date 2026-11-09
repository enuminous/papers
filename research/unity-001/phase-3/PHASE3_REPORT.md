# UNITY-001 — Phase 3: Classical Correspondence and Source-Identifiability Obstruction

**Research:** Matthew Chenoweth Wright / Monolithic LLC; AI-assisted mathematics, independent-source comparison and reproducibility tooling  
**Date:** 9 November 2026  
**Status:** **BOUNDED CLASSICAL CORRESPONDENCE PASS; EFMW-SPECIFIC PHYSICAL BRIDGE UNRESOLVED; TOTAL UNITY UNRESOLVED**  
**Document type:** executed mathematical research report with counterexamples, not empirical discovery or peer-reviewed proof.

**Upstream:** [Phase 1 source freeze](../phase-1/PHASE1_REPORT.md) · [717 original records](../phase-1/source-equations.csv) · [Phase 2 typed compiler](../phase-2/PHASE2_REPORT.md) · [8 preserved Phase 2 conflicts](../phase-2/conflicts.json)  
**Implementation:** [Exact rational checker](bridge.py) · [27 adversarial tests](test_bridge.py) · [Interface contracts](interfaces.json) · [Counterexample register](counterexamples.json) · [CI execution receipt](EXECUTION.json)  
**Executed independent CI instance:** [GitHub Actions run 42622880582](https://github.com/enuminous/papers/actions/runs/42622880582) · [result-manifest artifact](https://github.com/enuminous/papers/actions/runs/42622880582/artifacts/13677480505)

## Executive result

The first actually stated correspondence is **not a full Einstein–Standard Model–EFMW unification**. It is an exact *bulk action-density projection* of the frozen classical C1 candidate onto an Einstein–Maxwell reference action, **only** under explicitly restrictive field and coupling choices. The associated Abelian gauge kinetic expression matches the hypercharge kinetic term in a truncated Standard Model sector, once the opposite metric-signature convention is translated. The full Standard Model remains outside the correspondence.

A second, adversarial result shows that the Geometry source split \(S=T+\kappa I\) is **not identifiable from a source-only observable when \(T\) may vary freely**: the informational term can be reallocated to ordinary stress without changing \(S\). This is an algebraic conditional result, not an observation of gravity, and not a no-go theorem when independently measured matter dynamics restrict \(T\).

**The conditional projection and the source-split obstruction are the Phase 3 outcomes; neither supplies an EFMW-specific gravitational measurement or a Theory of Everything.**

## 1. Starting material and immutable anchors

The implementation checks five exact Phase 1 source records against their full archived Git commit/blob IDs before reporting a result. The core source anchors are:

| Record | Frozen source | What is imported |
|---|---|---|
| \`E021-EFMW_Lagrangian\` | [C1 action](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md#L16) | Bulk classical action |
| \`E022-EFMW_Lagrangian\` | [C1 interaction potential](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md#L22) | Pair/triple-sector couplings, including \(g_{EM}RX\) |
| \`E025-EFMW_Lagrangian\` | [C1 metric equation](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md#L36) | Candidate classical stress equation |
| \`E027-Standard_Model_Reduction\` | [Classical SM Lagrangian](https://github.com/enuminous/Standard-Model-Reduction/blob/aa569b13a594735774c7b643d44aebff4d5ad17c/three_line_standard_model_geometric_reduction.md#L15) | Established classical Abelian gauge kinetic term and Higgs potential |
| \`E002-Geometry\` | [\`totalSource\` definition](https://github.com/enuminous/Geometry/blob/285b95551ca11c487eb6c0c13f8dde86b702df71/Geometry.lean#L33) | Abstract component-array source split |

These references are metadata and mathematical input contracts. **This phase does not alter any of the original 717 Phase 1 records, source conventions, or reported 585-statement mismatch classifications.**

## 2. Positive correspondence A: C1 to Einstein–Maxwell bulk action

### 2.1 Frozen C1 specification

With signature \((-+++)\), \(c=\hbar=1\), \(M_{\rm Pl}^2=(8\pi G)^{-1}\), two Abelian field strengths \(F=dA\) and \(H=dB\), and eight neutral scalar fields \(\varphi_a\), the C1 bulk action is

\[
S_{C1}=\int d^4x\,\sqrt{-g}\left[
\frac{M_{\rm Pl}^2}{2}(R-2\Lambda)
-\frac14X-\frac14Y
-\frac12\sum_a\nabla_\mu\varphi_a\nabla^\mu\varphi_a
-\mathcal U
\right],
\]

where \(X=F_{\mu\nu}F^{\mu\nu}\), \(Y=H_{\mu\nu}H^{\mu\nu}\), and

\[
\mathcal U=\frac12\sum_a(m_a^2+\xi_aR)\varphi_a^2
+\sum_{i<j}g_{ij}Q_iQ_j
+\sum_{i<j<k}h_{ijk}Q_iQ_jQ_k,
\]

with \(Q_E=R,\;Q_M=X,\;Q_S=Y,\;Q_a=\varphi_a\).

### 2.2 Explicit projection \(r_{\rm EM}\)

Define the restricted subfamily as follows: all eight \(\varphi_a=0\); the \(B\) gauge field and its strength \(H=0\); **all pair and triple interaction couplings \(g_{ij},h_{ijk}=0\)**. Keep the spacetime metric \(g\), the first Abelian field strength \(F\), \(M_{\rm Pl}\), and \(\Lambda\). The map is a *restriction of the theory's field/coupling family*, not evidence that nature selects this subfamily.

With these conditions, every term of \(\mathcal U\) vanishes and the bulk density becomes

\[
\boxed{\mathcal L_{C1}\big|_{r_{\rm EM}}=
\frac{M_{\rm Pl}^2}{2}(R-2\Lambda)-\frac14F_{\mu\nu}F^{\mu\nu}
=\mathcal L_{\rm Einstein\text{-}Maxwell}.}
\tag{P3-1}
\]

The exact-rational checker verifies this as a **formal polynomial identity** in the independently declared symbols \(M_{\rm Pl}^2,R,\Lambda,X\). The identity itself is algebraically immediate from the displayed action, rather than an unexpected prediction.

Subject to the usual smooth-field, boundary-condition, variational and gauge assumptions, the **standard** Euler–Lagrange equations of this restricted Einstein–Maxwell action are

\[
\nabla_\mu F^{\mu\nu}=0,\qquad
M_{\rm Pl}^2(G_{\mu\nu}+\Lambda g_{\mu\nu})
=F_{\mu\rho}F_\nu{}^\rho-\tfrac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}.
\tag{P3-2}
\]

Equation (P3-2) is the known formal classical variation of the restricted model. **This phase does not independently prove the continuum functional variation in Lean, construct an Einstein–Maxwell spacetime solution, or establish a complete boundary-term prescription.** It also does not derive observed Maxwell dynamics from an EFMW-specific primitive; Maxwell was already in the C1 action.

### 2.3 Counterexample: fields zero does not suffice

If scalars vanish and \(H=0\) but the C1 pair coupling \(g_{EM}\) remains, then

\[
\mathcal U\big|_{\varphi=H=0}=g_{EM}RX,\qquad
\mathcal L_{C1}-\mathcal L_{\rm EM}=-g_{EM}RX.
\tag{P3-3}
\]

A concrete **off-shell algebraic witness**, with \(g_{EM}=1/7,R=3,X=4\) in arbitrary compatible formal units, gives

\[
\Delta\mathcal L=-12/7\ne0.
\]

This proves the stronger unconditional projection statement **false**; it is not a physically realized curved spacetime solution. No silent adjustment of \(g_{EM}\) is allowed. The projection succeeds precisely because we declare the coupling-free subfamily.

## 3. Positive correspondence B: the classical Standard Model Abelian gauge expression

The pinned Standard Model reference uses metric convention \((+---)\), whereas C1 uses \((-+++)\). If a common rank-two metric is compared by the **global convention reversal** \(g_{\rm SM}=-g_{C1}\), then its inverse reverses sign. For an antisymmetric two-form,

\[
F_{\mu\nu}F_{\rho\sigma}g_{\rm SM}^{\mu\rho}g_{\rm SM}^{\nu\sigma}
=
F_{\mu\nu}F_{\rho\sigma}g_{C1}^{\mu\rho}g_{C1}^{\nu\sigma}.
\tag{P3-4}
\]

The two factors of the inverse metric cancel the two sign reversals. In four spacetime dimensions, the magnitude of the determinant and hence the natural volume-density factor is unchanged. This establishes a **convention translation for the Maxwell kinetic expression**, not automatic equivalence of Einstein–Hilbert terms, stress-tensor conventions, curvature signs, or full physical dynamics. In particular, a bare flip of metric sign also changes the scalar-curvature sign under consistently held connection conventions; full gravitational translation remains a separate obligation.

In the classical Standard Model, set the SU(3) and SU(2) field strengths, all fermions and the Higgs field \(H_{\rm SM}\) to zero. Keep only the hypercharge \(U(1)_Y\) gauge strength, identified with C1's surviving Abelian \(F\) for comparison of the kinetic term. The pinned SM Lagrangian then yields

\[
\mathcal L_{\rm SM}|_{\rm gauge\ branch}
=-\tfrac14X-\underbrace{\lambda v^4/4}_{V(H_{\rm SM}=0)}.
\tag{P3-5}
\]

The Higgs vacuum-energy offset **must not be silently discarded**. At \(\lambda=2,v=2\), the example difference from pure Maxwell is \(-8\), even at zero gauge field. On a fixed background the constant does not change the gauge Euler–Lagrange equation. In a proposed gravitational coupling, however, it affects effective vacuum energy. In an explicitly chosen common action convention it corresponds to an effective cosmological-constant contribution \(V_0/M_{\rm Pl}^2\); this is **not** a claimed complete gravitational/signature mapping of the original Minkowski-space SM reference.

The \(H_{\rm SM}=0\) configuration is stationary but typically **unstable** in the Standard Model's symmetry-breaking Higgs potential. Therefore this is a narrow algebraic/reference branch, not the observed electroweak vacuum, not a demonstration of the full Standard Model with three generations, Yukawa interactions or QFT quantization.

## 4. Metric and gauge-variation diagnostics

The Python checker uses exact rational arithmetic in four dimensions, not floating-point comparisons. It implements

\[
X=F_{\alpha\beta}g^{\alpha\gamma}g^{\beta\delta}F_{\gamma\delta}
\]

for antisymmetric \(F\) and symmetric contravariant metrics. With

\[
K_{\mu\nu}=F_{\mu\rho}g^{\rho\sigma}F_{\nu\sigma},
\]

the directional variation of \(X\) with respect to \(g^{\mu\nu}\), varying the symmetric off-diagonal pair together, obeys

\[
\partial_{g^{\mu\mu}}X=2K_{\mu\mu},\qquad
\partial_{g^{\mu\nu}_{\rm symmetric}}X=4K_{\mu\nu}\quad(\mu\ne\nu).
\tag{P3-6}
\]

The matter kinetic variation \(\delta(-X/4)=-\tfrac12 F^{\mu\nu}\delta F_{\mu\nu}\) is also checked by exact rational polarization. An ordinary analytic variation of the volume factor then yields the standard Maxwell Hilbert stress tensor in (P3-2).

**Executed examples:** 24 seeded antisymmetric 4×4 fields on a fixed nondegenerate diagonal inverse-metric example; 240 exact symmetric-metric direction comparisons, 24 gauge kinetic polarizations and 24 signature reversals. These are **finite diagnostic tests of exact formulas**, not a new general formal theorem for arbitrary curved metrics or a PDE existence proof.

## 5. Negative result: Geometry source-only EFMW identifiability

The pinned Geometry library defines only **component-level** arrays

\[
S_{\mu\nu}=T_{\mu\nu}+\kappa I_{\mu\nu}.
\]

For any other component array \(J\), let

\[
T'_{\mu\nu}=T_{\mu\nu}+\kappa J_{\mu\nu},
\qquad
I'_{\mu\nu}=I_{\mu\nu}-J_{\mu\nu}.
\]

Then

\[
\boxed{T'+\kappa I'=T+\kappa I=S.}
\tag{P3-7}
\]

Choosing the absorbed representation \(T'=S,I'=0,\kappa'=0\) also leaves \(S\) unchanged. Every source-only observation \(f(S)\) therefore receives the same input. These are exact component-array identities, closely tracking Geometry's pinned Lean theorems \`affine_split_invariance\`, \`source_absorption\`, and \`source_only_observable_blind\`. **That upstream Lean project had historical successful CI; the new Phase 3 workflow executes independent exact rational checks, not a new Lean kernel replay.**

The executable tested 24 seeded source reallocations and 24 absorbed-source equalities. It also includes a **negative control**: when ordinary \(T\) is held fixed by independent information and \(I\ne0\), the total sources at \(\kappa=0\) and \(\kappa\ne0\) differ. All 24 tested independently-fixed-matter controls discriminated in the constructed examples.

The result is therefore **conditional non-identifiability from source-only data**, not a physical theorem that every informational correction is forever unobservable. A valid EFMW-specific physical program must now identify a covariant admissible \(I\), define constraints on \(T\), specify a real observation map and noise model, and predict a measurable signal against \(\kappa=0\) and conventional alternatives.

## 6. Exact execution record and gate ledger

GitHub Actions run [42622880582](https://github.com/enuminous/papers/actions/runs/42622880582) completed on the pinned Phase 3 source branch using Python 3.12. The job ran:

~~~bash
python3 -m unittest discover -s research/unity-001/phase-3 -p 'test_*.py' -v
python3 research/unity-001/phase-3/bridge.py --out research/unity-001/phase-3/build/phase3.json
~~~

**Observed:** 27/27 tests passed. The bounded manifestation is retained as [artifact 13677480505](https://github.com/enuminous/papers/actions/runs/42622880582/artifacts/13677480505), and an indexed summary appears in [EXECUTION.json](EXECUTION.json).

| Finding | Outcome | Precisely what passed or failed |
|---|---|---|
| P3-REF-001 | **PASS** | C1 coupling-restricted Einstein–Maxwell *bulk density* identity |
| P3-REF-002 | **PASS** | Abelian SM Maxwell kinetic expression under explicit signature translation, with Higgs offset retained |
| P3-CEX-001 | **FAIL** | Stronger **unconditional** Einstein–Maxwell projection: \(g_{EM}RX\) survives if not set zero |
| P3-CEX-002 | **FAIL** | Stronger **exact** hypercharge-only SM = Maxwell density: fails by Higgs constant \(V(0)\) |
| P3-NEG-001 | **PASS** | Conditional source-only component-array non-identifiability, with fixed-matter counter-control |
| P3-GR-EFMW | **UNRESOLVED** | No source-preserving map from original EFMW informational stress to conserved gravitational stress |
| P3-FULL-SM | **UNRESOLVED** | No complete chiral/Yukawa/quantized SM correspondence |
| P3-FULL-DYNAMICS | **UNRESOLVED** | No independent full PDE-equivalence theorem, coupled spacetime solution or fresh Lean replay |

**Denominator:** 3 PASS, 2 FAIL, 3 UNRESOLVED **out of 8 explicitly scoped Phase 3 findings**. The two FAIL are valid refutations of overly broad interface claims, **not** experimental evidence that all versions of C1 or EFMW are false. The original MOC-001 5/40, Phase 2 9/717, and Phase 3 3/8 metrics are separate and cannot be added into a cumulative “unification score.”

## 7. Remaining correspondence obligations and next decision

1. **Covariant map:** model the actual Einstein–matter source in a metric spacetime, with constraints on its possible matter reallocations. The 4×4 component model does not prove a tensor-bundle or Bianchi correspondence.
2. **Energy/stress:** derive a mathematically and dimensionally correct EFMW informational stress and its necessary reservoir/energy exchange, if one exists; compare it with C1 stress **without repairing original signs or currents silently**.
3. **Gauge and signature:** reconcile the \((+---)\)/\((-+++)\) conventions including curvature, spinors, volume and stress—not only the quadratic Maxwell expression.
4. **Strong comparator:** require a conventional, non-EFMW null that uses the same observations and nuisance information, alongside \(\kappa=0\).
5. **Independent physical test:** only after a nonzero observable survives the above, freeze a measurement protocol and compare to independent data. No such experiment was executed here.

**Phase 3 campaign disposition:** the **reference-projection subtask is closed as a bounded algebraic result**, and the proposed EFMW-specific gravitational bridge is **not closed**. A prospective Phase 4 dynamical-consistency study can proceed on carefully selected models but must retain every previous physical and mathematical uncertainty.

## References

- [UNITY-001 action plan](../../../UNITY-001-Pathway-to-Physical-Unification-Action-Plan-2026-11-08.md).
- [MOC-001 Unity Appendix](../../moc-001/UNITY_APPENDIX.md).
- [C1 candidate / explicit projection rule, pinned](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md).
- [Classical Standard Model reference, pinned](https://github.com/enuminous/Standard-Model-Reduction/blob/aa569b13a594735774c7b643d44aebff4d5ad17c/three_line_standard_model_geometric_reduction.md).
- [Geometry component-array identities, pinned](https://github.com/enuminous/Geometry/blob/285b95551ca11c487eb6c0c13f8dde86b702df71/Geometry.lean).
- [Previous Phase 1 preserved source and audit identities](../phase-1/PHASE1_REPORT.md).
- [Phase 2 preserved typed interpretations and conflicts](../phase-2/PHASE2_REPORT.md).

*The first nontrivial deliverable is a bounded formal relationship plus a precisely scoped obstruction. No EFMW-specific physical interaction or total physical unification is established.*
