# EFMW L1–L3: Experimental Test Designs v0.1
Prepared for Matthew Chenoweth Wright / Monolithic LLC
Status: proposed protocols; no experiment, dataset analysis, or independent Lean compilation has been performed.

## Scope and scientific contract

The supplied Aristotle 156-theorem audit identifies three physical candidate families: L1 scalar propagation, L2 modified gravitational coupling, and L3 a Friedmann expansion correction. It does not contain their complete field equations, parameter domains, actions, matter couplings, or detector responses. These protocols specify experiments and decisions as far as that source permits. New measurement formulas below are experimental definitions or explicitly stated conditional deductions, not missing EFMW equations reconstructed from theorem names.

For each candidate, freeze a signed model specification: exact equations and units; allowed parameter domain; boundary/initial conditions; source and detector coupling; baseline recovery; predicted observable; nuisance parameters; minimum effect of interest; and a source commit. L1 and L2 must use the same scalar sector and couplings if they describe the same physical field. Do not fit them independently and later claim joint confirmation.

Use blind signal injections for pipeline validation, distinguish simulations from observations, freeze analysis before unblinding, and retain all exclusions and negative results. Existing public observations constitute retrospective tests; reserve independent data or new observations for confirmation.

A null result excludes a stated parameter region at stated coverage. If arbitrarily small nonzero couplings remain allowed, no finite-precision null result excludes the entire family. A detected departure from a baseline is evidence for EFMW only to the extent that EFMW predicts features competing models do not.

## EXP-L1: Differential scalar-wave phase propagation

### Question and prerequisite

Does an identified, detectable scalar mode obey the EFMW dispersion relation over a controlled range of frequencies and propagation distances?

The audit supports a plane-wave relation and phase-speed consequences involving alpha but does not give the exact relation. Before apparatus selection, supply omega(k; alpha, background), the admissible alpha domain, and physical mechanisms for excitation and readout. Do not replace the scalar field with a laser beam without deriving a coupling to light. An engineered analogue tests the implemented dynamics, not the existence of a fundamental scalar field.

### Apparatus and acquisition

Use a coherent scalar source, a phase-referenced receiver, and a calibrated variable path or independently calibrated receiver positions. The physical technology must follow the source/detector coupling. If no demonstrated source exists, first test excitation and detection feasibility; absent a detected mode, phase speed cannot be measured.

Select at least three distinct path lengths and five frequencies within the derived model's validity band. Choose actual values after computing predicted phases and instrument resolution. Record complex transfer functions, source amplitude, environmental channels, path calibration, timing reference, and receiver response.

Randomize path/frequency order; repeat configurations in independently calibrated blocks; interchange readout channels; perform source-off and sham-modulation runs. Test direction/orientation only if the equation predicts directional dependence. Use reciprocal paths or a common timing reference to avoid treating clock synchronization conventions as a measured one-way speed.

### Observable

For phase convention Phi(omega,L) = k(omega)L + b(omega), estimate k from the slope of unwrapped phase versus length. The intercept b absorbs path-independent instrument phase. Path-dependent detector and cable effects require separate calibration.

v_phase(omega) = omega / k(omega)
delta_v(omega) = v_phase(omega) / c_ref - 1.

The reference speed must correspond to the same identified physical mode in the baseline, with a defined calibration. A pulse-delay cross-check measures group delay; compare it with d omega/d k derived from the model rather than equating phase and group speeds by assumption.

### Comparison and controls

Fit the complete complex response jointly under:
M0: baseline scalar propagation plus calibrated apparatus effects;
M1: the frozen EFMW dispersion relation;
M2: conventional dispersive medium or instrument explanations;
M3: a generic modified-dispersion model with comparable flexibility.

A genuine propagation effect must reproduce the predicted path-length slope, frequency dependence, and any predicted orientation dependence. A constant electronics delay or source-correlated electromagnetic pickup must be modeled and challenged by channel swaps and shielding diagnostics.

### Sensitivity and decisions

For a specified alpha*, predict the observable phase difference at every configuration. Compute sensitivity from the joint covariance, including shared calibration errors; do not count correlated samples as independent replications.

Illustration only: if a hypothetical model predicts delta_v = 10^-6, a nominal five-standard-deviation separation requires combined speed-ratio uncertainty at most 2 x 10^-7. This is a metrology target, not an EFMW prediction or a statement of achievable hardware performance.

Publish a simulation-calibrated 95% confidence region for alpha and other identified physical parameters. Before unblinding, require at least 90% power to exclude the selected benchmark at that coverage if the baseline is true. A discovery claim additionally requires a predeclared global significance threshold (suggested five sigma), survival of controls, and independent replication. A failure of the predicted frequency/path pattern can reject the benchmark even if an unexplained phase shift exists.

### Archival alternative

Multi-messenger propagation observations may constrain the model only after deriving its effect on the observed gravitational or electromagnetic modes and accounting for intrinsic emission delays. GW170817 is not automatically a constraint on an otherwise unobserved scalar field.
Reference: https://ligo.org/detections/gw170817/

## EXP-L2: Modulated-source gravity response

### Question and prerequisite

Does the proposed gravitational coupling predict a measurable force pattern that cannot be absorbed into the measured gravitational constant or ordinary apparatus backgrounds?

The audit's I = T_phi + Ric and substitution equivalence are insufficient to specify a force. First derive a consistent weak-field solution for a real source, including matter coupling, boundary conditions, background scalar value, and any screening. Check units, conservation/Bianchi compatibility, degrees of freedom, and stability in the experimental regime. An action is one route; a complete consistent set of field equations can also supply the needed specification.

Calculate g_EFMW(r, geometry, material, environment; theta) and the baseline g_GR for the actual source. Determine whether the result predicts distance dependence, composition dependence, orientation dependence, or only a constant renormalization of G. If it is exactly a rescaling of G throughout the accessible regime, this apparatus cannot identify the extension independently of G.

### Apparatus and acquisition

Use a precision torsion balance or differential accelerometer selected for the derived force range. Move a characterized source mass between at least three separations while monitoring the test body's force or acceleration. Use periodic source motion and synchronous detection, with randomized block order and independently calibrated source positions.

Measure the source geometry and density distribution rather than approximating every configuration by a point mass. Record gravity gradients, tilt, seismic motion, temperature, magnetic fields, electrostatic potentials, and actuator coupling. Include matched mechanical sham runs designed to reproduce actuator motion while suppressing the predicted gravitational modulation.

If the model predicts composition dependence, compare two appropriately chosen test-body compositions in the same external field. If the coupling is universal, prioritize distance or environment dependence instead.

### Observables

For each configuration j:
R_j = g_observed,j - g_GR,j.

Fit R_j = Delta g_EFMW,j(theta) + instrument/background terms jointly with Newtonian source calibration and G where necessary.

For a composition-dependent prediction, use:
eta = 2(g_A - g_B)/(g_A + g_B),
with a frozen sign convention.

A generic Yukawa potential,
V(r) = -GMm/r [1 + beta exp(-r/lambda)],
may serve as a comparison model only. Do not present it as the EFMW force law unless derived from the actual equations. If derived, integrate the resulting interaction over the finite apparatus geometry.

### Controls and decisions

Predeclare the full predicted pattern across separation, composition (if applicable), source mass and orientation (if applicable). A source-synchronous signal alone is insufficient because actuator-driven disturbances can share its frequency.

Use injections into calibration data to determine the number of independent measurement blocks and systematic floor required for 90% power against a frozen benchmark. Report joint parameter exclusions at 95% coverage, calibrated for boundaries and nuisance parameters. Follow any discovery-level effect with a second apparatus or independent laboratory and the same physical parameter prediction.

Reject a benchmark if its predicted force is excluded, its distance/material pattern fails, or achieving a fit requires incompatible coupling values across configurations. Do not claim rejection of untested screening regimes.

### Archival gate before new hardware

Map the derived prediction onto applicable existing limits. MICROSCOPE tested differential free fall of titanium and platinum alloys and found no WEP violation at its reported sensitivity. Those results constrain this EFMW candidate only if its matter coupling predicts the corresponding composition-dependent acceleration.
Primary result: https://arxiv.org/abs/2209.15487

## OBS-L3: Expansion–geometry consistency, followed by rotation signatures

### Question and exact identifiable quantity

Can an added expansion term be distinguished from spatial curvature, and does it have the proposed rotational origin?

In the audit's convention, constant Omega_U gives Q = Omega_U^2 >= 0 and the background form:
H^2(a) = F(a; other parameters) - k/a^2 + Q/a^2.

Only k_eff = k - Q appears in this expression. H(a) data alone cannot separately determine k and Q without independent information or assumptions. Setting k = 0 to obtain a tight Q estimate must be reported as a flatness-conditional constraint, not detection of rotation.

F and k must be defined with consistent units; the following formulas use c = 1 and an FLRW distance law. Restore c in observational code. Any rescaling of a must also rescale associated parameters consistently.

### First test: exact degeneracy demonstration

Before fitting data, evaluate the forward model at parameter pairs (k,Q) and (k+Delta,Q+Delta), keeping Q nonnegative. H(a) must be identical for constant Q. Inspect the likelihood ridge and parameter Jacobian. If an expansion-only analysis claims independent precise estimates for both, identify the prior or implementation choice that supplied the information.

This is a model-identifiability check, not an empirical detection.

### Conditional route A: independently accessible geometric curvature

If the complete EFMW metric retains the standard FLRW distance law with geometric curvature k distinct from k_eff, combine expansion measurements with transverse distances. For transverse comoving distance D(z), that geometry implies:
[H(z) D'(z)]^2 = 1 - k D(z)^2.
Thus k_geometry = [1 - (H D')^2] / D^2 where the expression is well-defined.

This is a conditional geometric identity, not an additional EFMW law. Prefer joint forward modeling of distances over noisy numerical differentiation of observations.

Combine radial and transverse BAO information, supernova distances, and any independently justified calibration. Treat sound-horizon calibration, absolute supernova magnitude, matter content, H0, and shared covariances as nuisance quantities. Do not claim a modified model has been tested using a CMB-derived prior that presupposes the very gravitational model being changed.

If both quantities are identified under the completed theory:
Q = k_geometry - k_eff.

Fit standard curved cosmology, flat cosmology plus Q, curved cosmology plus Q, and relevant alternative expansion histories. Profile/marginalize other parameters and test sensitivity to calibration assumptions. Distance data may break the background degeneracy only if the theory really supplies this separate geometric role for k.

Relevant method: Clarkson, Bassett and Lu, https://arxiv.org/abs/0712.3457
BAO source and data documentation: https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/

### Conditional route B: a genuine rotation prediction

If the proposal claims physical cosmic rotation, derive a consistent rotating spacetime solution and its temperature, polarization, distance or other observable signatures. Freeze the relationship between Omega_U and those signatures, their evolution, and any orientation parameters. Do not add a free sky template unrelated to the background parameter.

Use an established CMB likelihood with the appropriate foreground, beam, mask, noise and calibration treatment. Propagate the same physical parameters through temperature and polarization predictions. Calibrate global significance with end-to-end simulations including any sky-axis search. A template tuned to temperature must correctly predict withheld polarization or another declared independent observable.

Planck's Bianchi analyses provide a relevant methodological precedent and model-specific constraints. Their numerical vorticity limit cannot be transferred to EFMW without deriving the parameter/model mapping.
Primary result: https://arxiv.org/abs/1502.01593

### Decisions

Exclude the frozen constant-Q benchmark if the joint observable predictions fail at the preregistered confidence level. A fit requiring Q < 0 would contradict Q = Omega_U^2 for real Omega_U within that completed model, after nuisance and alternative-model checks.

A positive expansion contribution alone does not establish rotation. Require a linked independent rotation signature. If the completed model offers neither independently accessible geometry nor any other distinction from curvature, classify Q as observationally unidentified in this program and stop short of a rotation claim.

Existing public sky data offer retrospective assessment. Confirmation requires a predeclared independent observable/dataset whose errors and selection have been accounted for, rather than reusing the discovery residual.

## Execution order and deliverables

1. Recover exact ScalarField, Cosmology and PhysicalTest module definitions and linked source equations. Freeze the L1 dispersion and couplings; L2 consistent weak-field observable; L3 metric, parameter evolution and distances.
2. Complete the L3 degeneracy check and L2 G-rescaling check. These can invalidate an intended experiment before apparatus expenditure.
3. Translate each identifiable prediction to existing observations where justified. Freeze a surviving benchmark only with transparent acknowledgment of this retrospective selection.
4. Run blinded sensitivity/injection studies and publish the resulting power, attainable systematic floor and acquisition plan. Simulated survival establishes pipeline capability only.
5. Acquire or designate independent observations, unblind once, release likelihoods/calibrations, and seek replication.

Required outputs per candidate: equation-and-units specification; forward model; baseline and adversarial alternatives; acquisition/data manifest; calibration/covariance model; preregistered benchmark, power and decision rules; raw-to-result code; exclusion plot or joint predictive comparison; and a report distinguishing detection, exclusion and non-identifiability.

Readiness: L1 has a conditional phase-propagation protocol but lacks a specified physical source/readout. L2 has a conditional force protocol but lacks a derived force law. L3 has an immediately defined background-identifiability analysis; empirical separation requires a complete geometric or rotation observable model. These are designs, not completed experimental validations.

Primary EFMW source: ARISTOTLE_156_TOTAL_NOVELTY_AUDIT(1).md supplied by the user; entries 100–106, 109, 127–128 (L1), 130–132 (L2), 46–48 and 107–108 (L3).

