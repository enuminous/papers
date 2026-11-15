# Base888 Quantum Geometry

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Base888-Quantum-Geometry) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#fundamental-physics-cosmology-and-quantum-geometry)

<details open>
<summary><strong>On this page</strong></summary>

- [Open and deploy](#open-and-deploy)
- [What it does](#what-it-does)
- [First experiments](#first-experiments)
- [Source files (flat root)](#source-files-flat-root)
  - [Run mathematical regression tests](#run-mathematical-regression-tests)
- [Connection to original sources](#connection-to-original-sources)
- [Connected physics research units](#connected-physics-research-units)


</details>

**Related repositories:** [Quantum-Gravity](https://github.com/enuminous/Quantum-Gravity) · [QST](https://github.com/enuminous/QST) · [Codex-888](https://github.com/enuminous/Codex-888) · [EFMW](https://github.com/enuminous/EFMW) · [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction) · [EFMW-Physics-Lab](https://github.com/enuminous/EFMW-Physics-Lab) · [Higgs-Gauge-Lab](https://github.com/enuminous/Higgs-Gauge-Lab) · [papers](https://github.com/enuminous/papers)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


**Interactive finite quantum-information and relational-geometry laboratory** inspired by the symbolic `enuminous/Codex-888` system and the EFMW research program. **Not a solution of quantum gravity.**

## Open and deploy

- Open `index.html` directly in a current browser. It is self-contained, includes its own JavaScript and CSS, and needs no packages, network, account, or server.
- For GitHub Pages: create a new repository named `Base888-Quantum-Geometry`, upload all files from this ZIP directly to its root (not into a nested folder), go to **Settings → Pages**, select **Deploy from a branch → main → /(root)**.
- Optionally use `python3 -m http.server 8000` in the repository folder and browse to `http://localhost:8000`.

## What it does

- Evolves a 49-register quantum graph made from 120 **exact independent entangled pair states**.
- Uses the mutual information of those states to *assign* positive edge lengths and constructs a 72-face triangulated geometry. Calculates interior angle-defect curvature and graph shortest paths.
- Compares the reference evolution with a separately prescribed `kappa` perturbation called **EFMW-inspired candidate**, with side-by-side interactive visualizations and a difference map.
- Implements a genuinely complex **888-amplitude single-qudit** unitary circuit as an independent demonstration.
- Computes an EFMW-style **recursive residual monitor** (an estimator, not quantum coherence).
- Checks limited quantum and geometry identities with PASS/FAIL/UNRESOLVED/N/A; exports JSON, CSV and PNG.
- Offers 887, 888, and 889 state-count control options. In this construction all three support the same local effective 64-dimensional space, so its geometry does not depend on 888.

## First experiments

1. Launch with default `Localized entanglement pulse`, `d=888`, `kappa=+0.80`. Let it evolve. Switch **Mutual information → Curvature → Metric distortion**.
2. Press **κ = 0 null**. Both displayed geometries and their paths should match exactly; check Zoo status `PASS` for null reduction.
3. Set `Uniform state · flat control`, `kappa=0`. At baseline every link has the same pair entropy and edge-length scale, so interior curvature should vanish to numerical precision.
4. Change the state dimension to 887 or 889, or press **887 / 888 / 889**. The current reduced model cannot establish that 888 is special. Independent register wavepacket plot uses each selected `d`.
5. Click two nodes to compute weighted shortest-path lengths and compare the candidate against the reference.
6. Export the experiment JSON for a full reproducibility snapshot. Run the independent tests below.

## Source files (flat root)

| File | Purpose |
|---|---|
| `index.html` | Full independent browser simulation |
| `README.md` | Setup and quick-start experiments |
| `MODEL.md` | Equations, derivations, scope and assumptions |
| `VALIDATION.md` | Tests and limits of the checks |
| `model.py` | Independent stdlib reference calculations |
| `test_model.py` | Small independent regression suite |
| `TEST_RESULTS.md` | Results of browser and Python validation |
| `browser_checks.json` | Machine-readable browser smoke-test record |
| `LICENSE_NOTICE.md` | Rights notice: no license assigned on author's behalf |
| `preview.png` | Browser screenshot |

### Run mathematical regression tests

```bash
python3 -m unittest -v test_model.py
```

These checks do not constitute independent physical verification. The browser alone is sufficient to run the simulation.

## Connection to original sources

- [enuminous/Codex-888](https://github.com/enuminous/Codex-888): symbolic 888-state foundation, cyclic phase arithmetic; no quantum amplitudes in the original formalization.
- [enuminous/EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian): separately versioned effective-action candidate with open physical obligations.
- [EFMW-F001 recursion specification](https://github.com/enuminous/papers/blob/main/EFMW-F001-Recursive-Coherence-Dynamics.md): candidate residual/coherence estimator.

**This application does not claim to implement the complete Codex888 theorem library, the EFMW C1 Lagrangian, general relativity, quantum field theory or quantum gravity.** It is an executable route for asking specific questions of finite quantum information and candidate relational geometry.

<!-- ENUMINOUS-RESEARCH-CHAIN:START -->
## Connected physics research units

**Established-theory reconstructions and baseline laboratories:** [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction) · [Higgs-Gauge-Lab](https://github.com/enuminous/Higgs-Gauge-Lab) · [EFMW-Physics-Lab](https://github.com/enuminous/EFMW-Physics-Lab)

**Proposed quantum-geometry bridge:** [Base888-Quantum-Geometry](https://github.com/enuminous/Base888-Quantum-Geometry) · [QST-001](https://github.com/enuminous/Quantum-Gravity/blob/main/QST-001.md) · [QST-002](https://github.com/enuminous/QST/blob/main/QST-002.md)

**EFMW definitions, pressure-cycle model, and spacetime investigations:** [Canonical 102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean review](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [RHC-001: Rahasya pressure-cycle formalization](https://github.com/enuminous/papers/blob/main/RHC-001-EFMW-Rahasya-Pressure-Cycle-Formalization.md) · [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian) · [Cosmology](https://github.com/enuminous/Cosmology)

> **Interpretation:** Cross-links represent research dependencies and comparisons. The Standard Model and continuum gravity are inputs in current QST calculations; their emergence from Base888 and the physical status of the pressure cycle remain **UNRESOLVED**.
<!-- ENUMINOUS-RESEARCH-CHAIN:END -->
