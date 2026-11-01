# Referee report on retrocausal access via parallel qudit sheets

**Date:** 1 November 2026  
**Prepared for publication by:** Matthew Chenoweth Wright / Monolithic LLC, with AI-assisted technical analysis and reproducible algebra checks.  
**Attribution supplied with the material:** John Bloke, @BlokeMan00 on X.  
**Review status:** Public technical commentary in referee-report form; not a journal-appointed review or an editorial decision.  
**Reviewed version:** Two supplied image files and the accompanying explanatory paragraph, identified below. No complete manuscript, source code, experimental record, or canonical post URL was supplied. Authorship and posting dates have not been independently authenticated.

## Abstract

The reviewed material proposes that time emerges from quantum gates, that localized matrix inversion opens retrocausal paths, and that block-diagonal quantum sectors support access to parallel historical configurations. It assigns the unitary anomalous Master Ward Identity (uAMWI) the role of a causality firewall that cancels paradox-producing amplitudes. This report finds that these physical conclusions do not follow from the supplied mathematics. The stated conversion of a lower-triangular matrix into an upper-triangular matrix by inversion is false in a fixed basis. Replacing a time difference by its negative inside a squared interval does not change that interval. Exact dynamical decoupling forbids inter-sector transfer, while a coupling that enables transfer requires a separate protection argument. The cited uAMWI literature does not establish the proposed paradox-cancellation mechanism. The diagrams can motivate a model of quantum sectors and controlled state transfer, but they do not establish physical access to the past, immunity to noise, or paradox-free time travel. Exact finite-dimensional checks accompany the report; their scope is explicitly limited.

## 1. Recommendation, evidence boundary, and review protocol

**Recommendation: the supplied material is not acceptable as a proof of physical time travel. Substantial mathematical reconstruction is required before its physical claims can be evaluated.** This is a judgment about the supplied argument, not a general impossibility theorem for every conceivable retrocausal theory.

The frozen inputs are:

| ID | Supplied item | Location within this repository |
|---|---|---|
| A | *Beyond the Single Timeline: Retrocausal Access via Parallel Qudit Sheets* | [Poster A](Bloke-Parallel-Qudit-Sheets-Review-2026-11-01/poster-a.jpeg) |
| B | *Reformulating Time Travel: From Emergent Time to Retrocausal State Reconfiguration* | [Poster B](Bloke-Parallel-Qudit-Sheets-Review-2026-11-01/poster-b.jpeg) |
| C | Accompanying explanatory paragraph attributed by the submitter to John Bloke | Preserved verbatim in the [input manifest](Bloke-Parallel-Qudit-Sheets-Review-2026-11-01/inputs.json) |

The manifest records the original image filenames, byte counts, and SHA-256 hashes. The images are reproduced as objects of critical review. Attribution does not establish permission for unrelated reuse. The report evaluates the displayed statements without silently replacing an inverse by a transpose, supplying an omitted Hamiltonian, or interpreting an undefined threshold as an established physical law.

The following operations and criteria define this bounded review. They are ordinary mathematical and source checks, not a claim that a complete automated Monolithic Zoo suite or Lean formalization has been executed.

| Operation | Input and transformation | Criterion for support | Result |
|---|---|---|---|
| Matrix inverse check | Invert a nonsingular lower-triangular matrix in the displayed fixed ordering | Claimed triangular reversal must follow from inversion | **Rejected as written**; section 2 |
| Interval and signature check | Substitute negative time difference; distinguish metric signature from orientation | The operation must establish more than an unchanged interval or a convention change | **Rejected as a sufficient derivation**; section 3 |
| Sector-transfer check | Evaluate the cross-sector block of the evolution operator | Transfer and protection must follow from specified dynamics | Decoupled no-transfer result **demonstrated**; protected handoff **unresolved** |
| Source comparison | Compare the firewall claim with the original uAMWI papers | A stated result must identify the relevant histories and prove cancellation | Claimed attribution **unsupported**; section 5 |
| Stability check | Distinguish global unitarity from reduced-system coherence | A noise model and bound must support the promised immunity | **Unresolved**; a general unitarity-implies-immunity inference is **rejected** |
| Physical interpretation check | Compare register labels with measurable temporal relations | Historical access must have operational content beyond preparing a represented configuration | **Hypothesis**, not demonstrated |

Here, **rejected** identifies a false step or invalid inference; **unresolved** identifies a missing specification or proof. Neither label is applied to the author's competence or intentions. EFMW is not used as an assumed physical truth in this review.

## 2. Matrix inversion does not reverse triangular causal support

Poster B, section 2C, depicts a lower-triangular Møller operator becoming upper-triangular under inversion. For ordinary finite-dimensional matrices in a fixed basis this is false. For any scalar $a$,

$$
M=\begin{pmatrix}1&0\\a&1\end{pmatrix},\qquad
M^{-1}=\begin{pmatrix}1&0\\-a&1\end{pmatrix}.
$$

Both products equal the identity. For $a\ne0$, the inverse is lower-triangular and is not upper-triangular.

The general finite-dimensional result follows by forward substitution. For an invertible lower-triangular matrix $L$, solve $Lx=e_j$. Its diagonal entries are nonzero. In row order, the first $j-1$ components of $x$ must vanish. Applying this argument to every column of $L^{-1}$ proves that the inverse is lower-triangular. If the displayed operator were strictly triangular with a zero diagonal, a finite-dimensional inverse would not exist in the first place.

Transposition, an adjoint, or a reversal of the basis ordering can change a triangular pattern. Those are different operations. Merely relabelling the order also does not demonstrate a physical reversal of causal influence. An infinite-dimensional alternative would require a specified operator domain, inverse, boundary conditions, and support theorem; it cannot be inferred from the finite matrix sketch.

The related expression $E'=UEU^\dagger$ is mathematically legitimate when the objects are appropriately defined. Unitary conjugation preserves the spectrum. It does not, by itself, establish that a retarded response has become advanced: causal support depends on the localization of observables and the meaning of the transformation. An active dynamics and a passive basis change must be distinguished.

**Required repair:** Supply the actual transformation and prove its effect on the support of a response kernel in fixed physical coordinates. Replacing the inverse by an adjoint would require a new derivation, not just a typographical correction.

## 3. A squared interval and a metric signature do not select the past

The proposed reversed interval contains a term of the form

$$
-c_{\mathrm{eff}}^2(-\Delta t)^2
=-c_{\mathrm{eff}}^2(\Delta t)^2.
$$

The sign replacement leaves this term exactly unchanged. This does not disprove time-reversal symmetry. It shows that the displayed scalar interval cannot distinguish the claimed forward and reverse orientations.

Likewise, replacing a nondegenerate metric $g$ by $-g$ preserves its null cone because $g(v,v)=0$ if and only if $(-g)(v,v)=0$. Overall sign convention is not a choice of future direction. If instead only the single negative eigenvalue of a diagonal Lorentzian form is changed to positive while the others remain positive, the result is positive definite rather than a reversed Lorentzian time direction. Poster B's language about one eigenvalue and its displayed spectrum require clarification.

The centered construction $K=-\tfrac12 JD^{(2)}J$ also needs its input defined; $D^{(2)}$ here denotes the entrywise squared dissimilarity matrix, rather than an unspecified matrix square. For Euclidean distances, centered points $x_i$ give $K_{ij}=x_i\cdot x_j$, hence

$$z^T Kz=\left\|\sum_i z_i x_i\right\|^2\ge0.$$

A negative eigenvalue therefore requires inputs outside that Euclidean-distance case. Signed spacetime separations or other dissimilarities may produce an indefinite matrix, but their physical meaning must be supplied. A finite Gram matrix with one negative eigenvalue can support a conditional pseudo-Euclidean embedding; it does not by itself construct a smooth spacetime, its time orientation, or its dynamics.

The gate sequence $\psi_{n+1}=U\psi_n$ supplies an evolution indexed by an already ordered integer. A claim that physical time emerges from that sequence still needs an operational clock, a continuum limit or an explicitly discrete alternative, and a derivation of the relevant causal structure. The printed eikonal expression lacks sufficient definitions and boundary data to provide that derivation here.

**Status:** Interval invariance is demonstrated. The claimed emergence and controllable reversal of physical time remain unresolved.

## 4. Dynamically isolated sectors cannot exchange a traveler

Let the proposed sectors be an orthogonal direct sum,

$$\mathcal H=\mathcal H_\alpha\oplus\mathcal H_\beta,$$

with projectors $P_\alpha$ and $P_\beta$. If evolution remains block diagonal,

$$U=U_\alpha\oplus U_\beta,$$

then

$$P_\beta U P_\alpha=0.$$

Thus a state initially confined to $\alpha$ cannot transfer to $\beta$. This conclusion follows from exact dynamical isolation, independently of the names assigned to the sectors.

A block-diagonal density operator is weaker than this assumption. It can be written as $\rho=p\rho_\alpha\oplus(1-p)\rho_\beta$ for normalized sector states. It specifies no cross-sector coherence at that instant; it does not specify the Hamiltonian. If each displayed block were separately normalized without weights, their direct sum would have trace two, so normalization conventions also need stating.

A coupling can make transfer possible. For example, on two one-dimensional sectors,

$$
U(\theta)=\begin{pmatrix}\cos\theta&-i\sin\theta\\-i\sin\theta&\cos\theta\end{pmatrix}
$$

is unitary and transfers an initial $\alpha$ state into $\beta$ with probability $\sin^2\theta$. At $\theta=\pi/2$ transfer is complete. This is an ordinary quantum transition. During generic intermediate stages, the state acquires off-diagonal coherence in this sector basis.

The posters do acknowledge a later firewall rupture. That acknowledgment means the model must explain which protection persists when isolation is lifted. The no-transfer theorem does not rule out controlled couplings; it rules out using uninterrupted decoupling as the explanation for both transfer and protection.

The labels also change roles: $\alpha$ denotes the untouched original present, while the handoff is described as entering a historical $\alpha$ sector. A distinct destination needs a distinct definition. If the same physical sector is intended, the report's claimed protection must be reconciled with its alteration. If a separate historical representation is intended, its relation to the original past must be established.

**Required repair:** Define the world, traveler, destination, and any control system; specify whether they combine by direct sum or tensor product; provide the complete channel; and prove an explicit preservation condition for the original world's observables.

## 5. The uAMWI does not supply the asserted paradox firewall

The uAMWI is an established construction in algebraic quantum field theory. Brunetti, Dütsch, Fredenhagen, and Rejzner formulate it as a condition on quantum symmetries and anomalies. The original paper assumes globally hyperbolic dynamical spacetimes with a chosen time orientation, and derives a time-slice result within that setting. The underlying algebraic construction has genuinely nonperturbative aspects. [1, sections 1, 2.1, 5.2 and 6]

The ideal $I_\zeta$ introduced following Axiom 3 encodes relations annihilated in representations satisfying the specified identity; the corresponding quotient imposes those relations. Its appearance does not identify paradox-producing histories or prove that their transition amplitudes cancel. The follow-up paper relates the anomaly's cocycle condition to Wess–Zumino and BV consistency structures, using perturbation theory. [1, Axiom 3; 2]

The posters' light-cone pinch, null-amplitude, and rupture claims require an additional theorem. None is supplied. In particular, the input spacetime's causal restrictions cannot be reused as independent evidence that a proposed extension permitting new temporal paths is automatically consistent.

For a valid firewall construction, the author would need to define the candidate histories, identify the relevant operator or distribution for each, prove membership of the prohibited contribution in the chosen ideal, and show that the resulting theory has appropriate nontrivial positive states and unitary dynamics. A singular product of distributions is not, merely by being singular, a zero transition amplitude. Any claimed cancellation requires a specified prescription and derivation.

**Status:** The uAMWI itself is established literature. Its proposed application as a time-travel paradox filter is an unsupported additional hypothesis.

## 6. Global unitarity does not establish noise immunity or a handoff threshold

Global unitary evolution does not guarantee coherence of a subsystem. An exact example starts with a qubit in $|+\rangle$ and an environment qubit in $|0\rangle$. A controlled-NOT produces the pure entangled state

$$|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2.$$

The system's reduced state is then $I/2$, with purity $1/2$, although the joint state still has purity one. This is ordinary loss of local coherence under globally unitary dynamics. It does not establish a fundamental collapse process; it refutes an unrestricted inference from global unitarity to subsystem noise immunity.

The advertised stability therefore needs a specified subsystem, environment, noise channel, observable, time interval, and quantitative bound. Block-diagonal notation alone supplies none of these.

The thresholds involving $c_{\mathrm{eff}}\ge1$ and $c(\Phi_{\mathrm{eff}})\ge1$ also lack adequate definitions. If the former is a speed, its comparison to one requires stated units or normalization. A numerical threshold, a gradient of mutual information, and a geodesic sketch do not substitute for a metric, its connection, boundary conditions, and a dynamically derived transition rule.

**Status:** The claimed immunity and handoff thresholds are unresolved; the unqualified inference from unitarity to local coherence preservation is rejected.

## 7. What survives, and what has not been established

Direct-sum decompositions, unitary state transfer, indefinite bilinear forms, and algebraic quotients are legitimate mathematical tools. Their roles here are adjacent to familiar constructions; the report makes no exhaustive priority claim about the proposed combination.

A finite quantum simulation could represent two histories and transfer a state between registers or sectors. Such a simulation would demonstrate its implemented operations. Assigning one register a historical date would not establish that the register is that physical era, or that information has influenced an earlier physical event.

The report identifies three assumption-to-conclusion gaps: protection is inferred from stipulated isolation even while transfer requires lifting it; historical access is inferred from labels assigned to destination states; and paradox suppression is inferred by assigning the required meaning to an algebraic ideal. These are missing derivations, not independent validations.

No experimental evidence for temporal access is supplied. The mathematically rejected steps cannot be retained as proofs. The proposed physical interpretation, revised transfer mechanism, and stability properties remain hypotheses or unresolved obligations.

## 8. Reproduction and a discriminating next submission

The [Python script](Bloke-Parallel-Qudit-Sheets-Review-2026-11-01/checks.py) uses only the standard library and exact rational arithmetic. Run from the repository root:

```bash
python3 Bloke-Parallel-Qudit-Sheets-Review-2026-11-01/checks.py
```

It reproduces seven checks: two-sided inverse verification, interval sign invariance, block-diagonal no-transfer, an exact unitary sector swap, the absence of Lorentzian null directions after changing only the negative diagonal sign, unchanged nullness under overall metric sign reversal, and reduced mixedness after a globally unitary entangling operation. It also verifies both exhibit hashes. The [recorded output](Bloke-Parallel-Qudit-Sheets-Review-2026-11-01/checks.json) is deterministic. A check's `PASS` means that the review's stated algebraic check reproduced, not that time travel passed a test. General claims are supported by the arguments above, not inferred from a finite test count. No Lean proof or physical experiment was run.

A revised submission should specify a finite model first: Hilbert spaces and observables; the circuit or Hamiltonian; the proposed temporal observable; the transfer operation; and an explicit preservation condition. Freeze the definitions and tolerances before examining results.

The first acceptance criterion is internal: demonstrate nonzero transfer and the claimed protection under the same fully specified dynamics, without replacing an inverse by a transpose or assuming the requested conclusion. Failure is a contradiction of those conditions or dependence on an unstated operation.

The separate physical criterion is operational: identify an observable distinction from ordinary forward evolution that prepares or accesses a representation of an earlier configuration. A circuit that only reproduces stored historical data meets the simulation claim, not the physical time-travel claim. Without that distinction, the appropriate presentation remains a speculative quantum-information model with a temporal interpretation.

## References

1. R. Brunetti, M. Dütsch, K. Fredenhagen, and K. Rejzner, *The Unitary Master Ward Identity: Time Slice Axiom, Noether’s Theorem and Anomalies*, **Annales Henri Poincaré 24**, 469–539 (2023); published online 11 August 2022. [DOI: 10.1007/s00023-022-01218-5](https://doi.org/10.1007/s00023-022-01218-5). Specific locations used: section 2.1 (spacetime assumptions), Axiom 3 and the following definition of $I_\zeta$, and Theorem 6.1 (time slice).
2. R. Brunetti, M. Dütsch, K. Fredenhagen, and K. Rejzner, *Unitary, Anomalous Master Ward Identity and its Connections to the Wess–Zumino Condition, BV Formalism and $L_\infty$-algebras*, **Annales Henri Poincaré 25**, 2547–2583 (2024); published online 12 December 2023. [DOI: 10.1007/s00023-023-01388-w](https://doi.org/10.1007/s00023-023-01388-w). Specific locations used: abstract, introduction, and section 2.2.
3. Supplied posters and accompanying text attributed to John Bloke (@BlokeMan00), frozen for this review on 1 November 2026. [Exhibits and input manifest](Bloke-Parallel-Qudit-Sheets-Review-2026-11-01/inputs.json). This is an artifact-specific attribution; no canonical X post URL or complete manuscript is asserted.
