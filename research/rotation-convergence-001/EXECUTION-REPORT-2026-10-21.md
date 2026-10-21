# RC-001 Execution report — 21 October 2026

## Execution environment
Python 3.11 environment with NumPy 2.3.5, SciPy available; Linux container. Lean, lake and elan were **not installed**, and GitHub DNS resolution from this container failed. Consequently **no local Lean compilation occurred**. A pinned Lean 4.28/Mathlib lake project and GitHub Actions workflow were committed; remote build status is **unverified**.

## A. Ordinary scalar-wave flux control (executed)
Exact baseline: φ=(x²+t²)y/2, π=ty, j=π∇φ, predicted curl(j)=-txy. Grid sizes n=21,41,81,161; times t=0,0.1,0.4,1,-0.4. All 20 cases agreed with formula within the largest absolute interior error **2.49e-14**. Zero-time control yielded exactly zero at every grid size. Three extra reversed-flux controls (n=21,41,81; t=0.4) matched their sign-reversed expectations at ≤3.00e-15. **23 cases checked**.

This diagnostic flux is *not* the physical Landau-frame velocity. Its curl is not physical fluid vorticity. The selected polynomial is differentiated exactly by centered differences up to roundoff: these values do not constitute empirical significance or meaningful order-of-convergence evidence.

## B. Independent two-scalar C1-compatible Landau-frame sample (executed)

Recovered frozen source: [EFMW-C1-LOCAL-VORT-001](../cmb-alignment/nonzero-vorticity/v1/DERIVATION.md) (relative path correction: [open source](../../research/cmb-alignment/nonzero-vorticity/v1/DERIVATION.md)).

Here a second, independent numerical implementation was performed in a Python notebook using stress tensors constructed directly from
φ=t(1+x), χ=t(1+2y) in Minkowski units. For each coordinate, form T^{μν}=Σ ∂^μφ_i∂^νφ_i-(1/2)η^{μν}Σ(∂φ_i)^2, solve the 4×4 eigenproblem for the unique normalized future-directed timelike energy-frame vector, and compute the four-dimensional Levi-Civita contraction through fourth-order centered finite differences. This numerical path does not use the analytic vorticity formula to compute the measured values. Compare separately with the published analytic root formula.

| (t,x,y) | Analytic ω̂^z | Independent finite difference at h=0.0005 | Absolute error |
|---|---:|---:|---:|
| (0,0,0) | 0 | 0 | 0 |
| (0.01,0,0) | -1.50018748125e-6 | -1.50018748466e-6 | 3.41e-15 |
| (0.05,0.1,-0.1) | -2.08527839428e-4 | -2.08527839454e-4 | 2.61e-14 |
| (0.1,0,0) | -1.51855915116e-3 | -1.51855915123e-3 | 6.97e-14 |
| (0.1,0.15,-0.12) | -1.52504372595e-3 | -1.52504372595e-3 | 4.42e-16 |

Finite-difference steps h=0.002,0.001,0.0005 were tested; errors decreased as step shrank for these samples. The signed analytic value at the origin and t=0.1 matches the previously published frozen construction.

**Interpretation:** Selected points from the local two-scalar Landau vorticity calculation have now been independently recomputed with a distinct eigenvector/differentiation implementation. This is a substantial mathematical replication, **not a full re-execution** of the frozen verification protocol (125-point grid, random 10,000 orientations, all ablations, freeze hash validation, and symbolic checks were not rerun here). The model is ordinary free massless two-scalar dynamics, allowed as a C1 specialization with the EFMW-specific interactions set to zero. It does **not** distinguish EFMW from conventional physics.

## C. Formal Lean compilation
**Not achieved.** Candidate `RotationBridge.lean`, `lean-toolchain`, `lakefile.toml`, and CI workflow were created. The remote workflow's success/failure has not been verified. Any errors must be fixed against actual Lean logs, not assumed absent.

## D. Zoo/cosmology
The existing audit and predeclared cosmology gates remain applicable. No integrated Einstein-constraint dynamics, CMB likelihood, cosmological vorticity spectrum, preferred axis or global rotation has been executed or established.

## Decision
Mathematical rotational correspondence: **analytic PASS, formal compilation open**.
Ordinary flux control: **PASS, physics non-diagnostic**.
Local two-scalar Landau-frame reproduction: **PASS for five sample points; full suite open**.
Unique EFMW dynamical novelty: **NO SUPPORT; conventional free two-scalar theory already produces this local effect**.
Self-consistent cosmology: **OPEN**.
