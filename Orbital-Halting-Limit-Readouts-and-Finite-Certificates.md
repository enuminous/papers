# Orbital and the Halting Problem: Limit Readouts, Finite Certificates, and the Boundary of Computability

**Matthew Chenoweth Wright**  
Monolithic LLC · 19 October 2026 · Version 1.0

**Status:** Source-level mathematical analysis and expository deductions. No new independent Lean build, physical experiment, or universal halting solver is reported.  
**Work examined:** C. Forrester's *Orbital*, commit [`59bb0c1cc5dcfd88663c92b0117121f61e2223bf`](https://github.com/CasimirKnights/Orbital/tree/59bb0c1cc5dcfd88663c92b0117121f61e2223bf).

## Abstract

Orbital connects a computation's stopping event with a modeled phase observable, a normalized Boolean pin, a scalar kernel, and an exact first-hit address. Its universal readout is defined by a limit over arbitrarily long computation prefixes. We examine whether these constructions establish progress toward a general solution of the halting problem. The source contains both an equivalence between the limit readout and halting and an explicit theorem that the corresponding predicate is noncomputable. These results are compatible: a mathematical specification can identify every correct answer without supplying a terminating algorithm that obtains it. We explain the finite-prefix obstruction, derive elementary consequences concerning computable convergence bounds and finite-valued address specifications, and separate finite decoding from acquisition of the decoded record. We then formulate a constructive research target: sound, mechanically checkable certificates for selected halting or nonhalting instances. The analysis preserves Orbital's possible value for formal representations and restricted machine analysis while rejecting the inference that its current limit construction supplies a universal finite halting decider. Physical hypercomputation remains a separate hypothesis requiring an explicit operational model.

**Keywords:** halting problem; limit computation; Lean 4; formal verification; nonhalting certificates; interference; de Bruijn decoding; EFMW Zoo.

## 1. Question, frozen scope, and evidence

The question is whether the examined Orbital release supplies a method that, for every finitely described program and input, terminates and correctly returns either **halts** or **never halts**. This is the ordinary algorithmic decision problem. A procedure that succeeds on a specified subclass, a mathematical object containing the answer, and a proposed physical device are different targets with different obligations.

The source was inspected at the commit above on 19 October 2026. The main files are `Hypercomputer.lean`, `Correspondence.lean`, `DeBruijn.lean`, `InfiniteAddress.lean`, and the repository README [1–5]. The archived toolchain is Lean `v4.30.0-rc1`; the dependency lock identifies Mathlib commit `9470b68e2f52705134448bb88b97d85470c06908`. The relevant Mathlib halting theorems were inspected at that revision [6].

This paper distinguishes three evidence classes:

- **Source observations:** definitions, theorem statements, proof dependencies, and explicit scope qualifications present in the pinned files.
- **Mathematical deductions:** the elementary arguments supplied below, using standard computability assumptions. These are written proofs, not newly compiler-checked additions to Orbital.
- **Research proposals:** certificate construction and physical-readout obligations that remain to be discharged.

A fresh independent Lean rebuild was not completed in the preceding audit: the toolchain launcher reported `error: failed to locate application`. That environment failure did not establish a source compilation failure. This paper performs no new build and does not upgrade the earlier verification status. The captured upstream axiom report is a separate historical artifact, not a fresh execution receipt.

Orbital is Forrester's construction. This paper contributes an interpretation of its proof boundary; it does not attribute the underlying construction to EFMW or claim that Orbital validates EFMW physics.

## 2. The ordinary decision problem and its limit approximation

Let $c$ be a code for a partial-recursive program and $n$ its input. Write

$$
H(c,n)=
\begin{cases}
1,&\text{if the computation terminates},\\
0,&\text{otherwise}.
\end{cases}
$$

There is no total computable function equal to $H$ on all program-input pairs. Mathlib supplies the stronger fixed-input formulation `ComputablePred.halting_problem`: even for a fixed input $n$, the halting predicate over arbitrary program codes is not computable. It also formalizes that halting is recursively enumerable and its complement is not [6]. Turing's work provides the foundational historical setting [7]; the exact formal result used by Orbital is the Mathlib theorem.

Nevertheless, one can compute finite approximations. For an ordinary effective simulation, define

$$
b_t(c,n)=
\begin{cases}
1,&\text{if a halt has been observed by stage }t,\\
0,&\text{otherwise}.
\end{cases}
$$

Every finite-stage value is computable, the sequence is monotone, and

$$
\lim_{t\to\infty}b_t(c,n)=H(c,n).
$$

If the program halts, the sequence eventually becomes permanently 1. If it never halts, the sequence is 0 throughout. Thus the correct answer exists as a limit for every input, while there is no general effective stopping rule that announces when an observed 0 is permanently correct. This distinction is central to limiting recursion [8].

For any finite observation horizon $T$, a program that halts later and one that never halts can both produce the observed history $0,\ldots,0$. That observation alone cannot distinguish them. This finite-history example illustrates the problem; the general impossibility theorem also covers algorithms that inspect the program's source rather than merely observing its execution.

## 3. What Orbital's universal theorem actually states

In `Hypercomputer.lean`, `codeRow` uses Mathlib's bounded evaluator to represent a program as a machine in Orbital's configuration model. `code_halts_iff` connects termination of that representation with the original partial-recursive computation [1]. Its representation clock should not automatically be identified with the original program's instruction count.

The source then defines `hyperRead` by `limUnder atTop` applied to the sequence of stop pins. The core statements are:

| Source identifier | Mathematical content | Scope |
|---|---|---|
| `pin_tendsto` | The pin converges to 1 for halting programs and 0 otherwise | A convergence statement |
| `hyperRead_decides` | The readout equals 1 exactly when the encoded program halts | An equivalence of propositions |
| `hyperRead_not_computable` | The predicate that this readout equals 1 is not computable | Explicit universal-decision obstruction |
| `spherical_unit_base_hypercomputer` | Packages kernel convergence, Boolean output, halting equivalence, and noncomputability | A combined mathematical specification |

The noncomputability proof transports the assumed computability of the readout predicate through the halting equivalence and invokes Mathlib's halting theorem. It is therefore not an incidental caveat added by an external reviewer: the obstruction is part of the packaged theorem [1,6].

The Lean keyword `noncomputable` alone would not prove that a function has no alternative computable implementation. Here the additional theorem is decisive. In this source, the name `hyperRead_decides` expresses exact mathematical classification; it does not establish an executable decision procedure.

Likewise, “at $\omega$” identifies a limiting or ordinal construction in the formalization. It does not, by itself, specify an experiment that completes infinitely many computational stages in finite laboratory time.

## 4. Why an effective convergence guarantee would supply the missing decider

The following elementary consequence makes the missing algorithmic resource explicit. It is a standard consequence of undecidability, included for explanation rather than as a novelty claim.

**Proposition 1 — No total computable convergence bound.** For the computable binary sequence $b_t$ above, there is no total computable function $m(c,n,k)$ such that, for every $c,n,k$ and every $t\ge m(c,n,k)$,

$$
|b_t(c,n)-H(c,n)|\le 2^{-k}.
$$

**Proof.** If such an $m$ existed, compute $t=m(c,n,2)$ and then compute $b_t(c,n)$. Both $b_t$ and $H$ are binary. Their difference is therefore either 0 or 1, and a difference at most $1/4$ must be 0. This computes $H$ for every input, contradicting the halting theorem. $\square$

The bound was allowed to depend on the entire program and input. The obstruction is not merely the absence of one fixed waiting time for all programs.

**Corollary 1 — A guaranteed computable approximate readout would also decide halting.** Suppose a total computable procedure returned a rational $r(c,n)$ satisfying

$$
|r(c,n)-H(c,n)|<\frac12
$$

for every input. Thresholding $r$ at $1/2$ would return the exact halting answer, contradicting undecidability. This concerns a guaranteed ordinary computable readout; it is not a claim about an unspecified physical device or an unspecified statistical error model.

Consequently, a useful claim about accessing Orbital's limit must identify the operation that obtains it. Supplying a computable finite-time guarantee with these universal correctness properties would itself supply the forbidden ordinary decider.

## 5. The kernel preserves the stop information supplied to it

Orbital's configuration model makes the distinction between an active and stopped configuration explicit. The clock advances during activity and stays fixed at a stop. Its normalized pin is

$$
D=1-\frac{\Delta^2}{d(p)^2},
$$

where the positive clock increment $d(p)$ equals the defect $\Delta$ on an active transition, while $\Delta=0$ at a stop. The source identifies $D$ with the stopped-state indicator [2].

For the stated scalar kernel

$$
K(u)=\frac{\pi^4}{96}(32u^3-24u^2+1),
$$

substitution gives

$$
\frac{K((1-D)/4)}{\pi^4/96}=\frac{3D-D^3}{2}=D
\qquad\text{for }D\in\{0,1\}.
$$

This identity is useful as a consistency relation between representations of the same completion event. The identity does not acquire the future halt information. That information must come from the modeled configuration or, in the universal construction, from the limiting sequence.

There is also a quantifier boundary in the interference theorem: coherence **for every phase parameter** characterizes a stopped configuration. A single observed intensity at a selected phase is not automatically an implementation of that universally quantified statement [2]. A physical measurement claim must specify the phase selection, precision, and error guarantees that connect its instrument to the theorem.

## 6. Finite decoding and the finite-valued infinite word

The finite scanner in `DeBruijn.lean` has a precise conditional specification. If the first stop occurs at address $\tau$, a prefix contains it, and enough pages can be scanned, then

$$
\tau<N,\qquad \left\lfloor\frac{\tau}{32}\right\rfloor<\mathrm{fuel}
\quad\Longrightarrow\quad
\operatorname{scan}(\operatorname{word}(N),\mathrm{fuel},0)=\operatorname{some}(\tau).
$$

The covered first-hit word is $2^\tau$. A verified 32-position de Bruijn lookup recovers the position inside its nonzero page [3]. Starting at page zero, the implemented sequential scan must reach page $\lfloor\tau/32\rfloor$; the local lookup theorem does not supply an end-to-end complexity bound for obtaining the word or executing the original source.

The implication cannot be reversed by interpreting every `none` as nonhalting. A too-short prefix or insufficient fuel can also return no address. In fact, the source's finite “reads nothing” theorem assumes absence of a stop within the inspected prefix, not an independently acquired proof of absence at every future time [3].

`InfiniteAddress.lean` removes the chosen horizon mathematically by taking the supremum over all finite first-hit words. Its results imply

$$
W_\infty(c,n)=
\begin{cases}
2^\tau,&\text{if the represented computation first stops at }\tau,\\
0,&\text{if it never stops}.
\end{cases}
$$

The source proves that this value is never the infinite top element, despite its definition by an infinite supremum [4]. That is a useful structural fact. It does not imply that its finite value can be computed uniformly from the program.

**Proposition 2 — Finite output does not imply computable acquisition.** There is no total ordinary computable procedure returning the exact natural-number value $W_\infty(c,n)$ for every encoded program and input.

**Proof.** If such a procedure existed, compute its output and test whether it is zero. By the displayed characterization, nonzero means halting and zero means nonhalting. This decides $H$, a contradiction. $\square$

This separates an exact address specification from a procedure for acquiring the address. It also explains why the finite bit length of each particular output cannot, by itself, establish a universal algorithm.

## 7. A constructive target: sound certificates for selected machines

The README describes charge/drain observations as an experiment under investigation and proposes obtaining a finite reason that certain machines can never reach a halt [5]. That is a legitimate research direction. An empirical association with observed stopping events is not yet a theorem; the README also acknowledges drain behavior away from stops.

One precise target is an inductive invariant. Let $S$ be the configuration space, $T:S\to S$ the transition function, $s_0$ the initial configuration, and $F\subseteq S$ the halted configurations. A candidate predicate $I$ should satisfy

$$
I(s_0),
\qquad
\forall s,\ I(s)\Rightarrow I(T(s)),
\qquad
\forall s,\ I(s)\Rightarrow s\notin F.
$$

**Proposition 3 — Invariant nonhalting certificate.** Under these three hypotheses, $T^t(s_0)\notin F$ for every natural number $t$.

**Proof.** Induction gives $I(T^t(s_0))$ at every stage. The third hypothesis then excludes membership in $F$. $\square$

A charge/drain invariant could instantiate this pattern if its definitions and preservation law were proved for the actual machine transitions. The observation interface would then help formulate or verify a substantive nonhalting argument.

For mechanization, the deliverable should include a finite certificate format, a terminating checker, and a soundness theorem

$$
\operatorname{Check}(c,n,\pi)=\mathrm{true}
\quad\Longrightarrow\quad H(c,n)=0.
$$

Universal completeness must not be silently added to this target.

**Proposition 4 — No effective sound certificate system complete for all nonhalting instances.** A total computable checker over effectively enumerable finite certificates cannot be both sound and complete for nonhalting of arbitrary programs.

**Proof.** Completeness would allow enumeration of certificates until one is accepted for any nonhalting input. In parallel, simulate the program to recognize a halt. Soundness prevents contradictory answers; completeness ensures that one of the two searches eventually succeeds. This yields a total halting decider. Equivalently, it contradicts Mathlib's result that the complement of the halting predicate is not recursively enumerable [6]. $\square$

This obstruction leaves substantial room for sound, incomplete tools and for complete deciders on precisely restricted classes. Termination proofs, nontermination invariants, symbolic execution, and specialized recurrence arguments can all settle important individual problems without deciding every possible program.

## 8. Proof obligations for a physical interpretation

A claim that a physical apparatus accesses the limit requires its own model. The mathematical theorem about ordinary algorithms does not, by itself, settle every proposal about physically realizable processes. Conversely, an infinite-limit definition does not establish that a device implements it.

An operational proposal must specify:

1. **Preparation:** how an arbitrary finite program and input are encoded without supplying a noncomputable parameter or the desired answer.
2. **Dynamics:** the physical evolution law, boundary conditions, and justification for the correspondence with the program's computation.
3. **Readout:** how a finite observation produces an answer, including the never-halting case; state the time, precision, noise, energy, and resource assumptions.
4. **Correctness:** the quantifiers governing the guarantee, including whether it is exact, probabilistic, restricted to a class, or conditional on idealizations.
5. **Independence:** a derivation and experimental program that do not assume the limit-access operation whose realizability is being claimed.

The current README explicitly separates apparatus and measurement back-action from its formalized phase observables [5]. The physical universal-decider interpretation is therefore **unresolved as a physical hypothesis**; the inference that the present formalization already establishes such an instrument is **rejected**.

If a proposed implementation can be modeled entirely by ordinary total computable preparation and readout with universal correctness, Propositions 1–2 apply. A claim beyond that model must identify and justify the additional physical resource rather than treating its existence as a consequence of the kernel identity.

## 9. Evidence status, independence, and novelty

| Claim | Status in this analysis | Reason |
|---|---|---|
| The pinned source contains a halting/readout equivalence and a noncomputability theorem | **Demonstrated** by source inspection | Both statements and the reduction to Mathlib are explicit |
| The examined source independently rebuilds in a fresh environment | **Supported but incomplete** | Upstream build material exists; the prior independent launcher attempt did not complete; no new build is reported here |
| An ordinary computable readout uniformly returns the universal halting answer | **Rejected** | Contradicts the preserved halting theorem |
| The finite decoder returns the address under its coverage and fuel hypotheses | **Supported but incomplete** as independent implementation verification | The pinned source supplies a proof; a fresh independent build remains outstanding |
| Propositions 1–4 follow under their stated mathematical hypotheses | **Demonstrated** by the deductions in this paper | Standard computability and induction arguments; not new Lean artifacts |
| Charge/drain structure yields sound certificates for specified machines | **Hypothesis/postulate** pending a concrete invariant and proof | The proposed mechanism has not been instantiated by this paper |
| A physical device obtains the universal limit answer in finite observation | **Unresolved** | An operational model and supporting evidence are missing |

The analysis is retrospective: Orbital's claims and source were known before these arguments were selected. No prospective experimental validation or new execution of named Zoo operators is claimed. Anti-circularity requires retaining the source's hypotheses, refusing to treat a supplied first-hit word as evidence that it can be acquired universally, and separating an upstream proof record from an independent rebuild.

The approximation of halting by a convergent sequence belongs to established computability theory and limiting recursion [6,8]. The Boolean kernel calculation is an elementary identity. The certificate soundness and incompleteness arguments are standard. Orbital's specific connection among source dynamics, interference, kernels, and address representations may be assessed as a particular formal construction; this paper makes no comprehensive priority determination. Recasting a known noncomputable predicate does not create a new ordinary decision algorithm.

Calculations concerning a particular Busy Beaver candidate are a separate problem. Even a rigorous stopping-time formula or residue for one named machine would not supply a universal halting decider, and would not alone prove that machine's maximality among all machines of the relevant size.

## 10. Proposed next proof and acceptance criteria

The next useful target is **one sound certificate theorem for a frozen machine or explicitly defined class**. The following is a proposed protocol, not a report of completed preregistration or testing.

| Stage | Required artifact | Success criterion | Failure or limitation |
|---|---|---|---|
| Freeze | Transition table, initial state, representation conventions, and exact claim | All inputs and semantics fixed before evaluation | Changing the machine or claim requires a new version |
| Derive | Candidate invariant or exact recurrence tied to source transitions | Initialization, preservation, and halt-exclusion proved | A sampled correlation or assumed future behavior is insufficient |
| Check | Finite certificate, terminating checker, and soundness proof | Accepted certificates imply the claimed result | Invalid certificates must not certify a claim |
| Challenge | Frozen halt/nonhalt controls and deliberately corrupted certificates | Controls behave according to the proved specification | Selected successful examples alone do not establish coverage |
| Reproduce | Pinned dependencies and independent execution receipt | A second environment reproduces the build and certificate check | Reusing a captured log does not establish a fresh run |

The minimal deliverable is a source-pinned certificate and a checked implication from its acceptance to nonhalting, or a corresponding sound termination theorem. An unsuccessful search for a certificate means that this method has not resolved the case; it does not certify the opposite outcome.

Orbital's present universal construction is a precise limit characterization with an explicit computability boundary. Its credible path to further computational results is to establish additional finite theorems for specified machines, while any physical hypercomputation proposal must meet the separate operational obligations above.

## References

1. C. Forrester. *Orbital*, `BeaverHalting/Hypercomputer.lean`, pinned commit `59bb0c1cc5dcfd88663c92b0117121f61e2223bf`. [Source](https://github.com/CasimirKnights/Orbital/blob/59bb0c1cc5dcfd88663c92b0117121f61e2223bf/BeaverHalting/Hypercomputer.lean). Principal identifiers: `code_halts_iff`, `pin_tendsto`, `hyperRead`, `hyperRead_decides`, `hyperRead_not_computable`, `spherical_unit_base_hypercomputer`, `spherical_unit_base_addressable`.
2. C. Forrester. *Orbital*, `BeaverHalting/Correspondence.lean`, same pinned commit. [Source](https://github.com/CasimirKnights/Orbital/blob/59bb0c1cc5dcfd88663c92b0117121f61e2223bf/BeaverHalting/Correspondence.lean). Principal identifiers: `coherent_iff_stopped`, `pin_eq_indicator`, `kernel_reads_pin`, `P_eq`.
3. C. Forrester. *Orbital*, `BeaverHalting/DeBruijn.lean`, same pinned commit. [Source](https://github.com/CasimirKnights/Orbital/blob/59bb0c1cc5dcfd88663c92b0117121f61e2223bf/BeaverHalting/DeBruijn.lean). Principal identifiers: `scan`, `debruijn_table_reads_tau`, `debruijn_table_reads_nothing`.
4. C. Forrester. *Orbital*, `BeaverHalting/InfiniteAddress.lean`, same pinned commit. [Source](https://github.com/CasimirKnights/Orbital/blob/59bb0c1cc5dcfd88663c92b0117121f61e2223bf/BeaverHalting/InfiniteAddress.lean). Principal identifiers: `infiniteWord`, `infiniteWord_ne_top`, `infiniteRead`, `infiniteRead_code_iff`.
5. C. Forrester. *Orbital* README and dependency manifest, same pinned commit. [README](https://github.com/CasimirKnights/Orbital/blob/59bb0c1cc5dcfd88663c92b0117121f61e2223bf/README.md); [dependency lock](https://github.com/CasimirKnights/Orbital/blob/59bb0c1cc5dcfd88663c92b0117121f61e2223bf/lake-manifest.json); [toolchain](https://github.com/CasimirKnights/Orbital/blob/59bb0c1cc5dcfd88663c92b0117121f61e2223bf/lean-toolchain). Relevant sections: scope and proof boundary, limit computation, and charge/drain research direction. Associated release: [Zenodo record 23182375](https://zenodo.org/records/23182375).
6. The mathlib Community. `Mathlib/Computability/Halting.lean`, commit `9470b68e2f52705134448bb88b97d85470c06908`. [Pinned source](https://github.com/leanprover-community/mathlib4/blob/9470b68e2f52705134448bb88b97d85470c06908/Mathlib/Computability/Halting.lean). Principal identifiers: `ComputablePred.halting_problem_re`, `ComputablePred.halting_problem`, `ComputablePred.halting_problem_not_re`.
7. A. M. Turing. “On Computable Numbers, with an Application to the Entscheidungsproblem.” *Proceedings of the London Mathematical Society*, s2-42(1), 230–265, 1936–1937. [DOI: 10.1112/plms/s2-42.1.230](https://doi.org/10.1112/plms/s2-42.1.230).
8. E. Mark Gold. “Limiting Recursion.” *The Journal of Symbolic Logic*, 30(1), 28–48, 1965. [DOI: 10.2307/2270580](https://doi.org/10.2307/2270580).

**Preparation note:** This manuscript was prepared with AI-assisted source inspection and drafting. All claimed source results are tied to the pinned files above. The manuscript's expository propositions are not represented as newly verified Lean declarations or new discoveries in computability theory.
