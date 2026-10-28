# QNET-001: Dynamical Connections and Obstructions to 3+1-Dimensional Emergence

**Matthew Chenoweth Wright**  
**Monolithic LLC**  
**2026-10-28**

## Abstract

A dynamical connection rule does not, by itself, establish an emergent spatial dimension. This study examines a postulated finite quantum graph Hamiltonian with vertex matter spaces, binary edge degrees of freedom, degree and triangle penalties, a matter-swap interaction, and coherent edge flips. The model is mathematically well defined and yields an exact connection-occupation equation. Exhaustive static enumeration covers every labelled simple graph on four, five, and six vertices at four fixed chemical potentials; exact finite-dimensional quantum evolution covers all three edge qubits on three vertices. All recorded numerical checks satisfy their locally frozen tolerances. The dimensionality results are negative or unresolved. At one frozen static parameter point, every disjoint union of cycles of length at least four is an exact ground graph, including both connected and disconnected examples. Three constructed 216-vertex, six-regular, triangle-free references have identical static energies despite sharply different distance and connectivity structure. A positive-semidefinite comparison proves that, for nonnegative swap coupling, the full ground energy is independent of the local matter dimension for every positive integer dimension, including 887, 888, and 889. These results identify specific obstructions in the proposed model; they neither establish new physics nor constitute a universal no-go theorem for dimensional emergence. Three-dimensional space, relativistic time, and a 3+1-dimensional continuum remain undemonstrated.

**Keywords:** dynamical graphs; quantum graphity; emergent geometry; exact enumeration; ground-state degeneracy; reproducible computation.

## 1. Question and scope

The question is whether a specified quantum rule for changing connections supplies evidence for three-dimensional spatial structure without inserting that structure into an initial lattice or a fitted target. The answer for the bounded study reported here is that a consistent connection dynamics can be established, but the required geometric selection has not been demonstrated. Exact static counterexamples and a matter-dimension null result delimit what this particular postulate can support.

The nominated local matter dimension, $q=888$, comes from [QST-001 §8 at pinned repository revision `4d533344e2f05c365b24acb9616e8a303fcc4587`](https://github.com/enuminous/Quantum-Gravity/blob/4d533344e2f05c365b24acb9616e8a303fcc4587/QST-001.md). That source provides the motivating local state count; it does not supply the connection Hamiltonian analyzed below. This Hamiltonian is an additional postulate, not a derivation from EFMW or an implementation of the source repository.

Dynamical graphs and the aim of emergent locality have established precedent in quantum graphity. Konopka, Markopoulou, and Severini developed such a setting in *Quantum Graphity: A Model of Emergent Locality*. The present work is adjacent to that program, without claiming that its Hamiltonian, results, or scope are identical. No comprehensive novelty search is reported, and no novelty claim is made. [Quantum graphity, Phys. Rev. D 77, 104029 (2008)](https://doi.org/10.1103/PhysRevD.77.104029)

The evidence consists of finite-dimensional mathematics and bounded computation, not a physical experiment. In particular, the presence of an external time parameter is not evidence of emergent relativistic time.

## 2. Model and exact connection rule

### 2.1 Degrees of freedom and Hamiltonian

Let $N$ be a finite positive integer and $q$ a positive integer. Each of $N$ labelled vertices carries a matter space $\mathbb C^q$, and each unordered vertex pair carries an edge qubit. With $M=N(N-1)/2$, write

$$
\mathcal H=\mathcal H_{\mathrm m}\otimes\mathcal H_{\mathrm e},
\qquad
\mathcal H_{\mathrm m}=(\mathbb C^q)^{\otimes N},
\qquad
\mathcal H_{\mathrm e}=(\mathbb C^2)^{\otimes M}.
$$

The edge computational basis represents labelled simple graphs: no self-loops or multiple edges are included. For the Pauli operators on edge $ij$, define

$$
n_{ij}=\frac{I-Z_{ij}}2,
\qquad
d_i=\sum_{j\ne i}n_{ij}.
$$

An occupied edge has $n_{ij}=1$. Let $S_{ij}$ swap the matter factors at vertices $i$ and $j$. It is Hermitian, satisfies $S_{ij}^2=I$, and commutes with every edge operator. Suppressing identity tensor factors, the proposed Hamiltonian is

$$
\begin{aligned}
H={}&\frac U2\sum_i d_i(d_i-1)
-\mu\sum_{i<j}n_{ij}
+V\sum_{i<j<k}n_{ij}n_{jk}n_{ik}\\
&-J\sum_{i<j}n_{ij}S_{ij}
-g\sum_{i<j}X_{ij}.
\end{aligned}
\tag{1}
$$

All five coefficients $U,\mu,V,J,g$ have energy units and are real. Every summand is Hermitian: the number operators commute with one another, and the matter swaps commute with the edge operators multiplying them. At finite $N$ and $q$, equation (1) therefore defines a finite Hermitian matrix and a unique unitary evolution for every initial state. For time-independent couplings,

$$
i\hbar\,\partial_t\lvert\Psi(t)\rangle=H\lvert\Psi(t)\rangle,
\qquad
\lvert\Psi(t)\rangle=e^{-iHt/\hbar}\lvert\Psi(0)\rangle.
\tag{2}
$$

The model presupposes continuous external time. It contains no derivation of a metric, a causal cone, or Lorentz symmetry.

### 2.2 Occupation dynamics

Only the edge-flip term fails to commute with $n_{ij}$. Since

$$
[X_{ij},n_{ij}]=iY_{ij},
$$

the Heisenberg equation gives the exact identity

$$
\frac{d n_{ij}}{dt}
=\frac{i}{\hbar}[H,n_{ij}]
=\frac g\hbar Y_{ij},
\qquad
\boxed{\frac{d\langle n_{ij}\rangle}{dt}
=\frac g\hbar\langle Y_{ij}\rangle.}
\tag{3}
$$

For a fixed edge, define the incident degrees excluding that edge by

$$
r_i=\sum_{k\ne i,j}n_{ik},
\qquad
r_j=\sum_{k\ne i,j}n_{jk}.
$$

Using $n_{ij}^2=n_{ij}$, the Hamiltonian can be collected as

$$
H=H_{\mathrm{rest}}+n_{ij}\Delta_{ij}-gX_{ij},
$$

where $H_{\mathrm{rest}}$ does not act on the $ij$ edge and

$$
\Delta_{ij}=U(r_i+r_j)-\mu
+V\sum_{k\ne i,j}n_{ik}n_{jk}-JS_{ij}.
\tag{4}
$$

Because $\Delta_{ij}$ also does not act on that edge, the Pauli commutators yield

$$
\frac{dY_{ij}}{dt}
=\frac{2gZ_{ij}-\Delta_{ij}X_{ij}}{\hbar}.
\tag{5}
$$

The expectation $\langle\Delta_{ij}X_{ij}\rangle$ is a correlation. Replacing it with $\langle\Delta_{ij}\rangle\langle X_{ij}\rangle$ would introduce an approximation that is not used here. A number-basis initial state can have zero initial occupation derivative while subsequently developing nonzero occupation. A vanishing initial slope therefore does not imply frozen connections.

### 2.3 Aligned matter restriction

For every normalized $\lvert\phi\rangle\in\mathbb C^q$,

$$
S_{ij}\lvert\phi\rangle^{\otimes N}
=\lvert\phi\rangle^{\otimes N}.
\tag{6}
$$

Consequently the subspace

$$
\mathcal K_\phi
=\operatorname{span}\{\lvert\phi\rangle^{\otimes N}\}
\otimes\mathcal H_{\mathrm e}
$$

is invariant under $H$. On this subspace, replacing every $S_{ij}$ by $+1$ gives the exact reduced edge Hamiltonian, denoted $H_{\mathrm g}$. Its coefficients do not depend on $q$. This is a symmetry restriction, not an approximation to a simulation of the complete matter Hilbert space.

## 3. Frozen design and evidence provenance

The [local protocol](QNET-001-artifacts/PROTOCOL.md), version 1, is dated 2026-10-28 UTC. The recorded workflow states that it was frozen before numerical calculations. Its SHA-256 digest is

```text
fc264efee375c6509fab46a00c8907e0b48856e51843f4330558508939116ec3
```

This is a **local protocol freeze, not an external preregistration**. The digest identifies the preserved protocol bytes; by itself it does not independently establish when they were written. The [run manifest](QNET-001-artifacts/results/manifest.json) records completion at `2026-10-28T03:46:03.543174+00:00`. The original source and results are preserved as a historical record. Statements in the [original README](QNET-001-artifacts/README.md) that nothing had been published describe the local study at that time; this paper is a later presentation of that recorded study.

**Table 1. Prespecified computations and their limits.** Couplings are expressed in a chosen energy unit; the dynamical calculation uses $\hbar=1$.

| Component | Fixed inputs | Output and acceptance criterion | Scope limit |
|---|---|---|---|
| Static census | $N=4,5,6$; $U=V=J=1$; $g=0$; $\mu=0,1,2,4$; aligned matter | Enumerate all $2^M$ labelled graphs using integer energies; retain all ground masks and structural histograms | No thermodynamic extrapolation or dimension fit |
| Quantum dynamics | $N=3$; $U=V=J=1$; $\mu=1$; $g=1/4$; initially empty graph; $t=0,0.5,\ldots,4$ | Hermitian eigendecomposition of the full $8\times8$ edge Hamiltonian; identity and conservation residuals below $10^{-12}$ | Full edge space only; no full matter simulation |
| Derivative check | $t=0.7$; central-difference step $10^{-5}$ | Agreement with $g\langle Y\rangle$ to $10^{-9}$ | Numerical consistency check, not independent empirical evidence |
| Matter-dimension null | $q=887,888,889$; aligned matter | Exact swap-invariance argument | No numerical arrays of size $q^N$ |
| Geometry references | Three constructed graphs with $N=216$, degree six, and no triangles | Compare static energies, distance growth, components, and Laplacian spectra | Neither emergent outputs nor asserted ground states |
| Conditional degeneracy | Static aligned sector; fixed $N$, regular degree, and zero triangles | Derive equal energy independently of distance structure | Does not determine the finite-$g$ phase |

The complete classification of static cycle ground graphs in Section 4.2 and the full-Hilbert-space ground-energy theorem in Section 7 are **supplemental analytic deductions**, added after the local freeze and before the original final report. They are not retrospectively described as prespecified tests. No frozen graph sizes, coupling values, times, tolerances, or dimensional targets were changed in the recorded run, and no implementation repair or protocol amendment was reported.

No fixed animal-specific Zoo operations were supplied. The study therefore uses the conventional operations explicitly specified in the protocol: type and commutator audit, exhaustive finite search, finite-dimensional dynamics, symmetry restriction, and counterexample diagnostics. No animal operation is invented to obtain a preferred conclusion.

## 4. Static spectrum and exact counterexamples

### 4.1 Complete small-graph census

At $g=0$, the aligned-sector Hamiltonian is diagonal in the graph basis. For a labelled simple graph $G$, let $m(G)$ be its edge count, $d_i(G)$ its vertex degrees, and $T(G)$ its number of triangles. Its energy is

$$
E(G)=U\sum_i\binom{d_i(G)}2
-(\mu+J)m(G)+VT(G).
\tag{7}
$$

All frozen static energies are integers, so no floating-point comparison is needed to identify their minima. There are 64, 1,024, and 32,768 labelled graphs at $N=4,5,6$, respectively: 33,856 distinct graphs, each evaluated at four chemical potentials, for 135,424 graph/parameter cases.

**Table 2. Exact static minima for $U=V=J=1$ and $g=0$.** Counts refer to labelled ground graphs in the aligned sector, not total matter-inclusive degeneracies.

| $N$ | Graphs per $\mu$ | $\mu$ | Minimum energy | Ground graphs | Connected ground graphs | Connected fraction |
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

Every enumerated ground graph is triangle-free. At $\mu=2$, the ground graphs are precisely the labelled copies of $C_4$, $C_5$, and $C_6$ for the three respective sizes. At $\mu=4$, they are the labelled copies of $C_4$, $K_{2,3}$, and $K_{3,3}$. At $\mu=1$, connected paths and cycles coexist with disconnected ground graphs. These small finite structures are not dimension estimates.

The [complete static results](QNET-001-artifacts/results/static.json) retain all ground masks and degree, component-size, triangle, and joint-structure histograms. Labelling multiplicities are bookkeeping counts; no physical probability measure on unlabelled topologies is inferred from them.

### 4.2 Supplemental proposition on cycle ground states

**Proposition 1.** For $U=V=J=1$, $\mu=2$, and $g=0$, the aligned static energy satisfies

$$
E(G)=\frac12\sum_i(d_i(G)-2)^2-2N+T(G)\ge-2N.
\tag{8}
$$

For every $N\ge4$, the ground graphs are exactly the 2-regular triangle-free simple graphs. Equivalently, they are disjoint unions of cycles of length at least four that use all $N$ vertices.

**Proof.** The degree-sum identity is $\sum_i d_i=2m$. Substituting the specified couplings in equation (7) gives

$$
\begin{aligned}
E(G)
&=\frac12\sum_i(d_i^2-d_i)-3m+T(G)\\
&=\frac12\sum_i d_i^2-2\sum_i d_i+T(G)\\
&=\frac12\sum_i(d_i-2)^2-2N+T(G).
\end{aligned}
$$

Both the squared-degree term and $T(G)$ are nonnegative. Equality holds exactly when every degree is two and there are no triangles. Every finite 2-regular simple graph is a disjoint union of cycles, and excluding triangles requires each cycle length to be at least four. The connected cycle $C_N$ supplies a saturating graph for each $N\ge4$, so the bound is attained. ∎

At $N=8$, both $C_8$ and $C_4\sqcup C_4$ have ground energy $-16$. They are exact global minimizers of the static graph energy, not merely equal-energy trial configurations. By the ground-energy comparison in Section 7, their aligned-matter states also attain the full Hamiltonian ground energy at these couplings for every $q\ge1$.

This gives a precise obstruction: the frozen static model at this parameter point does not require connectedness and does not uniquely select an extended three-dimensional ground geometry. It is not a theorem against emergence for arbitrary couplings, finite edge-flip strength, different interactions, or a specified thermal or nonequilibrium selection mechanism.

## 5. Geometry blindness of the static regular sector

For any $k$-regular triangle-free graph with $N$ vertices, equation (7) reduces to

$$
E(G)=\frac{UN}{2}k(k-1)
-\frac{(\mu+J)N}{2}k.
\tag{9}
$$

**Proof.** All degrees equal $k$, the edge count is $Nk/2$, and the triangle count vanishes. Substitution into equation (7) gives equation (9). ∎

Distance growth, connectedness, and the Laplacian spectrum do not appear in this expression. The frozen diagnostic compares three explicitly constructed graphs: a periodic $6\times6\times6$ nearest-neighbour cubic graph, a circulant on $\mathbb Z/216\mathbb Z$ with offsets $\pm1,\pm3,\pm5$, and 18 disjoint copies of $K_{6,6}$. Each has 216 vertices, degree six, 648 edges, and zero triangles.

For the combinatorial Laplacian $L=D-A$, let $\lambda_2$ denote its second-smallest eigenvalue. Ball sizes below count vertices within the stated graph distance of vertex 0, including the root.

**Table 3. Constructed geometry references, not emergent graphs or simulation initial conditions.**

| Reference | Components | Whole-graph diameter | Mean finite nonself distance | $\lambda_2$ | Ball sizes at radii 1, 2, 3 |
|---|---:|---:|---:|---:|---|
| Periodic cubic graph | 1 | 9 | 4.520930 | 1.000000 | 7, 25, 60 |
| Circulant with offsets $\pm1,\pm3,\pm5$ | 1 | 23 | 11.655814 | 0.029573 | 7, 17, 27 |
| 18 disjoint $K_{6,6}$ | 18 | $\infty$ | 1.454545 | 0 | 7, 12, 12 |

The disconnected reference has within-component diameter two. Its finite-pair mean excludes unreachable pairs and must not be read as a whole-network mean distance. Its 18 Laplacian zero modes agree with its component count; each connected reference has one zero mode, using the recorded spectral tolerance of $10^{-8}$.

For all three references, equation (9) gives

$$
E=2592-648\mu,
$$

and hence the identical energies 2592, 1944, 1296, and 0 at $\mu=0,1,2,4$. The [geometry results](QNET-001-artifacts/results/geometry.json) include complete distance shells, spectra, multiplicities, and zero-mode counts.

The cubic graph contains three-dimensional organization by construction. Its inclusion is a test of whether the static energy distinguishes it from other geometries, not evidence that the Hamiltonian produces it. None of these reference graphs is asserted to be a ground state at the frozen chemical potentials, and no dimension was fitted. Equation (9) alone also does not determine how coherent edge flips affect the full spectrum at $g\ne0$.

## 6. Exact finite edge dynamics

The dynamical computation uses $N=3$, $U=V=J=1$, $\mu=1$, $g=1/4$, and $\hbar=1$ in the aligned sector, starting from the empty graph. All three edge qubits are retained, giving an eight-dimensional edge space. The full matter space is not constructed.

The diagonal energy at $g=0$ depends on the edge count as follows: the empty graph has energy 0; each one-edge graph has energy $-2$; each two-edge graph has energy $-3$; and the triangle has energy $-2$. The off-diagonal matrix element is $-1/4$ between graph masks differing by one edge and zero otherwise. This specifies the full $8\times8$ Hamiltonian, which is also preserved numerically in the [quantum results](QNET-001-artifacts/results/quantum.json).

Hermitian eigendecomposition evaluates equation (2) at the fixed times. Permutation symmetry of this initial state and Hamiltonian makes the three edges equivalent. Table 4 reports the expectation for **each edge**, not a sum over edges or a dimensionality observable.

**Table 4. Recorded edge occupation and Pauli-$Y$ expectation.**

| $t$ | $\langle n_{ij}\rangle$ | $\langle Y_{ij}\rangle$ |
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

The complete JSON retains the tiny eigendecomposition roundoff at $t=0$, rather than silently replacing it with the exact initial values. It also retains all eight graph-basis probabilities at every sampled time.

**Table 5. Numerical consistency checks against frozen tolerances.**

| Check | Maximum residual | Tolerance | Outcome |
|---|---:|---:|---|
| Hermiticity of $H$ | 0 | $10^{-12}$ | Pass |
| Norm squared relative to 1 | $6.66\times10^{-16}$ | $10^{-12}$ | Pass |
| Energy relative to exact initial energy 0 | $2.36\times10^{-16}$ | $10^{-12}$ | Pass |
| Full-matrix identity $i[H,n]=gY$ | 0 | $10^{-12}$ | Pass |
| Occupation derivative from state versus $g\langle Y\rangle$ | $1.39\times10^{-17}$ | $10^{-12}$ | Pass |
| Central finite difference at $t=0.7$, step $10^{-5}$ | $4.52\times10^{-12}$ | $10^{-9}$ | Pass |

These checks support implementation consistency with the defined Hamiltonian. They do not supply independent empirical evidence for the postulate. The resulting motion is coherent closed-system evolution, not relaxation to a ground state: a time-independent Hamiltonian conserves the energy expectation, and no environment, cooling rule, dissipation, or measurement-selection mechanism is supplied. A uniform expected adjacency matrix likewise does not specify the geometry of an individual graph-basis outcome.

## 7. What the matter dimension can select

### 7.1 Prespecified aligned-sector null

Equation (6) holds for every positive integer $q$, so the aligned-sector edge Hamiltonian is identical at $q=887,888,889$ when the couplings are fixed independently of $q$. The recorded [matter-dimension null](QNET-001-artifacts/results/q_null.json) is this exact statement. It is not the result of three large full-matter simulations. In particular, no array with $888^N$ matter amplitudes was constructed.

### 7.2 Supplemental full ground-energy theorem

**Theorem 2.** For the Hamiltonian (1), finite $N$, every positive integer $q$, and $J\ge0$, with $U$, $\mu$, $V$, $J$, and $g$ fixed independently of $q$,

$$
\boxed{E_0(H;q)=E_0(H_{\mathrm g}).}
\tag{10}
$$

Here $E_0$ denotes the minimum eigenvalue and $H_{\mathrm g}$ is the edge Hamiltonian obtained by replacing every matter swap by $+1$. The result holds for arbitrary real $g$ and does not require the static limit.

**Proof.** Restoring the tensor factors, subtract the aligned edge Hamiltonian from the full Hamiltonian:

$$
H=I_{\mathrm m}\otimes H_{\mathrm g}
+J\sum_{i<j}(I_{\mathrm m}-S_{ij})\otimes n_{ij}.
\tag{11}
$$

Since $S_{ij}$ is a Hermitian involution, its eigenvalues belong to $\{-1,+1\}$, so $I_{\mathrm m}-S_{ij}$ is positive semidefinite. The number operator $n_{ij}$ is also positive semidefinite. Their tensor product is therefore positive semidefinite, and multiplying by $J\ge0$ preserves this property. The summands need not commute for their sum to be positive semidefinite. Thus, for every normalized full state $\lvert\Psi\rangle$,

$$
\langle\Psi\rvert H\lvert\Psi\rangle
\ge
\langle\Psi\rvert I_{\mathrm m}\otimes H_{\mathrm g}\lvert\Psi\rangle
\ge E_0(H_{\mathrm g}),
$$

which proves $E_0(H;q)\ge E_0(H_{\mathrm g})$.

Conversely, choose a normalized edge ground state $\lvert\chi_0\rangle$ of $H_{\mathrm g}$ and any normalized $\lvert\phi\rangle\in\mathbb C^q$. Equation (6) implies that every added term in equation (11) annihilates

$$
\lvert\Phi_0\rangle
=\lvert\phi\rangle^{\otimes N}\otimes\lvert\chi_0\rangle.
$$

Consequently $H\lvert\Phi_0\rangle=E_0(H_{\mathrm g})\lvert\Phi_0\rangle$, giving the reverse inequality and proving equation (10). ∎

The theorem rules out a special **ground-energy-selection role** for $q=888$ within this exact Hamiltonian and the stated coupling assumptions. It does not imply that all ground-state degeneracies, excited spectra, finite-temperature entropies, or dynamics from arbitrary entangled matter states are independent of $q$. It also does not cover negative $J$ or couplings assigned an explicit $q$-dependence. The local matter state count has not, in this model, been converted into a demonstrated spatial dimension.

## 8. Evidence audit and limitations

The study keeps mathematical identities, finite numerical results, and physical claims separate. A successful commutator check confirms the defined evolution rule; it is not a measurement of spacetime. An exact ground-state counterexample rejects a selection claim in its specified regime; it is not a universal statement about all quantum graph theories.

**Table 6. Claim-level evidence status.**

| Claim or obligation | Status | Basis or remaining gap |
|---|---|---|
| A well-defined finite Hamiltonian and unitary connection rule | **Demonstrated** | Hermiticity, finite-dimensional evolution, and exact commutator |
| The reported small-$N$ static census | **Demonstrated** | Complete integer enumeration on the frozen grid |
| Static degeneracy across regular triangle-free geometries | **Demonstrated** | Equation (9) and the constructed reference checks |
| Unique connected extended 3D ground geometry at $\mu=2$, $g=0$, $U=V=J=1$ | **Rejected** | Exact connected-cycle and disconnected-cycle ground states |
| Different aligned-sector dynamics at $q=887,888,889$ | **Rejected** | Exact invariant-sector reduction |
| A distinct full ground energy selected by $q=888$ for fixed couplings and $J\ge0$ | **Rejected** | Theorem 2 |
| Derivation of the proposed Hamiltonian from EFMW | **Hypothesis/postulate, not derived** | No derivation fixes these terms and couplings |
| An emergent 3D phase at some finite $g$ or in general states | **Unresolved** | No suitable finite-size phase or state-selection analysis |
| Emergent 3+1 spacetime, Lorentz symmetry, or gravity | **Unresolved / not demonstrated** | No continuum, causal, relativistic, or gravitational derivation |
| Novelty relative to prior literature | **No novelty claim** | Conceptual adjacency to quantum graphity; no comprehensive search |

Several limitations are decisive. Only $N=3$ is evolved as a complete edge-state vector, and only $N\le6$ is exhaustively enumerated. The 216-vertex references are ordinary graph-matrix calculations, not a quantum simulation of $2^{23220}$ edge states. The finite samples do not provide a scaling regime, an emergent spatial metric, a robust dimension estimator, or evidence of a stable low-energy continuum.

The anti-circularity safeguards are correspondingly narrow and explicit. Neither $q=888$ nor a target dimension sets a fitted coupling or numerical acceptance threshold. The cubic graph is not counted as an emergent success. Static minima are not equated with real-time attraction. Multiple checks of the same operator identities are not counted as independent physical evidence. Negative and null results are retained rather than removed through parameter retuning.

The test suite includes an adjacency-matrix check against the bitset graph calculations at $N=4$, as well as hand-derived small-system energies. These are useful cross-checks of implementation paths and mathematical consistency within the same AI-assisted study. They are not independent replication by another research group.

## 9. Reproducibility and AI-assistance disclosure

The [reproducibility companion](QNET-001-artifacts/README.md) preserves the original protocol, implementation, tests, complete JSON results, manifest, and checksums. The recorded environment is Python 3.12.14 with NumPy 2.3.5. The implementation uses Python standard-library facilities and NumPy; no external repository code was executed and no package was installed in the recorded run.

From the repository root, with the recorded dependencies already available:

```sh
cd QNET-001-artifacts
sha256sum -c CHECKSUMS.sha256
python qnet.py --output reproduced-results
python -m unittest -v test_qnet
```

The separate output directory preserves the original numerical results during regeneration, and the module-based test invocation avoids overwriting the recorded test report. Runtime metadata and floating-point details can vary across environments; integer static results and the stated numerical tolerances are the appropriate scientific comparisons. The original [test report](QNET-001-artifacts/results/tests.json) records eight tests run, all successful, with no failures, errors, or skipped tests.

**Table 7. Companion contents.**

| Artifact | Purpose |
|---|---|
| [Original README](QNET-001-artifacts/README.md) | Recorded study report and original interpretation |
| [Protocol](QNET-001-artifacts/PROTOCOL.md) | Frozen inputs, operations, tolerances, and decision rules |
| [Implementation](QNET-001-artifacts/qnet.py) | Original graph enumeration, dynamics, and reference diagnostics |
| [Tests](QNET-001-artifacts/test_qnet.py) | Eight implementation and analytic consistency tests |
| [Requirements](QNET-001-artifacts/requirements.txt) | Exact NumPy version used |
| [Static results](QNET-001-artifacts/results/static.json) | Every ground graph mask and all static histograms |
| [Quantum results](QNET-001-artifacts/results/quantum.json) | Full edge Hamiltonian, eigenvalues, probabilities, observables, and residuals |
| [Geometry results](QNET-001-artifacts/results/geometry.json) | Reference distances, growth, and complete Laplacian spectra |
| [Matter-dimension null](QNET-001-artifacts/results/q_null.json) | Exact restricted-sector statement and its scope |
| [Test results](QNET-001-artifacts/results/tests.json) | Recorded test outcomes |
| [Manifest](QNET-001-artifacts/results/manifest.json) | Runtime information and protocol, source, and result hashes |
| [Run summary](QNET-001-artifacts/run_summary.json) | Compact numerical results |
| [Checksums](QNET-001-artifacts/CHECKSUMS.sha256) | Integrity checks for the preserved source and result files |

**AI-assistance disclosure.** This research note and its underlying local study were prepared with AI assistance in mathematical derivation, implementation, computation, checking, and editorial preparation. The computations and consistency checks belong to that same assisted workflow. They are not represented as independent replication, experimental validation, or external peer review.

## 10. Conclusion and next proof obligation

QNET-001 supplies a precise finite quantum connection rule and reproducible checks of its implementation. It does not supply a demonstration of 3+1-dimensional emergence. The strongest results are exact: static cycle ground states obstruct unique connected three-dimensional ground selection at one frozen parameter point; equal-degree, triangle-free geometries are indistinguishable to the specified static energy; and the full ground energy cannot single out $q=888$ when $J\ge0$ and the couplings are fixed independently of $q$.

A justified next step would specify a derived or independently motivated correlation-sensitive interaction and a state or ensemble selection mechanism before another dimensionality calculation. The first acceptance gate should address the explicit cycle/disconnected-cycle and regular triangle-free counterexamples in the regime being claimed. A proposed modification should fail that gate if the relevant blind spots remain, or if three-dimensional structure is supplied as an initial lattice or success-fitted target. Passing the gate would still require a separately frozen finite-size, stability, dimension-estimation, and low-energy-physics program before any dimensional-emergence claim. That proposed work was not executed in QNET-001.

## References

1. **QST-001, §8.** `enuminous/Quantum-Gravity`, pinned revision `4d533344e2f05c365b24acb9616e8a303fcc4587`. [Pinned source](https://github.com/enuminous/Quantum-Gravity/blob/4d533344e2f05c365b24acb9616e8a303fcc4587/QST-001.md). Cited for the nominated local matter dimension, not for the Hamiltonian introduced in this paper.

2. **Tomasz Konopka, Fotini Markopoulou, and Simone Severini.** “Quantum Graphity: A Model of Emergent Locality.” *Physical Review D* **77**, 104029 (2008). [DOI: 10.1103/PhysRevD.77.104029](https://doi.org/10.1103/PhysRevD.77.104029); [arXiv:0801.0861](https://arxiv.org/abs/0801.0861).
