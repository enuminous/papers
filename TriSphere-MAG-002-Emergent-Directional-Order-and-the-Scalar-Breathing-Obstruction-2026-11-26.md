# TRISPHERE-MAG-002 — Emergent directional order and the scalar breathing obstruction

26 November 2026 · Monolithic LLC · exploratory computational extension. Not peer reviewed.

## Verdict
PASS for the analytical ground-state construction, electronic symmetry checks and radial time-change control. FAIL for the tested random-start local optimizer reaching the exact three-step ground state (0/72). UNRESOLVED: independently deriving the magnetic interactions from TriSphere or quantitatively explaining EuSi. Fourteen programmed diagnostic assertions passed; the relaxation failure is an experimental outcome, not an assertion success or a universal dynamical impossibility.

## Evidence and scope
Prior benchmark: [MAG-001](https://github.com/enuminous/trisphere/tree/90120858f49229d04c8c33e7ed81cf9e49340c67/experiments/TRISPHERE-MAG-001). Audited [Blueprint snapshot](https://github.com/enuminous/trisphere/tree/86115e01fdde06df9f06ecadfb3b576a6288121b), in particular [scalar trajectory and pump](https://github.com/enuminous/trisphere/blob/86115e01fdde06df9f06ecadfb3b576a6288121b/source/blueprint-corrected.txt#L205-L267) and [boundedness proof](https://github.com/enuminous/trisphere/blob/86115e01fdde06df9f06ecadfb3b576a6288121b/protocol/RETURN-MAP-002.md). The live manuscript was not retrieved for this follow-up. External experiment: Cheng et al., [Nature, 18 November 2026](https://doi.org/10.1038/s41586-026-11295-9). The measured EuSi spiral turns 60 degrees between adjacent double layers, with threefold periodicity along the crystallographic b axis. The 120-degree single-site model here is an illustrative three-step analog, not the material's magnetic structure. Its exchange constants are dimensionless and not derived from the Blueprint or fitted to EuSi. No material-specific predictions, finite-temperature phase transitions, or 10-micrometer domains are calculated.

## 1. Constructed minimal extension and exact ground-state bound
Let z_j=exp(i theta_j) denote independent planar unit vectors on N periodic sites. Add H= sum_j [cos(theta_(j+1)-theta_j)+r cos(theta_(j+2)-theta_j)], r=J2/J1>=0, with J1=1. The Hamiltonian does not contain a preferred pitch or handedness. Both the phase plane and interactions are additional assumptions. With Fourier amplitudes a_k=N^(-1)sum_j z_j exp(-ikj), Parseval gives sum_k |a_k|^2=1, and H/N=sum_k (cos k+r cos 2k)|a_k|^2. Hence H/N>=min_k (cos k+r cos 2k), saturated by a uniform twist at a minimizing allowed k. In the infinite-chain limit minimize 2r x^2+x-r on x=cos Q in [-1,1]. For r<=1/4, Q=pi. For r>1/4, cos Q=-1/(4r). The two signs of Q are degenerate; at r=.5, Q=+/-2pi/3. The ratio .5 was chosen as a comparison and the model cannot predict it. At N=24,48,96 and nine ratios, the maximum discrepancy between uniform-twist energy and its exact finite-grid Fourier bound is 2.22e-16. The collinear and spiral states both have zero mean moment when the pitch is commensurate and nonzero. No finite-temperature spontaneous symmetry breaking is claimed.

| J2/J1 | Infinite-chain pitch (degrees) | N=96 allowed pitch (degrees) |
|---:|---:|---:|
| .2 | 180 | 180 |
| .3 | 146.442690 | 146.25 |
| .4 | 128.682187 | 127.5 |
| .5 | 120 | 120 |
| .6 | 114.624318 | 116.25 |
| .8 | 108.209957 | 108.75 |
| 1 | 104.477512 | 105 |

## 2. Can the system reach that state?
For each of 3 sizes and ratios .2,.5,.8, generate 12 independent random angle vectors and their exact reflections using NumPy seed 20261126. Relax using L-BFGS-B with analytic gradient. Reflection pairing tests equivariance, not independent statistical preference for chirality. The optimizer is not physical spin dynamics or a thermal sampler. Ground hit: energy gap per site <1e-6. All 216 runs report optimizer success, but only 26 meet the ground criterion. At r=.5, 0/72 meet it. Best remaining gaps at N=24,48,96 respectively .041666667,.041666667,.031384172; mean gaps .062493407,.064185233,.066786519. Dominant Fourier mode mean weight .338640,.212312,.181342 respectively, vs 1 for a uniform twist. Reflected outcomes have identical energies and opposite chirality to reported precision. This is a failure of the tested local search, not proof that all dynamics fail. No claim that every endpoint is a proven local minimum. Full final angle vectors are in results.json.

| N | Ground hits, r=.2 | Ground hits, r=.5 | Ground hits, r=.8 |
|---:|---:|---:|---:|
| 24 | 10/24 | 0/24 | 4/24 |
| 48 | 8/24 | 0/24 | 0/24 |
| 96 | 4/24 | 0/24 | 0/24 |

## 3. Electronic consequences of the ideal ordered state
For the ideal continuum pitch Q, use MAG-001's standard rotating-frame exchange-only electronic model, t=1, J=1, no spin-orbit coupling. H(k)=-2 cos k cos(Q/2) I -2 sin k sin(Q/2) sigma_y + J sigma_z. Unfold physical momentum p using k=p+sQ/2 and project onto s=+/-1 y-spin. Lorentzian broadening eta=.08. Each of nine ratios is evaluated with positive Q, reversed Q, and zero exchange (27 spectral arrays; each 241x151). This uses ideal uniform spiral states, not the failed random-relaxation endpoints. Define A=A_plus+A_minus, Y=A_plus-A_minus; odd and even components normalized by max A. Collinear cases r<=.25 have odd signal <=1.66e-15. For r>.25 odd signal .469–.535, even residual <=3.80e-15. At r=.5, peak |Y/A|=.987359 where A>.1 max A, and odd spectral maximum .513694. Chirality reversal residual zero in this implementation; zero-exchange residual <=3.41e-15. These are model spectra, not independent measurements or a material-specific band fit. The unfolding formula was previously cross-checked in MAG-001; this follow-up uses its analytic implementation only.

## 4. Does the breathing oscillator generate magnetic order?
The scalar radial return-map candidate uses R=12, gamma=.08, V=.02 min(rho,11)^2, elastic outer reflection and a central kick of 5. Reconstructed one excursion at the earlier fixed launch energy 7.268050808342798. Numerically T=9.638611257581818, loss=5.000000000009045. Test the explicitly added one-way common modulation H(t)=f(t)H_mag, f(t)=1+.6 rho(t)/12>0. For overdamped spin relaxation dtheta/dt=-f(t) grad H_mag(theta), define tau(t)=integral_0^t f(s) ds. Then dtheta/dtau=-grad H_mag, exactly the unmodulated dynamics with a new clock. The oscillator cannot change energy minima, select a handedness, or change paths in configuration space in this model. It can change the amount of effective relaxation reached at a given physical time. Eight random paired trajectories across the period give tau(T)=12.714661894225346 and max unit-vector discrepancy 5.50e-9 compared to unmodulated relaxation at tau(T); exact reflection discrepancy zero to reported precision. This is not a claim about all possible radial couplings, especially differential or feedback couplings. The actual Blueprint lacks a specified microscopic spin exchange law.

## 5. Next gate and scientific boundary
If local dynamics should reach the ordered state, a distinct MAG-003 test could compare stochastic annealing, domain coarsening and frustrated conventional controls. To test a uniquely TriSphere-derived mechanism, first specify a nonfactorizable coupling (e.g. distinct radial dependence of J1 and J2) from the Blueprint before measuring the outcomes. Preserve reflection symmetry unless a physical chiral bias is derived; predeclare a discriminator against the ordinary frustrated spin chain. Without that independent specification, the conventional ground-state model already explains these results and does not validate TriSphere or predict EuSi's pitch. A shared mathematical structure is not a shared physical mechanism.

## Replay
Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. `OPENBLAS_NUM_THREADS=1 python run.py > log.txt` regenerates results.json and checks 14 predicates. The pre-execution protocol is included. The first attempt completed calculations but JSON serialization rejected NumPy booleans; original source and traceback are retained. The final correction converts check values to native bool only. Independent scientific replication remains outstanding. Parameters and thresholds were selected for this exploratory test, not independently preregistered. All quantities dimensionless.

## Published laboratory

All nine files were verified against their original local Git blob hashes: https://github.com/enuminous/trisphere/tree/8b27d640c7b298c2208ad75f554201e97f43b5e1/experiments/TRISPHERE-MAG-002 .
