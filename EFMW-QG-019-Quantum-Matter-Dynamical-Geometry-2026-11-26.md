# QG-019 — Quantum matter and dynamical geometry

26 November 2026 · Monolithic LLC · EFMW exploratory research. **PASS_BOUNDED** for the specified oscillator and static Poisson models; no derivation of quantum gravity.

## Scope

QG-018 tested nonlinear classical spherical Einstein–scalar dynamics. QG-019 is a separate controlled diagnostic, not a quantization of that solver. It tests which information is lost by replacing a quantum source with its mean. Two probes interact with a quantum oscillator; a separate periodic one-dimensional Poisson problem tests expectation-value versus branch-level constraints. Neither model includes dynamical Einstein constraints or a derived gravitational mediator. All parameters and acceptance thresholds are exploratory, not preregistered.

## A. Quantum mediator and controls

Set ℏ=ω=1, H=a†a+F(a+a†), F=g_A Z_A+g_B Z_B. Initial probes |+>|+>; oscillator starts in a thermal state with mean occupation n̄. Six coupling pairs (0,0), (.25,0), (.1,.1), (.25,.25), (.35,.35), (.2,.3); n̄=0,.5,2. With f_i the eigenvalues of F, the exact reduced probe density matrix is

ρ_ij(t)=¼ exp[i(f_i²−f_j²)(t−sin t)] exp[−(2n̄+1)(f_i−f_j)²(1−cos t)].

This follows by completing the square in each displaced oscillator Hamiltonian. Conditional oscillator displacement is ⟨a+a†⟩_i=−2 f_i(1−cos t); ensemble mean vanishes. The self-consistent mean-field equations are ẍ+x=−2⟨F⟩, with local spin Hamiltonian xF; ⟨F⟩=0 is constant, and zero initial mean position/momentum yields x=0 and unchanged probes. This is analytical, not a separately integrated nonlinear mean-field code.

Classical stochastic comparator: average product phase rotations exp(−i ξF) with ξ Gaussian, variance 2(2n̄+1)(1−cos t). Its reduced matrix reproduces every coherence magnitude exactly but lacks the f_i² phase. This is a prescribed correlated classical random field, not a general stochastic Einstein theory or a model of all classical mediation. Each realization is a product of local unitaries, so the mixture cannot entangle the probes.

At a full oscillator period 2π, the mediator returns to its initial thermal state independently of the probes, leaving the probe gate exp(i 4π g_A g_B Z_A Z_B) up to a global phase. The negativity (sum of negative partial-transpose eigenvalue magnitudes) is |sin(8πg_Ag_B)|/2. At g_A=g_B=.25 the negativity is .5, the two-qubit maximum, for all three thermal occupations. At .1,.1 it is .124344943582; at .35,.35 it is .031395259765 (nonmonotonic due to phase periodicity). With one or both couplings zero, negativity is zero up to rounding. Intermediate probe purity for initial vacuum diagnoses probe–oscillator entanglement because the total state is pure; for thermal initial states reduced purity alone is not an entanglement witness. The oscillator/probe partition disentangles at full revival in the ideal model.

| n̄ | Negativity at t=π | Negativity at t=2π |
|---:|---:|---:|
| 0 | .132056212483 | .5 |
| .5 | .056104410312 | .5 |
| 2 | .003324904490 | .5 |

18 analytic configurations ×129 samples =2322; 54 independent finite-matrix configurations (18 × cutoffs 24,48,80) ×33 samples =1782. Finite matrix eigendecomposition uses four independent oscillator blocks and a truncated thermal mixture; computes reduced matrix by tracing the oscillator, conditional position and total energy. Worst analytic–numeric element errors at cutoffs 24,48,80: 9.95558e-4,5.64077e-7,1.11810e-11. At 80, worst energy residual 2.52503e-15, trace error 7.77156e-16, conditional position discrepancy 4.39900e-10, minimum sampled probe eigenvalue −2.56999e-16. Classical stochastic negativity ≤2.603e-16. All 12 programmed checks (including Poisson) passed; exact null controls and nonzero coupling controls included. The coarse cutoff discrepancies are retained, not hidden. No irreversible loss or universal classical limit is inferred. Weak coupling and fixed-source limits agree in the bounded senses tested.

## B. Static Poisson constraint

Periodic unit-length ring, two normalized Gaussian profiles centered at .25 and .75 (width .045); subtract uniform background to ensure zero mean. Discrete Laplacian L=(shift+inverse shift−2I)N², source ρ̂=diag(ρ_A,ρ_B) in the matter branch basis, dimensionless coefficient 1. For p in 0,.1,.25,.5,.75,.9,1 and N=64,128,256, compare the single mean potential φ̄=L⁺(pρ_A+(1−p)ρ_B) with controlled branch potentials φ_i=L⁺ρ_i. The mean residual Lφ̄−⟨ρ̂⟩ is zero to numerical precision; the RMS residual of Lφ̄ I−ρ̂ is sqrt[p(1−p) mean((ρ_A−ρ_B)²)], nonzero for mixed branch weights. At p=.5,N=256: mean residual 6.61027e-13; operator residual RMS 1.770419886712; branch residual 2.49045e-12; potential RMS fluctuation .0345367161962; branch mean and semiclassical mean agree to 3.47e-18. Operator RMS vanishes at p=0 or 1 to numerical precision. Across 21 cases, worst mean/branch residual 2.49045e-12; variance-identity error 8.11544e-13. This compares static branchwise constraints, not gravitational quantum dynamics. The controlled potential is an operator defined algebraically on the source space, not an independent quantum geometry Hilbert space. The RMS is not a violation of the semiclassical equation, which requires only the mean identity, and identical results hold for incoherent branch mixtures. This test is not an entanglement witness.

## Interpretation and limitations

The closed oscillator gate is standard quantum mechanics, familiar from spin-dependent force gates. Entanglement generation in this model does not certify actual gravity, exclude all possible classical/nonlocal/hybrid theories, or derive a gravitational coupling. A single-mode model has no spatial tensor structure, Lorentzian dynamics, gauge constraints or local stress-energy tensor. The static Poisson problem illustrates mean versus branch fluctuations but does not test momentum constraints or covariance. The two parts are distinct diagnostic models. EFMW-specific predictions and empirical evidence remain absent; independent replication outstanding. Next gate: build a spatially extended quantized linearized gravitational reference coupled to explicitly conserved matter sources, check gauge-invariant observables and contrast expectation-value and quantum responses with identical sources, before seeking nonlinear closure.

## References

- C. Marletto and V. Vedral, PRL 119, 240402 (2017), https://doi.org/10.1103/PhysRevLett.119.240402
- S. Bose et al., PRL 119, 240401 (2017), https://doi.org/10.1103/PhysRevLett.119.240401
- B. L. Hu and E. Verdaguer, Stochastic Gravity: Theory and Applications (2004), https://doi.org/10.12942/lrr-2004-3
- P. C. Haljan et al., PRA 72, 062316 (2005), https://doi.org/10.1103/PhysRevA.72.062316
- QG-018 classical benchmark: https://github.com/enuminous/Quantum-Gravity/tree/ec7b038e6233554f251d2e0abddd674dfaaa1095/QG-018

## Replay

Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. `OPENBLAS_NUM_THREADS=1 python run.py > log.txt` writes `results.json`; `python verify.py` verifies original package bytes before replay. `index.html` is an offline browser explorer with the recorded analytical curves and Poisson diagnostics. No physical units are claimed.

## Published laboratory

All eight files were verified against their original local Git blob hashes: https://github.com/enuminous/Quantum-Gravity/tree/05d1b9de8156a899f4073cb15393ff840e036d57/QG-019 .
