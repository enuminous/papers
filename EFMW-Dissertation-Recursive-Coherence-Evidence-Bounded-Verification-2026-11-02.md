# Recursive Coherence as a Falsifiable Principle
## Model-Based Early Warning, Formal Evidence Boundaries, and Identifiability in the Einstein–Feynman–Maxwell–Wright Research Program

**A dissertation-style research monograph and critical synthesis**

**Matthew Chenoweth Wright**  
Monolithic LLC · Independent Research  
**2 November 2026 · Version 1.0 · Public research draft**

**Status:** COMPLETE DOCUMENTARY DRAFT / NOT AN AWARDED OR SUBMITTED DISSERTATION / NOT PEER REVIEWED. This manuscript synthesizes already published experiments, mathematical constructions, formalization artifacts, limitations, and proposed studies. It does **not** claim that the author has completed a university doctoral program; that new experimental work was run specifically for this manuscript; or that an EFMW-specific fundamental law of physics has been demonstrated. The program remains an independent research program.

**Scientific integrity statement.** In this document *verified* means verified **to the expressly identified extent** (e.g., checked-in numerical output, successful CI compilation, or a documented analysis). It never silently means independently validated physics. Claims requiring additional evidence retain **UNRESOLVED** status. Experimental screening results are preserved whether favorable or unfavorable. AI assistance was used in research tooling and in preparation of this synthesis; the human author remains responsible for checking all assertions, sources, permissions, and any future academic submission.

---

## Abstract

The Einstein–Feynman–Maxwell–Wright (EFMW) program investigates recursive dynamics, mathematical physics, computational monitoring, and evidence-bounded technical review. Its broad physical ambitions are not yet supported by an independently discriminating observation of a new interaction or a completed derivation of established physical theories. A narrower, testable question is whether a recursive model-consistency statistic offers earlier warnings of a changing dynamical system at an acceptable false-alarm burden, and whether any observed advantage can be distinguished from familiar signal-processing operations. This dissertation-style synthesis examines that question using a frozen synthetic control-degradation sequence, formal verification artifacts, a biological transfer with a negative comparator result, and a structured methodology for reporting what is established and what remains unknown.

In EFMW-EXP-001, a signed residual-memory monitor met its prespecified synthetic warning-lead criterion: median paired gain 16.5 timesteps over an exponentially weighted average of absolute residuals in 40 confirmatory seeds (95% bootstrap interval 3.5–18.5). EXP-002 exposed a serious operational defect: the same thresholds produced sustained alerts in 82.5% of no-degradation traces, failing a 10% absolute false-alarm limit. EXP-003 recalibrated both monitors separately to an empirical 5% whole-run false-alarm budget. On distinct held-out traces, the signed-memory monitor had 2/80 null alerts rather than 6/80, actionable warnings in 77/80 degradation traces rather than 65/80, and a median paired warning-lead gain of 41.5 timesteps (95% bootstrap interval 37–47). All three experiments use the same synthetic generator, and their results are not field validation.

The crucial mathematical result is also a limitation: the implemented recurrence is an ordinary exponentially weighted average of **signed** residuals, followed by absolute value. The comparison changes both sign handling and memory coefficient; therefore the available improvement cannot be assigned to a new EFMW-specific physical or computational mechanism. A secondary analysis of real, publicly deposited cellular measurements likewise found that the selected EFMW-inspired memory feature was exactly reproducible by conventional exponential filtering, and it underperformed a training-selected conventional comparator. This manuscript derives these equivalences, explains the comparator problem, specifies new discriminating experiments without inventing their results, and separates software proof, simulation, secondary-data analysis, and physical interpretation.

The principal defended conclusion is methodological rather than cosmological: recursive-consistency proposals can be operationalized, audited, and falsified, but a distinctive EFMW contribution remains **UNRESOLVED** until it survives matched conventional controls, independent fault distributions, and preferably external operational evidence. A failed distinctive-mechanism test would not erase the value of the reproducible experimental and evidence-accounting methods; it would narrow their proper interpretation.

**Keywords:** EFMW; dynamical systems; early warning; residual monitoring; exponentially weighted moving average; change detection; false-alarm calibration; formal verification; identifiability; negative results; reproducibility.

---

## Contents

1. Introduction and thesis boundary  
2. Background and related work  
3. Mathematical definition and elementary results  
4. Research design, sources, and epistemic methodology  
5. The three frozen synthetic experiments  
6. Ablation, identifiability, and out-of-distribution behavior  
7. Formal methods, the Monolithic Zoo, and evidence semantics  
8. Transfers to measured systems and physical interpretation  
9. Prospective discriminating research program  
10. Discussion, limitations, and dissertation contributions  
11. Conclusion  
12. References  
13. Appendices A–J

---

# 1. Introduction and thesis boundary

## 1.1 The practical problem

Many physical, biological, computational, and industrial systems evolve under imperfect models. The observer has access to an observed state or measurements, a model's expected state, and an interval over which intervention would matter. A useful monitor must distinguish relevant deterioration from benign fluctuations early enough to inform action and infrequently enough that its alerts remain credible. Warning lead without a controlled false-alarm budget can be operationally meaningless; a low false-alarm count achieved by never alerting can be equally meaningless.

EFMW's computational research offers a candidate based on recursively updating discrepancies between a system's observations and its model. This candidate can be studied with ordinary mathematics and executable tests even while the physical interpretation of the larger EFMW program remains open. The key issue is not whether recursive state is conceivable, but whether the **specified transformation** of observations delivers information or utility that appropriate conventional comparators do not already provide.

The distinction matters scientifically and commercially. A reproducible result about a synthetic monitor is not a claim about a power plant, a clinical process, a cosmic field, or a customer's performance. A formal theorem about an encoded assumption is not a measurement that the assumption is realized in nature. An audit of a published model is not an endorsement of the model. These boundaries are methodological design requirements, not rhetorical disclaimers added after results are known.

## 1.2 Research questions

**RQ1 — Operational feasibility.** Does the published signed-memory monitor satisfy its previously frozen warning-lead and whole-run false-alarm screening criteria on the specified synthetic generator?

**RQ2 — Mechanistic identifiability.** Can its reported advantage be attributed to something other than the conventional choices to average signed rather than absolute residuals and to use a different decay coefficient?

**RQ3 — Transfer.** Does the useful effect generalize to independently generated fault mechanisms or measured external systems, with honest uncertainty about false alarms and missed warnings?

**RQ4 — Evidence governance.** Can mathematical, software, computational, and empirical claims be tracked without promoting a local check into an unsupported general conclusion?

**RQ5 — Physical meaning.** Does the tested monitoring statistic, or another precisely defined EFMW quantity, possess an independently identifiable physical observable or effect not already explained by appropriate established physics?

Answers are currently mixed: RQ1 is answered **yes, within the stated screens and generator**, with an important failure in the intervening specificity experiment; RQ2 is **not established**; RQ3 is **not established** for operational deployment; RQ4 has executable evidence-governance implementations but incomplete semantic coverage; RQ5 remains **UNRESOLVED**.

## 1.3 Hypotheses, with their logical scope

Define a specific fault-distribution family \(\mathcal F\), data-generation law \(\mathcal D\), monitoring horizon \(H\), and maximum admissible whole-run false-alarm incidence \(\alpha\). Let \(A\) be a candidate monitor and \(B\) a predeclared conventional comparator. A narrow empirical claim is

\[
H_{\mathrm{perf}}(\mathcal D,\mathcal F,\alpha):
\quad \operatorname{Med}_{i\in\mathcal F}
\left[L_i(A)-L_i(B)\right] > 0 ,
\]

subject to the same event definition and acceptable held-out null-alarm incidence for both methods. The median is taken over **paired differences** and is generally not the difference of two group medians.

A different and stronger claim is

\[
H_{\mathrm{distinct}}:\quad
\exists\ \mathcal D,\mathcal F
\text{ such that an explicitly new EFMW mechanism improves a
predeclared endpoint over all appropriately matched conventional
implementations of the same available information.}
\]

The existential form alone is weak if \(\mathcal D\) is selected after observing favorable results. A convincing version must predeclare the intended domain, comparator family, allocation of tuning budget, effect-size threshold, and a decision rule. At present, the tested recurrence itself is algebraically identical to a conventional signed exponential filter. **Without additional specified machinery, a distinct-mechanism claim for that recurrence is false by construction.** Any future distinctive claim must identify a genuinely different operation or demonstrate a newly justified explanatory use of a known operation, not rename its coefficients.

The dissertation therefore distinguishes *operational utility* from *mechanistic novelty*, and both from *new physics*.

## 1.4 Originality claim and non-claim

This draft does **not** claim priority for exponential smoothing, CUSUM, sequential testing, state observers, or formal theorem proving. Possible scholarly contributions are (i) a fully documented sequence of preregistered positive and negative screens, (ii) a careful explanation of how a favorable comparator result arose and how to test its provenance, (iii) a reproducible system of evidence statuses and dependency propagation, and (iv) falsification-focused integration of the monitoring and mathematical-physics research records. Their degree of academic novelty still requires review against literature more exhaustive than the bounded sources used here.

# 2. Background and related work

## 2.1 Statistical process monitoring preceded EFMW

Quality-control research has long examined residual accumulation, state change, and competing delay/false-alarm objectives. Page's continuous inspection schemes formalized cumulative monitoring [1]. Roberts studied geometrically weighted moving averages [2]. Lorden treated decision rules for detecting a distribution change under stopping-time loss [3]. Adams and MacKay described Bayesian online changepoint inference [4]. These methods and the larger literature on observer-based fault detection provide mandatory comparators, not incidental citations.

An exponentially weighted moving average is a stateful recursion. Calling a computation recursive cannot by itself distinguish it from this literature. Likewise, a statistic that remembers the sign of an innovation can be better at persistent mean drift while doing worse at changes of variance. A coherent dissertation must therefore place signal class and operating point ahead of overarching explanatory terminology.

## 2.2 Model-consistency and observer residuals

For a discrete plant, suppose that

\[
x_{t+1}=f(x_t,u_t,\eta_t),\qquad
y_t=h(x_t,\nu_t),
\]

where \(x_t\) is the latent state, \(u_t\) the input, \(y_t\) the measurement, and \(\eta_t,\nu_t\) disturbances. A predictor \(\widehat y_t\) is specified before the outcome at time \(t\), yielding a residual \(r_t=y_t-\widehat y_t\). Residuals can be tested for mean shifts, variance shifts, innovations inconsistent with an assumed distribution, or deviations in temporal dependence. Distinct mechanisms require different tests.

An EFMW-inspired *recursive coherence* score is operationally meaningful only once its input, update rule, threshold, alarm policy, and decision endpoint are specified. The word coherence is descriptive in this setting; it must not be confused with quantum coherence, phase coherence, entropy, or a new thermodynamic quantity without an explicit derivation.

## 2.3 Formal verification and experimental inference

Lean 4 provides a kernel-oriented environment for checking propositions under given definitions and assumptions [5]. Its correctness claim is conditional: if a formal statement expresses the intended property and accepted axioms hold, a valid proof establishes that formal statement. It does not verify that a physical interpretation is adequate, that a dataset was collected correctly, or that an unimplemented part of a pipeline works.

The FAIR principles [6] identify findability, accessibility, interoperability, and reusability of scientific artifacts. The EFMW archive's use of pinned versions, coverage records, source manifests, reproducibility scripts, and separate findings is aligned with reproducibility goals. It is not evidence of universal FAIR conformance or independent certification.

## 2.4 Relation to the rest of EFMW

The EFMW catalogue contains mathematical and physical hypotheses spanning field equations, informational stress, recursive state, and other models. The canonical frozen review explicitly separates 53 structural entries, 15 analytic models, one partial specialization, and 33 open analytic entries [7]. Those categories do not represent 102 experimentally established laws. This dissertation uses the mathematical and computational monitoring strand as its test case. A dedicated later chapter states what the physical strand has and has not established, without importing its ambitions as premises for the monitoring conclusions.

# 3. Mathematical definition and elementary results

## 3.1 The exact published monitoring equations

The public synthetic experiment uses the one-step residual

\[
r_t=y_t-\bigl(0.82y_{t-1}+u_t\bigr).
\]

Its baseline accumulates absolute residuals:

\[
b_t=0.90b_{t-1}+0.10|r_t|,
\qquad b_0=0.
\]

The candidate accumulates signed residuals and then takes magnitude:

\[
m_t=0.97m_{t-1}+0.03r_t,
\qquad c_t=|m_t|,
\qquad m_0=0.
\]

The precise simulator, initial indexing, alarm semantics, and source code—not a generalized drawing of a feedback system—define the tested object [8,9]. Unless separately stated, \(r_t,m_t,b_t,c_t\) have the same measurement units; the coefficients and normalized threshold ratios are dimensionless. These recurrences do not become field equations through notation alone.

## 3.2 Proposition 1: the signed memory is conventional EWMA

For any real sequence \(r_1,\ldots,r_t\), fixed \(0\le\lambda<1\), and \(m_0=0\),

\[
m_t=\lambda m_{t-1}+(1-\lambda)r_t
     =(1-\lambda)\sum_{j=1}^{t}\lambda^{\,t-j}r_j.
\]

**Proof.** The expression holds at \(t=1\). Multiplying the claimed sum at \(t-1\) by \(\lambda\), then adding \((1-\lambda)r_t\), gives the claim at \(t\). Induction completes the proof. \(\square\)

This elementary proof is given here in mathematical prose and is **not presented as a new Lean-checked theorem**. It establishes exact identity between the EFMW-labelled update and an ordinary signed exponential filter. An implementation using exactly the same equation, initialization, precision, and alarm policy must produce identical scores and alerts on exactly the same inputs. Accordingly, *no benchmark can distinguish those two labels as distinct algorithms*.

A legitimate claim may concern a particular application of this filter, an auditable integration, or a later non-equivalent extension. It may not concern an algebraically unique filter on the evidence above.

## 3.3 Proposition 2: sign placement changes the detector

For common decay \(\lambda\), compare

\[
C_t=\left|(1-\lambda)\sum_{j=1}^{t}\lambda^{t-j}r_j\right|
\]

with

\[
B_t=(1-\lambda)\sum_{j=1}^{t}\lambda^{t-j}|r_j|.
\]

By the triangle inequality, \(C_t\le B_t\) for all \(t\) with nonnegative weights, assuming zero initial states. Equality holds when there is no effective cancellation, including sequences whose nonzero residuals share one sign. A persistent signed shift can accumulate coherently; alternating innovations partially cancel.

This relation does not order two *separately calibrated* detectors' alert times. It demonstrates why comparing absolute-before-smoothing to absolute-after-smoothing changes the statistical question. A lower score can have a proportionately lower threshold when calibrated separately.

## 3.4 Proposition 3: behavior under idealized signal classes

For a constant residual \(r_t=a\) after initialization,

\[
m_t=a(1-\lambda^t)\longrightarrow a,\quad
c_t\longrightarrow |a|.
\]

For strictly alternating \(r_t=(-1)^t a\), the steady periodic signed state has magnitude

\[
|m|_{\mathrm{steady}}=|a|\frac{1-\lambda}{1+\lambda}.
\]

For \(\lambda=0.97\), this is approximately \(0.01523|a|\), while an average of \(|r_t|\) tends toward \(|a|\). Thus signed filtering strongly attenuates a symmetric alternating signal. This is conventional filter behavior, not a physical prediction.

For independent, mean-zero residuals with variance \(\sigma_r^2\), the stationary variance of signed memory is, when the assumptions apply,

\[
\mathrm{Var}(m_t)
=\frac{(1-\lambda)^2}{1-\lambda^2}\sigma_r^2
=\frac{1-\lambda}{1+\lambda}\sigma_r^2.
\]

The result follows by solving \(V=\lambda^2 V+(1-\lambda)^2\sigma_r^2\) in stationarity. For \(\lambda=0.97\), the variance factor is approximately \(0.01523\). Dependence, colored noise, unstable state prediction, or changes in mean invalidate use of this expression without additional terms.

**Consequences:** (i) a signed filter naturally favors persistent mean deviations; (ii) it can overlook mean-preserving variance changes; (iii) a claimed generic early-warning superiority requires distinct fault families and matched filters. These are mathematical predictions about the filter. None is a new force, field, or energy law.

## 3.5 Detection-time functionals

Let \(\tau\) be degradation onset, \(T_f\) the labeled simulated failure, \(s_t\) a score, \(\theta\) a threshold, and \(k=3\) the required consecutive exceedances. Define the alarm index as the first monitoring index at which the implementation identifies a run of three strictly suprathreshold samples. The exact convention—whether the alarm index marks the beginning or end of that run—is defined by the archived runner. The *first* alarm matters: accepting a later favorable alarm after a pre-onset false alert would overstate usefulness.

For a degradation trace, the published EXP-003 scoring sets an actionable indicator

\[
A=\mathbf 1\{\tau\le T_{\mathrm{alarm}}<T_f\}.
\]

Lead is \(L=T_f-T_{\mathrm{alarm}}\) if \(A=1\) and a fixed sentinel \(-999\) otherwise. The sentinel implements an explicit project decision rule, not a physical negative warning time. It makes the median sensitive to failure and pre-onset alarm counts and is not transferable without the scoring convention. A future study should report event incidence and conditional warning lead separately as well as the legacy composite statistic.

On no-degradation traces, whole-run false-alarm incidence is

\[
\mathrm{FAR}_{H}=
\Pr\{\text{at least one sustained alert within horizon }H\}.
\]

This is not the fraction of individual observations above threshold. Multiple-testing over time makes that distinction central.

# 4. Research design, sources, and epistemic methodology

## 4.1 A historical synthesis, not a new experimental run

Chapters 5–8 report public work completed before this manuscript. Reproduction statements identify *which* code and data were reported as rerun in their own published records. This drafting session did not execute all original code, rebuild all Lean packages, independently download all biological data, or rerun an operational benchmark. New mathematical deductions in Chapter 3 are elementary consequences of displayed equations. Proposed tests in Chapter 9 are prospective and must not be advertised as frozen or completed.

## 4.2 Source hierarchy

Evidence is interpreted under the following hierarchy:

1. A version-pinned executable and its data/analysis outputs support a **source-specific computational result**, subject to implementation and measurement limitations.
2. A kernel-checked theorem supports a **formal conditional statement**, subject to imported assumptions, proof dependencies, and adequacy of the statement.
3. An independently repeated run supports **reproducibility of the specified computational object**, not necessarily validity of its scientific interpretation.
4. A public measured dataset can support an **analysis of those data**; provenance, processing, sample dependence, and external validity must be assessed separately.
5. A simulator supports a **conditional synthetic finding**, not empirical deployment performance.
6. An unrun design is a **proposal**, not evidence.

The primary EFMW experiment sources and commands are cited at [8–12]; the canonical formal-review boundary is [7,13]; the measured-cell negative result is [14]; the broader physics research docket is [15]. A link to an adjacent repository is navigation, not proof of shared validity.

## 4.3 Four outcome classes

**PASS:** an actually performed and adequately evidenced check satisfied its *specific* prespecified criterion.

**FAIL:** an actually performed check did not satisfy its criterion or exposed a direct contradiction.

**UNRESOLVED:** evidence is missing, method incomplete, premise unsettled, or no adequate conclusion can be reached.

**N/A:** the check is genuinely inapplicable, with an affirmative reason and supporting evidence.

A pass on a test does not override a fail on a different test. N/A is not a synonym for unknown. Missing proof dependencies must remain visible. Confidence is not increased by counting an unchecked item as passed.

## 4.4 Threats to valid inference

The study keeps separate: selection of the generator, threshold fitting, monitoring equations, operating horizon, fault labels, baseline strength, hyperparameter search, per-seed dependence, missing alerts, multiple endpoints, and post-hoc interpretation. Reusing one generator in three stages creates replication of execution, not independent variation of the underlying synthetic mechanism.

The synthetic benchmark's criterion of a +10-timestep median advantage was selected for that protocol; it is not an industry response-time standard. The whole-run 5% calibration budget is a screen for the stated simulated horizon; it does not guarantee a 5% long-term false-alarm rate in the field.

# 5. The three frozen synthetic experiments

## 5.1 Simulator and evaluation setting

The documented source constructs 500-step traces with latent state \(x_t\), measurement \(y_t\), and control \(u_t\). In degradation runs, the onset is drawn from steps 140–199 and a nominal failure is assigned 120 steps later. The degradation variable grows after onset and perturbs the state transition, adds drift, and introduces a small oscillatory term. The published summary gives

\[
d_t=\mathrm{clip}((t-\tau)/120,0,1.25),\qquad u_t=-0.45x_t,
\]

\[
x_{t+1}=(0.82+0.08d_t)x_t+u_t+\eta_t
          +0.05d_t+0.012d_t\sin(0.18t),
\]

with process-noise standard deviation 0.035 and observation-noise standard deviation 0.02 in the specified synthetic generator [10]. The actual archived simulator governs numerical reproduction; the equation above is a readable summary. No physical units or real machine were assigned to this toy plant. The controller and monitor share model structure that could create favorable alignment between injected drift and the chosen residual.

## 5.2 EXP-001: predeclared warning lead

Calibration seeds: 101–120. Confirmatory seeds: 1001–1040 (40 traces). Frozen thresholds: baseline 0.0455502027202869 and signed-memory score 0.00834791535743751. The declared primary gate was median paired lead improvement of at least 10 timesteps.

The reconciled confirmatory run reports baseline median lead 59.0, candidate median lead 78.0, and **median paired gain +16.5** timesteps, bootstrap 95% interval [3.5, 18.5], Wilcoxon two-sided \(p=0.0039232744\) [8]. The medians need not subtract to the paired median. The candidate had 30 wins in 40 paired trials. Pointwise pre-onset exceedance fractions were approximately 5.13% baseline and 6.15% candidate; these values were **not** whole-run sustained false-alarm rates.

**Decision:** PASS for the prespecified synthetic lead criterion. NOT a demonstration that the candidate has tolerable sustained false alarms, is optimal among conventional detectors, or is independently validated outside its generator.

The reconciliation also identifies an older exploratory report's unsupported RMS-EWMA/CUSUM runtime and false-positive figures. Those are not canonical confirmatory results, and this document does not reuse them as verified findings.

## 5.3 EXP-002: specificity under no degradation

The next frozen screen kept EXP-001's equations and thresholds unchanged. It used 80 no-degradation seeds, 2001–2080, with an unmodified null condition and a paired benign observation-offset condition. The perturbation was \(+0.05\) during steps 220–231. A sustained alert meant three consecutive suprathreshold samples during the 480 monitored steps.

In both the stable and benign-pulse conditions, 66/80 (82.5%) candidate runs and 78/80 (97.5%) baseline runs generated sustained false alerts [9]. The candidate was 15 percentage points lower than baseline in these paired samples, but its absolute incidence exceeded the frozen 10% ceiling by 72.5 percentage points.

**Decision:** FAIL for the frozen absolute false-alarm criterion. The benign pulse did not change the aggregate alarm counts on these runs; the crucial issue was high null-alert incidence even without a fault. This failure must remain in a dissertation incorporating EXP-001.

## 5.4 EXP-003: whole-run false-alarm calibration

EXP-003 preserved the generator and scoring forms but changed the **operating-point calibration protocol**. Each monitor used 80 separate null traces, seeds 3001–3080. For every trace, the runner computed the maximum across all three-sample windows of the minimum score in that window. The 76th sorted trace maximum became the threshold under the strict greater-than rule, corresponding to 5% empirical calibration incidence. The thresholds were frozen before two disjoint evaluation sets: null seeds 4001–4080 and degradation seeds 5001–5080.

The resulting thresholds were baseline 0.0542015183 and signed-memory 0.0136069679. On held-out null traces, 6/80 (7.5%) baseline and 2/80 (2.5%) candidate runs alarmed. Actionable degradation warnings occurred in 65/80 (81.25%) and 77/80 (96.25%), respectively. Median paired gain across all 80 degradation runs using the frozen composite lead score was **+41.5 timesteps**, paired bootstrap 95% interval [37.0,47.0]. Detection discordances favored candidate (15 against 3; exact two-sided McNemar \(p=0.00754\)) [10,11].

The gate required at least +10 timesteps median paired gain, no more than 10% held-out null incidence for either monitor, and at least 60% candidate actionable detection. All three gates were met.

**Decision:** PASS for this exact synthetic screen. Because the monitors have different sign processing and different time constants, this result cannot identify a new recursion-specific mechanism. EXP-003 is a new protocol, not a repaired or retrospectively rewritten EXP-001 experiment.

## 5.5 Results together

| Experiment | Baseline / candidate null behavior | Detection / lead behavior | Predeclared outcome | Interpretation |
|---|---|---|---|---|
| EXP-001 | Pointwise pre-onset exceedances 5.13% / 6.15%; whole-run null not measured | Median leads 59 / 78; paired median gain +16.5, CI [3.5,18.5] | PASS | Defined synthetic lead comparison |
| EXP-002 | Stable null sustained alarm 97.5% / 82.5%; same aggregate rates in pulse condition | No degradation in either condition | FAIL | Thresholds inadequate for long-run alarm incidence |
| EXP-003 | Held-out whole-run null 7.5% / 2.5% | Actionable 81.25% / 96.25%; paired median gain +41.5, CI [37,47] | PASS | Separately calibrated synthetic operating point |

The correct cumulative scientific narrative is **positive lead finding → specificity failure → separately calibrated synthetic finding**, not three independent confirmations of one universal advantage.

# 6. Ablation, identifiability, and out-of-distribution behavior

## 6.1 Why the comparison is confounded

The originally named methods differ along **two independent design dimensions**:

1. Score construction: smooth \(|r_t|\) versus smooth signed \(r_t\) and apply absolute value afterward.
2. Decay coefficient: 0.90 versus 0.97.

Therefore a comparison between only these two endpoints cannot tell whether a lead gain arises from sign preservation, longer memory, their interaction, calibration details, or a distinct mechanism. In fact, the proposed EFMW score is exactly the signed-EWMA comparator with decay 0.97. Mathematical equivalence rules out claiming an algorithmic distinction between those expressions.

A minimally necessary 2×2 factorial comparison is:

| Arm | Input before smoothing | Decay | Score |
|---|---|---:|---|
| A | \(|r_t|\) | 0.90 | conventional absolute EWMA |
| B | \(r_t\) | 0.90 | absolute value of conventional signed EWMA |
| C | \(|r_t|\) | 0.97 | conventional absolute EWMA |
| D | \(r_t\) | 0.97 | published EFMW-labelled signed-memory score |

All arms require identical trace splits, three-sample sustained-alert policy, independent threshold calibration to a shared whole-run alarm budget, and a predeclared primary comparison. The historical EXT-003 output compares A and D. It does not, alone, establish the causal contribution of either factor.

## 6.2 External technical challenge: disclosure boundary

A subsequent **privately communicated technical review** reported that a conventional signed-residual arm captured much of the gain in the mean-drift generator, and that an independently constructed zero-mean variance-fault variant reversed the direction of advantage. Because the review's complete driver, logs, release permission, and independent reproduction have not been established in this public manuscript, its private correspondence, reviewer identity, and numerical claims are **not reproduced here as published experimental evidence**. Its role is to motivate publicly reproducible controls, not to add an unverified result row to Table 5.1.

**Status:** UNRESOLVED pending a permission-cleared, independently reproducible artifact. The fact that this challenge is not yet a public experiment is itself a limitation on the current mechanistic interpretation.

## 6.3 Stronger baseline families

A rigorous comparator set should include: (i) ordinary signed EWMA at matched decay; (ii) absolute EWMA at matched decay; (iii) matched-decay two-sided CUSUM; (iv) an innovation likelihood or generalized likelihood-ratio detector appropriate to the declared noise model; (v) a variance-sensitive statistic; and (vi) one changepoint model trained exclusively on calibration partitions. The full set must be fixed or governed by a separate development/evaluation split. Adding sophisticated comparators only when they favor the candidate, or omitting them when they do not, invalidates selection.

Memory or runtime budgets must be fair. It is illegitimate to permit one monitor a longer lookback, tuned threshold, or richer fault prior and then call its advantage distinctive. Comparators may have different mathematical assumptions, but those assumptions must be recorded and suitable for the target fault.

## 6.4 Identifiability theorem for the implemented recurrence

Let \(F_{\lambda}\) be the mapping from an input residual stream to the complete score stream

\[
F_\lambda(r_{1:T})=
\left(\left|(1-\lambda)\sum_{j=1}^{t}
\lambda^{t-j}r_j\right|\right)_{t=1}^{T}.
\]

If algorithm \(E\), designated EFMW, and algorithm \(S\), designated signed EWMA, both compute \(F_\lambda\) with the same initialization and numeric precision, then \(E(r)=S(r)\) for every input sequence. If their alarm rules are also equal, then their alert times and any score-derived performance measure are equal.

**Proof.** Equality of update functions and initial conditions gives equality by induction at every time. The alarm function receives equal score sequences and thus returns equal alerts. \(\square\)

This is an identity argument, not a statistical null awaiting a large enough dataset. Under the stated definition, there is no possible dataset on which EFMW-labelled \(F_\lambda\) systematically outperforms the identical signed EWMA as an algorithm. A future claim of distinctive performance must therefore refer to **additional explicitly specified features**, not this recurrence alone.

## 6.5 Distribution shift and failure mode mapping

A serious test matrix separates at least: persistent mean drift; variance inflation without mean shift; slowly evolving variance; autocorrelation or colored-noise change; temporary benign offsets; observation dropout; gain or calibration change; control-policy change; model misspecification; abrupt reset; and adversarial correlated disturbances. Each fault class needs a rationale, scope of expected detectability, and null counterpart. Equal weighting should be declared or derived from a real use case—not silently adjusted to reward the favored detector.

For each class, report detection incidence, false-alarm incidence, conditional lead-time distribution, time-to-first-alert, and effect-size uncertainty. Include catastrophic failure modes, not only median improvements. For a deployed system, an early but false warning can have financial and safety costs that a toy score does not represent.

# 7. Formal methods, the Monolithic Zoo, and evidence semantics

## 7.1 Frozen formal scope

The EFMW review entry identifies a canonical frozen target:

**Repository:** enuminous/Monolithic-102-Zoo-Lean4  
**Review tag:** efmw-review-2026-10-25  
**Commit:** 01f51acb0b0e564105dcf7f14cc55998d41b91ce.

The review entry reports a structural Lean root using Lean 4.19.0 without Mathlib and an analytic package using Lean 4.28.0 with pinned Mathlib revision 8f9d9cff6bd728b17a24e163c9402775d9e6a365. The source describes a reproducible review script, source manifests, coverage file, obligation ledger, and a successful frozen-source CI run [7]. Those records support **a reproducible formally checked subset**; the present manuscript did not independently execute the entire suite.

Of the 102 frozen entries, 53 are structural encodings, 15 analytic models, one a partial specialization, and 33 open analytic entries. The flat Minkowski ME-003 specialization does not discharge the curved covariant obligation. More theorem declarations after that snapshot must be evaluated at their own commits.

## 7.2 The Zoo as a bounded checker

A related frozen Zoo package defines 46 operational checks and selected Lean models; it is not the entire heterogeneous research corpus nor an end-to-end translation of all upstream Python pipelines [13]. Seventeen modules implement rank aggregation from supplied columns rather than upstream feature extraction and training. Its documented reference runner passed 90 selected regression comparisons on a published CI run. This is meaningful engineering evidence and a limited coverage claim—not a theorem that the 46 operations detect all scientific errors.

Later Zoo names and additional experiments exist elsewhere in the program. They are not silently counted as part of the frozen 46-operation formal coverage.

## 7.3 Four-state propagation and non-vacuity

The separate Zoo limiter outputs PASS, FAIL, UNRESOLVED, or N/A for every frozen operation. It enforces an explicit full inventory and carries dependencies, omissions, mandatory checks, and policy thresholds. A reported PASS requires an observed basis and evidence; a missing required item is not converted to N/A. A failure cannot be averaged away. A dependent finding cannot be established if a required ancestor fails or remains unresolved [16].

A key limitation is equally important: the checker can enforce rules over the **supplied** inventory; it cannot, without a separate completeness argument, discover every premise omitted by its author. A mathematically vacuous theorem can be perfectly proved in Lean. An executable coverage policy can be satisfied by an inappropriately scoped set of obligations. Both problems require adversarial specification review.

The alternative limiter's output for an incomplete ME-007 example reports 46 UNRESOLVED operations; it is not proof that 46 substantive audits were performed on ME-007.

## 7.4 A formal claim/evidence relation

A proposed abstract record is

\[
\mathsf{Claim}=(P,v,A,S,D,E),
\]

where \(P\) is a proposition, \(v\) a frozen target version, \(A\) explicit assumptions, \(S\) the intended interpretation or scope, \(D\) dependencies, and \(E\) evidence references. Define a check-specific judgment

\[
\Gamma\vdash_{v,\mathcal M}
P:\{\mathrm{PASS,FAIL,UNRESOLVED,N/A}\}.
\]

Here \(\Gamma\) records premises and \(\mathcal M\) the performed method. It is **not** a new proof calculus in which a PASS label entails truth. A useful minimum discipline is:

- Evidence must link to the exact target, not an adjacent release.
- The specification must not become true merely by including a tautological escape clause.
- Every discharged dependency must have a traceable basis.
- Failure and unresolved states cannot be rewritten as pass by administrative policy.
- A proof statement must be compared to the original ordinary-language claim.
- A physical inference requires physical data and an identifiable observable, not just a derivable formula.

This is a proposed semantics for scientific reporting, not a demonstrated complete formal epistemology.

# 8. Transfers to measured systems and physical interpretation

## 8.1 A biological transfer supplies a direct negative result

The published EFMW-BIO-001 secondary analysis used publicly deposited single-cell ERK-signaling and nuclear readout measurements, with 71,459 cells in the downloaded tables and 70,987 retained by a frozen completeness rule, spread across three experimental replicates [14]. The tested candidate appended a fixed signed-memory feature to simpler trace summaries to predict log nuclear Fra-1 intensity.

The primary error decreased from 0.03040942 (ablation) to 0.02930860 (candidate), a 3.62% relative improvement against the weaker feature set. The conventionally selected comparator achieved 0.02896365, 1.19% lower error than the candidate. An independently implemented ordinary EWMA reproduced candidate predictions to floating-point precision. The candidate failed its prespecified practical advantage gate and had higher aggregate error than the selected comparator on seven secondary readouts.

**Conclusion:** adding temporal information can help a weak model, but the chosen recurrence offered no demonstrated EFMW-specific improvement on this measured dataset. This was a secondary analysis of existing experiments, not newly acquired laboratory measurements. Source-data normalization across replicates, only three independent replicates, unequal feature counts among some alternatives, and one cell line limit generalization.

This result is valuable precisely because it shows an apparent local benefit disappearing when the appropriate conventional comparator is used.

## 8.2 Another identifiability lesson: bubble memory

EFMW-RP-001 modeled a pressure-driven bubble with a phenomenological relaxation-memory term [17]. In its frozen synthetic benchmark, the detection rule identified the injected effect in 223/250 positive trials (89.2%) and none of 250 null trials. The prespecified positive-detection target was 90%, so that gate **failed**. More importantly, the study derived a conventional Maxwell-viscoelastic counterpart capable of generating the same modeled response. Even a stronger detection rate would not by itself identify a unique EFMW mechanism.

The analogy with the monitoring recurrence is exact at the level of research logic: detecting a mathematical feature is not the same as discovering a novel cause if an established model produces the same observations.

## 8.3 Physical field equations: necessary but insufficient conditions

The broader EFMW program includes a schematic modified gravitational equation,

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G\bigl(T_{\mu\nu}+\kappa I_{\mu\nu}\bigr),
\]

where \(I_{\mu\nu}\) is proposed as an informational or recursive contribution. This expression is a candidate model, not experimentally established physics. For constant \(\kappa\), the contracted Bianchi identity requires an appropriate covariant conservation relation for the **total** source:

\[
\nabla^\mu(T_{\mu\nu}+\kappa I_{\mu\nu})=0.
\]

This necessity does not prove that a proposed \(I_{\mu\nu}\) exists uniquely, is independently observable, or is realized in nature. If \(\kappa\) varies, derivative terms must be treated explicitly. Dimensional agreement requires that \(\kappa I_{\mu\nu}\) share the units of stress-energy. Boundary conditions, coupling conventions, and matter equations must be declared.

Even when a total tensor \(S_{\mu\nu}=T_{\mu\nu}+\kappa I_{\mu\nu}\) is conserved, a split into its terms is generally nonunique without an independently fixed interpretation. For constant nonzero \(\kappa\) and any allowed symmetric tensor \(J_{\mu\nu}\), the transformation

\[
T'_{\mu\nu}=T_{\mu\nu}+\kappa J_{\mu\nu},
\qquad I'_{\mu\nu}=I_{\mu\nu}-J_{\mu\nu}
\]

leaves \(T'+\kappa I'=T+\kappa I\) unchanged. This elementary degeneracy illustrates why formal conservation alone does not identify the informational term. A published two-scalar correspondence model makes a related nonuniqueness explicit [18]. This is *an illustrative mathematical argument*, not a classification of all possible physical EFMW theories.

## 8.4 Explicit open physics obligations

The canonical review lists at least these unresolved obligations [7]:

- ME-007-BIANCHI: specify the informational stress tensor and show noncircular compatibility with total-source conservation.
- ME-003-COVARIANT: extend the stated flat specialization to a specified curved covariant wave operator.
- ANALYTIC-33: supply explicit analytic semantics and proof scopes for 33 open entries.
- PHYSICAL-ID: define observables, symbols, dimensions, boundary conditions, and established-theory limits.
- NULL-2026-09-02: recover historical ablation artifacts and rerun the randomized coefficient null.
- META-INTERPRETATION: demonstrate a noncircular and suitably nontrivial interpretation into a specified target theory.

The separate Monolithic-23 physical falsification docket is a **proposal**, not 23 completed independent experiments [15]. This dissertation does not claim EFMW has derived the Standard Model, reproduced quantum gravity, discovered residual universal rotation, or experimentally established an informational stress-energy field.

# 9. Prospective discriminating research program

**Everything in this chapter is proposed future work. None of its acceptance criteria is retrospectively imposed on EXP-001, EXP-002, or EXP-003, and no results are invented.**

## 9.1 Research stage A: exact algorithm inventory

Freeze a table of every proposed EFMW monitor variant with source hashes, initialization, residual model, parameter values, feature inputs, state dimension, numeric precision, and alarm rule. Require at least one explicitly non-equivalent operation if a distinctive algorithmic contribution is claimed. Document which variants are identical to standard EWMA, observer residuals, or known sequential tests.

**Gate A:** if no non-equivalent operation exists, classify a new-mechanism claim as FAIL or withdraw it. An application-level benchmarking or software assurance dissertation may proceed without claiming a new filter.

## 9.2 Research stage B: matched 2×2 ablation

Run the four-arm design in §6.1. Match calibration and holdout splits, expected alert burden, execution budget, and warmup. Use the existing generator first as a reproducibility bridge, **but do not call that re-analysis an independent confirmation**. Measure the effects of sign processing and decay and their interaction with a prespecified primary endpoint.

**Gate B:** distinguish a mechanism effect from sign/timescale effects. For the exact published \(F_{0.97}\), the signed-EWMA comparator is identical by definition, so no unique-algorithm effect is possible.

## 9.3 Research stage C: generator diversity

Introduce independently written generators for mean drift, variance drift, correlated noise, sensor offsets, observation missingness, and control-policy change. An external party should select or implement at least some faults after candidate code is frozen. Retain null traces and pre-onset monitoring for every condition. Use calibration-only parameter selection and completely untouched final holdouts.

**Gate C:** require no prespecified catastrophic degradation on safety-relevant faults. If a detector is intentionally restricted to mean drift, say so explicitly and do not demand general superiority.

## 9.4 Research stage D: external measured data

Choose a public operational time series with defensible event labels, acquisition provenance, and a real intervention decision. A measured dataset should allow incident-level false alarm, latency, missing-data and utility calculations. Avoid retrofitting event labels after observing alarms. If no suitable real dataset exists, report the limitation rather than substituting another convenient synthetic generator.

**Gate D:** no deployment suitability or industry generalization without out-of-sample evidence and a domain-specific consequences model. No live safety-critical intervention should be based on the pilot without appropriate independent review and safety controls.

## 9.5 Research stage E: independent reproduction

Package exact source commits, toolchain versions, locked dependencies, integrity manifests, immutable input data, split keys, a single build-and-run recipe, and machine-readable outputs. Record reviewer independence and deviations. A replicator should attempt to reproduce failure cases, not merely confirm a headline number.

**Gate E:** distinguish verified reproduction of code and outputs from confirmation of scientific validity. An independent challenge that shows equivalence to a simpler method must be retained as a substantive result.

## 9.6 Statistical analysis and error discipline

For a predeclared primary outcome, use paired seed/run units for synthetic comparisons and appropriately clustered units for replicated measured experiments. Report paired uncertainty intervals, incidence uncertainty, and effect sizes. Do not treat repeated time points within a single trajectory as independent experiments. A Wilcoxon or McNemar \(p\)-value answers a specific null under its assumptions; it does not measure the probability that a broad theory is true.

Prefer a hierarchical or stratified design when comparing fault families, with family-level results and sensitivity analyses. Prespecify a multiple-comparison approach or a hierarchical primary/secondary structure. Use a separate development split for comparator and hyperparameter selection, a calibration split for operating thresholds, and a sealed final evaluation split. Record all exclusions and all attempted models. Avoid equating statistical detection with practical value: cost of an unnecessary intervention, missed fault, and operator fatigue belong in the deployment criterion.

## 9.7 Physical-stage interface

A physical application requires a bridge from an EFMW mathematical object to dimensionally specified observables and a prediction distinguishable from conventional theory with comparable flexibility. If such a bridge is absent, the result remains mathematical or computational. If a physical candidate simply rewrites an established action or constitutive model, demonstrate what is gained in prediction, constraint, simplicity, or scope without claiming a newly observed fundamental interaction.

# 10. Discussion, limitations, and dissertation contributions

## 10.1 What the positive results actually teach

EXP-001 shows that the predeclared candidate outperformed its chosen residual baseline on the specified synthetic mean-drift task under original thresholding. EXP-003 shows that the advantage persisted after recalibration to an operationally more appropriate whole-run false-alarm budget. These are real source-specific findings and are not nullified by refusing a sweeping interpretation. They motivate further testing of signed innovation smoothing and its use in a well-defined review workflow.

Yet neither experiment tests the candidate against the **identical signed exponential smoother**. The operational gain cannot be attributed to an algorithmically new recurrence. A dissertation that says so explicitly is more defensible than one that equates a favorable label with a new physical principle.

## 10.2 What the negative results teach

EXP-002 shows that pointwise exceedance rates can conceal intolerable long-horizon alarm incidence. The biological transfer shows that a feature improving a restricted ablation can fail against a suitable conventional comparator. The bubble study shows that even successful detection may not identify a particular origin, and it narrowly missed its own declared positive-detection criterion. The formal ledger shows how conditional proof, missing assumptions, and omitted obligations are distinct kinds of incomplete knowledge.

Together these findings suggest a common methodological thesis: **evaluation must test a claim's causal or mathematical attribution, not merely whether a selected procedure produces a favorable output.**

## 10.3 Unresolved originality

The paper's clearest original contribution may ultimately be the structured synthesis of verification, calibrated screening, ablation, and explicit negative evidence across a bounded corpus. Whether the particular framework for evidence dependency or testing discipline constitutes doctoral-level novelty requires independent comparison with existing formal methods and assurance-case research. Neither 102 equation entries nor 46 recorded audit operations is by itself a measure of independent theoretical content.

## 10.4 Principal limitations

1. The three control-monitor experiments share a single simulator and parts of a common model assumption.
2. Their candidate is a familiar signed exponential filter; some baselines are intentionally weaker on persistent signed mean drift.
3. Source-specific confidence intervals and \(p\)-values do not establish external or mechanistic validity.
4. The legacy \(-999\) lead sentinel mixes failures and warning timeliness into one ranking score.
5. The exact public status of some subsequent external ablation artifacts is unresolved; private correspondence is not treated as a public source.
6. The measured-cell transfer has only three experimental replicates and upstream cross-replicate normalization.
7. The formal corpus covers selected encodings and operations, not every physical meaning or source pipeline.
8. The physical theory has outstanding conservation, identifiability, semantics, and independent-observation obligations.
9. This document is a synthesis rather than a new full replication and has not undergone external dissertation examination.
10. Independent priority and novelty checks against the complete literature remain to be done.

## 10.5 Why this matters for independent technical review

A bounded reviewer can freeze a claim and a target revision, reconstruct an author's asserted proof or result, compare with simple competing explanations, and deliver a traceable finding without selling a predetermined conclusion. EFMW's evidence discipline can be useful in such work even if its candidate physics is not validated. Technical-review service viability, however, requires separate commercial evidence; publication of this manuscript is not proof of a paying customer, market demand, or certified audit capability.

# 11. Conclusion

The defensible nucleus of EFMW, as assessed in this manuscript, is **a falsification-first mathematical and computational research program**, not a demonstrated new fundamental physical theory. Its current synthetic monitoring record contains two bounded passes and a consequential failure. Its memory update is mathematically equivalent to an ordinary signed EWMA, while the principal published baseline averages absolute innovations at a different decay. Its promising early-warning differences therefore cannot presently establish a uniquely EFMW-specific monitoring mechanism. A measured biological transfer produced a valuable negative comparator result; other laboratory models underscore identifiability limits. Formal checks and evidence ledgers strengthen reproducibility while leaving open obligations explicit.

The most decisive next scientific act is to perform and independently archive matched-filter, fault-family, and external-data controls. If an additional specified EFMW mechanism survives, the thesis can become a stronger empirical claim. If it does not, a rigorous dissertation remains possible about the limits of attribution, benchmark design, and evidence-bounded verification.

**Final research verdict, 2 November 2026**

| Proposition | Status |
|---|---|
| Frozen EXP-001 primary synthetic lead criterion met | **PASS (bounded)** |
| EXP-002 absolute null-alarm requirement met | **FAIL** |
| Frozen EXP-003 matched whole-run synthetic screen met | **PASS (bounded)** |
| Published \(0.97m+0.03r\) update differs algorithmically from signed EWMA | **FAIL (exact equivalence)** |
| A distinct additional EFMW detection mechanism is established | **UNRESOLVED / not demonstrated** |
| General operational reliability or real-world deployment suitability | **UNRESOLVED** |
| Selected formal code compiles and passes stated checks at pinned scope | **PASS for documented coverage; not comprehensive** |
| A new universal EFMW physical interaction is independently observed | **UNRESOLVED / not demonstrated** |
| This document represents a completed, awarded university dissertation | **NO — research draft** |

---

# 12. References

## 12.1 Foundational and methodological literature

[1] Page, E. S. (1954). “Continuous Inspection Schemes.” *Biometrika*, 41(1–2), 100–115. https://doi.org/10.1093/biomet/41.1-2.100

[2] Roberts, S. W. (1959). “Control Chart Tests Based on Geometric Moving Averages.” *Technometrics*, 1(3), 239–250. https://doi.org/10.1080/00401706.1959.10489860

[3] Lorden, G. (1971). “Procedures for Reacting to a Change in Distribution.” *The Annals of Mathematical Statistics*. https://authors.library.caltech.edu/records/n9ryc-0sr08

[4] Adams, R. P., and MacKay, D. J. C. (2007). “Bayesian Online Changepoint Detection.” arXiv:0710.3742. https://arxiv.org/abs/0710.3742

[5] de Moura, L., and Ullrich, S. (2021). “The Lean 4 Theorem Prover and Programming Language.” *CADE 28*, 625–635. https://doi.org/10.1007/978-3-030-79876-5_37

[6] Wilkinson, M. D., et al. (2016). “The FAIR Guiding Principles for Scientific Data Management and Stewardship.” *Scientific Data*, 3, 160018. https://doi.org/10.1038/sdata.2016.18

## 12.2 Primary EFMW research and reproducibility artifacts

[7] Wright, M. C. (2026). *EFMW — review entry point*, frozen target and open-obligation ledger. https://github.com/enuminous/EFMW/blob/main/README.md ; https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md

[8] Wright, M. C. (2026). *EFMW-EXP-001: Confirmatory Reconciliation*. https://github.com/enuminous/EFMW-EXP-001/blob/main/CONFIRMATORY_RECONCILIATION.md

[9] Wright, M. C. (2026). *EFMW-EXP-002: Benign-Transient Specificity Screen*, protocol, code, and results. https://github.com/enuminous/EFMW-EXP-001/tree/main/EXP-002

[10] Wright, M. C. (2026). *EFMW-EXP-003: Matched Whole-Run False-Alarm Budget*, protocol, code, and results. https://github.com/enuminous/EFMW-EXP-001/tree/main/EXP-003

[11] Wright, M. C. (2026). *Recursive Coherence Monitoring for Early Warning of Synthetic Control Degradation*. https://github.com/enuminous/papers/blob/main/Recursive-Coherence-Monitoring-Synthetic-Control-Degradation.md

[12] Wright, M. C. (2026). *EFMW-EXP-001 source repository*. https://github.com/enuminous/EFMW-EXP-001

[13] Wright, M. C. (2026). *Monolithic Zoo, 46 selected Lean 4 operational kernels and source coverage*. https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/main/README.md

[14] Wright, M. C. (2026). *EFMW-BIO-001: A Negative Benchmark Result for an EFMW-Inspired Memory Feature in Single-Cell ERK Signaling*. https://github.com/enuminous/papers/blob/main/EFMW-BIO-001-Cellular-Memory-Negative-Result.md

[15] Wright, M. C. (2026). *The Monolithic Twenty-Three: A Falsification-First Experimental Program for EFMW*. **Proposal only.** https://github.com/enuminous/papers/blob/main/MONOLITHIC-23-EFMW-Physical-Falsification-Program.md

[16] Wright, M. C. (2026). *Alternative Zoo Limiter Report and Input Contract*. https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/main/ALTERNATIVE_REPORT.md

[17] Wright, M. C. (2026). *EFMW-RP-001: Bubble Memory Detection and Identifiability*. https://github.com/enuminous/papers/blob/main/EFMW-RP-001-Bubble-Memory-Detection-and-Identifiability.md

[18] Wright, M. C. (2026). *TOE-001: Covariant EFMW-Inspired Unified Action and Correspondence Test*. https://github.com/enuminous/papers/blob/main/TOE-001-Unified-Action-and-Correspondence-Test.md

**Reference-use caution:** Internal GitHub manuscripts and independent third-party literature are different evidentiary classes. The former establish what this research program has reported and archived; they are not automatically peer-reviewed. Any subsequent academic submission requires citation-format review, literature-completeness review, provenance checks, and verification that the cited commit still contains the referenced material.

---

# Appendix A. Traceable source and version register

| Object | Frozen or identified boundary | What the source supports | What it does not support |
|---|---|---|---|
| EXP-001 | Published freeze metadata, confirmatory reconciliation, code and raw/processed traces | Prespecified synthetic lead result; per-seed reconstruction | Independent physical measurement |
| EXP-002 | Frozen protocol and source revision 048e26372279de6da70e0db71033a883dba67b87 copied from EXP-001 | Stable/pulse no-degradation specificity screen | Adequate false alarms or field performance |
| EXP-003 | Disjoint calibration 3001–3080, null 4001–4080, degradation 5001–5080 | Whole-run calibrated synthetic comparison | New recursion-specific mechanism |
| EFMW formal review | 01f51acb0b0e564105dcf7f14cc55998d41b91ce; tag efmw-review-2026-10-25 | Stated formal encodings, scope, and open obligations | Original physics verified |
| Zoo 46 | Pinned selected source models, coverage.json, formal CI | Bounded operational kernels, fixtures, and reporting | Full upstream pipeline equivalence |
| BIO-001 | Published protocol/source manifest/results in enuminous/papers | Secondary data comparison with negative comparator result | New biological mechanism |
| Bubble RP-001 | Published report and reproduced model specification | Synthetic relaxation response and conventional-model equivalence | Observed new information field |
| Monolithic-23 | Proposed unexecuted docket | Falsification design | Twenty-three completed tests |

A future reviewer should replace default-branch links with immutable commit URLs in the final submitted edition. This manuscript specifies the canonical EFMW frozen SHA but does not pretend that all currently linked repositories share one freeze timestamp.

# Appendix B. Full elementary mathematical derivations

## B.1 Signed memory as a convolution

Starting from \(m_t=\lambda m_{t-1}+(1-\lambda)r_t\) and \(m_0=0\),

\[
m_1=(1-\lambda)r_1,
\]
\[
m_2=(1-\lambda)(\lambda r_1+r_2),
\]
\[
m_3=(1-\lambda)(\lambda^2r_1+\lambda r_2+r_3).
\]

The pattern follows by induction. If \(m_0\ne0\), add \(\lambda^t m_0\). This makes explicit why the initialization and warmup period are part of the algorithm's specification.

## B.2 Cancellation versus rectification

For nonnegative weights \(w_j=(1-\lambda)\lambda^{t-j}\),

\[
\left|\sum_j w_jr_j\right|\le\sum_jw_j|r_j|.
\]

The right side is the smoothed magnitude, while the left side is the magnitude of the smoothed signed residual. The inequality is an exact mathematical fact and not a universal alert-ranking relation once thresholds differ.

## B.3 Alternating residual steady state

Suppose \(r_t=a(-1)^t\). Seeking a two-cycle \(m_t=c(-1)^t\) gives

\[
c(-1)^t=\lambda c(-1)^{t-1}+(1-\lambda)a(-1)^t
\quad\Rightarrow\quad c=\frac{1-\lambda}{1+\lambda}a.
\]

Thus \(|m_t|\to|a|(1-\lambda)/(1+\lambda)\), apart from transient effects and the sign convention on the first sample.

## B.4 Stationary variance

If the residuals are independent with mean zero, constant variance \(\sigma_r^2\), and independent of past memory, then

\[
V=\lambda^2V+(1-\lambda)^2\sigma_r^2,
\quad
V=\frac{1-\lambda}{1+\lambda}\sigma_r^2.
\]

If residuals are autocorrelated, cross-covariance terms enter; reusing this formula without the independence assumption is an error.

## B.5 Equivalence and identifiability

Define \(E_\lambda(r)=F_\lambda(r)\) and \(S_\lambda(r)=F_\lambda(r)\). Their outputs are exactly equal for every \(r\). Consequently \(\Pr\{E_\lambda\ne S_\lambda\}=0\) under **any** data-generating law, abstracting from floating-point implementation differences. A claim that the same recurrence produces a distinctive advantage over itself is contradictory; distinctive physical or computational content must be placed elsewhere.

## B.6 Tensor-allocation nonuniqueness

With constant \(\kappa\ne0\), define \(S=T+\kappa I\). For any admissible \(J\), \(T'=T+\kappa J\) and \(I'=I-J\). Then

\[
T'+\kappa I'=T+\kappa J+\kappa I-\kappa J=S.
\]

All observations depending only on \(S\) are invariant under this reassignment. To identify \(I\), one needs independently fixed sector definitions, equations, coupling, or observables that break the degeneracy. Conservation of \(S\) alone does not.

# Appendix C. Exact experimental split and reproduction checklist

## C.1 EXP-001

- Calibration seeds: 101–120; confirmatory: 1001–1040.
- Baseline threshold: 0.0455502027202869.
- Signed-memory threshold: 0.00834791535743751.
- Primary gate: at least +10 timesteps median paired gain.
- Entry commands from source root: run Python script *run_confirmatory.py*, then *analysis.py*.
- Archive and compare source SHA-256, runner hashes, per-seed outputs, and frozen analysis.
- Keep pointwise exceedance separate from sustained whole-run incidence.

## C.2 EXP-002

- Null seeds: 2001–2080.
- Stable and paired pulse conditions; pulse +0.05 at times 220–231.
- Candidate and baseline equations and thresholds unchanged from the frozen source.
- Three-sample sustained alert over the 480-step monitoring horizon.
- Absolute false-alarm gate: no more than 10%.
- Reproduce using *EXP-002/run.py* and *EXP-002/analyze.py*.

## C.3 EXP-003

- Calibration seeds: 3001–3080.
- Held-out null seeds: 4001–4080.
- Held-out degradation seeds: 5001–5080.
- 5% empirical whole-run calibration target, 76th ordered run-max statistic among 80.
- Strict threshold comparison, warmup from step 20, three consecutive exceedances.
- Actionable iff the **first** sustained alert lies on or after onset and before failure.
- Lead sentinel \(-999\) if not actionable.
- Joint gate: median paired gain at least 10; each null incidence no more than 10%; candidate detection at least 60%.
- Reproduce using *EXP-003/run.py* and *EXP-003/analyze.py*; require Python 3.10+ and NumPy per the frozen protocol.
- Check *EXP-003/calibration.csv*, *EXP-003/results.csv*, and the analysis output against the version under test.
- Record source commit, dependency installation, platform, test command, exit status, output hashes, and any deviations.

**Reproducibility boundary:** commands are copied from published artifacts. They are not represented as freshly executed by this dissertation-writing step.

# Appendix D. Evidence ledger schema and worked example

A minimal reusable schema for one reviewed claim:

| Field | Required content |
|---|---|
| claim_id | Stable, unique identifier |
| version | Immutable commit/tag or document version |
| statement | The exact claim, without interpretive enlargement |
| assumptions | All known premises and admissibility conditions |
| domain | Simulator, theorem, measured dataset, or physical system |
| test_id | One reproducible test with a defined acceptance rule |
| evidence_url | Exact run, data, proof declaration, or report |
| observed_status | PASS / FAIL / UNRESOLVED / N/A |
| rationale | Why this status follows; failure or limitation details |
| dependencies | Required prior claims and their states |
| reviewer | Person or process, independence, and date |
| open_obligations | Items necessary to support the broader interpretation |

**Worked example:**

Claim ID EXP-002-NULL. Statement: Under original EXP-001 thresholds, sustained null-alarm incidence of the candidate is at most 10% on the specified EXP-002 no-degradation screen. Observed: 66/80, or 82.5%. Status: **FAIL**. This result does not negate the separate EXP-001 warning-lead gate, but it blocks a claim that the original operating thresholds are operationally acceptable over the test horizon.

An **UNRESOLVED** example is the proposition that the general EFMW informational tensor has been physically identified. A Lean build or conserved total source does not supply an independent measurement or unique split. An **N/A** example would require affirmative documentation that a particular operation is irrelevant to a purely symbolic theorem; absence of a measurement is not sufficient.

# Appendix E. Falsification and decision matrix

| Target claim | Favorable observation | Strong falsifier or limiting result | Present state |
|---|---|---|---|
| EXP-001 early lead on frozen generator | Prespecified lead gate met | Gain below +10 on exact frozen test | PASS, bounded |
| Original thresholds provide tolerable run-level alarms | ≤10% sustained null alarms | EXP-002 82.5% candidate null incidence | FAIL |
| EXP-003 calibrated screen works on its generator | All three frozen gates met | Any frozen criterion missed | PASS, bounded |
| Current recurrence is a new filtering algorithm | A non-equivalent operation | Closed-form identity to signed EWMA | FAIL for novelty claim |
| A new EFMW mechanism supplies extra predictive value | Improvement after identical signed-EWMA and strong controls | No residual advantage after fair controls | UNRESOLVED; current update alone cannot suffice |
| Improvement transfers to real operations | Sealed external evaluation with appropriate controls | No gain, unreliable alarms, or dangerous missed faults | UNRESOLVED |
| EFMW-informed memory is uniquely implicated in measured cells | Advantage over exact conventional equivalent | BIO-001 equivalent EWMA and comparator defeat | FAIL for tested candidate |
| New bubble memory origin uniquely identified | Distinguishable model response | Exact Maxwell-viscoelastic counterpart | FAIL for uniqueness of tested response |
| New informational stress source independently detected | Distinctive, dimensionally grounded observable | Complete observational degeneracy or failed prediction | UNRESOLVED |

# Appendix F. Reproducibility and artifact audit form

For any future release, record the following without omitting inconvenient fields:

**Identity:** project, research question, author, reviewer, artifact license, contact, revision date.  
**Frozen target:** repository, full commit SHA, dependency pin, hash manifest, execution environment.  
**Scope:** explicit proposition, assumptions, exclusions, known unimplemented components.  
**Measurements:** raw source, processing steps, sample unit, labels, target transformations, missingness, provenance.  
**Protocol:** preregistered endpoints, thresholds, splits, sample size rationale, statistical tests, failure conditions.  
**Comparators:** simplest equivalent method, strong conventional methods, tunable degrees of freedom, equal budgets.  
**Results:** per-unit records, uncertainty, null outcomes, failed criteria, runtime qualified by environment.  
**Review:** specification match, kernel/axiom dependencies, external reproducibility, confidence bounds.  
**Interpretation:** what the result supports, does not support, and would require to generalize.  
**Ethics:** consent and publication permission for private peer comments or unpublished materials; data handling conditions.

No placeholder should be turned into a numeric value in a publication simply to improve the appearance of completeness.

# Appendix G. Glossary and notation

**EFMW:** Einstein–Feynman–Maxwell–Wright research program; a collection of research hypotheses and computational/formal methods, not an independently confirmed unified physical theory.  
**Recursive coherence:** in this dissertation, an operational score formed from a model residual's recurrent memory; **not** a universal physical coherence observable.  
**Residual \(r_t\):** observed value minus the defined model prediction.  
**Signed EWMA:** exponentially weighted moving average retaining residual sign until the final score.  
**Absolute EWMA:** exponentially weighted average of residual magnitudes.  
**Warning lead:** interval from the first valid actionable alert to the simulated labeled failure, under the source scoring rule.  
**Pointwise false-positive fraction:** fraction of sampled timepoints exceeding a threshold in a declared window.  
**Whole-run false-alarm incidence:** fraction of fault-free runs with at least one qualifying alert during a defined monitoring horizon.  
**Null control:** data or setup with the targeted fault/effect absent.  
**Ablation:** controlled removal or replacement of a model component while preserving a comparable evaluation.  
**Identifiability:** ability to distinguish a proposed mechanism or parameter from alternatives using specified observations.  
**Lean-checked:** checked conditional formal statement in a particular software environment.  
**UNRESOLVED:** evidence insufficient or claim not yet specified adequately; not implied truth or falsity.  
**Novelty:** difference from published mathematical, algorithmic, or empirical prior work, requiring independent literature and comparator assessment.

# Appendix H. Authorship, AI assistance, ethics, and competing interests

This is a research draft attributed to Matthew Chenoweth Wright, founder of Monolithic LLC. Portions of the underlying software development, documentation, mathematical exploration, and synthesis have used AI assistance. The human author is responsible for verifying source quotations, code integrity, mathematical derivations, citations, assumptions, and permissions before formal submission. This document makes no claim that an academic institution or supervisor approved, examined, or conferred a degree.

**Potential interest:** Monolithic LLC develops independent technical-review offerings based in part on this research and has an interest in the perceived utility of its methods. The existence of that business interest is a reason to use strong comparators, publish unfavorable results, and distinguish auditing services from verified scientific discoveries. No client, paying endorsement, capacity, grant, institutional affiliation, peer-review acceptance, or research funding is asserted without primary evidence.

**Private scientific correspondence:** nonpublic correspondence and unlicensed attachments must not be treated as public-domain source material. This draft does not quote or name the private reviewer of the subsequent filter ablation. A final academic edition should obtain permission or instead rely on a released artifact and independent verification.

**Research ethics:** future work with human-subject measurements, restricted data, safety-critical equipment, or proprietary models must follow applicable permissions, institutional requirements, and data-protection obligations. A public dataset license is not universal authorization to publish raw private records.

# Appendix I. Oral-defense questions and evidence-limited answers

**Q1. What exactly is new about the monitoring recurrence?**  
**A.** Nothing established as algorithmically unique. It is signed EWMA followed by absolute value. The contribution under investigation is its bounded application, evidentiary testing, and possibly later separately specified extensions.

**Q2. Why does EXP-003 not prove a new detector?**  
**A.** It compares a signed-memory filter with an absolute-residual smoother at a different decay. It demonstrates performance under a defined simulator and calibrated alarm budget, not novelty against an identical signed-EWMA control.

**Q3. Why retain EXP-002 if EXP-003 passes?**  
**A.** EXP-002 tests the original frozen thresholds and reveals high long-run false-alarm incidence. EXP-003 changes calibration under a new protocol. Removing EXP-002 would hide the reason that new calibration was needed.

**Q4. Does successful Lean compilation verify the physical program?**  
**A.** No. It establishes conditional formal claims under encoded assumptions, toolchain, and declared coverage. The physical interpretation requires separate modeling and empirical tests.

**Q5. Can recursive coherence be detected in biology?**  
**A.** A selected memory feature was tested against measured ERK data, but it was equivalent to conventional filtering and underperformed the best selected conventional comparator. No EFMW-specific biological mechanism was established.

**Q6. Why speak of falsifiability when EFMW has broad ambitions?**  
**A.** Each explicit, version-pinned candidate and endpoint can fail. The broad label by itself is not the experimental proposition. A testable research program requires narrowing to statements that generate discriminating predictions.

**Q7. If future tests find no distinctive advantage, is the dissertation worthless?**  
**A.** No. Clear null and equivalence results, robust negative controls, validated reproductions, and a reusable evidence-accounting method can be scholarship if original and rigorous. Their novelty and quality must be independently examined.

**Q8. What would justify extending the claims to physics?**  
**A.** A dimensionally specified, noncircular relation from defined EFMW variables to measurable observables; independent predictions; strong established-theory comparators; and successful external evidence. None has been completed across the general physical framework.

# Appendix J. Roadmap from research draft to examinable dissertation

This is a **requirements list, not a claim of work completed**.

1. Freeze the final research question, thesis proposition, and candidate mechanisms, retaining all historical frozen experiments.
2. Perform a systematic literature review across quickest-change detection, observer-based fault diagnosis, assurance cases, proof-carrying claims, and experimental reproducibility.
3. Obtain public, permission-cleared source and logs for external ablations or independently reproduce equivalent controls.
4. Execute the 2×2 factorial comparison with full matched calibration and sealed final evaluation.
5. Add independently designed fault families and no-fault controls with prospective preregistration.
6. Identify a measured external testbed if an applied performance claim is retained.
7. Establish independent code and result replication, including negative cases.
8. Verify formal target statements, full import dependencies, axioms, and actual coverage; distinguish structural encoding from analytic theorem.
9. Check the physical bridge, dimensional consistency, identifiability and observational predictions if any physics chapter claims more than a research agenda.
10. Commission a critical scholarly review of novelty, statistical reasoning, claims-to-evidence mapping, and writing, without presupposing acceptance.
11. Apply any relevant academic submission rules for format, originality, ethics approval, attribution, and examination; no such institutional process is claimed here.
12. Release a versioned final artifact with immutable references, full scripts, results, corrections, and an explicit changelog.

**End of dissertation-style research monograph.**
