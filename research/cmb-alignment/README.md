# CMB alignment and the 100,000-object claim

**Reproducibility companion, 18 October 2026.** This directory supports [R-001](../../EFMW-Zoo-R001-Primordial-Recursion-Boundary.md) and [Great Recursion](../../great-recursion-primordial-rotation.md). It is an evidence audit and numerical baseline, not a new cosmology paper or a reconstruction of the historical simulation. The separate bouncing-geometry tests are outside its scope.

## Findings

A **January 23, 2025 narrative matching the 100,000-object claim was recovered** in the author's archived article, *Foundations of a Dynamic Cosmos*. Its section 3.1.1 describes Gaussian spins and assigned directional momenta. However, no corresponding executable package, complete parameters, original seed, numerical output array, or CMB sky-map product was recovered. The narrative establishes that the claim was documented, not that its computation or physical interpretation was verified. Some equations and results are external images whose contents could not be inspected; their contents are not assumed absent. See the bounded [provenance ledger](PROVENANCE.md).

Separate October 18 records preserve a 100,000-object toy merger calculation. Its Universe 003 source and saved ensemble were recovered and rerun; they are **not the January experiment**. They model vector bookkeeping, with no positions, gravitational field evolution, or transfer from primordial objects to a microwave sky.

The independent benchmark here executed:

| Calculation | Fixed sample size | Purpose |
|---|---:|---|
| Independent isotropic axis pairs | 1,000,000 | Primary directional-null distribution |
| Gaussian quadrupole/octopole coefficient pairs | 20,000 | Check the harmonic estimator against the axis null |
| Nine isotropic axes, multipoles 2–10 | 100,000 realizations | Distribution of the maximum over 36 pairs |
| Isotropic unit-spin sums | 64 populations of 100,000 | Finite-population spin control; no EFMW dynamics |
| Recovered Universe 003 | 128 null + 32 biased populations | Reproduce the separate October toy calculation |
| Public WMAP nine-year ILC pixels | One sky, two fixed treatments | Independent measurement of the relevant CMB statistic |

The first row is one million axis pairs, **not one million simulated instrument sky maps**.

## Observational result

The new pixel measurement uses the NASA WMAP DR5 nine-year ILC v5 temperature map. The primary treatment within this secondary observation check subtracts the specified leading blackbody Doppler quadrupole (DQ). All results, including the uncorrected diagnostic, are retained.

| WMAP9 ILC treatment | Axis separation | A23 | Exact ideal single-pair p | Monte Carlo p for any of 36 pairs |
|---|---:|---:|---:|---:|
| No DQ subtraction, diagnostic only | 3.16463° | 0.99847503 | 0.152497% | 5.36095% |
| Specified DQ subtraction | **5.85464°** | **0.99478389** | **0.521611%** | **17.17283%** |

For the corrected result, the quadrupole axis is Galactic (l,b) = (236.03309°, 57.15036°), and the octopole axis is (238.14226°, 62.91023°), choosing the northern representatives of headless axes. The full 2–10 scan actually finds its largest alignment at (2,3), so its observed maximum equals A23.

The corrected single-pair simulation has 5,347 exceedances in 1,000,000 trials, giving the plus-one estimate 0.534799% and a 95% Wilson interval of 0.520595–0.549185%. The 36-pair calculation has 17,172 exceedances in 100,000 trials, giving 17.17283%, with interval 16.93951–17.40701%. These intervals describe **Monte Carlo sampling error**, not measurement uncertainty. The analytical single-pair probability is preferable where its assumptions hold.

The 36-pair family was explicitly frozen. It answers the question “how often does any pair among multipoles 2–10 align at least this strongly?” It is **not a reconstruction of all choices in the historical anomaly search**, and is not the universally correct correction for every quadrupole–octopole question. If (2,3) alone was a genuinely prior physical prediction, its single-pair test is the relevant conditional test. Choosing (2,3), a statistic, a map, a mask, or a reference direction after inspecting data adds selection that must be represented in the null.

At the declared 5% level, the corrected result is unusual in the ideal preselected single-pair test but does not reject the declared 36-pair null. Neither conclusion is a posterior probability of isotropy or of EFMW. No end-to-end instrumental or foreground significance is claimed.

This calculation supplies no quantitative upper limit on EFMW rotation or primordial-black-hole abundance, and excludes no general class of rotating universes. Such limits require a specified physical prediction. What it rules out is the inference that a finite random spin sum or this unmodeled alignment alone demonstrates universal rotation.

The implementation also scores all 13 compatible published map/correction variants transcribed in [observations.json](observations.json), with rounding intervals. These are correlated views of the same sky, not 13 independent confirmations. The raw WMAP numbers agree with the corresponding rounded entries in Copi et al. (2015), Tables 4–5; the calculation was not tuned to force agreement.

## Frozen protocol and estimator

[protocol.json](protocol.json) records the distribution, statistic, coordinates, seeds, sample sizes, and comparison family. The session freeze at 17:19:44 UTC preceded the new simulations and numerical extraction of published axes. Git commit [f9c7b56](https://github.com/enuminous/papers/commit/f9c7b56c8c1e52027f4202357e922a9d7f5c373e) preserved the protocol before simulation execution, but after the published table had been looked up. This is a prospectively fixed computational protocol, **not an external preregistration and not a blind discovery test of a previously unknown anomaly**.

The secondary [raw-map protocol](raw-map-protocol.json) was fixed after published summary values and the baseline were known, but before downloading and processing the FITS pixels. It was committed in [5261d0a](https://github.com/enuminous/papers/commit/5261d0a0945b147e181b4d42518501040e1c9506). The input checksum was recorded on download and then enforced; it was not known before retrieval.

Coordinates are right-handed Galactic Cartesian, with x toward (l,b)=(0°,0°), y toward (90°,0°), and z toward the north Galactic pole. Angles use degrees in records and radians in trigonometry. Axes are headless: n and −n represent the same axis.

For complex spherical harmonics with the standard Condon–Shortley convention, define

$$Q_{ij}^{(\ell)}=\operatorname{Re}[(L_i a_\ell)^\dagger(L_j a_\ell)],\qquad
\hat n_\ell=\operatorname{eigvec}_{\max}Q^{(\ell)},\qquad
A_{23}=|\hat n_2\cdot\hat n_3|.$$

This is maximum angular-momentum dispersion in the harmonic representation. The name does **not** mean that mechanical angular momentum or fluid vorticity has been measured. Multipole-vector area-normal statistics are different estimators and are not silently substituted.

Under independent isotropic Gaussian multipoles, the unique axes are independent uniform headless directions, hence

$$A_{23}\sim U(0,1),\qquad p_{\rm ideal}=1-A_{23,\rm obs}.$$

This null is stronger than isotropy alone: an isotropic non-Gaussian model can contain inter-multipole correlations. Directional samples use uniform z and azimuth, not uniform latitude. Gaussian coefficient draws use real a_l0 with variance one, positive-m real and imaginary parts with variance one-half, and the real-field conjugacy relation. Setting C_l=1 is harmless for this scale-invariant axis statistic under the specified independent Gaussian null.

The dependency-free JavaScript generator is xoshiro128** with explicitly implemented SplitMix32 initialization, open-interval uniforms, and ordered Box–Muller pairs. Seeds are 2026101801 (pairs), 2026101802 (harmonics), 2026101803 (36-pair family), and 2026101805 (spin sums). Seed 2026101804 is reserved in the protocol but unused because the five-degree positive control is deterministic. Draw order and stream fingerprints are saved.

The benchmark checks antipodal symmetry, common-rotation invariance, known harmonic axes, tensor trace and eigenpair identities, and Gaussian-axis calibration. The primary sample mean is 0.500118 and its Kolmogorov distance from uniform is 0.0007222; the harmonic sample mean is 0.500843. Reproduction tolerances and broad six-standard-error diagnostic gates were added after the first execution, as engineering checks rather than preregistered scientific rejection criteria. Some nested pointwise 95% Monte Carlo intervals miss the exact tail, as can happen under repeated comparisons; the seed was retained, and analytical probabilities were not replaced by a favorable simulated estimate.

## What the recovered October experiment establishes

Universe 003 starts with lognormal toy masses, normalized Gaussian directions, and assigned dimensionless spin factors. It randomly pairs objects and removes assigned scalar fractions of mass and vector spin until four remnants remain. Its orientation-independent operations preserve rotational symmetry in the ensemble. A nonzero random resultant in one realization is expected; it does not select a shared preferred direction across realizations.

The saved and reproduced first run has |cos(theta_z)|=0.465682 and ideal fixed-axis p=0.534318. Among the 128 saved null runs, the most aligned has |cos|=0.973147, but the probability of at least this extreme a result in 128 independent isotropic runs is about 0.969322. The explicitly biased controls add 0.2 to a Gaussian z component before normalization; they demonstrate sensitivity to an inserted direction. They do not derive that direction from EFMW.

Universe 002 additionally assigns a rebound inheritance factor of 0.65. Neither record supplies physical units, a spacetime solution, a sky-transfer calculation, or a CMB likelihood. Its bookkeeping conservation checks are useful within the algorithm, not proof of relativistic merger or bounce dynamics. [recovered-reproduction.json](recovered-reproduction.json) records the rerun scope; the original source snapshots are unchanged.

## Systematics and selection boundaries

| Issue | Treatment here | Remaining requirement |
|---|---|---|
| Kinematic quadrupole | Report fixed uncorrected and leading blackbody-corrected results | Frequency-dependent ILC response, calibration and motion uncertainties |
| Foregrounds and component separation | Use released bias-corrected ILC; retain published map variants | Joint foreground uncertainty and alternative cleaned-map pipelines |
| Masks and inpainting | Full-sky released map; no new mask or inpainting | Apply every chosen mask/reconstruction identically to data and null skies |
| Beam, pixelization, noise and scan | Preserve map metadata; compare harmonic iterations 0, 3, 5 | End-to-end instrument/noise/calibration simulations |
| Numerical estimation | Independent NumPy and JavaScript axis implementations agree; A23 iteration shift below 1.4e-7 | These checks do not bound foreground or instrumental error |
| Axis or statistic selected after inspection | Headless two-axis statistic fixed; explicit 36-pair scan | Reproduce the complete selection algorithm, including map/statistic choices |
| Mission or frequency replication | Treat common-sky products as dependent | Independent nuisance responses and genuinely held-out predicted observables |

Optimizing a free reference direction to match a single observed vector gives perfect alignment on **every null realization**. Its correctly calibrated optimized test has p=1. Several axes require a specified joint optimization statistic, repeated identically in each control. A posteriori references such as the dipole, ecliptic or Galactic plane cannot be added without their search cost.

Planck's broader isotropy analyses and temperature/polarization checks provide observational context, not a license to label this temperature alignment a rotation detection. Model-dependent Bianchi shear constraints likewise cannot be converted into a universal vorticity bound for an unspecified EFMW cosmology.

## Scientific disposition and next decisive evidence

| Claim | Disposition |
|---|---|
| A historical 100,000-object claim exists | **Documented**, January 2025 archive |
| The historical simulation was executed as described | **Unresolved**; original execution evidence missing |
| The separate October toy ensemble is reproducible | **Demonstrated computationally**, within its bookkeeping assumptions |
| WMAP quadrupole/octopole axes are close | **Reproduced** for the specified map and processing |
| This rejects every isotropic cosmology | **Unsupported**; null and search family matter |
| EFMW caused the observed alignment | **Not demonstrated**; no quantitative forward prediction |
| A preferred observational axis proves global cosmic rotation | **Invalid inference without a physical model and independent observables** |

A reproducible historical claim needs an immutable source revision, environment, seeds or full RNG states, all initial distributions and physical units, evolution equations, resolution/convergence records, raw outputs, and the exact transformation to temperature/polarization maps. The original selection history and failed runs matter. A new reconstruction must be labeled as such and compared with, not substituted for, any recovered historical output.

A physical EFMW test additionally needs a covariant dynamical model and a specified fluid congruence with a measurable vorticity tensor, valid source/constraint evolution, and predictions for amplitudes, relative directions, scale dependence, handedness where applicable, and polarization. Primordial spin sums alone do not provide these. Randomly oriented realizations can predict *relative* alignments without preferring an absolute Galactic direction; any claimed absolute direction needs an independently specified reference or symmetry-breaking mechanism.

Before a new measurement, freeze the EFMW-to-sky transfer model and its parameters, the baseline cosmology, nuisance priors, map treatments, comparison family, and a likelihood or score. Compare full simulated skies with identical processing, include isotropic and injected-anisotropy controls, ablate the claimed rotational source, and test held-out predictions. An observed anisotropic pattern must distinguish rotation from non-rotating anisotropic alternatives. Expansion history retains the curvature degeneracy discussed in Great Recursion.

The Zoo principle Freeze → Predict → Score → Ablate → Replicate guides these obligations. Only the computational null, prescribed controls, and observation extraction have been exercised here. The canonical Tortoise temporal prediction/Brier experiment was **not** run, and no animal-pass or full-Zoo certification is claimed. EFMW prediction and physical ablation remain open.

The null distribution, harmonic estimator and CMB anomaly are established statistical/observational ideas. The contribution here is the traceable provenance audit, frozen implementation, independent reproduction, and narrower evidentiary conclusion—not a new law or evidence for universal rotation.

## Reproduce

Use Node 20 or newer for the dependency-free benchmark. The recorded local rerun used Node 24.19.0. From this directory:

    node run.cjs --check
    node score_raw.cjs --check

For fresh pixel extraction and the recovered October ensemble, use Python 3.12 and the pinned packages:

    python3.12 -m venv .venv
    .venv/bin/pip install -r requirements-map.txt
    OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 .venv/bin/python measure_wmap.py --data data/wmap_ilc_9yr_v5.fits --out /tmp/wmap-reproduction.json
    .venv/bin/python verify_map.py /tmp/wmap-reproduction.json
    .venv/bin/python verify_recovered.py
    sha256sum --check SHA256SUMS

The map script downloads the 25,174,080-byte public FITS file if absent and requires SHA-256 **4501090f824f9140e916339f9e8e490333f6ffe4257a6ee6a02526c8640099a9**. The FITS file is not duplicated in Git. [raw-map-results.json](raw-map-results.json) preserves all low-ell coefficients, axes, metadata and extraction variants; [raw-map-significance.json](raw-map-significance.json) preserves exact and Monte Carlo scores. The [workflow](../../.github/workflows/cmb-alignment.yml) repeats the numerical checks; its run status is separate from the scientific scope.

## Sources

1. Wright and Millie Complex AI, [archived January 23, 2025 article](https://github.com/enuminous/medium/blob/61f5f441628563a313ed64a295f69c7baeb71c72/2025-01-23_Foundations-of-a-Dynamic-Cosmos--Resolving-Anomalies-with-Rotational-Potentials--Linear-Potentials--79279ea03332.html).
2. Copi, Huterer, Schwarz and Starkman, [Large-scale alignments from WMAP and Planck](https://arxiv.org/abs/1311.4562), MNRAS 449 (2015), 3458–3470; arXiv v3, section 3.3 and Tables 4–5.
3. NASA LAMBDA, [WMAP nine-year ILC products](https://lambda.gsfc.nasa.gov/product/wmap/dr5/ilc_map_get.html) and [map description](https://lambda.gsfc.nasa.gov/product/wmap/dr5/ilc_map_info.html).
4. Planck Collaboration, [Planck 2018 results. VII. Isotropy and Statistics of the CMB](https://arxiv.org/abs/1906.02552).
5. Saadeh et al., [How Isotropic is the Universe?](https://arxiv.org/abs/1605.07178), PRL 117 (2016), 131302.
6. HEALPix/healpy documentation: [read_map](https://healpy.readthedocs.io/en/latest/generated/healpy.fitsfunc.read_map.html), [map2alm](https://healpy.readthedocs.io/en/latest/generated/healpy.sphtfunc.map2alm.html).

**Disclosure:** New null simulations, raw WMAP extraction and the separate Universe 003 rerun were executed. The historical January simulation was not recovered or recreated. No measurement here establishes a dynamical EFMW cosmology or global cosmic rotation.
