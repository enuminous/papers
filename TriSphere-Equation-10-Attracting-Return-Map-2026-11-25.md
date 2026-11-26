# TriSphere Equation 10: an attracting return map
November 25, 2026 — Monolithic LLC. Candidate mathematical realization; not physical validation.

Source: https://tri-sphere-text.abethjones.workers.dev/ (live blueprint, Equation 10; external drive explicitly distinguished from mirror). The live source is mutable. This extension chooses its own potential and kick, not an assertion that the source specifies them.

## Construction
rho''=-V'(rho)-gamma*rho' between impacts. V(rho)=omega^2 min(rho,11)^2/2 on [0,12]. omega=.2, gamma=.08, external energy injection J=5 at each central return. Elastic outer reflection reverses velocity; central reflection launches with speed sqrt(v_in^2+2J). Time is dimensionless in the candidate model; no identification with GPS or physical time is made. The flat band requires entry speed > gamma*(12-11) for outbound crossing, and >2 gamma*(12-11) for both outbound and inbound crossings with elastic reflection. Grazing and stalled trajectories are outside this regular branch.

Energy E=v^2/2+V obeys dE/dt=-gamma*v^2 between kicks. The return map P(E)=E-L(E)+J has fixed point when J=L(E). On the smooth transverse wall-reaching branch, the variational determinant is exp(-gamma*T), since the phase-space divergence is -gamma. The section velocity factors cancel after conversion to energy; elastic reflection and constant energy addition have unit energy derivative. Thus P'(E)=exp(-gamma*T) on that branch. This is local stability, not a global guarantee. A fixed point at a regular crossing also gives a periodic hybrid trajectory.

## Independent numerical recheck
Piecewise analytic damped harmonic solutions and exact flat-band transit formulas, with bisection for crossing times and fixed point, were evaluated in JavaScript. A standard-library Python translation is supplied for reproduction; Python execution was not independently verified in this publication turn.
- Fixed launch energy 7.268050808342798
- Return energy 2.268050808342798
- Period 9.638611257566753
- Wall arrival speed 1.973957373322011
- Energy loss 5 by fixed-point balance
- Analytic multiplier 0.4625091674996027
- Central finite difference (step 1e-5) 0.46250916749812626
- Initial energies 5, 10, 20 after 15 cycles: 7.2680336254818325, 7.268082789797785, 7.268318994472176.

These values refine the earlier rounded numerical report; the finite-difference check now agrees closely. No claim is made of global convergence, autonomous energy creation, guaranteed periodicity for arbitrary drive, fluid dynamics, or physical cosmology. The imposed reflection is not the same as a smooth zero-velocity turn at the wall. The fixed point is numerical, and the stability expression is analytical conditional on regular crossings.

## Reproduce
In the TriSphere repository run python simulation/return_map.py. The script explicitly rejects stalled flat-band cases rather than silently asserting a return.

## Verdict
Bounded candidate oscillator: numerical PASS for an attracting wall-reaching periodic orbit with stated drive and reflection. Original blueprint as a complete fluid or physical model: UNRESOLVED. The historical audit is not overwritten.

Pinned computational package: https://github.com/enuminous/trisphere/tree/58c756870b601e7b83b6dcccec071daa2ca6d366
