# Physlib Maxwell: fixed-scope Zoo audit plan

Audit ID: PHYSLIB-MAXWELL-ZOO-2026-11-16. Source review preceded this local execution freeze. This is not a blind study, independent preregistration, or externally commissioned audit.

## Target and pins

- Physlib commit `892e8fcba8af5ec691ca7a8ad82ee5dbe3180b17`.
- Root module: `Physlib.Electromagnetism.ThreeDimension.MaxwellEquations`.
- Roots: `Electromagnetism.ThreeDimension.gaussLawElectric`, `gaussLawMagnetic`, `ampereLaw`, `faradayLaw`.
- Trace their imports, theorem dependencies, assumptions, and physical interpretation. Repository-wide source inventory is supplementary; this is not a semantic audit of every Physlib theorem.
- Required Lean: `leanprover/lean4:v4.35.0`; dependency revisions from the unchanged `lake-manifest.json`.
- Zoo core/formalized extensions: `enuminous/Monolithic-Zoo-Lean4@8b22841ffcf44e41451e7696335bf6a6ae8f222e`.
- Executable selected kernels: `enuminous/EFMW_Post156_Zoo_Audit@fd4ac30ffdbb44c78e7ea69e2424beaa9f3fdb93`.
- PEGASUS standalone extension: `enuminous/Pegasus@41d57615f16c43ea8858e35cd1250d44c3c7df97`.
- Account for all 46 registered core animals, five extensions recorded in `extension-sources.json`, PEGASUS, and the previously named HUMMINGBIRD. HUMMINGBIRD source/contract was not located by exact repository lookup and scoped repository search; mark UNRESOLVED rather than inventing an operation. No global numbering is inferred for extensions.

## Evidence rules

PASS means the stated bounded check passed. FAIL requires a reproducible contradiction or violated declared criterion. UNRESOLVED means an applicable question lacks required inputs, executable bridge, or completed replay. NOT_APPLICABLE means the operation's domain is absent from this target; it is not a pass. Test-fixture success is a tool check, not evidence for Maxwell or EFMW. Native Zoo outputs retain their original labels and are separate from audit verdicts.

## Frozen checks and criteria

1. Verify target and dependency pins and unchanged tracked source before/after. PASS requires exact matches.
2. Build the root module with pinned Lean, then independently re-elaborate its source with `lake env lean`. Cached upstream dependencies are allowed and must be disclosed. A failed command is a replay failure, with attribution to code/environment only if established. Never substitute hosted CI for local replay.
3. Print all four elaborated types and transitive axioms. Allowed foundational axioms: `propext`, `Classical.choice`, `Quot.sound`. Any other axiom is a failure of this strict audit policy, not automatically a proof of mathematical falsity. Record direct references and the Physlib portion of each declaration closure.
4. Validate the axiom checker with a valid theorem plus quarantined public-axiom, private-axiom, placeholder, and native-computation controls. All forbidden cases must be detected for the intended reason. A false arithmetic proposition without extra axioms must fail elaboration. These are harness controls, never target defects or proposed upstream code.
5. Inspect physical/mathematical contracts: fields from potentials, source/current definitions, positivity and speed-of-light convention, variational-gradient definition, smoothness, derivative identities, signs and constants. Identify missing hypotheses or mismatches against the module's own documented claims. Do not require integral/boundary/material results the module explicitly excludes.
6. Assess anti-circularity and vacuity. Trace `IsExtrema` to the independently defined action gradient. A stationary-action hypothesis is an expected conditional premise, not circularity by itself. Seek a zero-potential/zero-current witness if practical; inability to construct it locally remains an open audit obligation, not evidence of inconsistency.
7. Execute existing Python fixture suites for all selected core adapters and PEGASUS. Preserve outputs and counts. Formal Zoo replay is supplemental if its separate pinned toolchain can be installed. No inference from numerical fixture agreement to full Lean/Python equivalence.
8. Account for each fixed animal's purpose, inputs, transformation, output, applicability and criterion. Never supply invented scores, fabricated experiments, or arbitrary EFMW equation mappings.
9. ELEPHANT: use the actual first-parent Git history of changes to the root source, oldest-to-newest IDs, the pinned version active for this audit, predecessors superseded, and fuel equal to history length plus one. PASS requires lineage terminates at origin, covers all supplied records in reverse order, and exactly one active pinned record. This is selected file-version provenance, not complete Git-DAG ancestry or proof validity.
10. CIRCUS: feed an evidence ledger for this audit. Preserve that no externally independent validation of this audit has occurred. Its native N/A/FAIL/PASS concerns declared report gates, not Maxwell's mathematical truth.
11. PEGASUS: expose the three-dimensional/covariant bridge as an explicit obligation graph. Its v0.1 registry has no Lean proof checker; run the fixed obligation operation and retain UNRESOLVED. A manually supplied PASS cannot certify the bridge. Lean replay is reported separately.

## Interpretation and next-test rules

No aggregate probability, universal coherence score, or count of animal passes is a proof of physics. Formal mathematical correctness, correspondence to intended classical physics, and empirical confirmation are separate. Standard Maxwell identities are not an EFMW-specific prediction. An EFMW claim needs a precise additional proposition and independently testable difference from the standard model.

All amendments, failed runs and diagnostic controls remain in the bundle. Do not modify or publish upstream source. No external messages are authorized by this audit request.
