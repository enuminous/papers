# QNET-001 — first bounded test of dynamical connections

**Result: a consistent connection-evolution rule, but no demonstrated 3+1-dimensional structure.** The frozen static model has exact non-three-dimensional ground states and geometric degeneracies. Neither the checked dynamics nor the nominated matter dimension 888 removes that gap.

This is an original local diagnostic implementation of a **new postulate**, not a derivation from EFMW, not an implementation of the user's repository, and not a claim of novelty. No external repository code was executed or modified; no package was installed and nothing was published.

## 1. Frozen scope and evidence

The complete design locally frozen before computation is [`PROTOCOL.md`](PROTOCOL.md), written before running numerical calculations. Its SHA-256 is:

`fc264efee375c6509fab46a00c8907e0b48856e51843f4330558508939116ec3`

- Static: every labelled simple graph at N=4,5,6; U=V=J=1; g=0; μ=0,1,2,4; aligned matter.
- Dynamics: the complete three-edge 8-dimensional quantum edge space at N=3; μ=1, g=0.25, U=V=J=ℏ=1; initially empty graph; t=0,0.5,…,4.
- Geometry references: three explicitly constructed N=216, degree-6, triangle-free graphs. They are **diagnostic references**, not emergent graphs or simulation initial conditions. They are not asserted to be ground states at these μ values.
- The q=887/888/889 null is an exact symmetry restriction, not a huge numerical matter simulation.
- Supplemental analytic deductions below were added after the protocol freeze and before final reporting, with no changes to frozen grids, thresholds, or numerical targets. They are distinguished from the prespecified tests.

## 2. Mathematical rule

Each of N labelled vertices has matter space C^q; each unordered pair has a two-state connection. Set M=N(N−1)/2 and

\[
\mathcal H=(\mathbb C^q)^{\otimes N}\otimes(\mathbb C^2)^{\otimes M},\qquad
n_{ij}=\frac{I-Z_{ij}}2,\quad d_i=\sum_{j\ne i}n_{ij}.
\]

The matter swap S_ij is Hermitian, S_ij²=I, and commutes with all edge operators. The proposed Hamiltonian is

\[
H=\frac U2\sum_i d_i(d_i-1)-\mu\sum_{i<j}n_{ij}
 +V\sum_{i<j<k}n_{ij}n_{jk}n_{ik}
 -J\sum_{i<j}n_{ij}S_{ij}-g\sum_{i<j}X_{ij}.
\]

All five coefficients have energy units. For time-independent H, the complete rule is

\[
 i\hbar\partial_t|\Psi(t)\rangle=H|\Psi(t)\rangle,
 \qquad |\Psi(t)\rangle=e^{-iHt/\hbar}|\Psi(0)\rangle.
\]

Only the X term changes an edge occupation. The exact Heisenberg equation is

\[
\boxed{\frac{d\langle n_{ij}\rangle}{dt}=\frac g\hbar\langle Y_{ij}\rangle.}
\]

This follows from [X,n]=iY and i[−gX,n]=gY. In particular, a diagonal number-basis initial state can have zero initial occupancy derivative while developing edges at second order; zero initial slope is not frozen dynamics.

A useful local form is H=H_rest+n_ij Δ_ij−gX_ij, where H_rest does not act on the ij edge and

\[
\Delta_{ij}=U(r_i+r_j)-\mu
 +V\sum_{k\ne i,j}n_{ik}n_{jk}-JS_{ij},\qquad
r_i=\sum_{k\ne i,j}n_{ik}.
\]

Consequently

\[
\frac{dY_{ij}}{dt}=\frac{2gZ_{ij}-\Delta_{ij}X_{ij}}\hbar.
\]

The expectation of Δ_ij X_ij is a correlation: replacing it with a product of expectations is an additional approximation, not part of this study. This is an externally timed quantum graph model; writing a time coordinate does not establish emergent relativistic time.

## 3. Exact static enumeration

In aligned matter, every swap acts as +1. With g=0 the graph-basis energy is exactly

\[
E(G)=U\sum_i {d_i\choose 2}-(\mu+J)|E(G)|+V T(G).
\]

Integer arithmetic was used for all static energies. Graph counts are over **labelled** graphs and are not a physical probability measure over unlabelled topologies. They are not total matter-inclusive ground-state degeneracies.

| N | Graphs per μ | μ | Minimum E | Ground graphs | Connected ground graphs | Connected fraction |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 64 | 0 | −2 | 3 | 0 | 0/3 |
| 4 | 64 | 1 | −4 | 18 | 15 | 15/18 |
| 4 | 64 | 2 | −8 | 3 | 3 | 3/3 |
| 4 | 64 | 4 | −16 | 3 | 3 | 3/3 |
| 5 | 1,024 | 0 | −2 | 45 | 0 | 0/45 |
| 5 | 1,024 | 1 | −5 | 102 | 72 | 72/102 |
| 5 | 1,024 | 2 | −10 | 12 | 12 | 12/12 |
| 5 | 1,024 | 4 | −21 | 10 | 10 | 10/10 |
| 6 | 32,768 | 0 | −3 | 15 | 0 | 0/15 |
| 6 | 32,768 | 1 | −6 | 750 | 420 | 420/750 |
| 6 | 32,768 | 2 | −12 | 60 | 60 | 60/60 |
| 6 | 32,768 | 4 | −27 | 10 | 10 | 10/10 |

All enumerated ground graphs are triangle-free. At μ=2, they are C4, C5 and C6 respectively. At μ=4, they are C4, K2,3 and K3,3 respectively. These small finite graphs do not establish a spatial dimension. At μ=1, connected paths/cycles coexist with disconnected ground graphs.

All ground graph masks, sorted degree-sequence histograms, component-size histograms, joint structure histograms and triangle histograms are in [`results/static.json`](results/static.json). There were 33,856 distinct labelled graphs across N=4,5,6, evaluated at four μ values (135,424 graph/μ cases).

### Supplemental exact counterexample: global static ground states

For μ=2, U=V=J=1 and g=0,

\[
E(G)=\frac12\sum_i(d_i-2)^2-2N+T(G)\ge -2N.
\]

Every 2-regular triangle-free graph saturates the bound. In particular, at N=8:

- a connected cycle C8 has E=−16;
- two disconnected cycles C4 ⊔ C4 also have E=−16.

These are exact ground states, not merely equal-energy trial graphs. More generally, any disjoint union of cycles of length at least four is a saturating ground graph whenever it uses all N vertices. The energy therefore selects neither a unique connected geometry nor an extended three-dimensional geometry in this static setting. This is not a no-go theorem for all g, all matter sectors, or every possible added interaction.

## 4. Geometry blindness at fixed degree and triangle count

For every k-regular triangle-free graph on the same N,

\[
E=\frac{UN}{2}k(k-1)-\frac{(\mu+J)N}{2}k.
\]

Distance growth, dimension and connectedness do not occur in this expression. The frozen N=216 references all have k=6, 648 edges and zero triangles:

| Constructed reference | Components | Diameter | Mean finite nonself distance | Laplacian λ₂ | Ball sizes at radius 1,2,3 |
|---|---:|---:|---:|---:|---|
| 6×6×6 periodic cubic graph | 1 | 9 | 4.520930 | 1.000000 | 7, 25, 60 |
| Circulant offsets ±1,±3,±5 | 1 | 23 | 11.655814 | 0.029573 | 7, 17, 27 |
| 18 disjoint K6,6 | 18 | ∞; component diameter 2 | 1.454545 | 0 | 7, 12, 12 |

Their energies are **identically** 2592, 1944, 1296 and 0 at μ=0,1,2,4 respectively. No dimension was fitted. The disconnected graph's mean only averages finite pairs and must not be interpreted as a whole-network mean distance. Full distance shells, spectra, eigenvalue multiplicities and zero-mode counts are in [`results/geometry.json`](results/geometry.json).

The cubic graph's construction contains three dimensions by design. Its presence in this comparison is not evidence that the Hamiltonian generates them.

## 5. Exact quantum edge dynamics

The three edges are permutation-equivalent in this particular initial state. Below is the occupancy for **each** edge, not a dimension estimate:

| t | ⟨n_ij⟩ | ⟨Y_ij⟩ |
|---:|---:|---:|
| 0.0 | 0.0000000000 | 0.0000000000 |
| 0.5 | 0.0142983745 | 0.2084315344 |
| 1.0 | 0.0437122529 | 0.2232892012 |
| 1.5 | 0.0620796437 | 0.0511897917 |
| 2.0 | 0.0558110219 | −0.1385088827 |
| 2.5 | 0.0334528304 | −0.1887526839 |
| 3.0 | 0.0159747562 | −0.0675552150 |
| 3.5 | 0.0193070232 | 0.1169401863 |
| 4.0 | 0.0406304054 | 0.1952101356 |

Checks against the frozen tolerances:

| Check | Maximum error | Tolerance | Result |
|---|---:|---:|---|
| H=H† | 0 | 10⁻¹² | Pass |
| Norm squared =1 | 6.66×10⁻¹⁶ | 10⁻¹² | Pass |
| Energy conserved (initial E=0) | 2.36×10⁻¹⁶ | 10⁻¹² | Pass |
| i[H,n]=gY as full matrices | 0 | 10⁻¹² | Pass |
| State derivative =g⟨Y⟩ | 1.39×10⁻¹⁷ | 10⁻¹² | Pass |
| Separate finite difference, t=0.7, step 10⁻⁵ | 4.52×10⁻¹² | 10⁻⁹ | Pass |

The Hamiltonian, eigenvalues, all graph-basis probabilities and observables are in [`results/quantum.json`](results/quantum.json). Numerical diagonalization causes tiny roundoff at t=0 (reported without hiding it in JSON).

**This does not show relaxation to a ground state.** A closed, time-independent Hamiltonian evolves unitarily and conserves energy; no environment, measurement selection, cooling or dissipative mechanism was supplied. Nor does the uniform expected adjacency matrix identify the geometry of individual graph-basis outcomes.

## 6. What the q=888 test does—and does not—mean

For any normalized local matter vector |φ⟩ and every q≥1,

\[
S_{ij}|\phi\rangle^{\otimes N}=|\phi\rangle^{\otimes N}.
\]

Thus the aligned tensor sector is invariant, and the reduced edge Hamiltonian is exactly the same at q=887,888,889. This is a proof of a null in that sector, not three full-matter simulations. No array with 888^N entries was constructed.

### Supplemental theorem: full ground energy is q-independent for J≥0

Let H_g denote the edge Hamiltonian obtained by replacing all S_ij with +1. On the full Hilbert space,

\[
H=I_{\mathrm{matter}}\otimes H_g
 +J\sum_{i<j}(I-S_{ij})\otimes n_{ij}.
\]

Each term of the added sum is positive semidefinite: I−S_ij has eigenvalues 0 or 2; n_ij has eigenvalues 0 or 1; the two factors act on separate spaces. The added terms need not commute with one another for their sum to be positive semidefinite. Therefore E₀(H)≥E₀(H_g).

Conversely, tensor any normalized ground state of H_g with |φ⟩^{⊗N}. Every added term annihilates that state, so it has energy E₀(H_g). Hence

\[
\boxed{E_0(H;q)=E_0(H_g)\quad\text{for every }q\ge1\text{ and }J\ge0.}
\]

This holds at any g for this exact Hamiltonian, with all other coefficients fixed independently of q. It says nothing by itself about q-dependence of degeneracies, excited sectors, finite-temperature entropy, or dynamics from general entangled matter states. It does mean that q=888 has no special **ground-energy-selection** role here; this postulate has not translated the local state count into spatial dimension.

## 7. Audit, novelty and remaining obligations

No fixed animal-specific Zoo operations were supplied, so none were invented. The named conventional operations and their prespecified criteria are tabulated in the protocol.

| Claim / obligation | Evidence status | What is established or missing |
|---|---|---|
| Finite-space Hamiltonian and unitary connection rule are well defined | **Demonstrated** | Hermiticity, units and operator commutator; numerical identity checks |
| Frozen small-N ground census | **Demonstrated** | Complete exact integer enumeration; independently checked features at N=4 |
| Distinct regular triangle-free geometries are energetically degenerate at g=0 | **Demonstrated** | Formula plus three constructed references |
| Unique connected extended 3D ground geometry at μ=2,g=0 | **Rejected** | Exact cycle and disconnected-cycle ground-state counterexamples |
| q=888 differs from 887/889 in the aligned-sector dynamics | **Rejected** | Exact swap-invariance proof |
| q=888 selects a distinct full ground energy for this H with J≥0 | **Rejected** | Positive-semidefinite comparison theorem |
| An emergent 3D phase for some finite g or general states | **Unresolved** | Not tested at suitable scale; static counterexample is not a universal no-go |
| 3+1 spacetime, Lorentz symmetry, emergent gravity | **Unresolved / not demonstrated** | No continuum limit, causal structure, Lorentz sector, metric dynamics or gravity derivation |
| This Hamiltonian follows from EFMW | **Hypothesis/postulate, not derived** | No supplied derivation fixes these terms or couplings |
| Novelty | **Adjacent to established quantum graphity** | Dynamical graphs and emergent-locality objectives are prior art; no comprehensive novelty search or novelty claim |

Anti-circularity checks: the parameters and tolerances were frozen; no dimension-targeted tuning was performed; constructed cubic geometry was not used as evidence of emergence; static minima were not equated with real-time dynamical attraction; mathematical checks of the same identities were not counted as independent empirical evidence. The study contains no physical experiment. No implementation bug or protocol amendment was needed in the recorded run.

The user's source for the nominated local matter dimension is [QST-001 §8, pinned repository revision 4d533344e2f05c365b24acb9616e8a303fcc4587](https://github.com/enuminous/Quantum-Gravity/blob/4d533344e2f05c365b24acb9616e8a303fcc4587/QST-001.md). That source supplies the nominated local state space but not the graph-evolution rule tested here. The present H is an explicit proposed addition, not a claim that the source contains it.

The known conceptual precedent is Konopka, Markopoulou and Severini, [*Quantum Graphity: a model of emergent locality*](https://arxiv.org/abs/0801.0861), [Phys. Rev. D 77, 104029 (2008)](https://doi.org/10.1103/PhysRevD.77.104029). It supplies a prior-art dynamical-graph setting, not proof for the particular Hamiltonian tested here.

### Minimal next step (proposed, not executed)

Before another dimensionality run, require a derivation or independently justified correlation-sensitive interaction that can distinguish geometry beyond degree and triangle count, and state how a state/ensemble is selected. A penalty fitted until it produces three dimensions would not supply that derivation. Freeze that specification and its q-dependence before looking at dimension estimates. The first acceptance gate should be mathematical: **pass** only if the proposed rule demonstrably resolves the explicit cycle/disconnected-cycle and same-degree triangle-free blind spots relevant to its claimed regime, without presupposing a 3D lattice; **fail** if the exact same blind spots remain or 3D is inserted as an initial lattice or fitted target. Passing this gate would still not establish 3D; a separate finite-size/scaling and low-energy-physics protocol would be required.

## 8. Reproduce and inspect

Tested with **Python 3.12.14 and NumPy 2.3.5**; `requirements.txt` records the exact NumPy version. Only Python standard library and preinstalled NumPy were used. No network or extra package is needed, and no installation was performed.

```sh
cd qnet001
python qnet.py --output results
python test_qnet.py
```

All 8 tests passed. These cover the frozen protocol hash, independent adjacency-matrix versus bitset graph features/energies, hand-derived N=3 energies, Pauli/commutator identities, norm and energy checks, reference graph construction and spectra, the C8/two-C4 ground-bound examples, and histogram bookkeeping. Complete machine-readable outputs:

- `results/static.json`: every ground mask and all static histograms.
- `results/quantum.json`: full 8×8 Hamiltonian, eigenvalues, time-series probabilities and diagnostics.
- `results/geometry.json`: all reference-graph distance growth and Laplacian spectra.
- `results/q_null.json`: exact-sector null statement and scope.
- `results/tests.json`: test counts and any errors (none).
- `results/manifest.json`: runtime versions, protocol/source hashes, hashes of computed results.
- `run_summary.json`: concise numerical run output.
- `CHECKSUMS.sha256`: hashes for the delivered source and results (generated after final validation).

The 216-vertex references use ordinary graph matrices, not a 2^23220-dimensional quantum simulation. Only N=3 was evolved as a full edge-state vector; only N≤6 was exhaustively enumerated.
