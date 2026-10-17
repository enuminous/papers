# Exact Parity in a Three-Prime Elliptic-Curve Image

## A Lean-Verified Contribution to a Birch–Swinnerton-Dyer Audit

**Matthew Chenoweth Wright**  
Monolithic LLC · 17 October 2026 · Version 1.0 · Research preprint

[Papers catalogue](README.md) · [Proof package](formal/bsd-parity/README.md) · [Central Lean theorems](formal/bsd-parity/BSDImprovements/CurveImage.lean) · [Axiom audit](formal/bsd-parity/verification/axiom-audit.json) · [Verification workflow](.github/workflows/bsd-parity.yml)

## Abstract

We study a finite arithmetic example published in Chris Forrester's BSD materials: the curve $E:y^2+xy=x^3-x^2-79x+289$, four specified rational points, and their simultaneous coordinate reductions at the primes 5, 13, and 19. The observed generated image has 2,800 elements inside a product of 5,600 finite-curve points. We prove an exact characterization: after choosing explicit cyclic generators, the image consists precisely of the triples whose discrete-log coordinates have even total parity. The proof supplies constructive preimages and is connected to Mathlib's elliptic-curve group law, rather than assuming an abstract log table. The finite group orders, logarithms, point coverage, image characterization, and cardinality are checked in Lean.

A separate specification analysis identifies why a freely chosen positive period weakens a proposed refined BSD product to a positivity condition. We give an interface with fixed numerical inputs, define its regulator as a Gram determinant, and verify the determinant transformation under a change of frame. The accompanying package contains 52 named theorem declarations, including helper lemmas and finite certificates. These results strengthen the arithmetic and specification components of the research program. They do not construct the actual elliptic L-function, identify all BSD invariants, establish the missing central vanishing, or prove BSD.

**Keywords:** elliptic curves; finite reduction images; parity; Lean; formal verification; BSD; regulator; mathematical specification.

## 1. From an audit to a precise theorem

An audit of a proposed major theorem should recover the valid mathematics as carefully as it identifies missing implications. Forrester's published illustration supplies a concrete curve, a four-point frame, finite-prime calculations, height data, and an analytic construction. Its detailed account explicitly retains unresolved targets, including a coefficient denoted $c_2$ and a global identity involving a regulator [1].

The earlier audit reproduced a finite count: the four-point word lattice has an image of order 2,800 in a product with 5,600 elements. The present paper strengthens that count into a structural theorem with an explicit converse. It answers not only how many combinations occur, but exactly which combinations occur and how to produce each of them.

The classical BSD target relates the rank of $E(\mathbb Q)$ to the order of vanishing of the actual Hasse–Weil L-function at $s=1$. Its refined form additionally identifies a leading coefficient using the real period, a canonical-height regulator, torsion, Tamagawa factors, and the Tate–Shafarevich group [2]. A finite reduction identity is a component of arithmetic information; a further argument is needed to connect it to this analytic target.

Two outputs are therefore kept distinct throughout:

1. An unconditional theorem about three explicit finite elliptic-curve groups and four explicit simultaneous point tuples.
2. Generic specification and determinant results whose application to BSD requires the actual arithmetic inputs to be constructed and identified.

The source snapshot and evaluation criteria were fixed before the follow-on proof work. The upstream repository reference is `916ab476012852778edd9ca63aecf200a8e90ed1` [3]. The website is a separate evidence object; no undocumented correspondence between its payload and that repository commit is assumed. Its illustration was fetched again for this paper and matched the audited SHA-256 digest recorded in the publication note [4].

## 2. The curve, points, and finite groups

We use the generalized Weierstrass model

$$
E:\quad y^2+xy=x^3-x^2-79x+289,
\qquad [a_1,a_2,a_3,a_4,a_6]=[1,-1,0,-79,289],
$$

with the ordered points

$$
P_1=(6,-1),\quad P_2=(4,3),\quad P_3=(5,-2),\quad P_4=(7,3).
$$

Exact substitution verifies that they lie on the rational curve. For $p\in\{5,13,19\}$, let $P_{i,p}$ be the point obtained by reducing these integral coordinates modulo $p$. The Lean construction proves that every displayed finite point is nonsingular.

The following table is certified using Mathlib's nonsingular affine-point group [5]. Infinity is included in each group order.

| Prime $p$ | $N_p=\#E(\mathbb F_p)$ | Generator $G_p$ | $P_{1,p}$ log | $P_{2,p}$ log | $P_{3,p}$ log | $P_{4,p}$ log |
|---|---:|---|---:|---:|---:|---:|
| 5 | 10 | $(1,0)$ | 9 | 5 | 8 | 7 |
| 13 | 20 | $(0,4)$ | 6 | 8 | 17 | 10 |
| 19 | 28 | $(0,2)$ | 9 | 21 | 5 | 25 |

A log entry $d$ means $P_{i,p}=dG_p$. The certificates establish that $G_p$ has exact order $N_p$ and that its multiples exhaust the points of the curve. Thus the table supplies actual cyclic coordinates on the finite groups.

Put

$$
A=E(\mathbb F_5)\times E(\mathbb F_{13})\times E(\mathbb F_{19}),
$$

and define the homomorphism

$$
\rho:\mathbb Z^4\longrightarrow A,\qquad
\rho(n_1,n_2,n_3,n_4)
=\left(\sum_{i=1}^4n_iP_{i,5},\sum_{i=1}^4n_iP_{i,13},
\sum_{i=1}^4n_iP_{i,19}\right).
$$

Write $H=\operatorname{im}\rho$. This definition requires no assertion that the four rational points form a basis of $E(\mathbb Q)$.

In cyclic coordinates the map is the integer matrix

$$
M=\begin{pmatrix}
9&5&8&7\\
6&8&17&10\\
9&21&5&25
\end{pmatrix},
$$

with its three rows interpreted modulo 10, 20, and 28, respectively.

## 3. Exact characterization of the joined image

**Theorem 1 — parity kernel.** For every $a,b,c\in\mathbb Z$,

$$
(aG_5,bG_{13},cG_{19})\in H
\quad\Longleftrightarrow\quad a+b+c\equiv0\pmod2.
$$

Consequently, in the stated cyclic coordinates,

$$
H=\ker\left[
\chi:\mathbb Z/10\mathbb Z\times\mathbb Z/20\mathbb Z\times
\mathbb Z/28\mathbb Z\longrightarrow\mathbb Z/2\mathbb Z,
\quad \chi(a,b,c)=a+b+c
\right].
$$

**Proof: necessity.** All three moduli are even, so the parity test is independent of the representatives. The sums of the four columns of $M$ are 24, 34, 30, and 42. Every integer combination of those columns therefore has even total parity. Changing a row representative by its modulus preserves this property.

**Proof: sufficiency.** Consider the three words

$$
u=(5,5,0,3),\qquad v=(3,9,3,2),\qquad w=(5,0,0,5).
$$

Their ordinary integer images are

$$
Mu=(91,100,225),\quad Mv=(110,161,281),\quad Mw=(80,80,170).
$$

Reducing by the row moduli gives

$$
Mu\equiv(1,0,1),\qquad Mv\equiv(0,1,1),\qquad
Mw\equiv(0,0,2).
$$

If $a+b+c$ is even, then $t=(c-a-b)/2$ is an integer. The word $au+bv+tw$ has image $(a,b,c)$. Explicitly, a preimage is

$$
\left(5a+3b+5t,\ 5a+9b,\ 3b,\ 3a+2b+5t\right).
$$

This proves the converse and supplies a constructive witness for every compatible triple. ∎

The corresponding Lean declaration is `BSDImprovements.curve_joined_image_iff_even`. The proof first establishes the integral congruence statement, then transfers it through the checked discrete logs and exact generator orders to the curve groups. The transfer itself is proved in `curve_image_iff_log_image`; it is not an additional assumption.

**Corollary 1 — exact cardinality.** The group $H$ has 2,800 elements and index two in $A$.

For each of the $10\times20$ choices of the first two coordinates, exactly 14 residues modulo 28 have the required parity. Therefore

$$
|H|=10\cdot20\cdot14=2800,
\qquad |A|=10\cdot20\cdot28=5600.
$$

The formal cardinality result is stated for the actual finite-curve point tuples in `curve_reduction_image_card`, rather than only for an abstract residue set.

## 4. Pairwise coverage and a three-coordinate obstruction

The theorem shows that every pair of coordinates can occur: choose the parity of the omitted coordinate to make the total even. Nevertheless the triple $(0,0,1)$ cannot occur. Thus all pairwise projections are surjective while the joint image is proper.

| Fixed pair | Number of pair values | Compatible values of the remaining coordinate |
|---|---:|---:|
| Modulo 5 and 13 | $10\cdot20=200$ | 14 modulo 19 |
| Modulo 5 and 19 | $10\cdot28=280$ | 10 modulo 13 |
| Modulo 13 and 19 | $20\cdot28=560$ | 5 modulo 5 |

These are written corollaries of Theorem 1, not additional separately named Lean declarations in the 52-theorem count. The final row explains the finite conditional factor $2800/560=5$ appearing in the motivating calculation. Multiplying three marginal group orders would miss the compatibility condition.

Here “parity” means the finite character $\chi$. It is not the root number of an elliptic L-function, and the proof supplies no identification between those two notions.

An exploratory attempt to enlarge the frame by adding $Q=(8,7)$ gives a useful negative result. Its logs are $(4,4,22)$, which already satisfy the parity condition. Exact rational group arithmetic also verifies

$$
Q=-P_1-P_4.
$$

Consequently this particular extra point cannot enlarge the generated image. This identity is checked by the supplied Python implementation, not added to the Lean theorem inventory. It neither proves saturation of the rational frame nor rules out every possible missing rational point.

## 5. Why a free period weakens a coefficient statement

The inspected upstream `StrongLeadingCoefficientStatement` combines a rank equality with existentially quantified positive period, Sha-order, and Tamagawa-product witnesses [6]. The issue is the meaning of the quantified statement, independently of whether its conditional helper theorems compile.

**Proposition 2 — free-period diagnostic.** For fixed real numbers $R>0$ and $T>0$, the statement

$$
\exists n,m\in\mathbb N,\ \exists\Omega\in\mathbb R:
\quad n>0,\ m>0,\ \Omega>0,\quad
C=\frac{\Omega Rnm}{T^2}
$$

is equivalent to $C>0$.

**Proof.** Positive factors imply $C>0$. Conversely, if $C>0$, choose $n=m=1$ and $\Omega=CT^2/R$. These witnesses satisfy the equality and all positivity conditions. ∎

This is a written proof reproduced here for the specification argument. It was also checked as a standalone diagnostic in the preceding audit; that earlier diagnostic file is not part of the present 52-declaration inventory.

The conclusion is limited but decisive: this existential product does not identify the actual period, actual Sha order, or actual Tamagawa product. It cannot by itself encode the classical refined coefficient assertion. The argument does not disprove BSD, show an inconsistency in Lean, or identify who or what caused the specification choice.

## 6. Fixed inputs and the regulator definition

The replacement component `FixedInvariants r` stores a real matrix $G$ of size $r\times r$ together with four fixed numerical inputs:

$$
\Omega\in\mathbb R,\quad S\in\mathbb N,\quad
\mathcal T\in\mathbb N,\quad T\in\mathbb N.
$$

The intended meanings are period, Sha cardinality, Tamagawa product, and torsion cardinality. The regulator is defined by

$$
R(G):=\det G,
$$

and the coefficient proposition for a given record $d$ is

$$
\operatorname{FixedCoefficientStatement}(d,C)
\quad:\Longleftrightarrow\quad
C=\frac{\Omega\det(G)S\mathcal T}{T^2}.
$$

There is no existential choice of these quantities inside the proposition. For a fixed record, two coefficients satisfying it must be equal. Under the explicitly supplied positive-input assumptions, the coefficient is positive. Conversely, positivity is insufficient: take $G=(1)$ and all four scalar inputs equal to one. The predicted coefficient is one, so the positive number $C=2$ fails the statement. These claims are checked in `FixedInvariants.lean` [7].

The upstream height interface stores a regulator scalar without an equality identifying it with its Gram-matrix determinant [8]. Defining the regulator as `gram.det` removes that specific degree of freedom.

This repair is necessary specification work, not a completed model of BSD. A caller could still supply an arbitrary record. To apply it to a curve, one must construct the data from that curve and prove the interpretation of every field. In particular, a natural-number field named `shaCard` is not a proof that the actual Tate–Shafarevich group is finite. Rank equality and the identification of $C$ as the actual leading coefficient remain separate obligations.

## 7. Frame changes and regulator normalization

**Theorem 3 — Gram determinant transformation.** For real $r\times r$ matrices $G,U$,

$$
\det(U^TGU)=\det(U)^2\det(G).
$$

**Proof.** Multiplicativity of the determinant and $\det(U^T)=\det U$ give

$$
\det(U^TGU)=\det(U^T)\det(G)\det(U)
=\det(U)^2\det(G).
$$

The proof is formalized in `regulator_under_change`. ∎

An integral unimodular change, with determinant $1$ or $-1$, preserves the Gram determinant. More generally, if a chosen frame is obtained from an actual full lattice basis by an integral matrix of determinant of absolute value $k$, its Gram determinant is $k^2$ times that of the full basis. The formal package proves the matrix identity and its determinant specializations; the identification of $k$ with a Mordell-Weil subgroup index still requires the arithmetic basis comparison.

Positive definiteness of a genuine canonical-height matrix would prove independence of its points. It would not alone prove that those points form a saturated full basis. Accordingly, a determinant from a four-point frame cannot be promoted to the full-group regulator without the missing identification. This distinction is relevant even when all numerical determinant calculations are correct.

The determinant identities are standard linear algebra. Their contribution here is to make the normalization obligation explicit and enforce the determinant definition in the interface.

## 8. Formalization and reproducibility

The proof package is published at [`formal/bsd-parity/`](formal/bsd-parity/README.md). Its files have distinct roles:

| Module | What it establishes | Named theorems |
|---|---|---:|
| `FiniteCurve.lean` | Nonsingular points, discrete logs, exact generator orders, exhaustive finite-point coverage, and finite group cardinalities | 31 |
| `JoinedPrimes.lean` | Integral parity characterization, constructive residue equivalence, and cardinality | 6 |
| `CurveImage.lean` | Transfer to actual curve groups and the final image/cardinality statements | 9 |
| `FixedInvariants.lean` | Fixed-coefficient properties and determinant transformation laws | 6 |
| **Total** | **Includes helpers and finite arithmetic certificates** | **52** |

Finite decisions use `decide +kernel`. The generated Lean source is checked by Lean; the Python generator is not a trusted oracle. A separate standard-library Python implementation enumerates the finite groups, recomputes the logs and image, and verifies constructive preimages for all 2,800 compatible triples. This is an implementation cross-check, not a second independent proof of the entire BSD program.

The build uses Lean **4.28.0** and Mathlib commit
`8f9d9cff6bd728b17a24e163c9402775d9e6a365`. Every named theorem's transitive axiom list was checked against `propext`, `Classical.choice`, and `Quot.sound`. No audited theorem depends on an admission, a custom axiom, or a native decision certificate. These checks establish formal validity of the stated propositions relative to the pinned Lean/Mathlib foundation; they do not establish an external interpretation that the propositions omit.

From the repository root, reproduction is:

```sh
cd formal/bsd-parity
lake exe cache get
bash verify.sh
```

The dependency cache command is optional if the dependencies are already available or are built from source. The verification script checks exact arithmetic, builds the library, prints the theorem dependencies, and rejects unexpected axioms. The published workflow repeats these checks in GitHub Actions [9]. Its actual result is given by the linked run history, separately from the recorded local result.

The copied package retains the original local provenance: pinned dependency caches were reused; a pre-existing deletion of `batteries/docs/README.md` did not affect Lean source; and the authoring host used a path-lookup compatibility shim. Those details are recorded rather than treated as an independent conventional-environment build. The GitHub workflow uses the normal toolchain installation.

Ramtastic's inspected snapshot uses Lean **4.30.0-rc1**. This standalone development does not import or rebuild that upstream release. Porting the results into it is an integration task, distinct from the proofs reported here.

## 9. What remains between these results and BSD

The result is about $H$, the subgroup generated by four specific simultaneous finite tuples. Identifying $H$ with the image of **all** of $E(\mathbb Q)$ would require additional rational-group information. The current Lean package does not construct the general reduction homomorphism from rational points, prove the rational rank, or prove saturation.

Likewise, no finite character computed here identifies the order of vanishing of the actual L-function. Even a separately established even functional-equation parity would leave orders two and four compatible with that parity. The illustration's remaining target called $c_2=0$ must be proved for its precisely defined object and connected to the intended L-function coefficient. A displayed or reconstructed quantity is not automatically $L''(E,1)/2$.

For a rank-four endpoint, one ultimately needs the appropriate lower-derivative vanishings and a nonzero fourth leading term, together with the algebraic-rank statement. Establishing one coefficient's vanishing alone would not discharge all those obligations. The leading coefficient must then be related to the actual BSD invariants, including consistent period and height normalizations.

| Claim or obligation | Evidence status in this work |
|---|---|
| The finite groups and the displayed log table | **Demonstrated:** Lean proofs against Mathlib |
| Exact parity characterization and 2,800-element image | **Demonstrated:** end-to-end finite-group formalization |
| Fixed-input coefficient and determinant identities | **Demonstrated:** generic formal statements with stated inputs |
| Rational identity for $Q=(8,7)$ | **Demonstrated computationally:** exact rational Python arithmetic |
| Identification with all rational points and a full saturated basis | **Unresolved here** |
| Identification of supplied heights with canonical heights | **Unresolved here** |
| Actual Euler-product L-function and analytic comparison | **Unresolved in this formalization** |
| Required central vanishing and actual analytic rank | **Unresolved here** |
| Sha finiteness and the full refined equality | **Unresolved here** |

“Unresolved here” describes the scope of this development. It is not a claim that all of these topics are unknown to the wider mathematical literature.

## 10. Contribution, method, and the next test

The contribution is a concrete refinement of a published arithmetic example and a correction to the form of a coefficient specification. The parity argument is elementary finite abelian-group reasoning; the Gram determinant law is standard. We make no priority claim for either general method or for the first possible discovery of this particular finite relation. The substantive deliverable is an explicit proof and its checked connection to the stated curve groups.

The EFMW Zoo supplied the audit discipline: freeze the example, inspect the meaning of each statement, preserve counterexamples and unsuccessful branches, and distinguish proved components from unresolved implications. No EFMW physical field equation is used in these proofs. This paper reports the focused follow-on development; it does not claim a fresh complete run of every Zoo operation or establish a general performance advantage for the audit framework.

The most useful next step is an explicit identification theorem for the analytic construction. Its input should be a precisely defined analytic object and the actual elliptic L-function, with normalizations fixed before comparison. Success requires a proved equality strong enough to transfer the claimed coefficient or vanishing statement. A supplied equality field, a fitted multiplicative constant, or agreement at finitely many numerical samples would not meet that criterion.

Alongside that analytic task, canonical-height and saturation certificates can make the regulator interpretation precise. These are concrete interfaces through which the verified finite arithmetic could become part of a larger proof. They prevent a correct partial theorem from being asked to carry a conclusion it does not establish.

## Authorship and acknowledgments

Matthew Chenoweth Wright commissioned and directed this follow-on audit and formalization. The manuscript, code construction, and verification were developed with OpenAI Codex assistance. Chris Forrester's published BSD example and Ramtastic interfaces supplied the motivating target; he is credited for those materials and is not represented as having approved this manuscript. Mathlib's elliptic-curve implementation supplies the formal group foundation. No external peer-review claim is made.

## References and artifacts

1. Chris Forrester / Casimir Knights. [Published BSD sphere–cube–Bessel illustration](https://cknights.com/works/bsd/sphere_cube_bessel.html). Inspected 17 October 2026. Concrete example and expressly retained analytic targets; snapshot digest in [publication provenance](formal/bsd-parity/PUBLICATION.md).
2. Andrew Wiles. [The Birch and Swinnerton-Dyer Conjecture](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf). Clay Mathematics Institute problem description. Reference target for the rank and refined coefficient assertions.
3. CasimirKnights. [Ramtastic, inspected commit `916ab476…`](https://github.com/CasimirKnights/Ramtastic/tree/916ab476012852778edd9ca63aecf200a8e90ed1). The website and this source snapshot are treated as separate evidence objects.
4. Monolithic follow-on artifacts. [Publication provenance](formal/bsd-parity/PUBLICATION.md), [frozen scope](formal/bsd-parity/FROZEN-SCOPE.json), [exact arithmetic results](formal/bsd-parity/verification/arithmetic.json), and [file digests](formal/bsd-parity/SHA256SUMS).
5. David Kurniadi Angdinata and Mathlib contributors. [Affine elliptic-curve point group](https://github.com/leanprover-community/mathlib4/blob/8f9d9cff6bd728b17a24e163c9402775d9e6a365/Mathlib/AlgebraicGeometry/EllipticCurve/Affine/Point.lean). Pinned Mathlib source; Apache-2.0 licensed.
6. Ramtastic. [`BSD/Statement.lean`](https://github.com/CasimirKnights/Ramtastic/blob/916ab476012852778edd9ca63aecf200a8e90ed1/Ramtastic/BSD/Statement.lean). Inspected statement and endpoint interfaces.
7. Monolithic follow-on formalization. [`FixedInvariants.lean`](formal/bsd-parity/BSDImprovements/FixedInvariants.lean), [`JoinedPrimes.lean`](formal/bsd-parity/BSDImprovements/JoinedPrimes.lean), [`FiniteCurve.lean`](formal/bsd-parity/BSDImprovements/FiniteCurve.lean), and [`CurveImage.lean`](formal/bsd-parity/BSDImprovements/CurveImage.lean).
8. Ramtastic. [`BSD/HeightPairing.lean`](https://github.com/CasimirKnights/Ramtastic/blob/916ab476012852778edd9ca63aecf200a8e90ed1/Ramtastic/BSD/HeightPairing.lean). Inspected canonical-height and regulator interface.
9. Reproducibility record. [Local axiom audit](formal/bsd-parity/verification/axiom-audit.json), [local provenance](formal/bsd-parity/verification/provenance.json), [verification script](formal/bsd-parity/verify.sh), and [GitHub verification runs](https://github.com/enuminous/papers/actions/workflows/bsd-parity.yml).
