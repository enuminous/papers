# EFMW and the Physical Cost of Recursive Computation

**A proposed hypothesis and falsifiable experimental framework**  
Version 0.1 · September 21, 2026  
Research context: Matthew Chenoweth Wright / Monolithic LLC  
Status: hypothesis proposal; no hardware anomaly demonstrated

## Abstract

Computation is a physical process. An experiment controlled entirely through software can therefore investigate physical behavior when its outcomes are measurements of the executing hardware. We propose testing whether the temporal organization captured by an EFMW residual-memory recurrence predicts a reproducible change in measured energy per update beyond a prespecified conventional hardware model. The proposal distinguishes mathematical properties of the recurrence, ordinary implementation effects, and a possible additional physical contribution. Existing support establishes an executable mechanism and the physical relevance of information processing; it does not establish the proposed additional contribution. A positive result would initially be a hardware anomaly or an improved empirical energy model. Evidence of new physics would require a stronger physical derivation and successful independent discriminating tests.

## 1. Full hypothesis

**Under controlled execution conditions, changing the temporal organization of an input sequence changes the accumulated state of an EFMW recurrence. We hypothesize that a prespecified measure of that state will predict an additional, reproducible component of energy per update that a frozen conventional hardware model does not account for, and that the relationship will predict held-out experimental conditions.**

This is a proposed phenomenological extension motivated by EFMW. It is not currently a theorem or a derived physical law of EFMW. Its coefficient, sign, magnitude, and transfer across hardware remain unknown.

Three claims must be distinguished:

1. **Mathematical claim:** the recurrence responds differently to persistent and alternating residuals. This follows from the equation.
2. **Experimental claim:** its state statistic predicts measured hardware energy beyond the chosen baseline model. This is untested.
3. **Physical-law claim:** the extra predictive relationship reflects physics absent from established descriptions. This is a further hypothesis; rejecting an incomplete hardware model would not establish it.

## 2. Defined system

The tested EFMW-FULL monitor uses

\[
r_t=y_t-(0.82y_{t-1}+u_t),\qquad
m_t=\lambda m_{t-1}+(1-\lambda)r_t,\qquad C_t=|m_t|,
\]

with \(\lambda=0.97\) and zero initial memory. For the first physical experiment, precomputed residual sequences should drive the update directly. This isolates the memory operation and avoids mixing the physical cost of the simulator with the cost under investigation. A subsequent experiment can include the full residual calculation.

Define a candidate dimensionless block statistic

\[
q_b=\frac{1}{Ns_r^2}\sum_{t=1}^{N}m_{b,t}^{2},
\]

where \(s_r>0\) is a fixed residual scale chosen from calibration data before confirmation, and each block contains the same number \(N\) of measured updates. Memory initialization, warm-up, block boundaries, and numeric representation must be identical or explicitly modeled.

This statistic measures normalized squared filter state. It is introduced here as an experimental design choice; it is not an established EFMW energy variable, quantum coherence measure, or thermodynamic entropy. Neither a large \(q_b\) nor a large \(C_t\) automatically means better control or greater efficiency.

## 3. Candidate measurement equation

Let \(e_b=E_b/N\) denote measured energy per update in joules per update. A proposed test model is

\[
e_b=g_h(z_b)+\beta_h q_b+\epsilon_b.
\]

Here \(h\) identifies hardware and execution configuration; \(g_h\) is a conventional baseline fixed using separate calibration data; \(z_b\) contains prespecified execution and environmental descriptors; and \(\epsilon_b\) represents measurement noise and unmodeled variation. Because \(q_b\) is dimensionless, \(\beta_h\) has units of joules per update.

The statistical null is \(\beta_h=0\), conditional on this model. The candidate alternative is \(\beta_h\ne0\), with improved prediction on untouched data. This is deliberately a two-sided hypothesis. No evidence currently determines whether the proposed contribution would increase or decrease energy.

A residual coefficient is not proof of an additional force, field, or energy source. It may absorb ordinary operand switching, thermal history, voltage management, or an inadequate baseline. The physically conventional null permits sequence-dependent energy use. It does not predict that reordered inputs consume identical energy.

Allowing arbitrary coefficients for every device would weaken the claim. An initial machine-specific study can establish feasibility, but cross-device confirmation must freeze a transfer rule or a stated shared qualitative prediction in advance. A universal coupling cannot be inferred merely by renaming several fitted coefficients.

## 4. Supporting evidence and its limits

| Evidence | What it supports | What it does not establish |
|---|---|---|
| Physical information erasure has measured thermodynamic costs [1] | Information processing is an appropriate subject for physical experiments | An additional energy term caused by EFMW |
| EFMW-FULL supplies an executable residual-memory monitor [3] | A specific reproducible mathematical target exists | A physical bridge from its state to joules |
| The NIGHTINGALE audit executed on 3,600 snapshots from 36 synthetic trajectories [4] | The monitor and audit can be run and inspected | A hardware-energy effect or independent physical validation |
| The one-step adapter exactly matched the published monitor in that audit [4] | Implementation fidelity on those trajectories | Correctness of a broader physical theory |
| Memory had approximately 15 times the first-order ALE amplitude of current residual in the reduced audit representation [4] | State history strongly shaped the score on that sampled distribution | A universal importance ratio, energy advantage, or causal result |
| Linux exposes energy counters on supported powercap/RAPL configurations [2] | Some machines permit energy observations through software | Universal sensor access, perfect accuracy, or per-instruction calorimetry |

Bérut and colleagues experimentally investigated erasing a one-bit memory and found dissipation approaching the Landauer bound in sufficiently slow erasure cycles [1]. This supports the physical-information premise. It does not supply the proposed coefficient or imply that ordinary CPU energy is determined solely by logical erasures.

The Landauer result is not an EFMW prediction. Under the relevant standard assumptions, the familiar bound is \(k_BT\ln2\) for erasing an initially unbiased bit. It is not a claim that every instruction dissipates that amount, nor a reason to expect this experiment to violate thermodynamics.

A negative finding from NIGHTINGALE is equally important: highly stable recursive branches appeared for an exactly linear signed update. Its raw local differences tracked quantile-bin widths, and correlated inputs carried that structure into deeper branches. Consequently, recursive branch stability is not supporting evidence for the additional physical term. It is evidence that the proposed physical experiment needs an independently specified endpoint and controls.

## 5. Predictions available before hardware measurements

For the fixed recurrence, the following are mathematical predictions:

| Input or operation | Predicted response |
|---|---|
| Constant residual \(b\), zero initialization | \(m_t=b(1-0.97^t)\) |
| Isolated residual followed by zeros | Its contribution decays by 0.97 per update; half-life approximately 22.76 updates |
| Alternating \(+b,-b\), after transients | Score approaches \(|b|(0.03/1.97)\), approximately \(0.01523|b|\) |
| Independent, zero-mean residuals of variance \(\sigma_r^2\) | Stationary signed-memory variance is \((0.03/1.97)\sigma_r^2\) |
| Negation of every residual, zero initialization | Memory changes sign; \(C_t\) and \(q_b\) remain unchanged |
| Mathematically equivalent EMA implementation | Same mathematical state trajectory, subject to numerical evaluation differences |

These are properties of an ordinary exponentially weighted signed average as well as of this EFMW implementation. Their confirmation would validate execution, not demonstrate novelty.

The proposed physical extension additionally predicts that, if the linear measurement equation is adequate, calibrated \(\beta_h\) predicts held-out energy contrasts through \(\Delta e-\Delta g_h=\beta_h\Delta q\). This prediction becomes numerical only after independent calibration and freezing of its coefficient and uncertainty. It is not currently an advance numerical prediction derived from EFMW physics.

## 6. Experiment and controls

Prepare equal-length sequences with exactly the same residual values and marginal distribution but different temporal arrangements: alternating signs, long same-sign runs, and fixed-seed random permutations. Precompute every arrangement outside the measured region. Use the same update kernel and sequential access pattern across these conditions. Prevent compiler removal of the computation with a checked final result.

Equal input multisets do not match the processor's switching behavior. Operand transitions, memory-state values, instruction dependencies, and floating-point corner cases remain conventional explanations requiring characterization. Additional surrogate sequences should match prespecified transition statistics while differing in longer-range organization where feasible. Inability to achieve adequate separation is an identifiability limitation, not a null discovery.

Include an independently written equivalent EMA implementation. Its purpose is to test implementation dependence, not to provide a physically non-EFMW mathematical process. If the proposed effect depends on the recurrence's state, equivalent physical realizations should obey whatever implementation-transfer relationship the hypothesis specifies; the code's name cannot be the cause.

Use sign-reversed sequence pairs as a diagnostic: the proposed \(q\)-dependent term is unchanged, while conventional bit-level energy may change. Model those ordinary differences rather than expecting raw measured energy to be identical.

Measure package-domain energy per update as the single primary endpoint on a supported device. Record elapsed time, frequency, initial temperature, relevant counters, and background activity for diagnostics. Account for counter wraparound, sensor update resolution, measurement overhead, warm-up, run order, and thermal carryover. Avoid confusing a whole-package reading with energy uniquely attributable to the tested loop.

Some counters may be consequences of the manipulation rather than independent confounders. Prespecify an unadjusted randomized energy contrast and a separate mechanistic prediction analysis. Do not interpret indiscriminate adjustment for post-treatment quantities as a causal estimate of new physics.

Randomize paired block order, balance conditions across sessions, and hide condition labels during quality screening. Repeat across days. Blocks and sessions, rather than individual updates, are the relevant units for uncertainty. Replication by a separate operator and device is necessary for a strong claim.

## 7. Decision rules, null outcomes, and falsifiability

Before confirmation, freeze the kernel, input sequences, statistic, hardware configuration, calibration procedure, conventional baseline, coefficient, exclusions, sample size, and analysis code. Determine sample size from pilot session-level variability and an explicit minimum effect \(\delta_{\min}\) in joules per update. This threshold expresses experimental sensitivity, not a theoretical EFMW prediction.

A proposed confirmation gate requires: a two-sided 99% interval excluding zero for the prespecified residual energy contrast; effect magnitude exceeding the frozen sensitivity threshold; agreement with calibration's held-out prediction within its frozen uncertainty; and successful independent replication under the declared transfer rule. Secondary endpoints cannot replace a failed primary endpoint after inspection. These are proposed design choices, not a universal discovery standard.

If a well-powered interval lies wholly within \([-\delta_{\min},+\delta_{\min}]\), the experiment excludes effects at or above that scale for the tested configuration. A wide interval is inconclusive. Since the current broad alternative permits arbitrarily small effects, it cannot be fully falsified by a finite-precision null; specifying a physically motivated lower bound or fixed coupling is a remaining obligation.

If an apparent effect vanishes under better conventional controls, reject the extra-term interpretation for that result. If the frozen equation fails on held-out sequences, reject that candidate equation in its tested domain. If all positive results require a new coefficient after every experimental change, the proposal has not demonstrated a predictive physical law.

## 8. What would justify a new-physics claim?

A positive first study would justify reporting a reproducible association or hardware anomaly. A stronger claim requires a bridge derived from EFMW to physical observables, with units, parameters, boundaries, and predictions that rival conventional accounts cannot reproduce. Independent instrumentation may eventually be necessary to exclude counter-specific artifacts; a software-only starting point does not guarantee software-only final validation.

No such bridge has yet been established in this proposal. The present evidence justifies a disciplined experiment and supplies a runnable target. It supplies no measured support for nonzero \(\beta_h\), no established energy saving, and no proof that ordinary physics is incomplete.

## References and provenance

[1] Bérut, A., et al. (2012). *Experimental verification of Landauer’s principle linking information and thermodynamics*. Nature 483, 187–189. DOI: 10.1038/nature10872. https://www.nature.com/articles/nature10872

[2] Linux kernel documentation. *Power Capping Framework*. Accessed September 21, 2026. https://docs.kernel.org/power/powercap/powercap.html

[3] EFMW-FULL, `monitors.py`, commit `6da1de09919b65f3b5caeeeb08038d740abc350b`. https://github.com/enuminous/EFMW-FULL/blob/6da1de09919b65f3b5caeeeb08038d740abc350b/monitors.py

[4] *NIGHTINGALE-EFMW-Audit.zip*, generated in this conversation on September 21, 2026. Includes source snapshots, REPORT.md, inputs.csv, effects.csv, checks.json, protocol.json, and reproduction scripts. NIGHTINGALE commit: `849c39363beafc3dac70430bf1f032e7f7ce1623`. This is a computational audit, not independent laboratory evidence.

**Provenance of the new proposal:** the statistic \(q_b\), added coefficient \(\beta_h\), measurement equation, and proposed confirmation gates were introduced in this draft. They must not be represented as previously published EFMW equations or previously observed effects.
