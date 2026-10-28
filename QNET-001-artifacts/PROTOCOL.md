# QNET-001: frozen bounded study

Frozen before numerical results: 2026-10-28 UTC. Version 1.

## Target and epistemic status

Test a newly **postulated**, quantum-graphity-style connection Hamiltonian; it is not derived from EFMW and is not claimed novel. Ask whether the prescribed rule by itself selects three-dimensional spatial structure. A nontrivial quantum evolution is not evidence of three dimensions, Lorentz symmetry, or 3+1 spacetime.

For N labelled vertices, matter at each vertex is C^q (q=888 is the nominated value), and every unordered pair has a qubit. The full space is (C^q)^{⊗N} ⊗ (C^2)^{⊗M}, M=N(N−1)/2. Let n_ij=(I−Z_ij)/2, d_i=∑_{j≠i}n_ij, and S_ij swap the two matter factors. Fix

H = (U/2)∑_i d_i(d_i−1) − μ∑_{i<j}n_ij + V∑_{i<j<k}n_ij n_jk n_ik − J∑_{i<j}n_ij S_ij − g∑_{i<j}X_ij.

Schrödinger evolution is iℏ ∂_t|Ψ⟩=H|Ψ⟩. U,V,J,μ,g have energy units. Time is external and continuous; space dimension is not specified. All coupling values below are dimensionless after choosing an energy unit and ℏ=1.

## Frozen computations

1. **Static exact enumeration:** U=V=J=1, g=0, μ∈{0,1,2,4}, N∈{4,5,6}. All matter factors begin in the same pure state. This invariant sector has S_ij=+1 exactly. Enumerate every labelled simple graph once (2^{N choose 2} graphs). Report exact integer ground energies; ground counts; connected count and fraction; sorted component-size and degree-sequence histograms; triangle-count histogram. Do not interpret label multiplicities as an equilibrium distribution over unlabelled topologies. No dimension-targeted parameter search or fit.
2. **Quantum edge evolution:** N=3, U=V=J=1, μ=1, g=1/4, ℏ=1, same aligned-matter invariant sector, initial graph |000⟩. Construct the full 8×8 edge Hamiltonian and evolve by Hermitian eigendecomposition at t=0, 1/2, 1, …, 4. This is fully quantum for all three edge qubits, not the full q^N matter space. Report all edge occupancies, all edge Y expectations, energy, norm, and computational-basis graph probabilities. Verify Hermiticity, norm/energy conservation, and the exact operator commutator i[H,n_ij]=gY_ij; check the state derivative of occupancy against g⟨Y⟩, with a separate central-finite-difference sanity check at t=0.7 and step 10^-5. Floating-point pass tolerances are 10^-12 for matrix/expectation identities and 10^-9 for the finite-difference check.
3. **q null:** For q∈{887,888,889}, report exact aligned-sector independence as a symbolic restriction, not three enormous matter simulations. The vector |φ⟩^{⊗N} is fixed by every swap for any q≥1; the same edge Hamiltonian acts on it. No claim about unaligned/entangled matter, the full spectrum, or q-sensitive sectors is permitted.
4. **Geometry diagnostic (reference graphs, not initial conditions or emergent outputs):** N=216, compare a 6×6×6 periodic nearest-neighbour cubic graph; the circulant graph with offsets ±1,±3,±5 modulo 216; and 18 disjoint copies of K_6,6. Each is 6-regular and triangle-free. Check equal static energy for every frozen μ; report connected components, finite within-component diameter, mean finite-pair distance, distance-shell/cumulative-ball growth from vertex 0, full combinatorial-Laplacian eigenvalues and multiplicities within numerical tolerance, algebraic connectivity, and zero eigenvalue count. Their construction contains chosen geometry and therefore cannot demonstrate emergent dimension. Do not fit a dimension to these finite examples. In particular, these degree-6 reference graphs are not asserted to be ground states at the frozen μ values.
5. **Analytic degeneracy:** In the aligned static sector, every k-regular triangle-free graph on the same N has E=(UN/2)k(k−1)−((μ+J)N/2)k, regardless of distances, dimension or connectedness. This is an exact conditional degeneracy, not a proof about the full g≠0 model.

## Operations and criteria

No animal-specific Zoo operations were supplied, so none will be invented. This study uses explicitly named conventional operations:

| Operation | Inputs | Transformation/output | Criterion |
|---|---|---|---|
| Type/commutator audit | Frozen H and Hilbert space | Hermiticity; i[H,n] | Matching dimensions and exact edge rule |
| Exhaustive finite search | N, μ grids above | Every labelled graph and complete ground histograms | Exact integer arithmetic; enumerated count 2^M |
| Exact finite-dimensional dynamics | 8×8 H, |000⟩, frozen times | Unitary states and observables | Numerical residuals below stated tolerances |
| Symmetry restriction | Aligned matter tensor and swaps | q-independent reduced Hamiltonian | Exact invariance proof; no numerical extrapolation |
| Counterexample diagnostic | Three reference graph families | Geometry statistics and equal energy | Same N,k,triangle count; different distance/connectivity structure |

## Anti-circularity and decision rules

- Neither q=888 nor three dimensions determines a coefficient or acceptance threshold.
- The small-N enumeration is only a bounded static-sector test. It cannot establish or rule out a thermodynamic phase of the full theory.
- A **demonstrated** statement requires an analytic identity or the explicitly bounded reproducible computation.
- The claim that this Hamiltonian establishes 3+1-dimensional spacetime remains **unresolved/not demonstrated** without scale-dependent emergent geometry, stability, low-energy continuum and causal/Lorentz-sector evidence.
- Equal energies for different geometric reference graphs **reject** unique geometry selection by the static degree-and-triangle energy within that regular triangle-free sector; they do not alone rule out geometry selection by finite g, matter entanglement, thermal effects or other terms.
- Negative and null results will be preserved. No coefficients, graph sizes, times, tolerances or dimension targets will be tuned after results.

## Sources and implementation boundaries

Conceptual prior-art reference: Konopka, Markopoulou and Severini, *Quantum Graphity: A Model of Emergent Locality*, https://arxiv.org/abs/0801.0861 . User repository context: https://github.com/enuminous/Quantum-Gravity . Neither source is treated as establishing this proposed Hamiltonian or its claimed dimension.

Write original local code using only Python standard library and preinstalled NumPy. Do not install packages, execute external repository code, publish, or modify the user's repository. Deliver source, tests and complete JSON results. Fixing implementation bugs is allowed and must be disclosed; changing scientific targets requires a versioned amendment.
