import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.Prod

/-!
Exact image of the four reduction-log columns for the curve
y² + xy = x³ - x² - 79x + 289 at primes 5, 13, 19.

This file proves an integral lattice statement. FiniteCurve.lean independently
checks the displayed logarithms against Mathlib's elliptic-curve group law.
No statement about the analytic rank or the L-function is made here.
-/

namespace BSDImprovements

/-- Membership in the image, using integer representatives modulo 10, 20, 28. -/
def JoinedImage (a b c : ℤ) : Prop :=
  ∃ x₁ x₂ x₃ x₄ q₅ q₁₃ q₁₉ : ℤ,
    9*x₁ + 5*x₂ + 8*x₃ + 7*x₄ = a + 10*q₅ ∧
    6*x₁ + 8*x₂ + 17*x₃ + 10*x₄ = b + 20*q₁₃ ∧
    9*x₁ + 21*x₂ + 5*x₃ + 25*x₄ = c + 28*q₁₉

/-- The joined image is exactly the parity kernel, not just a proper subgroup. -/
theorem joined_image_iff_even (a b c : ℤ) :
    JoinedImage a b c ↔ Even (a + b + c) := by
  constructor
  · rintro ⟨x₁, x₂, x₃, x₄, q₅, q₁₃, q₁₉, h₅, h₁₃, h₁₉⟩
    refine ⟨12*x₁ + 17*x₂ + 15*x₃ + 21*x₄ - 5*q₅ - 10*q₁₃ - 14*q₁₉, ?_⟩
    omega
  · rintro ⟨k, hk⟩
    -- The three explicit words represent (1,0,1), (0,1,1), and (0,0,2).
    let t := k-a-b
    refine ⟨5*a+3*b+5*t, 5*a+9*b, 3*b, 3*a+2*b+5*t,
      9*a+11*b+8*t, 5*a+8*b+4*t, 8*a+10*b+6*t, ?_, ?_, ?_⟩
    · dsimp [t]; omega
    · dsimp [t]; omega
    · dsimp [t]; omega

/-- A precise obstruction to treating the three reductions as independent. -/
theorem incompatible_triple : ¬ JoinedImage 0 0 1 := by
  rw [joined_image_iff_even]
  norm_num

/-- Every pair of residue coordinates extends to a compatible triple. -/
theorem every_pair_extends (a b : ℤ) : JoinedImage a b (a+b) := by
  rw [joined_image_iff_even]
  exact ⟨a+b, by ring⟩

/-- Changing representatives does not change the parity test. -/
theorem parity_representative_invariant (a b c u v w : ℤ) :
    Even ((a+10*u) + (b+20*v) + (c+28*w)) ↔ Even (a+b+c) := by
  constructor
  · rintro ⟨k, hk⟩
    exact ⟨k-5*u-10*v-14*w, by omega⟩
  · rintro ⟨k, hk⟩
    exact ⟨k+5*u+10*v+14*w, by omega⟩

def JoinedResidues :=
  {v : Fin 10 × Fin 20 × Fin 28 //
    JoinedImage v.1.val v.2.1.val v.2.2.val}

noncomputable instance : Fintype JoinedResidues := by
  classical
  unfold JoinedResidues
  infer_instance

/-- The last coordinate has exactly fourteen choices for each first pair. -/
def joinedResiduesEquiv : (Fin 10 × Fin 20 × Fin 14) ≃ JoinedResidues where
  toFun v := ⟨(v.1, v.2.1,
    ⟨2*v.2.2.val + (v.1.val+v.2.1.val)%2, by omega⟩), by
      apply (joined_image_iff_even _ _ _).mpr
      refine ⟨(v.1.val+v.2.1.val)/2 + v.2.2.val + (v.1.val+v.2.1.val)%2, ?_⟩
      dsimp
      omega⟩
  invFun v := (v.val.1, v.val.2.1, ⟨v.val.2.2.val/2, by omega⟩)
  left_inv v := by
    rcases v with ⟨a, b, c⟩
    simp only [Prod.mk.injEq, true_and]
    apply Fin.ext
    dsimp
    omega
  right_inv v := by
    apply Subtype.ext
    rcases v with ⟨⟨a,b,c⟩, hv⟩
    simp only [Prod.mk.injEq, true_and]
    apply Fin.ext
    dsimp
    obtain ⟨k, hk⟩ := (joined_image_iff_even _ _ _).mp hv
    dsimp at hk
    omega

/-- Exact size of the logarithm image. -/
theorem joined_image_card : Fintype.card JoinedResidues = 2800 := by
  rw [← Fintype.card_congr joinedResiduesEquiv]
  norm_num

/-- The product has twice as many elements as the joined image. -/
theorem joined_image_half_product :
    Fintype.card (Fin 10 × Fin 20 × Fin 28) = 2 * Fintype.card JoinedResidues := by
  rw [joined_image_card]
  norm_num

end BSDImprovements
