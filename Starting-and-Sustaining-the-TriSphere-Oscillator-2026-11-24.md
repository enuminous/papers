# Starting and sustaining the Tri-Sphere oscillator

*Matthew Chenoweth Wright · Monolithic LLC · Technical correction · 24 November 2026*

## Abstract

Can the same pump start a motionless oscillator and sustain its swing? In the Tri-Sphere laboratory, the pump fires when the oscillator returns to the center. An oscillator resting there never triggers its first kick. Once launched, however, a damped harmonic oscillator can approach a repeating orbit because each kick replaces the energy lost on the previous trip. This distinction corrects Equation 10’s claim of a repeating orbit from every starting state. [Corrected blueprint (Word)][word] · [Exact text changes][patch]

## The work done on a round trip

A. Beth Jones’s TGS:ATE / ORION blueprint describes an outward excursion from a center to a shell and a return through a Filter. Its tenth equation includes a restoring potential V, damping γ, and a drive D. Hold the valve setting fixed so that D depends only on radius. The work supplied on the outward path then cancels the work on the inward path. With positive damping, a moving oscillator still loses energy on both legs.

More precisely, let W′(r) = D(r) and define E = v²/2 + V(r) − W(r). Along a smooth solution, dE/dt = −γv². A periodic orbit would recover its initial energy after one period. For γ > 0, the integral of γv² can vanish only when the velocity stays zero. The laboratory’s Lean proof establishes this result under the stated smoothness and fixed-drive assumptions. [Lean source][lean]

## A pump that acts on return

In the laboratory’s alternative model, the oscillator follows r″ + γr′ + r = 0 between center visits. An incoming center crossing reverses the velocity and adds energy J. Let Eₙ denote the energy just after a launch or kick. If each excursion retains a fraction q with 0 < q < 1, then

**Eₙ₊₁ = qEₙ + J**, with steady return energy **E★ = J/(1 − q)**.

Each trip multiplies the deviation from E★ by q. The trajectory repeats exactly at E★. A positive launch energy approaches that orbit while the excursions stay inside the shell. At rest there is no crossing, so the recurrence has no first event. Substituting zero into the recurrence would insert a kick that the trigger never delivered.

| Test in the dimensionless model | Outcome |
| --- | --- |
| Launch with E₀ = 2, damping γ = 0.35, and kick J = 1.2 | Return energy approaches 1.78393. The steady excursion peaks at radius 1.47411. |
| Keep the same launch and damping, then remove the kick | Return energy falls to about 4 × 10⁻¹⁰ after 20 returns. |
| Start at rest with the return pump enabled | The oscillator stays at the center. It receives zero kicks. |

The full 80-case grid includes 20 zero-energy starts. All 20 stayed at rest. Nine numerical first-return comparisons checked the analytic flight time and the energy arriving back at the center. The Lean proofs cover the fixed point and convergence of the specified map. [Numerical records][sim] · [Parameter sweep][sweep] · [Verification run][ci]

## What the five-position GPS describes

In Jones’s revised blueprint, the thirteen layers form an atlas. The five positions describe one oscillator from the observer’s seat at Layer 6. The center and shell are the endpoints. The inner membrane represents inhalation, the Filter is the observer’s seat, and the outer membrane represents exhalation. The fixed-point result explains how a modeled breath can repeat. Deriving the thirteen-layer geometry from Filter imbalance and establishing periodicity for an entire density field remain open questions. [Author’s living blueprint][beth] · [Monolithic corrected text][text]

The accompanying Word document is the Monolithic editorial copy of Jones’s blueprint. The five edited paragraphs address the return trigger, the initial push, and the claims that depended on automatic periodicity. The original audit and the laboratory release identify the source versions and retain the earlier findings. [Full audit][audit] · [Open the laboratory][lab] · [Download release 1.0.1][zip]

[word]: TriSphere-Blueprint-Equation-10-Corrected-2026-11-24.docx
[patch]: https://github.com/enuminous/trisphere/blob/6735e3cab5c963a590e91acca31f9fd64e2cc1cf/source/equation-10.patch
[lean]: https://github.com/enuminous/trisphere/blob/6735e3cab5c963a590e91acca31f9fd64e2cc1cf/TriSphere.lean
[sim]: https://github.com/enuminous/trisphere/blob/6735e3cab5c963a590e91acca31f9fd64e2cc1cf/simulation/README.md
[sweep]: https://github.com/enuminous/trisphere/blob/6735e3cab5c963a590e91acca31f9fd64e2cc1cf/evidence/sweep.json
[ci]: https://github.com/enuminous/trisphere/actions/runs/45510947721
[beth]: https://tri-sphere-text.abethjones.workers.dev/
[text]: https://github.com/enuminous/trisphere/blob/6735e3cab5c963a590e91acca31f9fd64e2cc1cf/source/blueprint-corrected.txt
[audit]: https://github.com/enuminous/trisphere/blob/6735e3cab5c963a590e91acca31f9fd64e2cc1cf/AUDIT.md
[lab]: https://enuminous.github.io/trisphere/
[zip]: https://github.com/enuminous/trisphere/releases/download/lab-v1.0.1/TriSphere_Laboratory.zip
