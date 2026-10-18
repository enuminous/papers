# EFMW-COSMO-C1Q 1.0.0 — cosmological freeze

Prepared for Matthew Chenoweth Wright, 16 October 2026 (Pacific).

**Status: specified classical hypothesis, with a numerical reference implementation. No observational fit or experimental validation is claimed.** The active physics is the known class of canonical quadratic quintessence. The contribution here is a versioned, executable specialization of the C1 action, with explicit matter, initial data, perturbation rules and verification. It is not a new law of nature.

## 1. Meaning and domain of the freeze

This is a closed post-nucleosynthesis cosmology on a spatially flat expanding FLRW background, starting at a_i=10^-8 and ending at a=1 in the supplied calculation. Linear inhomogeneities are evolved on that background. The initial stochastic spectrum is an input, not an inflation prediction. Nuclear abundances, baryon asymmetry and dark-matter abundance are inputs. Inflation, reheating, baryogenesis, quantum gravity, nonlinear galaxy formation and a fundamental explanation of dark matter are not furnished by this model. Continuing the background into the future is mathematically possible but is not part of the frozen reference integration.

“Closed” means that no free function remains to be chosen after reading the data. It does not mean that every physical scale or the universe's origin has been explained. Finite tolerances are part of numerical implementation, not changes to the action.

Parent: `enuminous/EFMW-Lagrangian` at commit `2e392b9fb5bbfa35667cd562787e23cadcc1623f`, C1 v1.0.0. Exact parent specification and convention file are preserved under `sources/`. The parent is not modified.

## 2. Fields, action, units and sources

Use signature (-,+,+,+), the parent's Riemann convention, c=hbar=1 and M^2=(8 pi G)^-1. Let phi be C1 scalar sector F. The sector label is a bookkeeping choice; it assigns no cognitive observable to phi.

The action is

S = integral sqrt(-g) [M^2 R/2 - (nabla phi)^2/2 - m^2 phi^2/2 - F_mu_nu F^mu_nu/4] d^4x + S_matter_without_EM_kinetic[g,A,psi].

M and m have mass dimension 1; phi has dimension 1; V has dimension 4; R has dimension 2. The kinetic sign is positive-energy in the stated metric convention.

The matter extension contains ordinary baryonic nuclei and electrons with electromagnetic coupling, photons, three decoupled neutrino species, and collisionless pressureless cold dark matter. A_mu is identified with ordinary electromagnetism and its kinetic term is counted once. The new scalar has no direct matter coupling. Standard homogeneous and linear kinetic/fluid equations, including photon scattering and recombination, define the cosmological effective description; a particle origin of cold dark matter is not specified. The continuum CDM limit is described by conserved particle number and geodesic motion. Its background density is proportional to a^-3. Baryon rest mass is likewise treated as pressureless in the background, with thermal pressure included in perturbations by CLASS.

Exact C1 choices: Lambda=0; all xi_a=0; all g_ij=0; all h_ijk=0; the other seven scalar sectors and the second gauge field are absent. Homogeneous electromagnetic field strength is zero; photons retain a thermal distribution. Matter currents come from the separately declared matter extension, not from the source-free catalogue audit. No arbitrary phi-gradient gauge current is imported. Restrict the action before variation. The separate sourced root equation involving E+cP is not identified with this massive cosmological phi equation.

The resulting covariant equations are

M^2 G_mu_nu = T_mu_nu(matter+EM) + nabla_mu phi nabla_nu phi - g_mu_nu[(nabla phi)^2/2 + m^2 phi^2/2],

Box_g phi - m^2 phi = 0,

nabla_mu T_total^(mu nu)=0,

together with the ordinary matter kinetic equations. Total matter+EM stress is conserved, although photon/baryon momentum exchange occurs. Scalar stress is conserved separately. There is no additional Friedmann rotation term and no preferred observer dynamics.

## 3. Background equations and exact closure

ds^2=-dt^2+a(t)^2 dx^2; H=a_dot/a; a_today=1; expanding root H>0.

3 M^2 H^2 = rho_b+rho_c+rho_gamma+rho_nu+phi_dot^2/2+m^2 phi^2/2.

-2 M^2 H_dot = rho_b+rho_c+4 rho_gamma/3+rho_nu+p_nu+phi_dot^2.

phi_ddot+3H phi_dot+m^2 phi=0.

rho_phi=(phi_dot^2+m^2 phi^2)/2; p_phi=(phi_dot^2-m^2 phi^2)/2; w_phi=p_phi/rho_phi.

rho_b,c=rho_b,c,0 a^-3; rho_gamma=rho_gamma,0 a^-4. Neutrinos are not approximated as dust through their relativistic transition. Each species has g=2 and f(q)=1/(exp(q)+1), zero chemical potential. Its density and pressure are

rho_nu_i = Tnu0^4/(pi^2 a^4) integral_0^infinity q^2 sqrt(q^2+(a m_i/Tnu0)^2) f(q) dq,

p_nu_i = Tnu0^4/(3 pi^2 a^4) integral_0^infinity q^4/sqrt(q^2+(a m_i/Tnu0)^2) f(q) dq.

Tnu0/Tgamma0=(4/11)^(1/3)(N_eff/3)^(1/4). This explicitly thermal effective prescription encodes N_eff=3.044; it is not the exact momentum-dependent neutrino-decoupling distortion. The same prescription is used in both codes.

For computation define N=ln(a), x=phi/M, y=phi_dot/(M H0), mu=m/H0, E=H/H0, and r_i=rho_i/(3M^2 H0^2). Then

E^2 = r_b+r_c+r_gamma+r_nu+(y^2+mu^2 x^2)/6,

dx/dN=y/E; dy/dN=-3y-mu^2 x/E.

These equations, the positive Friedmann root and the fixed initial conditions are a complete background initial-value system. Flatness at a=1 fixes x_i through a boundary-value shooting problem. A successful shot is a normalization condition, not a successful empirical test.

## 4. Frozen reference inputs

All values are chosen fiducial assumptions, not EFMW measurements or best fits.

| Input | Value or rule |
|---|---|
| H0 | 67.4 km s^-1 Mpc^-1 |
| Omega_b,0 | 0.049 |
| Omega_c,0 | 0.265, excluding neutrinos |
| Tgamma0 | 2.7255 K |
| Neff | 3.044 |
| Neutrino masses | 0, 0.0086, 0.050 eV |
| Scalar mass | m=H0 in natural units, mu=1 |
| Initial scale factor | 10^-8 |
| Initial scalar velocity | y_i=0 exactly |
| Initial scalar amplitude | positive shooting solution giving E(1)=1 |
| Geometry and cosmological constant | K=0, Lambda=0 |
| Scalar initial spectrum | Gaussian growing adiabatic mode |
| Curvature power | P_R(k)=2.1e-9 [k/(0.05 Mpc^-1)]^(0.965-1) |
| Running, primordial tensor power, independent isocurvature | zero |
| Helium mass fraction | Y_He=0.245, fixed rather than BBN-inferred |
| Recombination | pinned CLASS 3.4.1 HyRec2020 |
| Reionization | reio_camb: z_mid=7.7, exponent=1.5, width=0.5 |
| Second helium reionization | z_mid=3.5, width=0.5 |

The reionization optical depth is derived; it is not independently fixed as well as the midpoint. Vector modes and primordial tensor modes are zero. Primordial perturbations specify an ensemble, not a particular realization of the sky. No random realization or seed is needed to compute its ensemble power spectra.

The Python shooting rule scans [0] plus 37 logarithmically spaced x_i values from 10^-4 to 1000, solves each sign-changing bracket, and chooses the first positive root found. It reports all brackets. This is an operational branch rule, not a proof that there are no other roots. For the reference point one bracket is found. Absence of a root invalidates the point; it never authorizes adding Lambda or changing the potential.

## 5. Perturbations, thermal history and stability

The complete linear closure, scalar stress, metric constraints, initial-mode rule and CLASS mappings are in `PERTURBATIONS.md` and the pinned CLASS configurations. They include photon polarization, baryon drag, massless and massive neutrino hierarchies, neutrino anisotropic stress, and the actual scalar perturbation. No smooth-dark-energy replacement is used in the CLASS calculation.

For this minimally coupled canonical action, scalar and tensor principal kinetic terms have the healthy sign, scalar propagation speed is c_s^2=1, tensor propagation speed is c_T^2=1, and V''=m^2>0. The scalar potential is bounded below by zero. Thus rho_phi>=0 and -1<=w_phi<=1 whenever rho_phi>0. These are analytic properties of this action. They do not rule out ordinary gravitational Jeans growth, guarantee every numerical solution, or establish cosmic acceleration for every parameter choice. There is no direct scalar-mediated fifth force in the chosen matter frame. A claim of superluminal scalar propagation is not a prediction of this branch.

## 6. Observable definitions

D_H(z)=c/H(z); D_M(z)=c integral_0^z dz'/H(z'); D_L=(1+z)D_M; D_A=D_M/(1+z). Etherington reciprocity is assumed through standard photon propagation. Age since the initial surface is integral_a_i^1 da/(aH). Any quoted age since a=0 uses an explicitly labeled negligible radiation-era extrapolation outside the model domain.

q=-1-H_dot/H^2. The onset of acceleration is a root q(z)=0. A local CPL slope may be quoted as w_a,local=-dw/dln(a)|_0, but the solver integrates phi and does not replace it with a fitted CPL equation of state.

BAO observables are D_M/r_d and D_H/r_d with the drag sound horizon computed from the same thermal history, not borrowed from a LambdaCDM fit. CMB and linear matter spectra are ensemble predictions from the primordial spectrum. Matter power is linear only; high-k output does not license nonlinear inference. CLASS outputs spectra, lensing and transfer functions to the limits stated in the configuration. Sigma8 follows from the matter spectrum; it is not a second adjustable normalization in addition to A_s.

## 7. Falsifiability and comparison

Canonical positive-potential scalar dynamics cannot produce w_phi<-1. A robust inference of phantom behavior under a correct common likelihood would exclude this branch. The nonzero mass reference point predicts a specific H(z), distance relation, sound horizon, CMB and structure growth. Agreement with its own shooting target or with another implementation is not evidence that the universe follows it.

Comparison baseline: flat LambdaCDM with the same H0, baryons, CDM, neutrinos, photon temperature, primordial spectrum and thermal prescriptions; scalar absent; Lambda fills the remaining density budget. A conventional quadratic-quintessence calculation with identical inputs is the same physical model and must agree. It cannot count as an independent competing novel EFMW theory. The prior f(T) and nonlocal bounds do not constrain C1Q's mass without an explicit likelihood analysis of C1Q.

See `TEST_PROTOCOL.md` for numerical gates and the prospective observational protocol. No observational data or likelihood has been evaluated here. No new Lean theorem is claimed by this package.

## 8. Change control

`FREEZE.json` hashes physical specifications, configurations, source, verification and provenance files. `MANIFEST.sha256` also covers delivered numerical outputs. A changed potential, coupling, mass prior, source term, initial-mode rule, species content or empirical acceptance criterion requires a new model version and new predictions. Display-only edits can be separately versioned. Neither solver may silently repair a rejected point.
