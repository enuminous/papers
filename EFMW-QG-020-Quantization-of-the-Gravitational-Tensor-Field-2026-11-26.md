# QG-020 — Quantization of the gravitational tensor field

26 November 2026 · Monolithic LLC · EFMW exploratory research · Not peer reviewed.

**PASS_BOUNDED_QUANTIZED_LINEAR_TENSOR_REFERENCE.** A canonical quantization of the two physical modes of the QG-015 staggered linearized ADM lattice, coupled to prescribed, static, commuting quantum stress probes. The full nonlinear gravitational field, scalar/longitudinal sourced constraints, relativistic dynamical matter, UV limit, and microscopic emergence from EFMW remain unresolved. This is conventional free linearized gravity with a restricted interaction, not a quantization of QG-018's nonlinear geometry.

## 1. Construction

Units hbar=c=lattice spacing=1. Use the exact QG-015 local operators, included as `qg015_reference.py` (published at https://github.com/enuminous/Quantum-Gravity/blob/e2490da554158f4b8a18aa90f4e7786baaee87f1/QG-015/run.py). Odd periodic lattice sizes L=3,5,7,9 avoid self-conjugate Nyquist momenta; omit homogeneous k=0, which is not a pair of propagating waves. With staggered phases, q_i=2 sin(k_i/2), s=q.q. D is divergence symbol, t is trace vector, K is the QG-015 stiffness, and W is an orthonormal basis for ker(D) intersect ker(t). The canonical constraint rank is four, W has two columns, and W^T K W=s I. For each conjugate momentum pair use real cosine and sine functions (including face-center offsets); this yields 2(L^3-1) real physical oscillator modes, not twice that number. Q_m and P_m are canonically quantized on the reduced Hilbert space, [Q_m,P_n]=i delta_mn. The field operator is sum_m u_m(x) Q_m, with P_m defined analogously. All physical modes satisfy the vacuum linearized constraints. The normal-ordered Hamiltonian is H_g=sum_m omega_m a_m^dag a_m, omega_m=sqrt(s). The TT projection enters reduction and mode extraction, not the parent local Hamiltonian. This procedure does not establish emergent gauge symmetry, nonlinear quantum constraint closure, or a local gauge-invariant quantum field observable algebra.

## 2. Conserved source profiles and interaction

Start with a localized diagonal seed T with entries (1,-1,0) at one vertex. Let K be the actual real-space local stiffness and L0=-lap. Define S=(K^2+L0 K)T/2 and normalize its Euclidean norm to one. For nonzero momentum, K=s(P T P-P tr(P T)) as an operator on symmetric tensors, P=I-qq^T/s. On the two TT directions K=s, on the transverse trace K=-s, and on the three spatial gauge directions K=0. Thus the polynomial is s^2 times the TT projector, realized by finite local differences. S has vanishing divergence, trace and mean; a bare seed has nonzero divergence. B is a translation of A by dx lattice steps in the first direction. Source operator S_hat=g (sigma_z^A S_A+sigma_z^B S_B). The probe operators commute with H; density and momentum perturbations are set to zero, so the linearized source continuity conditions are satisfied identically. This is an engineered stationary anisotropic stress perturbation, not a stress-energy tensor derived from a physically realizable positive-energy matter action. The model has no dynamical density sourcing, Newtonian attraction, recoil, or self-interaction of gravitons.

If c_Am=<u_m,S_A>, c_Bm=<u_m,S_B>, define f_sm=g(s_A c_Am+s_B c_Bm)/sqrt(2 omega_m), s_A,s_B=+/-1. Joint H=H_g+sum_m [g_Am sigma_z^A+g_Bm sigma_z^B](a_m+a_m^dag), where g_Am=g c_Am/sqrt(2 omega_m). Because all source components are TT, coupling preserves the linearized constraints of the reduced model. Check reconstructed source, basis orthonormality and smeared canonical commutator via inner products independently in real space. The probes begin in |+x,+x>, and the field starts in a product thermal state at dimensionless T=0,.5,2.

## 3. Exact conditional oscillator evolution

For branch s, alpha_sm=f_sm (exp(-i omega_m t)-1)/omega_m. Reduced probe matrix is

rho_ss'(t)=1/4 exp[-sum_m (f_sm-f_s'm)^2 (1-cos omega_m t) coth(omega_m/(2T))/omega_m^2] exp[i sum_m (f_sm^2-f_s'm^2)(omega_m t-sin omega_m t)/omega_m^2].

Use coth=1 at zero temperature. An independently specified classical shared Gaussian random phase comparator reproduces the first (dephasing) factor: it is a mixture of local phase rotations and is separable. A mean-field source has zero average stress under the chosen symmetric preparation. Neither comparator includes an entangling direct probe interaction. The quantum response contains an additional coherent conditional phase. This does not exclude arbitrary classical/quantum hybrid models; an explicit direct quantum interaction can also generate that phase. The branch energy increment sum_m [omega_m |alpha_sm|^2+2 f_sm Re(alpha_sm)] vanishes. This checks displacement and interaction energy balance, not a nonlinear GR energy theorem. For nonzero T, the background thermal energy is a constant.

Primary sweep: L=3,5,7,9; dx in unique {0,1,floor(L/2)}; g=.2,.5,1; T=0,.5,2; t=0..40, 161 samples. 99 runs, 15,939 time points; 8 zero/one-probe controls. Full oscillator Fock spaces are treated by exact analytic factorization, not explicit diagonalization of a many-body Hilbert space. Independent sparse matrix evolution on the two actual L=5 modes with greatest joint source weight uses cutoffs 6,10,16 and 41 samples each (largest 1,024-dimensional full joint Hamiltonian). This verifies that two-mode subset, not the entire field by a second solver. Additional L=11, 2,660-mode Fourier-only tests at dx=4,5, g=.5,1,2, T=0, t=0..100 (401 samples each) examine source separation after the initial sweep. These are exploratory parameters, not preregistered. All 17 programmed final checks passed; disjoint control verifies zero overlap, not a universal absence-of-entanglement theorem.

## 4. Results and adverse findings

| L | modes | min omega | sites with nonzero source |
|---|---:|---:|---:|
|3|52|1.732051|22|
|5|248|1.175571|34|
|7|684|.867767|34|
|9|1456|.684040|34|

Maximum negativity is .49539684 (L=3, dx=0, g=.5, T=0); the maximum for distinct centers is .47580926 (L=3, dx=1, g=1, T=0). These sources overlap on 19 lattice-index cells, so this is not evidence of entanglement between disjoint sources. Negativity is bounded by .5 for two qubits. Classical stochastic negativity is <=1.30e-16, null/one-probe <=2.89e-16. For L=9, g=1, T=0: dx=0,.439524; dx=1,.430090; dx=4, no entanglement above numerical precision. At L=11, dx=5 (disjoint support), no detectable negativity over 401 samples for each of three couplings; maxima 1.42e-16. No claim of long-range gravitational entanglement is justified. The tested local source is derivative-weighted: its static cross coefficient sum_m c_Am c_Bm/omega_m^2 reduces to a local polynomial kernel (s^3 TT projector), and vanishes at the larger offsets in this experiment. This is a restricted-source limitation rather than a generic prediction of gravity. Neither the continuum limit at fixed physical volume nor microcausality has been tested.

| Diagnostic | Maximum error |
|---|---:|
| Source divergence |1.1103e-16|
| Source trace |3.4695e-18|
| Mode stiffness/transversality/trace |4.4409e-15|
| Basis orthonormality |8.1047e-15|
| Real-space curvature of sampled modes |7.9798e-16|
| Source reconstruction |7.4941e-16|
| Branch energy increment |2.7930e-16|
| Classical vs quantum coherence magnitude |8.3267e-17|
| Two-mode sparse density matrix at N=16 |1.3490e-13|
| Two-mode sparse norm at N=16 |2.9455e-13|

The direct finite-matrix calculation and exact Gaussian solution agree. These checks do not demonstrate experimental gravity, unique EFMW physics, or independent replication. Fixed spacing and growing boxes probe an infrared/finite-volume direction only; gravitational coupling normalization is exploratory. The main source profile is deliberately chosen to make local conservation exact. The missing sector is a dynamical, covariantly coupled quantum stress-energy source with nonzero density and momentum, including its gravitational constraints and reciprocal backreaction.

## 5. Replay

Install pinned NumPy and SciPy from requirements.txt. Run `OPENBLAS_NUM_THREADS=1 python run.py` in this directory; outputs results.json and prints verification data (redirect to log.txt if desired). The archived log includes a SciPy dtype FutureWarning; no assertion failed. `python verify.py` checks the archived SHA-256 file hashes before replay; JSON serialization and floating-point results can differ across environments. `index.html` is an offline viewer of the computed trajectories. No new run is performed by its controls. Independent review remains outstanding.

## Next gate

QG-021: a covariantly motivated quantum matter model with dynamical density, momentum and stress; compare constraint-consistent scalar/longitudinal sourcing and tensor radiation, reciprocal weak-field matter–geometry interaction, a direct-interaction comparator and nonoverlapping physical probes. Derive or clearly distinguish all imposed ingredients.

## Published laboratory

All nine files were verified against their original local Git blob hashes: https://github.com/enuminous/Quantum-Gravity/tree/580e520c1552949de6ab88c2af28bba9c4db4711/QG-020 .
