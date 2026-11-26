# QG-021 — Quantum matter and Newtonian backreaction

26 November 2026 · Monolithic LLC · EFMW exploratory research. **PASS_BOUNDED**; not peer reviewed.

## Scope

Two distinguishable mobile particles of equal dimensionless mass 5 occupy disjoint width-two hard-wall intervals centered at 0 and D. The positive separation is r=D+y−x, with D=3,4,6. The usual three-dimensional Newtonian pair potential evaluated along this axis is V=−g/r, g=Gm² in dimensionless units (g=0,2,8). This is an instantaneous reduced quantum Hamiltonian on matter, not an independent quantum metric or a quantization of QG-018. There is no singularity or overlap in the allowed domain; no softening is used. The external walls break translation symmetry; total particle momentum need not be conserved. No physical units, weak-field scale calibration, retardation, tensor radiation or self-gravity are modeled.

Use finite differences for each kinetic term T with Dirichlet boundaries. Evolve the joint amplitude Psi by exp(−iHt), H=T⊗I+I⊗T+diag(V). Compare with self-consistent product-state (Hartree) dynamics i dA/dt=T A+(V |B|²)A and i dB/dt=T B+(V^T |A|²)B. The Hartree energy counts the pair potential once; this is a specified expectation-value comparator, not every classical-gravity theory. Initial wavefunctions are normalized double Gaussian lobes (centers ±0.42, width parameter 0.18) or a single central Gaussian (width parameter 0.22). Use 81 times on [0,4]. The additive control replaces V by its first Taylor expansion −g/D+g(y−x)/D²; it has force but no nonseparable interaction.

## Results

Thirteen matched configurations (26 trajectories, 2,106 recorded diagnostic rows). At n=47 per particle, double-lobe peak linear entropy 1−Tr(rho_A²):

| D | g=0 | g=2 | g=8 |
|---:|---:|---:|---:|
|3|<1e-14|0.008690277621|0.133404512438|
|4|<1e-14|0.001194517918|0.017328456301|
|6|<1e-14|0.000088765459|0.001384859452|

Single-lobe D=3,g=8 gives peak linear entropy 0.277053507501 (negativity 0.693375387860; this is not a two-qubit model). The matched Hartree state remains separable by construction; additive and zero-coupling controls have absolute linear entropy within 1.56e-12 of zero on the sampled grid (negative values from roundoff possible). The n=47,D=3,g=8 double-lobe case has initial accelerations +0.202050008452 and −0.202050008452; mean distance decreases from 3 to 2.997977701891 at t=.1, then 2.525348426809 at t=4 versus Hartree 2.501077292126. Hard walls affect later evolution; the initial attraction is the cleaner diagnostic. At D=6,g=2, the maximum mean-separation difference is only 2.80304e-6 despite nonzero entanglement.

## Analytical check

For an initial product, remove the two marginal means and add the global mean to obtain V_c(x,y)=V(x,y)−E_B[V|x]−E_A[V|y]+E[V]. Then linear entropy S_L(t)=2 t² E[V_c²]+o(t²) in hbar=1 units. The measured short-time coefficient at t=.002 matches the analytical value within 2.53e-5 relative error across interacting cases. For the double-lobe D=3,g=8 case, predicted 0.0342471081465, observed 0.0342475020287. At large D the leading mixed Taylor term is 2gxy/D³, giving a short-time coefficient proportional to D^-6 for fixed initial variances. The additive force-only model has identically zero V_c mathematically. This explains why attraction alone is insufficient to establish entanglement.

## Verification

All 12 programmed checks pass: quantum norm <1e-9, energy <1e-8, Hartree norm and energy <1e-7, product-state linear entropy <1e-7, null controls <1e-9, interacting disjoint entropy >1e-5, early attraction, opposed initial accelerations, short-time coefficient within 1%, improved spatial refinement, fine-grid initial-force correspondence within 2%. Observed maxima: quantum norm 2.095e-11, energy 1.851e-12, Hartree norm 6.685e-12, energy 5.327e-9; Hartree absolute entropy 1.337e-11. The discrete initial acceleration uses −[H,[H,X]], with the free wall contribution subtracted for comparison to E[g/r²]/m. Relative error improves from 4.951% to 1.266% to 0.3182% at n=23,47,95. Peak entropy at D=3,g=8: 0.136081202028, 0.133404512438, 0.132386863584; successive differences decrease by factor 2.6303, not a demonstrated asymptotic order. A separate small dense eigensolver crosscheck verifies sparse exponential evolution (crosscheck.json). The original positive-peak-only null diagnostic was tightened to a maximum absolute entropy test at the same threshold; original source and log are retained, and the rerun passed. Dense spectral crosscheck: separation error 4.761e-13, entropy error 4.257e-13, eigen residual 4.264e-14. No independent scientific replication or empirical test.

## Interpretation

This positive result does not reverse the QG-020 disjoint tensor-stress null result: it uses a different, reduced Newtonian scalar interaction channel. The entangling operator was supplied, not derived from the EFMW microscopic graph system. The source-density Poisson constraint is represented by its conventional pair Green function, not evolved as a quantum operator constraint. This model does not solve nonlinear quantum constraint closure or demonstrate propagation of gravity-mediated information at finite speed. Classical comparator separability is built in. Full trajectories of observables, not wavefunctions, are recorded in results.json. Numerical choices and tolerances are exploratory, not preregistered.

## Replay

`OPENBLAS_NUM_THREADS=1 python run.py` then `OPENBLAS_NUM_THREADS=1 python crosscheck.py` with Python 3.13.5 and requirements.txt. `index.html` is an offline viewer of the measured trajectories. SHA-256 manifest checks original archived files; replay may change rounding or serialization. The next gate is a gauge-consistent dynamical matter–tensor coupling with constraint and energy checks, rather than simply adding a nonrelativistic potential to QG-020.

## References

- Bose et al., *Spin Entanglement Witness for Quantum Gravity*, Phys. Rev. Lett. 119, 240401 (2017), https://doi.org/10.1103/PhysRevLett.119.240401
- Marletto and Vedral, *Gravitationally Induced Entanglement between Two Massive Particles is Sufficient Evidence of Quantum Effects in Gravity*, Phys. Rev. Lett. 119, 240402 (2017), https://doi.org/10.1103/PhysRevLett.119.240402
- QG-020: https://github.com/enuminous/Quantum-Gravity/tree/580e520c1552949de6ab88c2af28bba9c4db4711/QG-020

## Published laboratory

All twelve files were verified against their original local Git blob hashes: https://github.com/enuminous/Quantum-Gravity/tree/a7700c7a8d8e6895b735535a80a493e469f6cbfd/QG-021 .
