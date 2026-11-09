# IST-FAM-001 — Joint Referee Review, Conventional Spectral Containment, and a Bounded EFMW Novelty Audit

**Program:** Matthew Chenoweth Wright / Monolithic LLC · EFMW / IST-001 / UNITY-001  
**Date:** 9 November 2026  
**Document class:** Critical research memorandum and proposed falsification protocol; **not** peer-reviewed theory, an original physical discovery, or completed audit  
**Review provenance:** Dialogue between the program author, ChatGPT (“Millie”), and comments the author attributed to Boardy. Boardy's independent identity, institutional affiliation, and sign-off are **not independently authenticated** by this record. AI assistance produced this synthesis.  
**Disposition:** CONVENTIONAL RESERVOIR CONTROL: BOUNDED MATHEMATICAL SUPPORT · EFMW-SPECIFIC GRAVITATIONAL NOVELTY: **UNRESOLVED** · IST-FAM-001 SOURCE-CONSTRAINT AUDIT: **NOT EXECUTED**

**Important chronology:** The **two-hypothesis audit contract was frozen first** in [research/ist-fam-001/PROTOCOL.json](research/ist-fam-001/PROTOCOL.json), commit [3661841](https://github.com/enuminous/papers/commit/3661841f69bb9dbd01338ee21f494d8d0b8ca7ce). It is an **author-defined hypothesis lock**, not an external preregistration and not a blind exercise: earlier EFMW work has already examined portions of the canonical corpus. The present publication does **not** carry out its source search, execute new calculations, or modify the original IST-001 findings.

## Abstract

IST-001 models memory with conventional interacting scalar fields, a finite harmonic reservoir, and a proposed route to a generalized Langevin equation. Its Hilbert stress and exchange identities are meaningful within the chosen action, but they do not by themselves establish informational gravity: gravity couples to the **total** stress-energy tensor, and the division between an ordinary field and a memory sector is not intrinsically observable from total stress alone.

The referee exchange identified scope corrections in the use of a prescribed external drive, the disappearance of a standalone memory mass term between candidate actions, the requirement for a justified overdamped continuum limit, and the lack of a source-faithful map from the historical EFMW corpus. It also corrected two initial reviewer claims: the completed-square oscillator interaction already includes the static counterterm, so the exact finite-bath reduction preserves the coefficient $K$; and spatially nonuniform or multiple scalar fields can exhibit anisotropic stress in appropriate frames, even though homogeneous single canonical scalars do not.

A pointwise test of stress-energy decomposition is generally inadequate. The appropriate mathematical comparison concerns **families of observable responses under one parameter assignment** across predeclared conditions. For IST-001's finite-bath memory kernel, the positive discrete spectral representation places it inside the conventional oscillator-bath class; this alone is not new physics. To avoid an unconstrained search for post-hoc novelty, the accompanying protocol names **exactly two speculative source constraints**, their mapping prerequisites, and the stop rule before inspecting the frozen source inventory under that protocol.

## 1. Original IST-001 evidence boundary

The [IST-001 theoretical memorandum](IST-001-Deriving-Informational-Stress-from-Covariant-Memory-and-Reservoir-Models-2026-11-09.md) and its [executed companion report](research/ist-001/IST001_REPORT.md) construct an illustrative classical covariant action and a finite oscillator-bath parent. The archived [CI run 42669567461](https://github.com/enuminous/papers/actions/runs/42669567461) reports **24/24 software tests passing**, covering six narrowly defined bounded gates; two remain UNRESOLVED. No EFMW-specific physical PASS is established.

This review does not relabel those existing gates, claim new independent replay, or resolve [UNITY-001 Phase 5](research/unity-001/phase-5/PHASE5_REPORT.md), which documented a co-located conventional-source degeneracy in a dimensionless synthetic setup.

A mathematical or software check is a prerequisite to physical modeling, not empirical verification of a new interaction.

## 2. Conservation: autonomous system versus prescribed drive

The conservative action treats the fields $q$ and $m$ dynamically, and its metric-derived *total* stress satisfies the on-shell conservation identity

$$
\nabla^\mu\left(T_{\mu\nu}^{(q)}+I_{\mu\nu}\right)=0
$$

when both Euler–Lagrange equations hold. The split $I_{\mu\nu}$ need **not** be conserved separately; it exchanges energy-momentum with the $q$ sector.

In the homogeneous reservoir calculation, however, IST-001 takes $q(t)$ as an **externally prescribed drive** to exhibit a generalized Langevin reduction. This is not the same autonomous test. For

$$
E_{m+B} = \frac{Z}{2}\dot m^2+\frac K2(m-q)^2+
\sum_j\frac{z_j}{2}\left[\dot x_j^2+\omega_j^2(x_j-a_jm)^2\right],
$$

the memory-and-bath equations imply

$$
\boxed{\frac{dE_{m+B}}{dt}=K(q-m)\dot q.}
$$

That right-hand term is work supplied by the prescribed driver; it does not generally vanish. The fully dynamical $q$ sector supplies the compensating balance on its equations of motion. A scalar source can be treated covariantly as an external background, but **holding it prescribed means its field equation is not available to infer full on-shell conservation for the reduced subsystem**.

**Referee finding R1 — VALID SCOPE CORRECTION.** Preserve the full-parent conservation identity, but do not use a manufactured externally driven residual as independent evidence for the autonomous system's complete conservation or dynamics.

## 3. The counterterm correction: no forced shift of static K

A preliminary objection suggested that eliminating the bath must renormalize the restoring coefficient $K$ appearing in IST-6, IST-8 and IST-10. That objection was withdrawn after inspecting IST-6's **completed-square displacement**:

$$
V_B=\sum_j\frac{z_j\omega_j^2}{2}(x_j-a_jm)^2.
$$

Writing $c_j=z_j\omega_j^2a_j$, expansion gives

$$
V_B=\sum_j\left[
\frac{z_j\omega_j^2}{2}x_j^2-c_jx_jm
+\frac{c_j^2}{2z_j\omega_j^2}m^2
\right].
$$

The last quadratic contribution is the usual static counterterm. In the **exact finite-bath elimination of this specified action**, the static displacement cancels, leaving $K$ unchanged in the generalized Langevin equation:

$$
Z\ddot m+K(m-q)+\int_0^t\gamma(t-s)\dot m(s)\,ds=\xi(t).
$$

Dynamical self-energy and low-frequency response still require analysis; the continuum friction coefficient $\Gamma$ has not been derived from a specified spectral-density limit. Thus $\alpha=K/\Gamma$ is **conditional** at the Markov/overdamped stage, not an already calibrated microscopic prediction.

**Referee finding R2 — OBJECTION WITHDRAWN AS TO EXACT FINITE-BATH K.** The original counterterm objection applied to a *different, counterterm-free action*. Disclose the completed square and preserve the unresolved continuum derivation; do not change $K$ by fiat.

## 4. The missing memory mass is a substantive model change

The conservative illustrative action IST-1 contains $\mu_m^2 m^2/2$; the reservoir parent IST-6 omits this standalone memory-mass term. The shifted oscillator bath does **not** automatically supply an equivalent isolated mass: its potential vanishes when each $x_j=a_jm$.

If an explicit positive memory mass is retained, the overdamped reduced equation takes the form

$$
\Gamma\dot m+(K+\mu_m^2)m=Kq
$$

in the specified simple approximation, leading at constant $q$ to

$$
\boxed{m_{\rm eq}=\frac K{K+\mu_m^2}q.}
$$

For $K>0$ and $\mu_m^2>0$, the equilibrium gain is below one. Exact unit-gain tracking $\dot m=\alpha(q-m)$ emerges in this simple parent if $\mu_m^2=0$, if the offending independent restoring effect is canceled, or if a different physically justified potential has its minimum at $m=q$.

This does **not** mean all restoring forces must vanish. The potential $K(q-m)^2/2$ *restores toward $q$* and gives unit equilibrium gain by construction. The problem is that IST-001 has supplied no independent symmetry, source derivation, or other physical protection for the required parameter restriction. Selecting a term to vanish because it reproduces WITD is not a source-faithful derivation.

**Referee finding R3 — VALID STRUCTURAL DISCREPANCY.** The IST-6 parent must be declared a deliberately modified candidate model, not an automatic extension retaining every term of IST-1. Source-derived unit-gain tracking remains UNRESOLVED.

## 5. Why a finite conservative bath is not demonstrated irreversible relaxation

A closed finite set of oscillators is Hamiltonian/reversible in the proposed classical parent. It can transfer energy and exhibit transient dephasing, but its mere existence does not establish autonomous irreversible **Markovian** damping with the WITD first-order tracking law.

To derive controlled irreversible or effectively dissipative behavior, one must specify a suitable reservoir limit, relevant initial-state ensemble, causal coarse-graining and quantitative approximation, and where thermal claims are made, appropriate fluctuation–dissipation constraints.

IST-001's finite-bath experiment and prescribed-drive residual support the bounded algebraic reduction, not an independently validated continuum or thermodynamic limit.

**Referee finding R4 — MOST IMPORTANT NEGATIVE DISCIPLINE.** Ordinary closed scalar actions do not acquire a universal autonomous first-order dissipative semigroup merely by naming a field “memory.” No irreversible WITD derivation has been demonstrated.

## 6. Stress anisotropy does not rescue a gravitational discriminator

In a rest frame of a homogeneous single minimally coupled canonical scalar with timelike gradient, anisotropic stress vanishes. But for a spatially varying memory field in a chosen local frame the traceless spatial contribution can be

$$
\pi_{ij}^{(m)}
=Z\left(\partial_i m\,\partial_j m
-\tfrac13\delta_{ij}|\nabla m|^2\right).
$$

Nonparallel gradients among multiple fields can lead to imperfect-fluid behavior. Therefore the categorical claim that **all scalar sources have zero anisotropic stress** is too strong.

Equally, a nonzero $\pi_{ij}$ does not uniquely identify informational physics: conventional matter, scalar models and imperfect-fluid constitutive descriptions can reproduce such stresses. The choice of rest frame and on-shell physical states must be stated before interpreting a spatial-traceless component.

**Referee finding R5 — MATHEMATICAL CORRECTION, NOT NOVELTY.** The existence of anisotropic stress in a candidate configuration does not by itself evade the co-located conventional-source degeneracy.

## 7. Move from pointwise matching to response-family containment

A single stress configuration does not test the explanatory constraints of a model across experimental interventions. For predeclared conditions $\mathcal C$, consider a model response map

$$
\mathcal R_I:\Theta_I\longrightarrow\mathcal Y^\mathcal C
$$

and a conventional comparator

$$
\mathcal R_N:\Theta_N\longrightarrow\mathcal Y^\mathcal C.
$$

The substantive comparison asks whether

$$
\operatorname{Im}(\mathcal R_I)\subseteq\operatorname{Im}(\mathcal R_N),
$$

with **a single coherent comparator parameter set across the whole response family**, not independent retuning at each condition.

For an unconstrained phenomenological imperfect fluid, pointwise matching may be easy because its constitutive freedom is broad. Serious comparison requires prior constraints on admissible conventional responses, not a model so flexible it cannot fail.

For the present IST-001 finite harmonic bath, however, family-level equivalence has a transparent conventional construction. Its linear memory kernel is

$$
\gamma_\theta(t)=\sum_{j=1}^{N}b_j\cos(\omega_jt),\qquad
b_j=z_j\omega_j^2a_j^2\ge0,
$$

and corresponds to a positive *finite discrete* spectral measure,

$$
d\rho_\theta(\omega)=\sum_jb_j\,\delta_{\omega_j}(d\omega),
\qquad
\gamma_\theta(t)=\int_0^\infty \cos(\omega t)\,d\rho_\theta(\omega).
$$

This is the conventional oscillator-bath spectral representation. Broader positive measures may produce suitable cosine kernels subject to convergence, regularity and physical-realization assumptions; positivity alone is not a complete continuum-bath or thermodynamic existence proof.

For zero initial perturbations with fixed driving/noise conventions, the corresponding linear transfer function is

$$
H_\theta(s)=\frac{\widetilde m(s)}{\widetilde q(s)}
=\frac{K}{Zs^2+K+s\widetilde\gamma_\theta(s)}.
$$

An ordinary oscillator-bath comparator that admits the same spectral measure, parameters, and initial-state assumptions produces the same kernel and transfer response. A conventional comparator with the **identical full action** also produces the same total stress. This latter inclusion is logically straightforward and should **not be advertised as a novel theorem**.

**Referee finding R6 — CONVENTIONAL FAMILY CONTAINMENT.** The finite-bath formulation supplies positive discrete spectral structure, but that structure is already conventional. A more general fluid comparator must be constrained meaningfully before a discriminatory result can be interpreted.

## 8. Calibration and theoretical discrimination remain separate

**Independent calibration** fixes relevant physical inputs—e.g., $K$, $Z$, $z_j$, $\omega_j$, $a_j$, and eventually $\Gamma$—without estimating them from the target gravitational residual. This makes a model testable and potentially predictive.

**Theoretical discrimination** requires the independently calibrated candidate to predict something that comparably constrained conventional alternatives do not.

Calibration is necessary for a noncircular claim in the present gravitational test strategy; it is not sufficient for **EFMW-specific** novelty. An independently calibrated ordinary oscillator bath can give excellent predictions and still be ordinary matter.

A single source decomposition in Einstein's equation is not independent evidence: the metric couples to the total gravitating stress. More elaborate comparisons can become informative when conventional-source priors and response laws are fixed by independent data, but a new name for one portion of the same full stress cannot create a new gravitational effect.

**Referee finding R7 — DO NOT CONFLATE JOBS.** A successful constrained spectral prediction would be useful science even if it provides no uniquely EFMW gravitational phenomenon.

## 9. IST-FAM-001 — Exactly two prospective source constraints

The objective is **not** to ask vaguely whether any of the 102 EFMW formulas resembles a bath constraint. That creates an uncontrolled pattern search without an informative failure condition.

Before any new confirmatory-source scan, the [IST-FAM-001 protocol](research/ist-fam-001/PROTOCOL.json) fixes exactly two speculative targets:

**H1 — Consecutive physical-mode frequency ratios:**

$$
\frac{\omega_{j+1}}{\omega_j}=\varphi,\qquad
\varphi=\frac{1+\sqrt5}{2},
$$

for two adjacent intervals in one **source-justified consecutive triple** of at least three modes.

**H2 — The same triple's spectral-weight ratios:**

$$
\frac{b_{j+1}}{b_j}=\varphi^{-2}
$$

for its two adjacent intervals, using strictly positive weights.

**These particular forms are speculative audit hypotheses, not previously demonstrated derivations.** Golden-ratio and Scalar-23 motifs motivate examining them, but the ratio and exponent are **not evidence**, and the exponent $-2$ must not be retuned after source inspection.

A genuine source-constrained result must identify, at frozen source revisions:

- A noncircular map from original EFMW quantities to physical bath modes and weights, including units and domain.
- A unique pre-specified mode index, with no post-hoc subset selection.
- A derivation that is **not** a definition, ordinary positivity, or freely selected parameterization.
- The precise source coordinates, assumptions, required exclusions, and independently reproducible algebra.

The frozen search domain is the **102 canonical formulas plus 585 FieldSpace source lines**, exactly 717 archived source-ledger records. There has already been prior exposure to some source content: the current contract is **not blind**. New attractive constraints found outside H1 and H2 are labeled **EXPLORATORY ONLY** and may not enter this confirmatory decision.

### Outcome rules

| Classification | Meaning |
|---|---|
| SOURCE PASS | A pinned original entails the predeclared relation under a justified nondefinitional mapping and replayable proof; **not** a physical novelty PASS |
| COUNTEREXAMPLE FAIL | An explicit admissible source-derived result contradicts the predeclared relation |
| NO SOURCE SUPPORT | The bounded source audit finishes without a qualifying derivation: this source-support claim fails, but no general impossibility follows |
| UNRESOLVED | Incomplete search, missing mapping, ambiguous semantics, or insufficient premises |
| EXPLORATORY ONLY | A different relation is noticed after inspection; never silently promoted |
| PHYSICAL DISCRIMINATION | **Not evaluated by this audit**; requires separate calibrated, prospective comparisons and independent observation |

A constraint realized within a conventional positive spectral model remains compatible with conventional physics, even when genuinely source-derived.

### Stop rule

If **neither H1 nor H2** receives source-faithful support, classify this bounded IST-001 **spectral-novelty route as NOT ESTABLISHED IN THE FROZEN CORPUS** and do not use the route to justify additional costly gravitational experiments. This is not a proof that no alternative EFMW model or constraint can ever exist. Any new family must be proposed and frozen in a separately versioned investigation.

## 10. Decision and evidence ledger

| ID | Topic | Present review disposition |
|---|---|---|
| R1 | Prescribed q versus autonomous conservation | VALID QUALIFICATION; no new physical PASS |
| R2 | Exact finite bath static K counterterm | ORIGINAL OBJECTION WITHDRAWN; K preserved for the stated action |
| R3 | Missing standalone memory mass | MODEL-DIFFERENCE CONFIRMED; physical rationale for $\mu_m^2=0$ unresolved |
| R4 | First-order irreversible relaxation | CONTINUUM/COARSE-GRAINING LIMIT UNRESOLVED |
| R5 | Scalar anisotropic stress | CATEGORICAL ZERO-STRESS CLAIM CORRECTED; novelty still unsupported |
| R6 | Family-level conventional spectral containment | CONSTRUCTIVE CONVENTIONAL EQUIVALENCE; not a new EFMW theorem |
| R7 | Calibration versus discrimination | DISTINCT REQUIRED INFERENTIAL TASKS |
| H1 | Source-derived golden frequency ratios | NOT EXECUTED |
| H2 | Source-derived golden weight ratios | NOT EXECUTED |
| IST-G | Independently distinguishing gravitational response | UNRESOLVED |
| UNITY-001 P5 | Confirmatory physical prediction | NOT READY (unchanged) |

**Program decision:** Retain IST-001 as a conventional covariant memory-and-reservoir control with meaningful bounded algebraic checks. Suspend claims of an **additional EFMW-specific gravitational stress or detection** until source-faithful physical structure and independent discriminator conditions are met. Do not claim that IST-FAM-001 has been executed, that H1/H2 are true, or that physical gravity is unified.

## 11. Evidence, provenance and next permissible work

**No new run was performed for this review.** The original IST-001 report and its [24/24 GitHub CI result](https://github.com/enuminous/papers/actions/runs/42669567461) remain the relevant executed controls; [WITD-002](https://github.com/enuminous/papers/blob/main/WITD-002-Where-Does-the-Memorys-Energy-Go-2026-11-05.md) still carries its original two numerical refinement FAIL groups.

To proceed, first obtain explicit approval for **executing** the newly frozen two-hypothesis source audit, then issue an execution ledger preserving source coordinates and all negative results. Separately, develop a controlled continuum-bath spectral/Markov limit with independently stated physical assumptions, but do not use it as evidence of new gravity without discrimination.

### Primary references

1. [IST-001 main theoretical memorandum](IST-001-Deriving-Informational-Stress-from-Covariant-Memory-and-Reservoir-Models-2026-11-09.md).
2. [IST-001 executed report and reproducibility package](research/ist-001/IST001_REPORT.md).
3. [IST-FAM-001 frozen protocol, v1](research/ist-fam-001/PROTOCOL.json).
4. [UNITY-001 Phase 1 source provenance](research/unity-001/phase-1/PHASE1_REPORT.md).
5. [UNITY-001 Phase 5 synthetic identifiability](research/unity-001/phase-5/PHASE5_REPORT.md).
6. [WITD-002 energy accounting and representation obstruction](WITD-002-Where-Does-the-Memorys-Energy-Go-2026-11-05.md).
7. [Original IST-001 CI run](https://github.com/enuminous/papers/actions/runs/42669567461).

---

*The review is a record of corrections and narrower conclusions, not an endorsement of original physical claims. The scientific standard is not whether the new construction can be made to fit, but whether it survives a test that could have failed.*
