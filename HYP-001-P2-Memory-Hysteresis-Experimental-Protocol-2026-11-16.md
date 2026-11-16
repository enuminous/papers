# EFMW memory hysteresis force experiment

**Publication status: proposed bench protocol v0.1; experiment NOT RUN; physical coupling UNRESOLVED.**

[Download the original Word protocol](HYP-001-P2-Memory-Hysteresis-Experimental-Protocol-2026-11-16.docx) · [Papers index](README.md)

HYP-001 P2  |  Proposed bench protocol v0.1  |  16 November 2026

Prepared for Matthew Chenoweth Wright and a participating experimental physics laboratory. This document specifies a proposed test; no apparatus performance or physical signal is reported as measured.

## Choice and bounded claim

Choose P2, memory hysteresis read out as force. It reuses the classical force apparatus needed for P1, while comparing different histories with identical present drive. That gives more discrimination per apparatus than a static force association. P3 adds a closed energy budget and P4 needs quantum hardware. This cost judgment assumes access to a calibrated force bench and DAQ; it is not a parts quotation.

The primary observable is the difference between high-history and low-history force residuals after both histories reach the same coherence C₁ = 0.5. HYP-001 predicts:

$$
\Delta F(t)=A e^{-t/\tau_M}, \qquad A=\kappa C_1\Delta M(0).
$$

Use nominal τM = 2 s, independently measured and frozen before force trials. Set the minimum effect of interest to |A| = 10 µN, approximately a 1 mg weight. For C₁ = 0.5 and ΔM(0) ≈ 1, this corresponds to |κ| = 20 µN. These are proposed engineering targets, not amplitudes or timescales derived by EFMW.

## Apparatus

| Item | Minimum implementation |
| --- | --- |
| Coherence source | Four phase-programmable electrical sine channels at 1 kHz, each nominally 1 V RMS into its own measured 1 kΩ resistor. Measure actual terminal phases and per-channel power; total source, controller and memory-circuit power are separate monitored quantities. |
| Physical memory | For this explicit realization, measured C drives a 0–1 V DAC followed by a buffered RC low-pass. Nominal 200 kΩ × 10 µF gives 2 s. Measure M as capacitor voltage divided by the calibrated voltage reference; identify the actual time constant with the force experiment disconnected. |
| Force readout | A grounded 10 g proof mass on a horizontal single-axis flexure, with optical or capacitive displacement readout and independently calibrated force conversion. Fix a 50 mm gap from the source shield to the near proof-mass surface; record dimensions and the sensitive-axis direction. |
| Isolation and controls | Source on a separate rigid support inside a conductive shield; common draft enclosure. Battery power and optical control avoid variable cable forces. Log proof-mass and source temperatures, base vibration, acoustic pickup and electromagnetic pickup. |
| Force calibration | An independently calibrated actuator applies blinded zero and ±10 µN exponential force injections. Establish static force scale, dynamic transfer and electronic pickup with a dummy readout. An actuator command is not itself a force calibration. |

Scope gate: the RC realization and this source–probe geometry are additional operational choices. Accept them as the tested realization before measurement. A null does not exclude couplings to other memory states, geometries, shielding conditions or timescales. The RC voltage decay alone is ordinary circuit behavior; the sought signal is an additional mechanical force.

## Acquisition and time resolution

| Channel | Proposed acquisition | Acceptance condition |
| --- | --- | --- |
| Force and displacement | 200 samples/s, synchronously timestamped | Analog anti-alias filter with 20 Hz passband and verified attenuation above 100 Hz. Calibrated readout settling to 95% within 0.2 s; include its full transfer function in the prediction. |
| Oscillator voltage and current | 20,000 samples/s per channel | Measure terminal signals rather than using commanded phases. Analog anti-alias filtering; adequate rejection above the 10 kHz Nyquist limit. |
| Coherence C and memory M | C from 10 ms phase-estimation windows; M at 200 samples/s | Archive raw voltage/current, computed C, capacitor voltage, clock and phase command. Inter-channel timing error below 1 ms. |
| Whole-device electrical input | 20,000 samples/s for voltage and current | Include controller and memory hardware, not only the four resistors. Retain power histories and supply ripple. |
| Environment | Temperature at 10 samples/s; vibration, acoustics and EM witness at 10,000 samples/s | Appropriate anti-alias filters. Calibrate nuisance-to-force transfer separately; equal nominal power does not establish equal thermal state. |

Sample rates are design choices for a seconds-scale response. The sampling interval does not define the number of independent observations. The statistical unit is a complete randomized history pair. A different independently measured τM requires a revised, frozen schedule before force data are unblinded.

## One history pair

| Stage | Instruction |
| --- | --- |
| Reset | Hold C = 0.5 for at least 10τM, and longer if witness channels require it. Pilot data define the washout and baseline acceptance limits. At nominal τM this is at least 20 s. |
| Condition | For 10τM, use high coherence with phases (0, 0, 0, 0), C ≈ 1; or low coherence with (0, π/2, π, 3π/2), C ≈ 0. Keep each load amplitude and frequency fixed. |
| Common present | Over a fixed 20 ms transition, move both histories to exactly the same waveforms, with phases (0, 0, π/2, π/2), giving C = 0.5. Record actual C and M throughout. Set t = 0 at the end of this transition. |
| Observe | Acquire for 5τM, nominally 10 s. The locked primary fit uses 0.25–10 s. Predict from measured C and M, including the transition and calibrated sensor transfer; do not assume an instantaneous ideal step. |
| Pair and blind | Repeat from reset with the other history. Randomize high-first versus low-first within each pair. A separate custodian retains the key; the force analyst receives coded runs and blinded calibration injections. |

For C = 0.5, accept measured coherence within ±0.01 and per-channel RMS power mismatch below 0.1% only if pilot nuisance calibration also bounds the resulting force bias. Keep record length, averaging, drive amplitude and phase-processing code identical across histories.

## Controls and fixed run count

Acquire 48 primary history pairs, split into 24 pairs on each of two separately calibrated days. Interleave 24 C = 0 control pairs and 24 controller-sham pairs, balanced between days. That is 96 pairs in total, about 2.7 hours of acquisition at the minimum nominal timing, excluding warmup, calibration and longer washout.

| Control | What it must establish |
| --- | --- |
| Zero coherence present | Apply the same high/low conditioning, then end with measured C ≈ 0. The κCM term predicts zero history force in the ideal C = 0 limit, even while memory differs. Use measured residual C to bound any allowed HYP contribution. |
| Controller sham | Run the same command-processing activity and coded labels, but keep physical phases at C = 0.5 throughout, with M driven by measured C. A label-correlated force here points to controller, acquisition or ordinary environmental effects. |
| Instrument and nuisance calibration | With phase histories disabled, inject known force, heating, vibration and electrical disturbances spanning the planned operating envelope. Quantify force-sensor creep, settling, dielectric and thermal lag, and pickup using actual measurement paths. |
| Positive injection | Recover blinded physical ±10 µN force histories through the full frozen pipeline with mean amplitude bias no greater than 1 µN. A software-added signal checks analysis only; it does not validate the apparatus. |

## Analysis qualification before hardware claims

HYP-001A reported 99.9% false positives for its naive regression and 9.9% for its nuisance-adjusted HAC regression at nominal 5% significance. Its adjusted pipeline is not qualified for a confirmatory force claim. Use a newly frozen estimator validated against known-zero histories before interpreting experimental residuals. [2]

Fit one signed amplitude per history pair to X(t) = C\_H(t)M\_H(t) − C\_L(t)M\_L(t), normalized by X(0) and passed through the measured sensor transfer. For identical present coherence this reduces to C(t)ΔM(t). Obtain the conventional force prediction and nuisance coefficients from separate calibration data. Do not choose τM, frequency band, fit window or nuisance terms after seeing condition-dependent force traces.

Use whole-pair randomization or a correlation-aware interval procedure whose complete decision rule has passed fresh null tests. Preserve within-run autocorrelation; do not use 200 Hz samples as independent replicates. Propagate force-scale, memory and nuisance uncertainty into the amplitude interval. The control-derived limits contribute to the primary systematic budget; do not add that same budget back to the control intervals a second time.

Proposed gate: use at least 10,000 fresh synthetic null repetitions for each declared stress family, including drift, thermal lag, crosstalk, imperfect nuisance sensors and order effects. Require the one-sided 95% upper bound on the false-positive rate to be ≤1%, and the 95% lower bound on power for ±10 µN injections to be ≥90%. Freeze calibration separately; a failure requires revised analysis and fresh validation data.

Pilot acceptance target: paired amplitude SD ≤2 µN, residual systematic uncertainty bounded by ≤2 µN, and force calibration drift ≤2%. With 48 independent pairs the ideal normal 99% random-error half-width would be about 0.74 µN before systematic uncertainty; this planning calculation is not a performance claim or a substitute for the empirical gate.

## Null positive and inconclusive outcomes

| Outcome | Required interpretation |
| --- | --- |
| Null at the target scale | After the frozen corrections, the combined 99% amplitude interval contains zero and lies entirely inside −10 to +10 µN; calibration and controls pass. Report the numerical interval and corresponding κ bound using measured C₁ΔM(0). This excludes the stated detectable range in this realization, not all nonzero κ. |
| Candidate positive | A signed history-force difference follows the frozen measured-memory template; its systematic-inclusive 99% interval excludes zero on each of the two days with the same sign. Both primary sessions and all controls pass. The sign is not predicted in advance; use two-sided tests. Record smaller-than-target effects explicitly rather than relabeling them as the target-sized result. |
| Confirmed anomaly only | A separate operator and independently calibrated instrument reproduce the frozen effect and its control behavior on new data. This supports an anomaly in this apparatus. An EFMW-specific interpretation still requires excluding conventional mechanisms and comparing alternative models. |
| Inconclusive | The interval overlaps zero and extends beyond the target range, sensitivity fails, the memory mapping is unaccepted, or conventional explanations cannot be separated. Publish UNRESOLVED; additional sampling requires a new prospectively specified run. |

## When the experimentalist stops

Before acquisition: stop if the physical meaning of M, the tested geometry, the independent τM measurement or the minimum effect of interest is not agreed. Do not replace an unidentified physical memory state with a fitted software timescale and call that a physical confirmation.

During qualification: stop if known-zero coverage fails, blind force injections are not recovered, the instrument cannot resolve the target, or a measured conventional effect is indistinguishable from the proposed template. A matching exponential is insufficient: load-cell creep itself can have exponential components. [3]

During acquisition: pause for sensor saturation, lost timing, calibration drift above 2%, a >1% shift in measured τM, or environmental/power conditions outside the frozen envelope. Retain all records. If exclusions exceed 5% of attempted pairs, terminate this run as a quality failure rather than selectively replacing bad outcomes.

After unblinding: stop attributing the signal to HYP-001 if it appears in controller shams, exceeds the measured allowance in the C = 0 control, or disappears under a calibrated conventional correction. Require control-effect 99% intervals to lie within ±2 µN after allowing measured residual coherence. If the primary result is null at target sensitivity, close this parameter range. If positive, stop tuning and arrange independent replication.

Run count is fixed. No stopping when significance first appears, extending until it appears, changing the sensitivity target after looking, or treating an unclosed energy budget as established energy creation.

## Bench release record

Complete and freeze this record after qualification, before decoding any physical force comparison. These entries define the tested realization and prevent the hypothesis from moving after a null.

| Item | Record to freeze |
| --- | --- |
| Apparatus | Source channel frequencies and amplitudes, resistor values, shield construction, proof-mass material and geometry, exact 50 mm gap, sensor axis and wiring photographs. |
| Memory | Acceptance of the RC realization; measured τM and uncertainty; voltage reference; capacitor and resistor IDs; measured C-to-M response and nonidealities. |
| Sensitivity | Independent force calibration and transfer function; paired-noise estimate; nuisance coupling measurements; total systematic budget; ±10 µN injection recovery. |
| Design | Washout duration; randomization seed and concealed key; custodian; day and run IDs; 48 primary pairs plus 24 pairs of each control; exact exclusion and stopping rules. |
| Analysis | Source and analysis code hashes; null-calibration results; interval construction; frozen fit window and endpoint; raw-data paths and recorded checksums. |

## References

[[1] Wright 2026  EFMW HYP 001  P2 and its physical scope](https://github.com/enuminous/papers/blob/e472280c6bfb8d1e3b2b318c7ee4b58a122bf045/EFMW-HYP-001-Testable-Physical-Predictions-2026-11-12.md)

[[2] Wright 2026  HYP 001A known zero recovery and failed calibration](https://github.com/enuminous/papers/blob/e472280c6bfb8d1e3b2b318c7ee4b58a122bf045/EFMW-HYP-001A-Known-Zero-Recovery-2026-11-13.md)

[[3] Bartel and Yaniv 1997  Load cell creep and recovery  NIST](https://pmc.ncbi.nlm.nih.gov/articles/PMC4894594/)

[[4] NIST  Force calibration via electrostatics](https://www.nist.gov/publications/force-calibration-electrostatics)

[[5] NI  Anti aliasing filters and their usage](https://www.ni.com/en/shop/data-acquisition/measurement-fundamentals/analog-fundamentals/anti-aliasing-filters-and-their-usage-explained..html)

Before release to the lab, freeze apparatus photographs and wiring, material/dimension records, calibration files, measured τM and its uncertainty, the permitted environment envelope, randomization/key custodian, code hashes, exact exclusions and the full decision rule. No custodian or laboratory engagement is assumed by this proposal.
