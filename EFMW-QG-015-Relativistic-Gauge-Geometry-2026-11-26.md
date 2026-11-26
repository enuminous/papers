# QG-015 — Relativistic gauge geometry on a staggered lattice

26 November 2026 · Monolithic LLC · EFMW exploratory research · Not peer reviewed.

**Verdict: PASS for a constructed free linearized gravitational reference; microscopic emergence remains UNRESOLVED.** QG-014's vector-plus-trace-electric constraints obstructed a nontrivial local two-derivative stiffness in its tested ansatz. Here the trace-electric constraint is replaced by the linear scalar curvature constraint. The result is local, exactly linearly constrained, has two physical canonical pairs at every nonzero lattice momentum, and approaches relativistic dispersion in the infrared. These are properties of deliberately discretized linearized ADM gravity, not a new derivation of gravity, Lorentz covariance at finite lattice spacing, or a connection to the quantum graph Hamiltonian of QG-006.

## Specification

Periodic cubic lattice, spacing 1, dimensionless canonical units, six orthonormal symmetric tensor components (diagonal components and sqrt(2) times each off-diagonal component). Diagonal components live at vertices; off-diagonal ij components live at ij face centers; vector i components live at i-edge centers. A forward difference maps vertex to edge or edge to face, and a backward difference maps in reverse. All differences commute on compatible staggered locations. For a Fourier mode after removal of the location phases, q_i = 2 sin(k_i/2), s=q·q. D maps a symmetric tensor to its contraction with q, and t=(1,1,1,0,0,0) is the trace vector.

In real Fourier canonical coordinates define c=q^T D-s t^T, C=(c h,D pi). Define P=I-tt^T/2 and

K=s I-2 D^T D+D^T q t^T+t q^T D-s tt^T.

H=(pi^T P pi+h^T K h)/2. The kinetic and potential terms are the rescaled quadratic ADM reference. Let J be the canonical symplectic matrix. The identity c D^T=0 gives C J C^T=0. D K=0 and c P=q^T D give dot(C0)=q^T C_vec, dot(C_vec)=0. For q≠0, rank C=4; the 12-dimensional phase space reduces by eight dimensions after quotienting the four gauge directions, giving two canonical pairs. The gauge-invariant TT subspace W=ker(D,t^T) is used only to diagnose the quotient, never to construct K. On W, P=I and K=s I. Thus the reduced Hamiltonian is two positive oscillators, omega=sqrt(s). The unreduced kinetic form is indefinite; it is not a positive unconstrained microscopic oscillator Hamiltonian. At q=0 the four constraints vanish and homogeneous modes require separate treatment; no claim of two modes at zero momentum.

In real space let D_r be staggered divergence, D_r* its adjoint, grad/div the vertex-to-edge gradient/edge-to-vertex divergence and Delta the nearest-neighbor Laplacian. The curvature is C_R=div D_r h-Delta tr(h). With trace lift t, the local Hessian is K_r=-Delta I-2 D_r* D_r+D_r* grad tr+t(-div D_r+Delta tr). The trace and derivative terms are necessary. The identities C_R D_r*=0, D_r K_r=0, C_R P=div D_r follow from commuting differences. Each term uses at most two differences. This is a local real-space operator, not a Fourier TT projector. The curvature convention differs by sign from the real Fourier c; the zero constraint surface is identical. Lapse/shift multipliers may generate gauge shifts; the tested time evolution fixes them to zero. The background and constraint algebra are imposed.

## Execution protocol

`OPENBLAS_NUM_THREADS=1 python run.py` writes `results.json`; see `log.txt` for output. Seed 15026; Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. Exploratory fixed tolerance 2e-10; not preregistered. 64 independently sampled nonzero Fourier momenta; 17 times per mode comparing pairs of gauge-equivalent states by matrix exponentiation. 20 random off-shell real-space tests (L=4,6,8,12,16; 4 per size). Five full Brillouin-zone spectral grids (8,16,32,64,128); these are spectral evaluations, not full dynamical simulations. Three direct local leapfrog experiments on 8³ sites, each with two gauge-equivalent initial states, dt=.1,.05,.025, final time 8. Three static zero-mean source tests. All programmed assertions passed. The local wave evolution is classical canonical; canonical quantization of the physical sector gives two oscillator modes at nonzero momentum, but no independent quantum evolution or interacting quantum algebra was tested here.

## Results

| Diagnostic | Maximum absolute residual (unless indicated) |
|---|---:|
| First-class Poisson brackets | 5.450913075833194e-15 |
| Fourier constraint closure | 4.953780304294372e-15 |
| Reduced Hamiltonian | 5.397567705555396e-15 |
| Gauge-equivalent physical amplitude | 2.486899575160351e-14 |
| Evolved constraints | 4.405364961712622e-13 |
| Conserved energy (matrix exponential) | 6.920686246303376e-12 |
| Real-space curvature gauge identity | 2.131628207280301e-14 |
| Real-space momentum closure | 1.776356839400251e-14 |
| Real-space scalar closure | 8.881784197001252e-15 |
| Adjoint test (normalized) | 3.369614140010616e-17 |
| Hessian symmetry (normalized) | 1.553434251851019e-16 |
| Independent Fourier vs stencil symbol (relative) | 1.755834969448497e-15 |

Three ablations, minimum spectral operator-norm constraint leakage across 64 momenta: replace P with identity .3440401551; replace K with s I .1199889369; remove both mixed divergence/trace terms .2399778738. All fail; not merely selected examples. Arbitrary real-space fields also expose broken kinetic and potential identities. Numerical values depend on the chosen normalization and momenta.

| Grid L | Max relative dispersion error over four fixed integer directions (%) | Centered zeros | Staggered zeros |
|---:|---:|---:|---:|
| 8 | 8.436699 | 8 | 1 |
| 16 | 2.165654 | 8 | 1 |
| 32 | .544978 | 8 | 1 |
| 64 | .136468 | 8 | 1 |
| 128 | .034131 | 8 | 1 |

Centered q_i=sin(k_i) produces seven extra zero points for even L; staggered q_i=2 sin(k_i/2) has only the genuine homogeneous zero. The tested modes use integer directions (1,0,0),(1,1,0),(1,1,1),(2,1,0). Larger L approaches the infrared at fixed lattice spacing; equivalently one may restore spacing a and hold physical wavelength fixed. Exact Lorentz invariance at finite lattice spacing is absent.

| dt | Steps per trajectory | Max physical wave amplitude error | Max relative energy error |
|---:|---:|---:|---:|
| .1 | 80 | .007207060815 | .004391432201 |
| .05 | 160 | .001796949613 | .001098316895 |
| .025 | 320 | .000448936539 | .000274587180 |

Halving dt reduces the error by approximately 4 (second-order time integration). Max local constraint residual 1.387778780781446e-15; max normalized TT amplitude difference between gauge-equivalent wave trajectories 4.575363707941798e-16. The integrator is symplectic and not exactly energy conserving at finite dt. The gauge amplitudes are randomized; the tested physical plane wave has k=2 pi (1,1,1)/8.

Static scalar curvature test: h=-2 Phi I, C_R=4 Delta Phi. Solve Delta Phi=4 pi rho (G=1) for a zero-mean signed source on a periodic domain, rescaling to max|Phi|=.001. Max relative residual across 8³,16³,32³ is 5.140019928599737e-14. A unit nonzero mean source would leave unavoidable mean residual 16 pi because the integrated periodic Laplacian is zero. This is a linear time-symmetric constraint check, not full matter coupling, universal attraction, or a cosmological solution.

## Evidence-bounded verdict

- PASS: local staggered linear reference; four first-class constraints and two physical tensor pairs at nonzero momentum; relativistic infrared dispersion; no spurious finite-momentum zeros of the derivative symbol; controlled local propagation; static scalar constraint; failures under mechanism removal.
- FAIL: tested ablations as gravitational Hamiltonians; exact finite-spacing relativistic dispersion; direct identification of QG-014 trace-electric symmetry with this curvature constraint.
- UNRESOLVED: homogeneous and nonlinear modes, interacting quantum closure, physical Hilbert-space derivation from QG-006 graphs, background independence, universal matter coupling, regulator removal beyond free reference, independent empirical signature and replication.

## Next gate QG-016

Try a consistent weak-field matter coupling to these local constraints. Derive the sourced constraint propagation identities from a discrete continuity equation, test static and dynamical conserved sources and deliberate nonconservation, and compare with linearized Einstein response. Keep the graph-to-ADM derivation as a separate unresolved obligation. Nonlinear constraint closure cannot be inferred from this linear test.

## References

- QG-014: https://github.com/enuminous/Quantum-Gravity/tree/441dc48e58bfeb03e360366999ecc6a23f0dc128/QG-014
- Interim report: https://github.com/enuminous/papers/blob/main/EFMW-Quantum-Gravity-Interim-Report-QG-003-013-2026-11-26.md
- Linearized ADM reference: https://arxiv.org/abs/gr-qc/9908079 (linearized ADM equations and constraints).
- Canonical linearized gravity review notes: https://relativity.phys.lsu.edu/ilqgs/chen041426.pdf (normalization conventions differ).

`index.html` is an offline interactive companion, with analytical dispersion and stored measured diagnostics; it does not rerun the Python simulation. `MANIFEST.sha256` records the source, report, outputs, requirements and HTML. Independent replication remains outstanding.

## Published evidence

- Exact source and evidence: https://github.com/enuminous/Quantum-Gravity/tree/e2490da554158f4b8a18aa90f4e7786baaee87f1/QG-015
- Browser lab source: https://github.com/enuminous/Quantum-Gravity/blob/e2490da554158f4b8a18aa90f4e7786baaee87f1/QG-015/index.html

All seven lab files were checked against local Git blob hashes before commit. Independent reproduction remains outstanding.
