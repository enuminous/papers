# QG-017 — Reciprocal Einstein–matter dynamics

26 November 2026 · Monolithic LLC · EFMW exploratory research. Not peer reviewed.

**Verdict: PASS_BOUNDED for a constructed homogeneous classical Einstein–scalar reference; emergence from EFMW and inhomogeneous quantum gravitational backreaction remain unresolved.** This is a new symmetry-reduced reference, not a reciprocal extension of QG-016's spatially resolved elastic lattice.

## Specification

The supplied action is conventional Einstein gravity with a minimally coupled scalar: S = ∫√−g [R/(16πG) − (∇φ)²/2 − V(φ)] d⁴x. Set 8πG=1 and fiducial coordinate volume=1. In Bianchi I use lapse N, α=ln a, β± with directional exponents α+β+±√3β− and α−2β+. The reduced Lagrangian (after the standard boundary term) is

L = exp(3α)[(−3α̇²+3β̇+²+3β̇−²+φ̇²/2)/N − NV].

In proper time define H=α′, s±=β±′, v=φ′, ρ=v²/2+V, p=v²/2−V. Then

- α′=H; β±′=s±; s±′=−3Hs±;
- H′=−3(s+²+s−²)−v²/2; φ′=v; v′=−3Hv−V′(φ).
- C=3H²−3(s+²+s−²)−ρ=0 from lapse variation.

The evolution written above uses the constraint to simplify the Einstein equations. Its algebraic extension away from C=0 satisfies C′=0; this is not an off-shell test of the full 3+1 diffeomorphism algebra. Direct differentiation cancels all terms. Removing v²/2 from H′ gives C′=+3Hv²; removing 3Hv from the scalar equation gives C′=−3Hv². Both controls are deliberately inconsistent, not alternative covariant theories. They start from exactly the same constraint-satisfying data. No constraint projection or reset occurs. For expanding solutions H decreases, and scalar energy density decreases when v≠0; in contraction the signs reverse for density evolution.

Canonical momenta are pα=−6a³H, p±=6a³s±, pφ=a³v. The independent canonical integrator uses Hcan=N Ccan with Ccan=a⁻³(−pα²/12+(p+²+p−²)/12+pφ²/2)+a³V. This agrees with the velocity equations on the constraint surface. Variation of lapse enforces Ccan=0. No claim of quantum constraint closure follows from this reduced classical system.

Matter obeys ρ′=−3Hv² and d(a³ρ)/dτ=−p d(a³)/dτ. W=∫p d(a³); the diagnostic a³ρ+W is constant. This is a pressure-work balance, not a separately conserved global gravitational energy. Shear momenta a³s± are constant. For V=0, f=1+3H₀τ, a³=a₀³f, H=H₀/f, s±=s±₀/f, v=v₀/f, β±=β±₀+s±₀ ln(f)/(3H₀), φ=φ₀+v₀ ln(f)/(3H₀). Compare only f>0. For lapse N(t)=1+.3 sin(t), τ=t+.3(1−cos t); compare equal proper times.

## Design and results

Three potentials V=m²φ²/2+λφ⁴/4: massless (m,λ)=(0,0), quadratic (.7,0), mixed quartic (.35,.4). Two initial H signs; four deterministic seeds per combination, including isotropic shear seed 0. 24 full runs and 48 matched ablations, 101 samples each. Main matched proper-time window .6/|H₀| for expansion, .17/|H₀| for contraction. 24 independent canonical and 24 lapse-reparameterized runs; 8 analytic massless comparisons, 8 RK4 refinement runs, 128 arbitrary states × 3 identities = 384 off-shell checks. DOP853 rtol=2e−12, atol=2e−13. Relative constraint uses 3H²+3(s+²+s−²)+ρ+1e−15 as denominator; scaled state error uses 1+|reference| componentwise. Thresholds are exploratory and embedded in run.py, not preregistered.

| Diagnostic | Observed maximum |
|---|---:|
| Full relative constraint residual | 7.8658954e−12 |
| Full absolute constraint residual | 1.2028711e−12 |
| Pressure-work scaled residual | 2.7678837e−12 |
| Shear-momentum residual | 6.8209327e−13 |
| Canonical/velocity scaled difference | 7.0103470e−12 |
| Canonical scaled Hamiltonian residual | 3.8022676e−12 |
| Equal-proper-time lapse scaled difference | 6.7944542e−12 |
| Analytic massless scaled difference | 2.8196170e−12 |
| Off-shell derivative identity error | 2.7200464e−15 |
| Matter→geometry removed: max relative violation | .9468060 |
| Geometry→matter removed: max relative violation | .999999228 |

All 48 controls exceeded .001 relative violation; minimum per-run maxima .1072978 and .0688713 respectively. Across the controls the largest H difference (no matter→geometry) was .29746994, and largest φ difference (no geometry→matter) was .62901311. These show sensitivity, not novel EFMW physics. RK4 expansion final scaled errors from 64/128/256/512 steps: 2.08607e−9, 1.29215e−10, 8.02650e−12, 4.87397e−13. Contraction: 6.71951e−10, 4.22285e−11, 2.54920e−12, 5.89408e−14. Fine-grid errors approach the adaptive-reference floor. Eleven assertions pass.

## Stress test and retained development failures

Initial matched expansion horizon 2.5/|H₀| encountered a step-size failure in an ablated trajectory; shortened the matched comparison window to .6/|H₀| and retained the original attempted source as initial_attempt.py. A NumPy bool JSON serialization failure was corrected by explicit bool conversion; serialization_failure.log is retained. In a separate long-window stress test of the same 12 expanding starts and all three arms (36 runs), terminate at |H|/|H₀|=20 or a³=.001. All 12 full and 12 no-matter→geometry runs completed the requested long window; 11 of 12 no-geometry→matter controls crossed a stopping threshold. No solver errors occurred with the stopping rule. These stops are numerical domain limits in deliberately inconsistent models, not evidence for physical singularities or bounces. Contracting comparisons stop before the massless singular time. No singularity avoidance claim.

## Replay and artifacts

`OPENBLAS_NUM_THREADS=1 python run.py` regenerates results.json and primary_trajectories.npz. `python verify.py` verifies archived SHA-256 digests; verify before replay because the binary archive may differ in representation across versions. Requirements pinned. results.json includes every primary run summary, all independent canonical/lapse/analytic residuals, off-shell identities, refinement results, 18 representative trajectories and long-window outcomes. primary_trajectories.npz stores every primary 101-sample state; each key encodes potential, sign, seed and arm; rows are proper time, α,H,β+,β−,s+,s−,φ,v,W. Interactive index.html embeds representative trajectories and requires no external libraries. Raw auxiliary integration trajectories are not retained; their diagnostics are. No independent scientific replication has occurred.

## Limitations and next gate

Classical spatially homogeneous Bianchi I has no propagating local matter or gravitational-wave degrees of freedom; one global Hamiltonian constraint is not the full local hypersurface-deformation algebra. Although the action is covariant before reduction, the simulation tests only homogeneous dynamics and time-reparametrization. The scalar potential, seeds, durations, normalization and stress thresholds are exploratory. The established action is supplied, not derived from EFMW. Neither microscopic gauge emergence, Lorentzian quantum geometry, nor quantum Einstein dynamics is established. QG-018 should test an inhomogeneous reciprocal Einstein–matter reduction with local Hamiltonian and momentum constraints, compare constraint propagation against QG-011 and QG-016, and retain ablations.

References: Bianchi I canonical minisuperspace and lapse constraint, https://doi.org/10.1140/epjc/s10052-019-7193-6 ; Bianchi I scalar and shear equations, https://indico.mpp.mpg.de/event/1856/contributions/2366/attachments/2120/2391/Uhlemann_Cora_23_2012.pdf . Prior lab: https://github.com/enuminous/Quantum-Gravity/tree/1b6232da9565e64dccdeed6a57a1a1c4a1f4eaa6/QG-016 .

## Published evidence

- Exact source, raw trajectories and browser lab: https://github.com/enuminous/Quantum-Gravity/tree/65b9b1a812bf72963bd7d8f3364c40115a040d3d/QG-017

All twelve lab files were verified against local Git blob hashes before commit. Independent scientific replication remains outstanding.
