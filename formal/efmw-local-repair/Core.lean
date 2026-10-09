import Mathlib

/-!
# Observer / discrepancy / local repair core

The model is deliberately small. A graph specifies which coordinates an
observer may inspect. A residual is the observer's discrepancy, and each
coordinate is repaired synchronously by subtracting a nonzero gain times its
residual. Global convergence is a separate contraction hypothesis; locality
alone does not imply it.
-/

namespace EFMW.LocalRepair

universe u v

structure Neighborhood (ι : Type u) where
  adjacent : ι → ι → Prop

def AgreeNear {ι : Type u} (G : Neighborhood ι)
    (x y : ι → ℝ) (i : ι) : Prop :=
  x i = y i ∧ ∀ j, G.adjacent i j → x j = y j

def LocallyDetermined {ι : Type u} (G : Neighborhood ι)
    (f : (ι → ℝ) → ι → ℝ) : Prop :=
  ∀ i x y, AgreeNear G x y i → f x i = f y i

def LocalResidual {ι : Type u} (G : Neighborhood ι)
    (r : (ι → ℝ) → ι → ℝ) : Prop :=
  LocallyDetermined G r

def repairStep {ι : Type u} (r : (ι → ℝ) → ι → ℝ) (η : ℝ)
    (x : ι → ℝ) : ι → ℝ :=
  fun i => x i - η * r x i

theorem repairStep_locallyDetermined {ι : Type u}
    (G : Neighborhood ι) (r : (ι → ℝ) → ι → ℝ) (η : ℝ)
    (hr : LocalResidual G r) :
    LocallyDetermined G (fun x => repairStep r η x) := by
  intro i x y hxy
  simp [repairStep, hxy.1, hr i x y hxy]

theorem repairStep_fixed_iff_residual_zero {ι : Type u}
    (r : (ι → ℝ) → ι → ℝ) (η : ℝ) (hη : η ≠ 0) (x : ι → ℝ) :
    repairStep r η x = x ↔ ∀ i, r x i = 0 := by
  constructor
  · intro h i
    have hi := congrFun h i
    dsimp [repairStep] at hi
    have hmul : η * r x i = 0 := by linarith
    exact (mul_eq_zero.mp hmul).resolve_left hη
  · intro h
    funext i
    simp [repairStep, h i]

/-! ## Contraction and convergence -/

def Contractive {α : Type v} [PseudoMetricSpace α]
    (T : α → α) (q : ℝ) : Prop :=
  ∀ x y, dist (T x) (T y) ≤ q * dist x y

def iterateN {α : Type v} (T : α → α) : ℕ → α → α
  | 0 => id
  | n + 1 => fun x => T (iterateN T n x)

theorem fixedPoint_unique {α : Type v} [MetricSpace α]
    (T : α → α) (q : ℝ) (hT : Contractive T q)
    (hq0 : 0 ≤ q) (hq1 : q < 1) {x y : α}
    (hx : T x = x) (hy : T y = y) : x = y := by
  have hdist : dist x y ≤ q * dist x y := by
    calc
      dist x y = dist (T x) (T y) := by rw [hx, hy]
      _ ≤ q * dist x y := hT x y
  have hnn : 0 ≤ dist x y := dist_nonneg
  have hfac : 0 < 1 - q := by linarith
  have hprod : (1 - q) * dist x y ≤ 0 := by nlinarith [hdist]
  have hzero : dist x y = 0 := by
    by_contra hne
    have hpos : 0 < dist x y := lt_of_le_of_ne hnn (Ne.symm hne)
    have : 0 < (1 - q) * dist x y := mul_pos hfac hpos
    linarith
  exact dist_eq_zero.mp hzero

theorem iterateN_distance_bound {α : Type v} [MetricSpace α]
    (T : α → α) (q : ℝ) (hT : Contractive T q) (hq0 : 0 ≤ q)
    (x xStar : α) (hfix : T xStar = xStar) (n : ℕ) :
    dist (iterateN T n x) xStar ≤ q ^ n * dist x xStar := by
  induction n with
  | zero => simp [iterateN]
  | succ n ih =>
      simp only [iterateN]
      calc
        dist (T (iterateN T n x)) xStar =
            dist (T (iterateN T n x)) (T xStar) := by rw [hfix]
        _ ≤ q * dist (iterateN T n x) xStar := hT _ _
        _ ≤ q * (q ^ n * dist x xStar) :=
              mul_le_mul_of_nonneg_left ih hq0
        _ = q ^ (n + 1) * dist x xStar := by
          rw [pow_succ]
          ring

def TendsToDistanceZero {α : Type v} [PseudoMetricSpace α]
    (s : ℕ → α) (xStar : α) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ N, ∀ n, N ≤ n → dist (s n) xStar < ε

def GeometricDecay (q : ℝ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ N, ∀ n, N ≤ n → q ^ n < ε

theorem iterateN_converges_of_geometric_decay
    {α : Type v} [MetricSpace α]
    (T : α → α) (q : ℝ) (hT : Contractive T q) (hq0 : 0 ≤ q)
    (hdecay : GeometricDecay q) (x xStar : α)
    (hfix : T xStar = xStar) :
    TendsToDistanceZero (fun n => iterateN T n x) xStar := by
  intro ε hε
  let d := dist x xStar
  have hd : 0 ≤ d := dist_nonneg
  obtain ⟨N, hN⟩ := hdecay (ε / (d + 1)) (div_pos hε (by linarith))
  refine ⟨N, ?_⟩
  intro n hn
  have hp0 : 0 ≤ q ^ n := pow_nonneg hq0 n
  have hp := hN n hn
  have hmul : q ^ n * (d + 1) < ε :=
    (lt_div_iff₀ (by linarith : 0 < d + 1)).mp hp
  calc
    dist (iterateN T n x) xStar ≤ q ^ n * dist x xStar :=
      iterateN_distance_bound T q hT hq0 x xStar hfix n
    _ ≤ q ^ n * (d + 1) := by
      dsimp [d]
      exact mul_le_mul_of_nonneg_left (by linarith) hp0
    _ < ε := hmul

/-! ## Small falsifiers: locality without contraction is insufficient. -/

def swapPair (x : ℝ × ℝ) : ℝ × ℝ := (x.2, x.1)

theorem swapPair_two_cycle :
    swapPair (swapPair (0, 1)) = (0, 1) ∧ swapPair (0, 1) ≠ (0, 1) := by
  constructor <;> norm_num [swapPair]

def identityPair (x : ℝ × ℝ) : ℝ × ℝ := x

theorem identityPair_has_two_fixed_points :
    identityPair (0, 0) = (0, 0) ∧
    identityPair (1, 0) = (1, 0) ∧
    (0, 0 : ℝ × ℝ) ≠ (1, 0) := by
  norm_num [identityPair]

end EFMW.LocalRepair
