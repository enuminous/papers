# QG-024 — Quantum gravitational causality

26 November 2026 · Monolithic LLC · EFMW exploratory research. Not peer reviewed.

**PASS — bounded reconstruction of free linearized curvature microcausality.** Not interacting quantum Einstein gravity, not emergent EFMW gravity, and not an experimental measurement. The gravitational Hamiltonian is the conventional free massless spin-2 reference. No new physical constant or EFMW-specific prediction is introduced.

## Model and exact causal identity

Use a canonically normalized free TT tensor h on a periodic flat cube of side L=16, c=hbar=1. Each nonzero Fourier wavevector has two orthonormal TT polarizations. Overall metric coupling is absorbed in normalization. The local electric curvature is E_ij=R^(1)_(0i0j)=-1/2 ∂_t² h^TT_ij in vacuum. With P_ij=δ_ij-k_i k_j/k², the polarization projector is Λ_ij,kl=(P_ik P_jl+P_il P_jk-P_ij P_kl)/2. In particular k⁴Λ_xx,xx=(k²-k_x²)²/2. The E_xx commutator is therefore the local spatial differential operator (∂_y²+∂_z²)²/8 applied to the massless scalar Pauli–Jordan commutator. The latter has light-cone support; derivatives do not enlarge support. This proves free continuum microcausality for this component, also on the periodic box before a wrapping signal can arrive. The homogeneous TT mode is omitted; its time-independent/linear free motion has zero electric curvature. No nonlinear gauge-invariant dressing is attempted.

Smear E_xx with four convolutions of a normalized uniform ball of radius a/4, a=1. The resulting profile has support in the radius-a ball; Fourier transform F(k)=[3 j_1(ka/4)/(ka/4)]⁴. The two centers are separated along z by D=2.5,3,4. Spacelike support separation holds for |t|<D-2a; direct massless response is supported within D±2a. Periodic images are outside all observed causal windows (nearest image distance ≥12). Spatially nonlocal bare TT h_xx is a deliberate comparator; applying its TT projection involves inverse Laplacians, so assigning it a local operational interpretation is invalid. Its commutator need not have local support. This does not imply that physical gravity signals superluminally.

For the vacuum, weights w_k=Λ_xx,xx F² k³/(4 L³), normalized variance V=Σ w_k/2. Define A=E(f)/sqrt(V), B(t)=E(g,t)/sqrt(V), [A,B]=i C(t). Then C=Σ w_k cos(k_z D) sin(kt)/V and symmetrized covariance S=Σ w_k cos(k_z D)cos(kt)/(2V). The bare TT comparator uses weights Λ F²/(k L³) with its own variance normalization. Both Fourier sums include ±k, with no extra polarization factor. C is state-independent for this free theory; S is a vacuum statistic.

Operational model: sender applies exp(∓i α A) (binary choice); receiver starts a qubit in |+> and applies a controlled exp(i β B). Baker–Campbell–Hausdorff shifts B by ±α C, and the vacuum characteristic function is exp(-β²/2). The trace distance between receiver states is exp(-β²/2)|sin(αβ C)|. α=β=0.5; instantaneous spatially compact ideal operations, not a realistic conserved laboratory apparatus. Covariance alone does not demonstrate harvested entanglement or a quantum-specific witness. No claim is made about gauge-dressed matter observables, interacting gravity, or signaling in the instantaneous reduced Newtonian model QG-021.

## Numerical experiment

Five spherical momentum cutoffs |n|≤16,32,48,64,96; box length fixed. Three distances, 281 times each (0 to 7 in steps of .025), two observables. 8,430 sampled observable/time combinations. Largest sum has 3,705,092 nonzero wavevectors; no full many-oscillator state vector is constructed. Shell grouping is exact for the specified frequencies. The spacelike audit uses t≤D-2a-0.1, and the late-time audit uses t≥D+2a+0.1. The direct-response interval is D±2a. All thresholds are exploratory and coded explicitly; no sealed/preregistered protocol.

| cutoff | nonzero k vectors | maximum abs spacelike curvature commutator |
|---:|---:|---:|
| 16 | 17076 | 0.053494687399229454 |
| 32 | 137064 | 0.00013408342696067987 |
| 48 | 462780 | 2.10620675213639e-9 |
| 64 | 1097916 | 4.201012659884408e-8 |
| 96 | 3705092 | 3.594044145240604e-10 |

Refinement is not monotone: the smearing Fourier transform oscillates. No exact finite-regulator microcausality is asserted. The reduction from coarse to finest is about 1.49e8. Finest max spacelike qubit trace distance 7.929332064817831e-11. Max postpulse commutator 1.1380537604322463e-10.

| D | normalized equal-time curvature covariance | max spacelike curvature signal | peak direct curvature signal | max spacelike bare-TT signal |
|---:|---:|---:|---:|---:|
| 2.5 | 9.008893005164033e-5 | 7.929332064817831e-11 | .025506569341985093 | .0021489273540781927 |
| 3 | 2.8568122485283158e-5 | 5.607365308721339e-11 | .02137147911061086 | .003179928903260739 |
| 4 | 4.845098092011989e-6 | 5.1787506988453604e-11 | .01612443163633794 | .003647242957416392 |

Independent infinite-volume radial quadrature: integrate w(k)=k⁵ F²/(16π²) times angular factor (8/15)j0(kD)-(8/21)j2(kD)+(3/35)j4(kD); for variance use angular factor 8/15. Simpson integration k=0..160, step .005. This follows from the azimuthal average 3/8+u²/4+3u⁴/8 of (1-k_x²/k²)². At nine sampled times per distance, max normalized commutator difference vs finest periodic sum 1.7737228075187517e-9; independent spacelike commutator max 4.837584846864947e-17. The comparison is for commutators; vacuum covariance is sensitive to periodic images. This is an independently formulated numerical check within the same research process, not external replication.

128 random TT projector tests confirm rank two, trace and transverse identities, idempotence and the polynomial relation. All 12 programmed checks passed. The first launch reached serialization and failed because a NumPy integer was passed to JSON. The original source and reproduced traceback are retained; converting the rank to Python int fixed serialization without modifying the physics or numerical thresholds.

## Verdict and next gate

PASS: local curvature commutator, explicit sender/readout no-signaling test in continuum limit, direct causal response, nonzero spacelike covariance, nonlocal comparator detected, and independent integral check. UNRESOLVED: entanglement harvesting in this specific lab, dynamical conserved quantum matter coupling, interacting quantum Ward identities, nonlinear constraints, microscopic EFMW emergence and empirical discrimination. The next gate should test a covariant second-order interaction, e.g. gravitational Compton scattering or soft-graviton Ward identities including all required diagrams and contact terms, with mechanism-removal controls. This is a more useful test than simply increasing the oscillator count.

## Replay

`OPENBLAS_NUM_THREADS=1 python run.py` writes results.json and prints diagnostics. `index.html` is an offline viewer of recorded data; it does not rerun the field solver. `sha256sum -c MANIFEST.sha256` checks original package bytes. Python 3.13, NumPy 2.3.5, SciPy 1.17.0. No independent scientific replication.

## References

- QG-023, covariant scalar exchange and classical retarded field: https://github.com/enuminous/Quantum-Gravity/tree/6dd5068f7b13aee55706a1e327134f63d638251c/QG-023
- Perche, Ragula & Martín-Martínez, Harvesting entanglement from the gravitational vacuum, Phys. Rev. D 108, 085025 (2023), https://doi.org/10.1103/PhysRevD.108.085025 . This lab tests commutators/covariances, not their harvesting protocol.

## Published laboratory

All ten files were verified against their original local Git blob hashes: https://github.com/enuminous/Quantum-Gravity/tree/ebe3638fed3ccad7d3f931e1dc8df6565f0c3916/QG-024 .
