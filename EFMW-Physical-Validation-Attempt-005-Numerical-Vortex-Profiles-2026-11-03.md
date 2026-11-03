# EFMW Physical Validation — Attempt 005: Numerical Vortex Profiles

Date: 2026-11-03
Status: NUMERICAL MODEL RESULT; EFMW-SPECIFIC PHYSICAL PREDICTION UNRESOLVED

## Model
This is the phenomenological density-gradient extension from Attempt 004, **not a canonical EFMW-derived interaction**. Dimensionless vortex amplitude f(s), s=r/xi, q=1, solves:

(1+beta f²)(f''+f'/s) + beta f(f')² - f/s² + f(1-f²)=0.

Boundary approximation: f(s_min)=s_min f'(s_min) with s_min=0.015, and f(25)=1-1/(2*25²). The outer condition uses the GP leading asymptotic and is an approximation for nonzero beta; results therefore require outer-boundary sensitivity tests before precision claims.

## Method
SciPy solve_bvp on 900 initial nodes spanning s=0.015 to 25, tolerance 1e-7, maximum 20000 nodes. Computed normalized density f² at s=0.5,1,2,3,5 and half-density radius by scalar root finding. All runs returned status 0 with maximum reported RMS residual below 1e-7. This is convergence of the numerical solver, not an independent discretization-error bound.

## Results
| beta | s_half | n(0.5xi)/n0 | n(xi)/n0 | n(2xi)/n0 | n(3xi)/n0 | n(5xi)/n0 |
|---:|---:|---:|---:|---:|---:|---:|
|0|1.554892|0.079988|0.270454|0.647956|0.841772|0.953793|
|0.1|1.550732|0.081614|0.273578|0.647498|0.839594|0.953051|
|0.25|1.544707|0.084053|0.278104|0.646885|0.836558|0.951930|
|0.5|1.535141|0.088120|0.285248|0.646032|0.832019|0.950057|
|1.0|1.517362|0.096252|0.298244|0.644824|0.824443|0.946376|

At beta=1 versus beta=0, the half-density radius decreases by approximately 2.41%; normalized density at s=1 increases by approximately 10.28% relative. These are model-to-model differences only.

## Limitations and required follow-up
- No physical mechanism or independent value for beta derived from canonical EFMW.
- Outer boundary asymptotic is GP-derived; repeat with beta-dependent asymptotics and several larger outer radii.
- Repeat with varied mesh and tolerances, and independently check the differential residual.
- Compare with established GP extensions, including beyond-mean-field, trap, temperature and imaging convolution.
- No experimental data used. No external evidence or independent replication claimed.
- A density-gradient term can be interpreted as an effective modification of quantum-pressure cost; it is not intrinsically unique to EFMW.

## References
- https://github.com/enuminous/papers/blob/main/EFMW-Physical-Validation-Attempt-004-Density-Gradient-Coupling-2026-11-03.md
- https://ctp.itp.ac.cn/EN/10.1088/1572-9494/ac86bd
- https://github.com/enuminous/Phase-Vorticity-Lab/blob/main/docs/MODEL.md

## Gate verdict
Mathematical construction: PASS.
Numerical solver convergence: PASS within stated solver tolerance.
Robust numerical verification: UNRESOLVED.
EFMW-specific coefficient and source derivation: UNRESOLVED.
Established-theory alternative-model comparison: UNRESOLVED.
External physical evidence: NOT TESTED.
