# QG-014 — Local rank-2 gauge symmetry and its relativistic obstruction

26 November 2026 · Monolithic LLC · EFMW exploratory research. Not peer reviewed.

## Scope and conclusion

Three local linear rank-2 tensor Hamiltonians and a relativistic projected control were tested. Two local constructions possess exactly two TT physical modes at nonzero momentum, but have quadratic or cubic frequency dispersion. A separate finite Z3 charge model demonstrates exact constraint-preserving interactions and approximate gap protection, including virtual spectral corrections. Neither construction derives gauge symmetry from unconstrained EFMW quantum connectivity, nor is the finite Z3 system a discretization of the three-dimensional Cotton Hamiltonian. No nonlinear quantum gravity, Einstein correspondence, continuum phase, or physical claim is established.

## A. Local tensor laboratory

Use symmetric A and conjugate E in a Frobenius-orthonormal six-component basis. Vector charge G_j=∂_i E_ij generates A→A+sym(∂ξ). Add the trace constraint tr E=0 to generate A→A+φI. At nonzero wave vector q the vector constraint has rank 3; adding trace gives rank 4, leaving three and two canonical physical pairs respectively. The gauge algebra is Abelian in this linear model. Set the kinetic term to E:E/2. On the periodic cubic lattice use commuting centered differences, q_i=sin(k_i) (lattice spacing one).

Let X(q) be the cross-product matrix, B(A)=X A X^T (double curl up to sign), R(A)=(|q|²A−q⊗Aq−Aq⊗q+qq^T tr A)/2, S=R−I tr R/4, C(A)=XS−SX (a normalized linearized Cotton symbol; Fourier i omitted because the squared norm is unchanged). B annihilates vector gauge directions; C annihilates vector and trace gauge directions. Vector model H_B=1/2(E:E+B:B), giving three modes of frequency |q|². Cotton H_C=1/2(E:E+C:C), giving two modes of frequency |q|³. The quartic comparison uses H_4=1/2(E:E+B:B−(tr B)²/2). In the transverse plane the latter potential is the squared norm of the traceless part of B, so its integrated quadratic energy is nonnegative and invariant under both gauges, even though B itself is not trace-gauge invariant. Its stiffness is local, fourth-order, with two frequencies |q|². It need not define a compact microscopic magnetic operator or a stable quantum phase. The projected comparison H_TT uses K=|q|² P_TT, nonlocal as an operator on unconstrained A; it supplies two frequencies |q| by construction. P_TT is used to diagnose these models, not in B or C or the quartic Hamiltonian.

### Bounded obstruction for a second-order stiffness

In the parity-even rotationally invariant homogeneous second-order symmetric stiffness ansatz, K=a|q|² I+b D^T D+c(st^T+ts^T)+d|q|²tt^T, where D A=Aq, s=vec(qq^T), t=vec(I). Gauge invariance requires K D^T=0 and Kt=0. At unit q along z, the xz shear gives a+b/2=0. Applying K to s gives a+b+c=0 and c+d=0; applying K to t gives b+3c=0 and a+c+3d=0. Substitution gives a=b=c=d=0. This is an exact obstruction in this ansatz with the stipulated gauge action and ordinary kinetic term, not a general no-go theorem for local relativistic spin-2 physics. In particular linearized GR uses a scalar curvature constraint on A, not the trace constraint on E, and a different canonical Hamiltonian (QG-010).

72 momentum configurations (12 directions × 6 magnitudes) give fitted exponents 2,3,2,1 respectively. Maximum gauge residuals: vector 3.73e-18, Cotton 1.39e-17, quartic 1.39e-17. TT rotation residual 1.30e-16. Degree-two coefficient system has rank 4, smallest singular value .703975. Adding mass stiffness .1I violates gauge invariance (tested T K T^T residual .3). A symmetry-preserving quartic addition to Cotton changes the infrared exponent from 3 to 2, not 1: ω²=q^6+.1q^4. This is an analytical comparison, not a renormalization-group flow. Actual periodic stencil tests on 5³,7³,9³,8³ show Cotton gauge residual ≤1.33e-15 and integrated quartic relative error ≤5.17e-16. Even 8³ has eight derivative-zero momentum symbols (doublers), odd grids one; zero momentum is not included in the polarization count. No claim of regulator-independent continuum physics.

## B. Finite quantum charge laboratory

Independent finite example, three periodic sites and six Z3 electric components/site (xx,yy,zz,xy,xz,yz). Constraints are forward differences of E_zj and on-site trace modulo 3. The 12×18 constraint matrix has rank 9 over F3, giving 3^9=19,683 allowed electric basis configurations out of 3^18; all 19,683 enumerated and checked. The three global fluxes are fixed to zero for quantum evolution, leaving six qutrits (dimension 729). Six local shift generators preserve all charges exactly: xx+1,yy−1 or xy+1 on each site. Nearest-neighbor products preserve them too. Diagonal physical electric cost is .4 times the count of nonzero components; shifts have coefficients −.23, nearest-neighbor paired xx shifts −.12, both with Hermitian conjugates. Adding the paired shifts changes the ground energy from −1.1959673424 to −1.6095546972 without violating the constraints.

For a breaking control extend the system with a trace-charge qutrit on site zero, holding xx and xy fixed (so yy changes). Dimension 2187. The diagonal and invariant H1 are identical in the three blocks by explicit design, not derived from an unconstrained microscopic energy. H=I⊗H1+ΔQ+ε(Z+Z†)⊗F, where Q projects onto nonzero trace charge, Z is the cyclic shift, ε=.18, F is diagonal with entries 1.5 for xy(0)=0 and 1 otherwise. Initial state is ground state of H1 in physical block. At second order in inverse gap, H_eff=H1−2ε²F²/Δ. Compare six lowest eigenvalues of full and effective Hamiltonians at positive gaps; at Δ=0 the low-energy block is not isolated and the correction is undefined.

| Δ | Max sampled leakage (probability) | Bare max spectral error | Corrected max spectral error |
|---:|---:|---:|---:|
| 0 | .8581948113 | — | — |
| 4 | .0246643573 | .0270034630 | .0020230704 |
| 16 | .0017360697 | .0071057364 | .0001243970 |
| 64 | .0001108758 | .0017981400 | .00000772489 |

Exactly invariant interaction: [P,H]=0, zero sampled leakage. Breaking term: max absolute matrix entry of [P,V]=.27, independent of Δ. All five trajectories have 101 samples over t=0..20. Max norm and energy residuals among breaking trajectories 9.61e-12 and 1.55e-11. Only static perturbations tested here; no arbitrary-noise or indefinitely stable dynamics claim. Low-energy spectral improvement does not establish state fidelity or exact gauge protection. The initial exploratory eigensolver start was all ones; final run uses a deterministic nonsymmetric start and larger Krylov subspace to better resolve degeneracies. At Δ=0 low-energy multiplicities were sensitive to the starting vector; the final values are recorded and no spectral matching claim is made there.

## Verification and evidence boundaries

All final scripted assertions pass. Tolerance 1e-10 for linear diagnostics, 1e-9 for quantum norm; check rank, exact finite charge enumeration, exact invariant leakage, positive breaking commutator, decreasing large-gap leakage and improved corrected high-gap spectrum. These are exploratory thresholds, not preregistered. Seed 1414, eigensolver start seed 34; Python 3.13, NumPy 2.3.5, SciPy 1.17.0. The source, complete numerical result arrays and log are included locally. No independent replication has been performed.

- PASS (constructed): local linear gauge invariance, two TT polarizations, finite quantum charge preservation, bounded virtual correction.
- FAIL (specified models): three-mode vector model as exclusive spin-2; relativistic dispersion of the local two-mode Hamiltonians; nonzero second-order stiffness in the specified ansatz; exact protection by finite gap under breaking perturbation.
- UNRESOLVED: emergence from QG-006/QG-012 links, compact 3D continuum phase, Lorentz symmetry, nonlinear quantum algebra and conserved universal matter coupling.

## Next gate: QG-015

Test a microscopic constraint mechanism whose scalar generator acts on the canonical coordinate sector as in linearized GR instead of using the trace-electric constraint. Require local Hamiltonian, positive physical sector, constraint closure, and z=1 without projecting by hand; distinguish an imposed GR reference from emergence. Carry over compactness, zero modes, lattice artifacts, and symmetry-breaking controls.

## References (established comparison theories)

- Xu and Hořava, *Emergent gravity at a Lifshitz point from a Bose liquid on the lattice*, Phys. Rev. D 81, 104033 (2010), https://arxiv.org/abs/1003.0009 ; https://doi.org/10.1103/PhysRevD.81.104033 .
- Prem, Vijay, Chou, Pretko and Nandkishore, *Pinch Point Singularities of Tensor Spin Liquids*, Phys. Rev. B 98, 165140 (2018), https://arxiv.org/abs/1806.04148 ; https://doi.org/10.1103/PhysRevB.98.165140 .

## Replay

`OPENBLAS_NUM_THREADS=1 python run.py` (Python + NumPy + SciPy). Writes `results.json` alongside the source. `index.html` is an offline interactive companion. No external libraries needed in the browser.

## Published research artifacts

- Exact source and evidence: https://github.com/enuminous/Quantum-Gravity/tree/441dc48e58bfeb03e360366999ecc6a23f0dc128/QG-014
- Interactive lab source: https://github.com/enuminous/Quantum-Gravity/blob/441dc48e58bfeb03e360366999ecc6a23f0dc128/QG-014/index.html

All seven lab files were checked against the local Git blob hashes before the commit. Independent scientific reproduction remains outstanding.
