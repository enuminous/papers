# EFMW force experiment feasibility and model development

**Publication status: feasibility protocol v0.5; EFMW force derivation INCOMPLETE; Stage two NOT RELEASED; screen and experiment NOT RUN. Instrument feasibility is a separately scoped service; no laboratory engagement is established.**

[Download the revised Word protocol](HYP-001-P2-Memory-Hysteresis-Experimental-Protocol-2026-11-16.docx) · [Screen arithmetic calculator](HYP-001-P2/screen_decision.py) · [Papers index](README.md)

**Revision v0.5 — 16 November 2026.** Corrects and supersedes [v0.4](https://github.com/enuminous/papers/blob/1b9ce6da996e328247b03c3e3093b03403e673c2/HYP-001-P2-Memory-Hysteresis-Experimental-Protocol-2026-11-16.md). The point-estimate screen rule is withdrawn: the one-sided 95% upper bound on paired SD must be strictly below 2 µN, with justified sampling assumptions and acceptable nuisance checks. Stage zero now requires six defined evidence checks, including derivation, physical accounting, independent replay and discrimination; a reviewer cannot waive them. The missing force law is an unfinished theory output. A bounded instrument feasibility package can be quoted and completed separately, including a negative result, without claiming an EFMW test. The calculator checks conditional arithmetic only; it cannot verify the noise model or release Stage two.

HYP-001 P2  |  Feasibility protocol v0.5  |  16 November 2026

Prepared for Matthew Chenoweth Wright and a prospective experimental physics laboratory. The current laboratory request is a bounded instrument feasibility study. An EFMW force test is deferred because its physical coupling prediction has not been derived. This revision defines the theory deliverable, objective review criteria and a conservative sensitivity screen. No screen, physical experiment, laboratory appointment or approval is established.

## Choice and bounded claim

P2 compares different histories at identical present drive and could reuse a P1 force apparatus. Neither proposal yet supplies the physical coupling needed for a decisive EFMW test. P3 needs a closed energy budget and P4 needs quantum hardware. The work available to scope now is instrument feasibility and model development; no claim that P2 is the cheapest decisive physical test is supported.

The proposed observable is the difference between high-history and low-history force residuals after both reach coherence C₁ = 0.5. The HYP-001 ansatz supplies the following temporal template [1]. It becomes an apparatus prediction only if a specified source-to-probe interaction justifies this form:

$$
\Delta F(t)=A e^{-t/\tau_M}, \qquad A=\kappa C_1\Delta M(0).
$$

The ansatz supplies no measured κ, lower bound on its magnitude or derived physical timescale. The 10 µN value remains a planning option. The required source-to-probe force prediction is a research output still to be produced, not a premise established by this protocol. Until that output is complete, instrument intervals cannot be reported as EFMW coupling limits. Even later, a null excludes only a specified parameter range.

## Physical meaning of memory

Define the measured circuit state as capacitor voltage divided by its calibrated reference voltage. A 200 kΩ resistor and 10 µF capacitor give a nominal RC time of 2 s. Measure the actual response, uncertainty, leakage and temperature dependence with the force experiment disconnected. Freeze that measured circuit time before Stage two. Identifying it with τ<sub>M</sub> is an additional hypothesis, not a consequence of calibration.

A circuit voltage is an operational state variable. Its identification with an interaction-producing memory remains a hypothesis. Before Stage two, specify what carries that state, what property of the probe responds, and a force law that predicts their interaction in the actual geometry. Calling a search conditional does not waive this requirement. Independent review checks the model and claim scope; agreement alone is not evidence that the interaction exists.

For four measured oscillator phases, C is the squared magnitude of their mean unit phase phasor [1]. This definition gives C = 1 for equal phases, C = 0 for quadrature phases, and C = 0.5 for (0, 0, π/2, π/2). Archive the phase-estimation code and normalization. Neither a fitted force decay nor a successful RC calibration identifies a new physical interaction.

An unspecified interaction does not logically guarantee zero measured force. It leaves the physical interpretation and the hypothesis excluded by a null undefined. The RC decay remains ordinary circuit behavior. The proposed additional mechanical interaction has not been specified sufficiently to release Stage two.

## Work that a laboratory can quote now

Request a quote for the first package below, with a separate option for further qualification. Neither package depends on a new interaction existing. The theory work is commissioned separately from bench work; completing its report may leave Stage two blocked. A quotation is not a laboratory engagement or an authorization to spend.

| Package | Scope and completion evidence |
| --- | --- |
| A Instrument feasibility | Check the candidate force readout and traceable scale, record the fixed template and statistical assumptions, then acquire eight driven C ≈ 0 pairs if calibration is valid. Deliver all raw traces, calibration uncertainty, paired amplitudes, s₈, U₀.₉₅, witness channels and the screen decision. If work stops early, deliver the failed check and available data. |
| B Optional qualification | Price separately the existing zero-injection, physical-injection and deliberate disturbance blocks. Deliver measured nuisance transfer, drift, recovery, uncertainty and attainable sensitivity. This option requires a new written scope after Package A; it does not authorize a confirmatory EFMW run. |
| C Theory development | Produce a source-to-probe model paper and executable predictions satisfying G1–G6 below, or a documented non-closure identifying the missing step. The coupling derivation belongs to the theory work, not to the laboratory’s acceptance of Package A. No model or completion date is promised. |

### Completion and permission to proceed

Package A is complete when the agreed records and a signed decision are delivered, including a negative or incomplete screen. A scientifically useful failure is not a failed service delivery. Acceptance of the report does not mean the instrument met the noise criterion. Package B is complete when its specified calibration and uncertainty results are delivered, even if the proposed force sensitivity proves unattainable.

The quotation must state the apparatus and configuration, operator, included calibration work, cost or cost ceiling, time ceiling, stop conditions, data ownership and delivery format. Those commercial fields remain unfilled. Do not purchase a 96-pair run on the strength of a quotation, a screen pass or a reviewer’s general approval.

The EFMW physical test is currently not ready to commission. An exploratory search using an independently postulated force law would need its own hypothesis label and prospective protocol; it cannot substitute for the missing EFMW prediction. No exploratory force run is authorized by this document.

## Stage zero theory output and release criteria

Current status: UNRESOLVED. Stage two is not released. G1–G6 must each be MET with the evidence below. A missing artifact is UNRESOLVED; a demonstrated inconsistency is FAIL. Six MET entries permit EFMW model handoff. Instrument feasibility remains separately commissionable. Handoff establishes a testable specification, not a real force or a confirmed EFMW claim.

The model paper is a required research output. Pin the EFMW equations used and show the steps connecting them to this apparatus. Label every added constitutive or bridge assumption. Merely postulating κCM, or programming an actuator to follow it, does not supply the derivation. A separate phenomenological hypothesis may motivate other research; it is not a completed EFMW derivation. [1, 8]

| Check | MET only when the following evidence is present |
| --- | --- |
| G1 Physical mapping | The paper defines the source state, memory carrier, probe property, units and spatial support. A dimensional calculation maps measured voltages and phases to those quantities; no unidentified state is hidden in κ. |
| G2 Derived observable | An explicit derivation from the pinned premises produces the sensitive-axis force or interaction energy, including geometry, distance, direction, shielding and time response. Every extra assumption is identified. A new force postulate must be labeled as a separate hypothesis, not marked as a derivation. |
| G3 Physical accounting | The same model identifies the energy source, reaction degrees of freedom and mechanical power over its parameter range. Its energy and momentum balance is shown, including a declared approximation and error bound. Unclosed accounting cannot support an energy-creation claim or a MET entry. |
| G4 Independent replay | Archive code, inputs and expected force traces for null, active and changed-geometry cases. Divide every trace by the same declared nonzero reference force. An independent runner reproduces each normalized sample within absolute error 10⁻⁶, with a run log and hashes. A zero active template fails. |
| G5 Discrimination | Specify an additional contrast and its predicted sign or ratio. Stack planned-condition templates; normalize each nonzero column to unit Euclidean norm. Adding the model column to the declared nuisance matrix must increase rank at SVD tolerance 10⁻⁶ times its largest singular value. Archive matrices and singular values. Physical resolvability remains a Stage-one requirement. |
| G6 Falsifiable scope | Freeze the parameter domain, observable, null range and interpretation for a positive, null or ambiguous result. State exactly which finite parameter range can be excluded and which claims cannot. An amplitude with no lower bound cannot make every null a falsification of EFMW. |

The independent reviewer records one status per check with an artifact path, equation or run-log locator and a reason. The reviewer cannot waive a check. Conflicting reviews remain UNRESOLVED with the disputed check identified. The release rule is the conjunction of G1–G6, followed separately by full instrument and analysis qualification and the named signatures. All six checks are currently UNRESOLVED; P1 does not close them.

### What calibration can establish

A calibrated actuator establishes known conventional force and detector recovery. Driving it with CM validates the measurement chain only. Keep injections separate from the scientific source and independently calibrated. Synthetic-data success and actuator recovery cannot satisfy the theoretical derivation or demonstrate a new interaction.

## Apparatus

| Item | Candidate implementation subject to qualification |
| --- | --- |
| Coherence source | Four phase-programmable electrical sine channels at 1 kHz, each nominally 1 V RMS into its own measured 1 kΩ resistor. Measure actual terminal phases and per-channel power; total source, controller and memory-circuit power are separate monitored quantities. |
| Candidate memory | Measured C drives a 0–1 V DAC and buffered RC low-pass. Nominal 200 kΩ × 10 µF gives 2 s. Measure capacitor voltage and reference voltage independently; identify actual circuit response with the force experiment disconnected. Its interpretation as M remains conditional. |
| Force readout | Grounded 10 g proof mass on a horizontal single-axis flexure, with optical or capacitive readout and independent force calibration. Candidate shield-to-mass gap: 50 mm. Measure stiffness, bandwidth, tilt and cross-axis coupling. Freeze actual geometry after qualification. |
| Isolation and controls | Separate rigid source support, conductive shield and draft enclosure. Battery power and optical control reduce variable cable forces. Log temperatures, base vibration, tilt, acoustic pickup and electromagnetic pickup; measure residual coupling through the full installation. |
| Force calibration | Independently calibrated actuator supplies zero and signed physical force histories over a prospectively chosen range. Measure static scale, dynamic transfer, injection uncertainty and dummy-readout pickup. A command value alone is not a force calibration. [4] |

The 10 g mass has approximately 98 mN vertical weight; that ratio alone does not determine horizontal force resolution. Tilt and cross-axis leakage can couple weight into the measurement and must enter the uncertainty budget. Neither 10 µN resolution nor a 2 µN paired SD is assumed.

## Acquisition and time resolution

| Channel | Proposed acquisition | Acceptance condition |
| --- | --- | --- |
| Force and displacement | 200 samples/s, synchronously timestamped | Analog anti-alias filter with 20 Hz passband and verified attenuation above 100 Hz. Candidate settling: 95% within 0.2 s. Measure the full transfer; revise bandwidth and timing before freeze if this target fails. |
| Oscillator voltage and current | 20,000 samples/s per channel | Measure terminal signals rather than using commanded phases. Analog anti-alias filtering; adequate rejection above the 10 kHz Nyquist limit. |
| Coherence C and memory M | C from 10 ms phase-estimation windows; M at 200 samples/s | Archive raw voltage/current, computed C, capacitor voltage, clock and phase command. Inter-channel timing error below 1 ms. |
| Whole-device electrical input | 20,000 samples/s for voltage and current | Include controller and memory hardware, not only the four resistors. Retain power histories and supply ripple. |
| Environment | Temperature at 10 samples/s; vibration, acoustics and EM witness at 10,000 samples/s | Appropriate anti-alias filters. Calibrate nuisance-to-force transfer, including tilt and slow drift. Equal nominal power does not establish equal thermal state. |

These sample rates are starting choices for a seconds-scale response. Qualification determines the final bandwidth, anti-alias rejection, settling and fit window. The statistical unit is a complete randomized history pair, not each 200 Hz sample. Freeze a revised schedule if the independently measured circuit time differs from 2 s.

## Stage one conservative eight pair screen

### Decision rule for the original 10 µN option

After valid force calibration, acquire exactly eight diagnostic pairs in the fixed configuration. Use high and low conditioning histories, ending both at measured C ≈ 0 with the source driven. Randomize four high-first and four low-first orders. Keep the planned timing and final wiring. The zero-history-force expectation is conditional on the CM ansatz; this is instrument characterization, not an EFMW null experiment.

Fit a fixed unit-force temporal template through the calibrated readout and compute the sample SD s₈ of the eight paired force amplitudes in µN, with divisor seven. Do not divide by CΔM at C ≈ 0. Freeze the template and fit window before acquisition. Let U₀.₉₅ denote the one-sided 95% upper confidence bound on the true paired SD σ. [7]

Advance only if U₀.₉₅ < 2 µN and the predeclared nuisance and data-quality limits pass. Equality does not pass. Stop the original planning option if a valid bound is at least 2 µN. If the bound is not justified or data are incomplete, record UNRESOLVED and do not advance. A pass permits full qualification only; it never releases Stage two.

$$
U_{0.95}(\sigma)=s_8\sqrt{\frac{7}{\chi^2_{0.05,7}}}\approx1.7971507317\,s_8.
$$

For eight independent normal paired amplitudes, divide seven by the lower 5th percentile of chi-square with seven degrees of freedom, 2.1673499093, then take the square root. Thus the strict criterion is s₈ < 1.1128727072 µN. Use the full-precision calculation in the companion arithmetic script; the rounded figures here are explanatory. [7]

| Illustration | Bound and decision under the stated assumptions |
| --- | --- |
| Observed s₈ = 1 µN | U₀.₉₅ ≈ 1.797 µN. Meets the noise criterion; nuisance checks and all later qualification remain required. |
| Observed s₈ = 2 µN | U₀.₉₅ ≈ 3.594 µN. Does not pass. The earlier 1.3–4.1 µN interval was two-sided 95%; its upper endpoint is not this one-sided bound. |
| True σ = 2 µN | For a single valid screen the corrected noise criterion passes with probability 5%, compared with about 57% for s₈ ≤ 2 µN. These are calculated properties, not measured bench performance. |

The chi-square rule requires independent normal paired amplitudes with one stable variance. Justify those assumptions before the screen from the measurement model and independent calibration history; eight observations cannot establish them. Correlation, changing variance or non-normal tails invalidate this particular bound. Do not invent effective degrees of freedom or use an unqualified eight-point bootstrap. The stated factor treats the calibrated force scale as fixed; material scale uncertainty requires a validated joint upper bound, otherwise record UNRESOLVED.

One screen applies to one frozen configuration. Preserve every result; no extra pairs, selective replacement or repeat-until-pass. A redesigned apparatus requires a new prospective record and disclosure of prior attempts. Do not aggregate repeated attempts into a claim of a 5% overall false-clearance risk. The small screen deliberately requires a margin below the 2 µN ceiling.

## Full apparatus qualification

Begin this work only under the separate qualification scope. For the original 10 µN option, the valid upper-bound screen must pass first. Record all configurations, injections, counts and disturbance ranges before collection. Pilot data never enter the confirmatory sample. Freeze the developed estimator before fresh qualification; retain every failed attempt and revision. An alternative bound-setting study requires a new prospective scope, not a relabeled screen failure.

| Qualification block | Required measurement |
| --- | --- |
| Baseline and drift | After the eight-pair screen, plan 24 zero-injection pairs across two days, with phase histories disabled and representative powered conditions. Repeat the full cycle; estimate paired spread, day drift, order effects and dependence. |
| Physical injections | Preselect three calibrated magnitudes over the prospective range; plan six paired recoveries per sign and magnitude. Include 10 µN only if it can be calibrated. Mask signs and magnitudes; report recovery bias, uncertainty and saturation. These are development counts, not certified power. |
| Nuisance transfer | Separately vary heating, electrical pickup, vibration, acoustics and tilt across the envelope, with phase histories disabled. Measure creep and settling. Then run controller shams and driven C = 0 endpoint controls through the final installation. Eight passive pairs alone do not measure these transfer functions. |
| Fresh qualification | Freeze the candidate pipeline, then collect at least 12 fresh zero-injection control pairs over two days and repeat selected blinded physical injections. Retain discrepancies. Freeze any larger sample in advance; a small physical pilot cannot certify a 1% false-positive rate. |

Zero injection means no added calibration force, not an absence of all forces. Record each control’s null assumption. Estimate nuisance corrections from dedicated disturbance calibration, never from primary high/low contrasts or an unexplained history-correlated residual.

### Scientific target and demonstrated capability

Before inspecting an active high/low force contrast, specify a scientifically motivated minimum effect δ<sub>science</sub>, or explicitly choose a bound-setting objective if none is defensible. Separately estimate the minimum detectable amplitude D for the complete decision rule, including random variation, dependence, calibration and systematic uncertainty. Report uncertainty in D and choose the planned test amplitude A<sub>test</sub> and sample size from this qualification record.

If D exceeds δ<sub>science</sub>, improve the apparatus or register a less sensitive bound-setting experiment while retaining the original scientific threshold. If capability is only about 100 µN, report that limitation. A 100 µN force bound would correspond approximately to a 200 µN bound on |κ| only when measured C₁ΔM(0) ≈ 0.5 and its uncertainty is included. No such capability or bound has yet been measured.

## Stage two history pairs and controls

| Stage | Instruction |
| --- | --- |
| Reset | Hold C = 0.5 for at least 10τ<sub>M</sub>, and longer if witness channels require it. Qualification sets washout and baseline limits. At nominal τ<sub>M</sub> = 2 s, the minimum is 20 s. |
| Condition | For 10τ<sub>M</sub>, use high coherence with phases (0, 0, 0, 0), C ≈ 1; or low coherence with (0, π/2, π, 3π/2), C ≈ 0. Keep each load amplitude and frequency fixed. |
| Common present | Over a fixed 20 ms transition, move both histories to exactly the same waveforms, with phases (0, 0, π/2, π/2), giving C = 0.5. Record actual C and M throughout. Set t = 0 at the end of this transition. |
| Observe | Acquire for 5τ<sub>M</sub>, nominally 10 s. Candidate fit window: 0.25–10 s. Freeze the actual window after qualification. Use measured C and M, the transition and calibrated sensor transfer; do not assume an ideal instantaneous step. |
| Pair and blind | Repeat from reset with the other history; randomize high-first versus low-first. An independent custodian holds assignments and injection codes. Matthew Wright cannot be the custodian. Restrict access to label-revealing phase and memory channels as specified in the release record. |

For C = 0.5, starting tolerances are measured coherence within ±0.01 and per-channel RMS power mismatch below 0.1%. Retain them only if qualification bounds the resulting force bias inside the frozen budget. Keep record length, averaging, amplitude and phase processing identical across histories.

## Confirmatory sample and control allocation

The former 96-pair schedule (48 primary, 24 C = 0 and 24 controller-sham pairs) remains an example. It cannot start before G1–G6 are MET, the applicable upper-bound screen passes, full qualification succeeds and all release signatures are recorded. Freeze exact counts, day and order allocation, and resource limits prospectively. Size the complete rule for both signs at A<sub>test</sub>, including same-sign effects on at least two separately calibrated days; pooled 48-pair power does not establish each day’s power.

| Control | What it must establish |
| --- | --- |
| Zero coherence present | Apply the same high/low conditioning, then end with measured C ≈ 0. The κCM term predicts zero history force in the ideal C = 0 limit, even while memory differs. Use measured residual C to bound any allowed HYP contribution. |
| Controller sham | Run the same command-processing activity and coded labels, but keep physical phases at C = 0.5 throughout, with M driven by measured C. A label-correlated force here points to controller, acquisition or ordinary environmental effects. |
| Instrument and nuisance calibration | Use independently measured disturbance transfer functions and frozen correction coefficients. Exercise both phase-disabled calibration and actual switching controls. Quantify creep, thermal and dielectric lag, pickup and order effects; freeze allowed control-effect bounds before Stage two. |
| Positive injection | Recover blinded zero and ±A<sub>test</sub> physical force histories through the frozen pipeline. Predefine allowable recovery bias and uncertainty as part of the total budget; demonstrate that they preserve planned sensitivity. Software-added signals validate analysis only. |

## Analysis qualification and frozen estimator

HYP-001A reported 99.9% false positives for naive regression and 9.9% for nuisance-adjusted HAC regression at nominal 5% significance [2]. Those are synthetic results, not force measurements. Neither pipeline is qualified for this confirmatory experiment. Validate a newly frozen estimator before interpreting experimental residuals.

After the model handoff, generate each signed force predictor from the released law and pass it through the calibrated sensor transfer. X(t) = C<sub>H</sub>(t)M<sub>H</sub>(t) − C<sub>L</sub>(t)M<sub>L</sub>(t) is valid only if the derivation justifies it in the frozen geometry. Retain pair-specific scales and uncertainty. Any changed law, added assumption or predictor must repeat affected G1–G6 checks and qualification before new confirmatory acquisition; do not choose it from active force contrasts.

Use randomization inference at the actual randomized unit, or a validated correlation-aware interval method. Preserve within-run and between-pair dependence and day structure; do not treat 200 Hz samples as replicates. Propagate force-scale, memory, transfer-function and nuisance uncertainty into each interval. Specify distributions, covariance assumptions and how bounded biases enter the interval. Shared drift and systematic uncertainty do not shrink merely by dividing by the square root of the number of pairs. [6]

Run at least 10,000 fresh synthetic null repetitions for each declared stress family: drift, thermal lag, crosstalk, imperfect nuisance sensors, order effects and between-pair dependence. Validate the complete frozen decision rule, not only an isolated regression test. Require a one-sided 95% upper confidence bound on false-positive probability ≤1%, and a 95% lower bound on power ≥90% for each sign at ±A<sub>test</sub>. Use fresh injected repetitions for power, with counts frozen in advance. Include uncertainty in pilot-derived noise and nuisance parameters. Synthetic qualification does not establish that all physical confounders are represented.

Conditional planning example: 48 independent paired amplitudes with true SD 2 µN give standard error about 0.29 µN and an ideal normal 99% random-error half-width about 0.74 µN. These exclude systematic uncertainty and separate day tests. Version 0.5 replaces the point-estimate screen with U₀.₉₅ < 2 µN for the original planning option. Full qualification must still include uncertainty in noise, nuisance transfer and drift; a screen pass is not a power calculation.

Calibrate interval coverage at zero and across the proposed coupling range, and check robustness to model misspecification. Keep analysis-development, synthetic validation, physical calibration and confirmatory data identifiable and separate. If validation fails, revise the estimator and use new validation data. Do not reuse failed validation outcomes to claim an unchanged preregistered pass.

Control-derived uncertainty enters the primary budget once. Do not double-count it in control intervals or assume a non-significant control is acceptably small. Require the full control intervals to lie inside predeclared equivalence limits, allowing measured residual coherence where appropriate. These limits replace the universal ±2 µN requirement and must be justified against the chosen scientific target or bound-setting objective.

Freeze all primary and control endpoints, multiplicity handling, exclusions, confidence-interval construction and the complete positive/null decision rule before Stage two begins. Both signs require two-sided inference. The custodian runs the signed, frozen pipeline with the full phase and memory records; sealed results and quality-control decisions precede key release.

## Null positive and inconclusive outcomes

| Outcome | Required interpretation |
| --- | --- |
| Stage two not released | Any G1–G6 check, required qualification or signature is incomplete. Do not begin the EFMW force experiment. Instrument feasibility and theory non-closure reports may be delivered separately. This is the current status, not a physical null or a failure of EFMW. |
| Null within the tested range | The released model, calibration and controls pass. The systematic-inclusive 99% amplitude interval contains zero and lies inside ±δ<sub>science</sub> if specified; otherwise report its endpoints as a bound-setting result. A κ bound requires the released physical mapping and predictor uncertainty. Exclude only the stated range of that model in this apparatus. |
| Candidate positive | The frozen template fits a signed history-force difference and its systematic-inclusive 99% interval excludes zero on each separately calibrated day with the same sign. All controls, calibration and frozen decision gates pass. Report the amplitude and interval, including effects below A<sub>test</sub> or δ<sub>science</sub>; do not relabel them as target-sized results. |
| Confirmed anomaly only | A separate operator and independently calibrated instrument reproduce the frozen effect and control behavior on new data. This supports an apparatus anomaly. An EFMW-specific interpretation still requires a defensible physical mapping, exclusion of conventional mechanisms and comparison with alternative models. |
| Inconclusive | The interval cannot exclude the scientifically relevant range, required sensitivity or controls fail, the signal is confounded, or the physical interpretation remains unsupported. State which conclusion is UNRESOLVED. Report any valid apparatus-level interval separately; do not convert a failed quality gate into a physics bound. |

## When the experimentalist stops

Before Stage two: require every G1–G6 check to be MET, the applicable upper-bound screen to pass, and calibration, recovery, analysis qualification, independent custody and signatures to be complete. A model paper is a research output, not something a laboratory reviewer supplies by approval. An independently postulated force search needs its own hypothesis and protocol. Freeze a justified δ<sub>science</sub> or a finite bound-setting objective.

During qualification: stop advancement to Stage two if the chosen objective cannot be resolved, held-out validation fails, or a conventional effect is indistinguishable from the proposed template. Redesign or register a weaker bound-setting objective before new confirmatory data. A matching exponential is insufficient because force-sensor creep can also have exponential components. [3]

During Stage two: pause for saturation, lost timing, environmental excursions or calibration and memory drift beyond the frozen limits. Starting candidates are 2% force-scale drift and 1% circuit-time drift; retain them only if qualification shows they protect the uncertainty budget and can be measured reliably. Retain all records. Terminate as a quality failure if exclusions exceed 5% of attempted pairs; do not selectively replace outcomes.

After key release: withhold a HYP-001 attribution if the force follows controller shams, violates the C = 0 control allowance, or is explained by calibrated conventional corrections. Close a parameter range only when the valid interval and controls support it. A candidate positive triggers independent replication, with no retrospective retuning.

The confirmatory run count is fixed before collection. Do not stop when significance appears, extend until it appears, move thresholds after inspecting active contrasts, or treat an unclosed energy budget as established energy creation. Any later experiment requires a new prospective freeze.

## Bench release and independent custody

Stage two release requires six MET model checks, completed instrument and analysis qualification, and approval of the same version and hashes by every named signatory. A general endorsement cannot waive a criterion. Blank entries are not approvals. Publish only the secret key’s commitment hash before release.

| Item | Record to freeze |
| --- | --- |
| Apparatus | Actual frequencies, amplitudes, loads, shielding, geometry and gap; sensor axis, stiffness and bandwidth; photographs and wiring; calibration traceability, uncertainty and safe operating range. |
| Memory and coupling | Measured circuit response and uncertainty; G1–G6 model paper, mapping, derivation, conservation calculation, fixtures, independent replay, discrimination matrices, parameter domain and permitted interpretation. |
| Sensitivity | Screen s₈ and U₀.₉₅, assumption record and decision; paired dependence, drift, nuisance covariance, total uncertainty, injection recovery, δ<sub>science</sub> or bound-setting objective, D and A<sub>test</sub>, and control limits. |
| Design | Exact primary and control counts by day; washout; assignment; exclusions and stops; custodian identity; secret key location and hash; access restrictions; release procedure and timestamps. |
| Analysis | Estimator, source and code hashes; fresh null and injection validation; interval and multiplicity rules; template, fit window and endpoint; immutable raw-data paths and checksums. |

Name a custodian independent of Matthew Wright, hypothesis development and outcome analysis; disclose affiliations and conflicts. Matthew cannot hold the key. The custodian seals label-revealing phase, memory, predictor and injection records. Analysts receive coded forces and predeclared non-revealing quality summaries. An authorized independent runner executes frozen code on complete records and seals outputs and exclusions before key release after the full run. Log access breaches and their effect on claim status.

### Required approval record

| Role | Sign-off responsibility | Name signature and date |
| --- | --- | --- |
| Laboratory lead | Calibration, controls, operating envelope and feasibility | Unappointed |
| Analysis lead | Frozen estimator, power, coverage and decision rule | Unappointed |
| Independent technical reviewer | G1–G6 evidence locators, statuses and independent replay; no discretionary waivers | Unappointed |
| Independent key custodian | Independence, access controls, commitment and key-release record | Unappointed |
| Matthew Chenoweth Wright | Hypothesis and model selection, conditional scope and closure after a qualified null | Pending signature |

No appointment or engagement is assumed. Record key release separately after sealing results, exclusions and quality decisions.

## References

[[1] Wright 2026  EFMW HYP 001  P2 and its physical scope](https://github.com/enuminous/papers/blob/e472280c6bfb8d1e3b2b318c7ee4b58a122bf045/EFMW-HYP-001-Testable-Physical-Predictions-2026-11-12.md)

[[2] Wright 2026  HYP 001A known zero recovery and failed calibration](https://github.com/enuminous/papers/blob/e472280c6bfb8d1e3b2b318c7ee4b58a122bf045/EFMW-HYP-001A-Known-Zero-Recovery-2026-11-13.md)

[[3] Bartel and Yaniv 1997  Load cell creep and recovery  NIST](https://pmc.ncbi.nlm.nih.gov/articles/PMC4894594/)

[[4] NIST  Force calibration via electrostatics](https://www.nist.gov/publications/force-calibration-electrostatics)

[[5] NI  Anti aliasing filters and their usage](https://www.ni.com/en/shop/data-acquisition/measurement-fundamentals/analog-fundamentals/anti-aliasing-filters-and-their-usage-explained..html)

[[6] NIST  Basic definitions of measurement uncertainty](https://physics.nist.gov/cuu/Uncertainty/basic.html)

[[7] NIST  One sided and two sided confidence limits for standard deviation](https://www.itl.nist.gov/div898/handbook/prc/section2/prc231.htm)

[[8] Eöt-Wash  Results and interaction assumptions for force limits](https://www.npl.washington.edu/eotwash/results)

## Review recommendations and pilot record

The record below includes the correction to v0.4’s point-estimate gate and the requirement for objective model handoff. Laboratory feasibility is a separate deliverable. No completed measurement, theory derivation or approval is claimed.

| Recommendation | Protocol response | Evidence status |
| --- | --- | --- |
| Identify physical memory | G1 requires a physical carrier and dimensional mapping. An independently measured RC time does not identify physical memory. | Mapping unresolved |
| Specify the coupling path | The model paper must satisfy G1–G6. The reviewer checks identified artifacts and replay results; no criterion may be waived. Theory non-closure is an allowed deliverable. | Stage two blocked |
| Measure sensitivity first | Eight driven C ≈ 0 pairs precede qualification. Advance only with a justified one-sided upper 95% bound U₀.₉₅ < 2 µN and acceptable nuisance checks; s₈ alone cannot pass. | Screen not run |
| Report real noise and nuisance transfer | A bounded instrument report can be commissioned without an EFMW law. Report actual noise, nuisance transfer and attainable sensitivity; do not call a capability estimate a physics bound. | Not measured |
| Independent custody and freeze | Matthew cannot hold the key. Record G1–G6 evidence and all named signatures before Stage two acquisition. | Unappointed |

### Required pilot decision record

Before the screen, freeze its configuration, force template, window, nuisance limits and the independent normal-noise assumption record. Use all eight valid amplitudes with divisor seven; record U₀.₉₅ and its method. Missing justification gives UNRESOLVED, not permission to use s₈ instead. Invalid data give an incomplete screen; preserve all attempts.

| Record | Required entry before a laboratory commits to Stage two |
| --- | --- |
| Screen result | Eight amplitudes, order, timestamps, raw-data and code hashes; mean, s₈, one-sided U₀.₉₅, assumption record and quality checks. Current entry: NOT MEASURED. |
| Nuisance result | Dedicated perturbation ranges, transfer estimates and uncertainty; residual force budget and drift. Eight passive pairs do not supply this. Current entry: NOT MEASURED. |
| Capability and scope | D and uncertainty, recovery and proposed counts. A κ limit requires all model checks and qualified normalization. Feasibility may be reported without that model. Current entry: NOT QUALIFIED. |
| Decision and signatures | STOP ORIGINAL PLAN, PROCEED TO QUALIFICATION, or UNRESOLVED; criterion, evidence, operator, lab lead and date. Stage two separately requires G1–G6, qualification and full signed release. Current entry: UNRESOLVED. |

For example, s₈ = 2 µN now stops the original plan because U₀.₉₅ ≈ 3.594 µN. Deliver that result as an instrument finding. A redesigned apparatus or different bound-setting objective needs a new prospective scope. No measurement service can stand in for the unfinished EFMW force derivation.
