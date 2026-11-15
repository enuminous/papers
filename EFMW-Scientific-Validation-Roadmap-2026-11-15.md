# EFMW Scientific Validation Roadmap

**Matthew Chenoweth Wright / Monolithic LLC**  
**15 November 2026 — Evidence assessment and proposed research plan**  
Prepared with AI assistance. External experimental work is attributed separately to Garret Sutherland.

[Repository index](README.md) · [Earlier physical-validation roadmap](EFMW-Physical-Validation-Research-Roadmap-2026-11-03.md) · [C1 specificity supporting package](research/efmw-c1-rel-001/README.md)

As of **15 November 2026**. EFMW has a reproduced result on a specified synthetic monitoring task and conditional mathematical derivations. These support narrow claims about algorithms and selected model branches. They do not yet establish an EFMW-specific physical prediction or physical confirmation of the broader framework.

The immediate scientific priority is to separate signed residual averaging from memory length, verify the execution record, and test a frozen claim on independently controlled data. Mathematical and physical work should proceed as distinct tracks with explicit assumptions and rejection conditions. This roadmap concerns scientific validation.

## What each kind of validation establishes

| Evidence track | A defensible result | What it cannot establish by itself |
| --- | --- | --- |
| Computational validation | Specified code reproduces a statistic and meets a frozen criterion on a defined data-generating process. Independent implementation and new data can establish broader reliability. | A theorem about all inputs, a unique EFMW mechanism, or a law of nature. |
| Mathematical proof | A conclusion follows from explicit definitions and assumptions. A kernel-checked formalization additionally verifies the encoded proof term. | That the assumptions describe nature, that an encoding faithfully captures the intended claim, or that finite numerical checks prove a universal theorem. |
| Physical confirmation | Calibrated observations test predeclared quantitative predictions against alternatives, with uncertainty, controls and independent replication. | Deductive proof of an entire theory. Equivalent models remain indistinguishable in their shared prediction domain. |

A simulation pass does not automatically advance to a mathematical proof or a physical result. Each track needs its own evidence.

## Current evidence and permitted claims

**Verification basis.** The five EXP-003 source files listed in the source register were examined. The 960 per-seed records were regrouped, paired by seed, and checked against the recorded onset, failure and alert fields; all 640 degradation classifications and lead values were internally consistent. The driver and runner were inspected alongside the pinned original monitor and simulator source. This is a reanalysis of supplied records, not a new end-to-end simulator run. The C1 archives and published audit were inspected; the specificity archive’s 25 manifest entries matched their stored bytes. Its recorded checks were not rerun.

### EXP-003 results

Each cell below uses **80 traces per arm and condition**. “Actionable” means the recorded first alert is at or after onset and before the simulator-defined failure. A null false alarm means at least one sustained alert anywhere in a null trace. It is not a per-timestep rate.

| Arm | Mean-drift actionable | Variance-fault actionable | Null false alarms | Mean-drift paired gain | Variance-fault paired gain |
| --- | ---: | ---: | ---: | ---: | ---: |
| Absolute residual, decay 0.90 | 65/80 | 77/80 | 6/80 (7.5%) | 0 | 0 |
| Absolute residual, decay 0.97 | 74/80 | 79/80 | 8/80 (10.0%) | +2.0 steps | 0.0 steps |
| Signed residual, decay 0.90 | 80/80 | 47/80 | 1/80 (1.25%) | +33.5 steps | −50.5 steps |
| Signed residual, decay 0.97, labeled EFMW | 77/80 | 41/80 | 2/80 (2.5%) | +41.5 steps | −61.5 steps |

Gains are medians of paired per-seed differences relative to the absolute/0.90 baseline. They use the historical **−999 lead for every unsuccessful actionable warning**, including pre-onset and late alerts. They are not differences of marginal medians or literal delays for missed detections. Sources: [per_seed.csv](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/per_seed.csv), [calibration_4arms.csv](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/calibration_4arms.csv) and the [driver](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/exp003_2x2_package.py.txt).

**Demonstrated in the supplied records:** the original EFMW comparison meets its frozen project screen: paired gain at least 10 steps, empirical null false-alarm incidence at most 10% for both original arms, and EFMW actionable detection at least 60%. Its original pass remains intact. The [protocol](https://github.com/enuminous/EFMW-EXP-001/blob/8f11bc5320cffb10932d5d31da7072d6ad4f65c2/EXP-003/protocol.md) describes a synthetic screen, not a safety or physical validation standard.

**Supported but incomplete:** retaining sign contributes substantially in this mean-drift setting. At decay 0.90, switching from absolute to signed averaging gives +33.5 steps; changing only the absolute arm’s decay gives +2.0. Within the signed arms, increasing decay to 0.97 gives +4.0 paired steps while actionable detections fall from 80 to 77. These are descriptive factorial contrasts with separately calibrated thresholds, not an additive causal decomposition.

**Rejected for a claim of superiority across both tested fault settings:** in the exploratory variance extension, EFMW produces 41 actionable alerts versus 77 for the baseline. Even among the 40 traces where both succeed, EFMW’s median paired lead is 24 steps shorter. This boundary is not solely a −999 artifact. All degradation traces eventually alert; the failures here are premature or late alerts. The [archive](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/README.md) attributes the original external reproduction and exploratory extension to Garret Sutherland and distinguishes them from later summary verification.

### Calibration uncertainty

All four arms target 5% empirical calibration incidence on seeds 3001–3080. Their independently evaluated null records use seeds 4001–4080. The following one-sided 95% exact binomial upper bounds were calculated from the supplied counts.

| Arm | Observed null incidence | Upper bound on trace-level false-alarm probability |
| --- | ---: | ---: |
| Absolute 0.90 | 6/80 | 14.27% |
| Absolute 0.97 | 8/80 | 17.32% |
| Signed 0.90 | 1/80 | 5.79% |
| Signed 0.97 | 2/80 | 7.66% |

None establishes a population false-alarm probability at or below 5% at this confidence level. This is insufficient evidence for that stronger guarantee, not a finding that all true rates exceed 5%. The calculation treats independent simulation seeds as Bernoulli trials at the specified 500-step horizon. It does not establish deployment reliability. Method: solve the binomial lower-tail probability equal to 0.05 for the upper bound, following [NIST exact confidence limits](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm).

### C1 mathematical and physical status

The 14 November 2026 C1 observable derivation and specificity audit establish the following recorded boundaries:

| Claim | Status | Evidence boundary |
| --- | --- | --- |
| A restricted C1 action yields a scalar–photon optical response with g = 4c_MW | Supported but incomplete; conditional derivation on record | The saved audit reports 35 forward-model grid checks. These are internal mathematical and implementation checks. |
| C1 fixes a unique nonzero photon coupling from a scalar mass | Rejected under the audited C1 assumptions | The specificity report supplies same-mass, different-coupling countermodels. |
| A selected positive-mass scalar branch links coupling to low-energy optical response | Supported but incomplete; conditional derivation on record | The archive records 33 passed symbolic/numerical checks. No Lean kernel proof or physical measurement was performed for this audit. |
| The derived optical relations uniquely identify EFMW | Rejected for the identical scalar comparator | The same restricted action produces the same relations in ordinary scalar effective theory. |
| The full EFMW framework describes observed physical reality | Hypothesis with unresolved evidence obligations | No new physical observation or outside replication is supplied by these packages. |

Sources: [published C1 audit](https://github.com/enuminous/papers/blob/c18b8f0aa3feba6477b828690d6be04bfa879e8b/research/efmw-c1-obs-001/AUDIT.md), [observable package](research/efmw-c1-obs-001/README.md) and [specificity audit package](research/efmw-c1-rel-001/README.md).

For one positive-mass, canonically normalized scalar, with the stated low-energy and weak-field assumptions and no independent four-photon contact term:

```math
a_X=\frac{g^2}{32m^2},
\qquad
\Delta n_{\rm scalar}=16a_XB^2+\text{higher-order terms}
=\frac{g^2B^2}{2m^2}+\text{higher-order terms}.
```

For multiple positive-mass modes the leading coefficient is the sum of g_i²/(32m_i²); an independently resolved subset supplies a lower bound. A one-mode equality cannot be replaced after an adverse result by a multimode inequality and still count as the original test passing. On-shell scalar production and the low-energy approximation have different validity regimes and require appropriate, independently constrained measurements.

The original coherence-memory force law still lacks the required operational variables, relaxation closure and detector coupling in the reviewed action. The existing optical branch does not fill that gap. The published [C1 README](https://github.com/enuminous/papers/blob/c18b8f0aa3feba6477b828690d6be04bfa879e8b/research/efmw-c1-obs-001/README.md) and the specificity package preserve this limitation.

## Methodological gaps to resolve

| Gap | Consequence | Required correction or test |
| --- | --- | --- |
| Both sign treatment and decay change in the original two-arm comparison | The original contrast cannot isolate a memory-length effect. | Keep the 2×2 design, estimate matched contrasts and interaction, and predeclare the primary contrast. |
| The EFMW score is the absolute value of a signed residual EWMA | The recurrence itself does not establish a new class of algorithm. | Compare equations with conventional EWMA, using smoothing weight α = 1 − decay. Include an independently implemented identical EWMA as an identity control; compare performance with non-equivalent CUSUM, variance-sensitive and robust monitors. |
| A 5% calibration target is estimated from 80 runs | Equal training incidence does not guarantee equal or acceptable holdout risk. | Separate development, calibration and sealed evaluation; apply uncertainty-based null acceptance. |
| First sustained alert is timestamped at the first sample of a three-sample window | An online alert can only be issued two steps later. | Freeze actual decision time t + 2 in the next protocol. Retain published historical timing and show any rescoring separately. |
| −999 mixes failure categories with lead time | Large gains or confidence limits can encode changes in success rate. Both-detected analysis selects successful pairs. | Report all failure categories; use a bounded all-trace endpoint for the next study and retain the historical endpoint as a secondary comparison. |
| The variance patch changes several generator features | It removes bias and sinusoid, increases noise, and retains the changing autoregressive coefficient. | Add a pure variance intervention with the coefficient fixed, then vary dynamics, bias and noise in separate controlled factors. |
| Known seeds, shared generator and outcome-informed extensions | The four-arm analysis and variance test cannot be described as new blinded confirmation. | Treat all existing records as development evidence. Give an independent custodian control of fresh seeds, generator variations and labels. |
| Finite computations and synthetic failure times | Neither universal validity nor operator benefit follows. | Test generalization on independent simulators and real telemetry with adjudicated failures; prove mathematical statements separately. |
| No EFMW-specific quantitative restriction in the optical branch | Even accurate scalar-model predictions cannot distinguish equivalent theories. | Derive an additional restriction from frozen premises before data access, or publish the branch explicitly as an equivalent conditional model. |

The timing issue follows directly from [monitors.py](https://github.com/enuminous/EFMW-EXP-001/blob/8f11bc5320cffb10932d5d31da7072d6ad4f65c2/EXP-003/monitors.py), which returns the start of a length-three qualifying window. The generator and patch boundaries follow from [simulator.py](https://github.com/enuminous/EFMW-EXP-001/blob/8f11bc5320cffb10932d5d31da7072d6ad4f65c2/EXP-003/simulator.py) and [variance_fault.patch.txt](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/variance_fault.patch.txt). The EWMA comparison uses the standard recurrence documented by [NIST](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc324.htm).

## Prioritized research plan

1. **Reproduce and reconcile the frozen evidence.** Retrieve the complete archived bundle, including calibration maxima, logs and results JSON. Run in a disposable checkout at the declared source revision. Preserve the original pass and the negative extension result. Resolve any discrepancy before changing a scientific claim.

2. **Freeze the mechanism question.** Decide whether the target is useful signed-EWMA behavior, a measurable memory-length effect, or a distinct proposed EFMW algorithm. An identical EWMA implementation is an identity control, not an independent mechanism. If no distinct algorithm remains, publish the bounded known-method result and stop claiming EFMW-specific algorithmic superiority.

3. **Register and run a sealed computational test.** Lock comparators, calibration budgets, timestamp semantics, fault families, margins, sample size and analysis. Require difficult null conditions, both drift signs, pure variance faults, mixed faults, autocorrelation, heavy tails, model misspecification, missing data and timing changes. Keep development and confirmation datasets separate.

4. **Establish transfer beyond the original simulator.** Replicate with an independently written generator and then a fixed, externally sourced telemetry dataset. Split by equipment or recording session where dependence requires it. Use independent event adjudication and report failures and false alerts in operational units.

5. **Complete one bounded mathematical result.** Prioritize the conditional positive-mass matching relation and its subset bound. State the matrix, normalization, regularity, boundary and approximation assumptions; obtain an external derivation review and, where feasible, a kernel-checked formalization.

6. **Qualify a physical test.** Identify an actual apparatus or suitable raw dataset, establish the mapping to measured electromagnetism, quantify sensitivity and nuisance effects, and freeze a conditional relation test. A distinctive EFMW claim needs an additional theory-derived prediction that differs from the generic scalar comparator.

## Proposed acceptance criteria for the next computational study

These are **new research design choices**, not retroactive conditions on EXP-003 or established operational standards. Freeze them before any sealed result is accessible.

Choose a calibration target below the 5% acceptance ceiling to allow for estimation uncertainty; freeze that choice using development-only power analysis. Use the independent trace as the analysis unit. Let T_decision be the first alarm’s actual issue time, O the onset and F the failure time. For the next 120-step fault window, define actionable lead R as F − T_decision when O ≤ T_decision < F, and zero otherwise. Preserve premature, late, missing and invalid-run categories separately. The primary contrast is the paired mean difference in R against a preselected non-equivalent comparator. Do not select the “best” comparator after test results are visible.

| Gate | Proposed acceptance rule | Failure or inconclusive interpretation |
| --- | --- | --- |
| Execution integrity | All frozen runs accounted for; required exit codes successful; provenance and outputs reconcile; declared tolerances met. | An integrity failure blocks inference. Repair and version the implementation before a new confirmation attempt. |
| Null false-alarm control | One-sided exact upper confidence bound ≤5% per 500-step null trace for the candidate and each comparator used in a superiority claim. Use simultaneous bounds if asserting a family-wide guarantee. | A bound above 5% leaves the guarantee unestablished. Never retune on the sealed null set. |
| Practical warning benefit | Family-adjusted 95% lower confidence bound for mean paired R gain >10 steps against the preselected comparator, within each fault family claimed to benefit. | If the upper bound is below the 10-step target, the practical-superiority claim fails. If the interval crosses the target, evidence is inconclusive. |
| Detection coverage | Lower confidence bound for candidate actionable detection ≥60%, and lower bound for candidate-minus-comparator detection >−5 percentage points. | Lead improvement cannot compensate silently for an unacceptable loss of coverage. These are research floors, not safety criteria. |
| Statistical error control | One primary comparison and named confirmatory secondary contrasts; family-wise α=0.05 with a prespecified adjustment such as Holm. Report effect sizes and intervals, including sign×decay interaction. | Unplanned contrasts are exploratory. Historical unadjusted significance does not count as new confirmation. |
| Sample size and stopping | Before unblinding, simulate the paired design and uncertainty procedure on development data; choose fixed sample sizes for ≥90% power at a declared plausible alternative above the 10-step margin. Declare an anticipated true null rate strictly below 5% and size the null study for ≥90% probability of passing at that rate. | “80 seeds” is not a universal sample-size justification. No optional stopping or post-result sample expansion. |
| External replication | A custodian-controlled dataset and separate implementation pass the same registered gates, with discrepancies published. | Recomputing the same CSV or changing only the random seed is not independent cross-system replication. |

Keep both-detected medians and the historical −999 statistic as labeled secondary analyses. Use paired resampling at the trace level, or at the highest independent cluster for real telemetry. Validate interval coverage under the planned design before registration; timestep resampling would create pseudoreplication. All invalid runs remain in the accounting, with exclusions fixed in advance.

## Falsification and proof obligations

| Target | Test capable of rejecting it | Evidence needed for a stronger claim |
| --- | --- | --- |
| Advantage in a declared fault family | Sealed paired comparison fails the predeclared benefit or coverage target with sufficient precision. | Eligible false-alarm rates, adjusted intervals and an independent replication. A failed broad claim may justify a narrower newly registered claim. |
| Benefit specifically from longer memory | Hold sign operation fixed; vary decay and calibration under equal rules. Add sign-randomization controls that preserve residual magnitudes. | A prespecified decay effect and interaction consistent across relevant settings. A favorable bundled comparison is insufficient. |
| Numerical correctness | Independent code disagrees, an invariance or limiting case fails, or output provenance breaks. | Minimal reproducible counterexample or corrected version with the original failure retained. |
| A universal mathematical implication | An admissible counterexample violates the conclusion. | Definitions and quantifiers, non-circular assumptions, a complete derivation, and independent proof review. Finite checks cannot close a universal obligation. |
| One-mode C1 optical relation | A valid joint confidence region has no intersection with the frozen equality. | Identifiable mass/coupling and a separate optical-response measurement with shared systematic errors modeled. |
| EFMW-specific physics | Every predicted observable remains identical to a known comparator, or a distinct frozen prediction is excluded. | A theory-derived discriminating restriction plus calibrated independent measurements. Equivalence is an attribution limit even if the common model fits. |

The C1 audits already reject a mandatory mass–coupling law and unrestricted rank-one response under the reviewed assumptions. Do not reintroduce those conclusions as premises. A new restriction is a new model version and must be tested accordingly.

### Mathematical release requirements

A proof release must include the exact theorem statement and its informal meaning, source revision, definitions, units and canonical normalization, hypotheses, nonvacuity checks, counterexamples outside the domain, and the chain from the selected action to the result. Separate exact identities from approximation theorems and quantify approximation errors.

For formalization, pin Lean, Mathlib and dependencies; provide one build command and an external replay log; inspect axioms and placeholders; and review whether the formal theorem expresses the scientific assertion. No circular conservation premise, assumed conclusion or definitional tautology can substitute for the intended derivation. Computational monitoring results have no automatic bearing on these proof obligations.

### Conditional physical test requirements

The [optical experiment contract](https://github.com/enuminous/papers/blob/c18b8f0aa3feba6477b828690d6be04bfa879e8b/research/efmw-c1-obs-001/EXPERIMENT_CONTRACT.md) and the specificity archive’s TEST_CONTRACT.md are proposals. They do not establish apparatus access or completed measurements.

Before unblinding, choose either the one-mode equality or the specified positive-mass multimode inequality. For a well-identified nonzero coupling, the one-mode diagnostic R_phys = 32m²a_X/g² predicts 1. If coupling is compatible with zero, test the undivided relation with its joint uncertainty rather than dividing by it.

Use a joint 95% confidence region with validated coverage and a declared multiplicity rule. Nonintersection with the selected relation rejects that conditional model only after validity checks pass. Intersection is compatibility, not confirmation; require predeclared resolving power and report the region’s width. Set the scientifically meaningful tolerance, global discovery threshold, exposures and stopping rule from an actual apparatus sensitivity analysis before registration. Those quantities remain open tracker items.

Required controls include field-off, either conversion region disabled, polarization changes, shuttered input, calibrated injections and held-out wavelength or length changes. Account for QED and material responses, light leakage, efficiency, alignment, field calibration, correlations and background transfer. Establish the positive kinetic domain, scalar transmission assumptions and relevant low-energy or propagation regime. Calibrated injections validate instruments; they do not demonstrate scalar production.

A null result can exclude a specified parameter region. It does not refute an unrestricted family that still allows zero or arbitrarily small coupling. A replicated signal matching this shared branch would support the scalar interaction model; it would not uniquely confirm EFMW. The existing [OSQAR publication](https://arxiv.org/abs/1506.08082) supplies prior experimental constraints, not new EFMW observations.

## Outstanding experiment and evidence tracker

All future owners below are **proposed roles**. Matthew coordinates the research record; no outside reviewer, custodian or laboratory commitment is established here. Timing is relative to satisfying dependencies, not a promise of completion.

| Priority and item | Current status | Next deliverable and closure evidence | Proposed responsibility and dependency |
| --- | --- | --- | --- |
| P0 Frozen EXP-003 replay | Recorded reproduction and summary agreement; fresh execution unresolved | Disposable pinned checkout, environment digest, full logs and exit codes; match thresholds, all per-seed outcomes and declared statistical outputs. | Matthew or reproducibility engineer; first task. |
| P0 Endpoint and comparator specification | Gaps identified | Versioned protocol resolving t versus t+2, −999 versus bounded lead, exact EWMA equivalence, primary comparator and claim scope. | Matthew plus methods reviewer; before new calibration. |
| P1 Null calibration study | Four holdout estimates available; 5% upper-bound gate unmet | New calibration and sealed null cohorts, justified sample size, exact bounds and risk audit by condition. | Statistician and independent custodian, unassigned; after protocol freeze. |
| P1 Sign and decay factorial test | Exploratory evidence available | Sealed 2×2 contrasts and interaction, signed CUSUM and variance-aware comparators, prespecified multiplicity and failure reporting. | Experiment implementer and custodian, unassigned; after P0. |
| P1 Fault generalization test | One exploratory ranking reversal | Pure variance, coefficient-only, mixed-fault and misspecified-generator results, with condition-specific acceptance decisions. | Independent simulator author, unassigned; same locked analysis. |
| P2 Telemetry transfer | Unresolved | Licensed raw traces, independently adjudicated events, split by independent equipment/session, streaming timestamps and operational false-alert units. | Domain data partner, unassigned; dataset suitability before testing. |
| P1 C1 proof and specificity review | Conditional derivations and saved checks; no new kernel proof | Independent derivation review, explicit theorem and approximation assumptions, known-model comparison; formal replay if formalized. | Mathematical reviewer, unassigned; use frozen C1 sources. |
| P2 Distinguishing EFMW prediction | Missing in audited optical branch | A quantitative restriction derived independently of test data, with a different comparator prediction and rejection region; otherwise retain equivalence claim. | Matthew plus theoretical reviewer, unassigned; required before EFMW-specific physical attribution. |
| P2 Physical feasibility and registration | Proposed contracts only | Identified apparatus/dataset, calibration and background model, parameter identifiability, uncertainty budget, power/precision calculation and locked analysis. | Experimental collaborator and statistician, unassigned; no booked experiment assumed. |
| P3 Physical replication | Unperformed | Independent acquisition and analysis, held-out cross-observable prediction, full null/negative record and resolved discrepancies. | Separate laboratory or custodian, unassigned; after a qualified first measurement. |

For each update, record the exact claim, version, run or dataset, observed outcome, evidence link, unresolved limitation, next action and date. Close a row only when its required evidence exists. A paper draft, repository upload, passing fixture or encouraging discussion does not close an experiment.

## Reproducibility package requirements

- Freeze the target statement, simulator, detector, calibration rule, endpoint, comparison set, planned analyses and exclusions. Keep the original EXP-003 record immutable and place extensions in separately versioned directories.

- Retain source revision **8f11bc5320cffb10932d5d31da7072d6ad4f65c2** for the auditor’s declared replay target. Record differences from the originally cited EXP-003 commits, source and data SHA-256 hashes, dependency lock, container digest, OS and numerical-library versions.

- Preserve the seed partitions: calibration 3001–3080, null 4001–4080, degradation 5001–5080 for historical replay. Fresh sealed tests require new inaccessible partitions; these existing seeds are public.

- Archive raw per-trace inputs or a fully specified deterministic generator, calibration maxima, thresholds, all outcomes, full stdout/stderr, analysis code and results JSON. Retain bootstrap RNG seed 230048 and 10,000 resamples when reproducing the historical interval.

- Check every subprocess exit code. [run_package.sh.txt](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/run_package.sh.txt) uses set -u rather than fail-fast execution and can continue after errors. Its original run command rewrites original-named CSV outputs, so execute only in a disposable checkout.

- Preserve original bytes and line endings. Report exact hashes separately from explicitly normalized LF/CRLF comparisons; normalized equality is not exact byte identity.

- Keep the variance patch confined to a copied simulator. Verify default and null paths remain equivalent and the four-arm implementation matches the original two monitors. Record tolerance and every deviation.

- Distinguish record reanalysis, same-environment replay, independent implementation, new-generator replication and physical replication in every release. Disclose AI assistance and the specific contribution of external reviewers.

## Publication milestones

| Milestone | Release content | Gate and permitted claim |
| --- | --- | --- |
| M0 Evidence and boundary record | Original protocol/results, external review attribution, four-arm tables, ranking reversal, timing and sentinel limitations, complete provenance. | Can describe the bounded result and reproducibility status. Preserve the original pass without turning exploratory extensions into preregistered confirmation. |
| M1 Registered computational protocol | Sealed-data custody, algorithms, identity control, power calculation, acceptance rules and analysis code. | Registration and freeze must precede access to confirmatory outcomes. A locked repository commit alone does not establish independent custody. |
| M2 Confirmatory computational paper | All registered results, per-condition decisions, confidence intervals, null results and deviations. | Claim only the algorithmic performance supported by the stated generators or telemetry. Publish whether the outcome passes, fails or remains unresolved. |
| M3 Conditional mathematics paper | C1 derivation, countermodels, overlap with known theory, proof review and any formal build evidence. | State the exact assumptions and distinguish analytic proof, symbolic checks, numerical examples and kernel checking. No physical validation claim. |
| M4 Physical protocol and feasibility report | Actual apparatus characterization, uncertainty and sensitivity, distinct measurement channels, analysis and discovery rules. | Feasibility and registration, not detection. Do not schedule a claimed result before these requirements are met. |
| M5 Physical results and replication | Raw observations, controls, calibrated likelihood, parameter regions, held-out predictions and independent replication. | Support or exclude the tested model/parameter region. Attribute uniquely to EFMW only if a discriminating prediction was tested successfully. |

The C1 observable derivation was already present in **enuminous/papers** at the inspected snapshot. The 14 November specificity audit is preserved in this release as a [supporting package](research/efmw-c1-rel-001/README.md), with its [publication record](research/efmw-c1-rel-001/PUBLICATION_NOTICE.md). Repository publication, peer review, mathematical proof and independent replication are separate milestones. This publication reports an evidence assessment and research plan, not a new end-to-end simulator run, formal kernel check or physical measurement.

## Source register

The assessment uses the following research records. The EXP-003 archive links are pinned to source revision `4d35d5b461cc3663d96152f0665b2f8683bf82ae`; the underlying historical replay target remains separately specified. Source data, analytical derivations, saved computational checks and proposed tests retain distinct evidence status.

| Source | Role |
| --- | --- |
| [exp003_2x2_package.py.txt](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/exp003_2x2_package.py.txt) | Four-arm definitions, threshold selection, endpoints, sentinel rule and paired analysis. |
| [run_package.sh.txt](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/run_package.sh.txt) | Declared replay revision, provenance procedure and execution caveats. |
| [variance_fault.patch.txt](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/variance_fault.patch.txt) | Exact exploratory intervention and retained generator dynamics. |
| [per_seed.csv](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/per_seed.csv) | 960 records used for recomputed counts, classifications and paired medians. |
| [calibration_4arms.csv](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/calibration_4arms.csv) | Thresholds and held-out null counts, cross-checked against per-seed data. |
| [Frozen EXP-003 protocol](https://github.com/enuminous/EFMW-EXP-001/blob/8f11bc5320cffb10932d5d31da7072d6ad4f65c2/EXP-003/protocol.md) and [external-review archive](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/README.md) | Original acceptance screen, attribution, additional logs, calibration maxima and verification record. |
| [C1 observable package](research/efmw-c1-obs-001/README.md) and [published audit](https://github.com/enuminous/papers/blob/c18b8f0aa3feba6477b828690d6be04bfa879e8b/research/efmw-c1-obs-001/AUDIT.md) | Conditional action-to-observable derivation, 35 recorded grid checks and known-model equivalence. |
| [C1 specificity audit package](research/efmw-c1-rel-001/README.md) | Conditional matching relation, countermodels, 33 recorded checks and proposed physical test contract. |
| [NIST binomial confidence intervals](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) and [EWMA reference](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc324.htm) | Statistical bound construction and conventional algorithm comparison. |
| [OSQAR 2015 primary paper](https://arxiv.org/abs/1506.08082) | Prior scalar–photon experiment and published constraints; not an EFMW measurement. |
