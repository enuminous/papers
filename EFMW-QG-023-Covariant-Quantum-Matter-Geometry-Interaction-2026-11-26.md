# QG-023 — Covariant weak-field scalar–metric interaction

26 November 2026 · Monolithic LLC · EFMW exploratory laboratory. Not peer reviewed.

**PASS_BOUNDED (18/18 implementation diagnostics).** This is a conventional perturbative Einstein–scalar reference, not an emergent EFMW derivation or an interacting quantum spacetime simulation. The quantum arm evaluates on-shell tree exchange; the retarded arm evaluates a separate classical distributional quadrupole source. They are not the same time-dependent matter configuration. No nonlinear quantum Ward identities, loop renormalization, interacting stress-energy conservation, radiation reaction, causal quantum channel, or physical measurement is established.

## 1. Specification

Use c = hbar = 1 and signature eta = diag(-1,1,1,1). Start with the Einstein–Hilbert action plus two minimally coupled real scalar fields:

    S = integral sqrt(-g) [R/(16 pi G) - sum_a ((grad phi_a)^2 + m_a^2 phi_a^2)/2] d^4x.

The linear expansion g = eta + kappa h, kappa^2 = 32 pi G, gives the leading metric–stress coupling kappa h_{mu nu} T^{mu nu}/2 (for covariant metric perturbation). Free external scalar matrix elements, with external normalization factored out, are

    V^{mu nu}(p',p) = p'^mu p^nu + p'^nu p^mu - eta^{mu nu}(p' dot p + m^2).

Direct contraction with q = p'-p gives

    q_mu V^{mu nu} = (p'^2+m^2) p^nu - (p^2+m^2) p'^nu.

It vanishes on shell. This is the leading free-scalar Ward identity, not a claim about the Ward identities of a resummed, loop-corrected, or nonlinear coupled system.

## 2. Quantum tree-exchange arm

For distinguishable scalar species A and B the t-channel numerator in de Donder gauge is

    N = V_A^{mu nu} V_B,mu nu - (tr V_A)(tr V_B)/2.

Overall S-matrix phase/sign conventions aside, matching to the static Born potential in the center-of-momentum frame gives

    V_Born(q) = -kappa^2 N / (16 E_A E_B |q|^2).

At small momentum N -> 2 m_A^2 m_B^2, yielding -4 pi G m_A m_B / |q|^2, whose inverse Fourier transform is -G m_A m_B/r. The tested dimensionless ratio to Newtonian exchange is N/(2 E_A E_B m_A m_B). This is tree-level Born matching, not an all-orders potential or a bound-state solution. There is no additional Newtonian term in the exchange amplitude.

Generate 128 deterministic random elastic COM events (seed 23001), masses in [0.5,2.5], momentum magnitude in [0.05,1.8], non-forward directions, and boosts with speeds in [0.05,0.75]. Test vertex conservation, decoupling from q_mu xi_nu+q_nu xi_mu, numerator invariance, and a representative longitudinal propagator-numerator change proportional to (q.V_A) dot (q.V_B)/q^2. This tests a longitudinal insertion, not an exhaustive covariant gauge-parameter family. Controls omit the eta term in the vertex, or move the final particle energies off shell by +/-0.12 preserving overall four-momentum. The latter is expected to obey the off-shell identity, not the on-shell zero.

For q^0=0, conservation implies spatial stress and momentum density are transverse to q. Write rho=V00, j_i=V0i, P_ij=delta_ij-n_i n_j, S=P V_spatial P, s=tr S and S_TT=S-P s/2. Algebraically,

    N = rho_A rho_B/2 + (rho_A s_B+s_A rho_B)/2 - 2 j_A dot j_B + S_A^TT:S_B^TT.

These are a COM-frame decomposition of the same exchange numerator, not separately invariant interactions or a canonical constrained Hamiltonian. The TT term alone misses Newtonian attraction. A second 63-case grid spans seven momenta, three mass pairs and three scattering angles. At p=.001, the largest ratio error is 6.842122830752473e-6; dropping the trace subtraction in the propagator gives a minimum ratio 1.9999986843646032; adding another Newtonian term gives minimum ratio 2.000003047005812; TT-only maximum absolute ratio 9.226179130519247e-13. Thus both double-counting and a wrong tensor propagator can introduce a factor-of-two error in the static limit. The deviation at large p is not a numerical failure: the Newtonian approximation is not valid there.

| Diagnostic | Maximum |
|---|---:|
| External mass-shell residual (absolute) | 6.21725e-15 |
| Normalized vertex conservation | 1.13872e-15 |
| Normalized pure-gauge coupling | 1.13777e-15 |
| Normalized Lorentz numerator error | 2.49036e-15 |
| Normalized longitudinal insertion | 8.41592e-30 |
| Missing vertex trace longitudinal insertion | 0.484121 |
| Missing vertex trace conservation residual | 0.419884 |
| Off-shell identity residual | 2.94122e-15 |
| Off-shell on-shell-condition violation (vertex residual) | 1.09036 |
| COM decomposition residual | 5.16322e-16 |

Normalization is explicit in run.py: vertex residual by max(1, norm(q)*max(norm(A),norm(B))); numerator error by max(1, abs(N)); pure-gauge residual by max(1,norm(q)*norm(T)). Norms here are Euclidean diagnostic norms, not Lorentz scalars. The Lorentz invariance check compares the contracted numerator, not those diagnostic norms.

## 3. Independent classical causal-response arm

Let gamma denote the dimensionless metric perturbation (gamma=kappa h), with trace reverse bar gamma. In Lorenz gauge, Box bar gamma^{mu nu}=-16 pi G T^{mu nu}. Retarded boundary conditions give bar gamma(t,x)=4G integral T(t-|x-y|,y)/|x-y| d^3y. For a conserved source, differentiation of the retarded solution gives the Lorenz gauge identity.

Choose F(t,x)=f(t) delta^3(x), a distributional idealization localized at the origin, and the constant traceless symmetric matrix M=[[1,.35,0],[.35,-1,0],[0,0,0]]. The pulse f(t)=[4(t/T)(1-t/T)]^6 for 0<t<T=2, zero otherwise. Define

    T00 = M_ij partial_i partial_j F
    T0i = -M_ij partial_t partial_j F
    Tij = M_ij partial_t^2 F.

Indices here are contravariant. Commutativity of partial derivatives gives exact partial_mu T^{mu nu}=0. This is a signed, distributional quadrupole source with zero integrated energy, not a positive-energy dynamical scalar field, and not a model of a physical binary. Its Fourier algebra was checked at 64 random four-momenta. The conservation residual is 3.07902e-15, compared with 24.85188 for the omitted momentum-density control.

Set U=f(t-r)/r at r>0. The retarded trace-reversed metric is 4G times the same derivative pattern applied to U. G=1e-6 is chosen to keep sampled metric perturbations small. Away from the source Box U=0 and partial_mu bar gamma^{mu nu}=0. No near-origin weak-field validity is asserted. The original metric with lowered indices is gamma=eta bar_gamma eta - eta tr(bar_gamma)/2. The lab independently estimates the tidal matrix

    R_0i0j = (partial_0 partial_i gamma_0j + partial_j partial_0 gamma_i0 - partial_j partial_i gamma_00 - partial_0^2 gamma_ij)/2.

This is a linearized gauge-invariant curvature observable; its numerical evaluation uses second-order centered differences. Tidal plus = (R_0x0x-R_0y0y)/2; cross = R_0x0y. These are transverse components measured along the z axis and are not asserted to be a pure far-zone TT field at finite radius.

Detectors at r=2,4,8 (z axis), 231 times per detector, from t=-.5 to 11, with finite-difference step .002. The causal test excludes 0.02 around the pulse edges so the derivative stencil does not cross the front. All sampled metric and tidal responses before t=r and tidal responses after t=r+2 vanish exactly outside the guard interval; both polarizations are nonzero during arrival. Instantaneous replacement U=f(t)/r produces pre-light-cone curvature at all detectors; it is not a solution of the sourced wave equation. Advanced U=f(t+r)/r is a boundary-condition control (the sampled time window covers part of its pre-arrival pulse at r=2, not the advanced pulses at r=4,8). The retarded support is built into the Green function; this is a check of the construction and curvature observable, not independent discovery of the speed of gravity.

| Radius | Peak norm of metric trace reverse | Peak tidal norm/(4G) | Pre-arrival tidal norm/(4G) |
|---:|---:|---:|---:|
| 2 | 3.5959978e-5 | 131.547022 | 0 |
| 4 | 1.7979989e-5 | 67.004837 | 0 |
| 8 | 8.9899944e-6 | 33.659421 | 0 |

## 4. Exterior finite-difference audit

24 seeded exterior points strictly inside the pulse, at r in [2,7]. Four steps h=.04,.02,.01,.005 (96 point/step pairs). At each, independently approximate divergence, wave equation, tidal curvature under addition of an analytic pure-gauge perturbation, and omitted mixed time-space metric components. All residuals in this table divided by 4G. They are absolute diagnostic norms, not relative errors.

| h | Lorenz residual | Vacuum wave residual | Curvature gauge difference | Missing momentum control |
|---:|---:|---:|---:|---:|
| .04 | .1131701 | .7924034 | 1.91627e-4 | 20.41052 |
| .02 | .0284477 | .1986778 | 4.79135e-5 | 20.55390 |
| .01 | .00712166 | .0497055 | 1.19788e-5 | 20.58986 |
| .005 | .00178102 | .0124286 | 2.99473e-6 | 20.59885 |

All three valid finite-difference diagnostics converge approximately quadratically; the damaged control does not converge to zero. This is differentiation of an analytic retarded solution, not an independent time-domain PDE solver. No constraints at the distributional origin are evaluated numerically. The source identity was verified separately.

## 5. Evidence boundaries and next gate

PASS: on-shell scalar vertex Ward identity; tested longitudinal and pure-gauge decoupling; contracted tree numerator Lorentz invariance; conditional Newtonian matching; same-numerator COM decomposition; engineered classical source conservation; sampled exterior retarded support and gauge-invariant tidal convergence; controls detect trace omission, off-shell inputs, double counting, nonretarded boundary choices, and removal of source momentum components.

UNRESOLVED: stress-energy conservation during interacting quantum matter evolution (including gravitational contributions at higher order); loop Ward/Slavnov–Taylor identities; real-time causal quantum observables; radiation reaction; matching to a dynamical reduced Hamiltonian with all scalar/vector/tensor terms; nonlinear quantum constraint closure; emergence from EFMW. The action and Green function are conventional inputs, not new EFMW physics. All tests, thresholds, masses, boosts, source shape and numerical units are exploratory choices; no preregistration or independent replication.

QG-024 proposed: use a free quantized scalar field stress tensor (including momentum and pressure), construct a causal in-in response at leading perturbative order, and compare a retarded commutator observable with a spacelike vacuum correlation. A nonzero correlation is not a signal. Check on-shell Ward identities and boundary/regulator effects before adding self-interaction or claiming backreaction.

## 6. Replay

Python 3.13.5, NumPy 2.3.5. Run `python run.py > replay.log` (writes results.json, asserts all 18 checks). Run `python verify.py` before modifying artifacts; `results.json` records all samples. `index.html` is an offline viewer of the recorded data, not a new time evolution solver. `MANIFEST.sha256` covers the other files. No external libraries required for the viewer.

## References (established theory)

- B. S. DeWitt, Quantum Theory of Gravity. III. Applications of the Covariant Theory, Phys. Rev. 162, 1239 (1967), https://doi.org/10.1103/PhysRev.162.1239 .
- N. T. Bishop and L. Rezzolla, Extraction of gravitational waves in numerical relativity, Living Rev. Relativ. 19, 2 (2016), https://doi.org/10.1007/s41114-016-0001-9 .
- Prior QG-022 reduced model: https://github.com/enuminous/Quantum-Gravity/tree/824ad0779b18323b40a91ad9f9054c77b0a1b111/QG-022 .

## Published laboratory

All eight files were verified against their original local Git blob hashes: https://github.com/enuminous/Quantum-Gravity/tree/6dd5068f7b13aee55706a1e327134f63d638251c/QG-023 .
