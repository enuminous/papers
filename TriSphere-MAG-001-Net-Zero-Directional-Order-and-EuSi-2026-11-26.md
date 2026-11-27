# TRISPHERE-MAG-001 — Net-zero directional order

26 November 2026 · Monolithic LLC · Exploratory computational correspondence test, not peer reviewed.

## Verdict
PASS for the specified conventional exchange-only model; TriSphere-to-EuSi physical correspondence UNRESOLVED. This is not a material-specific band calculation, a fit to spectroscopy, or an independently derived prediction of the Blueprint.

## External evidence and scope
Cheng et al., Nature (2026), [DOI 10.1038/s41586-026-11295-9](https://doi.org/10.1038/s41586-026-11295-9); [Max Planck Institute announcement, 18 November 2026](https://www.cpfs.mpg.de/3772423/20261118). Neutron diffraction supports a coplanar commensurate spiral between approximately 33.4 and 62 K with propagation vector (0,1/3,0). The moments rotate by pi/3 between adjacent double layers; the toy three-site 2pi/3 spiral is not the actual EuSi structure. Spin-ARPES finds polarization signatures consistent with odd parity; overlapping folded bands limit eigenstate-specific interpretation. The study's calculations with and without spin-orbit coupling support primarily exchange-driven splitting. The paper also reports chiral domains around 10 micrometers. No experimental data have been fit or reproduced here.

## Mathematical benchmark
Use a single-orbital chain with spin-independent nearest-neighbor hopping t=1 and on-site exchange J n_j dot sigma, with n_j=(sqrt(1-b^2)sin(Qj+phi), b, sqrt(1-b^2)cos(Qj+phi)). Q=2pi w/L. For b=0 and Q=2pi/3 the mean moment vanishes and mean directed nearest-neighbor cross product along y is sqrt(3)/2.

A site-dependent spin rotation U_j=exp(-i Qj sigma_y/2) gives the 2x2 generalized-momentum Hamiltonian

H(k)=-2t cos(k)cos(Q/2) I + [Jb-2t sin(k)sin(Q/2)] sigma_y + J sqrt(1-b^2)[cos(phi)sigma_z+sin(phi)sigma_x].

The spin-resolved *physical momentum* p spectrum must be unfolded: for y-spin s=+/-1 use k=p+sQ/2, and spectral projector (I+s sigma_y)/2. The independent implementation diagonalizes the 2L x 2L magnetic-cell Bloch matrix with boundary phase exp(ipL), and projects eigenvectors onto exp(ipj)/sqrt(L) plane waves. Lorentzian broadening eta is phenomenological. Define A=A_++A_-, Y=A_+-A_-, P_y=Y/A. For a coplanar real-space exchange Hamiltonian, complex conjugation maps p to -p and flips sigma_y; A is even and Y is odd. Reversing Q at phi=0 is related by a spin rotation of pi about z, so Y changes sign. Neither property follows from a zero vector sum alone. Global static rotation about y leaves the y-spin spectrum invariant; a time-dependent rotation is not tested by this statement.

## Numerical results
12 configurations, 241 momenta, 351 energies, 1,015,092 momentum-energy samples. All 16 checks passed. Peak absolute polarization uses A > 10% of its global maximum; it is not a physical spin-ARPES measurement. Odd and even spectral maxima are normalized to max A. Results below are rounded; results.json contains full summaries and a fixed energy cut; spectra.npz contains complete intensity and three spin spectral components.

| Model | Mean moment | Peak abs(P_y) | Odd spectral maximum | Even spectral maximum |
|---|---:|---:|---:|---:|
| Spiral | 1.33e-16 | .987339 | .495446 | 7.27e-15 |
| Reversed spiral | 1.33e-16 | .987339 | .495446 | 8.78e-15 |
| Zero exchange | 1.33e-16 | 2.21e-15 | 1.18e-15 | 7.80e-16 |
| Collinear antiferromagnet | 6.12e-17 | 2.53e-15 | 1.58e-15 | 3.31e-16 |
| Six-site spiral | 1.48e-16 | .987351 | .586064 | 6.50e-15 |
| Conical, b=.35 | .35 | .992741 | .343192 | .638933 |
| Ferromagnet along y | 1 | .996815 | 7.19e-15 | .996810 |

Across all cases, independent spectral unfolding residual <=2.01e-14. Chirality reversal residual 1.21e-14; equal-domain mixture residual 6.03e-15; global phase shift residual 1.60e-14. The nonzero odd signal persists at J=.25 and 2 and eta=.04 and .16. The conical and ferromagnetic controls produce an even component. An equally weighted incoherent mixture of opposite chiral domains cancels the odd spin spectrum, despite each domain being ordered. No transport calculation or material parameter fit is claimed.

## Blueprint audit
The live Blueprint at https://tri-sphere-text.abethjones.workers.dev/ was inaccessible. The audited repository snapshot is [86115e0](https://github.com/enuminous/trisphere/tree/86115e01fdde06df9f06ecadfb3b576a6288121b). The [corrected manuscript](https://github.com/enuminous/trisphere/blob/86115e01fdde06df9f06ecadfb3b576a6288121b/source/blueprint-corrected.txt#L205-L267) identifies a dimensionless scalar radial trajectory, damping and externally triggered energy kicks. Its [directional seam description](https://github.com/enuminous/trisphere/blob/86115e01fdde06df9f06ecadfb3b576a6288121b/source/blueprint-corrected.txt#L363-L395) is interpretive; the [two-way loop description](https://github.com/enuminous/trisphere/blob/86115e01fdde06df9f06ecadfb3b576a6288121b/source/blueprint-corrected.txt#L435-L451) distinguishes expansion, collapse and recurring motion. The [Lean source](https://github.com/enuminous/trisphere/blob/86115e01fdde06df9f06ecadfb3b576a6288121b/TriSphere.lean) includes phase/radius, Hopf and scalar energy identities, but no electron exchange Hamiltonian or spin-resolved momentum observable. The [return map](https://github.com/enuminous/trisphere/blob/86115e01fdde06df9f06ecadfb3b576a6288121b/protocol/RETURN-MAP-002.md) does not supply them either.

The same zero mean moment can coexist with positive, negative or absent odd spin texture. Consequently net zero plus generic two-way motion cannot establish the EuSi correspondence. Even setting an imposed spiral's common phase from a TriSphere oscillator would not derive its static spin texture: the spectrum is unchanged under that phase shift. No microscopic map is defined in the audited executable equations. This is a bounded missing-specification finding, not a general theorem ruling out extensions of the Blueprint. The live manuscript may have changed.

## Next gate: TRISPHERE-MAG-002
Before inspecting further outcome data, freeze a map from the Blueprint's states to a physical vector order parameter, a spatial handedness variable, electronic Hilbert space, translation action and an exchange Hamiltonian with units. Derive Q, the spin axis and parity from the proposed dynamics rather than inserting them. Demand chirality reversal, zero exchange, collinear order, equal-domain mixture and conical controls, plus comparison against the conventional exchange-only baseline. Without an additional prediction distinguishing the models, agreement would remain correspondence, not confirmation of TriSphere.

## Reproduce
Python 3.13.5, NumPy 2.3.5. Run `OPENBLAS_NUM_THREADS=1 python run.py`. The code writes results.json and spectra.npz, then checks all sixteen predicates. Redirect stdout to log.txt. Numerical tolerances are exploratory, not preregistered. Independent replication remains outstanding. SHA-256 manifest records original local bytes; a different runtime or archive serializer may produce different bytes.

## Published executable and evidence

https://github.com/enuminous/trisphere/tree/90120858f49229d04c8c33e7ed81cf9e49340c67/experiments/TRISPHERE-MAG-001

# Publication scope

This repository contains the executed Python source, its dependency pin, original README, 12-case rounded TSV and a SHA-256 manifest of the complete local archive. The full generated results.json, spectra.npz (approximately 29 MB), and log.txt are supplied in the separate downloadable archive; they can be regenerated from run.py. The manifest deliberately covers the original complete local package and is not a claim that those generated files were uploaded to GitHub. All 16 checks passed locally. Independent reproduction and physical validation are outstanding.
