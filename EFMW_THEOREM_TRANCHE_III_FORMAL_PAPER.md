# The EFMW Theorem Tranche III

## A Prospective, Adversarial Formalization Program for Identifiability, Convergence, Recursion, Relaxation, and Typed Dyads

**Matthew Chenoweth Wright · Monolithic LLC**  
**5 September 2026**

### Abstract

This paper specifies the third formal theorem tranche for the Monolithic 102 / EFMW program. Unlike Tranche II, whose eighteen declarations have recorded Lean 4 builds, Tranche III is prospective: it freezes five bounded theorem targets before implementation and makes their failure conditions explicit. The selected targets address (i) coefficient non-identifiability in the ME-036/037 symmetric cross-gradient model, (ii) a valid convergence condition replacing ME-096's insufficient vanishing-increment condition, (iii) the closed form and growth behavior of the ME-101 affine recurrence, (iv) the general constant-equilibrium solution of the ME-082 relaxation equation with ME-078 as a special case, and (v) a normed direct-sum repair for ME-066. Each target is admitted through an adversarial Zoo route and becomes a formal result only after compilation in the pinned P0 Lean repository. No target constitutes empirical confirmation of EFMW or a claim of new physical law.

## 1. Formalization policy

The third tranche has one governing rule: a theorem must be selected by a frozen need, not by an attractive conclusion. The common route is

`TORTOISE → WEAVER → SALMON → CROCODILE → HEDGEHOG → DRAGON → TURTLE`.

TORTOISE fixes the exact claim and assumptions. WEAVER records the dependency graph. SALMON verifies inference direction. CROCODILE perturbs or removes the decisive term. HEDGEHOG asks whether the result generalizes under its stated assumptions. DRAGON isolates the surviving mathematical core. TURTLE records a survivor only after those checks. This route is an audit protocol; correlated diagnostic outputs are not independent evidence.

## 2. ME-036/037: coefficient collapse and identifiability

Let `S` and `O` be differentiable scalar fields on a common domain with a symmetric inner product. Consider the paired cross-gradient term

\[
Q_{α,β}(S,O)=α\langle\nabla S,\nabla O\rangle+β\langle\nabla O,\nabla S\rangle.
\]

### Theorem III.1 — Cross-gradient coefficient collapse

\[
Q_{α,β}(S,O)=(α+β)\langle\nabla S,\nabla O\rangle.
\]

Consequently, the symmetric expression can identify at most `κ=α+β`; it cannot separately identify `α` and `β`.

**Proof.** Symmetry gives `⟨∇O,∇S⟩=⟨∇S,∇O⟩`; factoring produces the result.

**CROCODILE falsifier.** For every `δ`, the replacement `(α,β)↦(α+δ,β−δ)` leaves `Q` unchanged. Any theorem of separate recovery from this term alone is false.

**Formal consequence.** The repaired symmetric model must use one parameter `κ`. A directional model requires distinct, typed operators rather than merely two coefficient names.

## 3. ME-096: convergence from summable increments

Let `(x_n)` be a sequence in a complete normed vector space. The weaker condition `‖x_{n+1}-x_n‖→0` is insufficient: harmonic partial sums provide a counterexample.

### Theorem III.2 — Summable increments imply convergence

If

\[
\sum_{n=0}^{\infty}\lVert x_{n+1}-x_n\rVert<\infty,
\]

then `(x_n)` converges.

**Proof.** For `m>n`,

\[
\lVert x_m-x_n\rVert\le\sum_{k=n}^{m-1}\lVert x_{k+1}-x_k\rVert.
\]

The right-hand side is a tail of a convergent nonnegative series, hence vanishes as `m,n→∞`. The sequence is Cauchy; completeness supplies a limit.

This repairs ME-096 by substituting a real sufficient condition for a false one. It does not prove convergence of any EFMW recurrence until that recurrence is shown to meet the summability assumption.

## 4. ME-101: affine recursion and boundedness failure

For real `a`, `b`, and `x₀`, let

\[
x_{n+1}=a x_n+b.
\]

### Theorem III.3 — Closed form

For `a≠1`,

\[
x_n=a^n x_0+b\frac{a^n-1}{a-1}.
\]

For `a=1`, `x_n=x_0+nb`.

**Proof.** Induction on `n`, using the finite geometric-series identity.

### Theorem III.4 — Positive-gain divergence

If `a>1` and `x₀+b/(a-1)>0`, then `x_n→+∞`.

The closed form rewrites as

\[
x_n=a^n\left(x_0+\frac{b}{a-1}\right)-\frac{b}{a-1},
\]

and the positive coefficient of `a^n` diverges.

**CROCODILE conclusion.** A positive-gain affine update cannot be treated as a bounded persistence score without a separately stated saturation, decay, projection, or clipping mechanism.

## 5. ME-078/082: general relaxation solution

Let `τ>0`, let `η_eq` be constant, and consider

\[
\frac{dη}{dt}=\frac{η_{eq}-η}{τ},\qquad η(0)=η_0.
\]

### Theorem III.5 — Constant-equilibrium relaxation

The unique classical solution is

\[
η(t)=η_{eq}+(η_0-η_{eq})e^{-t/τ}.
\]

**Proof plan.** Differentiate the candidate solution, substitute it into the right-hand side, and apply standard uniqueness for a globally Lipschitz affine vector field.

### Corollary III.6 — ME-078 specialization

With `η₀=0` and `η_eq=η̄`,

\[
η(t)=η̄(1-e^{-t/τ}),
\]

which is exactly the ME-078 curve. Thus ME-078 is a special initial-value case of ME-082, not a general thixotropy identity.

The theorem assumes a constant equilibrium and positive time constant. Dropping either invalidates the displayed conclusion.

## 6. ME-066: direct-sum type and norm repair

Let `S` and `O` be normed vector spaces. Define the dyadic carrier `X=S×O` with product norm

\[
\lVert(s,o)\rVert_2=\sqrt{\lVert s\rVert^2+\lVert o\rVert^2}.
\]

Define embeddings `i_S(s)=(s,0)` and `i_O(o)=(0,o)`.

### Theorem III.7 — Canonical embeddings are isometries

\[
\lVert i_S(s)\rVert_2=\lVert s\rVert,\qquad
\lVert i_O(o)\rVert_2=\lVert o\rVert.
\]

### Theorem III.8 — Direct-sum norm decomposition

\[
\lVert i_S(s)+i_O(o)\rVert_2^2=\lVert s\rVert^2+\lVert o\rVert^2.
\]

These results provide a transparent carrier for different state spaces. They do not identify `S` and `O` with human or AI cognition, and they do not embed a tensor-product coupling back into the direct sum; that would require a separately specified operator.

## 7. Lean proof obligations and status

| Target | Proposed declarations | Current status |
|---|---|---|
| ME-036/037 | `crossGradientCollapse`, `effectiveCoefficientAgreement` | frozen; not yet compiled |
| ME-096 | `summableIncrements_convergent` | frozen; not yet compiled |
| ME-101 | `affineClosedForm`, `positiveGainDiverges` | frozen; not yet compiled |
| ME-078/082 | `constantEquilibrium_solution`, `zeroInitial_specialization` | frozen; not yet compiled |
| ME-066 | `embedS_isometry`, `embedO_isometry`, `directSumNormSq` | frozen; not yet compiled |

Completion requires a clean build under the P0 pinned toolchain, no `sorry`, `admit`, or custom axioms, and a crosswalk entry linking each declaration to source equation, assumptions, Zoo route, and theorem file.

## 8. Conclusion

Tranche III is an explicit formalization program, not a completed theorem count. Its central contribution is methodological: it turns failures—coefficient non-identifiability, insufficient convergence conditions, unbounded recursion, special-case relaxation, and type mismatch—into precise mathematical targets. If the listed proof obligations compile, the resulting results will establish the stated conditional propositions. They will not, by themselves, establish EFMW's empirical or physical interpretations.
