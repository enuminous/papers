# Two Oscillators, One Missing Force
## Monolithic's latest EFMW experiment finds measurable information—and a stubborn gap between correlation and gravity

**Science feature · 28 October 2026**  
**Research:** Matthew Chenoweth Wright / Monolithic LLC; model and analysis developed with AI assistance  
**Evidence basis:** Published TOE-001 F01–F03 protocols, source code, frozen synthetic results, and GitHub Actions. **No laboratory data were collected or analyzed for this study.**

---

The two oscillators were supposed to share information.

Not messages, consciousness or a mysterious cosmic signal. Information in the strict statistical sense: knowing the displacement of one oscillator should tell an observer a little about the displacement of the other.

When two objects are coupled by a restoring force, their movements are no longer independent. A statistical measurement can detect that relationship. Yet the Einstein–Feynman–Maxwell–Wright (EFMW) research program asks a substantially more ambitious question: might an informational contribution also enter the gravitational equations governing spacetime?

In a new stage of Matthew Chenoweth Wright's Monolithic research project, the first proposition survived a deliberately more realistic simulation. The second remains unproved.

In **F03**, the latest [TOE-001 experiment](https://github.com/enuminous/TOE-001/blob/main/F03_TWO_OSCILLATOR_MEASUREMENT_PROTOCOL.md), researchers simulated two noisy, damped and coupled oscillators through 200,000 steps of classical dynamics. After discarding the burn-in period and sampling the remaining trajectory, they estimated **0.008251 nats** of mutual information from 30,000 paired position readings. The independently specified equilibrium model predicted **0.007874 nats**.

The values agreed within the experiment's exploratory uncertainty interval. But the agreement was with the **ordinary theory of classical coupled oscillators**, not a new law of informational gravity.

That distinction is the main result.

### Why two oscillators?

The historical EFMW equations ME-006 and ME-007 propose that a tensor associated with information and recursive processes may contribute to Einstein's gravitational source. The original ME-006 expression combines familiar scalar-field stress-energy terms with a recursive remainder. The missing piece is an independently defined physical law for that remainder: what can be measured, where, and how does it affect matter or spacetime?

The TOE-001 project has tried to turn this ambiguity into a sequence of tests that can actually fail.

An earlier analysis demonstrated that an ordinary two-scalar gravitational system could be decomposed into named “ordinary” and “informational” stress components, while retaining the same total gravitational source. But the decomposition was not unique. Changing the bookkeeping allocation could change the claimed informational tensor without changing the physical dynamics.

That is a warning about interpretation, not a discovery that gravity depends on how researchers label an equation.

The follow-up, **F01**, pursued an information quantity that did not depend on those arbitrary allocations. It identified Gaussian mutual information between two measured oscillator coordinates in a specified thermal equilibrium ensemble. For positive-definite stiffness parameters, the standard statistical prediction is

\[
\mathcal M
=-\frac12\ln(1-\rho^2)
=\frac12\ln\left(\frac{m^2M^2}{m^2M^2-\gamma^2}\right),
\]

where \(m^2\) and \(M^2\) represent the two uncoupled stiffnesses, \(\gamma\) is the coupling, and \(\rho=-\gamma/\sqrt{m^2M^2}\) is the signed equilibrium correlation.

This gives a genuine operational question. Two position sensors can, in principle, measure the covariance and test the prediction without referring to a gravitational field equation.

But mutual information is a **statistical scalar measured in nats**. A gravitational stress tensor has a different mathematical role, dimensions and transformation properties. Identifying one with the other requires physical definitions that were not supplied by the formula.

In **F02**, the research introduced a new scalar field into an explicitly covariant gravitational action. The resulting equations were consistent within a conventional scalar–tensor framework, but the tempting move of equating that local gravitational field to the fixed nonzero F01 equilibrium information generally violated the field's own equation of motion.

Another shortcut failed.

The natural next question was therefore smaller and more testable: could the supposedly measurable information quantity be recovered from an independently generated *dynamical* record rather than sampled directly from the desired Gaussian distribution?

### A simulation with memory in time

F01 had generated independent synthetic samples from its specified equilibrium covariance. That is useful for checking a formula or statistical estimator, but it is not a stringent test of whether the dynamics produce that covariance.

F03 changed the generator.

The new model uses the standard underdamped **Langevin equations**. Each oscillator feels an ordinary restoring force and a coupling to the other oscillator, together with damping and independent stochastic forcing. A conventional fluctuation–dissipation relation determines the noise strength. The simulation evolves this system with the established BAOAB integration method.

Unlike independent Gaussian draws, the resulting trajectory has temporal structure. An oscillator's position now is related to its position a moment ago, and the two oscillators can influence one another over time.

The frozen reference run uses illustrative, dimensionless parameters: stiffnesses of 1 and 4, coupling 0.25, inverse temperature 1, damping 0.8 and step size 0.04. It evolves **200,000 steps**, discards the first **20,000**, and retains every sixth subsequent position pair, yielding **30,000 paired samples**.

Only after generating those samples does the separate analysis estimate position covariance and Gaussian mutual information.

This is an important methodological advance over F01. The dynamics and information estimator are distinct calculations. If the solver, noise prescription, equilibration or sampling procedure is wrong, the reported information need not match the independent equilibrium expectation.

It is still a simulation of familiar physics, not an independent experiment in nature.

### What the record shows

The [frozen F03 result](https://github.com/enuminous/TOE-001/blob/main/results/f03_oscillator_reference.json) reports the following values:

| Quantity | Result |
|---|---:|
| Predicted classical equilibrium mutual information | 0.007874178484 nats |
| Estimated mutual information from simulated trajectory | 0.008250895642 nats |
| Expected signed correlation | −0.125000 |
| Estimated signed correlation | −0.127931 |
| Exploratory moving-block 95% interval | 0.006049–0.010775 nats |
| Retained paired samples | 30,000 |

The recorded interval includes the expected value, but it is **not a preregistered discovery interval**. Its moving-block resampling length of 173 samples has not been validated against the autocorrelation structure of real instruments. The two halves of the same trajectory also produced somewhat different estimates, approximately 0.00675 and 0.00989 nats.

Those differences are a reminder that physical time-series measurements are not simply large collections of independent points.

The researchers also examined time-shifted nulls. Offsetting one record against the other breaks the aligned relationship while preserving much of each stream's internal behavior. Across the frozen shifts, the median estimated mutual information was about **0.0000236 nats**, with a maximum of about **0.000408 nats**—far below the aligned estimate.

This supports the interpretation that the simulated coupling produces a real within-model statistical dependence. It does **not** constitute a formal statistical rejection of every alternative, nor does the null analysis identify any additional EFMW force.

The repository includes an [executable oscillator model](https://github.com/enuminous/TOE-001/blob/main/toe001/me007_experiment.py), [18 focused regression tests](https://github.com/enuminous/TOE-001/blob/main/tests/test_me007_experiment.py), and a [successful GitHub Actions run](https://github.com/enuminous/TOE-001/actions/runs/40777742179). These document the calculation and software checks, not independent laboratory replication.

### What an actual experiment would require

The most consequential part of F03 may be its readiness to accept data that do not originate inside the simulation.

The repository's [CSV analysis runner](https://github.com/enuminous/TOE-001/blob/main/scripts/run_f03_oscillators.py) accepts time-stamped paired position readings and a separately specified calibration record. It checks monotonic timestamps, calculates covariance, handles certain independently characterized sensor-noise terms and saves input-file hashes.

But parsing a data file cannot prove that the file came from a real instrument, was calibrated correctly or represented thermal equilibrium. The code explicitly labels external files as **user-supplied, not independently authenticated**.

To run the test honestly, researchers would need two distinguishable physical modes, independent estimates of their stiffness and coupling, measurement of damping and noise, a clearly defined temperature or forcing distribution, and held-out simultaneous sensor recordings. Inferring coupling from the same covariance later used to “confirm” its predicted mutual information would make the comparison circular.

Zero-coupling trials, sign-reversed coupling where feasible, monitoring of sensor cross-talk and blocked uncertainty estimates would all matter.

An intriguing starting point already exists beyond the simulation. A publicly available dataset, [*Mimicking Cochlear Pre-Processing using Critically Coupled MEMS Sensors*](https://zenodo.org/records/18336535), describes real measurements of two coupled microelectromechanical resonators. The collection, published on Zenodo in 2026 and amounting to about **35.1 GB**, includes paired high-rate recordings, feedback settings and driven frequency sweeps.

Those files have not been downloaded or analyzed for F03. And the dataset cannot simply be treated as the equilibrium system F03 models. Its driven, feedback-controlled and sometimes nonlinear behavior would require a justified nonequilibrium analysis or a defensible stationary subset.

That is the point of an authentic experiment: the measurement is allowed to disagree with the model.

### Measurable information is not yet information gravity

The completed synthetic test confirms that, given conventional coupled-oscillator dynamics and a suitable equilibrium regime, a correlation-based information prediction can be recovered from independently evolved time-series samples.

It does **not** show that the mutual information determines a local gravitational scalar field, that the gravitational field couples to it with a specific strength, or that ME-006's recursive stress tensor has been uniquely identified.

Those remain separate scientific questions.

The gravitational theory would need a noncircular law mapping actual physical observables to a locally defined information field, an action or constitutive equation determining its dynamics, and a quantitative prediction that ordinary oscillator theory and conventional scalar–tensor gravity cannot explain equally well.

Neither more simulated oscillator trajectories nor a perfectly matched covariance can provide that missing physical law by themselves.

### Why a limited result can still matter

Researchers often face a choice between making their prototypes sound revolutionary and making them difficult to fool. F03 leans toward the second approach.

It replaces direct equilibrium draws with an evolving stochastic system. It preserves time dependence, uses a null comparison and treats uncertainty as a question rather than decoration. It distinguishes source code from actual apparatus, and calibration files from externally authenticated measurements.

Its reported success is specific: **a conventional information-theory prediction survived an end-to-end synthetic dynamics test**.

Its unresolved result is equally specific: **the step from that measured statistical information to an EFMW-specific gravitational stress tensor remains physically unestablished**.

That outcome neither proves nor refutes EFMW as a whole. It clarifies the standard a future attempt must meet.

The immediate next step is to examine independent physical oscillator recordings against the correct model for their actual experimental conditions. The larger and harder task is to derive a unique, measurable difference between informational gravity and standard theories, then put that difference in front of nature.

For now, two oscillators shared measurable information in a simulation.

**They did not reveal a new force.**

And publishing that distinction is part of doing the science properly.

---

### Sources and provenance

This feature is grounded in [TOE-001 F03's technical protocol](https://github.com/enuminous/TOE-001/blob/main/F03_TWO_OSCILLATOR_MEASUREMENT_PROTOCOL.md), [frozen result](https://github.com/enuminous/TOE-001/blob/main/results/f03_oscillator_reference.json), [implementation](https://github.com/enuminous/TOE-001/blob/main/toe001/me007_experiment.py), [18 regression tests](https://github.com/enuminous/TOE-001/blob/main/tests/test_me007_experiment.py), and [successful CI check](https://github.com/enuminous/TOE-001/actions/runs/40777742179). The preceding [F01](https://github.com/enuminous/TOE-001/blob/main/F01_ME007_INFORMATION_IDENTIFICATION.md) and [F02](https://github.com/enuminous/TOE-001/blob/main/F02_COVARIANT_INFORMATION_ACTION.md) studies provide the history of the question. The independent [Zenodo MEMS archive](https://zenodo.org/records/18336535), DOI 10.5281/zenodo.18336535, was inspected as a data-source candidate; its raw measurements were not analyzed.

Wright's EFMW program is the motivating research context. Standard Gaussian mutual information, Langevin dynamics, fluctuation–dissipation physics, and scalar–tensor field theory are established scientific methods, not claimed as original EFMW discoveries. The model, code and this article were prepared with AI assistance. No interviews, physical measurements or independent discovery claims have been fabricated.
