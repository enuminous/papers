# Tranche IV theorem register

Tranche IV formalizes finite-precision testing and conditional observational bounds.

| # | Lean declaration | Role |
|---:|---|---|
| 1 | `Measurement.Compatible_of_strict` | Strict compatibility implies compatibility. |
| 2 | `eventually_strictlyCompatible` | Strict compatibility is locally stable for continuous observables. |
| 3 | `no_exact_parameter_verification` | Finite strictly compatible continuous data cannot isolate one real parameter value. |
| 4 | `measurement_discriminates` | Predictions separated by more than twice the error bar cannot both fit one reading. |
| 5 | `falsification_by_measurement` | A concrete finite measurement refutes a parameter value. |
| 6 | `phaseSpeed_zero` | Zero scalar coupling gives the baseline speed. |
| 7 | `sqrt_one_sub_sq_pos` | The phase-speed denominator is positive in the admissible regime. |
| 8 | `sqrt_one_sub_sq_le_one` | The phase-speed denominator is at most one. |
| 9 | `ME002_005.phaseSpeed_satisfies_homogeneous_relation` | The phase-speed formula satisfies the source-free ME-002/005 dispersion relation. |
| 10 | `ME002_005.phaseSpeed_unique_nonneg` | It is the unique nonnegative speed satisfying that relation. |
| 11 | `le_phaseSpeed` | The modeled scalar-wave speed is at least the baseline speed. |
| 12 | `lt_phaseSpeed` | Nonzero admissible coupling makes the modeled speed strictly larger. |
| 13 | `alpha_sq_le_of_speed_measurement` | A finite-precision null result bounds the squared scalar coupling. |
| 14 | `alpha_eq_zero_of_exact_lightspeed` | Exact baseline speed forces zero coupling within the model. |
| 15 | `phaseSpeed_gap` | Coupling bounded away from zero yields a definite prediction gap. |
| 16 | `speed_experiment_discriminates` | Sufficient precision separates the zero and nonzero-coupling hypotheses. |
| 17 | `decisive_precision_exists` | A discriminating positive precision exists. |
| 18 | `ME056.friedmann_deviation` | The ME-056 extension differs from ΛCDM by the rotation term. |
| 19 | `ME056.OmegaU_sq_le_of_hubble_measurement` | A cosmological null result bounds residual rotation. |
| 20 | `ME056.OmegaU_eq_zero_of_exact_hubble` | Exact agreement forces zero residual rotation within the model. |
| 21 | `physical_test_asymmetry` | Refutability and non-verifiability are combined in one proposition. |

These are formal consequences of explicit models and assumptions. They do not report
measurements, prove that the scalar-wave law is physically correct, or derive ME-056
from general relativity.
