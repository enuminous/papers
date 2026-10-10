# Finite-Lattice OPH Warm-Ups: Analytic Results, an Exploratory Flux Test, and Lean Cores

**Matthew Chenoweth Wright**  
**October 10, 2026**  
**Research progress report; not a claim of physical validation**

## Abstract

This paper records four finite-lattice workstreams undertaken around Observer Patch Holography (OPH): (1) a heat-bath construction and transfer-spectrum derivation for a uniformly anchored periodic Gaussian scalar model; (2) an independent $U(1)$ character-orthogonality check relevant to a proposed zero-flux argument; (3) an exploratory four-dimensional $N=2$ flux-channel simulation; and (4) a small Lean formalization of reusable algebraic cores. The results are deliberately separated by evidential status. For the specified Gaussian model, conditional heat-bath updates preserve the target Gibbs law and the analytic transfer calculation gives the massive free-scalar lattice dispersion, conditional on a Mehler-kernel spectral relation. The Haar calculation projects onto zero net link exponent; it implies zero plaquette occupation only with an additional topology and boundary condition. The $N=2$ Monte Carlo run did not resolve a positive pole and does not establish a clean no-pole result. Lean verifies the abstract Haar selection rule, the algebra converting a transfer-cosh relation to the dispersion identity, and positivity and zero-momentum properties of the declared spatial symbol. It does not formalize the full Gaussian transfer spectrum, the explicit finite $U(1)^E$ model, or the $N=2$ simulation. None of these results identifies the transfer coordinate with physical time.

## 1. Scope and evidential categories

The work proceeds from explicit finite models rather than treating a desired physical conclusion as an input to be confirmed. We use the following statuses:

- **Demonstrated analytically:** follows from the stated mathematical model and assumptions.
- **Machine-checked:** a Lean declaration compiled in the pinned project.
- **Supported but incomplete:** numerical or analytic evidence is consistent with a statement but cannot decide it.
- **Unresolved:** the source, model, topology, or test sensitivity needed for a conclusion is missing.
- **Not established:** the evidence does not entail the stronger claim.

The research notes and runnable artifacts are in the [`enuminous/oph-lab` fork](https://github.com/enuminous/oph-lab). The paper summarizes those artifacts, rather than replacing their detailed assumptions and run records.

## 2. Uniformly anchored Gaussian model and transfer dispersion

### 2.1 Frozen model

Let φ be a real scalar field on a finite periodic $d$-dimensional hypercubic lattice. Consider the quadratic potential

\[
V(\phi)=\frac12\sum_x\left[ J_0(\phi_{x+e_0}-\phi_x)^2 + \sum_{j=1}^{d-1}J_j(\phi_{x+e_j}-\phi_x)^2 + \kappa\phi_x^2\right],
\]

with $J_0,J_j,\kappa>0$. The corresponding target law is

\[
\pi(d\phi)=Z^{-1}e^{-V(\phi)}\prod_xd\phi_x.
\]

The uniform positive anchor makes the precision operator positive definite. Translation symmetry and the plane-wave dispersion below depend on the periodic lattice and the uniform anchor $\kappa I$; they do not follow from the more general finite-graph model with arbitrary nonnegative site anchors. A nonuniform anchor or irregular graph is outside this derivation.

### 2.2 Heat-bath invariance

For a site $x$, define

\[
D_x=\kappa+2J_0+2\sum_{j=1}^{d-1}J_j.
\]

Completing the square in the terms of $V$ that contain $\phi_x$ gives the exact conditional

\[
\phi_x\mid\phi_{z\ne x}\sim\mathcal N\!\left(
\frac{J_0(\phi_{x+e_0}+\phi_{x-e_0})+\sum_{j=1}^{d-1}J_j(\phi_{x+e_j}+\phi_{x-e_j})}{D_x},\frac1{D_x}\right).
\]

Resampling from this conditional leaves $\pi$ invariant: the joint density factors into the marginal on the other sites times the conditional at $x$. The single-site kernel is reversible, and any fixed random-scan mixture of these kernels is stationary and reversible. A deterministic composition of such updates is stationary, but need not itself be reversible. This is algorithmic sampling time; the argument does not equate update count with the transfer coordinate or physical time.

**Status:** demonstrated analytically for the specified Gibbs law. The heat-bath calculation has not yet been formalized in Lean.

### 2.3 Transfer kernel and lattice dispersion

Fourier transformation in the $d-1$ transverse periodic directions gives, for momentum $k_j=2\pi n_j/L_j$,

\[
\Omega^2(k)=\kappa+4\sum_{j=1}^{d-1}J_j\sin^2(k_j/2).
\]

For the chosen transfer direction, splitting the action symmetrically between neighboring slices yields the one-mode kernel

\[
T_k(q,q')=\exp\!\left[-\frac{J_0}{2}(q'-q)^2-\frac{\Omega^2(k)}4(q^2+q'^2)\right].
\]

Under the Mehler-kernel eigenvalue relation, the transfer gap $E(k)$ obeys

\[
\cosh E(k)=1+\frac{\Omega^2(k)}{2J_0},
\qquad
4J_0\sinh^2(E(k)/2)=\Omega^2(k).
\]

The second equation is the massive free-scalar lattice dispersion for this specialization. It arises from the directional coupling already in $V$; no separate inertial update was added. The analytic note derives the displayed kernel and uses the Mehler spectrum. The Lean project proves only the hyperbolic-algebra conversion once the cosh relation is assumed; it does not prove that the transfer operator has the stated Mehler spectrum or that its Hermite eigenfunctions are complete. No physical clock or causal identification is supplied.

**Status:** analytic derivation conditional on the homogeneous periodic Gaussian model and the Mehler spectral result; only the final algebraic conversion is machine-checked.

## 3. Finite $U(1)$ Haar selection and the zero-flux boundary

Let $E$ be a finite link set, assign independent $U(1)$ variables $U_e$, and let $j\in\mathbb Z^E$. For the product character $\chi_j(U)=\prod_{e\in E}U_e^{j_e}$, normalized product Haar measure gives

\[
\int_{U(1)^E}\chi_j(U)\,dU=\prod_{e\in E}\mathbf1_{\{j_e=0\}}.
\]

If a plaquette occupation vector $m\in\mathbb Z^F$ enters through the oriented boundary map $\partial_2:\mathbb Z^F\to\mathbb Z^E$, Haar integration retains exactly the assignments with $\partial_2m=0$. That is zero net link exponent, or a closed plaquette 2-chain. It does **not** generally imply $m=0$. On a periodic torus, nonzero 2-cycles can survive; concluding that only zero plaquette flux contributes requires a separately established trivial kernel and specified boundary treatment.

This is an independent proof of the character-selection identity under an explicit $N=1\equiv U(1)$ interpretation. The precise intended OPH $N=1$ theorem, including its definition of $N$, lattice complex, action, boundary conditions, and flux observable, was not source-pinned in the materials examined. The match to that intended theorem is therefore unresolved. The Gaussian integral can be factored out only when its precision and source are link-independent (or when their link dependence is separately tracked).

**Status:** the finite character theorem is demonstrated under stated assumptions. “All plaquette flux vanishes” is conditional on topology and boundaries. Equivalence to the intended OPH claim is unresolved.

## 4. Exploratory four-dimensional $N=2$ flux-channel simulation

### 4.1 Model and protocol

The independent implementation used an even periodic four-dimensional lattice and the joint matter/link/conductance weight

\[
V(\psi,U,w)=m^2\sum_{x,s}|\psi_{s,x}|^2+
\sum_{e=(x,y)}w_e\sum_{s=1}^{N}|\psi_{s,x}-U_e\psi_{s,y}|^2.
\]

Conductances were interpreted as independent Gamma(shape $\alpha$, rate $\beta$); the simulated point was $\alpha=2,\beta=1,m^2=1$. Exact coordinate conditionals were used for complex Gaussian matter, von Mises link phases, and Gamma conductances. The update sweep index is Monte Carlo time only.

The observable was the imaginary part of an oriented $01$ plaquette, averaged over the three spatial coordinates on each direction-3 slice. The primary Rao–Blackwell estimator analytically averaged link phases conditional on matter and conductances. The direct and Rao–Blackwell estimates use the same chains and are not independent replications. The published repository contains the aggregate summary CSV, not the per-chain raw JSON series.

Runs used $L=4,6,8$, matched $N=1$ control and $N=2$ target, three independent seeds per $(L,N)$, 1,000 warm-up sweeps, 3,000 measurements per chain, two sweeps between measurements, and chain/circular-block bootstrap intervals over block lengths 50, 100, and 200 with 500 replicates. The exact upstream model revision and conductance convention are not pinned. In addition, initial direct-estimator summaries were inspected before selecting the lower-noise Rao–Blackwell estimator. This estimator choice is a documented post-selection risk; the run is exploratory, not blind confirmation.

### 4.2 Numerical result

The primary $C_N(1)$ estimates and envelope of the 95% block-bootstrap intervals were:

| $N$ | $L$ | $C_N(1)$ | 95% interval envelope |
|---:|---:|---:|---:|
| 1 | 4 | $+2.77\times10^{-11}$ | $[-4.21\times10^{-11},+1.08\times10^{-10}]$ |
| 1 | 6 | $+2.49\times10^{-11}$ | $[-1.32\times10^{-12},+4.87\times10^{-11}]$ |
| 1 | 8 | $-3.58\times10^{-13}$ | $[-8.54\times10^{-12},+8.73\times10^{-12}]$ |
| 2 | 4 | $+2.73\times10^{-11}$ | $[-7.56\times10^{-10},+8.39\times10^{-10}]$ |
| 2 | 6 | $+3.15\times10^{-11}$ | $[-9.94\times10^{-11},+1.59\times10^{-10}]$ |
| 2 | 8 | $-2.20\times10^{-11}$ | $[-7.65\times10^{-11},+2.85\times10^{-11}]$ |

At $N=2,L=8$, the Rao–Blackwell estimates at $t=1,2,3,4$ were respectively $(-2.20,-3.90,-1.86,-8.62)\times10^{-11}$. Intervals at $t=1,2,3$ included zero for every tested block length. At the opposite slice $t=4$, all three block-length intervals were negative; their envelope was $[-1.68\times10^{-10},-7.74\times10^{-12}]$. The direct estimator was much noisier and did not independently resolve the channel.

No positive stable signal suitable for a transfer-gap fit was found. This is **not** a clean no-pole result: a pole with smaller residue is not excluded, no residue sensitivity threshold was preregistered, the source model dictionary remains unpinned, and the negative midpoint requires a reflection-positivity/parity analysis before a physical interpretation. The $N=1$ run is consistent with zero for the tested separated slice, but it does not replace an exact source-matched theorem.

**Status:** exploratory numerical evidence; pole/no-pole classification unresolved. The full performance envelope is limited to the settings actually run. Parameter, boundary, aspect-ratio, and broad nuisance sweeps were not performed.

## 5. Lean formalization and build record

The Stage 4 project is pinned to Lean `v4.35.0-rc4` and Mathlib commit `d3739f06187591e81887886ca767b6a2dc1416ea`. It contains these checked cores:

1. `trivial_character_integral`: a trivial character integrates to one under the stated normalized real mass.
2. `nontrivial_character_integral_zero`: a nontrivial group character has zero integral when left-translation invariance is provided as an explicit hypothesis.
3. dispersion_of_transfer_cosh: the assumed relation $\cosh E=1+\omega/(2j)$, for $j\ne0$, implies $4j\sinh^2(E/2)=\omega$.
4. `latticeOmega_nonneg`, `latticeOmega_zero_momentum`, and `latticeOmega_pos_of_positive_mass`: the declared finite-dimensional symbol
   \[
   \omega(\theta)=\kappa+4\sum_iJ_i\sin^2(\theta_i/2)
   \]
   is nonnegative for $\kappa,J_i\ge0$, equals $\kappa$ at zero momentum, and is strictly positive when $\kappa>0$ and all $J_i\ge0$.

The pinned GitHub Actions build passed on `main` at commit [`d84587e`](https://github.com/enuminous/oph-lab/commit/d84587ee7896688aa9356254f306fed5b49940ea); the [workflow run](https://github.com/enuminous/oph-lab/actions/runs/38088816494) completed successfully. The additional spatial-symbol declarations also passed on a validation branch before promotion to `main`.

These statements do not formalize the heat-bath invariance proof, instantiate product Haar measure on $U(1)^E$, construct the plaquette incidence map, derive the Fourier symbol from the actual finite operator, prove the Mehler spectral theorem, or formalize the simulation. They establish no physical-time conclusion. The transfer-cosh relation remains an explicit input, not a Lean-derived result.

## 6. Provenance and anti-circularity audit

The main dependency paths are:

| Claim | Evidence construction | Material dependency / feedback path | Independent check still needed |
|---|---|---|---|
| Massive scalar dispersion | Uniform $\kappa I$, periodic nearest-neighbor quadratic action, selected transfer axis | The assumed symmetry and mass form are part of the model from which the target dispersion follows | Derive the symbol from the declared operator and prove the transfer spectrum independently; do not present it as evidence that OPH or nature selected this model |
| Zero-flux rule | Haar average of integer link characters; plaquette character uses $\partial_2m$ | Stronger $m=0$ conclusion depends on the chosen topology/boundary conditions | Source-pin intended $N=1$ theorem; independently verify topology and integrated/fixed links |
| $N=2$ pole | Chosen odd-flux observable and its separated-slice correlator | The open pole question helped select the observable; direct summaries were inspected before choosing the primary lower-noise estimator | Freeze source, operator, estimator, residue threshold, and nuisance grid before new chains; use independent labels or analytic transfer reference where available |
| Lean verification | Mathematical definitions and hypotheses frozen in declarations | The transfer relation is assumed; formalization of a consequence cannot validate the assumption | Prove missing transfer/operator link and explicit model instantiations as separate obligations |

No independent physical labels are available in these workstreams. Missing provenance is **N/A**, not a pass. The simulation is useful as an exploratory stress attempt and a reproduction artifact, not as independent confirmation of a positive or negative pole claim.

## 7. Conclusions and next proof obligations

The defensible progress is narrow but concrete: an analytically solved uniformly anchored Gaussian specialization; an explicit $U(1)$ character projection theorem with a topology-sensitive flux interpretation; an exploratory $N=2$ simulation that resolves neither pole nor clean no-pole; and a pinned Lean build for abstract Haar, dispersion algebra, and spatial-symbol sign lemmas.

The next derivations with the best finite proof boundaries are:

1. Prove Fourier eigenvectors and eigenvalues for the finite periodic nearest-neighbor operator, then show that its eigenvalue is the declared `latticeOmega` symbol.
2. Instantiate the abstract Haar theorem on a finite product $U(1)^E$, construct the character from integer link charges, and formalize the incidence map without collapsing closed chains to zero chains absent a topological proof.
3. Formalize the Mehler transfer operator and its spectral gap, including the analytic function-space obligations; keep physical-time identification outside that theorem.
4. For $N=2$, obtain Bernhard's exact versioned model and convention, preregister the estimator, residue sensitivity threshold, parameter perturbations and stopping rule, then run larger-volume chains with archived raw trajectories and an independent reference where possible.

The present evidence supports formal and computational follow-up. It does not establish a new physical law, a physical photon, a no-pole theorem, or that OPH derives physical time.

## Reproducibility and source notes

- [Stage 1: heat-bath repair and anchored-Laplacian transfer analysis](https://github.com/enuminous/oph-lab/blob/main/docs/OPH_ANCHORED_LAPLACIAN_HEAT_BATH_TRANSFER.md)
- [Stage 2: independent finite-lattice $N=1$ zero-flux check](https://github.com/enuminous/oph-lab/blob/main/docs/OPH_N1_ZERO_FLUX_INDEPENDENT_CHECK.md)
- [Stage 3: $N=2$ flux-channel simulation report](https://github.com/enuminous/oph-lab/blob/main/docs/OPH_N2_FLUX_STAGE3.md)
- [Stage 3 summary data](https://github.com/enuminous/oph-lab/blob/main/docs/data/oph_n2_flux_stage3_summary.csv)
- [Monte Carlo sampler](https://github.com/enuminous/oph-lab/blob/main/scripts/oph_n2_flux_mc.py) and [bootstrap summarizer](https://github.com/enuminous/oph-lab/blob/main/scripts/summarize_oph_flux.py)
- [Stage 4 Lean source](https://github.com/enuminous/oph-lab/blob/main/formalization/oph-stage4/OphStage4.lean), [project README](https://github.com/enuminous/oph-lab/blob/main/formalization/oph-stage4/README.md), and [formalization status report](https://github.com/enuminous/oph-lab/blob/main/docs/OPH_STAGE4_LEAN_FORMALIZATION.md)

