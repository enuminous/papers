# G3-001: Conditional Identifiability of an Injected Informational Source in the Geometry Field Lab

## Initial synthetic results with an independently measured ordinary-matter channel

**Matthew Chenoweth Wright**  
Monolithic LLC · Independent Research  
3 November 2026 · Results manuscript v1.0

**Status:** EXPLORATORY SYNTHETIC COMPUTATIONAL RESULT. The numerical experiment is reproducible from the specified source code and settings. It is not physical evidence of a new gravitational interaction, is not externally preregistered, and has not undergone independent peer review.

**Laboratory:** [Geometry Field Lab](https://enuminous.github.io/Geometry/)  
**Pinned source:** [enuminous/Geometry at 1aad91c00c40e61a1ebf979c68a353194d190348](https://github.com/enuminous/Geometry/tree/1aad91c00c40e61a1ebf979c68a353194d190348)  
**Reproducibility:** [Replay script](research/geometry-g3-001/replay.cjs) · [Machine-readable receipt](research/geometry-g3-001/receipt.json)  
**Methods companion:** [Geometry-Foundation-002](Geometry-Foundation-002-Interactive-Counterexample-Laboratory-ME006-ME007-2026-11-03.md)

---

## Abstract

The Einstein–Feynman–Maxwell–Wright (EFMW) research program proposes a possible informational contribution to gravitational source equations. Before claiming that such a contribution is physically distinct, an observer must be able to separate it from lawful ordinary-matter contributions. This report presents initial results from the Geometry Field Lab's synthetic identifiability mode. The simulator generates artificial observations from a known ordinary signal, a known informational template multiplied by an injected coefficient, and random noise. It compares a zero-coupling null against a regression that estimates the coefficient. Three observation assumptions are available: ordinary matter unrestricted, known exactly, or independently measured with noise.

The selected run used the separately measured ordinary-matter option; 400 observations per synthetic trace; injected coupling \(\kappa=-0.2\); source-noise standard deviation 0.84; matter-measurement noise standard deviation 0.15; initial seed 1597; and 190 distinct synthetic trials in each of three sets (null calibration, held-out null, and held-out injected). Its displayed single-trace estimate was \(\widehat\kappa=-0.28203235\). A 95th-percentile calibration cutoff of \(\Delta\mathrm{SSE}=2.37920009\) led to 14/190 (7.37%) false alerts on held-out null trials and 176/190 (92.63%) detections on held-out injected trials. The values were independently recomputed in Node.js from the lab's source-defined numerical functions in the local HTML artifact. The function block's fingerprint matches that of the pinned public version, although the complete local HTML and public HTML are not byte-identical.

**Finding:** A familiar template-fitting detector is effective for its *known injected pattern* in this particular artificial noise environment when the ordinary sector is constrained by a separate synthetic observation. Conversely, when ordinary matter is unrestricted, the zero-coupling source model can absorb the extra source exactly, so the coupling is not identifiable from total-source observations alone. This is a bounded positive computational finding paired with a structural negative control. It does **not** establish an observed EFMW-specific informational field. The physical discrimination gate remains **UNRESOLVED**.

**Keywords:** EFMW; source identifiability; synthetic detection; least squares; null controls; calibration; negative results; reproducibility.

## 1. Research question and distinction from physical validation

The proposed gravitational-source equation can be written schematically as

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G(T_{\mu\nu}+\kappa I_{\mu\nu}).
\tag{1}
\]

This experiment does not solve that equation, derive a gravitational observation, or calculate a tensor field from a physical spacetime. Instead it investigates a preliminary statistical question: if an observed total signal is written as \(S=T+\kappa I\), under what assumptions can an observer distinguish \(\kappa=0\) from a nonzero coefficient?

With no independent constraint on ordinary matter, define \(T'=T+\kappa I\). Then \(S=T'+0I\) is the same observation. No amount of total-source-only measurement can uniquely recover the split if such reallocations remain admissible. If ordinary matter is separately known or measured, however, an extra contribution may become *conditionally* identifiable.

The study tests this mathematical distinction in one deliberately favorable synthetic setting. It is not a test of whether nature contains the proposed EFMW source.

## 2. Parameters and exact signal generator

The user-selected displayed run has the following fixed-for-reproduction settings:

| Parameter | Value |
|---|---:|
| Matter-information regime | Independently measured, noisy ordinary matter |
| Injected coupling \(\kappa\) | \(-0.2\) |
| Source observation noise \(\sigma\) | 0.84 |
| Matter observation noise \(\sigma_T\) | 0.15 |
| Samples per synthetic trace | 400 |
| Deterministic seed | 1597 |
| Null calibration trials | 190 |
| Held-out null trials | 190 |
| Held-out injected trials | 190 |
| Cutoff quantile | 0.95 |

These were interactive choices, not an externally deposited preregistration. Reproducing them does not convert the selected run into a confirmatory physics experiment. The negative coefficient is simply a signed simulator parameter, not evidence for repulsive gravity or negative gravitational mass.

Let sample index \(j=0,\ldots,399\) and \(w_j=j/399\). The actual lab code defines the ordinary and extra-source templates:

\[
T_j=0.4+0.20\cos(0.085j)+0.12w_j,
\tag{2}
\]

\[
I_j=\sin(0.15j)+0.4\cos(0.035j)+0.13w_j.
\tag{3}
\]

The source and independently noisy ordinary-matter measurements are

\[
y_j=T_j+\kappa I_j+\sigma\varepsilon_j,\qquad
z_j=T_j+\sigma_T\eta_j,
\tag{4}
\]

where the code uses a seeded pseudorandom normal generator for the two noise streams. In this model, the fitting procedure knows the exact template \(I_j\) that generated the injection. This is appropriate for testing a matched-template detector and simultaneously a major restriction on what the result means.

The independent matter channel \(z_j\) is independently *noised synthetic data*; it is not a measurement of real mass, energy, pressure, stress-energy, or curvature.

## 3. Estimator and calibrated decision rule

In the chosen mode, the reference matter signal is \(T_j^{\rm ref}=z_j\). Define residuals \(e_j=y_j-z_j\), and estimate a single template coefficient using least squares:

\[
\widehat{\kappa}=
\frac{\sum_j I_je_j}{\sum_j I_j^2}.
\tag{5}
\]

The improvement over the zero-coupling fit is

\[
\Delta\mathrm{SSE}
=\mathrm{SSE}(\kappa=0)-\mathrm{SSE}(\widehat\kappa)
=\frac{(\sum_j I_je_j)^2}{\sum_j I_j^2}.
\tag{6}
\]

This statistic is *nonnegative by construction*. Allowing an extra fitted parameter can only maintain or improve the in-sample least-squares fit. A positive improvement alone therefore cannot establish an effect. The calibration null determines which improvement sizes are treated as unusual under this synthetic background.

For calibration trial \(q=0,\ldots,189\), source code chooses seeds of the form

\[
s_{\rm cal,q}=1597+1000003+7919q;
\]
\[
s_{\rm null,q}=1597+2000003+7919q;
\qquad
s_{\rm alt,q}=1597+3000003+7919q.
\tag{7}
\]

Each set is evaluated with the same signal design but distinct pseudorandom seeds. The null calibration cutoff is the zero-based sorted-index 179 element, from \(\lfloor(190-1)\cdot0.95\rfloor\). A holdout triggers when

\[
\Delta\mathrm{SSE}>\mathrm{cutoff}+10^{-15}.
\tag{8}
\]

Thus 95th-percentile calibration targets a low simulated null alarm incidence. It does not guarantee that any new holdout will produce exactly 5% false alarms, and it says nothing about a real instrument.

## 4. Reproduced results

### 4.1 Headline observations

| Output | Reproduced value |
|---|---:|
| True injected coefficient | \(-0.20000000\) |
| Single-trace estimated coefficient | \(-0.28203235\) |
| Single-trace estimation error | \(-0.08203235\) |
| Null SSE in displayed trace | 337.023658 |
| Fitted SSE in displayed trace | 317.547084 |
| Improvement \(\Delta\mathrm{SSE}\) in displayed trace | 19.476574 |
| Frozen-from-calibration cutoff | **2.37920009** |
| Null holdout alerts | **14 / 190** |
| Null holdout alert incidence | **7.3684%** |
| Injected holdout detections | **176 / 190** |
| Injected holdout detection incidence | **92.6316%** |

The one example's estimate differs from the injected value by about \(-0.082\), but a single noisy sample cannot establish the bias of the estimator. The event fractions are across 190 separate simulated traces per condition, each containing 400 time-indexed points. The 400 points are not 400 independent replications of a physical experiment.

The detection incidence exceeds the false-alarm incidence by about **85.26 percentage points** in the selected simulator. This is a strong descriptive separation of its artificial null and injected distributions, not an observed universal effect.

### 4.2 Sampling uncertainty

For an illustrative 95% Wilson binomial confidence interval, treating the simulated trial outcomes as independent Bernoulli units under the fixed source model:

| Event rate | Fraction | Approximate 95% Wilson interval |
|---|---:|---:|
| Null alert incidence | 14/190 = 7.37% | **4.44%–11.99%** |
| Injected detection incidence | 176/190 = 92.63% | **88.01%–95.56%** |

The null interval includes 5%, so the 7.37% observed incidence is not, by itself, strong evidence that the underlying simulator null rate exceeds 5%. The intervals quantify uncertainty **inside the selected simulator**, subject to its pseudorandom sampling assumptions. They are not predictive intervals for real gravitational instruments or independently generated physical processes.

For the source template used here, \(\sum_j I_j^2\) is approximately 244.86. Under the independent synthetic noise assumption, the variance of measured-mode residual noise is \(\sigma^2+\sigma_T^2=0.7281\). The nominal single-trace least-squares standard error is approximately

\[
\mathrm{SE}(\widehat\kappa)
\approx\sqrt{\frac{0.7281}{244.86}}\approx0.0545.
\tag{9}
\]

The observed single-trace estimation difference is approximately 1.5 times that model-based standard error. This does not imply any measurement uncertainty for an EFMW field in nature.

### 4.3 Negative control: unrestricted ordinary matter

Without independent constraints on \(T\), the alternative \(T'=T+\kappa I\) and \(\kappa'=0\) preserves the exact total source \(S\). This identity means source-only observations are **structurally non-identifying** for the split. The laboratory's free-matter mode accordingly does not provide a meaningful coupling estimate or calibrated detection rate; a default value of zero in that mode is a bookkeeping convention, not a 0%-sensitivity result.

The contrast with the measured-matter run is the scientific point: **detection depends on what the observer is allowed to know independently about ordinary matter**. In realistic physics, these assumptions must be justified by actual matter equations, separate measurements and uncertainty budgets—not set by a dropdown menu.

## 5. Source provenance and computational reproduction

The user's first record was the Geometry Lab's interactive display. The numerical output was recomputed using the lab-defined pseudorandom generator, trial generator, sorted quantile and identifiability functions under the specified parameters in Node.js v22.16.0. The local HTML copy was not byte-for-byte identical to the full public version: its Git blob SHA-1 was e3ef0571615ed6a591ccfa0275f6cdceb82065b2, whereas the pinned public HTML blob SHA-1 was b9aee1175be9a59ed4fd58c09be93a1c98529a9a. The **3,940-character numerical-function block** in both had matching 32-bit FNV fingerprint 7e47a10c, and the local replay produced the exact figures in Table 4.1. FNV is not a cryptographic source-identity guarantee.

For a stronger source-identity check, the archived [replay driver](research/geometry-g3-001/replay.cjs) expects the pinned public Git blob SHA-1 and checks numerical output against the specific result. The [machine-readable receipt](research/geometry-g3-001/receipt.json) records the selected parameters, counts and source-identity qualification. Anyone reproducing the result should use the pinned GitHub source with the default strict script mode rather than relying on a local variant.

This is **computational reproduction of a selected simulated outcome**, not third-party independent replication, a Lean theorem-checker run, or a measurement of actual gravitational effects.

## 6. Interpretation, limits, and the next falsifiable question

Two findings are supported:

**Computational detection.** Under a known, exactly matched injected template, a separate synthetic matter channel, and the selected artificial noise law, a standard regression-plus-cutoff procedure detects the injected coefficient in 176/190 holdout cases and flags 14/190 null cases. This establishes a working numerical example with an observable false-alarm/detection tradeoff.

**Structural ambiguity.** When matter is entirely free, the same total observations do not identify the coefficient. This is an exact model-reallocation argument, not a failure caused by too few samples.

Several conclusions are **not** supported. There is no real measured informational field, no independent derivation of the synthetic template from ME-006 or ME-007, no coupled Einstein–matter solution, and no demonstration that admissible zero-coupling gravitational physics cannot explain the same measurements. Nor is the regression procedure algorithmically new; matching a known template using least squares is a familiar operation.

This selected synthetic run was also not prospectively registered or chosen without seeing prior exploratory results. The same template family generates all calibration and holdout trials, restricting transfer even though their seeds differ. The independent-matter assumption is simulated, not obtained from a real measurement channel. The result cannot establish a universal detection rate, deployment readiness, or a new physical force.

The next experiment must therefore define a **physically derived, independently measurable observable** with dimensional units; specify the ordinary matter model and every relevant admissible \(\kappa=0\) alternative; fix nuisance parameter freedoms; then freeze the prediction, baseline and failure condition *before* accessing held-out external observations. A negative or degenerate result must be publishable. Merely increasing the simulator's detection percentage would not address the missing physics.

## 7. Conclusion

The first reported G3 identifiability simulation of Geometry Field Lab v0.2.0, using an independently noisy synthetic matter channel, produced **92.63% detection of injected toy-model signals** against **7.37% null alerts**, under 190 holdout traces per condition. The calibrated \(\Delta\mathrm{SSE}\) threshold was 2.37920009, and the single selected trace's estimated coupling was \(-0.28203235\) against the injected \(-0.2\).

This is an **important bounded initial computational finding** because it makes the role of independent ordinary-matter knowledge experimentally visible and provides a reproducible positive result alongside an exact negative control. It is not a physical detection. The strongest research obligation remains unchanged: find an observation that distinguishes an EFMW-specific contribution from admissible conventional physics, rather than a synthetic pattern chosen in advance by the experiment designer.

**Verdict:** **PASS** for reproducing the selected synthetic measured-matter result; **PASS** for the algebraic unrestricted-source non-identifiability condition; **UNRESOLVED** for a unique EFMW informational field and for G3 real-world physical discrimination.

---

## References

[1] Wright, M. C. (2026). [Geometry-Foundation-002: An Interactive Counterexample Laboratory for EFMW Source Identifiability and Conditional Conservation](Geometry-Foundation-002-Interactive-Counterexample-Laboratory-ME006-ME007-2026-11-03.md).

[2] Wright, M. C. (2026). [Geometry Field Lab, version-pinned source code](https://github.com/enuminous/Geometry/tree/1aad91c00c40e61a1ebf979c68a353194d190348).

[3] Wright, M. C. (2026). [EFMW's outstanding physical-identification obligations](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md).

[4] [Reproduction script](research/geometry-g3-001/replay.cjs) and [machine-readable results receipt](research/geometry-g3-001/receipt.json).

## Appendix A. Exact reproduction protocol

From a trusted pinned checkout of the Geometry repository, invoke the Node.js replay program saved in this Papers repository with the path to the checked-out source HTML:

    node research/geometry-g3-001/replay.cjs /path/to/Geometry/index.html

The driver refuses an unexpected source blob or numerical function fingerprint, evaluates the matching source-defined functions and checks the exact reported output numbers. An optional local-variant flag exists for the previously inspected HTML derivative but offers weaker source-identity assurance; the pinned public file is preferred.

Preserve the full commit ID, source blob, version of Node.js, commands, program output, any deviations, and the accompanying JSON receipt. Do not count the three synthetic groups as external independent experiments. No data should be added to or withdrawn from this report simply to improve the stated detection rate.

## Appendix B. Claim-to-evidence ledger

| Claim | Evidence | Status |
|---|---|---|
| Selected synthetic detection output reproduces | Exact numerical replay and recorded settings | PASS, bounded |
| Null and injected groups use separate seeded synthetic trials | Source generator and seed derivation | PASS, source-level |
| Nonzero \(\kappa\) is identifiable from totally unrestricted \(T+\kappa I\) | Counterexample \(T'=T+\kappa I\) | FAIL, under unrestricted premise |
| A source template is conditionally detectable when \(T\) is independently constrained | 176/190 injected detections, 14/190 null flags | PASS, synthetic only |
| Data contain independently measured physical ordinary matter | Synthetic ordinary-matter channel only | UNRESOLVED |
| A new field equation is verified by this experiment | No curved-space equation solved | UNRESOLVED |
| An actual measured observation distinguishes \(\kappa I\) from zero | No external physical observation | UNRESOLVED |

**Research disclosure:** This report and its reproducibility tools were prepared with AI assistance. The author is responsible for independently checking the code, statistical treatment, scientific interpretation and provenance before external submission. The document does not claim institutional validation, an awarded degree, or discovery of a new gravitational interaction.
