# UNITY-001 source derivation and stationary gravity gate

16 November 2026 · Source-pinned analytic screen

**Result:** The minimally coupled free informational scalar slot in C1 yields a conserved scalar stress and an energy density in SI units once the initial energy, width and mass scale are supplied. Under the isolated static assumptions needed for the Phase 5 gravity template, that branch has only the zero field. The corresponding conventional Einstein–Klein–Gordon model has exactly the same action and stress. The physical prediction gate remains closed.

## Source and scope

- [Frozen C1 candidate](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md), source blob `916e04935f50cbbf07ddcd81e7c71a02954b1c96`. Retain the metric and the canonical scalar in the I slot, with nonnegative squared mass. Set pair/triple and nonminimal curvature couplings to zero, take zero cosmological constant for the isolated example, and set other fields to zero. These are explicit branch choices within C1.
- [Geometry source split](https://github.com/enuminous/Geometry/blob/285b95551ca11c487eb6c0c13f8dde86b702df71/Geometry.lean) models total-source absorption algebraically. The I slot label alone supplies no equality between C1 stress and historical ME-007 informational stress.
- [WITD-002 derivation](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/DERIVATION.md), source blob `d427b2f50bd8e577f6c206e076aa4121a612c6d9`, supplies a conditional energy ledger and a counterexample to constant rescaling of its displayed I00 into storage across all states. Its covariant reservoir tensor and source calibration are open.
- [Unity Phase 5](https://github.com/enuminous/papers/blob/cc04b04b953a14aefb2bf2f58041e99b4820a1ab/research/unity-001/phase-5/PHASE5_REPORT.md) uses a stationary hypothetical top-hat. The profile below follows from declared initial data in a particular branch. The original Phase 5 profile remains its own toy assumption.

## Conserved stress and SI profile

Use x⁰ = ct, signature (−,+,+,+), and a scalar φ with SI units (J/m)½. Let μ = m c/ℏ be the inverse Compton scale in m⁻¹. With the volume convention d⁴x/c, the scalar Lagrangian density is −[(∇φ)² + μ²φ²]/2 in J/m³. Metric variation gives

    Tμν = ∂μφ ∂νφ − gμν[(∇φ)² + μ²φ²]/2
    ∇μ Tμν = (□g φ − μ²φ)∂νφ = 0 on shell.

On a flat leading-order background choose spherical time-symmetric initial data φ(0,r) = A exp[−r²/(2L²)] and ∂tφ(0,r) = 0. The future field is determined by the homogeneous Klein–Gordon initial-value equation. Its initial energy-equivalent density is

    ρE(0,r) = A² exp(−r²/L²) [r²/L⁴ + μ²] / (2c²).
    E = π^(3/2) A² L³ [μ² + 3/(2L²)] / 2.

Specify E, L, μ before inspecting any gravitational data and solve the second equation for A. The enclosed energy-equivalent mass is E/c² times

    [∫₀^(r/L) u²(u² + (μL)²)e^(−u²) du]
    / [√π ((μL)² + 3/2)/4].

For a numerical normalization control only, E = 1 J, L = 1 m, μ = 1 m⁻¹ gives E/c² ≈ 1.113×10⁻¹⁷ kg. The values are independently declared inputs to the calculation. The action supplies no calibrated preparation process or actual values for E, L, and μ. This is the local energy density divided by c². A time-dependent gravitational measurement would require full stress, metric response and gauge-invariant readout, including the role of stresses and any source apparatus.

## Stationary no-go in the selected branch

For a time-independent, regular, localized field on a static spacetime with lapse α>0 and spatial metric h, the free equation is

    Dᵢ(α Dⁱ φ) − α μ² φ = 0.

Multiply by φ and integrate over the spatial slice. With no inner boundary and vanishing surface term at the outer boundary, integration by parts gives

    ∫ α (|Dφ|² + μ²φ²) √h d³x = 0.

Hence φ vanishes for μ²>0. For μ=0 it is constant on each connected component and vanishes under the zero-at-infinity condition. The prescribed Gaussian also fails the static equation directly: the operator (∇²−μ²) at its center equals −(3/L²+μ²)A. The no-go applies with the stated isolated boundary conditions. Interactions, a driven or supported source, nonminimal curvature coupling, or time-dependent states require separate analysis.

## Matched conventional model and disposition

Take conventional Einstein–Klein–Gordon theory with the same normalization, mass, boundary and initial data. Its stress and field equations coincide pointwise with the selected C1 branch. Any gravitational response computed solely from those equations and data is shared by the two descriptions. The equivalence holds for the entire selected branch and does not rely on the Gaussian example. The earlier independent-mass calibration screen remains a conditional design tool for alternatives that supply different source or instrument responses.

The same pinned sources give no operational preparation of a nonzero, stationary, EFMW-specific profile for Phase 5. C1's separate root equation leaves its external source J and the stress normalization undetermined. The WITD result does not furnish the missing covariant source identification. A distinct physical test would require a source interaction or boundary mechanism fixed independently of the gravitational outcome, a derivation of its conserved total stress in SI units, and a demonstrated response difference from a conventional model with matching preparation and controls.

**Disposition:** source derivation demonstrated for the conditional free scalar branch. Stationary isolated nonzero profile rejected in that branch. Historical tensor identification and an EFMW-specific physical signature remain unresolved.

## Reproduce

Run `python3 screen.py` to evaluate the enclosed mass and check the analytic integrals by independent radial quadrature. Default inputs reproduce `results.json`. The calculation was also checked with a massless case and a heavier case at different widths. No external dependencies or empirical observations are used.
