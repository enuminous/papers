# EFMW memory hysteresis force experiment

**Publication status: proposed bench protocol v0.2; experiment NOT RUN; physical coupling UNRESOLVED.**

[Download the revised Word protocol](HYP-001-P2-Memory-Hysteresis-Experimental-Protocol-2026-11-16.docx) · [Papers index](README.md)

**Revision v0.2 — 16 November 2026.** Supersedes [v0.1](https://github.com/enuminous/papers/blob/ba47f423b7991035113cd34c10f43aaea5ab9989/HYP-001-P2-Memory-Hysteresis-Experimental-Protocol-2026-11-16.md). Apparatus qualification now precedes a separately frozen experiment. Scientific effect size is separated from measured sensitivity; the RC memory mapping remains an explicit assumption. Independent custody covers label-revealing phase and memory records, with signed approval before confirmatory acquisition.

HYP-001 P2  |  Proposed bench protocol v0.2  |  16 November 2026

Prepared for Matthew Chenoweth Wright and a prospective experimental physics laboratory. Begin with apparatus qualification. A separate force experiment requires a signed protocol freeze and fresh data. No apparatus performance, physical signal, laboratory engagement or custodian appointment is reported as established.

## Choice and bounded claim

Choose P2, memory hysteresis read out as force, as a candidate for a classical bench study. It compares different histories at identical present drive and can reuse a P1 force apparatus. P3 requires a closed energy budget and P4 requires quantum hardware. The cost advantage remains conditional on access to suitable force metrology and data acquisition; it is not a parts quotation or a demonstrated cheapest test.

The primary observable is the difference between high-history and low-history force residuals after both reach the same coherence C₁ = 0.5. Conditional on the chosen physical mapping of memory and geometry, the HYP-001 phenomenological model gives [1]:

$$
\Delta F(t)=A e^{-t/\tau_M}, \qquad A=\kappa C_1\Delta M(0).
$$

The model does not supply a measured coupling κ, a lower bound on its magnitude, or a derived physical timescale. The former 10 µN target remains an illustrative planning benchmark only. It is neither demonstrated apparatus sensitivity nor an EFMW amplitude prediction. A null can constrain a specified coupling range in this realization; it cannot exclude every nonzero κ.

## Physical meaning of memory

Define the measured circuit state as capacitor voltage divided by its calibrated reference voltage. A 200 kΩ resistor and 10 µF capacitor give a nominal RC time of 2 s. Measure the actual response, uncertainty, leakage and temperature dependence with the force experiment disconnected. Freeze that measured circuit time before Stage two. Identifying it with τ<sub>M</sub> is an additional hypothesis, not a consequence of calibration.

Before a physical interpretation, record what object carries M, where it is located, how it couples to the probe, and why the effect should survive the selected shielding. Explain why this state should enter κCM rather than merely emulate its equation. An independent technical reviewer must distinguish evidence for that mapping from assumptions. If the mapping remains unsupported, label Stage two a conditional RC force search and retain UNRESOLVED for the EFMW interpretation.

For four measured oscillator phases, C is the squared magnitude of their mean unit phase phasor [1]. This definition gives C = 1 for equal phases, C = 0 for quadrature phases, and C = 0.5 for (0, 0, π/2, π/2). Archive the phase-estimation code and normalization. Neither a fitted force decay nor a successful RC calibration identifies a new physical interaction.

The RC realization, source–probe geometry and shielding are operational choices. Acceptance of this test scope does not establish that it realizes the physical memory responsible for an EFMW interaction. The capacitor decay is ordinary circuit behavior; the proposed observable is an additional mechanical force.

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

Record a pilot plan before collection: configurations, calibrated injection levels, block counts, disturbance ranges and analysis-development limits. Pilot data may develop the apparatus and estimator, but never enter the confirmatory sample. Freeze the revised estimator before fresh qualification data; retain failed attempts and identify every revision.

| Qualification block | Required measurement |
| --- | --- |
| Baseline and drift | Initial planning count: 24 zero-injection paired blocks, 12 on each of two days, with phase histories disabled and powered conditions representative of the experiment. Repeat the full reset and acquisition cycle. Estimate paired amplitude spread, day drift, order effects and dependence between blocks. |
| Physical injections | Preselect three traceably calibrated magnitudes spanning the prospective range, with six paired recoveries per sign and magnitude. Include 10 µN only if it can be generated and calibrated. Mask signs and magnitudes from the analyst. Report recovery bias, uncertainty and saturation; these counts support development, not a certified power claim. |
| Nuisance transfer | With phase histories disabled, vary heating, electrical pickup, vibration, acoustic input and tilt separately across the operating envelope. Measure creep and settling. Then run controller shams and C = 0 endpoint controls; the latter execute actual phase histories and transitions through the final wiring, shielding and acquisition path. |
| Fresh qualification | After freezing the candidate pipeline, acquire at least 12 fresh zero-injection control pairs across two days and repeat the selected blinded physical injections. Archive discrepancies. Freeze any required larger validation sample before collecting it; these small hardware samples cannot certify a 1% false-positive rate. |

Zero injection establishes no added calibration force; it does not prove the complete apparatus is free of forces. Document the null assumption for each control. Use dedicated disturbance calibration to estimate corrections. Do not learn nuisance coefficients from active high/low contrasts or subtract a history-correlated pilot residual as if its origin were known.

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

The former schedule of 48 primary pairs over two days, plus 24 C = 0 and 24 controller-sham pairs, is a planning example only. After qualification, freeze exact primary and control counts, allocation by day and order, and resource limits. Size the complete decision rule for both signs at A<sub>test</sub>, including the requirement for same-sign effects on each day. At least two separately calibrated days are required. A pooled 48-pair calculation does not establish power for each day.

| Control | What it must establish |
| --- | --- |
| Zero coherence present | Apply the same high/low conditioning, then end with measured C ≈ 0. The κCM term predicts zero history force in the ideal C = 0 limit, even while memory differs. Use measured residual C to bound any allowed HYP contribution. |
| Controller sham | Run the same command-processing activity and coded labels, but keep physical phases at C = 0.5 throughout, with M driven by measured C. A label-correlated force here points to controller, acquisition or ordinary environmental effects. |
| Instrument and nuisance calibration | Use independently measured disturbance transfer functions and frozen correction coefficients. Exercise both phase-disabled calibration and actual switching controls. Quantify creep, thermal and dielectric lag, pickup and order effects; freeze allowed control-effect bounds before Stage two. |
| Positive injection | Recover blinded zero and ±A<sub>test</sub> physical force histories through the frozen pipeline. Predefine allowable recovery bias and uncertainty as part of the total budget; demonstrate that they preserve planned sensitivity. Software-added signals validate analysis only. |

## Analysis qualification and frozen estimator

HYP-001A reported 99.9% false positives for naive regression and 9.9% for nuisance-adjusted HAC regression at nominal 5% significance [2]. Those are synthetic results, not force measurements. Neither pipeline is qualified for this confirmatory experiment. Validate a newly frozen estimator before interpreting experimental residuals.

Fit the signed force difference for each complete pair using the measured predictor X(t) = C<sub>H</sub>(t)M<sub>H</sub>(t) − C<sub>L</sub>(t)M<sub>L</sub>(t), passed through the calibrated sensor transfer. Fit a common coupling κ while retaining pair-specific predictor scales and uncertainties. Report amplitude A at the frozen reference C₁ΔM(0). A normalized amplitude fit is acceptable only if its conversion back to κ preserves those scales. Do not choose the decay time, band, fit window or nuisance terms from active force contrasts.

Use randomization inference at the actual randomized unit, or a validated correlation-aware interval method. Preserve within-run and between-pair dependence and day structure; do not treat 200 Hz samples as replicates. Propagate force-scale, memory, transfer-function and nuisance uncertainty into each interval. Specify distributions, covariance assumptions and how bounded biases enter the interval. Shared drift and systematic uncertainty do not shrink merely by dividing by the square root of the number of pairs. [6]

Run at least 10,000 fresh synthetic null repetitions for each declared stress family: drift, thermal lag, crosstalk, imperfect nuisance sensors, order effects and between-pair dependence. Validate the complete frozen decision rule, not only an isolated regression test. Require a one-sided 95% upper confidence bound on false-positive probability ≤1%, and a 95% lower bound on power ≥90% for each sign at ±A<sub>test</sub>. Use fresh injected repetitions for power, with counts frozen in advance. Include uncertainty in pilot-derived noise and nuisance parameters. Synthetic qualification does not establish that all physical confounders are represented.

Conditional planning example: if 48 independent paired amplitudes actually have SD 2 µN, their mean has standard error about 0.29 µN and an ideal normal 99% random-error half-width about 0.74 µN. These values exclude systematic uncertainty and do not describe the separate day tests. The former SD ≤2 µN and systematic ≤2 µN limits are withdrawn as universal entry gates; measured performance must support the frozen A<sub>test</sub>, control bounds and scientific objective.

Calibrate interval coverage at zero and across the proposed coupling range, and check robustness to model misspecification. Keep analysis-development, synthetic validation, physical calibration and confirmatory data identifiable and separate. If validation fails, revise the estimator and use new validation data. Do not reuse failed validation outcomes to claim an unchanged preregistered pass.

Control-derived uncertainty enters the primary budget once. Do not double-count it in control intervals or assume a non-significant control is acceptably small. Require the full control intervals to lie inside predeclared equivalence limits, allowing measured residual coherence where appropriate. These limits replace the universal ±2 µN requirement and must be justified against the chosen scientific target or bound-setting objective.

Freeze all primary and control endpoints, multiplicity handling, exclusions, confidence-interval construction and the complete positive/null decision rule before Stage two begins. Both signs require two-sided inference. The custodian runs the signed, frozen pipeline with the full phase and memory records; sealed results and quality-control decisions precede key release.

## Null positive and inconclusive outcomes

| Outcome | Required interpretation |
| --- | --- |
| Null within the tested range | Calibration and controls pass. The combined systematic-inclusive 99% amplitude interval contains zero and lies wholly inside ±δ<sub>science</sub>, if a scientific threshold was specified. Otherwise report its numerical endpoints as a bound-setting result. Translate to a κ interval using measured predictor scale and uncertainty. Close only the excluded range in this recorded realization. |
| Candidate positive | The frozen template fits a signed history-force difference and its systematic-inclusive 99% interval excludes zero on each separately calibrated day with the same sign. All controls, calibration and frozen decision gates pass. Report the amplitude and interval, including effects below A<sub>test</sub> or δ<sub>science</sub>; do not relabel them as target-sized results. |
| Confirmed anomaly only | A separate operator and independently calibrated instrument reproduce the frozen effect and control behavior on new data. This supports an apparatus anomaly. An EFMW-specific interpretation still requires a defensible physical mapping, exclusion of conventional mechanisms and comparison with alternative models. |
| Inconclusive | The interval cannot exclude the scientifically relevant range, required sensitivity or controls fail, the signal is confounded, or the physical interpretation remains unsupported. State which conclusion is UNRESOLVED. Report any valid apparatus-level interval separately; do not convert a failed quality gate into a physics bound. |

## When the experimentalist stops

Before Stage two: stop if calibration, physical-injection recovery, analysis qualification, custodian independence or required signatures are missing. An unsupported memory mapping permits only an explicitly approved conditional RC search; it cannot be released as a definitive EFMW test. Freeze either a justified δ<sub>science</sub> or an explicit bound-setting objective.

During qualification: stop advancement to Stage two if the chosen objective cannot be resolved, held-out validation fails, or a conventional effect is indistinguishable from the proposed template. Redesign or register a weaker bound-setting objective before new confirmatory data. A matching exponential is insufficient because force-sensor creep can also have exponential components. [3]

During Stage two: pause for saturation, lost timing, environmental excursions or calibration and memory drift beyond the frozen limits. Starting candidates are 2% force-scale drift and 1% circuit-time drift; retain them only if qualification shows they protect the uncertainty budget and can be measured reliably. Retain all records. Terminate as a quality failure if exclusions exceed 5% of attempted pairs; do not selectively replace outcomes.

After key release: withhold a HYP-001 attribution if the force follows controller shams, violates the C = 0 control allowance, or is explained by calibrated conventional corrections. Close a parameter range only when the valid interval and controls support it. A candidate positive triggers independent replication, with no retrospective retuning.

The confirmatory run count is fixed before collection. Do not stop when significance appears, extend until it appears, move thresholds after inspecting active contrasts, or treat an unclosed energy budget as established energy creation. Any later experiment requires a new prospective freeze.

## Bench release and independent custody

Freeze this record after Stage one and obtain every signature before Stage two acquisition. All signatories must approve the same protocol version and hashes. Blank entries are not approvals. Deposit only a commitment hash of the secret randomization key until release.

| Item | Record to freeze |
| --- | --- |
| Apparatus | Actual frequencies, amplitudes, loads, shielding, geometry and gap; sensor axis, stiffness and bandwidth; photographs and wiring; calibration traceability, uncertainty and safe operating range. |
| Memory | Circuit-state definition; measured response and uncertainty; component IDs and reference voltage; evidence and assumptions for the M mapping; permitted claim scope and reviewer decision. |
| Sensitivity | Paired spread and dependence; day drift; nuisance transfers and covariance; total uncertainty budget; measured injection recovery; δ<sub>science</sub> or bound-setting objective; D and A<sub>test</sub>; control equivalence and drift limits. |
| Design | Exact primary and control counts by day; washout; assignment method; exclusions and stops; custodian identity; secret key location and hash; access restrictions; release procedure and timestamps. |
| Analysis | Estimator, source and code hashes; fresh null and injection validation; interval and multiplicity rules; template, fit window and endpoint; immutable raw-data paths and checksums. |

The custodian must be independent of Matthew Wright, hypothesis development and outcome analysis, with affiliations and conflicts recorded. Matthew cannot hold the key. Phase traces, capacitor voltage, predictor signs and injection metadata can reveal assignments: keep them with the custodian until release. The analyst receives coded force data and predeclared non-revealing quality summaries. An independent custodian or authorized runner executes the frozen code on complete records, seals all outputs and exclusions, then releases the key after the full run. Record any access breach and its effect on claim status.

### Required approval record

| Role | Sign-off responsibility | Name signature and date |
| --- | --- | --- |
| Laboratory lead | Calibration, controls, operating envelope and feasibility | Unappointed |
| Analysis lead | Frozen estimator, power, coverage and decision rule | Unappointed |
| Independent technical reviewer | Memory mapping, uncertainty budget and permitted interpretation | Unappointed |
| Independent key custodian | Independence, access controls, commitment and key-release record | Unappointed |
| Matthew Chenoweth Wright | Hypothesis, conditional scope and closure after a qualified null | Pending signature |

No appointment or engagement is assumed. Record key release separately after sealing results, exclusions and quality decisions.

## References

[[1] Wright 2026  EFMW HYP 001  P2 and its physical scope](https://github.com/enuminous/papers/blob/e472280c6bfb8d1e3b2b318c7ee4b58a122bf045/EFMW-HYP-001-Testable-Physical-Predictions-2026-11-12.md)

[[2] Wright 2026  HYP 001A known zero recovery and failed calibration](https://github.com/enuminous/papers/blob/e472280c6bfb8d1e3b2b318c7ee4b58a122bf045/EFMW-HYP-001A-Known-Zero-Recovery-2026-11-13.md)

[[3] Bartel and Yaniv 1997  Load cell creep and recovery  NIST](https://pmc.ncbi.nlm.nih.gov/articles/PMC4894594/)

[[4] NIST  Force calibration via electrostatics](https://www.nist.gov/publications/force-calibration-electrostatics)

[[5] NI  Anti aliasing filters and their usage](https://www.ni.com/en/shop/data-acquisition/measurement-fundamentals/analog-fundamentals/anti-aliasing-filters-and-their-usage-explained..html)

[[6] NIST  Basic definitions of measurement uncertainty](https://physics.nist.gov/cuu/Uncertainty/basic.html)
