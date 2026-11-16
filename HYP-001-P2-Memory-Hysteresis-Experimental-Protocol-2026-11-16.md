# EFMW memory hysteresis force experiment

**Publication status: proposed bench protocol v0.4; coupling specification INCOMPLETE; Stage two NOT RELEASED; screen and experiment NOT RUN; physical coupling UNRESOLVED.**

[Download the revised Word protocol](HYP-001-P2-Memory-Hysteresis-Experimental-Protocol-2026-11-16.docx) · [Papers index](README.md)

**Revision v0.4 — 16 November 2026.** Supersedes [v0.3](https://github.com/enuminous/papers/blob/1659cca7bfbb35b1cb0b841bd2a205af7084cd6a/HYP-001-P2-Memory-Hysteresis-Experimental-Protocol-2026-11-16.md) and makes the response to Boardy’s recommendations explicit. For the original 10 µN planning option, an eight-pair driven C ≈ 0 screen with observed paired SD above 2 µN stops that plan before the full run; passing advances only to full qualification. The ceiling is an early feasibility rule for that option, not a certified noise floor or a universal scientific threshold. A new pilot record requires actual noise, nuisance transfer, uncertainty and a signed decision before committing to Stage two. The missing coupling specification still blocks Stage two, and P1 does not supply the missing interaction. Independent custody and the full signed release remain required.

HYP-001 P2  |  Proposed bench protocol v0.4  |  16 November 2026

Prepared for Matthew Chenoweth Wright and a prospective experimental physics laboratory. Status: coupling specification incomplete; Stage two is not released. Stage one can characterize instruments and conventional disturbances. A force experiment requires a specified interaction model, measured sensitivity, independent review and a signed freeze. No physical signal or laboratory engagement is established.

## Choice and bounded claim

P2 compares different histories at identical present drive and may reuse a P1 force apparatus. Its cost advantage remains conditional on a testable coupling model and suitable force metrology. P3 requires a closed energy budget and P4 requires quantum hardware. This document is a qualification plan with a deferred force experiment, not a demonstrated cheapest decisive EFMW test.

The proposed observable is the difference between high-history and low-history force residuals after both reach coherence C₁ = 0.5. The HYP-001 ansatz supplies the following temporal template [1]. It becomes an apparatus prediction only if a specified source-to-probe interaction justifies this form:

$$
\Delta F(t)=A e^{-t/\tau_M}, \qquad A=\kappa C_1\Delta M(0).
$$

The model supplies no measured κ, lower bound on its magnitude or derived physical timescale. The 10 µN value remains illustrative. Until Stage zero is complete, a force interval cannot be interpreted as an EFMW coupling bound. After model release, a null can exclude only the stated parameter range of that interaction in the recorded apparatus.

## Physical meaning of memory

Define the measured circuit state as capacitor voltage divided by its calibrated reference voltage. A 200 kΩ resistor and 10 µF capacitor give a nominal RC time of 2 s. Measure the actual response, uncertainty, leakage and temperature dependence with the force experiment disconnected. Freeze that measured circuit time before Stage two. Identifying it with τ<sub>M</sub> is an additional hypothesis, not a consequence of calibration.

A circuit voltage is an operational state variable. Its identification with an interaction-producing memory remains a hypothesis. Before Stage two, specify what carries that state, what property of the probe responds, and a force law that predicts their interaction in the actual geometry. Calling a search conditional does not waive this requirement. Independent review checks the model and claim scope; agreement alone is not evidence that the interaction exists.

For four measured oscillator phases, C is the squared magnitude of their mean unit phase phasor [1]. This definition gives C = 1 for equal phases, C = 0 for quadrature phases, and C = 0.5 for (0, 0, π/2, π/2). Archive the phase-estimation code and normalization. Neither a fitted force decay nor a successful RC calibration identifies a new physical interaction.

An unspecified interaction does not logically guarantee zero measured force. It leaves the physical interpretation and the hypothesis excluded by a null undefined. The RC decay remains ordinary circuit behavior. The proposed additional mechanical interaction has not been specified sufficiently to release Stage two.

## Stage zero specify the physical coupling

Current status: NOT MET. No source-to-probe interaction model is established by this protocol. Do not commission or begin Stage two as an EFMW test until the following record is complete. Stage one alone may be scoped as instrument qualification.

A test may begin from an explicit phenomenological hypothesis; a known new force or complete microscopic derivation is not required. The hypothesis must nevertheless map measurable source and probe properties to a falsifiable force prediction. Published force searches state the interaction and parameter assumptions under which their bounds apply. [8]

| Required model record | Evidence or specification needed before release |
| --- | --- |
| Source and probe | Identify the physical source state, its units and spatial distribution, the property of the probe that responds, and the assumption connecting the measured RC voltage to that state. The voltage definition alone is insufficient. |
| Interaction law | Provide an explicit force law or an interaction energy whose displacement derivative gives force. State direction, normalization, source and probe dependence, distance and orientation scaling, and the predicted effect of shielding. A constant κCM at an unspecified geometry is insufficient. |
| Time response and parameters | Specify memory dynamics, propagation or response delays, parameter units and allowed ranges. Generate the predicted sensitive-axis signal through the calibrated sensor transfer. If amplitude is free, freeze a range to constrain; do not invent a lower bound. |
| Discrimination and accounting | Specify at least one additional model-predicted contrast, such as separation, orientation or probe substitution, and conventional alternatives. Record the proposed energy source, reaction momentum and any unresolved dynamical completion; no energy-creation interpretation follows. |
| Independent release | Archive the model, assumptions, prediction code and prospective parameter bounds with version and hashes. The laboratory lead, analysis lead and independent technical reviewer must approve testability and permitted interpretation before the full signed release. |

The physical mapping, interaction law and independent contrast are currently missing. This is a specification task, not a completed model. The same missing coupling specification also limits P1; reusing its apparatus does not resolve it. The κCM temporal ansatz must not be relabeled as an apparatus derivation by filling in κ numerically.

### What calibration can establish

The calibrated actuator supplies a known conventional force. Driving it with a waveform proportional to CM can validate the detector and analysis, but cannot establish the proposed interaction. Keep such injections separate from the scientific source, with independent calibration and blinded codes. Neither actuator recovery nor synthetic-data success satisfies Stage zero.

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

## Stage one apparatus qualification

### Eight pair preliminary sensitivity screen

After force calibration, run eight diagnostic pairs before the larger qualification blocks. Use the high and low conditioning histories, ending both at measured C ≈ 0 with the source driven. Balance four high-first and four low-first orders in a randomized sequence. Use the planned timing and final wiring. Report paired amplitude SD, drift and witness-channel pickup. The zero-history-force expectation is conditional on the proposed CM ansatz.

For this screen and all zero-injection noise blocks, fit an independently fixed unit-force temporal template passed through the calibrated readout. Do not normalize by CΔM at C ≈ 0. Freeze the template and fit window before the screen; known-force injections establish its physical scale.

For the original 10 µN planning option, stop after this screen if paired SD s₈ > 2 µN or a frozen nuisance limit fails; do not start the full confirmatory schedule. A screen pass permits further qualification only. Eight pairs cannot certify the true SD: for independent normal pair amplitudes with observed SD 2 µN, the calculated 95% interval is about 1.3–4.1 µN. This is illustrative, not measured performance. Complete the pilot decision record below. [7]

Record all pilot configurations, injection levels, counts and disturbance ranges before collection. Pilot data never enter the confirmatory sample. Freeze the developed estimator before fresh qualification data; retain every failed attempt and revision. The eight-pair screen supplements the blocks below.

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

The former 96-pair schedule (48 primary, 24 C = 0 and 24 controller-sham pairs) remains a planning example. It must not start before the eight-pair screen, full qualification and Stage zero release. After qualification, freeze exact counts, day and order allocation, and resource limits. Size the complete decision rule for both signs at A<sub>test</sub>, including same-sign effects on each day. Require at least two separately calibrated days. A pooled 48-pair calculation does not establish power for each day.

| Control | What it must establish |
| --- | --- |
| Zero coherence present | Apply the same high/low conditioning, then end with measured C ≈ 0. The κCM term predicts zero history force in the ideal C = 0 limit, even while memory differs. Use measured residual C to bound any allowed HYP contribution. |
| Controller sham | Run the same command-processing activity and coded labels, but keep physical phases at C = 0.5 throughout, with M driven by measured C. A label-correlated force here points to controller, acquisition or ordinary environmental effects. |
| Instrument and nuisance calibration | Use independently measured disturbance transfer functions and frozen correction coefficients. Exercise both phase-disabled calibration and actual switching controls. Quantify creep, thermal and dielectric lag, pickup and order effects; freeze allowed control-effect bounds before Stage two. |
| Positive injection | Recover blinded zero and ±A<sub>test</sub> physical force histories through the frozen pipeline. Predefine allowable recovery bias and uncertainty as part of the total budget; demonstrate that they preserve planned sensitivity. Software-added signals validate analysis only. |

## Analysis qualification and frozen estimator

HYP-001A reported 99.9% false positives for naive regression and 9.9% for nuisance-adjusted HAC regression at nominal 5% significance [2]. Those are synthetic results, not force measurements. Neither pipeline is qualified for this confirmatory experiment. Validate a newly frozen estimator before interpreting experimental residuals.

After Stage zero, use the released interaction law to generate the signed force predictor for every pair and pass it through the calibrated sensor transfer. The simple X(t) = C<sub>H</sub>(t)M<sub>H</sub>(t) − C<sub>L</sub>(t)M<sub>L</sub>(t) form is valid only if that law justifies it in the frozen geometry. Retain pair-specific scales and uncertainty when fitting κ and reporting amplitude A. Any changed law or predictor requires new qualification and a new freeze before Stage two; do not select it from active force contrasts.

Use randomization inference at the actual randomized unit, or a validated correlation-aware interval method. Preserve within-run and between-pair dependence and day structure; do not treat 200 Hz samples as replicates. Propagate force-scale, memory, transfer-function and nuisance uncertainty into each interval. Specify distributions, covariance assumptions and how bounded biases enter the interval. Shared drift and systematic uncertainty do not shrink merely by dividing by the square root of the number of pairs. [6]

Run at least 10,000 fresh synthetic null repetitions for each declared stress family: drift, thermal lag, crosstalk, imperfect nuisance sensors, order effects and between-pair dependence. Validate the complete frozen decision rule, not only an isolated regression test. Require a one-sided 95% upper confidence bound on false-positive probability ≤1%, and a 95% lower bound on power ≥90% for each sign at ±A<sub>test</sub>. Use fresh injected repetitions for power, with counts frozen in advance. Include uncertainty in pilot-derived noise and nuisance parameters. Synthetic qualification does not establish that all physical confounders are represented.

Conditional planning example: if 48 independent paired amplitudes actually have SD 2 µN, their mean has standard error about 0.29 µN and an ideal normal 99% random-error half-width about 0.74 µN. These exclude systematic uncertainty and separate day tests. The 2 µN screen ceiling in v0.4 is an early feasibility rule for the original 10 µN planning option, not a certified noise floor or a universal scientific threshold. Full qualification must include uncertainty in measured noise and support the frozen A<sub>test</sub>, control bounds and objective.

Calibrate interval coverage at zero and across the proposed coupling range, and check robustness to model misspecification. Keep analysis-development, synthetic validation, physical calibration and confirmatory data identifiable and separate. If validation fails, revise the estimator and use new validation data. Do not reuse failed validation outcomes to claim an unchanged preregistered pass.

Control-derived uncertainty enters the primary budget once. Do not double-count it in control intervals or assume a non-significant control is acceptably small. Require the full control intervals to lie inside predeclared equivalence limits, allowing measured residual coherence where appropriate. These limits replace the universal ±2 µN requirement and must be justified against the chosen scientific target or bound-setting objective.

Freeze all primary and control endpoints, multiplicity handling, exclusions, confidence-interval construction and the complete positive/null decision rule before Stage two begins. Both signs require two-sided inference. The custodian runs the signed, frozen pipeline with the full phase and memory records; sealed results and quality-control decisions precede key release.

## Null positive and inconclusive outcomes

| Outcome | Required interpretation |
| --- | --- |
| Stage two not released | The source-to-probe interaction or required signatures are incomplete. Report specification incomplete and do not begin the force experiment. Instrument results may be reported separately. This is the present status, not a null result or a failure of EFMW. |
| Null within the tested range | The released model, calibration and controls pass. The systematic-inclusive 99% amplitude interval contains zero and lies inside ±δ<sub>science</sub> if specified; otherwise report its endpoints as a bound-setting result. A κ bound requires the released physical mapping and predictor uncertainty. Exclude only the stated range of that model in this apparatus. |
| Candidate positive | The frozen template fits a signed history-force difference and its systematic-inclusive 99% interval excludes zero on each separately calibrated day with the same sign. All controls, calibration and frozen decision gates pass. Report the amplitude and interval, including effects below A<sub>test</sub> or δ<sub>science</sub>; do not relabel them as target-sized results. |
| Confirmed anomaly only | A separate operator and independently calibrated instrument reproduce the frozen effect and control behavior on new data. This supports an apparatus anomaly. An EFMW-specific interpretation still requires a defensible physical mapping, exclusion of conventional mechanisms and comparison with alternative models. |
| Inconclusive | The interval cannot exclude the scientifically relevant range, required sensitivity or controls fail, the signal is confounded, or the physical interpretation remains unsupported. State which conclusion is UNRESOLVED. Report any valid apparatus-level interval separately; do not convert a failed quality gate into a physics bound. |

## When the experimentalist stops

Before Stage two: stop if Stage zero is incomplete, or calibration, injection recovery, analysis qualification, custodian independence or signatures are missing. A fully specified phenomenological interaction may be tested with its assumptions explicit. An unspecified interaction cannot proceed merely under a conditional label. Freeze a justified δ<sub>science</sub> or a bound-setting objective for the released model.

During qualification: stop advancement to Stage two if the chosen objective cannot be resolved, held-out validation fails, or a conventional effect is indistinguishable from the proposed template. Redesign or register a weaker bound-setting objective before new confirmatory data. A matching exponential is insufficient because force-sensor creep can also have exponential components. [3]

During Stage two: pause for saturation, lost timing, environmental excursions or calibration and memory drift beyond the frozen limits. Starting candidates are 2% force-scale drift and 1% circuit-time drift; retain them only if qualification shows they protect the uncertainty budget and can be measured reliably. Retain all records. Terminate as a quality failure if exclusions exceed 5% of attempted pairs; do not selectively replace outcomes.

After key release: withhold a HYP-001 attribution if the force follows controller shams, violates the C = 0 control allowance, or is explained by calibrated conventional corrections. Close a parameter range only when the valid interval and controls support it. A candidate positive triggers independent replication, with no retrospective retuning.

The confirmatory run count is fixed before collection. Do not stop when significance appears, extend until it appears, move thresholds after inspecting active contrasts, or treat an unclosed energy budget as established energy creation. Any later experiment requires a new prospective freeze.

## Bench release and independent custody

After Stages zero and one, all signatories must approve the same coupling model, protocol version and hashes before Stage two acquisition. Blank entries are not approvals. Publish only the secret key’s commitment hash before release.

| Item | Record to freeze |
| --- | --- |
| Apparatus | Actual frequencies, amplitudes, loads, shielding, geometry and gap; sensor axis, stiffness and bandwidth; photographs and wiring; calibration traceability, uncertainty and safe operating range. |
| Memory and coupling | Measured circuit response and uncertainty; component IDs and reference; complete Stage zero record including model, mapping, geometry, shielding response, independent contrast, predictor code and interpretation. |
| Sensitivity | Paired spread and dependence; day drift; nuisance transfers and covariance; total uncertainty budget; measured injection recovery; δ<sub>science</sub> or bound-setting objective; D and A<sub>test</sub>; control equivalence and drift limits. |
| Design | Exact primary and control counts by day; washout; assignment; exclusions and stops; custodian identity; secret key location and hash; access restrictions; release procedure and timestamps. |
| Analysis | Estimator, source and code hashes; fresh null and injection validation; interval and multiplicity rules; template, fit window and endpoint; immutable raw-data paths and checksums. |

Name a custodian independent of Matthew Wright, hypothesis development and outcome analysis; disclose affiliations and conflicts. Matthew cannot hold the key. The custodian seals label-revealing phase, memory, predictor and injection records. Analysts receive coded forces and predeclared non-revealing quality summaries. An authorized independent runner executes frozen code on complete records and seals outputs and exclusions before key release after the full run. Log access breaches and their effect on claim status.

### Required approval record

| Role | Sign-off responsibility | Name signature and date |
| --- | --- | --- |
| Laboratory lead | Calibration, controls, operating envelope and feasibility | Unappointed |
| Analysis lead | Frozen estimator, power, coverage and decision rule | Unappointed |
| Independent technical reviewer | Complete coupling specification, testable contrasts, uncertainty and permitted interpretation | Unappointed |
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

[[7] NIST  Standard deviation confidence limits](https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/sdconfli.htm)

[[8] Eöt-Wash  Results and interaction assumptions for force limits](https://www.npl.washington.edu/eotwash/results)

## Boardy recommendations and pilot record

The following record connects Boardy’s recommendations to the protocol. A written requirement is not a completed measurement or an approval. No laboratory engagement or endorsement is implied.

| Recommendation | Protocol response | Evidence status |
| --- | --- | --- |
| Identify physical memory | Measure circuit response separately. Stage zero requires the physical carrier and the assumption connecting voltage to interaction-producing memory. | Mapping unresolved |
| Specify the coupling path | Require source and probe properties, a force law, geometry and shielding response, a discriminating contrast and energy accounting before Stage two. P1 has the same gap. | Stage two blocked |
| Measure sensitivity first | Eight driven C ≈ 0 pairs precede full qualification. For the original 10 µN option, observed SD above 2 µN stops that plan before a full run. | Screen not run |
| Report real noise and nuisance transfer | Report measured SD with uncertainty, calibrated disturbance transfer and detectable amplitude D. State a weaker attainable bound honestly; retain the original scientific threshold. | Not measured |
| Independent custody and freeze | Matthew cannot hold the key. Name the custodian and laboratory, analysis and independent-review signatories in the approval record before acquisition. | Unappointed |

### Required pilot decision record

Before the screen, record the force template, window, nuisance limits and 2 µN ceiling. Compute s₈ from all eight paired force amplitudes in µN using the sample SD with divisor seven. Report the mean and uncertainty too. Invalid data give an incomplete screen; do not replace pairs selectively or repeat until a pass.

| Record | Required entry before a laboratory commits to Stage two |
| --- | --- |
| Screen result | Eight amplitudes, order, timestamps, raw-data and code hashes; mean, s₈, SD interval and dependence assessment. Current entry: NOT MEASURED. |
| Nuisance result | Dedicated perturbation ranges, transfer estimates and uncertainty; residual force budget and drift. Eight passive pairs do not supply this. Current entry: NOT MEASURED. |
| Capability and scope | D with uncertainty, injection recovery, objective and proposed counts. Convert a force interval to κ only after the model and normalization are released. Current entry: NOT QUALIFIED. |
| Decision and signatures | STOP ORIGINAL PLAN, PROCEED TO QUALIFICATION, or INCOMPLETE; reason, operator, lab lead and date. Stage two also requires the separate full signed release. Current entry: INCOMPLETE. |

For example, s₈ = 5 µN stops the original plan before any confirmatory run. Redesign or register a separately scoped bound-setting study prospectively; preserve the failed screen and do not relabel its noise as an achieved physics bound.
