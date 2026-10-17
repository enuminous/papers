import BSDImprovements.FiniteCurve
import BSDImprovements.JoinedPrimes

namespace BSDImprovements

/-- Membership expressed directly in Mathlib's three actual elliptic-curve groups. -/
def CurveJoinedImage (a b c : ℤ) : Prop :=
  ∃ x₁ x₂ x₃ x₄ : ℤ,
    x₁ • p1mod5 + x₂ • p2mod5 + x₃ • p3mod5 + x₄ • p4mod5 = a • gen5 ∧
    x₁ • p1mod13 + x₂ • p2mod13 + x₃ • p3mod13 + x₄ • p4mod13 = b • gen13 ∧
    x₁ • p1mod19 + x₂ • p2mod19 + x₃ • p3mod19 + x₄ • p4mod19 = c • gen19

theorem cyclic_multiple_eq_iff {G : Type*} [AddGroup G] (g : G) (n : ℕ)
    (hg : addOrderOf g = n) (a b : ℤ) :
    a • g = b • g ↔ ∃ q : ℤ, a = b + n*q := by
  rw [← addOrderOf_dvd_sub_iff_zsmul_eq_zsmul, hg]
  constructor
  · rintro ⟨q, hq⟩
    exact ⟨q, by omega⟩
  · rintro ⟨q, hq⟩
    exact ⟨q, by omega⟩

theorem word_mod5 (x₁ x₂ x₃ x₄ : ℤ) :
    x₁ • p1mod5 + x₂ • p2mod5 + x₃ • p3mod5 + x₄ • p4mod5 =
      (9*x₁ + 5*x₂ + 8*x₃ + 7*x₄) • gen5 := by
  rw [← log_p1_mod5, ← log_p2_mod5, ← log_p3_mod5, ← log_p4_mod5]
  simp only [← natCast_zsmul, smul_smul, ← add_zsmul]
  congr 1
  ring

theorem word_mod13 (x₁ x₂ x₃ x₄ : ℤ) :
    x₁ • p1mod13 + x₂ • p2mod13 + x₃ • p3mod13 + x₄ • p4mod13 =
      (6*x₁ + 8*x₂ + 17*x₃ + 10*x₄) • gen13 := by
  rw [← log_p1_mod13, ← log_p2_mod13, ← log_p3_mod13, ← log_p4_mod13]
  simp only [← natCast_zsmul, smul_smul, ← add_zsmul]
  congr 1
  ring

theorem word_mod19 (x₁ x₂ x₃ x₄ : ℤ) :
    x₁ • p1mod19 + x₂ • p2mod19 + x₃ • p3mod19 + x₄ • p4mod19 =
      (9*x₁ + 21*x₂ + 5*x₃ + 25*x₄) • gen19 := by
  rw [← log_p1_mod19, ← log_p2_mod19, ← log_p3_mod19, ← log_p4_mod19]
  simp only [← natCast_zsmul, smul_smul, ← add_zsmul]
  congr 1
  ring

theorem curve_image_iff_log_image (a b c : ℤ) :
    CurveJoinedImage a b c ↔ JoinedImage a b c := by
  unfold CurveJoinedImage JoinedImage
  simp only [word_mod5, word_mod13, word_mod19,
    cyclic_multiple_eq_iff gen5 10 generator_order_mod5,
    cyclic_multiple_eq_iff gen13 20 generator_order_mod13,
    cyclic_multiple_eq_iff gen19 28 generator_order_mod19]
  constructor
  · rintro ⟨x₁,x₂,x₃,x₄,⟨q₅,h₅⟩,⟨q₁₃,h₁₃⟩,⟨q₁₉,h₁₉⟩⟩
    exact ⟨x₁,x₂,x₃,x₄,q₅,q₁₃,q₁₉,h₅,h₁₃,h₁₉⟩
  · rintro ⟨x₁,x₂,x₃,x₄,q₅,q₁₃,q₁₉,h₅,h₁₃,h₁₉⟩
    exact ⟨x₁,x₂,x₃,x₄,⟨q₅,h₅⟩,⟨q₁₃,h₁₃⟩,⟨q₁₉,h₁₉⟩⟩

/-- Exact parity characterization for the actual finite-curve point groups. -/
theorem curve_joined_image_iff_even (a b c : ℤ) :
    CurveJoinedImage a b c ↔ Even (a+b+c) := by
  rw [curve_image_iff_log_image, joined_image_iff_even]

abbrev CurveTriple := (curve (ZMod 5)).Point ×
  (curve (ZMod 13)).Point × (curve (ZMod 19)).Point

def InCurveReductionImage (P : CurveTriple) : Prop :=
  ∃ x₁ x₂ x₃ x₄ : ℤ,
    x₁ • p1mod5 + x₂ • p2mod5 + x₃ • p3mod5 + x₄ • p4mod5 = P.1 ∧
    x₁ • p1mod13 + x₂ • p2mod13 + x₃ • p3mod13 + x₄ • p4mod13 = P.2.1 ∧
    x₁ • p1mod19 + x₂ • p2mod19 + x₃ • p3mod19 + x₄ • p4mod19 = P.2.2

def CurveReductionImage := {P : CurveTriple // InCurveReductionImage P}

noncomputable instance : Fintype CurveReductionImage := by
  classical
  unfold CurveReductionImage
  infer_instance

noncomputable def finiteTripleEquiv :
    (Fin 10 × Fin 20 × Fin 28) ≃ CurveTriple :=
  finiteCurveEquiv5.prodCongr (finiteCurveEquiv13.prodCongr finiteCurveEquiv19)

noncomputable def joinedImageEquiv : JoinedResidues ≃ CurveReductionImage :=
  finiteTripleEquiv.subtypeEquiv (by
    intro v
    change JoinedImage v.1.val v.2.1.val v.2.2.val ↔
      (∃ x₁ x₂ x₃ x₄ : ℤ,
        x₁ • p1mod5 + x₂ • p2mod5 + x₃ • p3mod5 + x₄ • p4mod5 = v.1.val • gen5 ∧
        x₁ • p1mod13 + x₂ • p2mod13 + x₃ • p3mod13 + x₄ • p4mod13 = v.2.1.val • gen13 ∧
        x₁ • p1mod19 + x₂ • p2mod19 + x₃ • p3mod19 + x₄ • p4mod19 = v.2.2.val • gen19)
    rw [← curve_image_iff_log_image]
    simp only [CurveJoinedImage, natCast_zsmul])

/-- End-to-end count in the actual three Mathlib elliptic-curve groups. -/
theorem curve_reduction_image_card : Fintype.card CurveReductionImage = 2800 := by
  rw [← Fintype.card_congr joinedImageEquiv, joined_image_card]

theorem curve_product_card : Fintype.card CurveTriple = 5600 := by
  rw [← Fintype.card_congr finiteTripleEquiv]
  norm_num

theorem curve_reduction_image_half_product :
    Fintype.card CurveTriple = 2 * Fintype.card CurveReductionImage := by
  rw [curve_product_card, curve_reduction_image_card]

end BSDImprovements
