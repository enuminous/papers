# EFMW Quantum Gravity — Interim Research Report
## QST-001 through QG-013: from quantum connectivity to protected gravitational sectors

26 November 2026 · Monolithic LLC · Matthew Chenoweth Wright · AI-assisted research synthesis

**Status: exploratory interim report; not peer reviewed; not a derivation of quantum gravity.** This synthesis records the reported computational investigations and their adverse findings. QG-003–013 numerical values below are taken from the experiment reports in the research conversation; the original local artifacts have not been independently replayed or uploaded with this paper. The established GR and quantum models used as controls are inputs, not EFMW discoveries.

## Abstract
The research program investigates whether microscopic quantum connectivity can yield an effective gravitational geometry. The initial QST studies separate finite quantum models from classical gravity. Subsequent experiments construct reciprocal spin–oscillator coupling, quantum propagation on graphs, quantum-informed graph rewiring, coherent superpositions of connectivity and graph-basis decoherence. The tensor and canonical studies then identify the requirements for a massless two-polarization gravitational sector, reconstruct the linearized constraint algebra, test a symmetry-reduced nonlinear Einstein–scalar reference and map microscopic links to canonical variables. The original link Hamiltonian fails gravitational constraint preservation; energetic penalties do not restore exact gauge symmetry. A regulated protected sector suppresses static leakage but exhibits coherent phase errors and resonant leakage. No microscopic derivation of Einstein gravity, unique EFMW interaction or physical quantum spacetime is established.

## 1. Baseline and existing obligations
QST-001 uses an assumed Einstein–Hilbert action and classical scalar FLRW dynamics, separately from an 888-state unitary ring. QST-002 finds spectral dimension near one for that ring; three axes must be supplied to obtain a three-dimensional torus. Base888 assigns distances from mutual information rather than deriving connectivity. TOE-001 supplies a conventional covariant two-scalar action with conserved total stress on shell. WITD-002 and IST-001 identify a mismatch between displayed informational stress and actual interacting energy storage. A unique independently constrained informational source remains unresolved.

Sources:
- https://github.com/enuminous/Quantum-Gravity/blob/main/QST-001.md
- https://github.com/enuminous/QST/blob/main/QST-002.md
- https://github.com/enuminous/Base888-Quantum-Geometry
- https://github.com/enuminous/EFMW-Lagrangian
- https://github.com/enuminous/papers/blob/main/TOE-001-Unified-Action-and-Correspondence-Test.md
- https://github.com/enuminous/papers/blob/main/IST-001-Deriving-Informational-Stress-from-Covariant-Memory-and-Reservoir-Models-2026-11-09.md

## 2. QG-003 — Reciprocal quantum backreaction
Hamiltonian H=(p²+q²)/2+Δσ_x/2+g q σ_z, in dimensionless units. The geometry label is an interpretation of an ordinary oscillator. In the untruncated canonical model q''+q=-g σ_z. The spin reciprocally depends on q. Reported 12 configurations, 36 trajectories, 14,436 sampled states, maximum dimension 96. At g=.6, maximum matter-to-mode response 1.556932 and mode-to-matter response 1.381328; minimum reduced purity .630043. At g=0 reciprocal effects vanish. With fixed positive σ_z and Δ=0 the equilibrium is q=-g. Maximum reported norm and energy errors 4.33e-14 and 7.93e-14; basis refinement discrepancy 7.55e-14. Bounded PASS for conventional spin–oscillator coupling; no curvature or gravity derived.

## 3. QG-004 — Collective quantum geometry
H=(pᵀp+qᵀ(m²I+L)q)/2. Frequencies sqrt(m²+λ(L)). Nine prescribed ring, square and cubic networks, up to 576 sites; 63 single-excitation propagation samples. Spectral dimension d_s(s)=2s Tr(L exp(-sL))/Tr(exp(-sL)). At s=8 cubic sizes 8³,16³,32³,64³ yield .509169,3.011013,3.050135,3.050135. The axes are imposed. Mutual information decreases with graph distance; at distances 1 and 3 the reported means are .168097 and .009320 (ring), .054131 and .002920 (square), .023781 and .000855 (cubic). Low-momentum dispersion is scalar. Norm error 5.55e-15; energy error 5.60e-14; static residual 4.22e-15. No emergent dimension or graviton.

## 4. QG-005 — Geometry without prescribed coordinates
Classical degree-preserving rewiring of connected 48-site degree-six graphs, informed by oscillator vacuum energy E0=Tr sqrt(m²I+L)/2. Eighteen runs, six seeds, 6300 attempts; random and classical triangle-clustering controls.
| Arm | Initial clustering | Final clustering | Final energy/site |
|---|---:|---:|---:|
| Random | .08125 | .08403 | 1.200710 |
| Quantum-energy | .08125 | .10764 | 1.200368 |
| Classical clustering | .08125 | .15556 | 1.199780 |
All began at mean energy/site 1.200793. No stable three-dimensional spectral plateau. Classical comparator also lowers quantum energy more in this exploratory setting; optimization strengths not matched. No distinctive quantum advantage or quantum superposition of graphs.

## 5. QG-006 — Quantum connectivity
Joint basis |G,i> for 15 labelled four-vertex four-edge graphs and four matter sites; dimension 60. H=h L_graph⊗I+Σ_G |G><G|⊗(g L_G+M). Nine parameter configurations, 241 samples per trajectory. Opposite relative phases and incoherent mixtures yield different graph populations when transitions are active. At h=.6,g=.5 reported phase TV difference .898868; maximum across tested cases .94254. Minimum matter purity .305344 (theoretical lower bound .25). At h=.2,g=.5 reciprocal TV responses .3225 and .1197. Null controls: no coupling removes reciprocal influence; no graph transitions freezes graph populations but does not necessarily eliminate graph-phase backreaction. Norm and energy errors 3.15e-14 and 2.93e-14. Labelled vertices and fixed potential are not background independence.

## 6. QG-007 — Decoherence and classical geometry
Graph projectors P_G define Lindblad generator -i[H,ρ]+γΣ_G(P_GρP_G-{P_G,ρ}/2). Fourteen configurations, 42 trajectories, 2562 samples, four and five vertices. Four-vertex final phase TV at γ=0,.5,2,10: .456275,.020836,.006223,.002761. Initial graph survival .079004,.097476,.12134,.491834. Five-vertex survival .7107,.2912,.1787,.4579: strong monitoring does not universally improve final survival. No graph obtains majority probability in the reported superposition runs. Trace error 3.02e-14, Hermiticity error 2.97e-14, minimum eigenvalue -2.12e-14 consistent with roundoff. Decoherence suppresses interference, not necessarily selects a unique classical geometry. Graph density changes between sizes, preventing clean scaling. Open-system energy need not be conserved.

## 7. QG-008 — Gravitational excitations
Original scalar network has mass gap .5. Removing mass gives ω²=4Σ sin²(k_i/2), approaching |k|² at long wavelength, but spin remains zero. Axial link perturbations have TT rank one for propagation along z; 45-degree rotation moves the plus tensor outside the diagonal representation. Full symmetric tensor positive control uses P=I-nnᵀ and S_TT=PSP-P Tr(PS)/2. 128 projection tests; two polarizations supplied, not emergent. Maximum dispersion errors at 16³,32³,64³,128³: 4.41224%,1.11909%,.28078%,.07026%. Gauge rejection residual 2.04e-15; rotational covariance residual 1.39e-15. All 24 vertex permutations tested for QG-006: original fixed potential symmetry violation .6, uniform control zero. Discrete permutation symmetry is not diffeomorphism invariance.

## 8. QG-009 — Tensor representation and extra modes
Nine axial and diagonal link directions measure nᵀεn; measurement rank six and TT rank two. Ordinary displacement strain ε_ij=(∂_i u_j+∂_j u_i)/2 has zero continuum TT projection. Reported finite-grid TT power decreases from .030386% at 16³ to .000000426% at 256³. Independent compatible links with K=|q|²I+4(I-AA⁺) retain six gapless modes and three gapped redundant modes. Finite trace penalty gaps one scalar; divergence penalty leaves vector frequency squared (1+α/2)|q|², hence gapless for finite α. Elastic, compatible-link and finite-penalty candidates fail exclusive two-mode criterion. Prescribed cubic embedding; not a derivation from QG-006.

## 9. QG-010 — Linear canonical constraints
For nonzero real Fourier mode, six h and six π components; constraints C0=k_i k_j h_ij-|k|² tr h and Ci=k_j π_ij. Four independent first-class constraints remove eight phase dimensions, leaving two canonical physical pairs. In normalized coordinates the constructed reference uses Kπ=I-ttᵀ/2 and Kh=I-2DᵀD+Dᵀntᵀ+tnᵀD-ttᵀ. Closure and gauge-equivalent evolution reported at ~1e-15. Twenty momentum configurations, 320 gauge-equivalent pairs. Ordinary oscillator leakage 1.414214; compatible links 2; reference 3.25e-16. Since {Cμ,Cν}=0, adding λΣC²/2 cannot alter {Cμ,H}. Imposed constraint-preserving quadratic ansatz yields potential coefficient ratio 1:-2:1:-1. Classical canonical reference, not microscopic emergence.

## 10. QG-011 — Nonlinear classical consistency
Symmetry-reduced Einstein–scalar action with spatial metric diag(e^{2a},e^{2b},e^{2c}), fields depending on one spatial coordinate. Constraint algebra {H[N],H[M]}=D[e^{-2a}(NM'-MN')], {D[v],H[N]}=H[vN'], {D[v],D[w]}=D[vw'-wv']. 300 configurations, 900 identities, five resolutions, 20 seeds. Reported maximum fine-grid residuals 3.20e-14,1.24e-14,1.78e-15. Frozen structure function residual 7.29879; removed nonlinear curvature term 8.43291; removed matter gradient 19.03043. Missing matter contribution -∫e^{-2a}(NM'-MN')pφ φ' dx agrees with numerical difference to 3.46e-14. Weak-field conformal curvature R=e^{2Φ}(4Φ''-2Φ'^2) approaches 4Φ''; time-symmetric constraint gives Poisson relation under appropriate assumptions. Coarse-grid and initial gradient-check failures retained; subsequent refinement passed as reported. No generic full 3+1 or quantum algebra test.

## 11. QG-012 — Canonical microscopic bridge
For full-column-rank link map A, h=A⁺x and π=Aᵀp give {h_i,π_j}=δ_ij; ideal canonical quantum operators obey the analogous commutator. With G=AᵀA, ordinary compatible-link effective H=πᵀG⁻¹π/2+ω²hᵀGh/2. Increasing redundant-sector compatibility gap does not change the six-mode sector; leakage 2 at penalties 0,4,100,10000. Ordinary vacuum constraint covariance minimum .25 in tested normalization, not a physical constrained vacuum. Pullback of QG-010 reference preserves constraints by construction. Reported canonical residual 9.82e-16, closure 8.93e-13. Perturbing reference by εH_links produces leakage 2ε on tested grid. Twenty momenta, 280 cases. Symplectic mapping PASS; spontaneous gauge symmetry unresolved.

## 12. QG-013 — Protected quantum gravitational states
Regulated compact gauge rotors with four charges Q_a; physical sector Q_a=0 and a two-state polarization doublet. H=H_TT+ΔΣQ_a²+εV. Twenty canonical configurations, 48 static experiments, 192048 static samples; largest factorized Hilbert dimension 4802. Static sampled leakage:
| Δ | Leakage (%) |
|---:|---:|
| 0 | ~100 |
| .5 | 43.5021 |
| 1 | 17.497 |
| 2 | 5.10593 |
| 4 | 1.33094 |
| 8 | .336278 |
| 16 | .0842975 |
| 32 | .0210889 |
Large-gap inverse-square behavior is consistent with static perturbation theory. At Δ=32 extended evolution to t=2000 retains small leakage but minimum postselected fidelity 6.25e-9. Branch-dependent virtual shifts δE≈-2a²/Δ produce relative phase; predicted splitting .0027, numerical .002699916; predicted reversal time 1163.58885, observed 1163.6. Resonant control P_leak=sin²(εt) reaches unity at t=π/(2ε), defeating all four tested gaps. [P0,H]=ε[P0,V]; penalty cannot restore exact symmetry. Direct/factorized agreement 6e-15. Compact regulator and imposed physical sector are not a derivation of GR. Zero-gap cutoff sensitivity retained. Coherent phase error is not irreversible information loss.

## 13. Consolidated evidence register
| Obligation | Interim verdict |
|---|---|
| Joint quantum matter–mode dynamics | PASS in specified toy model |
| Quantum connectivity interference | PASS in finite labelled graph model |
| Graph decoherence | PASS in imposed open-system model |
| Unique classical geometry | UNRESOLVED |
| Spontaneous three spatial dimensions | UNRESOLVED |
| Scalar or ordinary elastic modes as gravitons | FAIL for tested identifications |
| Complete spatial tensor representation | PASS conditional on embedding |
| Exclusive two tensor modes from links | FAIL for tested models |
| Linear first-class constraints | PASS for constructed reference |
| Nonlinear reduced classical closure | PASS for constructed reference |
| Microscopic canonical map | PASS for full-rank linear map |
| Compatibility/finite penalties as exact gauge symmetry | FAIL |
| Static energetic protection | PASS bounded |
| Arbitrary resonant protection | FAIL |
| Long-time unperturbed polarization fidelity | FAIL in tested example |
| Microscopic emergence of gauge symmetry | UNRESOLVED |
| Quantum nonlinear constraint closure | UNRESOLVED |
| Background independence, Lorentzian emergence, continuum/UV limit | UNRESOLVED |
| Unique EFMW physical signature and empirical confirmation | UNRESOLVED |

PASS here refers to reported bounded checks, not independent certification. No aggregate pass score is meaningful. The sequence is a collection of related diagnostic models, not a single integrated Hamiltonian. In particular, graph, embedded link, canonical GR and compact rotor models have distinct assumptions. Numerical precision is not physical accuracy.

## 14. Next gate: QG-014
Construct a local microscopic rank-2 gauge model with explicit symmetry generators and gauge-invariant interactions. Compare vector-charge and other conventional tensor-gauge constructions, count physical modes, derive effective dispersion and test symmetry-preserving perturbations and virtual corrections. Distinguish imposed exact symmetry from emergent low-energy symmetry. Require a mechanism-removal control and an independently reproducible source package. Do not claim Einstein correspondence merely from two polarizations. Subsequent gates must address nonlinear constraint structure, conserved matter coupling, universal low-energy response, Lorentzian continuum and independent empirical discrimination.

## 15. Publication and reproducibility boundary
This interim paper consolidates the previously reported QG-003–013 results, including failures. The individual local source files, raw trajectories, logs and archives are not included in this commit; exact artifact hashes, runtime replay and independent review remain outstanding. Reported numerical values are rounded or transcribed from prior reports. No new simulation is claimed for this publication. Preserve all historical results and publish original artifacts separately before claiming a complete reproducibility release.

## Conclusion
The research has identified increasingly restrictive mathematical targets for a microscopic theory of gravity. The strongest advances are conditional constructions and explicit obstructions: quantum graph coherence is not spacetime, tensor representation is not gauge symmetry, and energetic protection is not correct physical evolution. The central missing derivation is a microscopic mechanism yielding the gravitational constraint structure and its nonlinear quantum dynamics. The work is a research program, not a solved quantum theory of gravity.
