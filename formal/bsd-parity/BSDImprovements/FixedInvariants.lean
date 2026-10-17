import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
A specification component for a repaired refined BSD statement.

All arithmetic inputs are fixed BEFORE the coefficient equality is asserted.
The regulator is computed from the Gram matrix, rather than stored as an
unrelated scalar. This file does NOT construct a canonical height, a Néron
period, Sha, Tamagawa numbers, or an elliptic L-function. Those identifications
are still obligations for any application to an actual elliptic curve.
-/

namespace BSDImprovements

structure FixedInvariants (r : ℕ) where
  gram : Matrix (Fin r) (Fin r) ℝ
  period : ℝ
  shaCard : ℕ
  tamagawaProduct : ℕ
  torsionCard : ℕ

def FixedInvariants.regulator {r : ℕ} (d : FixedInvariants r) : ℝ :=
  d.gram.det

noncomputable def FixedInvariants.predictedCoefficient {r : ℕ} (d : FixedInvariants r) : ℝ :=
  d.period * d.regulator * (d.shaCard : ℝ) * (d.tamagawaProduct : ℝ) /
    (d.torsionCard : ℝ)^2

/-- This is the coefficient clause only; rank equality is a separate obligation. -/
def FixedCoefficientStatement {r : ℕ} (d : FixedInvariants r) (C : ℝ) : Prop :=
  C = d.predictedCoefficient

theorem fixed_coefficient_unique {r : ℕ} (d : FixedInvariants r) (C D : ℝ)
    (hC : FixedCoefficientStatement d C) (hD : FixedCoefficientStatement d D) :
    C = D := hC.trans hD.symm

theorem fixed_coefficient_positive {r : ℕ} (d : FixedInvariants r) (C : ℝ)
    (hC : FixedCoefficientStatement d C)
    (hp : 0 < d.period) (hg : 0 < d.gram.det)
    (hs : 0 < d.shaCard) (ht : 0 < d.tamagawaProduct) (hz : 0 < d.torsionCard) :
    0 < C := by
  rw [hC]
  exact div_pos
    (mul_pos (mul_pos (mul_pos hp hg) (Nat.cast_pos.mpr hs)) (Nat.cast_pos.mpr ht))
    (pow_pos (Nat.cast_pos.mpr hz) 2)

/-- Standard Gram determinant transformation, now enforced by the definition. -/
theorem regulator_under_change (r : ℕ) (G U : Matrix (Fin r) (Fin r) ℝ) :
    (U.transpose * G * U).det = U.det^2 * G.det := by
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose]
  ring

/-- A determinant-one or determinant-minus-one change preserves the regulator. -/
theorem unimodular_change_preserves_regulator (r : ℕ)
    (G U : Matrix (Fin r) (Fin r) ℝ) (hU : U.det = 1 ∨ U.det = -1) :
    (U.transpose * G * U).det = G.det := by
  rw [regulator_under_change]
  rcases hU with hU | hU <;> rw [hU] <;> norm_num

/-- If a frame has change-of-basis determinant k, its Gram determinant scales by k².
Identifying |k| with a Mordell-Weil subgroup index remains an arithmetic obligation. -/
theorem frame_determinant_correction (r : ℕ) (G U : Matrix (Fin r) (Fin r) ℝ)
    (k : ℝ) (hU : U.det = k) : (U.transpose * G * U).det = k^2 * G.det := by
  rw [regulator_under_change, hU]

/-- Positivity alone cannot establish the fixed coefficient clause. -/
theorem positive_coefficient_can_fail_fixed_statement :
    ∃ (d : FixedInvariants 1) (C : ℝ),
      0 < d.period ∧ 0 < d.regulator ∧ 0 < d.shaCard ∧
      0 < d.tamagawaProduct ∧ 0 < d.torsionCard ∧ 0 < C ∧
      ¬ FixedCoefficientStatement d C := by
  refine ⟨⟨1, 1, 1, 1, 1⟩, 2, ?_⟩
  norm_num [FixedCoefficientStatement, FixedInvariants.predictedCoefficient,
    FixedInvariants.regulator]

end BSDImprovements
