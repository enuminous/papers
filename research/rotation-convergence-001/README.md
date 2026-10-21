# RC-001 — EFMW × Ramtastic Rotation Convergence Test

**Status (21 October 2026):** research protocol and executable baseline prepared; finite-difference Python baseline executed locally. Lean source below is **uncompiled** (Lean/lake unavailable in execution environment). No independent GitHub Actions verification, full C1 EFMW simulation, Einstein-constraint solution or CMB inference has been completed.

This project executes four bounded workstreams:
1. **Formal bridge:** `RotationBridge.lean` is a Lean candidate with the standard plane hinge, rigid velocity, and coordinate curl identity; the existing [Two Paths to Rotation](../../Two-Paths-to-Rotation.md) gives fuller written derivations. This package still needs a real Lean+Mathlib build and tests of metric compatibility and arbitrary-axis extension.
2. **Dynamics:** `experiment.py` reproduces a *standard wave-equation* flux-curl control, including time-zero and spatial symmetry controls. It is not a reproduction of the C1 two-scalar Landau-frame calculation. That reproduction remains open and requires importing frozen C1 code/parameters rather than inventing them.
3. **Zoo audit:** `ZOO-AUDIT.md` classifies assumptions, mathematical conclusions and physical gaps.
4. **Cosmology:** `COSMOLOGY-PROTOCOL.md` specifies an observationally falsifiable sequence and stop conditions. No global cosmic rotation is asserted.

## What is known

The [joint discussion draft](../../Two-Paths-to-Rotation.md) proves in prose the correspondence between the *standard* planar Clifford hinge
`J(x,y)=(-y,x)`, a rotation flow with angular rate ω, and the rigid velocity `v=(-ω y,ω x,0)`. Its curl is `(0,0,2ω)`. This is **standard geometric correspondence, not new physics**.

The [R-001 cosmology audit](../../EFMW-Zoo-R001-Primordial-Recursion-Boundary.md) reports a **different**, local two-scalar C1 energy-flow vorticity calculation (section 9), not a globally rotating cosmology. That model, its Landau-frame extraction, and its frozen parameters must be reproduced before making a cross-model novelty claim.

## Run the independent baseline

```bash
python3 -m pip install numpy
python3 research/rotation-convergence-001/experiment.py
```

The scalar baseline is `φ=(x²+t²)y/2` solving the ordinary wave equation `φ_tt=φ_xx+φ_yy` with `c=1`. Its diagnostic current `j=φ_t∇φ` obeys `curl₂(j)=-txy`. Because it is a **flux proxy**, not the Landau-frame physical velocity, nonzero current curl cannot establish rotation of a physical cosmological fluid. The example does show why a comparison against ordinary coupled or uncoupled scalar dynamics is essential.

**Local run (numpy 2.3.5, 2026-10-21):** grid sizes 21, 41, 81, 161 had interior maximum absolute derivative errors of respectively 4.44e-16, 1.39e-15, 3.00e-15 and 1.03e-14. At t=0, calculated curl exactly zero. This near-machine-precision agreement is expected because the selected polynomial is exactly differentiated by centered differences; it is NOT a meaningful convergence-rate or physical-validation result.

## Collaborator ethics

Chris Forrester's coauthorship or approval is not presumed. The bridge manuscript lists him as **proposed** joint author pending consent. Any incorporated Ramtastic source code must maintain its original attribution and license. Review should explicitly solicit counterexamples rather than endorsements.

## Decision gates

- Gate A: successful independent Lean build **plus** no unreported `sorry` or axioms.
- Gate B: reproduce the cited frozen C1 result using the original action and physical velocity definition.
- Gate C: compare C1 with a matched conventional two-scalar action, initial-data budget, observables and numerical tolerances.
- Gate D: only after a genuinely different physical prediction survives, derive constrained cosmological observables and compare with standard data.

If a gate fails, publish the negative result and limit downstream claims.
