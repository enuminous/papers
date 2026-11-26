# QG-016 — Gravity meets matter: conserved classical source dynamics

26 November 2026 · Monolithic LLC · EFMW exploratory investigation. Not peer reviewed. **PASS_BOUNDED_LINEAR_SOURCE_REFERENCE**; no claim of emergent or quantum gravity.

## 1. Scope and result

QG-015 established a local staggered linearized ADM reference with two physical tensor modes and infrared relativistic dispersion. QG-016 adds independently evolving, spatially extended classical matter on that same prescribed periodic lattice. A conserved anisotropic elastic source produces both tensor polarizations, in agreement with an analytical driven-oscillator reference. An isotropic acoustic source produces no TT response at linear order. Constraint propagation succeeds for the matched conserved source and fails when density conservation or spatial stress coupling is deliberately broken. Notably, freezing the source density changes the scalar constraint residual while leaving the tensor wave exactly unchanged. This is a direct diagnostic of the inadequacy of a waveform-only verification test.

This is one-way test matter forcing, not a self-consistent Einstein–matter action, reciprocal matter–geometry evolution, an isolated outgoing radiation simulation, or a quantum model. Gauge constraints, matter constitutive law, background, normalization and diagnostic thresholds were chosen, not derived from EFMW. The density is a signed mean-zero perturbation, not the total positive rest-energy density of an isolated object. A homogeneous density background would require a different gravitational background or boundary treatment. No scientific novelty over conventional linearized GR is asserted.

## 2. Pinned source and local operators

QG-015 reference source is copied byte-for-byte as `qg015_reference.py` from commit `e2490da554158f4b8a18aa90f4e7786baaee87f1` at `QG-015/run.py`; its local Git blob ID is `808971a79a16d7fe50d7d2c5af18a3d20ac053ec` (matches published blob). Reference: https://github.com/enuminous/Quantum-Gravity/tree/e2490da554158f4b8a18aa90f4e7786baaee87f1/QG-015 .

We use the orthonormal six-component symmetric tensor basis B with diagonal unit entries and off-diagonal entries 1/sqrt(2). Normal components live at vertices, off-diagonal components on face centers and vectors at edge centers. Forward and backward nearest-neighbor differences are f_i a=a(x+e_i)-a(x) and b_i a=a(x)-a(x-e_i), with periodic boundaries and lattice spacing 1. D is the staggered tensor divergence, D* its adjoint (negative symmetric gradient), div is edge-to-vertex divergence, grad its negative adjoint, Δ=sum b_i f_i, tr the trace and lift(s)=s I. Define:

```
R(h) = div D h - Δ tr(h)
Kπ(p) = p - lift(tr p)/2
Kh(h) = -Δ h - 2 D*D h + D*grad(tr h) + lift(-div D h + Δ tr h)
```

The reused operators satisfy R Kπ=div D, D Kh=0 and R D*=0. These are exact discrete identities in real arithmetic on this periodic staggered construction. The homogeneous mode is not a propagating TT degree of freedom and is not sourced here.

## 3. Conserved test matter and sourced gravity

Dimensionless time and space; c=1. Let u be a negative-displacement-like vector at edges and j its time derivative, with the convention that j is negative momentum density. The independent matter stress S is

```
e = -D* u
S = A e
u_dot = j
j_dot = D S
rho_dot = div j
```

The symmetric constitutive matrix A is local and positive semidefinite in the acoustic arm and positive definite in the elastic arm. The acoustic arm is A=.25 t t^T, t=(1,1,1,0,0,0). Its longitudinal speed is .5; the other two directions have zero restoring force. The elastic arm is

```
A = [[.50,.12,.18,0,0,0],
     [.12,.40,.04,0,0,0],
     [.18,.04,.36,0,0,0],
     [0,0,0,.20,0,0],
     [0,0,0,0,.24,0],
     [0,0,0,0,0,.16]]
```

Cross-normal couplings are vertex-local; the shear block is diagonal so no cross-stagger interpolation is needed. With initial rho=div u, the continuity equation preserves that relation. The source has exactly conserved mean rho and j in the semidiscrete equations. The isolated matter quadratic energy E_m=(||j||²+<e,Ae>)/2 obeys dE_m/dt=<j,DS>-<D*j,S>=0. No claim of conserved *combined* gravity–matter energy is made, because the source evolution is independent of h and p. The largest speed in 128 seeded random unit directions is .6944941785996073 for the elastic model; this is a sampled speed diagnostic, not a theorem of relativistic microphysics.

With kappa=.1 (absorbing source normalization, corresponding to 16πG in matching continuum GR conventions), use

```
h_dot = Kπ p
p_dot = -Kh h + kappa S
C = R(h) - kappa rho
M = D p - kappa j
```

Direct substitution gives C_dot=div M+kappa(div j-rho_dot) and M_dot=kappa(D S-j_dot). With conserved source C_dot=div M and M_dot=0. If C=M=0 initially, they stay zero. This is constraint propagation, not a derivation of a nonlinear first-class algebra with dynamical matter Poisson brackets. Explicit fixed-lapse/shift equations are used. In the stress-omission control, M_dot additionally contains -kappa D S (matter remains independently conserved). In the frozen-density control rho_dot=0, the additional scalar term is kappa div j; this deliberately violates continuity.

## 4. Initialization, analytic wave reference and numerical protocol

Wavevectors k=2πd/L and q_i=2 sin(k_i/2). For a single Fourier mode, D(q) contracts the orthonormal tensor basis with q. The matter normal modes obey omega_m² v=(D(q) A D(q)^T)v. Choose the eigenvector with greatest longitudinal overlap, fix its sign, and initialize u=a v sin(k·x+edge phase), j=0, rho=div u, with a=1e-3/|q| (or twice this for linearity test). The initial metric is h=lift(kappa rho/(2|q|²)), p=0; hence both sourced constraints hold and the TT sector starts at zero. TT analysis uses a transverse basis derived from q; TT projection is *not* used in the gravitational evolution. The polarization source amplitudes s_TT are the projected A D(q)^T a v; omega_g=|q|. The exact test solution is

```
h_TT(t) = kappa s_TT (cos(omega_m t)-cos(omega_g t))/(omega_g²-omega_m²).
```

The tested frequencies are nonresonant. The model is integrated locally on the real staggered lattice with classical RK4 (all five state variables updated together at every stage). No constraint projection or post-step correction. Diagnostic times 0 through 8 inclusive. Seeds 16026 (off-shell, gauge perturbation), 16027 (sampled speeds). Program checks set before the run: absolute tolerance 2e-10 for algebra and constraints; 12–20 refinement-error ratio for RK4; max wave error <1e-6; isolated matter energy relative error <1e-3; specified negative control residuals >1e-5; both nonzero oblique tensor source components >1e-6; acoustic/zero-coupling nulls and gauge/linearity comparisons <2e-10. The freeze-density waveform identity is additionally asserted in the final replay. These are exploratory acceptance thresholds, not a registered independent confirmatory test. Numerical diagnostic arrays in results.json are recorded samples, not full spatial field checkpoints; fields can be regenerated with run.py.

Twelve trajectories: oblique elastic L=8 with dt=.2,.1,.05; axial elastic L=8,12,16 with dt=.1; oblique acoustic L=8 dt=.1; matched oblique elastic with added h and p gauge shifts; frozen-density and omitted-gravity-stress controls; zero coupling; double source amplitude. The axial size scan holds the integer mode fixed (physical wavelength changes), not a fixed-domain continuum refinement. 1,012 time samples. Twenty arbitrary off-shell field tests, four seeds on each of L=4,6,8,12,16. 128 seeded unit directions for matter speeds.

## 5. Results

All programmed assertions passed (Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0). Absolute maximum off-shell scalar and momentum propagation identity residuals: 7.993605777301127e-15 and 1.855460229904793e-14. Relative matter-energy identity residual: 2.907916525408748e-17. Maximum mean density and momentum rate residuals: 8.326672684688674e-17 and 6.579099405186112e-17.

| Matched oblique L=8, dt=.1 | Max scalar residual | Max momentum residual | Max TT amplitude |
|---|---:|---:|---:|
| Conserved elastic | 1.7482760e-18 | 1.3383121e-19 | 3.8818496e-6 |
| Frozen density | 1.9591666e-4 | 1.3383121e-19 | 3.8818496e-6 |
| Stress omitted | 1.9591666e-4 | 3.9958694e-5 | 1.0842022e-19 |
| Isotropic acoustic | 2.7579393e-18 | 2.2361670e-19 | 2.0328791e-20 |
| Zero coupling | 0 | 0 | 0 |

Both oblique elastic polarizations are excited; max magnitudes 3.881849645047575e-6 (plus), 5.943070837165093e-7 (cross). Source stress TT amplitudes 2.3545141081178535e-5 and -3.6047362497672556e-6. Frequencies omega_g=1.3256542961423672, omega_m=.7934928432354765. For all ten consistent trajectories, max C residual 9.19701880209457e-17, max M residual 7.066372362469e-18, max isolated matter energy relative error 8.846964762110332e-6. All source density continuity and momentum identity defects zero in implemented RHS. Maximum rho-div u residual 2.1141942363467336e-18. Max sampled |h| across these weak-field trajectories .0006895577012199443; no nonlinear dynamics claimed.

| dt | Maximum TT analytical error | Previous/finer error ratio |
|---:|---:|---:|
| .2 | 7.529124847755163e-10 | — |
| .1 | 4.997126948533655e-11 | 15.066907295530067 |
| .05 | 3.2223247634844874e-12 | 15.507831504636954 |

Gauge-shifted TT trajectory difference 1.3552527156068805e-20; double-amplitude linearity defect exactly 0 in this computation. **Frozen-density and conserved TT trajectories agree exactly (difference 0), despite the large constraint violation.** This is expected from the decoupled linear tensor equation but important for audit: wave agreement alone does not establish consistency of the sourced gravitational system. The omitted-stress control detects both missing tensor forcing and constraint violations. No negative control was excluded from the report.

## 6. Evidence register

| Obligation | Status |
|---|---|
| Independent local classical source dynamics | PASS — constructed |
| Discrete continuity, momentum and isolated matter energy identity | PASS — model |
| Sourced linear constraint propagation | PASS — bounded |
| TT stress drives two polarizations | PASS — chosen anisotropic mode |
| Acoustic and uncoupled null controls | PASS |
| Analytical wave correspondence and time-step refinement | PASS |
| Gauge-related tensor wave agreement | PASS |
| Source conservation can be omitted | FAIL — mechanism-removal control |
| Tensor-wave correctness sufficient for gravitational consistency | FAIL — frozen-density counterexample |
| Generic positive-density isolated matter source or outgoing radiation | UNRESOLVED |
| Reciprocal backreaction and total energy conservation | NOT IMPLEMENTED |
| Nonlinear coupled Einstein–matter constraint algebra | UNRESOLVED |
| Microscopic emergence or quantum gravity | UNRESOLVED |

The results demonstrate conventional linearized mathematics on a specified discretization; not an empirical finding about physical spacetime or validation of EFMW. No independent scientific replication has taken place.

## 7. References and next gate

- QG-015 pinned reference above.
- MIT, *Wave equations*, acoustic wave equations, https://math.mit.edu/icg/resources/teaching/18.367/notes367.pdf .
- J. Novak, *General Relativity and Gravitational Waves*, linearized gravity and generation of gravitational waves, https://apc.u-paris.fr/APC/Conferences/Site_Cargese/Courses_files/novak_notes.pdf .
- QG-011 nonlinear classical symmetry-reduced constraint benchmark, as documented in the interim report: https://github.com/enuminous/papers/blob/856119a1f9b821e3da3b4346d06e8230824d0080/EFMW-Quantum-Gravity-Interim-Report-QG-003-013-2026-11-26.md .

QG-017 should introduce reciprocal dynamics derived from one covariant action, beginning with Einstein–scalar matter in a tractable symmetry reduction. Test constraint propagation, geometric feedback on matter, exchange/conservation laws where defined, boundary conditions and nonlinear convergence. Do not simply add a hand-tuned force to j: that changes source conservation and can break the linearized constraint system. The next gate is genuine coupled classical dynamics; quantization and derivation from microscopic connectivity remain separate later gates.

## 8. Replay

`python -m pip install -r requirements.txt` then `OPENBLAS_NUM_THREADS=1 python run.py > log.txt`. `python verify.py` checks the committed SHA-256 manifest. `index.html` is a self-contained offline interactive diagnostic browser displaying rounded samples from results.json; raw results are authoritative. Integrity verification is not independent scientific reproduction. No browser-dependent compute is required. The HTML JavaScript was syntax checked, not visually tested in a live browser.

## Published evidence

- Exact source and evidence: https://github.com/enuminous/Quantum-Gravity/tree/1b6232da9565e64dccdeed6a57a1a1c4a1f4eaa6/QG-016
- Browser lab source: https://github.com/enuminous/Quantum-Gravity/blob/1b6232da9565e64dccdeed6a57a1a1c4a1f4eaa6/QG-016/index.html

All nine laboratory files were checked against their local Git blob hashes before commit. Independent reproduction remains outstanding.
