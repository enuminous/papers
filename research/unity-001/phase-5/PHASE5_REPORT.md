# UNITY-001 — Phase 5 Executed Identifiability Screen and Physical-Prediction Readiness

**Research program:** Matthew Chenoweth Wright / Monolithic LLC; AI-assisted technical implementation  
**Date:** 9 November 2026  
**Evidence disposition:** **BOUNDED IDENTIFIABILITY SCREEN PASS — PHYSICAL PREDICTION NOT CONFIRMATORY-READY**  
**Nature of result:** prospective, entirely **synthetic and dimensionless**. No real dataset, EFMW physical signal, registration, independent experimental reviewer, or experiment has been obtained.

**Inputs:** [Phase 1 source lock](../phase-1/sources.lock.json) · [Phase 2 open conflicts](../phase-2/conflicts.json) · [Phase 3 interface contracts](../phase-3/interfaces.json) · [Phase 4 dynamical checker](../phase-4/dynamics.py)  
**Frozen before execution:** [PROTOCOL.json](PROTOCOL.json) committed in [3bea0d0](https://github.com/enuminous/papers/commit/3bea0d0fb4c76c95a216541152a55a9877905774) before code, tests and analysis execution.  
**Reproduction:** [predict.py](predict.py) · [test_predict.py](test_predict.py) · [CI run 42633977283](https://github.com/enuminous/papers/actions/runs/42633977283) · [unmodified machine-generated CI artifact 13682645693](https://github.com/enuminous/papers/actions/runs/42633977283/artifacts/13682645693) · [execution receipt](EXECUTION.json).

## Executive finding

We can derive a **conditional, conventional weak-field observable** from a gravitational source model of the form \(T+\kappa I\), *provided* an admissible \(I\), a physical source interpretation, and a conventional-matter model are externally specified. We **cannot yet derive a novel EFMW-specific prediction** because the frozen corpus has not established that gravitational information density, its conserved dynamics, its independent physical calibration, or its distinguishability from ordinary matter.

An executed exact-rational identifiability study evaluates a deliberately hypothetical top-hat source using three predeclared conventional nuisance families. It finds positive conditional sensitivity under a **narrow** conventional baseline, zero sensitivity under a strong co-located conventional source, and severe loss of sensitivity under a nearly co-located source. This is the expected *obstruction*, not a discovery.

The core program decision is therefore **NOT READY FOR CONFIRMATORY PHYSICAL PREDICTION**. The project's next gate is an independently derived, source-pinned and physical-units-defined \(I_{\mu\nu}\) with a separately constrained matter sector—not a retrospective fit of \(\kappa\).

## 1. Conditional source-to-observable relation

The [pinned Geometry implementation](https://github.com/enuminous/Geometry/blob/285b95551ca11c487eb6c0c13f8dde86b702df71/Geometry.lean) defines a component-array source split \(S=T+\kappa I\), but no corresponding physical spacetime tensor. The [C1 effective action](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md) contains candidate metric stress, but has not established equivalence to the historical informational tensor. [WITD-002](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/DERIVATION.md) establishes conditional memory accounting while showing that a chosen \(I_{00}\) is generally not the physical storage energy for every field state.

**Only under additional hypothetical assumptions** that (i) the weak-field static slow-motion limit is valid; (ii) the \(\Lambda\) background can be treated separately; (iii) \(I^{00}/c^2\) corresponds to an independently derived admissible mass density \(\rho_I\) with correct units and conservation/exchange; (iv) \(\kappa\) is dimensionless under that normalization; and (v) the ordinary \(\rho_b\) is independently constrained, can one write

\[
\nabla^2\Phi=4\pi G(\rho_b+\kappa\rho_I),\qquad
a_r(r)=-\frac{G}{r^2}\left[M_b(<r)+\kappa M_I(<r)\right].
\tag{P5-1}
\]

This uses the conventional weak-field Poisson limit of Einstein gravity, **not** a new EFMW field equation. See [Carroll, *Spacetime and Geometry*, Einstein equation and Newtonian limit](https://www.astro.caltech.edu/~george/ay21/readings/carroll-gr-textbook.pdf). Pressure, anisotropic stresses, relativistic velocities, time dependence and photon propagation would require more than this approximation. Source conventions and units must be fixed before comparing to data.

If \(M_I(<r)\) is supplied *a priori*, its incremental response would be

\[
\Delta a_r(r)=-G\kappa\frac{M_I(<r)}{r^2}.
\tag{P5-2}
\]

**No frozen EFMW result supplies the physical \(M_I\).** The equation is a conditional prediction template, not an identifiable EFMW prediction.

## 2. Frozen hypothetical computation: no empirical data

The [frozen protocol](PROTOCOL.json) specifies an artificial spherical informational mass profile with radius \(R=4\), total mass \(M_I=1\), eight dimensionless radii \(r=1,\ldots,8\), and the normalized template

\[
s(r)=16\,\frac{M_I(<r)}{r^2},\qquad
M_I(<r)=\begin{cases}(r/4)^3&r\leq4,\\1&r>4.\end{cases}
\tag{P5-3}
\]

Its exact values at the eight synthetic radii are

\[
s=(1/4,\;1/2,\;3/4,\;1,\;16/25,\;4/9,\;16/49,\;1/4).
\]

The factor 16 is a numerical normalization **only**. No masses, accelerations, light curves, detector errors, or EFMW parameter values in the protocol represent actual physical quantities.

The synthetic linear response model is \(y=\kappa s+N\beta+\epsilon\), with an assumed independent equal-variance Gaussian noise scale \(\sigma=1/20\). **No random Gaussian observations were drawn.** The pseudo-data use a fixed, predeclared deterministic noise vector; their recovery checks are software controls, not a sampling-based significance test.

The exact-rational program computes the profile Fisher information via nuisance projection:

\[
I_{\kappa\mid\beta}
=\frac{s^{T}(I-P_N)s}{\sigma^2},\quad
P_N=N(N^TN)^{-1}N^T,
\quad
\sigma_\kappa=I_{\kappa\mid\beta}^{-1/2}
\tag{P5-4}
\]

when the nuisance Gram matrix is invertible and the residual signal has positive norm. The calculation explicitly returns \`UNIDENTIFIABLE\` if \(s\in\operatorname{col}(N)\). This rank condition is a *mathematical* criterion, not a guarantee that a physical source profile is true or detectable.

### 2.1 Three predetermined conventional model families

| Nuisance family | Precisely allowed ordinary-source/instrument templates | Executed implication |
|---|---|---|
| Narrow \(\mathcal N_0\) | \(1,1/r,1/r^2\) | \(s\) not in their span: nominal conditional Fisher positive |
| Strong \(\mathcal N_1\) | \(\mathcal N_0\) **plus the identical source profile \(s\)** | Exact degeneracy: \(I_{\kappa\mid\beta}=0\). A co-located *ordinary* mass can imitate all proposed \(I\) acceleration measurements |
| Near \(\mathcal N_2\) | \(\mathcal N_0\) plus \(s+(1/100)(r/8)\) | Almost degenerate; conditional information remains positive but too small for useful nominal sensitivity |

The strong \(\mathcal N_1\) alternative is deliberately serious: if the ordinary mass distribution is not independently measured or constrained, an unknown mass component with the candidate's own radial profile can absorb its entire effect. Excluding that alternative based only on the *same* gravitational response would be circular.

## 3. Executed results and reproducible diagnostics

GitHub Actions [run 42633977283](https://github.com/enuminous/papers/actions/runs/42633977283) completed successfully on Python 3.12 with **25 of 25 adversarial tests passing** and an archived [machine-generated result manifest](https://github.com/enuminous/papers/actions/runs/42633977283/artifacts/13682645693). All core projection and regression computations use exact \`Fraction\` arithmetic; the square root used to display a nominal standard-error scale is floating-point presentation only.

| Scenario | Profile Fisher information (toy) | Nominal \(\sigma_\kappa\) (toy) | Result |
|---|---:|---:|---|
| Narrow nuisance | ≈114.178 | ≈0.093586 | Conditionally identifiable |
| Co-located ordinary-mass nuisance | **0** | Undefined | **UNIDENTIFIABLE** |
| Nearly co-located nuisance | ≈0.000355 | ≈53.0824 | Extremely weak conditional information |

Under the near-degenerate alternative, the reported nominal uncertainty is **567.2× larger** than under the narrow baseline. This factor is an executed *synthetic-model* sensitivity result, not an experimental measurement.

For a locked synthetic injection \(\kappa_{\rm toy}=1/2\), the narrow nuisance model's deterministic pseudo-data give a fitted \(\widehat\kappa\approx0.511744\), versus \(\widehat\kappa\approx0.011744\) for the synthetic null. The exact difference in the fitted values equals the injected \(1/2\). The narrow fit crosses the protocol's **hypothetical** \(5\sigma_\kappa\approx0.46793\) threshold, while the null does not. This is **not a 5-sigma physical detection or a valid empirical false-alarm probability**; pseudo-data were constructed rather than observed, and a stronger admissible conventional model returns zero Fisher information.

The near alternative's nominal \(5\sigma_\kappa\) threshold is approximately **265.4** in the same arbitrary units, making the preset injection completely inadequate. Its fit coefficients are unstable under deterministic perturbations. The strong alternative makes a \(\kappa\) estimate mathematically nonunique, so no numerical detector result is valid under that family.

## 4. Claim-by-claim outcome ledger

The frozen prospective source audit yields **4 PASS, 1 FAIL, and 6 UNRESOLVED** across 11 precisely scoped findings:

| ID | Outcome | Meaning |
|---|---|---|
| P5-FWD-001 | **PASS** | Conditional spherical mass-to-acceleration template algebra; not an EFMW-supplied physical source |
| P5-NARROW-001 | **PASS** | Conditional Fisher information positive under restricted toy nuisance family |
| P5-NEAR-001 | **PASS** | Near-confounder destroys practical nominal sensitivity by more than 100-fold |
| P5-SYNTHETIC-001 | **PASS** | Exact-rational synthetic null/injection recovery check |
| P5-ROBUST-001 | **FAIL** | Claim of identification robust to an unconstrained co-located conventional mass is false: Fisher information zero |
| P5-EFMW-SOURCE | **UNRESOLVED** | No conserved calibrated and independently derived \(\rho_I\) from pinned corpus |
| P5-STRESS-CAUSAL | **UNRESOLVED** | Covariant stress, energy exchange, causal stability and physical admissibility incomplete |
| P5-MATTER-PRIOR | **UNRESOLVED** | Independent ordinary mass priors are unavailable |
| P5-OBSERVABLE | **UNRESOLVED** | No real instrument, physical units, covariance or justified sensitivity/power |
| P5-DATA-CUSTODY | **UNRESOLVED** | No permissioned external dataset or held-out evidence record |
| P5-CONFIRMATORY | **UNRESOLVED** | Independent reviews, approvals and physical preregistration absent |

A PASS on a toy rank or algebra condition never upgrades P5-EFMW-SOURCE or physical readiness. A FAIL on robustness does not refute all conceivable models of informational gravity; it exposes an admissible degeneracy any new model must rule out with *independent evidence*.

## 5. Why Phase 5 cannot yet claim a frozen physical prediction

A **frozen software/simulation design** is not the same as registering a quantitative prospective physical prediction. The required physical hypothesis still lacks:

1. A precise \(I_{\mu\nu}\) source with independent degrees of freedom, covariance, consistent energy/momentum accounting, and an Einstein-compatible stress term.
2. A uniquely computed \(\rho_I\), units, \(\kappa_I\) normalization and source parameter values **not fit from the target observations**.
3. A physical observable and complete forward instrument model, plus a source-independent ordinary-matter mass measurement/constraint.
4. Strong alternative nuisance families, error covariance, effect size, exclusion criteria, prospective data acquisition and formal power/sensitivity feasibility.
5. Recorded independent reviewer decisions, authorized data custody, a physical protocol amendment procedure and a prospective analysis lock.

Until these exist, the correct outcome is \`NOT_READY_FOR_CONFIRMATORY_PHYSICAL_PREDICTION\`. **Do not proceed to a confirmatory Phase 6 experiment by pretending the synthetic success is physical evidence.** Phase 6 protocol development can happen in parallel, clearly marked prospective.

## 6. Suggested minimal rescue experiment — an explicit design target

Choose one *independently measurable* matter distribution, one *mathematically defined and conserved* candidate \(I\), and one gravitational instrument. First measure or constrain the conventional matter source **without using the gravitational response that will test \(\kappa_I\)**. Then derive the full predicted response including measurement effects, calibration errors and competing material profiles. Freeze an error budget and null controls. Only if the residualized source vector remains identifiable under those independently justified alternatives should a blinded physical test be registered.

If every admissible ordinary source profile can imitate the candidate exactly, report non-identifiability in that observable domain. It is not a reason to fabricate a more favorable nuisance model, nor proof of a new fundamental coupling.

## 7. Publication and versioning

- Protocol source \`PROTOCOL.json\` predates compiler and CI.
- [Exact evaluator \`predict.py\`](predict.py) and [25 tests](test_predict.py) are dependency-free Python; reproduce with:

~~~bash
python3 -m unittest discover -s research/unity-001/phase-5 -p 'test_*.py' -v
python3 research/unity-001/phase-5/predict.py --out research/unity-001/phase-5/build/results.json
~~~

- [CI run](https://github.com/enuminous/papers/actions/runs/42633977283) and [artifact](https://github.com/enuminous/papers/actions/runs/42633977283/artifacts/13682645693) preserve the executed software record.
- The original MOC-001 **5/40 structural**, Phase 2 **9/717 typed**, Phase 3 **3/8** and Phase 4 **4/12** findings are not retuned or summed into an invented success score.

**Final Phase 5 finding:** a meaningful design obstruction has been quantified, and a conditional forward signal has been specified. **There is not yet an EFMW-specific, independently discriminating physical prediction to submit for confirmatory testing.**

**Physical UNITY status: UNRESOLVED.**
