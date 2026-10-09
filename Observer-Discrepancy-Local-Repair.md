# Observer–Discrepancy–Local Repair: A Minimal Lean Formalization with Conditional Convergence

**Matthew Chenoweth Wright**  
eNuminous / Monolithic LLC  
October 9, 2026

## Abstract

This note isolates a small mathematical core for an observer–discrepancy–local-repair mechanism. A graph specifies which coordinates a local observer may read; a residual records the discrepancy at a coordinate; and a synchronous update subtracts a nonzero gain times that residual. The accompanying Lean 4 source encodes locality preservation and the exact equivalence between zero residuals and fixed points. For a separate global update map, it encodes uniqueness under a strict contraction, a geometric error bound relative to an existing fixed point, and convergence when geometric decay is supplied. Two finite examples show why locality by itself yields neither convergence nor uniqueness: a two-node swap cycles, while the identity map has multiple fixed points.

The result is intentionally conditional. The source does not prove that a fixed point exists, nor does it derive geometric decay from the contraction factor. The Lean project was not kernel-compiled in the authoring environment. This is therefore a formalization candidate and an explicit proof-obligation ledger, not a machine-checked result, a derivation of a new general theorem, or evidence that an EFMW mechanism operates in nature.

## 1. Scope

The target is the abstract loop

\[
\text{local observation}\;\longrightarrow\;\text{residual}\;\longrightarrow\;\text{repair}.
\]

The formalization asks three narrow questions:

1. What does it mean for a residual to depend only on the state visible to one node?
2. Under what condition is a state unchanged by the repair step exactly when all residuals vanish?
3. What additional global hypothesis is sufficient for iterates to approach an equilibrium?

These questions are kept separate. Local information flow is a property of each coordinate rule. Convergence is a property of the assembled global map and a metric on its state space. Neither graph connectivity nor the word “repair” supplies a contraction estimate by itself.

## 2. Local observer and repair rule

Let \(V\) be a type of nodes and let \(E(i,j)\) denote that node \(j\) is adjacent to node \(i\). A state is a function \(x:V\to\mathbb R\). Two states agree on the closed neighborhood of \(i\) when

\[
x_i=y_i
\quad\text{and}\quad
E(i,j)\Rightarrow x_j=y_j.
\]

A residual rule \(r:(V\to\mathbb R)\to V\to\mathbb R\) is local if agreement on that neighborhood implies equality of the residual at \(i\):

\[
\operatorname{AgreeNear}(x,y,i)
\Rightarrow r_i(x)=r_i(y).
\]

For gain \(\eta\in\mathbb R\), the synchronous repair rule is

\[
T_\eta(x)_i=x_i-\eta r_i(x).
\]

The Lean source contains a proof script for the claim that if \(r\) is locally determined, then the coordinate update \(T_\eta(x)_i\) is locally determined too. This is an information-flow result: the update at \(i\) reads only \(x_i\) and the declared neighbors through the residual rule.

### Proposition 1 — Fixed point characterization

For \(\eta\ne0\),

\[
T_\eta(x)=x
\quad\Longleftrightarrow\quad
\forall i\in V,\;r_i(x)=0.
\]

The nonzero-gain condition matters. At \(\eta=0\), every state is fixed regardless of its residual. Proposition 1 characterizes equilibrium for this update definition; it does not say that the residual measures an objective truth, that zero residuals are desirable, or that the update will reach such a state.

## 3. Global convergence hypotheses

Let \((X,d)\) be a metric space and \(T:X\to X\) the assembled update. Assume a real \(q\) satisfies

\[
0\le q<1,
\qquad
d(Tx,Ty)\le q\,d(x,y)\quad\text{for all }x,y\in X.
\tag{C}
\]

### Proposition 2 — At most one fixed point

Under (C), any two fixed points \(x^*,y^*\) are equal. Indeed,

\[
d(x^*,y^*)=d(Tx^*,Ty^*)\le qd(x^*,y^*),
\]

and \(q<1\) forces their distance to be zero.

### Proposition 3 — Geometric error bound and conditional convergence

If a fixed point \(x^*\) already exists, then the \(n\)-th iterate obeys

\[
d(T^n x,x^*)\le q^n d(x,x^*).
\]

Consequently, if \(q^n\to0\), then \(T^n x\) converges to \(x^*\) in metric distance. The Lean source represents the final premise as an explicit `GeometricDecay q` hypothesis; it does not derive that premise from \(0\le q<1\). Thus the encoded convergence theorem has visible inputs rather than hiding this step.

Propositions 2–3 are contraction-mapping consequences, not proposed new general mathematics. Mathlib has a complete-space fixed-point API for maps satisfying its `ContractingWith` predicate [1]. This project uses a direct real-valued distance inequality and has not yet connected that definition to Mathlib’s API. A complete space plus a proved contraction estimate is the natural route for a later existence theorem; neither is established for an EFMW-specific update here.

## 4. Why locality does not suffice

Consider two adjacent nodes and the simultaneous neighbor-copy update

\[
S(a,b)=(b,a).
\]

Starting at \((0,1)\), the system alternates exactly between \((0,1)\) and \((1,0)\). Each coordinate reads only its adjacent node, yet this orbit does not settle at a fixed point. The example falsifies any inference from local communication alone to convergence.

For non-uniqueness, the identity update \(I(x)=x\) fixes every state. It has at least the distinct equilibria \((0,0)\) and \((1,0)\). The example falsifies an unconditional uniqueness claim. It is a counterexample to uniqueness without contraction, not an instance of the nonzero-residual repair rule in Proposition 1.

The source contains direct proof scripts for these exact finite facts, but those scripts remain pending kernel validation. The examples do not establish a general instability criterion or describe measured EFMW behavior.

## 5. Formalization and evidence status

The companion source is in [`formal/efmw-local-repair/`](formal/efmw-local-repair/). Its principal declarations are:

| Declaration | Intended result | Preconditions visible in the source |
|---|---|---|
| `repairStep_locallyDetermined` | Local residuals give local coordinate updates | Residual locality |
| `repairStep_fixed_iff_residual_zero` | Fixed state iff all residuals vanish | Nonzero gain |
| `fixedPoint_unique` | At most one fixed point | Metric space, contraction, \(0\le q<1\) |
| `iterateN_distance_bound` | Iteration error shrinks geometrically | Existing fixed point, contraction, \(q\ge0\) |
| `iterateN_converges_of_geometric_decay` | Iterates approach the fixed point | Above hypotheses and `GeometricDecay q` |
| `swapPair_two_cycle` | A local two-node update can cycle | Exact finite example |
| `identityPair_has_two_fixed_points` | Unconstrained updates need not be unique | Exact finite example |

The source was authored against Lean 4.19.0 and Mathlib v4.19.0. Static inspection found no `sorry` or declared axioms, but the environment did not contain `lean` or `lake`; therefore no kernel build was run. The evidence status is **supported but incomplete**: the project contains proof scripts, but they remain unverified until `lake build` succeeds. Absence of placeholders is not a substitute for compilation.

## 6. Open proof obligations

The next formal tranche should close these obligations in order:

1. **Kernel validation:** install/use the pinned Lean and Mathlib versions, run `lake update` and `lake build`, and fix any elaboration errors.
2. **Geometric decay:** prove in the selected Mathlib version that \(0\le q<1\) implies `GeometricDecay q`, then remove that extra premise from Proposition 3.
3. **Existence:** either package (C) as Mathlib’s `ContractingWith` on a nonempty complete metric space and invoke its fixed-point theorem, or prove a system-specific invariant/compactness result.
4. **EFMW instantiation:** choose a particular residual and state space from the EFMW corpus, type-check units/domains where relevant, and derive—not assume—the contraction or another convergence condition. If no such estimate is true, retain the counterexample or replace convergence with a weaker, accurately stated property.
5. **Empirical separation:** any observed system behavior must be tested independently. A Lean theorem about a defined recurrence proves a property of that recurrence, not that the recurrence models a physical process or predicts an experiment.

## 7. Novelty and claim boundary

The fixed-point, contraction, and geometric-decay statements are standard consequences of metric fixed-point theory. This note makes no novelty claim for them. Its limited contribution is an explicit interface that separates neighborhood-local observation from the global assumptions needed for convergence, together with counterexamples to two tempting overclaims. Whether this interface is useful for a specific EFMW equation remains unresolved until such an equation is instantiated and the resulting hypotheses are discharged.

## References

1. The mathlib Community, “`Mathlib.Topology.MetricSpace.Contracting`,” *mathlib4 documentation*, https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Contracting.html (accessed October 9, 2026).
2. The Lean Community, *Theorem Proving in Lean 4*, https://lean-lang.org/theorem_proving_in_lean4/ (accessed October 9, 2026).

## Reproducibility

The source project pins Lean 4.19.0 and Mathlib v4.19.0. From `formal/efmw-local-repair/`, run:

```sh
lake update
lake build
```

No successful build result is claimed in this paper. The public commit containing this paper and its source files is the reproducible snapshot to use when the build is performed.
