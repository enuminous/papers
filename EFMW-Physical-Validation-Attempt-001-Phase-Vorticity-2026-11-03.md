# EFMW Physical Validation — Attempt 001: Phase/Vorticity Observable Bridge

**Date:** 2026-11-03  
**Status:** UNRESOLVED for EFMW-specific physics; PASS for dimensional consistency of a selected kinematic model  
**Sources inspected:** `enuminous/Phase-Vorticity-Lab` README, `docs/MODEL.md`, `docs/FORMAL_BRIDGE.md`; `enuminous/EFMW` README. Source inspection was not a clean Lean rebuild or external experiment.

## Question
Can a defined EFMW variable generate a dimensionally specified, noncircular, independently discriminating observable?

## Source-grounded candidate
The Phase-Vorticity Lab defines `psi=rho exp(i theta)`, `J=a rho^2 grad(theta)`, and `a=hbar/m`. Its model explicitly states that the smooth vortex blob is **chosen rather than derived** from the phase identity:
`u(x)=a n (-y,x)/(r^2+epsilon^2)`,
`omega(x)=2 a n epsilon^2/(r^2+epsilon^2)^2`.
For a centered circle of radius R,
`Gamma(R)=2 pi a n R^2/(R^2+epsilon^2)`.

## Dimensional audit
With `[a]=L^2/T`, `[R]=[epsilon]=L`, `[n]=1`: `[u]=L/T`, `[omega]=1/T`, `[Gamma]=L^2/T`. **PASS**.

## Algebraic derivation
At radius R, the tangential speed is `u_theta=a n R/(R^2+epsilon^2)`; hence `Gamma=2 pi R u_theta=2 pi a n R^2/(R^2+epsilon^2)`. Its large-R limit is `2 pi a n`. **PASS conditional on the stipulated vortex profile**.

## Noncircularity and physical novelty
The lab's `epsilon` is an input and its blob profile is a stipulated regularization, not an EFMW dynamical consequence. The phase-current identity is conventional quantum mechanics. The laboratory itself says it does not solve Schrödinger/Gross–Pitaevskii/Euler dynamics and is not a physical EFMW discovery. Therefore **FAIL as an independently derived EFMW-specific law**, not a disproof of EFMW.

## Comparator
A physically appropriate next comparator is a vortex solution of a specified Gross–Pitaevskii model with independently known mass, coupling, density, boundary conditions and healing length, including instrument response. One must not compare a free-profile fit only against an unregularized singular vortex. No comparator simulation or external measurement was run in this attempt. **UNRESOLVED**.

## Required bridge
Find a pinned EFMW evolution equation or action that fixes `epsilon` or changes the predicted profile with no access to held-out circulation measurements. State parameter dimensions, gauge behavior, conservation laws and limiting cases. Derive a testable numerical `Gamma(R)` or `omega(r)` and freeze it before measurement. If EFMW yields only the standard model, report equivalence rather than novelty.

## Gate record
| Gate | Status | Reason |
|---|---|---|
| Source-defined kinematic observable | PASS | Source model and circulation integral explicit |
| Dimensional consistency | PASS | All terms consistent |
| EFMW-specific noncircular derivation | FAIL | Vortex blob and core scale not derived from EFMW |
| Independent discriminating prediction | UNRESOLVED | No source-derived EFMW correction or frozen numerical prediction |
| Strong physical comparator | UNRESOLVED | Not executed |
| External evidence | UNRESOLVED | Not tested |
| Independent replication | UNRESOLVED | Not tested |

## References
- https://github.com/enuminous/Phase-Vorticity-Lab/blob/main/docs/MODEL.md
- https://github.com/enuminous/Phase-Vorticity-Lab/blob/main/docs/FORMAL_BRIDGE.md
- https://github.com/enuminous/EFMW/blob/main/README.md

This is a bounded negative/partial finding, not a claim of empirical validation.
