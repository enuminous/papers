# Prediction lock EFMW-CMB-PRED-001 — v1.0.0

**Locked 18 October 2026; machine timestamp in [lock.json](lock.json).** This is an internal, versioned prediction record attached to the existing [CMB assessment](../../README.md), not an external registration or a new paper.

## The locked prediction

**EFMW-COSMO-C1Q v1.0.0 predicts no preferred cosmological axis in its isotropic Gaussian ensemble and zero vorticity in its FLRW background and retained linear scalar sector.**

For its ideal full-sky, **unlensed linear Gaussian temperature** multipoles, the headless maximum-dispersion quadrupole–octopole axes obey

$$A_{23}=|\hat n_2\cdot\hat n_3|\sim U(0,1),\quad
\mathbb E[A_{23}]=\tfrac12,\quad
\operatorname{Var}(A_{23})=\tfrac1{12}.$$

Consequently, the probability of a headless separation no greater than θ is 1−cos θ:

| Separation threshold | Locked probability |
|---|---:|
| 1° | 0.0152305% |
| 5° | 0.3805302% |
| 10° | 1.5192247% |

These are ensemble probabilities, not a prediction of the particular angle in our sky. There is no preferred Galactic longitude or latitude, nonzero rotation amplitude, or rotation handedness supplied by this model.

## Why this is the model's prediction

The October 16 frozen C1Q package specifies GR, a minimally coupled canonical scalar with quadratic potential, standard matter, a spatially flat FLRW background, Gaussian growing adiabatic initial perturbations, and zero primordial vector modes. Its model document explicitly excludes an additional Friedmann rotation term and preferred-observer dynamics. Its CLASS configuration retains scalar modes.

Linear isotropic transfer preserves a diagonal Gaussian covariance across distinct temperature multipoles. Rotation-equivariance makes each nondegenerate dispersion axis uniformly distributed; independence of distinct Gaussian multipoles gives the stated relative-angle distribution. The positive spectrum amplitudes affect power, not this ideal axis distribution.

The source package also computes **lensed** spectra. The exact uniform-axis statement here concerns its unlensed linear restriction, not a proof that the fully lensed, foreground-contaminated, masked instrumental sky has this exact likelihood. Nonlinear vector generation and local astrophysical spins are likewise outside the zero-vorticity assertion.

Five small [source snapshots](source/) preserve the relevant specification, with hashes checked against the package's original freeze where supplied. The 22 MB package is identified by SHA-256 in the machine record and is not republished in full. No CLASS or background calculation was rerun to make this lock.

## Prospective numerical check

The new realization set has **not been executed at lock time**. The entire generator and scoring procedure are in [run.cjs](run.cjs).

| Frozen item | Value |
|---|---|
| Sample size | 100,000 independent Gaussian quadrupole/octopole pairs |
| Seed | 2026101810 |
| Generator | Existing checksum-pinned xoshiro128**/SplitMix32 core |
| Coordinates | Right-handed Galactic Cartesian; headless axes |
| Coefficients | C_l=1; real-field conjugacy; exact Gaussian variances in lock.json |
| Primary statistic | Two-sided empirical-CDF distance D_N from U(0,1) |
| Primary test family | One distributional test |
| α | 0.01 |
| Compatibility threshold | D_N ≤ **0.005146997846583986** |
| Stop rule | Exactly 100,000 draws; no seed or threshold retries |

The threshold is sqrt(log(2/α)/(2N)), using the finite-sample Dvoretzky–Kiefer–Wolfowitz–Massart bound under independent draws. The stochastic interpretation assumes the pinned pseudorandom generator adequately implements that sampling law; the bound does not certify a deterministic PRNG. See [Massart (1990)](https://doi.org/10.1214/aop/1176990746).

Means, variances, three angular-window counts and the first ten draws are diagnostics, not additional opportunities to declare success. The outcomes are **COMPATIBLE_WITH_LOCKED_DISTRIBUTION** or **CALIBRATION_FLAG**. A flag can reflect a chance tail event or a computational defect. Neither outcome validates or falsifies the physical universe: the simulation is a check of a stipulated distribution.

Validation of the lock does not consume its new seed:

    node research/cmb-alignment/prediction-lock/v1/check.cjs

When the next numerical test is requested, run once into a new output file:

    node research/cmb-alignment/prediction-lock/v1/run.cjs --execute /tmp/EFMW-CMB-PRED-001-run.json

Keep the result, including a flag or execution failure, and its environment. A repeat with the same seed is reproduction, not another independent prediction. The run refuses to overwrite an existing result. CI validates hashes and state; it does not execute this new realization set.

## Known data and observational gate

The WMAP temperature result, both Doppler treatments, the 13 published variants, and earlier null realizations were already known. They cannot become prospective confirmations by placing them below a new heading. Another satellite or reduction of the same sky can check systematics but does not supply an independent cosmic realization.

**No new observational test is authorized by an empty specification.** The machine record deliberately sets observational readiness to false. Before a later version is eligible for empirical scoring, it must freeze:

1. Exact data products, checksums, the unexamined target and information already seen.
2. Foreground, mask/inpainting, kinematic, calibration, beam/noise and lensing treatments, with identical processing of controls.
3. The complete comparison and selection family, nuisance parameters, likelihood and decision thresholds.
4. Shared-sky covariance and, for polarization tested after temperature selection, the conditional TE relationship.
5. A prediction independent of the data used to develop it, plus an auditable holdout procedure.

A well-calibrated, prospectively specified directional discrepancy could challenge the tested isotropic model, but it would not identify rotation as the cause. A failure of the numerical calibration above is not that observational result.

## Rotating extension: explicit unresolved requirements

The broader rotational EFMW proposal is **not supplied by C1Q v1.0.0**. Its amplitude, evolution, physical axis and CMB transfer operator are null entries meaning **unspecified**, not numerical zero. They remain separate from C1Q's derived zero-vorticity statement.

A rotating extension needs a new model version: covariant equations, observer/fluid definitions and units; derived or explicitly inherited vorticity; fixed TT/TE/EE and applicable handedness/redshift predictions; isotropic and zero-source controls; and a likelihood distinguishing rotation from other anisotropic mechanisms. An arbitrary amplitude or the observed 5.85° separation will not be inserted as its prediction.

## Status, novelty and amendments

| Item | Status |
|---|---|
| C1Q source parameters and initial-mode specification | Demonstrated as preserved source content |
| Zero-vorticity and ideal directional-null consequences | Conditional mathematical predictions of that specification |
| New numerical realization test | Locked, not executed at publication |
| New empirical directional test | Unresolved; input and likelihood specifications incomplete |
| Nonzero rotational EFMW prediction | Unresolved; physical extension unspecified |
| Claim that C1Q predicts the observed alignment as evidence of rotation | Rejected interpretation of this version |

The Gaussian directional null is standard, and this C1Q branch belongs to the canonical-quintessence class. No novel rotation law is claimed. Zoo freeze and anti-circularity discipline is applied; no canonical animal experiment or full-Zoo pass is asserted.

**Amendments are append-only.** Changes to physics, seed, sample size, data, estimator, thresholds or the search family require a new version before evaluation. Preserve this version and every negative result. Hashes and a Git commit establish byte identity and publication history; they do not prove blindness, physical correctness or an external preregistration.
