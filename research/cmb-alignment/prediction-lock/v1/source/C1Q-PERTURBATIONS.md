# Full linear perturbation closure

This file defines the linear model; `config/class_c1q.ini` is its executed reference configuration. CLASS is pinned at commit 814ce59c380a5cccd0bed1747a384ff7bfc1f9cf (3.4.1). Standard kinetic, atomic and polarization modules at this revision are part of the operational specification. The transparent adapter changes only the scalar potential and its first two derivatives plus a necessary refresh of explicit scalar initial conditions after CLASS's shooting override.

## Conventions

Conformal Newtonian metric: ds^2=a^2[-(1+2 Psi)d eta^2+(1-2 Phi)dx^2]. A prime here is d/d eta, not d/d ln(a). Fourier waves are exp(i k.x); Laplacian=-k^2; theta=i k_j v^j. Hconformal=aH. Phi and Psi need not coincide because free-streaming neutrinos and photons carry anisotropic stress.

## Scalar and Einstein equations

Background: phi''+2 Hconformal phi'+a^2 m^2 phi=0.

Perturbation: delta_phi''+2 Hconformal delta_phi'+(k^2+a^2 m^2)delta_phi = phi'(Psi'+3 Phi')-2a^2 m^2 phi Psi.

delta_rho_phi = a^-2(phi' delta_phi' - phi'^2 Psi)+m^2 phi delta_phi.

delta_p_phi = a^-2(phi' delta_phi' - phi'^2 Psi)-m^2 phi delta_phi.

(rho_phi+p_phi) theta_phi = k^2 phi' delta_phi/a^2; sigma_phi=0. Evolve delta_phi directly at phi'=0; do not divide by rho_phi+p_phi to create a spurious singularity.

k^2 Phi+3 Hconformal(Phi'+Hconformal Psi)=-a^2 delta_rho_total/(2 M^2).

k^2(Phi'+Hconformal Psi)=a^2 sum_i[(rho_i+p_i)theta_i]/(2 M^2).

k^2(Phi-Psi)=3a^2 sum_i[(rho_i+p_i)sigma_i]/(2 M^2).

The trace spatial Einstein equation plus these constraints, or the equivalent constraint-preserving first-order system in CLASS, completes metric evolution. Bianchi conservation supplies the redundancy; constraints are not extra fit freedoms.

## Standard matter and radiation

The executed reference uses synchronous gauge with the CDM rest frame fixing its residual freedom. Its scalar equation is delta_phi''+2 Hconformal delta_phi'+(k^2+a^2 m^2)delta_phi=-phi' h'/2, where h is the synchronous spatial metric trace. This is the equation implemented by the pinned CLASS scalar module. The Newtonian equations above specify the equivalent covariant physics; do not run this adapter with CLASS's Newtonian option. Inspection and a diagnostic run found missing lapse-source terms in that option for the pinned revision, as recorded in AUDIT.md.

CDM: delta_c'=-theta_c+3Phi'; theta_c'=-Hconformal theta_c+k^2 Psi.

Baryons: delta_b'=-theta_b+3Phi'; theta_b'=-Hconformal theta_b+c_b^2 k^2 delta_b+k^2 Psi+(4rho_gamma/3rho_b) a n_e sigma_T(theta_gamma-theta_b). CLASS's thermal evolution supplies c_b and n_e.

Photons: delta_gamma'=-4theta_gamma/3+4Phi'; theta_gamma'=k^2(delta_gamma/4-sigma_gamma)+k^2Psi+a n_e sigma_T(theta_b-theta_gamma), with the intensity and linear-polarization multipole hierarchy and Thomson collision operator of the pinned `source/perturbations.c`. Do not truncate radiation to a perfect fluid outside the tight-coupling regime. HyRec2020 and the pinned reio_camb prescription supply the background opacity.

Collisionless neutrinos use f=f0(q)[1+Psi_nu(k,q,mu,eta)]. Write Psi_nu=sum_l (-i)^l(2l+1) F_l P_l(mu), epsilon=sqrt(q^2+a^2 m_nu^2), with q in matching momentum units. The hierarchy is

F_0'=-(qk/epsilon)F_1-Phi' dln(f0)/dln(q),

F_1'=(qk/3epsilon)(F_0-2F_2)-(epsilon k/3q)Psi dln(f0)/dln(q),

F_l'=[qk/(epsilon(2l+1))][l F_(l-1)-(l+1)F_(l+1)], l>=2.

Stress moments are the corresponding q integrals of energy, momentum and quadrupole. The massless limit is included, and the massive species are momentum resolved. This is the standard Ma-Bertschinger hierarchy; numerical closures, tight-coupling and streaming approximations are frozen by the CLASS commit and run settings and must pass precision convergence for their intended observable.

## Initial mode and ensemble

Use the regular growing adiabatic radiation-era mode, normalized to a Gaussian dimensionless curvature spectrum P_R(k)=A_s(k/k_p)^(n_s-1). Baryon/CDM/neutrino entropy modes and the decaying mode are zero. Neutrino shear is retained in the initial metric solution. No independent scalar-field isocurvature amplitude is introduced. The pinned CLASS implementation initializes delta_phi=delta_phi'=0 in synchronous gauge at its per-mode starting time. These are not simultaneous zero conditions in both gauges. Gravitational forcing generates subsequent scalar perturbations. The homogeneous initial surface is a=1e-8; perturbation start times are selected internally by the pinned implementation from the superhorizon and interaction-rate criteria. This finite-time approximation must be checked before precision inference; it does not derive the primordial spectrum. The reference and precision runs use synchronous gauge. An independent correct Newtonian implementation remains a future cross-check; the rejected diagnostic is preserved.

Primordial vectors and tensors are zero. For an optional tensor response test, the covariant model has h''+2Hconformal h'+k^2 h=2a^2 pi_T/M^2, with ordinary radiation anisotropic stress. Turning on primordial tensor amplitude changes the frozen ensemble and requires a new version.

## CLASS normalization and adapter

CLASS uses x=phi/M and potential V_class=V_physical/M^2 with dimensions Mpc^-2. In code H0 has units Mpc^-1 (physical H0 divided by c). Therefore

V_class(x)=0.5 (mu H0)^2 x^2; dV/dx=(mu H0)^2 x; d2V/dx2=(mu H0)^2.

The six `scf_parameters` are interpreted by this adapter as [mu,0,0,0,x_initial,x_initial_prime]. The middle three are unused zeros. `attractor_ic_scf=no`, `scf_tuning_index=4` and `Omega_scf=-1` make CLASS shoot the initial amplitude to fill the flatness budget, while Lambda and fluid dark energy are both zero. The adapter refreshes `phi_ini_scf` after this override; otherwise the upstream input order leaves the copied initial value unchanged while the shooting parameter changes.

One massless neutrino uses N_ur=N_eff/3; two massive species use m_ncdm=0.0086,0.050 eV, unit degeneracies and the same fixed Tnu/Tgamma as the Python solver. No duplicated massless density or separately imposed massive-neutrino Omega is used.

Recombination uses HyRec2020, YHe fixed, no exotic energy injection, no varying constants, no interacting dark matter, and no nonlinear matter correction. Reionization is prescribed phenomenologically; star formation is not simulated.

## Evidence and limitations

Executed background, CMB, matter, lensing and transfer outputs are recorded under results. A successful CLASS run is numerical execution of this candidate, not an observational likelihood test. Code cross-checks validate implementation conditional on the same assumptions. The reference overrides five default precision settings and has a further tightened run; measured differences are in class_comparison.json. This is not a universal error certificate for arbitrary likelihoods. The empirical protocol requires targeted convergence and external review before inference. Parent C1 Lean certificates do not certify this adapter or the Boltzmann solution.

Primary references: Ma & Bertschinger, Astrophys. J. 455 (1995) 7, https://arxiv.org/abs/astro-ph/9506072 ; Blas, Lesgourgues & Tram, JCAP 07 (2011) 034, https://arxiv.org/abs/1104.2933 ; pinned CLASS source https://github.com/lesgourg/class_public/tree/814ce59c380a5cccd0bed1747a384ff7bfc1f9cf .
