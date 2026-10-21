import Mathlib

/-!
RC-001 narrow finite algebraic bridge (CANDIDATE, UNCOMPILED).
No theorem here proves a field equation, physical rotation, or cosmology.
The coordinate curl is defined directly for the frozen rigid family.
-/

namespace RotationConvergence

def hinge (p : ℝ × ℝ) : ℝ × ℝ := (-p.2, p.1)

theorem hinge_sq (p : ℝ × ℝ) : hinge (hinge p) = (-p.1, -p.2) := by
  rcases p with ⟨x, y⟩
  simp [hinge]

def rigidVelocity (ω : ℝ) (p : ℝ × ℝ) : ℝ × ℝ :=
  (-ω * p.2, ω * p.1)

theorem rigidVelocity_is_hinge (ω : ℝ) (p : ℝ × ℝ) :
    rigidVelocity ω p = (ω * (hinge p).1, ω * (hinge p).2) := by
  rcases p with ⟨x, y⟩
  simp [rigidVelocity, hinge]

/-- In this fixed affine family, ∂x(v_y)=ω and ∂y(v_x)=-ω. -/
def frozenCurl (ω : ℝ) : ℝ := ω - (-ω)

theorem frozenCurl_eq_two_omega (ω : ℝ) :
    frozenCurl ω = 2 * ω := by
  dsimp [frozenCurl]
  ring

theorem zero_rate_zero_curl : frozenCurl 0 = 0 := by
  norm_num [frozenCurl]

end RotationConvergence
