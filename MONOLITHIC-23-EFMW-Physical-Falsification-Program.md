# The Monolithic Twenty-Three
## A Falsification-First Experimental Program for Testing EFMW at the Boundary of Established Physics

**Matthew Chenoweth Wright — Monolithic LLC**  
**Protocol manuscript prepared with AI assistance — 28 October 2026**  
**Version:** 0.1, **PROPOSED / NOT PREREGISTERED / NOT EXECUTED AS A 23-TEST CAMPAIGN**

### Abstract

The Einstein–Feynman–Maxwell–Wright (EFMW) research program comprises proposed field equations, informational and recursive dynamics, cosmological extensions, computation, and formal mathematical models. Its physical content must be distinguished from familiar general-relativistic, quantum-field-theoretic, scalar-field, information-theoretic, and signal-processing consequences. We propose **23 bounded tests** intended to separate (i) mathematical admissibility and specification adequacy; (ii) observational compatibility with established physics; and (iii) genuinely discriminating empirical evidence for an independently derived EFMW-specific effect. The docket comprises three foundational consistency/identifiability challenges, eighteen public-observation analyses, and two inexpensive laboratory analogues. Open datasets include Pantheon+ supernovae, DESI baryon acoustic oscillations, public cosmic microwave background maps, gravitational-wave strain, pulsar and magnetar catalogs, and Gaia astrometry. Each test specifies the relevant source or apparatus, a conventional control, a potential falsifier, and a *prediction readiness gate*. At this stage, the majority of proposed EFMW-specific predictions are **not frozen**, so the correct status for them is **UNRESOLVED**, not a retrospective PASS or FAIL. The primary recommendation is to freeze a single identifiable and quantitatively distinctive claim, then compare it against the best relevant conventional alternatives on held-out or independently reproduced observations. This manuscript contains an experimental plan, not new measurements or an experimental confirmation of fundamental EFMW physics.

**Keywords:** EFMW; falsification; general relativity; cosmology; informational stress-energy; supernovae; DESI; cosmic microwave background; gravitational waves; pulsars; quantum gravity; observational controls; preregistration; reproducibility.

---

## 1. Research question

What, if anything, does EFMW predict about the physical universe that is not already predicted by a conventional theory with equivalent assumptions and model flexibility?

A general scheme for the problem is

\[
\Delta\mathcal O(D;\theta,\eta)
=\mathcal O_{\mathrm{EFMW}}(\theta,\eta)
-\mathcal O_{\mathrm{reference}}(\theta_0,\eta_0),
\]

where \(\mathcal O\) is a measurable observable; \(D\) denotes the domain or physical configuration; \(\theta\) are physical parameters; and \(\eta\) are nuisance parameters, instrumentation, selection and environmental effects. The two compared models must use **appropriate matched treatment of their free parameters and priors**, rather than interpreting the flexibility of the larger model as an automatic discovery.

A **consistency test** asks whether a fully specified model remains compatible with known results. A **discriminating test** demands a prediction that survives data and distinguishes the EFMW model from applicable conventional alternatives. An independent test can constrain or exclude an EFMW candidate even if the broader research framework remains viable.

A failure of a specific candidate does not refute every mathematical object in the EFMW portfolio. Conversely, proving an identity or reproducing a benchmark does not verify EFMW as a theory of nature.

### 1.1 Current state of the candidate models

The canonical [102-equation catalogue](https://github.com/enuminous/Monolithic_102_EFMW) is a preserved collection with heterogeneous statuses. The [frozen review](https://github.com/enuminous/EFMW) explicitly identifies mathematical and physical obligations, including the curved-space wave operator, original informational-tensor conservation, open analytic semantics and physical identification of observables. A Lean success applies only to the theorem and assumptions actually encoded.

[TOE-001's ME-007 integration](https://github.com/enuminous/TOE-001/blob/main/ME007_INTEGRATION.md) defines **one** conventional two-scalar allocation reproducing the *form* of the canonical equation

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G(T_{\mu\nu}+\kappa I_{\mu\nu}),
\]

and shows conditional on-shell conservation, but the split into ordinary and informational sectors is **non-unique**. No independent informational observable has been identified, and the historical ME-007 tensor has not been derived.

The frozen [C1Q cosmology](https://github.com/enuminous/Cosmology) is based on ordinary general relativity and a chosen canonical scalar with a quadratic potential. It computes cosmological quantities but has not, merely by being called EFMW, acquired an EFMW-specific observational signature.

The [pulsar-glitch resonance proposal](https://github.com/enuminous/EFMW-Neutron-Star-Glitch-Resonance) offers a decaying sinusoidal transient with a mathematical peak-time ratio near \(0.402\) of the characteristic interval for a particular definition of the waveform. Whether pulsars exhibit this behavior, whether the timescale is physically predicted rather than fitted, and whether ordinary glitch models explain it remain open.

Earlier [EFMW-EXP-001](https://github.com/enuminous/EFMW-EXP-001/blob/main/CONFIRMATORY_RECONCILIATION.md) reports a reproducible *synthetic monitoring* benefit under its defined comparator; it is **not an experimental test of EFMW fundamental physics**. Existing negative and limited results are retained, not edited away.

## 2. Test classes, status vocabulary and measurement discipline

**Class F — foundational gates** (tests 1–3): equations, dimensions, identifiability and comparison with conventional mathematical descriptions. These may be performed with local source code but cannot independently establish new physics.

**Class O — observational constraints** (tests 4–21): physical measurements already acquired by observatories. Tests can reject or constrain specified EFMW candidates. Evidence for EFMW-specific novelty requires more than fitting the data.

**Class L — laboratory analogues** (tests 22–23): inexpensive apparatus testing the correctness and utility of mathematical dynamics. Such demonstrations cannot validate a universal information field unless an independently justified bridge from the apparatus to the fundamental hypothesis is supplied.

The mandatory vocabulary is:

| Status | Meaning |
|---|---|
| **PASS—CONSISTENCY** | A frozen candidate satisfies a specified mathematical or observational check. This does *not* show uniqueness or novelty. |
| **PASS—DISTINCTIVE EVIDENCE** | A prespecified, physically grounded EFMW-specific prediction survives independent data and appropriately outperforms the strongest relevant conventional controls. |
| **FAIL** | A defined candidate violates a mathematical gate, a predeclared bound, or an observational acceptance criterion under the given assumptions. |
| **UNRESOLVED** | The candidate lacks a defined observable, frozen physical parameterization, accessible data, viable likelihood, or adequate independent validation. |
| **N/A** | Inapplicability is positively justified; it is not a substitute for missing evidence. |

No experiment in this docket is reported as completed *by this manuscript*. Previously published computational checks retain their separate source-specific status.

## 3. The 23 experiments

The following order preserves the original Monolithic-23 research shortlist. **Priority order is not a claim about statistical significance, imminent discovery, or ease of eventual publication.** A low-cost public-data download can still demand advanced physics, large compute, or expert review.

### F01 — ME-007 informational-tensor identifiability

**Target:** Determine whether the \(I_{\mu\nu}\) in the original ME-007 equation has observable content that cannot be shifted between stress-energy accounts by redefining the partition.  
**Inputs:** Canonical ME-007 entry; TOE001–ME007–r1 action, tensor decomposition and energy-exchange identities.  
**Control:** The same two-scalar Einstein–matter theory with alternative allocations \(\alpha\), normalizations \(\kappa\), and a full unsplit stress tensor.  
**Required prediction:** An independently defined, measurable information functional or constitutive law that fixes \(I_{\mu\nu}\) *without using the desired Einstein source as its definition*.  
**Falsifier:** If all proposed observables depend only on \(T+\kappa I\) while the partition remains arbitrary, the unique-information interpretation fails *for the tested construction*.  
**Readiness:** **UNRESOLVED for uniquely physical EFMW**. A non-uniqueness result is already documented in TOE-001.  
**Effort:** Low for symbolic algebra; high for establishing independent physical semantics.

### F02 — ME-002 dimensional and source-convention closure

**Target:** Fix consistent units for the scalar wave operator, \(\phi\), its source variables \(E,P\), and any physical propagation velocity.  
**Inputs:** Original canonical ME-002/003/004/005 formulas; frozen sign conventions; physical definitions proposed for the source.  
**Control:** Standard covariant scalar wave/Klein–Gordon and acoustic equations under equal source assumptions.  
**Required prediction:** A source with dimensions and sign defined once, appropriate initial/boundary conditions, causal propagation and a measured coupling.  
**Falsifier:** An irreparable dimensional or sign contradiction under the proposed variable identification, or failure of a necessary known limit.  
**Readiness:** **UNRESOLVED** pending the physical meaning of the original source terms.  
**Effort:** Low for symbolic and dimensional audit; independent propagation data are a later gate.

### F03 — TOE-001 conventional two-scalar subtraction

**Target:** Test whether TOE-001 predicts anything beyond a standard two-scalar effective field theory.  
**Inputs:** TOE-001 frozen action, homogeneous oscillators, retarded memory reduction and optional FLRW model.  
**Control:** An ordinary two-scalar gravitational model with *identical action, coupling, initial conditions and observation map*.  
**Required prediction:** A new dynamical law, nontrivial measurement portal, or selection rule that cannot be absorbed into the conventional model.  
**Falsifier:** If all observables agree identically under the matched action, a claim of distinctive EFMW physics from this model fails, even if implementation and conservation checks pass.  
**Readiness:** Current TOE-001 construction reproduces conventional equations; **physical novelty UNRESOLVED**.  
**Effort:** Low for exact algebra and numerical comparison.

### O04 — Pantheon+ Type Ia supernova distance–redshift test

**Target:** Confront the *frozen* C1Q expansion \(H(z)\) with Type Ia supernova distances.  
**Data:** [Pantheon+ data release](https://github.com/PantheonPlusSH0ES/DataRelease), particularly the documented distances and covariance.  
**Control:** Flat \(\Lambda\)CDM, and a conventional quadratic-quintessence scalar with comparable freedom; calibrations and supernova nuisance parameters must be handled consistently.  
**Statistic:** Covariance-aware likelihood or \(\chi^2=(\boldsymbol\mu_{\rm obs}-\boldsymbol\mu_{\rm model})^\top C^{-1}(\boldsymbol\mu_{\rm obs}-\boldsymbol\mu_{\rm model})\), with justified treatment of absolute-magnitude/Hubble degeneracy.  
**Falsifier:** A prespecified out-of-sample or goodness-of-fit failure after accounting for covariance, selection and legitimate nuisance freedoms.  
**Caveat:** If C1Q has the same equations as ordinary quintessence, agreement tests quintessence rather than a new EFMW law.  
**Readiness:** C1Q equations are frozen; empirical comparison not reported here. **Highest-value initial observational analysis.**  
**Effort:** Low–moderate after reproducing the official likelihood.

### O05 — DESI DR2 baryon acoustic oscillation test

**Target:** Compare C1Q predictions for \(D_M(z)/r_d\), \(D_H(z)/r_d\) and/or \(D_V(z)/r_d\) as appropriate to the released data.  
**Data:** [DESI DR2 publication data and chains](https://data.desi.lbl.gov/doc/papers/dr2/). Some supporting cosmology products are public; underlying full DR2 spectra/redshifts may not be available in the same form.  
**Control:** \(\Lambda\)CDM and conventionally parameterized dynamical dark energy.  
**Statistic:** Published BAO likelihood/covariance and predeclared goodness-of-fit and complexity penalties; carefully specify any sound-horizon prior.  
**Falsifier:** Exclusion of the fixed C1Q point or family at the defined confidence/credibility level.  
**Readiness:** C1Q candidate exists; exact tested likelihood/pipeline needs freezing.  
**Effort:** Low–moderate for released summary products; substantially more for raw reduction.

### O06 — Cosmic chronometer expansion rate

**Target:** Evaluate C1Q \(H(z)\) against published differential-age cosmic-chronometer measurements.  
**Data:** Peer-reviewed \(H(z)\) compilations with measurement provenance and any shared systematic covariance.  
**Control:** \(\Lambda\)CDM and matched quintessence; do not treat chronometer points as perfectly independent without evidence.  
**Statistic:** Calibrated likelihood for the chosen catalog, including stellar-population nuisance/systematics.  
**Falsifier:** Prespecified incompatibility with the chronometer data or failure of consistency with the supernova/BAO constraints.  
**Readiness:** Data collection and covariance audit necessary; no uniquely EFMW signal yet.  
**Effort:** Low–moderate.

### O07 — Growth of cosmic structure

**Target:** Compute and test \(f\sigma_8(z)\) for the selected candidate's scalar perturbations.  
**Data:** Public redshift-space-distortion/growth-rate measurements, with survey-dependent covariance and assumptions.  
**Control:** \(\Lambda\)CDM and physically equivalent standard scalar dark-energy models.  
**Statistic:** Joint growth likelihood and a check that background-only fitting has not silently imposed the observed growth history.  
**Falsifier:** Failure to reproduce observed growth within frozen parameter/nuisance bounds.  
**Readiness:** Full perturbation prescription must be validated for the specific revision being tested.  
**Effort:** Moderate.

### O08 — Weak gravitational lensing and matter clustering

**Target:** Test \(S_8\), shear two-point statistics or equivalent model observables under C1Q.  
**Data:** Public KiDS/DES shear likelihoods and accompanying covariance, masks and nuisance specifications.  
**Control:** \(\Lambda\)CDM/quintessence with matched intrinsic-alignment, photo-\(z\), baryonic and selection treatment.  
**Statistic:** Official likelihood or an independently checked reproduction.  
**Falsifier:** Reproducible inconsistency beyond permitted systematics.  
**Readiness:** Observable pipeline and bias modeling not frozen.  
**Effort:** Moderate–advanced.

### O09 — CMB temperature and polarization spectrum

**Target:** Compare predicted \(C_\ell^{TT},C_\ell^{TE},C_\ell^{EE}\) and relevant lensing observables with public CMB products.  
**Data:** [NASA LAMBDA archive](https://lambda.gsfc.nasa.gov/product/) and linked Planck/WMAP products.  
**Control:** Standard \(\Lambda\)CDM and a conventional scalar-field cosmology using the same primordial spectrum and recombination assumptions.  
**Statistic:** Valid published likelihood, not comparison to a visually pleasing power-spectrum plot.  
**Falsifier:** The chosen model's spectrum fails prespecified constraints after propagated numerical and calibration uncertainties.  
**Readiness:** C1Q CLASS integration exists but data-level model comparison is not established here.  
**Effort:** Moderate–advanced.

### O10 — Cosmological preferred rotation axis

**Target:** Search for a predicted preferred direction or anisotropic signal from a **separately defined rotating EFMW spacetime**.  
**Data:** Public Planck/WMAP full-sky temperature and polarization maps with frequency channels, masks and noise/foreground simulations.  
**Control:** Isotropic Gaussian \(\Lambda\)CDM mock skies processed through the *same* axis-search pipeline, plus foreground and scan-systematic nulls.  
**Statistic:** A preregistered directional estimator, global significance calibrated over all searched directions and multipoles.  
**Falsifier:** Nondetection sufficiently constrains the predicted amplitude; detections that disappear under foreground/mask changes do not pass.  
**Readiness:** **BLOCKED until the theory provides a quantitative anisotropic observable.** Existing isotropic FLRW C1Q cannot do this.  
**Effort:** Moderate–advanced.

### O11 — Directional supernova expansion

**Target:** Test a prespecified sky-dependent expansion residual/dipole/rotation signature.  
**Data:** Pantheon+ sky coordinates, distance moduli and selection/covariance records.  
**Control:** Isotropic cosmology with survey footprint, peculiar velocities, redshift systematics and dust effects modeled.  
**Statistic:** Full-sky likelihood with trials-factor correction and, where possible, geographically distinct held-out surveys.  
**Falsifier:** Predicted directional dependence is absent or is explained by survey geometry and local flows.  
**Readiness:** The EFMW angular function, amplitude and scale must be frozen first.  
**Effort:** Low–moderate in code, advanced in bias control.

### O12 — Gravity/light propagation-speed constraint

**Target:** Test whether an explicit EFMW model predicts \(c_{\rm GW}\neq c_{\rm light}\).  
**Data:** [GW170817 strain and associated multimessenger observations](https://gwosc.org/events/GW170817/) plus established published joint-arrival constraints.  
**Control:** General relativity's propagation speed, with astrophysical source-delay nuisance bounds.  
**Statistic:** Predicted propagation time/distance effect compared to published confidence bounds, including source-emission uncertainty.  
**Falsifier:** A required EFMW speed deviation exceeds the allowed range under the same source-delay assumptions.  
**Readiness:** No specific nonzero EFMW speed shift is fixed in the cited core documents. A GR-compatible prediction would pass a *constraint* but add no novelty.  
**Effort:** Low for reinterpretation of published bounds.

### O13 — Gravitational-wave dispersion

**Target:** Derive a frequency-dependent waveform phase/dispersion correction from an EFMW action, not from an ad hoc fitted phase term.  
**Data:** [GWOSC strain data and tutorials](https://gwosc.org/tutorials/), suitable public event samples and detector noise estimates.  
**Control:** General-relativistic waveforms with calibration, spin/precession, eccentricity and environmental effects where applicable.  
**Statistic:** Corrected waveform likelihood, posterior predictive checks, model-complexity and injection/recovery studies.  
**Falsifier:** Bound excludes the frozen predicted dispersion; a post-hoc extra parameter with no microphysical EFMW derivation is exploratory only.  
**Readiness:** **BLOCKED on a unique dispersion law.**  
**Effort:** Moderate–advanced.

### O14 — Extra gravitational-wave polarizations

**Target:** Test a physically derived tensor/vector/scalar polarization content distinct from GR's two tensor modes.  
**Data:** Public multibaseline/interferometer observations with detector antenna responses.  
**Control:** GR tensor-only signals, detector geometry and calibration.  
**Statistic:** Network response with correct sky-position degeneracies, injection studies and model selection.  
**Falsifier:** Predicted mode amplitude or polarization fraction conflicts with the data's sensitivity and degeneracies.  
**Readiness:** Proposed field equations must first supply a consistent linearized spectrum and couplings.  
**Effort:** Advanced; not a novice single-afternoon experiment.

### O15 — Pulsar-timing gravitational-wave background

**Target:** Test a specific EFMW stochastic background spectrum or nonstandard angular correlation.  
**Data:** [NANOGrav public timing data, spectra and sensitivity products](https://nanograv.org/science/data).  
**Control:** Astrophysical supermassive-black-hole-binary background and conventional noise/common-process models.  
**Statistic:** Appropriate common-process/correlation likelihood or released posterior comparisons.  
**Falsifier:** The frozen EFMW spectrum/correlation is excluded or fails the relevant benchmark.  
**Readiness:** **BLOCKED on an independent EFMW background prediction.**  
**Effort:** Moderate for released constraints; advanced for full timing inference.

### O16 — Pulsar glitch resonance

**Target:** Test the oscillatory transient in the [EFMW glitch proposal](https://github.com/enuminous/EFMW-Neutron-Star-Glitch-Resonance), including its restricted peak-time ratio.  
**Data:** [Jodrell Bank pulsar glitch resources](https://www.jb.man.ac.uk/research/pulsar/Resources/) and individual high-cadence timing records where available.  
**Control:** Standard glitch recovery models with permanent spin-up, exponential relaxation and relevant timing noise.  
**Statistic:** Predeclared fit quality/held-out likelihood across independent pulsars, fixing or independently predicting the timescale rather than fitting it freely to each event.  
**Falsifier:** High-cadence data show no predicted component, or conventional recoveries fit as well with less complexity; failure of a neutron-decay explanation is distinct from failure of a phenomenological sinusoid.  
**Readiness:** A mathematical waveform exists; physical microphysical derivation and independent tests do not.  
**Effort:** Low–moderate for catalog screening; higher for raw timing analysis.

### O17 — Magnetar burst recurrence and memory

**Target:** Test an EFMW-derived waiting-time, clustering or conditional-memory law on independent magnetar bursts.  
**Data:** [Fermi GBM SGR/magnetar catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/gbm/sgr/), including burst/event metadata.  
**Control:** Stationary/nonstationary Poisson processes, renewal processes, self-exciting event models and exposure/detection thresholds.  
**Statistic:** Frozen likelihood or proper scoring rule on held-out sources/time intervals.  
**Falsifier:** No predictive improvement over matched conventional time-series controls, or failure under observation-efficiency corrections.  
**Readiness:** The actual EFMW burst-law parameters/functional must be specified.  
**Effort:** Low–moderate after detector-exposure modeling.

### O18 — Gamma-ray burst propagation

**Target:** Test a derived photon time-of-flight correction as a function of energy and redshift.  
**Data:** Public Fermi LAT/GBM high-energy transient products and source-redshift records.  
**Control:** Standard energy-independent light propagation with intrinsic source spectral/timing lags and detector-response uncertainties.  
**Statistic:** A multi-event hierarchical time-lag analysis avoiding single-burst emission-time assumptions.  
**Falsifier:** Existing bounds exclude the fixed magnitude/sign; apparent lags explained by source physics do not pass.  
**Readiness:** **BLOCKED until a dispersion law is derived and dimensionally fixed.**  
**Effort:** Moderate–advanced.

### O19 — Wide-binary stellar dynamics

**Target:** Test a fully specified EFMW fifth-force or modified-geodesic acceleration law in weakly bound stellar pairs.  
**Data:** Public [Gaia DR3 wide-binary candidate catalogs](https://zenodo.org/records/17957444) and documented sample cuts.  
**Control:** Newtonian/GR dynamics with external-field, unresolved companions, projection, contamination and survey-selection effects.  
**Statistic:** Forward model of observed projected separations and relative velocities with selection corrections.  
**Falsifier:** Predicted acceleration law does not reproduce the distribution within justified errors, or no gain beyond conventional dynamics.  
**Readiness:** The hypothetical fifth-force strength and length dependence must be derived/frozen; not currently a standalone physical law.  
**Effort:** Moderate–advanced, despite freely available source data.

### O20 — Exoplanet orbital timing

**Target:** Seek a quantitatively derived EFMW perturbation to transit timing or orbital precession.  
**Data:** Public NASA Exoplanet Archive transit/ephemeris records and published transit-timing series.  
**Control:** Newtonian N-body interactions, GR corrections, stellar activity, companion planets and instrumental trends.  
**Statistic:** Predeclared residual trend or TTV amplitude in an independent system, with system-specific detection limits.  
**Falsifier:** Predicted coherent perturbation absent at sufficient measurement sensitivity.  
**Readiness:** **BLOCKED pending a specific new force or orbital equation.**  
**Effort:** Moderate; detector precision sets practical relevance.

### O21 — CMB parity, handedness or birefringence

**Target:** Test a derived parity-odd signal, cosmic birefringence or directional coupling arising from a physically defined EFMW rotation/pseudoscalar sector.  
**Data:** Public CMB polarization maps and frequency-dependent calibrations from LAMBDA/experiment releases.  
**Control:** Instrument polarization-angle uncertainties, Galactic foregrounds, ordinary parity-even cosmology and known parity-odd systematics.  
**Statistic:** Frozen \(TB\), \(EB\) or other specified parity statistic with masks, simulations and a global trials correction.  
**Falsifier:** EFMW's fixed sign/amplitude is excluded or a putative signal follows calibration/foreground artifacts.  
**Readiness:** No specific coupling or magnitude is frozen in the current isotropic C1Q model.  
**Effort:** Moderate–advanced.

### L22 — Coupled pendulum tabletop analogue

**Target:** Test classical two-mode coupling and energy exchange with two weakly coupled pendulums.  
**Apparatus:** Two pendulums, adjustable coupling, inexpensive smartphone video and tracking/position extraction; isolate damping and driving.  
**Control:** Newtonian coupled oscillators with identical measured masses, lengths, coupling and dissipation.  
**Statistic:** Frequencies, mode mixing and energy-transfer traces compared with the standard oscillator solution and the TOE-001 mathematical reduction under an explicit mapping.  
**Falsifier:** The mapped oscillator equation fails to predict measured trajectories after uncertainty/damping are handled.  
**Readiness:** Executable as a **classical model check**, but even a perfect fit is **not** evidence of fundamental information gravity.  
**Effort:** Very low–low, subject to apparatus and safety.

### L23 — Electronic RC/RLC memory and feedback analogue

**Target:** Test whether an EFMW-inspired recurrence improves prediction or monitoring of a physical circuit beyond ordinary filter theory.  
**Apparatus:** Low-voltage RC/RLC circuit, function generator or microcontroller, measurement interface, and repeatable controlled disturbances. Avoid hazardous mains voltages.  
**Control:** Standard circuit ODEs, Kalman/AR/EWMA filters, and equal-budget conventional change detectors.  
**Statistic:** Held-out residual error, warning lead, false alarms and compute cost under fixed disturbances and scoring rules.  
**Falsifier:** No improvement over conventional controls, or failure of the proposed recursion after calibration.  
**Readiness:** A low-cost applied test; only a distinctive, physically motivated prediction could support more than an engineering result.  
**Effort:** Low.

## 4. Comparison matrix and prioritization

| ID | Class | Immediate software/data access | Need a new EFMW-specific prediction? | Primary next output |
|---|---|---|---|---|
| F01 | Foundational | Yes | Yes, to identify information | Identifiability counterexample or fixed \(I_{\mu\nu}\) |
| F02 | Foundational | Yes | Yes, to link to measurement | Unit/source/sign closure |
| F03 | Foundational | Yes | Yes, beyond two-scalar EFT | Equivalence/no-new-effect judgment |
| O04 | Observation | Yes | No for C1Q compatibility; yes for novelty | Pantheon+ likelihood |
| O05 | Observation | Yes, released DR2 cosmology products | No for C1Q compatibility; yes for novelty | BAO likelihood |
| O06 | Observation | Yes after compilation | No for expansion compatibility | \(H(z)\) test |
| O07 | Observation | Yes with specialist modeling | No for conventional C1Q growth | \(f\sigma_8\) constraints |
| O08 | Observation | Yes with specialist modeling | No for conventional C1Q lensing | Weak-shear likelihood |
| O09 | Observation | Yes with boltzmann/likelihood software | No for C1Q comparison | CMB likelihood |
| O10 | Observation | Public maps | **Yes** | Directional model and null simulations |
| O11 | Observation | Public sky coordinates | **Yes** | Directional distance estimator |
| O12 | Observation | Published multimessenger bounds | Only if speed differs | Propagation exclusion/constraint |
| O13 | Observation | Public waveforms | **Yes** | Dispersion law |
| O14 | Observation | Public multibaseline strain | **Yes** | Polarization law |
| O15 | Observation | Public PTA products | **Yes** | Background model |
| O16 | Observation | Glitch catalogs | Partly (waveform exists) | Holdout timing model |
| O17 | Observation | Magnetar catalogs | **Yes** | Frozen recurrence predictor |
| O18 | Observation | Fermi catalogs | **Yes** | Photon propagation law |
| O19 | Observation | Wide-binary catalogs | **Yes** | Fifth-force acceleration function |
| O20 | Observation | Transit archives | **Yes** | Orbital perturbation |
| O21 | Observation | Public CMB polarization | **Yes** | Parity-odd coupling |
| L22 | Lab analogue | Cheap hardware | No for analogy; yes for fundamental claim | Measured coupled-oscillator traces |
| L23 | Lab analogue | Cheap hardware | No for applied monitoring; yes for fundamental claim | Circuit holdout benchmark |

An **initial scientific work order** is F01–F03 (remove obvious formal/identifiability ambiguity), then O04 and O05 (test the frozen cosmological candidate on genuinely observational data), then O16 (test the bounded pulsar transient against actual timing observations). O10, O13, O19 and O21 become strong priorities **only if** the theory first supplies specific measurable deviations.

The 23 tests are **not all equally easy**. Public access eliminates instrument purchase, not the need for validated likelihoods, careful statistics, specialist computation, adequate storage or external review.

## 5. A shared preregistration and evidence protocol

Before reporting a result on an experimental record, create an independent machine-readable record with:

1. **Frozen claim:** exact EFMW/TOE/C1Q source commit and formula, including sign/units and conditions of applicability.
2. **Observable map:** a forward equation from theory variables to an instrument measurement; no hand-waving about information, coherence, universal rotation or memory.
3. **Null and alternative:** conventional theory, matched nuisance parameters/priors, and a justified *additional* null for simpler flexible conventional explanations.
4. **Dataset:** URL, release tag, license/access conditions, exact file hashes, observation dates, selection criteria, exclusions, covariance and known calibration issues.
5. **Primary outcome:** statistical test/likelihood, target effect size, confidence/credible criterion, acceptable systematic envelope, and a negative-result declaration.
6. **Freeze discipline:** preregister choices before looking at the selected confirmatory data or use genuinely independent held-out data; publicly released datasets are not inherently blind if previously inspected.
7. **Compute reproducibility:** code, package versions, random seeds, logs, data transformations and generated results. The raw instrument data may be linked rather than redistributed where licensing or size prevents bundling.
8. **Claim audit:** the Zoo returns evidence-linked PASS, FAIL, UNRESOLVED or justified N/A at its actual scope; do not turn unexecuted checks into PASS.
9. **Multiplicity:** distinguish exploratory scans from the designated primary comparison. Account for 23 trials, searched sky axes, energy bins, alternate filters and post-selection.
10. **Replication:** require independent code or methodological reproduction for important results; when original data are reused, describe it as reanalysis rather than independent experimental replication.

A suggested machine-readable result structure is:

\`\`\`json
{
  "id": "O04",
  "status": "UNRESOLVED",
  "frozen_claim_commit": null,
  "theory_equation": null,
  "observable": "Pantheon+ supernova distance moduli",
  "dataset_release": null,
  "baseline": ["LambdaCDM", "matched quadratic quintessence"],
  "primary_statistic": null,
  "threshold_frozen_before_data": false,
  "observed_result": null,
  "distinctive_efmw_signature": null,
  "limitations": ["No confirmatory likelihood evaluated"],
  "evidence": []
}
\`\`\`

All missing fields in this *proposed intake* are intentionally null. Nothing in this protocol supplies experimental results without computation.

## 6. How the Zoo should adjudicate physical claims

For physical claim \(c\), the scientific verdict must retain at least four separate labels: *mathematical well-definedness*, *numerical implementation*, *consistency with empirical data*, and *distinctiveness against conventional models*. These layers cannot be averaged into one flattering approval count.

Examples:

- A correct Lean proof of a conservation identity is a mathematical PASS under its assumptions; it does not show that the source tensor exists physically.
- A cosmological \(H(z)\) curve close to observation may be a consistency PASS, but if it duplicates quintessence it does not constitute an EFMW-specific discovery.
- A preferred-axis search with a result selected after examining thousands of sky directions is exploratory; the local significance is not a prespecified global discovery threshold.
- A failed held-out result is an informative **FAIL for the tested candidate**. It should be retained with code and raw outputs; nothing about a later modified model retroactively changes it.

In the [alternative Zoo limiter](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/main/ALTERNATIVE_REPORT.md), missing animal results remain UNRESOLVED, N/A remains in the denominator, and qualified dependencies prevent downstream establishment. That limiter is an *evidence-coverage mechanism*, not direct physical measurement.

## 7. Minimum viable campaign: two observational comparisons plus one identity test

The recommended near-term package contains:

**Phase A — source lock:** Verify F01/F02/F03 against canonical EFMW, TOE-001 and the Lagrangian audit. Publish a claim provenance table and, if physical identifiability fails, stop calling the chosen candidate a distinct field until an independent definition exists.

**Phase B — observational pipeline:** Reproduce Pantheon+'s baseline likelihood on the released reference model *before* trying C1Q; independently check C1Q's published background \(H(z)\). Freeze the C1Q point/allowed parameter set, nuisance parameters and loss function. Publish the C1Q versus \(\Lambda\)CDM and conventional quintessence result as O04, positive or negative.

**Phase C — second data modality:** Repeat against DESI DR2 BAO release products (O05), preserving cross-dataset overlap and covariance assumptions. Do not retune the originally frozen model using O04 and then call O05 an independent preregistered test unless this is explicitly allowed by the protocol.

**Phase D — candidate-specific physics:** Test O16 using the existing glitch waveform. Its approximately 0.401907 peak-time ratio is a mathematical consequence of the chosen damped sinusoid, not an independently derived neutron-decay frequency. For physical novelty, a microphysical prediction of the timescale or normalized amplitude is needed, along with a baseline and high-cadence event data.

**Decision:** Publish matched likelihoods, test outcomes, uncertainty, null controls, and clear limits. A physical claim is not elevated beyond *candidate* unless a distinctive effect survives a truly discriminating independent test.

## 8. Scope, hazards and limitations

The campaign is deliberately open to failure. Phenomenological fits with many free parameters are not evidence of new laws. Observational data can test some proposed quantities but not all metaphysical interpretations. In particular, consciousness, LOGOS, qualitative recursion, and generalized informational language are **not testable physical hypotheses** until the relevant variables and observation maps exist.

Environmental and astrophysical confounding matters; supernova calibration, large-scale-structure bias, CMB foregrounds, gravitational-wave waveform uncertainties, pulsar timing noise, magnetar detection efficiency, stellar multiplicity and circuit apparatus transfer functions can readily mimic or hide an apparent signal. Preregistered analysis and independent review are necessary.

The tabletop cases use safe low-energy systems; they can test equations and predictive methods but do not duplicate the gravitational or quantum conditions of the cosmos.

No human-subjects, clinical, hazardous-material or high-voltage experimentation is required by the proposed first campaign.

## 9. Conclusion

**Monolithic's Twenty-Three is not a count of discovered EFMW laws. It is a docket of ways the proposed laws might fail.** That is the relevant scientific standard.

The immediate best use of effort is to separate source-level mathematical consistency from physical claims and run a reproducible observational compatibility check against Pantheon+ and DESI, with identical conventional controls. The next genuinely new-physics milestone is to identify *one* noncircular observable whose predicted value differs from established theory, freeze it, and allow an independent dataset to decide its fate.

The project is successful as a falsification program even if all 23 outcomes are negative or unresolved—provided that the record prevents mathematical elegance from being mistaken for physical truth.

---

## Sources and reproducibility references

### EFMW primary and companion documents

1. Wright/Monolithic, [EFMW canonical front door and review freeze](https://github.com/enuminous/EFMW); [open obligations](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md).
2. Wright/Monolithic, [*EFMW at the Boundary of Established Physics*](https://github.com/enuminous/papers/blob/main/EFMW_Boundary_of_Established_Physics.md).
3. [Canonical 102 equations](https://github.com/enuminous/Monolithic_102_EFMW) and [the ME-007 frozen entry](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/01f51acb0b0e564105dcf7f14cc55998d41b91ce/Monolithic102/ME007.lean).
4. [TOE-001 ME-007 conditional conserved-source realization](https://github.com/enuminous/TOE-001/blob/main/ME007_INTEGRATION.md).
5. [Frozen C1Q cosmology model and reproducibility materials](https://github.com/enuminous/Cosmology).
6. [Pulsar glitch resonance candidate and mathematical prediction](https://github.com/enuminous/EFMW-Neutron-Star-Glitch-Resonance).
7. [EFMW-Lagrangian equation comparison](https://github.com/enuminous/EFMW-Lagrangian), [QST-002 quantum geometry caveats](https://github.com/enuminous/QST/blob/main/QST-002.md), and [Zoo's alternative evidence-limiter rules](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/main/ALTERNATIVE_REPORT.md).

### Observational and laboratory source portals

8. [Pantheon+SH0ES public data release](https://github.com/PantheonPlusSH0ES/DataRelease), including distances and covariance.
9. [DESI DR2 cosmology publications and released products](https://data.desi.lbl.gov/doc/papers/dr2/); releases must be distinguished from unreleased full underlying spectroscopy.
10. [NASA LAMBDA archive](https://lambda.gsfc.nasa.gov/product/) for public CMB maps and likelihood resources.
11. [Gravitational Wave Open Science Center](https://gwosc.org/tutorials/) and [GW170817 public event data](https://gwosc.org/events/GW170817/).
12. [NANOGrav public data and products](https://nanograv.org/science/data).
13. [Jodrell Bank pulsar resources and glitch catalogue](https://www.jb.man.ac.uk/research/pulsar/Resources/).
14. [Fermi GBM SGR/magnetar burst catalogue](https://fermi.gsfc.nasa.gov/ssc/data/access/gbm/sgr/).
15. [Gaia DR3 wide-binary catalogue](https://zenodo.org/records/17957444).
16. [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/).

**Provenance note:** This is a research-program manuscript derived from Wright's EFMW portfolio and the proposed Monolithic-23 shortlist, written with AI assistance. External observational archives and foundational scientific methods are credited to their respective collaborations. No 23-experiment dataset was downloaded or evaluated in preparing this paper; no positive physical detection is claimed.
