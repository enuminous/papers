# UNITY-001 — Phase 4: Bounded Dynamical Consistency, Counterexamples, and Open Formal Obligations

**Research program:** Matthew Chenoweth Wright / Monolithic LLC  
**Date of original Phase 4 execution:** 9 November 2026  
**Publication:** 9 November 2026; retrospective report assembled from already committed source and CI evidence  
**Implementation:** AI-assisted technical work  
**Disposition:** **4 PASS · 3 FAIL · 5 UNRESOLVED** across 12 precisely scoped checks. **Zero EFMW-specific physical PASS.**  
**Evidence class:** Executed, bounded mathematical/software checks; *not* a physical experiment, full formal proof, or completed Theory of Everything.

> **Record-integrity note.** The Phase 4 code and CI workflow already existed; this report fills a documentation gap. No experiment, theorem, numerical result, test, or historical scorecard was rerun, retuned, replaced, or silently promoted to create this document. See the original [implementation commit](https://github.com/enuminous/papers/commit/268baa7d93e7b40483a3a01aa64076b71c51b581), [test-and-workflow commit](https://github.com/enuminous/papers/commit/93b839ca602dc8ab2582afe45fe22cef0fe3c7f8), and successful [GitHub Actions run 42626896120](https://github.com/enuminous/papers/actions/runs/42626896120).

## Executive finding

Phase 4 is **not missing**. The implementation survives at [`research/unity-001/phase-4/dynamics.py`](dynamics.py), its [29 adversarial software tests](test_dynamics.py) and [CI workflow](../../../.github/workflows/unity-001-phase4.yml). It checks a restricted set of dynamical identities and supplies explicit counterexamples to stronger claims.

Within finite four-coordinate **polynomial, flat-spacetime** examples, Maxwell field strength is gauge invariant, the Abelian Bianchi identity holds, and the electromagnetic stress-current relation is reproduced. A separately constructed **1+1-dimensional WITD** example satisfies a conditional local energy-accounting identity only when the necessary modulation and map-work terms are retained.

Three documented counterexamples block overbroad claims: (i) certain allowed C1 cubic scalar-potential parameters make the potential unbounded below; (ii) the unconstrained neutral-scalar current `j^ν = φ∂^νφ` need not be conserved; (iii) a single constant coefficient cannot globally identify the displayed WITD `I00` expression with its smooth-storage energy over all examined states.

These failures do **not** refute every constrained C1 or EFMW model. They demonstrate why stability, admissible currents, and complete stress-energy must be independently derived rather than assumed.

**Phase 4 does not establish a conserved informational gravitational stress, a complete coupled Einstein–Maxwell–scalar system, quantum consistency, or an EFMW-specific physical signal.**

## 1. Scope and frozen dependencies

The source-side guard in `dynamics.py` checks the Phase 1 source-lock manifest for **four repositories and 209 Git-tracked file entries**, ensures **eight Phase 2 scientific conflicts remain UNRESOLVED**, and confirms the Phase 3 reference-interface record `P3-REF-001` is present.

The checker additionally compares the recorded original Git metadata for:

- C1 candidate action: [`enuminous/EFMW-Lagrangian`, commit `83f9d2e`, `candidate/CANDIDATE.md`](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md), source blob `916e04935f50cbbf07ddcd81e7c71a02954b1c96`.
- WITD-002: [`enuminous/Information-Tensor`, commit `b02b048`, `research/witd-002/DERIVATION.md`](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/DERIVATION.md), source blob `d427b2f50bd8e577f6c206e076aa4121a612c6d9`.

The guard verifies recorded metadata relationships; it is **not** a fresh full source re-extraction, independent Lean replay, or proof that all historical equations are physically consistent.

Method: Python standard library `fractions.Fraction` and sparse polynomials in four coordinates `(t,x,y,z)`; Minkowski signature `(-+++)`; bounded integer polynomial powers; deterministic pseudorandom examples. The checks do not include curved-spacetime topology, boundary conditions, material dispersion, full PDE existence, or new observations.

## 2. Executed bounded consistency checks

### 2.1 Maxwell gauge invariance and Bianchi closure

Define the Abelian field-strength tensor from a polynomial 4-potential:

\[
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
\]

Under the gauge shift `A → A + dχ`, exact commuting polynomial partial derivatives leave `F` unchanged. The cyclic identity

\[
\partial_\lambda F_{\mu\nu}+\partial_\mu F_{\nu\lambda}+\partial_\nu F_{\lambda\mu}=0
\]

also follows in the modeled class. The implementation exercises **12 deterministic sampled potentials**, records **12 gauge checks**, and evaluates **768 Bianchi component checks** (12 × 64).

**Scope:** a conventional Abelian identity within smooth polynomial fields. It is not an original EFMW field equation or a new gauge-theory result.

### 2.2 Maxwell stress/current consistency

The implementation constructs `J^ν = ∂_μ F^{μν}` and tests, within its sign and index conventions, the electromagnetic stress/current identity

\[
\partial^\mu T_{\mu\nu}=F_{\nu\lambda}J^\lambda.
\]

It records **48 exact polynomial component checks** (12 × 4). A manufactured source-free plane-wave field has `J = 0` and vanishing stress divergence. A deliberately sourceful potential `A_x=t²` has nonzero current and nonzero electromagnetic stress divergence, while preserving the correct sourceful identity. Incorrect trace/sign alternatives are tested as negative controls.

**Scope:** the modeled flat-space Maxwell sector, not a coupled curved Einstein–Maxwell PDE proof or an identification of the EFMW informational source.

### 2.3 Conditional WITD local energy accounting

The WITD check constructs polynomial field/memory states, an explicit manufactured forcing function, time-dependent modulation `g(t)`, and a map `h(t,x)`. It tests a local energy-flux balance for a **1+1-dimensional smooth subcase** of the prior WITD-002 model.

The example satisfies its identity only when the **modulation work** and, for evolving `h`, the **map-work transfer term** are included. Dropping the required work terms produces an explicit residual, not a new conservation theorem.

**Scope:** a manufactured solution satisfying a constructed forced system, not an independently validated source-free trajectory, numerical convergence study, covariant conserved tensor, or physical energy measurement.

## 3. Three explicit counterexamples

### 3.1 Permitted C1 cubic scalar potential is not universally stable

Within an allowed restricted C1 parameter family, take three equal scalars `s`, positive quadratic masses and a cubic coupling to obtain

\[
U(s)=\frac32 s^2+s^3.
\]

As `s\to-\infty`, the negative cubic dominates and `U(s)\to-\infty`. The executable checks witness decreasing potential along `s=-2,-4,-8,-16`. The code also records the particular `U(-16)=-3712`.

**FAIL:** a universal assertion that all permitted C1 potential choices are globally bounded below. **Not claimed:** every restricted effective field theory or all parameter choices are unstable.

### 3.2 An unconstrained neutral-scalar gauge current need not conserve

For `φ=t`, the proposed neutral-scalar current

\[
j^\nu=\phi\,\partial^\nu\phi
\]

has exact divergence `∂_ν j^ν = -1` in the chosen metric signature. A Maxwell-like antisymmetric-field equation imposes `∂_ν J^ν=0`, so this current is **not unconditionally admissible** as such a source without further constraints or additional equations.

**FAIL:** automatic conservation for an arbitrary unconstrained `φ∂φ` current. **Not claimed:** a no-go theorem against every constrained or properly coupled scalar current.

### 3.3 A constant WITD storage-tensor coefficient is insufficient

The existing WITD storage comparison supplies two elementary witnesses. In one homogeneous choice with `q=m=a` and positive `μ²`, equality forces the proposed coefficient `β=0`. In a second state with `q=0, m=a`, the resulting energy difference at `β=0` is `g a²/2`, nonzero when `g>0`. At the code's example parameters it is **3/2**.

**FAIL:** one state-independent `β` makes the displayed `I00` universally equal to smooth storage energy across those states. **Not claimed:** that no alternative energy tensor or improved model could satisfy a different, well-posed energy accounting condition.

## 4. Exact 12-finding evidence ledger

| Finding ID | Status | Bounded interpretation |
|---|---|---|
| `P4-MAX-GAUGE` | **PASS** | `F=dA` invariant under polynomial gauge shifts |
| `P4-MAX-BIANCHI` | **PASS** | Abelian cyclic Bianchi identity for sampled exact fields |
| `P4-MAX-STRESS` | **PASS** | Flat Maxwell stress/current identity and sourceful/vacuum controls |
| `P4-WITD-ENERGY` | **PASS** | Conditional 1+1 manufactured WITD energy balance including work terms |
| `P4-C1-UNBOUNDED` | **FAIL** | Universal C1 global potential boundedness refuted for permitted cubic ray |
| `P4-C1-NEUTRAL-CURRENT` | **FAIL** | Arbitrary neutral-scalar `φ∂φ` source need not be divergence free |
| `P4-WITD-STORAGE-TENSOR` | **FAIL** | One constant `β` cannot represent WITD smooth storage energy for all examined states |
| `P4-FULL-C1-METRIC` | **UNRESOLVED** | Full coupled curved metric/gauge/scalar variation and principal symbol |
| `P4-HISTORICAL-EFMW-STRESS` | **UNRESOLVED** | Full conserved original-EFMW informational stress not derived |
| `P4-FULL-WITD-TENSOR` | **UNRESOLVED** | Covariant total stress, reservoir momentum, physical calibration |
| `P4-QUANTUM-CAUSAL` | **UNRESOLVED** | Unitarity, microcausality, hyperbolicity, EFT cutoff |
| `P4-PHYSICAL-EVIDENCE` | **UNRESOLVED** | External measured-data test, independent physics replication, physical unity |

**Denominator:** 12 findings = **4 PASS + 3 FAIL + 5 UNRESOLVED**; **0 EFMW-specific physical PASS**. These are **finding counts, not a probability of correctness, a fraction of physics completed, or a measure of physical validity.**

## 5. Execution and replay record

Original commits:

1. [`268baa7d93e7b40483a3a01aa64076b71c51b581`](https://github.com/enuminous/papers/commit/268baa7d93e7b40483a3a01aa64076b71c51b581) — initial exact bounded dynamics implementation.
2. [`93b839ca602dc8ab2582afe45fe22cef0fe3c7f8`](https://github.com/enuminous/papers/commit/93b839ca602dc8ab2582afe45fe22cef0fe3c7f8) — 29 adversarial `unittest` methods and GitHub Actions workflow.

[CI run 42626896120](https://github.com/enuminous/papers/actions/runs/42626896120) completed **successfully** on 9 November 2026 for commit `93b839ca6`. Its workflow runs the 29 test methods and recomputes and uploads a machine-readable bounded findings manifest.

For a reader to perform a **new independent replay**, not an action performed for this report, use:

```bash
git clone https://github.com/enuminous/papers.git
cd papers
python3 -m unittest discover -s research/unity-001/phase-4 -p 'test_*.py' -v
python3 research/unity-001/phase-4/dynamics.py --out research/unity-001/phase-4/build/manifest.json
```

In a new replay, pin the repository at the relevant source/testing commit (or otherwise record the exact tested revision) and compare `counts`, `findings`, source-guard fields and output to the historical CI artifact. The upstream source files and their metadata are pinned in [Phase 1](../phase-1/sources.lock.json); the later publication of this report **does not itself constitute an independent reproduction**.

## 6. Interpretation for subsequent phases

The Phase 3 source-only ambiguity for `T + κI` remains open; Phase 2's eight conflicts are not marked resolved by these identities. Conventional Maxwell identities cannot demonstrate an independent informational gravitational source. The 1+1 WITD manufactured balance does not derive a conserved full spacetime stress tensor or close its energy-storage mismatch. Phase 4 counterexamples actively *limit* admissible future model claims.

The [Phase 5 synthetic identifiability screen](../phase-5/PHASE5_REPORT.md) already references the Phase 4 code. It concludes that an unconstrained co-located ordinary-mass profile exactly confounds the proposed gravitational signal and that **confirmatory physical prediction is not ready**. Phase 4 should therefore be reported **between** Phases 3 and 5 in the Observatory chronology, without changing the Phase 5 findings or the original MOC-001 baseline.

## 7. Outstanding work

- Derive a complete, source-faithful `I_{μν}` with independently stated dimensions, covariance, energy/momentum exchange, and matter-source normalization.
- Specify constrained stable C1 parameter regions and admissible conserved currents; do not generalize from selected healthy sectors to the unrestricted model.
- Perform exact curved metric/gauge/scalar variation and address field equations, initial/boundary conditions, constraint propagation and causal properties.
- If Lean certification is claimed, pin the exact toolchain and theorem statements and publish kernel replay, axioms and any nonmechanized bridges. **No such Phase 4 Lean kernel replay was executed.**
- Require separately measured conventional-matter constraints and prospective, independently reviewed physical experimental protocols before treating a residual as EFMW-specific.

**Final disposition:** **BOUNDED MATHEMATICAL CONSISTENCY IN SELECTED SUBMODELS; THREE EXPLICIT COUNTEREXAMPLES; PHYSICAL UNITY AND NEW EFMW COUPLING UNRESOLVED.**

---

*Publication is an archival documentation repair. It does not alter the underlying code, original CI results, Phase 1–3 datasets, Phase 5 simulation, MOC-001 scores, or any external scientific record.*
