# Standard Model Reduction

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Standard-Model-Reduction) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#fundamental-physics-cosmology-and-quantum-geometry)

<details open>
<summary><strong>On this page</strong></summary>

- [What this project does](#what-this-project-does)
- [Three-line classical Standard Model](#three-line-classical-standard-model)
  - [Tree-level consequences](#tree-level-consequences)
- [What has been verified](#what-has-been-verified)
  - [Reproduce the checks](#reproduce-the-checks)
- [Physical parameter budget](#physical-parameter-budget)
- [The 39-strata hypothesis: research, not result](#the-39-strata-hypothesis-research-not-result)
- [Files](#files)
- [Website deployment](#website-deployment)
- [Research standards and contributions](#research-standards-and-contributions)
- [Connected physics research units](#connected-physics-research-units)


</details>

**Related repositories:** [Higgs-Gauge-Lab](https://github.com/enuminous/Higgs-Gauge-Lab) · [EFMW-Physics-Lab](https://github.com/enuminous/EFMW-Physics-Lab) · [Base888-Quantum-Geometry](https://github.com/enuminous/Base888-Quantum-Geometry) · [Quantum-Gravity](https://github.com/enuminous/Quantum-Gravity) · [QST](https://github.com/enuminous/QST) · [EFMW-Grid](https://github.com/enuminous/EFMW-Grid) · [Ligo_EFMW_Search](https://github.com/enuminous/Ligo_EFMW_Search) · [EFMW](https://github.com/enuminous/EFMW) · [papers](https://github.com/enuminous/papers)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


[![Research status](https://img.shields.io/badge/status-classical%20SM%20reconstruction-69e1d0)](three_line_standard_model_geometric_reduction.md)
[![Verification](https://img.shields.io/badge/verification-16%20targeted%20checks-8ee2b4)](standard_model_check_results.txt)
[![39-strata](https://img.shields.io/badge/39--strata-unresolved-ffc17a)](three_line_standard_model_geometric_reduction.md)

**Interactive dashboard:** **https://enuminous.github.io/Standard-Model-Reduction/**  
**Repository:** https://github.com/enuminous/Standard-Model-Reduction

> **Scientific status (26 October 2026):** A three-line *notation-level* reconstruction of the established classical gauge-invariant Standard Model is given and specific symbolic consistency checks pass. This does **not** prove a new parameter-free theory or an equivalence with the proposed 39-strata lattice. The minimal three-generation Standard Model retains **19 physical parameters** when the strong-CP angle is counted.

## What this project does

The familiar Standard Model Lagrangian can span many lines when expanded into component fields and vertices. The same known theory can be written compactly in geometric language—gauge connections and curvature, associated matter bundles, a scalar Higgs field, and Yukawa morphisms.

The project supplies:

- A readable **three-line master Lagrangian**, with all hidden definitions spelled out.
- A standalone, responsive, dependency-free [research dashboard](index.html) with an interactive tree-level electroweak workbench.
- A technical [manuscript](three_line_standard_model_geometric_reduction.md) documenting the derivation, fermion representations, anomaly checks, parameter count, and limits of the geometric interpretation.
- A reproducible [Python/SymPy check suite](verify_standard_model_reduction.py) and its [recorded output](standard_model_check_results.txt).
- A conditional **39-strata internal-geometry hypothesis**, clearly separated from the established Standard Model reconstruction.

## Three-line classical Standard Model

With three generations, hypercharge convention \(Q=T_3+Y\), and repeated indices understood:

\[
\boxed{\begin{aligned}
\mathcal L_{\rm SM}={}&-\frac14(G^a_{\mu\nu}G^{a\mu\nu}+W^I_{\mu\nu}W^{I\mu\nu}+B_{\mu\nu}B^{\mu\nu})+\sum_{f\in\mathcal F}\bar f i\gamma^\mu D_\mu f\\
&+(D_\mu H)^\dagger D^\mu H-\lambda\left(H^\dagger H-\frac{v^2}{2}\right)^2\\
&-\left[\bar Q_LY_u\widetilde H u_R+\bar Q_LY_dH d_R+\bar L_LY_eH e_R+\mathrm{h.c.}\right]+\frac{\theta_3g_s^2}{32\pi^2}G^a_{\mu\nu}\widetilde G^{a\mu\nu}.
\end{aligned}}
\]

- **Line 1 — Gauge curvature + chiral matter:** the \(SU(3)_C\times SU(2)_L\times U(1)_Y\) field strengths and covariant fermion kinetics.
- **Line 2 — Higgs geometry:** Higgs kinetic term, scalar potential and spontaneous symmetry breaking.
- **Line 3 — Flavor and topological angle:** Yukawa matrices, complex mixing and the QCD \(\theta\) term.

This is an **algebraic rewriting** of the usual classical gauge-invariant SM, not a theory with fewer independent parameters. A gauge-fixed quantum formulation further includes gauge-fixing and Faddeev–Popov terms. In this minimal form neutrinos are massless; neutrino masses require an extension.

### Tree-level consequences

\[
m_W=\frac{gv}{2},\qquad
m_Z=\frac{v}{2}\sqrt{g^2+g'^2},\qquad
m_h^2=2\lambda v^2,\qquad
\sin^2\theta_W=\frac{g'^2}{g^2+g'^2}.
\]

The site has sliders for \(g,g',v,\lambda\) that **recalculate these identities locally in the browser**. They are not a parameter-free prediction, an experimental fit, or a loop-level renormalization calculation.

## What has been verified

The committed script performs **16 checks**:

| Class | Count | What it establishes |
| --- | ---: | --- |
| Yukawa hypercharge neutrality | 3 | Correct gauge-invariant charge combinations |
| Local triangle/mixed anomaly cancellation | 4 | Exact per-generation anomaly sums |
| Higgs and electroweak algebra | 5 | Scalar expansion, Higgs mass, neutral/charged boson relations |
| Parameter arithmetic | 1 | 19-parameter minimal-SM count |
| Errors in the original 39-strata infographic | 3 | Detects incorrect \(\sqrt{157}\), coupling arithmetic and mass-ladder claim |
| **Total** | **16** | **Targeted algebraic and consistency checks, not an equivalence proof** |

The graphic originally asserted \(\sqrt{157}=11.7047\), whereas \(\sqrt{157}\approx12.529964\); its displayed strong-coupling expression yields a different number than quoted; and a literal single-ratio fermion mass ladder conflicts with the electron–muon mass ratio.

**Independent physical predictions eliminated: 0** in the present 39-strata proposal.

### Reproduce the checks

Requirements: Python 3.10+ and SymPy.

```bash
python -m pip install sympy
python verify_standard_model_reduction.py
```

Compare with [the recorded output](standard_model_check_results.txt). Assertions are local algebraic checks; they do not establish physical equivalence of an unspecified geometric lattice.

## Physical parameter budget

| Sector | Number |
| --- | ---: |
| \(g_s,g,g'\) gauge couplings | 3 |
| Higgs potential \(v,\lambda\) | 2 |
| Quark and charged-lepton masses | 9 |
| CKM angles and CP-violating phase | 4 |
| Strong CP angle \(\bar\theta\) | 1 |
| **Total (minimal three-generation SM)** | **19** |

The gauge-group topology does not fix the three continuous gauge-kinetic normalization factors. Similarly, allowing an arbitrary internal overlap construction does not constrain the Yukawa matrices: without independently fixed profiles and operators, the same parameters have merely been moved.

## The 39-strata hypothesis: research, not result

A candidate finite internal geometry could generate flavor matrices through overlaps:

\[
(Y_f)_{ij} = g_*\sum_{k=1}^{39} w_k\,
u^{(f)*}_{L,i}(k)\,h_f(k)\,u^{(f)}_{R,j}(k).
\]

This is an **ansatz**. A meaningful reduction must:

1. Define an explicit graph and discrete Dirac/Laplacian, including symmetries and boundary conditions.
2. Derive the correct chiral matter and Higgs representation content, with anomaly cancellation.
3. Fix the coupling, spectral weights, eigenmodes and profiles **without using the observable being predicted**.
4. Freeze at least one observable prediction in advance and calculate the relevant renormalization/running.
5. Compare with experiment and seek independent replication.

Without those steps the notation is a model-building possibility, not evidence for parameter elimination.

## Files

| File | Purpose |
| --- | --- |
| [index.html](index.html) | Standalone, offline-capable dashboard; responsive; no frameworks or CDN |
| [three_line_standard_model_geometric_reduction.md](three_line_standard_model_geometric_reduction.md) | Complete technical reconstruction and conditional research program |
| [verify_standard_model_reduction.py](verify_standard_model_reduction.py) | Reproducible symbolic and numerical checks |
| [standard_model_check_results.txt](standard_model_check_results.txt) | Captured verification output |
| [.github/workflows/pages.yml](.github/workflows/pages.yml) | GitHub Pages build and deployment |

## Website deployment

The site is entirely static and can be opened directly from `index.html`. The included GitHub Actions workflow deploys the repository root to GitHub Pages on pushes to `main`.

**Deployment status (26 October 2026): ACTION REQUIRED.** The first workflow run [#1](https://github.com/enuminous/Standard-Model-Reduction/actions/runs/40396210227) failed at `actions/configure-pages@v5`. GitHub reported `Create Pages site failed: Resource not accessible by integration`, because the Pages site has not yet been configured and the workflow token cannot enable it.

**Repository owner action:** Open [Settings → Pages](https://github.com/enuminous/Standard-Model-Reduction/settings/pages), select **Build and deployment → Source: GitHub Actions**, then open [Actions](https://github.com/enuminous/Standard-Model-Reduction/actions/workflows/pages.yml) and rerun the deployment workflow if it does not start automatically. This is a repository administration setting that must be set by someone with the appropriate access. The HTML, README and deployment workflow are already committed.

**Expected website address:** https://enuminous.github.io/Standard-Model-Reduction/

## Research standards and contributions

Criticism, attempted falsification, independent reproduction, and mathematical corrections are welcome. Please cite a concrete equation, an explicit failing calculation, and ideally an executable counterexample. Report scientific claims as **PASS**, **FAIL**, or **UNRESOLVED**, never as established solely because the notation is elegant or concise.

The manuscript links sources including CERN teaching material and Particle Data Group reviews. This repository is an independent reconstruction and research exercise; it does not claim CERN, PDG, or other institutional endorsement.

<!-- ENUMINOUS-RESEARCH-CHAIN:START -->
## Connected physics research units

**Established-theory reconstructions and baseline laboratories:** [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction) · [Higgs-Gauge-Lab](https://github.com/enuminous/Higgs-Gauge-Lab) · [EFMW-Physics-Lab](https://github.com/enuminous/EFMW-Physics-Lab)

**Proposed quantum-geometry bridge:** [Base888-Quantum-Geometry](https://github.com/enuminous/Base888-Quantum-Geometry) · [QST-001](https://github.com/enuminous/Quantum-Gravity/blob/main/QST-001.md) · [QST-002](https://github.com/enuminous/QST/blob/main/QST-002.md)

**EFMW definitions, pressure-cycle model, and spacetime investigations:** [Canonical 102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean review](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [RHC-001: Rahasya pressure-cycle formalization](https://github.com/enuminous/papers/blob/main/RHC-001-EFMW-Rahasya-Pressure-Cycle-Formalization.md) · [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian) · [Cosmology](https://github.com/enuminous/Cosmology)

> **Interpretation:** Cross-links represent research dependencies and comparisons. The Standard Model and continuum gravity are inputs in current QST calculations; their emergence from Base888 and the physical status of the pressure cycle remain **UNRESOLVED**.
<!-- ENUMINOUS-RESEARCH-CHAIN:END -->
