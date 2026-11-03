# Geometry-Foundation-002: An Interactive Counterexample Laboratory for EFMW Source Identifiability and Conditional Conservation

### A reproducible mathematical-physics laboratory for source reallocation, coordinate invariance, FLRW profiles, and synthetic observational controls

**Matthew Chenoweth Wright**  
**Monolithic LLC · Independent Research**  
**November 3, 2026 · Technical methods and results paper · Version 1.0**

**Status:** AI-assisted computational research report. Describes a published software artifact and source-specific arithmetic checks, not a new physical observation, a verified covariant EFMW gravitational theory, or independent peer review.

**Laboratory:** [Geometry Field Lab](https://enuminous.github.io/Geometry/) · [Code repository](https://github.com/enuminous/Geometry)  
**Inspected version:** [Geometry commit 1aad91c00c40e61a1ebf979c68a353194d190348](https://github.com/enuminous/Geometry/tree/1aad91c00c40e61a1ebf979c68a353194d190348)

---

## Abstract

The Einstein–Feynman–Maxwell–Wright (EFMW) program contains a proposed informational contribution to gravitational source equations. A fundamental methodological risk is to construct a symmetric, correctly indexed object and treat successful mathematical specification as evidence that it is independently present in nature. We introduce **Geometry-Foundation-002**, a standalone browser laboratory built to expose that error. Its eight interactive modes and eighteen curated presets examine algebraic reallocation of ordinary and informational sources, a reduced conservation obstruction inspired by the contracted Bianchi identity, coordinate-representation invariance, synthetic coupling identifiability, and explicit evidence boundaries.

The principal algebraic result is that for a total source \(S=T+\kappa I\), the replacement \(T'=T+\kappa J\), \(I'=I-J\) preserves \(S\). Hence any observation depending only on the total source cannot distinguish the two splits *when both allocations are permitted by the physical model*. A second result identifies a conditional obstruction to separate informational-sector conservation: with \(I_{\mu\nu}=T^{(\phi)}_{\mu\nu}+R_{\mu\nu}\), an on-shell separately conserved scalar sector still leaves \(\nabla^\mu I_{\mu\nu}=\frac12\nabla_\nu R\), which need not vanish. The lab illustrates this relation using a spatially flat power-law FLRW curvature profile but does not construct a self-consistent coupled ME-007 solution.

The JavaScript verification harness defines eighteen checks. During this manuscript's preparation, its computational functions were executed in an isolated Node.js JavaScript environment against the local version-0.2.0 HTML source. The resulting classifications were **14 PASS, one COUNTEREXAMPLE, three UNRESOLVED**, and zero finite-test FAIL statuses at the tested defaults. The experiment used simulated inputs only. Lean kernel compilation, full covariant geometry, admissible Einstein–matter solutions, and a real observation distinguishing nonzero \(\kappa I\) from a zero-coupling theory remain unresolved or unexecuted. The laboratory is therefore a reproducible specification and falsification aid, not empirical confirmation of EFMW physics.

**Keywords:** EFMW; mathematical physics; general relativity; source identifiability; contracted Bianchi identity; FLRW geometry; coordinate invariance; negative controls; scientific reproducibility.

## 1. The scientific question

A gravitational field equation can be written schematically as

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G\bigl(T_{\mu\nu}+\kappa I_{\mu\nu}\bigr). \tag{1}
\]

Equation (1) has at least three logically independent obligations. **G1—Construction:** specify domains, dimensions, regularity, tensor types, transformation laws, and conventions. **G2—Consequences:** determine which conservation and dynamical relations follow from independently stated assumptions and which apparently plausible claims fail under counterexamples. **G3—Physical discrimination:** derive a quantity that differs observably between admissible nonzero-\(\kappa I\) and zero-coupling theories.

A well-typed mathematical construction may have no independent physical interpretation. A successful Lean build or green browser check also need not distinguish a novel mechanism from an established one. The laboratory was designed around that central epistemic separation, following the outstanding ME-007 obligations in the [EFMW review ledger](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md) and the distinction between mathematical correctness and physical observability in standard relativity [1].

The target is **not** to prove that a proposed tensor is a tensor by definition. It is to provide tests that can obstruct an overly broad claim or reveal a non-identifiable parameterization, and to keep the wider physical hypothesis open when the evidence does not decide it.

## 2. Artifact architecture and implemented modes

The release consists of a single dependency-free browser HTML file, accompanied by a laboratory guide, a Lean source package, a counterexample atlas, and an evidence ledger. Its root interface presents eight modes:

| Mode | Main controls | Output and scope |
|---|---|---|
| Mission control | Eighteen experiment presets | Navigable experimental menu, not an exhaustive list of all possible experiments |
| Source-split | Editable 4×4 ordinary, informational and reallocation arrays; coupling; symmetry toggle; observable | Heatmaps and source/sector comparison |
| Conservation and FLRW | Power \(p\), time \(t\), scalar divergence, coupling, finite-difference step | Curvature and divergence profiles; conditional exchange accounting |
| Coordinate firewall | Rotation, shear, scaling, tensor entries | 2×2 basis/metric heatmaps, invariant contraction, determinant/conditioning guards |
| Identifiability | Free/fixed/measured matter, injected \(\kappa\), noise, sample count, seed, calibration trials | Synthetic traces, fitted coupling statistics, null/alternative histograms |
| Counterexample atlas | Direct experimental presets | Cases designed to expose limitations of specific EFMW-inferred statements |
| Verification harness | Run/check/export operations | Eighteen labelled arithmetic, negative-control and unresolved statuses |
| Evidence notebook | Claim, status, evidence and notes | Locally editable and exportable receipts, not authenticated external evidence |

The interface supports deterministic presets, configurable rendering quality and graphical sample density, heatmaps, charts, JSON/CSV receipts, and PNG graph export. Browser-local storage preserves user notes where supported. Neither local storage nor source-code visibility establishes the authenticity of a scientific claim.

The implementation is intentionally **not** a full computational implementation of differential geometry. Four-by-four real arrays have no automatic tensor-bundle semantics. The coordinate mode checks a two-dimensional, finite-dimensional example; the FLRW mode evaluates formulas under fixed conventions; and the observation mode generates its own synthetic data.

## 3. Source-split invariance and identifiability

Set the total source to

\[
S_{\mu\nu}=T_{\mu\nu}+\kappa I_{\mu\nu}. \tag{2}
\]

For any permitted reallocation \(J_{\mu\nu}\), define

\[
T'_{\mu\nu}=T_{\mu\nu}+\kappa J_{\mu\nu},\qquad
I'_{\mu\nu}=I_{\mu\nu}-J_{\mu\nu}. \tag{3}
\]

Then, by substitution,

\[
T'_{\mu\nu}+\kappa I'_{\mu\nu}
=T_{\mu\nu}+\kappa I_{\mu\nu}. \tag{4}
\]

No numerical simulation is required to prove (4); the browser experiment makes the exact identity inspectable. Its 4×4 heatmaps show changes in \(T\) and \(I\) alongside the unchanged total \(S\). At \(\kappa=0\), the displayed total source reduces to \(T\), providing a trivial but useful regression control.

If an observer is only given a quantity of the form \(\mathcal O(S)\), then

\[
\mathcal O(T+\kappa I)=\mathcal O(T'+\kappa I'). \tag{5}
\]

**Result A—Conditional source-only blindness:** these allocations cannot be distinguished *through that observable* when both are allowed. This does not imply that they are physically equivalent once independent matter equations, constitutive relations, units, initial data, and sector-specific measurements constrain \(T\). A separate matter readout may indeed distinguish \(T\) from \(T'\).

This point is more consequential than checking symmetry. If the informational source can be entirely absorbed into an unconstrained ordinary source, the new label need not correspond to a measurable new interaction. A genuine physical test must specify which reallocations are forbidden and why.

### Numerical source-split control

The released harness calculates the componentwise residual between the two sides of (4). In the isolated version-0.2.0 JavaScript invocation, the default maximum discrepancy was approximately \(1.11\times10^{-16}\). A deterministic 160-case sweep with generated component arrays and couplings had a maximum discrepancy approximately \(1.42\times10^{-14}\). These values are consistent with floating-point roundoff in equivalent formulas, not measured gravitational effects.

## 4. A conditional conservation obstruction

The [EFMW theorem notes](https://github.com/enuminous/papers/blob/main/THEOREMS_IN_PLAIN_ENGLISH.md) describe ME-006 algebraically as a scalar stress tensor plus a Ricci tensor:

\[
I_{\mu\nu}=T^{(\phi)}_{\mu\nu}+R_{\mu\nu}. \tag{6}
\]

This is a mathematical schematic. Curvature and physical stress-energy do not generally have the same dimensions, so a physically meaningful implementation must introduce or specify the required normalization. In ordinary metric general relativity, the contracted Bianchi identity gives

\[
\nabla^\mu R_{\mu\nu}=\frac12\nabla_\nu R. \tag{7}
\]

Assuming (6) is meaningful and differentiable under the relevant connection,

\[
\nabla^\mu I_{\mu\nu}
=\nabla^\mu T^{(\phi)}_{\mu\nu}
+\frac12\nabla_\nu R. \tag{8}
\]

Even if an on-shell scalar has separately conserved stress-energy, a nonzero curvature gradient leaves

\[
\nabla^\mu I_{\mu\nu}=\frac12\nabla_\nu R\ne0. \tag{9}
\]

This refutes the unrestricted inference that a scalar being on shell automatically forces *separate* conservation of the full Ricci-containing informational sector. It does **not** prove inconsistency of every possible coupled model. Total-source conservation, exchange between sectors, and possible restrictions on solutions must be addressed separately. For constant \(\kappa\), total-source conservation requires \(\nabla^\mu(T_{\mu\nu}+\kappa I_{\mu\nu})=0\). For a variable coupling, the derivative of \(\kappa\) must also be included.

### FLRW profile and controlled witness

The laboratory considers the spatially flat power-law metric profile

\[
ds^2=-dt^2+a(t)^2(dx^2+dy^2+dz^2),\qquad
a(t)=t^p,\quad t>0. \tag{10}
\]

With the adopted sign convention, its scalar curvature and derivative are

\[
R(t)=\frac{6p(2p-1)}{t^2},\qquad
\frac{dR}{dt}=-\frac{12p(2p-1)}{t^3}. \tag{11}
\]

For \(p=2/3\), \(t=1\), and stipulated zero scalar-stress divergence,

\[
R=\frac43,\quad \partial_tR=-\frac83,\quad
\nabla^\mu I_{\mu0}=-\frac43. \tag{12}
\]

This is a **conditional witness**: the browser computes the analytic profile and inserts the reduced Bianchi relation. The companion Lean source represents the reduced identity as an explicit premise. It does not derive a Ricci tensor from a metric and prove that an admissible coupled ME-007 Einstein–matter system realizes this configuration.

At \(p=1/2\), the selected scalar curvature \(R\) and its derivative vanish. That is a useful negative control, but \(R=0\) does not imply the full Ricci tensor or Riemann tensor is zero.

The finite-difference mode compares an analytic derivative with a centered approximation. In the tested default regression, reducing the differentiation step changed the absolute error from \(0.01604271\) to \(0.00396548\), a roughly fourfold reduction consistent with the local second-order error expected from centered differences. This is one smooth numerical example, not a theorem of uniform convergence near \(t=0\) or for arbitrary user-supplied parameters.

## 5. Coordinate/invariant firewall

Geometric objects and their coordinate components are not interchangeable. For a two-dimensional invertible basis change \(x=Ax'\), the lab transforms a covariant rank-two component matrix \(M\) and a metric \(g\) as

\[
M'=A^\mathsf{T}MA,\qquad
g'=A^\mathsf{T}gA. \tag{13}
\]

The metric-contracted scalar

\[
\operatorname{tr}[(g')^{-1}M']
=\operatorname{tr}(g^{-1}M) \tag{14}
\]

is invariant under these exact rules for nonsingular \(A\), while the ordinary component sum \(\operatorname{tr}(M')\) is not generally invariant under a shear.

The interface visualizes rotations, reflections, shears, scales, basis vectors and matrix heatmaps. It also rejects singular or strongly ill-conditioned transformations rather than reporting their unstable numerical outputs as trustworthy invariant checks. The tested regression obtained a metric-contracted trace difference approximately \(-4.44\times10^{-16}\) for a nonsingular change of basis; a shear changed the naïve trace, and exact singular inversion was rejected.

**Result B—Finite-dimensional firewall:** these examples check expected algebraic transformation behavior. They neither prove smooth coordinate covariance of the full ME-006 construction nor independently verify geometric field equations.

## 6. Synthetic identifiability tests

The trial generator creates one-dimensional artificial observations

\[
y_j=T_j+\kappa I_j+\epsilon_j. \tag{15}
\]

The user can choose an unrestricted ordinary sector, an exactly fixed ordinary sector, or a separately measured ordinary sector with its own noise. In the unrestricted mode, the alternative \(T'_j=y_j\), \(\kappa'=0\) fits source-only observations by construction. Accordingly, the lab treats a reported coupling-detection rate there as **not applicable**, not as evidence for a scientifically measured zero detection rate.

With fixed or measured ordinary matter, it computes a simple regression estimate of injected coupling. Setting \(e_j=y_j-T_j^{\mathrm{ref}}\), the code uses

\[
\widehat\kappa
=\frac{\sum_j I_j e_j}{\sum_j I_j^2},\qquad
\Delta\mathrm{SSE}
=\frac{(\sum_j I_j e_j)^2}{\sum_j I_j^2} \tag{16}
\]

when the denominator is positive. A lower fitted sum of squared errors is expected when a parameter is added; it is not, by itself, proof of a physical interaction. The program also forms a threshold from separate seeded synthetic calibration trials and evaluates other synthetic null and injected-coupling runs.

The laboratory demonstrates that an assumed ability to measure matter separately changes the mathematical identifiability problem. It cannot establish what ordinary matter is independently measurable in an actual gravitational system or whether a proposed informational source is distinguishable in nature.

## 7. Verification and results

### 7.1 Scope of the execution

The JavaScript calculation functions of the laboratory's local HTML source were evaluated in an isolated Node.js VM context with default laboratory parameters and a minimal browser-storage stub. The actual released function named **runHarness** returned eighteen classified records. This is a programmatic rerun of the computational harness, **not** a full graphical browser acceptance test, independently conducted scientific replication, execution of Lean, or measurement from a physical instrument. The source snapshot and reproduction instructions are linked below.

| Classification | Observed count | Meaning |
|---|---:|---|
| PASS | 14 | Internal algebraic/finite numerical criteria were met |
| COUNTEREXAMPLE | 1 | Deliberate conditional obstruction to an overly broad conservation implication |
| UNRESOLVED | 3 | Lean compilation, complete coupled physical model, and observational identification not demonstrated |
| FAIL | 0 | No finite arithmetic criterion failed for these particular defaults |
| Total | 18 | Not eighteen independent proofs or empirical successes |

Representative named checks include:

| Check ID | Test | Reported result |
|---|---|---|
| ALG-001 | Current \(T+\kappa I\) versus reallocated source | Maximum difference approximately \(1.11\times10^{-16}\) |
| ALG-002 | 160 seeded reallocation examples | Maximum difference approximately \(1.42\times10^{-14}\) |
| ALG-003 | \(\kappa=0\) reduction | PASS |
| ID-001 | Unrestricted matter absorbs source coupling | PASS within selected synthetic model |
| ID-002 | Fixed matter exposes injected-model difference | PASS; synthetic \(\Delta\mathrm{SSE}\approx66.1802\) |
| FLRW-001 / 002 | Dust-profile \(R(1)\), \(\partial_tR(1)\) | \(4/3\), \(-8/3\) |
| FLRW-003 | \(p=1/2\) scalar-curvature cancellation | PASS |
| NUM-001 | Centered difference step convergence | Error \(0.01604271\to0.00396548\) |
| COORD-001 | Metric-contracted trace | Difference approximately \(-4.44\times10^{-16}\) |
| COORD-002 | Naïve trace under shear | Changes, as expected |
| COORD-003 | Singular matrix rejection | PASS |
| CONS-002 | Separate conservation inferred from on-shell scalar | COUNTEREXAMPLE, conditional |
| LEAN-001 | Kernel-level theorem checking | UNRESOLVED in browser |
| PHYS-001 | Coupled Einstein–matter consistency | UNRESOLVED |
| PHYS-002 | Real-world nonzero-coupling identification | UNRESOLVED |

A PASS here often tests an identity or expected implementation property, not a difficult hypothesis. Conversely, the deliberate COUNTEREXAMPLE is a successful *adversarial test of a claimed implication*, not an empirical falsification of all EFMW research. These distinctions prevent mechanically adding statuses into a misleading percentage of “validated physics.”

### 7.2 Source quality and reproducibility

The HTML contains no required third-party JavaScript packages or backend. Its finite computations use the user's selected parameters and seeded random generator. The test receipt records a parameter snapshot, tolerances, version identifier and per-check status; CSV and JSON exports can preserve those details. Rendering resolution, derivative step size, and conditioning matter for numerical quality, but increasing plot resolution is not a route to a physical conclusion.

The companion [Lean source](https://github.com/enuminous/Geometry/blob/1aad91c00c40e61a1ebf979c68a353194d190348/Geometry.lean) defines four-by-four component functions and selected algebraic identities, including an explicitly assumed reduced-Bianchi relation. The browser does **not** run Lean or inspect kernel axioms. The [project proof ledger](https://github.com/enuminous/Geometry/blob/1aad91c00c40e61a1ebf979c68a353194d190348/PROOF_RECEIPT.md) records Lean build verification as outstanding; the presence of a workflow file is not a successful build receipt.

## 8. Discussion: what the lab adds and what it does not

The value of Geometry-Foundation-002 is methodological. It separates three questions that can otherwise be mistaken for one:

- Is a proposed mathematical expression well defined in its chosen formal setting?
- Which nontrivial consequences follow, and what explicit counterexample defeats an overbroad statement?
- Is there a new effect that a real observation can distinguish from an admissible conventional model?

A successful construction check does not entail the second or third. A fully traceable and formally correct statement may be physically false, untestable, redundant, or dependent on unjustified matter-sector assumptions. Likewise, detecting an injected effect in a simulator is not proof that the same effect is present in the universe.

The counterexample atlas addresses EFMW-specific claims—source-split reallocation, scalar-on-shell conservation, the physical reach of a source-only observation, and the limits of a curvature profile—instead of treating generic textbook examples as evidence that the framework has been validated.

The strongest mathematical point is source-sector nonuniqueness **under explicitly unrestricted reallocations**. Its strongest negative example is the conditional divergence obstruction. Its deepest unsolved problem is the identification of a real observable whose measured behavior cannot be explained with \(\kappa=0\) once ordinary matter and competing physical models are specified independently.

## 9. Open obligations and next experimental design

Several requirements remain open:

1. **Covariant formulation:** construct the full specified metric, connection, Ricci tensor, scalar source, regularity assumptions, and dimensional normalization for the exact ME-006 candidate.
2. **Conservation theorem:** derive rather than assume relevant identities, and determine which coupling/exchange laws permit a complete ME-007 solution.
3. **Admissible comparator:** define \(\kappa=0\) ordinary-matter models without granting them unrestricted post-hoc freedom or artificially restraining them to favor EFMW.
4. **Independent physical observable:** specify what is measured, in which units, with what data provenance and likelihood.
5. **Falsification criteria:** freeze an effect size, null, systematic-error model, and decision procedure before comparing with held-out external data.
6. **Reproducibility:** retain a successful Lean kernel build and full axiom output at the exact revision, and arrange independent code and experimental replication.

In particular, a true physical identifiability study must begin with a prediction that may fail. Producing additional geometry definitions, more interface modes, or a longer theorem inventory cannot substitute for it.

## 10. Conclusion

Geometry-Foundation-002 is an interactive and inspectable mathematical audit laboratory for the EFMW ME-006/ME-007 candidate. It provides eight computational views, eighteen experiment presets, and an evidence-bounded harness. A source-based isolated JavaScript run reproduced fourteen finite PASS checks and a conditional conservation counterexample, while recording three critical unresolved obligations.

The central conclusions are deliberately limited. Source-split reallocation can make \(T+\kappa I\) observationally non-identifiable when only its total is observed and the matter sector remains unrestricted. A scalar field being on shell does not automatically make a Ricci-containing informational contribution separately conserved under the stated curvature identity. Neither result proves a new physical theory or a fully inconsistent one.

**The scientific threshold has not changed: unless a measured observation can distinguish nonzero \(\kappa I\) from admissible zero-coupling explanations, the physical hypothesis remains UNRESOLVED.** Geometry supplies the language needed to pose that test correctly, not the evidence that the test has already passed.

---

## References

[1] Carroll, S. M. (1997), *Lecture Notes on General Relativity*, arXiv:gr-qc/9712019. [Public manuscript](https://arxiv.org/abs/gr-qc/9712019). Standard references for tensor transformations, curvature, the contracted Bianchi identity, and FLRW cosmology.

[2] Wright, M. C. (2026), *Geometry-Foundation-002: Interactive Geometry Field Lab*. [Pinned HTML source](https://github.com/enuminous/Geometry/blob/1aad91c00c40e61a1ebf979c68a353194d190348/index.html) · [Laboratory guide](https://github.com/enuminous/Geometry/blob/1aad91c00c40e61a1ebf979c68a353194d190348/LAB_GUIDE.md).

[3] Wright, M. C. (2026), *Geometry-Foundation-001: Source-Split Algebra and Reduced Conservation Obstruction*. [Lean source](https://github.com/enuminous/Geometry/blob/1aad91c00c40e61a1ebf979c68a353194d190348/Geometry.lean) · [Proof receipt](https://github.com/enuminous/Geometry/blob/1aad91c00c40e61a1ebf979c68a353194d190348/PROOF_RECEIPT.md).

[4] Wright, M. C. (2026), *EFMW ME-006/ME-007 Counterexample Atlas*. [Source](https://github.com/enuminous/Geometry/blob/1aad91c00c40e61a1ebf979c68a353194d190348/COUNTEREXAMPLE_ATLAS.md).

[5] Wright, M. C. (2026), *Open Obligations at the Frozen EFMW Review Target*. [Review ledger](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md).

[6] Wright, M. C. (2026), *Every Proved Theorem in This Project, in Plain English*. [Formalization notes](https://github.com/enuminous/papers/blob/main/THEOREMS_IN_PLAIN_ENGLISH.md). These describe a separate formal source target and do not validate the browser's physics interpretation.

[7] Wright, M. C. (2026), *Recursive Coherence as a Falsifiable Principle*. [EFMW dissertation-style research monograph](https://github.com/enuminous/papers/blob/main/EFMW-Dissertation-Recursive-Coherence-Evidence-Bounded-Verification-2026-11-02.md).

## Appendix A — Reproduction and independent audit procedure

**A1.** Open the [pinned laboratory source](https://github.com/enuminous/Geometry/blob/1aad91c00c40e61a1ebf979c68a353194d190348/index.html) in a browser. Select Verification harness and run its checks, retaining the actual exported JSON/CSV receipt and parameter snapshot.

**A2.** In Source-split, change \(J\) with nonzero \(\kappa\). Inspect componentwise invariance of \(S\), then switch from a source-only observable to a matter-only observable. Do not conflate the two observation models.

**A3.** In Conservation, test \(p=2/3,t=1\), zero scalar divergence, and vary the derivative step. Then test \(p=1/2\) and nonzero scalar divergence. Record which relations are inputs and which are calculated consequences.

**A4.** In Coordinate firewall, compare invariant contraction under invertible shear with the naïve component trace; inspect determinant and conditioning. Reject singular matrices rather than reporting unstable numbers.

**A5.** In Identifiability, run unrestricted, fixed, independently measured, coupling-null and high-noise presets. Record exact seeds, signal templates, calibration sample counts, and whether the selected ordinary-matter model is genuinely independent of the candidate effect.

**A6.** Separately, execute the Lean source from the pinned project revision, with its pinned toolchain and dependencies, using:

    lake update
    lake build Geometry
    lake env lean Axioms.lean

Preserve exact commit, lockfile, exit status and axiom output. **These commands were not executed as part of the JavaScript rerun reported in this paper.** Do not infer compilation success from their inclusion.

**A7.** Report the physical discriminator gate G3 as **UNRESOLVED** until an independently measured physical quantity and a predeclared conventional comparison exist.

## Appendix B — Claims-to-evidence ledger

| Claim | Evidence | Status |
|---|---|---|
| Browser source implements eight laboratory modes | Pinned index.html and guide | IMPLEMENTED |
| Algebraic source reallocation preserves total components | Exact identity and numerical harness | PASS, bounded |
| Ordinary-source redefinition is always physically admissible | No complete matter laws supplied | UNRESOLVED |
| Separate informational conservation follows from scalar on-shell status alone | Conditional Bianchi countermodel | COUNTEREXAMPLE |
| Full Lorentzian tensor framework proved | Not present in browser or source package | UNRESOLVED |
| Standalone Lean proofs passed kernel build in this paper's run | Not executed | UNRESOLVED |
| Real physical measurements favor nonzero \(\kappa I\) | No measurements presented | UNRESOLVED |

**Research disclosure.** The laboratory and this paper were prepared with AI assistance. Mathematical and numerical identities are reported within their specified domains; no claim of physical validation, external peer review, or new experimental data is made. Future corrections should be versioned and should preserve the negative controls and unresolved questions.
