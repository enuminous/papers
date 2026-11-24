# A five-centimetre p9 coil shift moves the modeled strike point across a divertor corner in STEP EB-CC

*Matthew Chenoweth Wright · Monolithic LLC · Working paper · 24 November 2026*

## Abstract

Moving the upper and lower p9 poloidal-field coil packs 5 cm each toward the midplane in a reconstruction of the STEP SPP-001 EB-CC design equilibrium changed the projected lower-target heat flux from **10.45 to 56.04 MW/m²**. The two values come from the same 257 × 513 grid and the same upstream launch rule. The field line struck adjacent faces of the supplied wall polygon in the two cases. That change of face explains why a modest shift in strike location produces a 5.36-fold change in the projection. Separate tracing methods reproduce the effect on the saved magnetic fields. The +5 cm equilibrium passed acceptance on only one grid, and the +2.5 cm case remained unresolved on both. The displacement at which the transition occurs, its reproduction in Fiesta, and its implications for a physical divertor remain open.

## Equilibrium and heat calculation

UKAEA’s OpenSTEP release provides a Fiesta free-boundary magnetic equilibrium for the EB-CC design point and separate JETTO flat-top plasma outputs. The present calculation uses the former to reconstruct the magnetic configuration and the latter to prescribe source power. SPP-001 is a simulated power-plant design. The question addressed here is whether a specific coil displacement changes where one magnetic field line meets its modeled lower wall. [UKAEA data release][data] · [Pinned source files][upstream] · [Flat-top operating points][tholerus]

Only the two p9 packs move. A positive displacement lowers the upper pack and raises the lower pack by equal distances. The calculation fixes all coil currents, the other coil positions, the wall outline, the pressure function *p(s)* of normalized poloidal flux, the reconstructed baseline plasma current (22.77441 MA), and the boundary value of *F* = *R Bφ* (11.52 T m). The implementation uses FreeGS 0.8.2’s fourth-order Grad–Shafranov operator and boundary routines, with a cut-cell plasma-current source and numerical continuation. The protocol required a normalized full-domain defect ≤ 10⁻⁵, relative pressure-profile and total-current errors ≤ 10⁻⁹, positive *F*², and up/down flux symmetry within 10⁻⁸ Wb/rad. The log records additional restart attempts. [Scan protocol][protocol] · [Amendments][amendments]

For each accepted field, the representative trace starts 1 mm radially outside **that equilibrium’s own outboard-midplane separatrix**, the boundary of the confined plasma. The heat calculation follows the field to its first lower-wall intersection. It assumes an exponential upstream heat-flux width of 6 mm, a scrape-off-layer radiation fraction of 50%, and a one-target power share of 25%. The observable is the projected normal heat flux at that strike point. A peak over the whole target is a different quantity. [Heat-mapping model][heatmodel]

## Results

**Table 1.** Representative heat flux in MW/m². “Unresolved” denotes a grid and geometry for which no attempted equilibrium met the acceptance criteria. Eight of fourteen cases were accepted. [Machine-readable scan][scan]

| p9 movement (cm) | 129 × 257 | 257 × 513 |
|---:|---:|---:|
| −5 | 10.67 | Unresolved |
| −2.5 | Unresolved | Unresolved |
| −1 | 10.38 | 10.47 |
| 0 | 10.56 | 10.45 |
| +1 | 10.50 | 10.47 |
| +2.5 | Unresolved | Unresolved |
| +5 | Unresolved | 56.04 |

On the fine grid, the +5 cm case exceeds baseline by 45.59 MW/m². Both 1 cm shifts still land on baseline face 12. The missing coarse +5 cm result prevents applying the protocol’s coarse-to-fine test to the large increase. The missing fine −5 cm result also prevents comparing the two directions at 5 cm on the same grid. The original scan sought a reduction in heat load. No candidate met its design-selection rule, so the optional 513 × 1025 refinement did not run. [Scan decisions and failed attempts][scanreport]

**Table 2.** Lower-target strike coordinates from the fine-grid adaptive-tracer replay. Face numbers are zero-based indices in the released main-wall polygon. Area expansion is the flux-tube area ratio used by the heat map. [Full-precision trace records][refined]

| p9 movement | Wall face | R (m) | Z (m) | Magnitude of normal field (T) | Area expansion |
|---|---:|---:|---:|---:|---:|
| 0 cm | 12 | 5.801614 | −8.534336 | 0.216921 | 6.82565 |
| +5 cm | 13 | 5.855000 | −8.517715 | 1.146287 | 1.29026 |

![Baseline and displaced field lines intersect adjacent faces of the lower-wall polygon near its corner.][figure]

*Figure 1. Representative strikes on the released wall outline. At +5 cm, the field line meets a face whose normal is more closely aligned with the magnetic field. The same imposed upstream heat is spread over a smaller target area.* [Archived figure and tracer analysis][tracers]

A fixed-step Runge–Kutta tracer and an adaptive DOP853 tracer used different integration coordinates and wall-hit calculations. Across 40 comparisons on shared equilibrium fields, their largest differences were 3.587 µm in strike position, 0.199 mm in connection length, and 0.00015% in projected heat. The broader OPENSTEP-004 suite nevertheless recorded **792 PASS and 220 FAIL**, including flux-drift and tolerance-refinement failures. A later check at the representative launch offset recorded **32 PASS and 1 FAIL**. These counts describe numerical assertions. Neither replay supplied a separately computed magnetic equilibrium. [Original tests][tracers] · [Refinement verdicts][refinement]

Wall shape also matters. A subsequent calculation searched upstream launch offsets from 0.25 to 20 mm. On the sharp polygon, the maximum over that window was 13.69 MW/m² at baseline and 63.52 MW/m² at +5 cm. Substituting an assumed 10 mm corner radius gave 11.82 and 58.83 MW/m², respectively. The large modeled contrast survived this particular rounding test. Its relevance to a manufactured target depends on the actual surface geometry and on exhaust physics, including detachment, which the projection omits. [Geometry assumptions and footprint data][rounding]

## External validation request

On 23 November 2026 (Pacific time), I emailed **Dr Agnieszka Hudoba**, lead author of the STEP poloidal-field optimisation study, and copied **Dr Emmi Tholerus**, lead author of the flat-top scenario paper. I supplied the matched fine-grid baseline and +5 cm values, the unresolved −5 cm fine-grid case, and the wall-corner explanation. On 24 November I followed up with the strike coordinates, the shared FreeGS dependency, and asked a narrower question. **Does Fiesta also move the 1 mm lower-target strike to the adjacent wall face when the p9 packs move 5 cm toward the midplane?** The outreach disclosed the prediction before any response. At the 24 November manuscript cutoff, the correspondence contained **no reply or independently computed Fiesta result**. [PF optimisation study][hudoba] · [EB-CC scenario study][tholerus]

A decisive comparison for the **magnetic** claim would proceed as follows.

1. Compute a baseline and a +5 cm equilibrium in Fiesta. Match coil positions and currents, pressure and total-current constraints, boundary-field and flux conventions, wall coordinates, and spatial resolution. Record differences in the inputs or mesh and agree on coordinate and field tolerances before inspecting the returned fields.
2. Apply the same 1 mm launch rule to each field. Compare the first lower-wall hit in physical R and Z, its position relative to the common corner, and the local normal field. Comparing physical locations allows for different face numbering. If both codes reproduce the baseline but only one crosses the corner after the shift, the predicted transition fails that comparison. If baseline agreement or strike accuracy cannot distinguish the two faces, the result remains unresolved.
3. If the magnetic comparison succeeds, apply the same heat map to the returned fields to test the conditional flux ratio. Assessing a physical design margin requires a specified target surface and an independently constrained exhaust and heat-deposition model. A stock FreeGS rerun can test the custom continuation and source treatment, but it shares part of the equilibrium implementation.

## Evidence and reproducibility

The result available for independent review is a pair of strike locations and normal fields with a specified perturbation, launch rule and wall. A Fiesta reproduction would support that magnetic prediction in this design scenario. The EFMW audit workflow made the prediction and its failure conditions explicit. Establishing that the workflow improves solving performance would require a comparative test on held-out problems.

The OpenSTEP dataset is credited to Theodore Brown, Francis Casson, Agnieszka Hudoba, Stephen Marsden, Emmi Tholerus, Thomas Wilson, and the STEP Team. UKAEA’s source revision is `6f66ae09c60b361d600b178416ef3f22b8d0aa6a` (CC BY 4.0). The analysis, commands, environments, fields, rejected attempts, and tables cited here are pinned to `enuminous/Tokamak` revision `149f5eca9e82464fdc0c6bf274f757bd12221772`. To check the 5.36 ratio directly, select rows `grid=257`, `shift_m=0` and `shift_m=0.05` in the scan CSV and divide their `representative_heat_MW_m2` values, 56.04329199676229 / 10.45223893044388. To replay the solves, use the recorded environment and warm-start order. [Data attribution][data] · [Scan CSV][scan] · [Environment][env] · [Replay commands][commands]

[data]: https://doi.org/10.14468/07jt-s540
[upstream]: https://github.com/ukaea/OpenSTEP/tree/6f66ae09c60b361d600b178416ef3f22b8d0aa6a
[tholerus]: https://doi.org/10.1088/1741-4326/ad6ea2
[hudoba]: https://doi.org/10.1088/1741-4326/ad53e2
[protocol]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-003/PROTOCOL.md
[amendments]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-003/AMENDMENTS.md
[heatmodel]: https://github.com/enuminous/Tokamak/tree/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-002
[scan]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-003/results/candidate-grid.csv
[scanreport]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-003/README.md
[refined]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-004/results/representative-refinement.json
[figure]: https://raw.githubusercontent.com/enuminous/Tokamak/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-004/results/wall-corner.png
[tracers]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-004/README.md
[refinement]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-004/results/refinement-assessment.json
[rounding]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-005/README.md
[env]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-003/environment.json
[commands]: https://github.com/enuminous/Tokamak/blob/149f5eca9e82464fdc0c6bf274f757bd12221772/benchmarks/openstep-003/COMMANDS.md
