# Aristotle EFMW Lean — 156-Theorem Total Novelty / Relativity / Axiom Audit

Source: the 12 Aristotle Lean modules in `RequestProject/EFMW/` (156 theorem declarations).

## Classification key
- **N0** standard mathematics / textbook identity / routine corollary.
- **N1** EFMW-specific formalization or specialization; likely original as corpus analysis, not as general mathematics.
- **N2** cross-equation/model-specific deduction; potentially original to EFMW, but built from known mathematics.
- **P2** model-specific empirical consequence of an EFMW postulate; candidate physics, but the theory class has prior art.
- **A0–A3** increasing dependence on definitions, physical postulates, or conclusion-encoding assumptions.
- **R0–R3** increasing direct relevance to relativity/covariance/causality.

## Full theorem ledger

|#|Module|Theorem|Novelty|Axiom behavior|Relativity|Candidate law|Audit note|
|---:|---|---|---|---|---|---|---|
|1|ActionsAndFluids|`action_decomposition`|N0|A0|R0|—|Standard linearity/reduction/symmetry/trigonometric fact; theorem verifies internal consistency of the encoded sector.|
|2|ActionsAndFluids|`semiclassicalEq_no_efmw_sources`|N1|A2|R2|—|Standard linearity/reduction/symmetry/trigonometric fact; theorem verifies internal consistency of the encoded sector.|
|3|ActionsAndFluids|`relNavierStokes_inviscid`|N1|A2|R1|—|Standard linearity/reduction/symmetry/trigonometric fact; theorem verifies internal consistency of the encoded sector.|
|4|ActionsAndFluids|`density_stationary_of_uniform_flux`|N0|A2|R1|—|Standard linearity/reduction/symmetry/trigonometric fact; theorem verifies internal consistency of the encoded sector.|
|5|ActionsAndFluids|`fluidStress_symm`|N0|A2|R1|—|Standard linearity/reduction/symmetry/trigonometric fact; theorem verifies internal consistency of the encoded sector.|
|6|ActionsAndFluids|`torus888_mem_torus`|N0|A0|R0|—|Standard linearity/reduction/symmetry/trigonometric fact; theorem verifies internal consistency of the encoded sector.|
|7|CognitiveFields|`recursiveLagrangian_le`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|8|CognitiveFields|`recursiveLagrangian_eq`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|9|CognitiveFields|`recursiveStateEq_lam_zero`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|10|CognitiveFields|`orderParamRHS_eq_neg_grad`|N2|A2|R0|L4|Important cross-link ME-024↔ME-025, but quartic double-well gradient flow is classic Landau/Allen–Cahn structure.|
|11|CognitiveFields|`gradientFlow_potential_nonincreasing`|N0|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|12|CognitiveFields|`puddleRHS_symm`|N1|A2|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|13|CognitiveFields|`cognitivePressure_nonneg`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|14|CognitiveFields|`cognitivePressure_mono`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|15|CognitiveFields|`cognitiveTensor_symm`|N1|A2|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|16|CognitiveFields|`cognitiveCurvature_zero_irec`|N1|A2|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|17|CognitiveFields|`phiTiled_eq`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|18|CognitiveFields|`phiTiled_weights_sum`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|19|CognitiveFields|`memoryUpdate_gt_iff`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|20|CognitiveFields|`nullPair_consistent`|N1|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|21|CognitiveFields|`identityAttractor_iff`|N0|A1|R0|—|Mostly direct consequences of constructed cognitive-field definitions; new terminology does not imply new mathematics or physics.|
|22|Coherence|`coherence_denom_pos`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|23|Coherence|`coherenceScore_le_one`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|24|Coherence|`coherenceScore_pos`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|25|Coherence|`coherenceScore_nonneg`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|26|Coherence|`coherenceScore_eq_one_iff`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|27|Coherence|`abs_recursiveClosure_le_one`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|28|Coherence|`recursiveIntegrity_pos`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|29|Coherence|`recursiveIntegrity_le_one`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|30|Coherence|`recursiveIntegrity_eq_one_iff`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|31|Coherence|`divergence_mono_state`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|32|Coherence|`divergence_nonneg`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|33|Coherence|`warningCriterion_mono`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|34|Coherence|`warningCriterion_nontrivial`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|35|Coherence|`entropicHarmonyGradient_mul`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|36|Coherence|`risk_mem_unitInterval`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|37|Coherence|`risk_antitone_coherence`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|38|Coherence|`ethicalWeight_nonneg`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|39|Coherence|`gammaMetric_mono`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|40|Coherence|`identityStep_iterate`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|41|Coherence|`identityStep_tendsto_atTop`|N1|A1|R0|—|Well-posedness/monotonicity of a defined score or recursion; useful engineering semantics, not new general mathematics.|
|42|Cosmology|`emergenceForce_restoring_inner`|N1|A2|R0|—|Model-specific physical interpretation rests on postulated definitions; underlying force/gradient and Friedmann algebra are standard.|
|43|Cosmology|`emergenceForce_restoring_outer`|N1|A2|R0|—|Model-specific physical interpretation rests on postulated definitions; underlying force/gradient and Friedmann algebra are standard.|
|44|Cosmology|`fifthForce_const`|N1|A2|R2|—|Model-specific physical interpretation rests on postulated definitions; underlying force/gradient and Friedmann algebra are standard.|
|45|Cosmology|`modifiedGeodesic_beta_zero`|N1|A2|R2|—|Model-specific physical interpretation rests on postulated definitions; underlying force/gradient and Friedmann algebra are standard.|
|46|Cosmology|`friedmann_deviation`|N1|A2|R2|L3|Directly unfolds the postulated Friedmann extension. For constant Ω_U, the term is algebraically degenerate with spatial curvature: k_eff=k−Ω_U².|
|47|Cosmology|`friedmannEFMW_ge`|N1|A2|R2|L3|Correct consequence of the +Ω_U²/a² definition; adds no independent derivation of cosmic rotation.|
|48|Cosmology|`friedmannEFMW_lt_iff`|N1|A2|R2|L3|Correct consequence of the +Ω_U²/a² definition; adds no independent derivation of cosmic rotation.|
|49|Cosmology|`effectiveDensity_ge`|N1|A2|R2|—|Model-specific physical interpretation rests on postulated definitions; underlying force/gradient and Friedmann algebra are standard.|
|50|Dynamics|`hasDerivAt_coherencePotential`|N0|A0|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|51|Dynamics|`coherencePotential_critical_iff`|N0|A0|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|52|Dynamics|`coherencePotential_ge`|N0|A0|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|53|Dynamics|`coherencePotential_eq_min_iff`|N0|A0|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|54|Dynamics|`cognitivePotential_ge`|N1|A1|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|55|Dynamics|`selfModel_zero`|N1|A1|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|56|Dynamics|`selfModel_hasDerivAt`|N1|A1|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|57|Dynamics|`selfModel_tendsto`|N1|A1|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|58|Dynamics|`redQueen_equilibrium_iff`|N1|A1|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|59|Dynamics|`redQueen_equilibrium_exists`|N1|A1|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|60|Dynamics|`viscosity_hasDerivAt`|N1|A2|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|61|Dynamics|`viscosity_zero`|N1|A2|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|62|Dynamics|`decayDensity_hasDerivAt`|N1|A2|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|63|Dynamics|`emergentPhase_hasDerivAt`|N1|A2|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|64|Dynamics|`emergentPhase_strictMono`|N1|A2|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|65|Dynamics|`successive_increments_tendsto_zero`|N0|A0|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|66|Dynamics|`perturbation_recovery`|N0|A0|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|67|Dynamics|`lyapunov_negative_tendsto_zero`|N0|A0|R0|—|Standard calculus/ODE/dynamical-systems result specialized to EFMW notation; physical interpretation depends on the postulated model.|
|68|GoldenScaling|`phi_eq`|N0|A0|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|69|GoldenScaling|`phi_sq`|N0|A0|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|70|GoldenScaling|`one_lt_phi`|N0|A0|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|71|GoldenScaling|`phi_pos`|N0|A0|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|72|GoldenScaling|`scalar46_eq_scalar23_sq`|N1|A1|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|73|GoldenScaling|`phi_pow_succ`|N0|A0|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|74|GoldenScaling|`scalar23_eq`|N1|A1|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|75|GoldenScaling|`scalar23_pos`|N1|A1|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|76|GoldenScaling|`S23_add`|N1|A1|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|77|GoldenScaling|`S23_smul`|N1|A1|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|78|GoldenScaling|`S23_injective`|N1|A1|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|79|GoldenScaling|`S23_zero`|N1|A1|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|80|GoldenScaling|`phase_sync_unique`|N1|A1|R0|—|Golden-ratio/Fibonacci/scalar multiplication identity. No physical mechanism or dimensional prediction is established by the theorem.|
|81|Information|`shannonEntropy_nonneg`|N0|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|82|Information|`kl_term_ge`|N0|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|83|Information|`klDivergence_nonneg`|N0|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|84|Information|`shannonEntropy_le_log_card`|N0|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|85|Information|`mutualInformation_comm`|N0|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|86|Information|`collapseProb_nonneg`|N1|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|87|Information|`collapseProb_sum_eq_one`|N1|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|88|Information|`collapse_argmin_exists`|N1|A1|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|89|Information|`kuramoto_nonneg`|N0|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|90|Information|`kuramoto_le_one`|N0|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|91|Information|`kuramoto_of_const`|N0|A0|R0|—|Textbook information/statistical-mechanics mathematics (entropy, KL, Born normalization, finite argmin, Kuramoto bounds).|
|92|PhysicalTest|`Measurement.Compatible_of_strict`|N1|A3|R0|—|Routine consequence of stated definitions and hypotheses.|
|93|PhysicalTest|`eventually_strictlyCompatible`|N1|A3|R0|—|Routine consequence of stated definitions and hypotheses.|
|94|PhysicalTest|`no_exact_parameter_verification`|N1|A3|R0|—|Standard openness/continuity result. Scope is finite data, strict interior fit, continuous real parameter; not a universal theorem that all exact parameters are unknowable.|
|95|PhysicalTest|`measurement_discriminates`|N1|A3|R0|—|Routine consequence of stated definitions and hypotheses.|
|96|PhysicalTest|`falsification_by_measurement`|N1|A1|R0|—|Routine consequence of stated definitions and hypotheses.|
|97|PhysicalTest|`phaseSpeed_zero`|N1|A1|R3|—|Routine consequence of stated definitions and hypotheses.|
|98|PhysicalTest|`sqrt_one_sub_sq_pos`|N1|A1|R3|—|Routine consequence of stated definitions and hypotheses.|
|99|PhysicalTest|`sqrt_one_sub_sq_le_one`|N1|A1|R3|—|Routine consequence of stated definitions and hypotheses.|
|100|PhysicalTest|`le_phaseSpeed`|P2|A2|R3|L1|Empirical consequences of the scalar speed formula. Valuable test design; not independent physical laws.|
|101|PhysicalTest|`lt_phaseSpeed`|P2|A2|R3|L1|Empirical consequences of the scalar speed formula. Valuable test design; not independent physical laws.|
|102|PhysicalTest|`alpha_sq_le_of_speed_measurement`|P2|A2|R3|L1|Empirical consequences of the scalar speed formula. Valuable test design; not independent physical laws.|
|103|PhysicalTest|`alpha_eq_zero_of_exact_lightspeed`|P2|A2|R3|L1|Empirical consequences of the scalar speed formula. Valuable test design; not independent physical laws.|
|104|PhysicalTest|`phaseSpeed_gap`|P2|A2|R3|L1|Empirical consequences of the scalar speed formula. Valuable test design; not independent physical laws.|
|105|PhysicalTest|`speed_experiment_discriminates`|P2|A2|R3|L1|Empirical consequences of the scalar speed formula. Valuable test design; not independent physical laws.|
|106|PhysicalTest|`decisive_precision_exists`|P2|A2|R3|L1|Empirical consequences of the scalar speed formula. Valuable test design; not independent physical laws.|
|107|PhysicalTest|`OmegaU_sq_le_of_hubble_measurement`|P2|A2|R2|L3|Correct consequence of the +Ω_U²/a² definition; adds no independent derivation of cosmic rotation.|
|108|PhysicalTest|`OmegaU_eq_zero_of_exact_hubble`|P2|A2|R2|L3|Correct consequence of the +Ω_U²/a² definition; adds no independent derivation of cosmic rotation.|
|109|PhysicalTest|`physical_test_asymmetry`|P2|A2|R3|L1|Empirical consequences of the scalar speed formula. Valuable test design; not independent physical laws.|
|110|QuantumSector|`phaseCurrent_const_of_continuity`|N1|A2|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|111|QuantumSector|`gaussianAmplitude_pos`|N0|A0|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|112|QuantumSector|`hasDerivAt_gaussianAmplitude`|N0|A0|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|113|QuantumSector|`deriv_gaussianAmplitude`|N0|A0|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|114|QuantumSector|`d2_gaussianAmplitude`|N0|A0|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|115|QuantumSector|`quantumPotential_gaussian`|N1|A2|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|116|QuantumSector|`quantumHJ_freeParticle`|N0|A2|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|117|QuantumSector|`norm_normalize`|N1|A0|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|118|QuantumSector|`dyad_norm_one`|N1|A2|R0|—|Textbook Madelung/Bohm/normalization calculus or a direct specialization; no new quantum law established.|
|119|ScalarField|`EFMWScalarEq_iff_expanded`|N1|A2|R3|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|120|ScalarField|`EFMWScalarEq_iff_wave`|N1|A2|R3|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|121|ScalarField|`hasDerivAt_planeWave_time`|N0|A0|R0|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|122|ScalarField|`deriv_planeWave_time`|N0|A0|R0|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|123|ScalarField|`dtt_planeWave`|N0|A0|R0|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|124|ScalarField|`hasDerivAt_planeWave_space`|N0|A0|R0|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|125|ScalarField|`deriv_planeWave_space`|N0|A0|R0|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|126|ScalarField|`dxx_planeWave`|N0|A0|R0|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|127|ScalarField|`planeWave_solves_iff`|N2|A2|R3|L1|Key derived EFMW prediction. The PDE is a standard anisotropic/Lorentz-violating kinetic form; novelty would have to come from a principled derivation/meaning of α.|
|128|ScalarField|`planeWave_phase_speed`|N2|A2|R3|L1|Key derived EFMW prediction. The PDE is a standard anisotropic/Lorentz-violating kinetic form; novelty would have to come from a principled derivation/meaning of α.|
|129|ScalarField|`normSq_polarField`|N1|A0|R0|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|130|ScalarField|`wrightTensor_eq_scalarStress_add_ricci`|N1|A2|R2|L2|Algebraically I=Tφ+Ric. In a genuine spacetime this creates a Bianchi/conservation constraint not yet formalized.|
|131|ScalarField|`modifiedEinstein_iff_unity`|N1|A2|R2|L2|Substitution equivalence, not a derivation from an action. Full covariance, dimensions, Bianchi identity and degrees of freedom remain open.|
|132|ScalarField|`modifiedEinstein_kappa_zero`|N1|A2|R2|L2|Zero-coupling recovery is by construction; good conservative-limit check, not evidence for the extension.|
|133|ScalarField|`maxwellLagrangian_neg`|N0|A2|R1|—|Scalar/tensor sector mixes routine calculus with model-specific postulates; only the dispersion relation is a substantial new consequence of the written EFMW equation.|
|134|Synthesis|`unity_signature_universally_satisfiable`|N1|A3|R0|—|Strong epistemic diagnosis of ME-001 under-specification, but logically routine: an unspecified function can fit arbitrary mappings.|
|135|Synthesis|`unity_signature_two_distinct_functionals`|N1|A3|R0|—|Strong epistemic diagnosis of ME-001 under-specification, but logically routine: an unspecified function can fit arbitrary mappings.|
|136|Synthesis|`no_warning_at_perfect_coherence`|N2|A1|R0|L4|Cross-sector result is potentially useful for assurance/monitoring; mathematically follows from the chosen normalized-distance score and tracking dynamics.|
|137|Synthesis|`tracking_implies_asymptotic_coherence`|N2|A1|R0|L4|Cross-sector result is potentially useful for assurance/monitoring; mathematically follows from the chosen normalized-distance score and tracking dynamics.|
|138|Synthesis|`selfModel_coherence_tendsto_one`|N2|A1|R0|L4|Cross-sector result is potentially useful for assurance/monitoring; mathematically follows from the chosen normalized-distance score and tracking dynamics.|
|139|Systems|`leadTime_pos_iff`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|140|Systems|`warningUtility_nonneg`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|141|Systems|`warningUtility_mono_lead`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|142|Systems|`warningUtility_antitone_far`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|143|Systems|`basinFraction_nonneg`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|144|Systems|`basinFraction_le_one`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|145|Systems|`closurePair_bijective`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|146|Systems|`logos_recursion_unique`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|147|Systems|`chronoLogos_reversible`|N1|A3|R0|—|Reversibility is largely assumed in the hypotheses/group relation; theorem checks coherence of the definition rather than deriving an arrow-of-time law.|
|148|Systems|`chronoLogos_involution_iff`|N1|A3|R0|—|Reversibility is largely assumed in the hypotheses/group relation; theorem checks coherence of the definition rather than deriving an arrow-of-time law.|
|149|Systems|`evidenceStep_iterate`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|150|Systems|`confidenceStep_lt_iff`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|151|Systems|`legalCoherence_eq_zero_iff`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|152|Systems|`constitutional_argmax_exists`|N1|A1|R0|—|Standard arithmetic/finite-set/recursion/group consequence of the chosen systems definitions.|
|153|Systems|`accept_satisfiable`|N1|A3|R0|—|Checks the hand-defined acceptance rule. Falsifiability/monotonicity are properties of the criterion, not evidence that EFMW predicts nature.|
|154|Systems|`accept_falsifiable`|N1|A3|R0|—|Checks the hand-defined acceptance rule. Falsifiability/monotonicity are properties of the criterion, not evidence that EFMW predicts nature.|
|155|Systems|`accept_requires_replication`|N1|A3|R0|—|Checks the hand-defined acceptance rule. Falsifiability/monotonicity are properties of the criterion, not evidence that EFMW predicts nature.|
|156|Systems|`accept_mono`|N1|A3|R0|—|Checks the hand-defined acceptance rule. Falsifiability/monotonicity are properties of the criterion, not evidence that EFMW predicts nature.|