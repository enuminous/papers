# QG-018 — Inhomogeneous reciprocal Einstein–scalar gravity

26 November 2026 · Monolithic LLC · exploratory EFMW research · not peer reviewed

**PASS_BOUNDED after a documented numerical repair.** A classical, spherically symmetric, asymptotically flat Einstein–massless-scalar reference evolves spatially varying matter and metric fields together. It is not a derivation from EFMW, a generic 3+1 calculation, a quantum-gravity result, or a black-hole formation calculation.

## Specification

Use G=c=1 and scalar rescaled by sqrt(4 pi). In polar-areal coordinates ds²=-alpha² dt²+a² dr²+r² dΩ², let Phi=∂r scalar and Pi=(a/alpha)∂t scalar (both rescaled). Write f=a^-2=1-2m/r, S=Phi²+Pi², I(r)=∫_0^r x S(x) dx. Then

- m_r = (r²/2-r m) S; m(0)=0.
- m(r)=exp(-I(r)) ∫_0^r (x²/2) S(x) exp(I(x)) dx.
- (log(alpha a))_r = r S; alpha a=1 at the outer boundary, so alpha=exp(I-I(R))/a.
- Phi_t = ∂r(v Pi), Pi_t = ∂r(v Phi)+2v Phi/r, v=alpha/a.
- Regular center: Phi odd, Pi even, a(0)=1, Pi_t(0)=3∂r(v Phi)|0.
- Independent Einstein momentum/flux equation: m_t = r² alpha Phi Pi/a³.

Reference: Gundlach and Martín-García, *Critical Phenomena in Gravitational Collapse*, Living Reviews in Relativity 10, 5 (2007), equations (20)–(26), https://doi.org/10.12942/lrr-2007-5 . These are conventional GR equations. The lapse normalization matches the vacuum exterior at the finite boundary. No external metric time dependence is supplied in the full arm; radial constraints are integrated at every RK stage. The flux equation is not used in the evolution. Its residual is evaluated through a centered directional derivative of the radial mass solution along the matter RHS, not a fully independent spacetime evolution solver. The radial residuals are evaluated by a separate second-order numerical derivative and hence are not identities enforced to machine precision.

## Experimental design

Domain 0≤r≤20, 0≤t≤4, smooth compact initial scalar pulse A exp(1-1/(1-z²)) for |z|<1, z=(r-6)/2, zero elsewhere. Phi is its analytic derivative; Pi=±(Phi+scalar/r), representing initial inward/outward traveling profiles in the flat-space limit. At nonzero gravity they are not exact unidirectional solutions. A=.02,.05,.08; 200,400,800 intervals; time step chosen to be ≤0.2 dr with 40 equal recording intervals. Full arm at all 3 grids (18 trajectories); frozen metric and flat metric at 800 (12 negative-control trajectories). One additional vacuum run. Outer endpoint RHS fixed to zero; recorded outer ten points remain negligible (max <1e-9). Domain stop guard 2m/r≥.85, not a black-hole detection rule. All full runs remain well below it.

Initial implementation used second-order spatial derivatives. All checks except the specified final matter-profile convergence criterion (coarse/fine RMS error ratio >2.5) passed; ratios 1.398–1.907. A supplementary exploratory finer sweep of four profiles with the initial scheme (800,1600,3200 intervals) gave ratios 2.231,2.803,2.715,2.844 in order (.02 inward,.02 outward,.08 inward,.08 outward); the first still failed. The original script, failure log and diagnostic JSON are retained. The revised implementation uses fourth-order centered differentiation of the matter fluxes, parity-aware stencils at the center, trapezoidal radial quadratures, and RK4. The same original thresholds, initial conditions and three principal grids are retained. It passes all nine checks; final profile refinement ratios 2.593–3.014. These are measured ratios, **not proof of fourth- or second-order asymptotic convergence**. The modified scheme was selected after looking at results, so all evidence is exploratory.

## Results

At 800 intervals, across the six complete-model cases:

- Worst normalized radial mass constraint residual 0.0099621453 (0.996%).
- Worst normalized independent momentum/flux residual 0.0034845861 (0.348%).
- Worst relative outer mass drift 0.0000711076 (0.00711%); outer matter stays negligible.
- Vacuum: exact zero mass and scalar, unit lapse and radial metric.
- Frozen metric: all six runs have unit normalized flux residual at some sampled time. Flat metric: all six have unit normalized radial mass residual. Frozen/flat mass constancy by construction is not evidence of consistency.

Normalization: maximum absolute residual over interior nodes divided by maximum absolute corresponding source at that time, with 1e-14 floor; then maximum over sampled times. Mass drift normalized by initial mass, same floor. No claim of pointwise relative accuracy, especially near source zeros.

| Initial amplitude | Direction | Final full vs frozen matter difference (relative Euclidean norm) | Coarse/fine error ratio |
|---:|---|---:|---:|
| .02 | inward | .1004793504 | 2.5953023 |
| .02 | outward | .0055948818 | 3.0046536 |
| .05 | inward | .4152270305 | 2.5930437 |
| .05 | outward | .0343386509 | 3.0139707 |
| .08 | inward | .6290838355 | 2.8166101 |
| .08 | outward | .0842396825 | 3.0073836 |

In the strongest inward case, peak 2m/r rises from .088937708 to .162211805; central lapse falls from .888392521 to a minimum .735678117. Metric changes and final scalar differences between full and frozen arms show reciprocal backreaction in this model. The norm uses equally weighted grid points and both scalar derivatives, not invariant physical distance. No trapped surfaces are reached. In an additional exact flat-space traveling-wave endpoint comparison, the finest flat inward and outward profiles have relative RMS errors 0.0339661 and 0.0108957 respectively; these finite-resolution waveform errors must not be hidden. The relative differences in the full/frozen arms are computed from matched numerical runs and do not constitute an independent exact nonlinear solution comparison.

## Evidence and limitations

1,230 recorded radial snapshots (30 runs × 41), five arrays (Phi, Pi, m, a, alpha) per snapshot. `snapshots.npz` stores all final-sweep profiles and three radial grids. `results.json` contains complete recorded diagnostics plus vacuum diagnostics and assertions. The initial failed run is preserved as `initial_attempt.py`, `initial_failure.log`, `initial_results.json` (its full field snapshots were overwritten by the revised run; they can be regenerated by replaying the initial code in a separate directory). The supplementary finer exploratory results are summarized above, not archived as full profiles. `index.html` is a downsampled offline viewer of the six matched finest-grid triplets, not a solver. 

All checks are internal numerical diagnostics. The model imposes Einstein gravity, spherical symmetry, a gauge, compact initial data and finite-grid boundary conditions. Spherical symmetry removes gravitational tensor radiation; no quantum operators or microscopic EFMW-specific dynamics occur. Generic inhomogeneous 3+1 Einstein evolution, nonlinear quantum constraints, unique EFMW predictions, independent replay and empirical validation are outstanding.

## Replay

Create a separate directory for each run if preserving existing outputs. Install pinned dependencies in `requirements.txt`. Run `OPENBLAS_NUM_THREADS=1 python run.py`. Expected nine boolean checks are true, subject to ordinary numerical-platform variation. `python verify.py` checks the packaged originals (replaying may change log timing and archive metadata). `python flat_check.py` reproduces the additional exact flat endpoint comparison. All test thresholds are defined in run.py. Do not interpret this as independent reproduction.

## Next gate

QG-019: implement a perturbative reciprocal quantum field–geometry reference or a constrained quantization in spherical symmetry; distinguish semiclassical sourcing, operator-valued geometry, and quantum constraints. A classical nonlinear reference is now available, but quantization and microscopic emergence remain unresolved.

## Published evidence

Source, interactive viewer, full diagnostic JSON, failure records and replay instructions: https://github.com/enuminous/Quantum-Gravity/tree/ec7b038e6233554f251d2e0abddd674dfaaa1095/QG-018 . All 13 text artifacts match their local Git blob hashes. The full binary radial snapshot archive remains in the local download package; it can be regenerated by the published solver. No independent scientific replication has occurred.
