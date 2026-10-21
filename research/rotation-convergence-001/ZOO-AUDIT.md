# RC-001 Zoo audit — frozen scope, 21 October 2026

| Claim | Evidence/status | Verdict |
|---|---|---|
| Standard planar hinge obeys J²=-I | Direct 2×2 algebra; candidate Lean file uncompiled | **Analytically pass; formal build open** |
| Standard hinge flow matches v=(-ωy,ωx,0) | Written derivation in Two Paths to Rotation | **Analytically pass; integrated proof open** |
| Rigid flow has curl (0,0,2ω) | Coordinate derivatives; candidate Lean defines frozen curl algebraically | **Analytically pass; general derivative theorem open** |
| Every hinge J²=-I represents Euclidean rigid rotation | Counterexample J=[[0,-2],[1/2,0]] (not orthogonal) | **False without metric compatibility** |
| Curl determines any velocity field uniquely | Adding ∇f preserves curl | **False without gauge/boundary constraints** |
| Baseline ordinary wave scalar can exhibit nonzero curl of proxy current | Exact φ=(x²+t²)y/2; local numpy check; t=0 negative control | **Pass for proxy only** |
| Baseline current curl establishes physical fluid vorticity | Landau velocity not computed | **Unsupported** |
| EFMW C1 physically generates vorticity | Prior R-001 section 9 reports conditional local result; not independently reproduced in RC-001 | **Open for independent reproduction** |
| C1 exceeds matched conventional two-scalar dynamics | No matched comparator run | **Open** |
| EFMW requires universal rotation | Constant source-free φ is a valid counterexample to necessity from scalar equation alone | **Not established** |
| CMB preferred axis proves cosmic vorticity | An alignment statistic is not a dynamical global-rotation measurement | **Not established** |
| Independent Lean/CI reproduces results | No Lean executable available locally; workflow not installed | **Not verified** |

## Adversarial probes
- **CIRCUS**: require explicit citations from theorem statements to relevant source definitions; do not count declared axioms as derived dynamics.
- **MONSTER**: perturb initial gradients, sign of ω, metric-compatible vs nonorthogonal hinges, boundaries and numeric resolution.
- **TORTOISE**: demand controls for ω=0, initial momenta zero, single vs two scalars, and conventional Lagrangian.
- **DUCK**: record numerical seeds, physical units, action, stress tensor, observer convention, and solver before publication.
- **Goose**: reject any inference from a green build or aesthetically compelling plot to a cosmological law.

## The honest null
For the conventional polynomial wave example, curl(j)≠0 at positive time while curl(j)=0 at t=0. This is evidence against claiming that *flux-curl generation alone* is uniquely EFMW. It says nothing decisive about the reported two-scalar Landau-frame flow until the definitions and dynamics are matched.
