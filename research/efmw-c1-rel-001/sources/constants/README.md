# EFMW Constants Problem

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/EFMW-Constants-Problem) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#fundamental-physics-cosmology-and-quantum-geometry) · [Published site](https://enuminous.github.io/EFMW-Constants-Problem/) · [Web application](index.html)

<details open>
<summary><strong>On this page</strong></summary>

- [Core thesis](#core-thesis)
- [Contents](#contents)
- [Build](#build)


</details>

**Related repositories:** [EFMW-108-Minute-Tests](https://github.com/enuminous/EFMW-108-Minute-Tests) · [EFMW-Neutron-Star-Glitch-Resonance](https://github.com/enuminous/EFMW-Neutron-Star-Glitch-Resonance) · [Ligo_EFMW_Search](https://github.com/enuminous/Ligo_EFMW_Search) · [Oroboros](https://github.com/enuminous/Oroboros) · [EFMW](https://github.com/enuminous/EFMW) · [papers](https://github.com/enuminous/papers)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


A corrected successor to the 2025 essay **One Paper to Join Them All**.

This repository separates established identities from the open EFMW generative hypothesis.

## Core thesis

The meaningful unification target is not merely to show that physical constants are related. Standard physics already does that. The stronger target is to reduce the number of independent **dimensionless** inputs.

## Contents

- `index.html` — full public paper
- `DEPENDENCY_MAP.md` — identities, inputs, conventions, targets
- `CLAIMS_BOUNDARY.md` — scientific-status boundary
- `EFMWConstants/Core.lean` — Lean 4 formalization
- `EFMWConstants/Main.lean` — export surface
- `verify_constants.py` — numerical sanity checks
- `.github/workflows/lean.yml` — CI

## Build

```bash
lake update
lake build
python verify_constants.py
```

Lean proves consequences of the stated definitions and assumptions. It does not prove that EFMW derives any measured physical constant. In particular, the integer-ratio toy model is only an interface example; independent prespecification of parameters is an empirical/provenance condition outside Lean's object-level proof.

The numerical verifier uses the NIST 2022 CODATA recommended values, currently the latest available CODATA adjustment.
