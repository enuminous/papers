# Every proved theorem in this project, in plain English

This project formalizes the EFMW equation corpus in Lean 4 and proves 155 theorems
about it. The whole development builds cleanly, contains no `sorry`, and relies only
on Lean's standard axioms.

A word on what "proved" means here. These are proofs *about* the EFMW equations —
that a stated solution really solves its equation, that one item of the corpus follows
from another, that a defined quantity is bounded, that a criterion is or is not
falsifiable. Nothing below asserts that EFMW describes nature; the postulated physical
laws are treated as mathematical hypotheses whose consequences are derived.

Statements are grouped by file, in source order. Names in `code font` are the Lean
identifiers, all in the `EFMW` namespace.

---

## 1. Scalar-field and tensor sector — `RequestProject/EFMW/ScalarField.lean` (15)

1. `EFMWScalarEq_iff_expanded` — ME-005 is exactly ME-002 rewritten using the flat-space
   expansion ME-004 of the d'Alembertian: the two equations say the same thing.
2. `EFMWScalarEq_iff_wave` — the EFMW scalar equation is equivalent to an ordinary wave
   equation in which the time-derivative coefficient is `(1 − α²)/c²` instead of `1/c²`.
3. `hasDerivAt_planeWave_time` — the time derivative of the plane wave `A cos(kx − ωt)`
   is `Aω sin(kx − ωt)`.
4. `deriv_planeWave_time` — the same fact stated as an identity between functions.
5. `dtt_planeWave` — the plane wave's second time derivative is `−ω²` times the wave itself.
6. `hasDerivAt_planeWave_space` — the space derivative of the plane wave is `−Ak sin(kx − ωt)`.
7. `deriv_planeWave_space` — the same fact stated as an identity between functions.
8. `dxx_planeWave` — the plane wave's second space derivative is `−k²` times the wave itself.
9. `planeWave_solves_iff` — **dispersion relation.** A plane wave of nonzero amplitude
   solves the source-free EFMW scalar equation precisely when `(1 − α²)ω² = c²k²`.
10. `planeWave_phase_speed` — **consequence.** For `α² < 1` and positive `k`, `ω`, the
    admissible wave travels at phase speed `ω/k = c/√(1 − α²)`. This is a sharp, testable
    prediction of the postulated equation.
11. `normSq_polarField` — ME-017: the probability density of the polar field `ρe^{iθ}` is `ρ²`.
12. `wrightTensor_eq_scalarStress_add_ricci` — the ME-006 informational tensor is exactly the
    scalar stress tensor (ME-015) plus the Ricci tensor. This is the precise sense in which
    ME-006 is "ME-015 plus recursive informational structure".
13. `modifiedEinstein_iff_unity` — ME-008 is ME-007 with the informational tensor substituted:
    the two field equations are equivalent.
14. `modifiedEinstein_kappa_zero` — at zero coupling `κ = 0` the modified Einstein equation
    reduces exactly to the standard one; EFMW is a conservative extension in `κ`.
15. `maxwellLagrangian_neg` — the Maxwell Lagrangian is quadratic: flipping the sign of the
    field strength leaves it unchanged.

## 2. Coherence metrics — `RequestProject/EFMW/Coherence.lean` (20)

16. `coherence_denom_pos` — the denominator `‖x‖ + ‖m‖ + ε` in the coherence score is positive.
17. `coherenceScore_le_one` — the ME-047 recursive coherence score never exceeds 1.
18. `coherenceScore_pos` — it is always strictly positive (by the triangle inequality).
19. `coherenceScore_nonneg` — hence it is nonnegative.
20. `coherenceScore_eq_one_iff` — it equals 1 exactly when the self-model reproduces the state.
21. `abs_recursiveClosure_le_one` — ME-026: the recursive closure functional
    `⟪a,b⟫/(‖a‖‖b‖ + ε)` has absolute value at most 1 (Cauchy–Schwarz).
22. `recursiveIntegrity_pos` — recursive integrity is strictly positive.
23. `recursiveIntegrity_le_one` — recursive integrity never exceeds 1.
24. `recursiveIntegrity_eq_one_iff` — it equals 1 exactly when the self-model matches both the
    state *and* its rate of change.
25. `divergence_mono_state` — with nonnegative weights, state–model divergence grows with the
    state error.
26. `divergence_nonneg` — with nonnegative weights and a nonpositive recursive-closure term,
    divergence is nonnegative.
27. `warningCriterion_mono` — the ME-028 control-loss warning is monotone: more divergence or
    less coherence can only keep a warning triggered.
28. `warningCriterion_nontrivial` — the warning criterion is not vacuous: it fires on some
    inputs and fails to fire on others.
29. `entropicHarmonyGradient_mul` — the entropic harmony gradient `dS·H/dI` satisfies the
    defining relation `(dS·H/dI)·dI = dS·H` for nonzero `dI`.
30. `risk_mem_unitInterval` — the risk functional `P(1 − C)` stays in `[0,1]` when probability
    and coherence do.
31. `risk_antitone_coherence` — risk decreases as coherence increases.
32. `ethicalWeight_nonneg` — the ethical weight is nonnegative on nonnegative inputs.
33. `gammaMetric_mono` — the ME-100 metric `Γ = Φ·R·C` is monotone in each nonnegative factor,
    so its threshold condition is upward-closed.
34. `identityStep_iterate` — iterating the identity-persistence update `n` times adds exactly
    `n·λC`.
35. `identityStep_tendsto_atTop` — with positive coherence gain, identity persistence increases
    without bound.

## 3. Dynamics — `RequestProject/EFMW/Dynamics.lean` (18)

36. `hasDerivAt_coherencePotential` — the double-well coherence potential
    `U(Φ) = (a/4)Φ⁴ − (b/2)Φ²` has derivative `aΦ³ − bΦ`.
37. `coherencePotential_critical_iff` — its critical points are exactly `Φ = 0` and `Φ² = b/a`.
38. `coherencePotential_ge` — for `a > 0` it is bounded below by `−b²/(4a)`.
39. `coherencePotential_eq_min_iff` — that bound is attained exactly at the coherent minima
    `Φ² = b/a`.
40. `cognitivePotential_ge` — the cognitive potential on an inner-product space obeys the
    coercive lower bound `(a/4)‖z‖⁴ − (b/2)‖z‖² − ‖h‖‖z‖`.
41. `selfModel_zero` — the ME-023 self-model solution starts at its initial value.
42. `selfModel_hasDerivAt` — the proposed solution really does solve the self-model tracking
    equation `ṁ = α(H − m)`.
43. `selfModel_tendsto` — for `α > 0` the self-model converges to the tracked state.
44. `redQueen_equilibrium_iff` — ME-063: the coherence rate vanishes exactly when the Red
    Queen equilibrium condition `αC(1 − C/K) = βD − γḊ` holds.
45. `redQueen_equilibrium_exists` — an equilibrium coherence level in `[0, K/2]` exists
    whenever the environmental demand is nonnegative and does not exceed `αK/4`.
46. `viscosity_hasDerivAt` — ME-082: the thixotropic law `η(t) = η₀(1 − e^{−t/τ})` solves the
    relaxation equation `dη/dt = (η₀ − η)/τ`.
47. `viscosity_zero` — that law starts from zero viscosity.
48. `decayDensity_hasDerivAt` — ME-079: the exponential decay law solves `dρ/dt = −ρ/τ`.
49. `emergentPhase_hasDerivAt` — ME-075: accumulated recursive phase `Θ(t) = ∫₀ᵗ ω_rec`
    differentiates back to `ω_rec`, so the corpus's relation `dt = dΘ/ω_rec` is the
    fundamental theorem of calculus.
50. `emergentPhase_strictMono` — with a strictly positive recursive frequency, emergent time
    is a strictly monotone reparametrization of ordinary time.
51. `successive_increments_tendsto_zero` — ME-096: a convergent recursion has vanishing
    successive increments.
52. `perturbation_recovery` — ME-032: a trajectory converging to the attractor has vanishing
    deviation from it.
53. `lyapunov_negative_tendsto_zero` — ME-033: a perturbation bounded by `M e^{λt}` with
    `λ < 0` decays to zero.

## 4. Cognitive fields — `RequestProject/EFMW/CognitiveFields.lean` (15)

54. `recursiveLagrangian_le` — the divergence penalties can only lower the recursive Lagrangian
    below `λΦR`.
55. `recursiveLagrangian_eq` — equality holds exactly in the perfectly self-modeling case.
56. `recursiveStateEq_lam_zero` — switching off the recursive coupling recovers the baseline
    state dynamics `ẋ = f`.
57. `orderParamRHS_eq_neg_grad` — ME-024/025: in the noiseless, perfectly self-modeling limit
    with no recursive-closure drive, the order-parameter equation is exactly gradient descent
    on the double-well coherence potential.
58. `gradientFlow_potential_nonincreasing` — ME-069: along the cognitive attractor flow
    `ż = −∇V(z)`, the potential changes at rate `−(V'(z))² ≤ 0`, so it never increases.
59. `puddleRHS_symm` — with equal cross-coupling constants, the two-field "puddle" system is
    symmetric under exchanging the system field with the observer field.
60. `cognitivePressure_nonneg` — cognitive pressure is nonnegative on nonnegative demands.
61. `cognitivePressure_mono` — it increases with social demand.
62. `cognitiveTensor_symm` — the cognitive tensor is symmetric whenever the metric is.
63. `cognitiveCurvature_zero_irec` — with no recursive information the cognitive curvature
    equation reduces to pure thought-density sourcing.
64. `phiTiled_eq` — the φ-tiled operator is the affine combination
    `(2 − φ)·A(φX) + (φ − 1)·X`.
65. `phiTiled_weights_sum` — those two weights sum to 1, so the combination is affine.
66. `memoryUpdate_gt_iff` — a memory weight grows exactly when contextual coherence outweighs
    the penalized prediction error.
67. `nullPair_consistent` — ME-087: the null-pair relation `e₁e₂ = 0` with both factors nonzero
    is consistent — such a commutative ring exists.
68. `identityAttractor_iff` — ME-031: joint convergence of state, self-model and order parameter
    to an identity attractor is exactly componentwise convergence.

## 5. Quantum sector — `RequestProject/EFMW/QuantumSector.lean` (9)

69. `phaseCurrent_const_of_continuity` — ME-019: the stationary continuity equation `∇·J = 0`
    forces the phase current to be spatially constant.
70. `gaussianAmplitude_pos` — the Gaussian amplitude is everywhere positive.
71. `hasDerivAt_gaussianAmplitude` — its derivative is `−x` times itself.
72. `deriv_gaussianAmplitude` — the same, as an identity between functions.
73. `d2_gaussianAmplitude` — its second derivative satisfies `ρ'' = (x² − 1)ρ`.
74. `quantumPotential_gaussian` — ME-021: for a Gaussian amplitude the quantum potential is the
    harmonic-oscillator expression `Q(x) = −(ħ²/2m)(x² − 1)`.
75. `quantumHJ_freeParticle` — the free-particle phase `S(t,x) = px − p²t/(2m)` solves the
    quantum Hamilton–Jacobi equation with vanishing classical and quantum potentials.
76. `norm_normalize` — normalizing a nonzero vector produces a unit vector; this is the content
    of the ME-060 state-update rule.
77. `dyad_norm_one` — ME-066: the normalized dyadic cognition state
    `Ψ_dyad = N(Ψ_H + Ψ_A + λ Ψ_H⊗Ψ_A)` is a unit vector whenever the raw combination is nonzero.

## 6. Cosmology and force sector — `RequestProject/EFMW/Cosmology.lean` (8)

78. `emergenceForce_restoring_inner` — ME-051: inside the coherent well the emergence force
    pushes the order parameter up towards the minimum at `Φ² = b/a`.
79. `emergenceForce_restoring_outer` — outside the well it pushes back inwards; together with
    the previous item, the force is restoring.
80. `fifthForce_const` — a spatially uniform coherence field exerts no fifth force.
81. `modifiedGeodesic_beta_zero` — at zero scalar coupling the modified geodesic equation is
    exactly the standard geodesic equation; the extension is conservative in `β_φ`.
82. `friedmann_deviation` — ME-058: the EFMW Friedmann equation exceeds the ΛCDM right-hand
    side by exactly `Ω_U²/a²`.
83. `friedmannEFMW_ge` — residual cosmic rotation can only increase the expansion rate.
84. `friedmannEFMW_lt_iff` — the increase is strict precisely when the residual rotation is
    nonzero.
85. `effectiveDensity_ge` — the EFMW effective density is at least the ΛCDM density when the
    rotational, linear and high-energy contributions are nonnegative.

## 7. Information sector — `RequestProject/EFMW/Information.lean` (11)

86. `shannonEntropy_nonneg` — ME-034: phrase entropy is nonnegative on a probability vector.
87. `kl_term_ge` — the pointwise Gibbs inequality `a − b ≤ a log(a/b)`.
88. `klDivergence_nonneg` — **Gibbs' inequality:** the KL divergence between two probability
    vectors is nonnegative.
89. `shannonEntropy_le_log_card` — entropy on a nonempty finite alphabet of `n` symbols is at
    most `log n`.
90. `mutualInformation_comm` — mutual information is symmetric in its two arguments.
91. `collapseProb_nonneg` — Born-type collapse probabilities are nonnegative.
92. `collapseProb_sum_eq_one` — ME-061/071: they sum to 1 for any nonzero amplitude vector.
93. `collapse_argmin_exists` — ME-059: the Collapse-Ω functional is well posed on a finite
    nonempty outcome set — a minimizer exists.
94. `kuramoto_nonneg` — the ME-091 Kuramoto order parameter is nonnegative.
95. `kuramoto_le_one` — it never exceeds 1.
96. `kuramoto_of_const` — it equals exactly 1 at perfect phase synchronization.

## 8. Golden-ratio scaling — `RequestProject/EFMW/GoldenScaling.lean` (13)

97. `phi_eq` — `φ = (1 + √5)/2`.
98. `phi_sq` — the defining identity `φ² = φ + 1`.
99. `one_lt_phi` — `φ > 1`.
100. `phi_pos` — `φ > 0`.
101. `scalar46_eq_scalar23_sq` — ME-043: the asserted identity `φ⁴⁶ = (φ²³)²` holds.
102. `phi_pow_succ` — every power of φ is a Fibonacci combination: `φ^(n+1) = F(n+1)φ + F(n)`.
103. `scalar23_eq` — closed form for the Scalar-23 coefficient: `φ²³ = 28657φ + 17711`.
104. `scalar23_pos` — that coefficient is positive.
105. `S23_add` — the Scalar-23 operator is additive.
106. `S23_smul` — it commutes with scalar multiplication; with the previous item, it is linear.
107. `S23_injective` — it is injective, so it loses no information.
108. `S23_zero` — ME-086/088: it fixes the null state, so the recursive rebirth operator
     produces coherence only from a nonzero seed.
109. `phase_sync_unique` — ME-045: `T = ΔΦ/f` is the unique time satisfying `f·T = ΔΦ`.

## 9. Actions and fluids — `RequestProject/EFMW/ActionsAndFluids.lean` (6)

110. `action_decomposition` — ME-009: the unified EFMW action decomposes into the sum of its
     gravitational, matter, electromagnetic, scalar and recursive sector actions.
111. `semiclassicalEq_no_efmw_sources` — dropping the EFMW sources recovers the semiclassical
     Einstein equation.
112. `relNavierStokes_inviscid` — with no viscous stress and no external force, the model
     reduces to the relativistic Euler equation `ρu̇ = −∇P`.
113. `density_stationary_of_uniform_flux` — a spatially uniform mass flux forces the density to
     be constant in time.
114. `fluidStress_symm` — the fluid stress tensor is symmetric whenever the metric and shear
     tensors are.
115. `torus888_mem_torus` — the 8-8-8 toroidal mapping is well defined: both of its components
     land on the unit circle.

## 10. Systems, governance and the pilot criterion — `RequestProject/EFMW/Systems.lean` (18)

116. `leadTime_pos_iff` — warning lead time is positive exactly when the alarm precedes the
     failure.
117. `warningUtility_nonneg` — warning utility is nonnegative for admissible false-alarm rates
     and positive compute cost.
118. `warningUtility_mono_lead` — it increases with lead time.
119. `warningUtility_antitone_far` — it decreases as the false-alarm rate grows.
120. `basinFraction_nonneg` — the basin fraction of an attractor is nonnegative.
121. `basinFraction_le_one` — it never exceeds 1.
122. `closurePair_bijective` — recursive closure preserves bijectivity: if the observer and
     system maps are bijections, so is every stage of the mutual recursion.
123. `logos_recursion_unique` — ME-064: the LOGOS recursion is a well-founded definition —
     for any update rule and initial state there is exactly one trajectory.
124. `chronoLogos_reversible` — ME-073: an evolution family valued in bijections is inverted by
     its negative-time member.
125. `chronoLogos_involution_iff` — ME-074: the time-reversal condition `T⁻¹UT = U⁻¹` holds
     exactly when conjugation by `T` inverts the evolution.
126. `evidenceStep_iterate` — iterating the evidence update `n` times adds exactly `n·(dE·C)`.
127. `confidenceStep_lt_iff` — confidence increases exactly when evidence exceeds error.
128. `legalCoherence_eq_zero_iff` — the legal coherence functional collapses to zero exactly
     when one of its three factors is absent.
129. `constitutional_argmax_exists` — ME-097: the constitutional constraint
     `A(x) = argmax[Benefit − Harm]` is well posed over a finite nonempty action set.
130. `accept_satisfiable` — ME-102: some pilot outcome passes the acceptance criterion.
131. `accept_falsifiable` — some pilot outcome fails it, so the criterion is a genuine test and
     not automatically met.
132. `accept_requires_replication` — each clause is load-bearing: failure to replicate alone
     blocks acceptance, even with a perfect lead time.
133. `accept_mono` — acceptance is monotone in the quality of the evidence: better lead time,
     lower false-alarm rate and lower compute cost cannot turn an accepted pilot into a
     rejected one.

## 11. Cross-sector synthesis — `RequestProject/EFMW/Synthesis.lean` (5)

134. `unity_signature_universally_satisfiable` — ME-001: as literally written,
     "EFMW = F(φ, R, C, Ω)" is a signature, not a claim. Every assignment of outcomes to the
     four arguments is realized by some `F`, so nothing can contradict it until `F` is specified.
135. `unity_signature_two_distinct_functionals` — correspondingly, at least two distinct
     functionals `F` are available, so the form fixes nothing on its own.
136. `no_warning_at_perfect_coherence` — cross-sector consistency (ME-027/028/047): a perfectly
     self-modeling system with nonnegative recursive closure has nonpositive divergence, so the
     EFMW control-loss monitor raises no false alarm on it.
137. `tracking_implies_asymptotic_coherence` — if the self-model converges to the state, the
     coherence score converges to its maximum value 1.
138. `selfModel_coherence_tendsto_one` — concretely, the ME-023 tracking law drives the ME-047
     coherence score to 1.

## 12. What a physical test could establish — `RequestProject/EFMW/PhysicalTest.lean` (17)

A measurement is modelled the way experiments work: a theory-predicted observable as a function
of a parameter, a reading, and an error bar. A parameter value is *compatible* with the
measurement when the prediction sits inside the error bar.

139. `Measurement.Compatible_of_strict` — strict compatibility implies compatibility.
140. `eventually_strictlyCompatible` — strict compatibility with finite data is an open
     condition: it persists throughout a neighbourhood of any parameter value satisfying it.
141. `no_exact_parameter_verification` — **no experiment verifies an exact parameter value.**
     If a finite body of finite-precision data is strictly compatible with a parameter value,
     and the predicted observables depend continuously on the parameter, then the very same data
     are compatible with some *different* value. Measurement can bound a parameter; it can never
     pin it down. (This is not a special weakness of EFMW — it holds of any quantitative theory.)
142. `measurement_discriminates` — **a measurement can refute.** If two parameter values are
     predicted to differ by more than twice the error bar, no reading is compatible with both,
     so the experiment rules at least one out.
143. `falsification_by_measurement` — concretely, finite data can be flatly inconsistent with a
     parameter value: compatibility is not a vacuous criterion.
144. `sqrt_one_sub_sq_pos` — `√(1 − α²) > 0` when `α² < 1`.
145. `sqrt_one_sub_sq_le_one` — `√(1 − α²) ≤ 1`.
146. `le_phaseSpeed` — EFMW scalar waves are never slower than light.
147. `lt_phaseSpeed` — a nonzero coupling makes them strictly faster, so the prediction is sharp.
148. `alpha_sq_le_of_speed_measurement` — **a null result bounds the coupling.** If a measured
     scalar-wave speed agrees with `c` to precision `p`, then `α²(c + p)² ≤ p² + 2pc`.
149. `alpha_eq_zero_of_exact_lightspeed` — in the perfect-measurement limit that bound forces
     `α = 0`: an exactly light-speed scalar wave is inconsistent with a nonzero EFMW coupling.
150. `phaseSpeed_gap` — the predicted speed is monotone in `|α|`, so a coupling bounded away
     from zero puts a definite gap between the EFMW prediction and `c`.
151. `speed_experiment_discriminates` — with an error bar smaller than half that gap, no single
     reading is compatible with both `α = 0` and `|α| ≥ ε`.
152. `decisive_precision_exists` — hence a decisive experiment exists in principle: for every
     coupling bounded away from zero there is a positive precision at which the measurement
     rules out one of the two hypotheses.
153. `OmegaU_sq_le_of_hubble_measurement` — **a null cosmological result bounds the residual
     rotation.** If the measured expansion rate agrees with ΛCDM to precision `δ`, then
     `Ω_U² ≤ δa²`.
154. `OmegaU_eq_zero_of_exact_hubble` — exact agreement forces `Ω_U = 0`.
155. `physical_test_asymmetry` — **the epistemic asymmetry, in one statement.** A
     finite-precision experiment can refute an EFMW parameter hypothesis, but no
     finite-precision experiment can verify one. The "physical proof" available to EFMW is
     therefore only the negative kind: survival of attempted refutation, plus bounds on `α` and
     `Ω_U` that shrink with experimental precision.

---

**Total: 155 proved theorems**, distributed as: ScalarField 15, Coherence 20, Dynamics 18,
CognitiveFields 15, QuantumSector 9, Cosmology 8, Information 11, GoldenScaling 13,
ActionsAndFluids 6, Systems 18, Synthesis 5, PhysicalTest 17.
