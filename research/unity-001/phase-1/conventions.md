# UNITY-001 Phase 1 — Mathematical conventions inventory

**Evidence:** pinned files in [sources.lock.json](sources.lock.json); no new convention translation or equivalence was performed.

| Source | Spacetime convention | Fields / domains | Norms, units, and unresolved requirements |
|---|---|---|---|
| Geometry | Component arrays over `Fin 4 → Fin 4 → ℝ`; **no Lorentzian metric formalized** in the proof library | Ordinary source `T`, information `I`, scalar coupling `κ`; `ReducedBianchi.identity` assumed | `totalSource=T+κI` is component algebra; source-only observations may be degenerate; no physical `κI` observation |
| Information-Tensor | `η=diag(-1,+1,+1,+1)` fixed; `c=1`, `∂z=0`; historical catalogue source ME-004 uses opposite signature | `q,p,m,Phi,h` on periodic 2-D computational lattice; `I_ab=T_ab[q]+R_ab` | Dimensionless normalized simulation; authored closures `R_ab=βT_ab[m]`, not Ricci curvature; no fully conserved covariant action or calibration |
| EFMW-Lagrangian | `(-,+,+,+)`; `c=ℏ=1`; `□=g^{μν}∇_μ∇_ν`; compact support | Metric, two Abelian gauge potentials, eight neutral real scalars | Classical effective action C1; coefficient reciprocity assumptions; scalar signs, neutral gauge currents, metric stress incomplete in literal source |
| Standard-Model-Reduction | `(+,-,-,-)`; `ℏ=c=1`; `Q=T₃+Y` | 3-generation chiral Standard Model, SU(3)×SU(2)×U(1), Higgs, gauge connections | Classical SM rewrite with 19 parameters including strong CP in stated minimal model; no parameter-free 39-strata proof, gauge-fixed quantum completion not supplied |

## Nontrivial translation obligations

1. **Signature mismatch:** account for index raising, `□` sign, kinetic term signs and curvature conventions before comparing candidate source equations to the SM reference.
2. **Meaning of R:** Geometry refers to candidate Ricci/scalar curvature; Information-Tensor names `R_ab` a chosen memory residual, explicitly *not* spacetime Ricci curvature.
3. **Meaning of H and P:** C1's `H` gauge-field notation corresponds to historical sector `S`; scalar sector `P` does not automatically mean the physical root source `P`.
4. **Stress and conservation:** the information tensor and scalar stress in different repositories are **not** established equal; conditional `ReducedBianchi` is not a proof of the geometric Bianchi identity.
5. **Derivative/current signs:** preserve `□φ+C=0` source expressions and `□φ-∂U/∂φ=0` C1 variations as *distinct* formulas; gauge-current replacements require independent derivation.
6. **Units:** the Reference SM uses natural units, Geometry uses abstract real component arrays, Information-Tensor uses normalized units, and C1 uses natural units; no cross-sector physically calibrated dimension map exists.

**Gate:** all translations stay UNRESOLVED pending explicit source-faithful maps and tests.
