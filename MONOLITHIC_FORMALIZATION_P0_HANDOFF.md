# Monolithic 102 Formalization — P0 Handoff Package

**Status:** ready for repository implementation and independent review  
**Scope:** reproducible Lean companion; equation-level provenance; ME-036/037 repair; ME-028 external replication  
**Boundary:** this package does not claim that the Monolithic 102, EFMW's physical interpretations, or ME-102 are proved.

## Release gate

The P0 release is complete only when all of the following are true:

1. A clean clone of `Monlithic_EFMW_102_Lean4` completes `lake build` using a fixed Lean toolchain and committed dependency manifest.
2. CI executes that clean build on every protected-branch change.
3. Every ME-001–ME-102 entry has a machine-readable crosswalk row containing its canonical-source hash, formal status, assumptions, dependencies, and exact Lean target(s).
4. ME-036 and ME-037 have an explicit typed operator model and a minimal proved result.
5. The ME-028 preregistration is committed and tagged before any external evaluation data are scored.
6. ME-102 remains `ACCEPTANCE_GATE_UNMET` unless the ME-028 protocol receives independent external replication.

## 1. Reproducible Lean build

### Required repository layout

```text
Monolithic102/
  Schema.lean
  Catalog.lean
  ME001.lean ... ME102.lean
  Repairs/
    ME036_ME037.lean
  Tests/
    CatalogCoverage.lean
lakefile.lean
lake-manifest.json
lean-toolchain
.github/workflows/lean.yml
equation-crosswalk.json
```

### Frozen build contract

- `lean-toolchain` must name an exact Lean release, not `stable`.
- `lake-manifest.json` must be committed and pin Mathlib to a compatible exact revision.
- `lakefile.lean` must contain no moving Git revision.
- `lake build` must build every catalog module and all tests.
- No tracked Lean file may contain `sorry`, `admit`, `axiom`, or an unreviewed `opaque` placeholder.

### CI acceptance workflow

The CI job must perform only this independent sequence:

```bash
lake update
git diff --exit-code lake-manifest.json
lake build
rg -n "\\b(sorry|admit|axiom)\\b" Monolithic102 && exit 1 || true
lake env lean Monolithic102/Tests/CatalogCoverage.lean
```

The build log, exact commit SHA, Lean version, Mathlib revision, and artifact checksum must be retained with the release.

## 2. Equation crosswalk schema

Create `equation-crosswalk.json` with exactly 102 records, one for each `ME-001` through `ME-102`.

```json
{
  "id": "ME-036",
  "canonical_title": "Coupled thinking-puddle equation for system field S",
  "canonical_source_path": "equations/036.md",
  "canonical_source_sha256": "REQUIRED",
  "family": "F05_coupled_cognitive_fields",
  "status": "REVISION_REQUIRED",
  "claim_class": "conditional_derivation",
  "lean_module": "Monolithic102.Repairs.ME036_ME037",
  "lean_targets": ["ME036.crossGradientCollapse", "ME036.repairedOperatorWellTyped"],
  "assumptions": ["REQUIRED: typed state spaces", "REQUIRED: operator choice", "REQUIRED: boundary and initial conditions"],
  "upstream_dependencies": [],
  "downstream_dependencies": ["ME-037"],
  "empirical_status": "not_tested",
  "reviewer_note": "The symmetric cross-gradient form identifies only an effective coefficient."
}
```

Allowed `status` values: `FORMALIZED`, `PARTIAL_FORMAL`, `REVISION_REQUIRED`, `NEEDS_SPECIFICATION`, `SOURCE_ONLY`, `ACCEPTANCE_GATE_UNMET`.

The current source matrix is the authoritative starting record for titles, families, claim classes, and reviewer notes. It must be converted mechanically into this schema rather than rewritten from memory.

## 3. ME-036/037 repair specification

### Frozen issue

In the symmetric paired cross-gradient model, the two nominal cross-gradient coefficients collapse into one effective coefficient. They are not separately identifiable. Therefore neither directional/cognitive interpretation nor downstream PDE claim may rely on their being independently measured.

### Required choice (one only)

**Option A — symmetric repair (default):** Replace the two coefficients with one coefficient `κ` and state that the coupling is symmetric.

**Option B — asymmetric repair:** Define distinct typed operators `K_SO : OSpace → SSpace` and `K_OS : SSpace → OSpace`, state their domains/codomains, and prove that they are not definitionally the same operator. Do not claim asymmetry from notation alone.

### Minimum formal theorem sequence

1. Define `SSpace`, `OSpace`, the pairing, gradients/operators, parameters, and forcing terms.
2. Prove the repaired operator is well typed.
3. Prove the original symmetric formulation reduces to one effective coefficient.
4. Add one bounded mathematical result appropriate to the stated model: an energy identity/estimate, or local well-posedness under explicitly declared regularity and boundary conditions.

The theorem may establish only the mathematics of the specified operator. It must not assert that `S` and `O` are physical or cognitive fields without separate empirical support.

## 4. ME-028 external replication preregistration

### Hypothesis

On one independently sourced streaming or control dataset, the frozen EFMW recurrence produces earlier warnings than predeclared conventional monitors at matched false-positive budgets.

### Frozen monitor

\[
r_t=y_t-(0.82y_{t-1}+u_t),\qquad
m_t=0.97m_{t-1}+0.03r_t,\qquad
C_t=|m_t|.
\]

No recurrence coefficient, feature transform, event definition, or threshold-selection procedure may change after the dataset split is frozen.

### Protocol fields that must be committed before scoring

- Dataset owner/source, acquisition date, license/permission, and cryptographic file hashes.
- Prediction target, onset definition, observation cadence, exclusions, and missing-data rule.
- Development, calibration, held-out test, and independently held-out replication partitions.
- Alarm threshold-selection method, false-positive budget, lockout/refractory rule, and reporting window.
- Baselines: residual EWMA, RMS-EWMA, and CUSUM, each tuned only on the declared calibration partition.
- Primary metric: median paired warning lead at matched false-positive budget.
- Secondary metrics: false-positive rate, detection rate, latency, memory, CPU time/cycles where available, and energy where available.
- Statistical analysis: paired confidence interval, exact test/bootstrapping method, treatment of failed or absent alarms, and complete per-episode table.
- Failure criterion: failure to exceed the predeclared lead criterion at the matched false-positive budget, or any protocol deviation that changes the frozen monitor or target definition.

### Gate condition

ME-102 is not a standalone proof target. It changes status only after an external team executes this protocol from the preregistered artifact, publishes outputs and environment details, and satisfies the frozen success criterion without material deviation.

## 5. Required release artifacts

1. `P0_RELEASE_MANIFEST.json` — repository SHA, toolchain, Mathlib revision, source hashes, and build-output hashes.
2. `equation-crosswalk.json` — 102 exact records.
3. `ME036_ME037_REPAIR.md` — operator choice, assumptions, theorem statements, and Lean links.
4. `ME028_PREREGISTRATION.md` — the complete immutable protocol above, dataset-specific fields filled in before execution.
5. `BUILD_LOG.txt` — clean-clone command transcript.
6. CI run URL and release tag, e.g. `formalization-p0.1`.

## Reviewer-facing claim after P0

> The Monolithic 102 Lean companion is reproducibly buildable and provides equation-level provenance. The ME-036/037 cross-gradient defect has been made explicit and repaired at the operator level. A separate ME-028 replication protocol has been preregistered. These achievements formalize specified mathematical statements and experimental procedures; they do not by themselves validate EFMW's physical interpretations or prove the full 102-equation corpus.

