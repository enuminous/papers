# EFMW theorem continuation — adaptive tranche 2

## Outcome

This continuation converted four high-information zoo findings into **18 Lean theorem declarations**. All 102 equation modules compile together under Lean 4.19.0 and Mathlib 4.19.0. The Lean sources contain no `sorry`, `admit`, or custom `axiom` declarations.

The result is a mathematical audit of the written definitions. It is not empirical confirmation of EFMW and does not supply missing physical semantics.

## Adaptive route

| Equation | Zoo route used | Finding promoted to theorem form |
|---|---|---|
| ME-066 | SALMON → MAGPIE → CAT → DRAGON → WEASEL → TURTLE | The source adds vector states to a tensor state without a common embedding; use a typed product record that loses none of the three terms. |
| ME-078 | SALMON → CAT → WEASEL → TURTLE | The exponential curve is a special solution, not a general thixotropy law. |
| ME-082 | SALMON → CAT → CROCODILE → PENGUIN → TURTLE | The first-order relaxation field points toward equilibrium for positive relaxation time. |
| ME-047 | TORTOISE → BAT → TURTLE | The normalized distance has rigorous range and equality properties when the regularizer is positive. |

ME-066 was selected first because the zoo found a genuine typing obstruction. Its result favored a type-repair theorem family. ME-078 then selected its parent equation ME-082, allowing a cross-equation solution theorem. ME-047 supplied the next high-yield bounds family.

## Checked theorems in ordinary English

### ME-047 — recursive coherence

1. `coherenceDenominator_pos`: if the regularizer ε is positive, then the denominator `|x| + |m| + ε` is positive.
2. `recursiveCoherence_le_one`: with positive ε, recursive coherence can never exceed one.
3. `recursiveCoherence_pos`: with positive ε, recursive coherence is strictly greater than zero.
4. `recursiveCoherence_eq_one_iff`: with positive ε, recursive coherence equals one exactly when `x = m`.

Together these prove `0 < C ≤ 1` and characterize the maximum score.

### ME-066 — typed human–AI dyad

5. `typedDyad_human`: the human component of the typed dyad is exactly the supplied human state.
6. `typedDyad_ai`: the AI component is exactly the supplied AI state.
7. `typedDyad_coupling`: the coupling component is exactly `λ` times the human–AI tensor product.
8. `typedDyad_zero_gain`: zero coupling gain makes the tensor interaction zero.
9. `typedDyad_zero_human`: a zero human state makes the tensor interaction zero.
10. `typedDyad_zero_ai`: a zero AI state makes the tensor interaction zero.
11. `typedDyad_eq_iff`: two typed dyads are equal exactly when their human fields, AI fields, and coupling fields are all equal.

This is a conservative repair of the source expression: it does not invent an embedding or normalization map.

### ME-078 — exponential viscosity curve

12. `thixotropicViscosity_initial`: at time zero, the written curve has viscosity zero.
13. `thixotropicViscosity_gap`: its remaining gap to `η₀` is `η₀ exp(-t/τ)`.
14. `thixotropicViscosity_rate_eq_relaxationRHS`: its algebraic rate equals the right-hand side of ME-082's relaxation law.
15. `thixotropicViscosity_hasDerivAt`: the curve is differentiable and its derivative equals ME-082's relaxation right-hand side.

Thus the zoo's “special solution” classification is formally established. Lean's real-number division is totalized, so the theorem also has a formal value at `τ = 0`; a physical relaxation-time interpretation should impose `τ > 0`.

### ME-082 — relaxation direction

16. `equilibrium_is_fixed`: at equilibrium the relaxation rate is zero.
17. `relaxation_positive_below_equilibrium`: if `τ > 0` and viscosity is below equilibrium, the relaxation rate is positive.
18. `relaxation_negative_above_equilibrium`: if `τ > 0` and viscosity is above equilibrium, the relaxation rate is negative.

These sign theorems establish local direction toward equilibrium; they do not alone prove global convergence for every separately specified dynamical system.

## Verification

- Toolchain: Lean 4.19.0.
- Dependency: Mathlib pinned to `v4.19.0` in `lakefile.lean` and resolved in `lake-manifest.json`.
- Whole-project command: `lake build`.
- Result: successful build of `Monolithic102.All`, importing ME-001 through ME-102.
- Proof-hole scan: no `sorry`, `admit`, or custom `axiom` in any Lean source.

## Next adaptive target

The next efficient branch is **ME-067**, selected by ME-066's zoo result. The right animal route should begin with SALMON and CAT to determine whether ME-067 inherits the repaired dyad type, then use BAT or WEASEL according to whether the expression becomes a bounded metric or remains under-specified. ME-048 is the natural secondary target because it is the next homologue after ME-047.
