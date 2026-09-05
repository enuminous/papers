# The EFMW Theorem Tranche II

## Machine-Checked Bounds, Typed Dyadic Coupling, and Thixotropic Relaxation

**Formalization of ME-047, ME-066, ME-078, and ME-082 in Lean 4**  
Matthew Chenoweth Wright · Monolithic LLC  
5 September 2026

### Abstract

This paper records eighteen machine-checked theorem declarations drawn from four equations in the Monolithic 102 corpus. They establish: sharp bounds and an equality characterization for a scalar recursive-coherence score (ME-047); a type-safe replacement for an ill-typed dyadic expression (ME-066); a closed-form exponential relaxation curve and its relation to its governing first-order equation (ME-078); and equilibrium/sign properties of that relaxation field (ME-082). The formal development was compiled with Lean 4.19.0 and Mathlib v4.19.0 at repository commit `ae583082282786384f3280ece6b2a49ed2cc6729`, without proof holes or custom axioms. These are kernel-checked consequences of explicit definitions. They do not, by formal consistency alone, validate EFMW's physical, cognitive, or empirical interpretations.

## 1. Method and scope

The theorem selection was driven by an adversarial Zoo audit rather than an attempt to prove the entire 102-equation corpus. ME-047 was selected as a bounded-score candidate; ME-066 because its source notation combined values from incompatible types; ME-078 because it claimed an exponential thixotropic curve; and ME-082 because it supplied the associated relaxation field. The formal result is deliberately modular: every conclusion follows from a displayed definition and named assumptions, not from EFMW terminology.

## 2. ME-047: scalar recursive coherence

For real `x`, `m`, and `ε`, define

\[
C_ε(x,m)=1-\frac{|x-m|}{|x|+|m|+ε}.
\]

The theorem family assumes `ε>0`.

**Theorem 1 — Positive denominator.**

\[
ε>0\implies 0<|x|+|m|+ε.
\]

**Theorem 2 — Upper bound.**

\[
ε>0\implies C_ε(x,m)\le1.
\]

**Theorem 3 — Strict lower bound.**

\[
ε>0\implies 0<C_ε(x,m).
\]

**Theorem 4 — Maximum characterization.**

\[
ε>0\implies\bigl(C_ε(x,m)=1\iff x=m\bigr).
\]

The proofs use positivity of the regularized denominator and the triangle inequality `|x-m|≤|x|+|m|`. Thus the score lies in `(0,1]` and reaches one exactly at equality. It is not thereby a probability, a metric, or an empirically calibrated coherence measure.

## 3. ME-066: type-safe dyadic coupling

The source expression schematically adds two `V`-valued states to a tensor-product term in `V⊗V`. Such an addition is ill typed without a common carrier and explicit embeddings. The formalization does not invent either. Instead, for a real module `V`, it defines

\[
D_λ(h,a)=\bigl(h,a,λ(h\otimes a)\bigr)
\in V\times V\times(V\otimes_{\mathbb R}V).
\]

**Theorem 5 — Human projection.** `D_λ(h,a).human=h`.

**Theorem 6 — AI projection.** `D_λ(h,a).ai=a`.

**Theorem 7 — Coupling projection.** `D_λ(h,a).coupling=λ•(h⊗a)`.

**Theorem 8 — Zero gain.** `D_0(h,a).coupling=0`.

**Theorem 9 — Zero human factor.** `D_λ(0,a).coupling=0`.

**Theorem 10 — Zero AI factor.** `D_λ(h,0).coupling=0`.

**Theorem 11 — Componentwise equality.** Two typed dyads are equal if and only if their human, AI, and coupling fields are respectively equal.

The first three are definitional projection theorems; the next three follow from scalar multiplication and tensor bilinearity; the final theorem follows from equality of record fields. The result preserves the three source components without claiming that this carrier, any normalization, or any human–AI ontology is uniquely correct.

## 4. ME-078 and ME-082: exponential relaxation

Define

\[
η(t)=η_0\left(1-e^{-t/τ}\right),\qquad
R(η_{eq},η,τ)=\frac{η_{eq}-η}{τ}.
\]

The formal bridge treats ME-078 as the `η(0)=0`, `η_eq=η₀` special case of ME-082.

**Theorem 12 — Initial value.** `η(0)=0`.

**Theorem 13 — Equilibrium gap.**

\[
η_0-η(t)=η_0e^{-t/τ}.
\]

**Theorem 14 — Rate identity.**

\[
\frac{η_0}{τ}e^{-t/τ}=R(η_0,η(t),τ).
\]

**Theorem 15 — Special-solution theorem.** The function `η` is differentiable and

\[
\frac{dη}{dt}=R(η_0,η(t),τ).
\]

This is the tranche's cross-equation theorem: the proposed ME-078 curve is formally verified as a solution of ME-082 under the encoded equilibrium and initial condition.

**Theorem 16 — Fixed equilibrium.** `R(η_eq,η_eq,τ)=0`.

**Theorem 17 — Positive rate below equilibrium.**

\[
η<η_{eq},\;τ>0\implies R(η_{eq},η,τ)>0.
\]

**Theorem 18 — Negative rate above equilibrium.**

\[
η_{eq}<η,\;τ>0\implies R(η_{eq},η,τ)<0.
\]

The sign theorems establish equilibrium-directed flow for positive `τ`. Lean treats real division as total, so the algebraic statements can have a `τ=0` interpretation; that convention is not a physically admissible zero-time relaxation model. Scientific use must retain `τ>0`.

## 5. Formal catalogue

| No. | Lean declaration | Result |
|---:|---|---|
| 1 | `ME047.coherenceDenominator_pos` | positive denominator |
| 2 | `ME047.recursiveCoherence_le_one` | upper bound |
| 3 | `ME047.recursiveCoherence_pos` | strict lower bound |
| 4 | `ME047.recursiveCoherence_eq_one_iff` | maximum iff equality |
| 5 | `ME066.typedDyad_human` | human projection |
| 6 | `ME066.typedDyad_ai` | AI projection |
| 7 | `ME066.typedDyad_coupling` | coupling projection |
| 8 | `ME066.typedDyad_zero_gain` | zero gain |
| 9 | `ME066.typedDyad_zero_human` | zero human factor |
| 10 | `ME066.typedDyad_zero_ai` | zero AI factor |
| 11 | `ME066.typedDyad_eq_iff` | componentwise equality |
| 12 | `ME078.thixotropicViscosity_initial` | initial value |
| 13 | `ME078.thixotropicViscosity_gap` | equilibrium gap |
| 14 | `ME078.thixotropicViscosity_rate_eq_relaxationRHS` | rate identity |
| 15 | `ME078.thixotropicViscosity_hasDerivAt` | differential bridge |
| 16 | `ME082.equilibrium_is_fixed` | fixed equilibrium |
| 17 | `ME082.relaxation_positive_below_equilibrium` | positive sign below equilibrium |
| 18 | `ME082.relaxation_negative_above_equilibrium` | negative sign above equilibrium |

## 6. Interpretation and limits

The valid conclusion is narrow and concrete. ME-047's specified scalar formula has a sharp range; ME-066's replacement object is type safe and preserves its components; ME-078's curve solves the displayed ME-082 relaxation equation in its designated special case; and ME-082 points toward equilibrium for positive `τ`.

No result establishes a new physical law, shows a material obeys the relaxation model, calibrates a coherence score, proves the source expressions are uniquely correct, or validates EFMW empirically. Those questions require explicit model comparison, data, and independent replication. The value of Tranche II is that it identifies exactly which claims survive formal scrutiny and exactly which assumptions they need.

## 7. Reproducibility

Repository: `https://github.com/enuminous/Monlithic_EFMW_102_Lean4`  
Recorded commit: `ae583082282786384f3280ece6b2a49ed2cc6729`  
Toolchain: Lean 4.19.0 / Mathlib v4.19.0

The build record reports compilation of all 102 corpus modules, with no `sorry`, `admit`, or custom axioms. An independent review should separately verify (1) the kernel build, (2) faithfulness of the Lean definitions to the cited source equations, and (3) adequacy of the scientific assumptions. Only the first is closed by successful compilation.

## Conclusion

Tranche II contributes eighteen Lean-checked propositions selected through an adversarial, dependency-aware route. Its strongest result is the ME-078/ME-082 differential bridge; its most important diagnostic contribution is the conservative repair of ME-066's type mismatch. The appropriate use of these theorems is as audited mathematical infrastructure for further formalization—not as a substitute for empirical validation.
