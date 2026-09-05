# EFMW / Monolithic Theorem Tranche III — Frozen Docket

**Date:** 5 September 2026  
**Purpose:** derive bounded, Lean-formalizable mathematical results from Zoo-surviving equation repairs.  
**Non-claim:** a formal theorem about a specified recurrence, operator, or ODE does not validate an EFMW physical, cognitive, or consciousness interpretation.

## Global admission rule

An item enters this tranche only after its exact statement, assumptions, source equation, dependency path, and disproof condition are frozen. The required Zoo route is:

`TORTOISE → WEAVER → SALMON → CROCODILE → HEDGEHOG → DRAGON → TURTLE`.

TORTOISE freezes the claim; WEAVER records dependencies; SALMON checks inference direction; CROCODILE removes or changes the decisive term; HEDGEHOG checks generalization; DRAGON isolates the stable mathematical core; TURTLE records only survivors. Correlated animal outputs are not independent replication.

## TIII-01 — ME-036/037 coefficient-collapse theorem

**Frozen model.** Let `S` and `O` be differentiable scalar fields on the same domain. Suppose the cross-gradient contribution is

\[
\alpha\langle\nabla S,\nabla O\rangle+\beta\langle\nabla O,\nabla S\rangle.
\]

**Theorem.** Under a symmetric inner product,

\[
\alpha\langle\nabla S,\nabla O\rangle+\beta\langle\nabla O,\nabla S\rangle
=(\alpha+\beta)\langle\nabla S,\nabla O\rangle.
\]

Therefore observations of this symmetric term can identify at most the effective coefficient `κ = α + β`, not `α` and `β` separately.

**CROCODILE test.** Replace `(α, β)` by any `(α+δ, β−δ)`; the term is invariant. A theorem claiming separate recovery of `α` and `β` therefore fails.

**Lean target.** `ME036.crossGradientCollapse` and `ME037.effectiveCoefficientAgreement`.

**Repair admitted.** The next operator model uses one symmetric coefficient `κ`, unless separately typed asymmetric operators are supplied.

## TIII-02 — ME-096 summable-increments convergence theorem

**Frozen model.** Let `(x_n)` be a sequence in a complete normed vector space. Assume

\[
\sum_{n=0}^{\infty}\lVert x_{n+1}-x_n\rVert < \infty.
\]

**Theorem.** `(x_n)` converges.

**Proof obligation.** For `m > n`, the triangle inequality gives

\[
\lVert x_m-x_n\rVert\le\sum_{k=n}^{m-1}\lVert x_{k+1}-x_k\rVert.
\]

The convergent series has vanishing tails, so `(x_n)` is Cauchy; completeness supplies the limit.

**CROCODILE test.** Remove summability and retain only `\lVert x_{n+1}-x_n\rVert→0`; the harmonic partial sums are a counterexample. Thus the original criterion is rejected and the strengthened theorem survives.

**Lean target.** `ME096.summableIncrements_convergent`.

## TIII-03 — ME-101 affine recursion theorem

**Frozen model.** For real `a`, `b`, and initial value `x₀`, define

\[
x_{n+1}=a x_n+b.
\]

**Theorem.** If `a ≠ 1`, then

\[
x_n=a^n x_0+b\frac{a^n-1}{a-1}.
\]

If `a = 1`, then `x_n = x₀ + nb`. If `a > 1` and `x₀+b/(a-1) > 0`, then `x_n→+∞`.

**CROCODILE test.** The positive-gain model cannot represent a bounded persistence score without an additional saturation, decay, or clipping mechanism.

**Lean targets.** `ME101.affineClosedForm`, `ME101.positiveGainDiverges`.

**Repair branch.** A bounded-persistence interpretation requires a new, explicitly separate recurrence; it must not be inferred from the divergent one.

## TIII-04 — ME-078/082 relaxation solution theorem

**Frozen model.** Let `τ > 0`, `η_eq` be constant, and

\[
\frac{d\eta}{dt}=\frac{\eta_{eq}-\eta}{\tau},\qquad \eta(0)=\eta_0.
\]

**Theorem.** The unique classical solution is

\[
\eta(t)=\eta_{eq}+(\eta_0-\eta_{eq})e^{-t/\tau}.
\]

For `η₀=0` and `η_eq=η̄`, this becomes `η(t)=η̄(1-e^{-t/τ})`, the specific ME-078 exponential recovery form.

**CROCODILE test.** Change `η_eq` to a nonconstant function or remove `τ>0`; the stated exponential solution no longer follows. ME-078 therefore remains a special case, not a general thixotropy law.

**Lean targets.** `ME082.constantEquilibrium_solution`, `ME078.zeroInitial_specialization`.

## TIII-05 — ME-066 direct-sum norm theorem

**Frozen model.** Let `S` and `O` be normed vector spaces and define the dyadic state as `X = S × O` with norm

\[
\lVert(s,o)\rVert_2=\sqrt{\lVert s\rVert^2+\lVert o\rVert^2}.
\]

**Theorem.** The canonical embeddings `i_S(s)=(s,0)` and `i_O(o)=(0,o)` are isometries, and

\[
\lVert i_S(s)+i_O(o)\rVert_2^2=\lVert s\rVert^2+\lVert o\rVert^2.
\]

**CROCODILE test.** Remove the direct-sum construction; expressions combining `s` and `o` are not even well typed when their spaces differ. This establishes a type repair, not a theory of cognition.

**Lean targets.** `ME066.embedS_isometry`, `ME066.embedO_isometry`, `ME066.directSumNormSq`.

## Sequencing and completion criteria

| Order | Target | Completion requirement |
| --- | --- | --- |
| 1 | TIII-01 / ME-036/037 | Lean proof of collapse plus chosen repaired operator signature |
| 2 | TIII-02 / ME-096 | Lean proof of summable-increments convergence and explicit counterexample to the weaker claim |
| 3 | TIII-03 / ME-101 | Lean closed form and divergence theorem; separate repaired recurrence if proposed |
| 4 | TIII-04 / ME-078/082 | Lean ODE solution under constant-equilibrium assumptions |
| 5 | TIII-05 / ME-066 | Lean direct-sum typing and norm theorem |

No item is counted as formalized until its theorem compiles in the pinned, clean-build P0 repository; source line, assumptions, Zoo route, and Lean theorem identifier are added to the 102-row crosswalk.
