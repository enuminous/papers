import Physlib.Electromagnetism.ThreeDimension.MaxwellEquations

set_option maxRecDepth 10000
set_option maxHeartbeats 800000
open Electromagnetism Electromagnetism.ElectromagneticPotential
open SpaceTime Space Time ContDiff

namespace PhyslibAuditWitness

def unitFreeSpace : FreeSpace := ⟨1, 1, by norm_num, by norm_num⟩

lemma zero_smooth : ContDiff ℝ ∞ (0 : ElectromagneticPotential 3) := by
  change ContDiff ℝ ∞ (fun _ : SpaceTime 3 => (0 : Lorentz.Vector 3))
  fun_prop

lemma zero_scalar (c : SpeedOfLight) :
    scalarPotential c (0 : ElectromagneticPotential 3) = 0 := by
  funext t x
  simp [scalarPotential, timeSlice]

lemma zero_vector (c : SpeedOfLight) :
    vectorPotential c (0 : ElectromagneticPotential 3) = 0 := by
  funext t x
  ext i
  simp [vectorPotential, timeSlice]

lemma zero_electric (c : SpeedOfLight) :
    electricField c (0 : ElectromagneticPotential 3) = 0 := by
  funext t x
  simp [electricField, zero_scalar, zero_vector]

lemma zero_matrix (c : SpeedOfLight) :
    magneticFieldMatrix c (0 : ElectromagneticPotential 3) = 0 := by
  funext t x ij
  rcases ij with ⟨i,j⟩
  rw [magneticFieldMatrix_eq_vectorPotential _ (zero_smooth.differentiable (by simp))]
  simp [zero_vector]

lemma zero_stationary (F : FreeSpace) :
    IsExtrema F (0 : ElectromagneticPotential 3) (0 : LorentzCurrentDensity 3) := by
  apply (isExtrema_iff_gauss_ampere_magneticFieldMatrix zero_smooth
    (0 : LorentzCurrentDensity 3) (by exact contDiff_const)).mpr
  intro t x
  simp [zero_electric, zero_matrix]

theorem premises_inhabited : ∃ (F : FreeSpace) (V : ElectromagneticPotential 3)
    (J : LorentzCurrentDensity 3),
    IsExtrema F V J ∧ ContDiff ℝ ∞ V ∧ ContDiff ℝ ∞ J := by
  exact ⟨unitFreeSpace, 0, 0, zero_stationary unitFreeSpace, zero_smooth, contDiff_const⟩

#print axioms premises_inhabited
end PhyslibAuditWitness
