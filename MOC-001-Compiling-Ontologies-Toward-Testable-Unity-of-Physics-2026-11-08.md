# MOC-001 — Compiling Ontologies Toward a Testable Unity of Physics

**Author:** Matthew Chenoweth Wright, Monolithic LLC  
**Preparation:** AI-assisted mathematical and software drafting, reviewed as an independent research working paper  
**Date:** 8 November 2026  
**Status:** Architecture and reproducible *structural* prototype; **not** a completed physical theory, independent physics verification, or peer-reviewed result.

**Companion:** [Unity Appendix — compatibility, correspondence, and empirical closure](research/moc-001/UNITY_APPENDIX.md)  
**Reproduction notes and navigation:** [MOC-001 research companion](research/moc-001/README.md)

## Abstract

The ambition of unifying physics requires more than juxtaposing equations from general relativity, quantum field theory, statistical mechanics, geometry, information theory, and proposed novel models. The equations must carry exact mathematical semantics, declared approximations, compatible observables, reproducible provenance, and falsifiable relationships. We introduce MOC-001, a *Master Ontology Compiler* scaffold that represents heterogeneous physical ontologies and candidate claims as a typed, evidence-scoped dependency graph. A first executable Python implementation checks referential integrity, dependency cycles, and a restricted form of SI dimensional consistency; it generates a navigable equation manifest, structural gate report, and read-only observatory. The original prototype contains 22 ontology sectors, 22 equation records (including unimported placeholders), 17 quantities, 12 source entries, four proposed interfaces, and nine explicit research obligations. On 8 November 2026, 16 local Python tests passed. The compiler emitted five bounded structural PASS findings, zero structural FAIL findings, and 35 UNRESOLVED findings. These are software and bookkeeping results, **not** evidence of successful physical unification. A separately linked Unity Appendix states a stronger criterion for legitimate cross-theory correspondence, dynamical compatibility, and empirical discriminability.

**Keywords:** ontology compilation; foundations of physics; reproducible science; formal methods; mathematical physics; model comparison; EFMW; dimensional analysis; evidence provenance.

## 1. The problem: compilation is not unification

Physics is described through multiple partially overlapping mathematical languages. A metric theory of spacetime, a gauge-field description of particle interactions, an effective many-body theory, and a stochastic measurement model may all be useful without being interchangeable or mutually fundamental. A plausible route toward total physical unity is to compile these descriptions into a common *auditable framework* that records both legitimate reductions and outstanding incompatibilities.

The phrase "all ontologies" must not mean all proposed premises are simultaneously true. We use *ontology* operationally to mean a domain-specific mathematical model with specified entities, state space, laws, measurements, and limitations. Every ontological import is labeled as established reference physics, an independently supported result, a research candidate, a simulation fixture, or an unimported placeholder. Unknown or conflicting assumptions are preserved, not automatically resolved.

The central research question is therefore not "Can every equation be placed in one file?" but:

> Can a precisely defined common framework produce mathematically compatible sector descriptions, recover independently successful physical limits, and generate distinctive, risky predictions that survive independent measurement?

The necessary compatibility and unity criteria are given in the [Unity Appendix](research/moc-001/UNITY_APPENDIX.md).

## 2. Typed ontologies and evidence-bearing equations

For an ontology \(\mathcal O_i\), a proposed formal contract is

\[
\mathcal O_i=(X_i,\mathscr E_i,\Theta_i,\mathscr C_i,\mathscr A_i,\mathscr P_i),
\]

where \(X_i\) is a declared state/domain representation, \(\mathscr E_i\) its equations or evolution laws, \(\Theta_i\) its parameters and conventions, \(\mathscr C_i\) constraints and boundary conditions, \(\mathscr A_i\) observable or measurement maps, and \(\mathscr P_i\) provenance and evidence. This is a design schema, not a theorem that a common \(X_i\) exists across all sectors.

An equation record carries at minimum: a stable ID, original source path, version/commit or explicit unpinned flag, original notation, normalized expression where possible, mathematical domain, units, premises, boundary conditions, dependencies, known conflicts, verification method, and claim status. Original statements and normalized translations are different records or linked representations; a compiler must not silently "repair" a source.

A useful master-density *organizing ansatz* is

\[
\mathcal L_{\mathrm{organizational}}
=\mathcal L_{\mathrm{GR}}
+\mathcal L_{\mathrm{SM}}
+\mathcal L_{\mathrm{interactions}}
+\mathcal L_{\mathrm{candidate}}.
\]

This equation only describes intended bookkeeping. It does **not** assert that all terms already share a compatible measure, tensor structure, renormalization prescription, variational principle, or physical ontology. If a suitable action exists, equations may be compared with variational conditions such as \(\delta S/\delta\Phi_i=0\); constraints, stochastic models, and history-dependent theories may require a different representation. Simply summing classical gravity and quantum matter does not solve quantum gravity.

## 3. Compiler structure

MOC-001 has eight layers:

1. **Source capsule.** Immutable repository commit, file bytes hash, permissions, conventions, exact extraction point, and build or measurement receipt. An unpinned README link is inspection, not a frozen import.
2. **Ontology registry.** Typed declarations of fields, state/domain, symmetries, observables, equations, assumptions, and limits.
3. **Equation registry.** Source-faithful LaTeX plus an optional restricted expression abstract-syntax tree for static checks.
4. **Interface registry.** Explicit proposed maps or couplings between sectors; a missing map definition is UNRESOLVED.
5. **Dependency and conflict graph.** Links, required premises, cycles, conditional theorems, alternative candidates, and unresolved clashes.
6. **Verification engines.** Presently implemented: reference integrity and basic SI dimensions. Planned: tensor variance, gauge transformation, covariance, conservation, independent variation, formal replay, and numerical comparators.
7. **Evidence ledger.** Separate PASS, FAIL, and UNRESOLVED findings, each tied to a named gate and reproducible scope.
8. **Observatory and export.** A browser-readable manifest, equation index, Graphviz dependency graph, LaTeX projection, and auditable report.

The bounded dimension engine represents SI exponents as \((M,L,T,I,\Theta,N,J)\). It can detect some incompatible sums and equalities but does not verify field equations, tensor identities, coordinate independence, or empirical truth.

## 4. Pilot inputs and source boundaries

The initial scaffold includes conventional reference examples: the special-relativistic mass-shell relation and a classical Einstein-equation form. It includes an organizational master-density equation and an explicitly *toy*, dimensionless memory example. These four equations receive only dimensional checking. The remaining equation slots are placeholders or candidate imports, not a secretly completed corpus.

On 8 November 2026, source READMEs were inspected for:

- [Geometry](https://github.com/enuminous/Geometry): bounded component proofs and conditional conservation/source-split statements; the G3 question of observing a nonzero informational coupling remains UNRESOLVED.
- [Information-Tensor](https://github.com/enuminous/Information-Tensor): a specified simulation and semantic engine; its tensor and memory interpretation must not be conflated with established physical laws. See also [WITD-002 energy accounting](WITD-002-Where-Does-the-Memorys-Energy-Go-2026-11-05.md).
- [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian): frozen C1 candidate and reported audit of 585 source statements; source-sign discrepancies, unmatched gauge currents, and gravity/stress identifications remain open.
- [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction): a notation-level restatement of the established classical Standard Model; the proposed 39-strata extension is not thereby established.

Additional links in the MOC-001 source registry are queued leads, **not inspected or ingested sources**. These first four README pointers were not yet frozen to immutable commits within the compiler; full authoritative equation imports and independent upstream Lean replays were **not** performed.

This work complements but does not supersede the earlier [TOE-001 classical effective-field-theory candidate](TOE-001-Unified-Action-and-Correspondence-Test.md). In particular, its conventional two-scalar model does not recover the original EFMW equations or supply a uniquely EFMW physical signature.

## 5. Executed local scaffold checks

The 8 November 2026 local rerun used Python's standard-library test runner and compiler:

~~~bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m moc compile --out build
~~~

| Observation | Local result | Scope |
|---|---:|---|
| Automated tests | 16/16 passed | Compiler unit, invalid-input, and adversarial regression tests |
| PASS gate findings | 5 | Four dimension-compatible example expressions and one static registry pass |
| FAIL gate findings | 0 | No failure in the executed bounded checks; **not** a global correctness result |
| UNRESOLVED gate findings | 35 | Missing equation expressions, interface mappings, source pins, and research obligations |
| Lean 4 replay | Not executed | Proof claims are not certified by this paper |
| Independent physical experiment | None | No physical novelty or mechanism established |

The test suite includes rejection of malformed exponents, incompatible dimensions, unknown symbols, duplicate IDs, missing dependencies, cycles, and unjustified evidential promotion. An absence of static FAIL findings must not be promoted to a physical PASS.

For traceability, the locally built ZIP was named `Master-Ontology-Compiler-MOC-001-2026-11-08.zip` with SHA-256 `77509faffce09dcbe23d31c4cb956d5e335fbd6c113edfed9cae7e22cbadeb7e`. This digest identifies the session artifact; **the code ZIP has not been published to this repository**. The generated source registry and reports remain in the separately prepared scaffold, not falsely described as independently retrievable GitHub assets.

## 6. A stronger criterion: unity as a correspondence problem

A successful unified physical framework must define explicit restricted-domain maps between candidate unified states and the descriptions already tested by experiment. Mere agreement on terminology, equations with matching units, or a visually appealing diagram is not enough. The maps must make predictions and dynamics commute to quantified accuracy, preserve appropriate symmetry and conservation properties, and explain when a reduction is only approximate. Observable novelty must then survive comparison with well-established and conventional alternative models.

The [Unity Appendix](research/moc-001/UNITY_APPENDIX.md) develops this criterion using restriction maps \(r_i\), evolution operators \(T_{\rm U}^t,T_i^t\), explicit tolerances, and observable prediction maps. It lists the initial four unfilled interfaces: GR/Standard Model, EFMW/gravity, topology/fields, and observers/measurement.

## 7. Falsification and acceptance gates

A claim of physical unification requires, at minimum:

- **G0:** deterministic structural compilation with recorded test outputs (bounded local PASS).
- **G1:** immutable source/notation provenance and third-party replay (UNRESOLVED).
- **G2:** exact GR and Standard Model correspondence in stated limits, including compatible conventions and quantum domain boundaries (UNRESOLVED).
- **G3:** full candidate EFMW source-equation import, explicit source-sign adjudication, and independent action/field-equation comparison (UNRESOLVED).
- **G4:** mathematically specified cross-ontology maps that preserve the claimed structures (UNRESOLVED).
- **G5:** exact conditional Lean proofs and independent numerical reproductions, including negative controls (UNRESOLVED).
- **G6:** prospective, operationally measurable prediction distinct from established physics and matched non-EFMW explanations (UNRESOLVED).
- **G7:** blinded or genuinely held-out external evaluation (UNRESOLVED).
- **G8:** independent physical replication, or a documented failed prediction (UNRESOLVED).

Crucial open problems include an EFMW-specific discriminating observable (the \(\kappa_I=0\) comparison), informational energy accounting, gauge-current derivation, source scalar-sign mismatches, stress-energy compatibility, possible quantum-gravity completion, and the proposed 39-strata Standard Model relationship. A conventional model explaining a candidate effect is a valid *negative* result for a novelty claim.

## 8. Conclusion

MOC-001 establishes a **method for refusing premature unity**: it can inventory incompatible or incomplete theories without erasing the gaps. The scientific promise is not the number of ontologies loaded, but whether each attempted bridge can be stated, checked, contested, reduced to familiar physics, and confronted with measurement. The pilot reports structural progress while retaining the outstanding theoretical and empirical work as explicit obligations.

**Unity status on 8 November 2026: UNRESOLVED.** The linked [Unity Appendix](research/moc-001/UNITY_APPENDIX.md) defines the target and a failure-aware research path.

## References and project links

1. [MOC-001 Unity Appendix](research/moc-001/UNITY_APPENDIX.md) — formal criteria, interfaces, and failure modes.
2. [MOC-001 research companion](research/moc-001/README.md) — reproduction status and source references.
3. [Geometry](https://github.com/enuminous/Geometry), [Information-Tensor](https://github.com/enuminous/Information-Tensor), [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian), [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction).
4. [TOE-001 — unified action and correspondence test](TOE-001-Unified-Action-and-Correspondence-Test.md).
5. [EFMW physical-validation roadmap](EFMW-Physical-Validation-Research-Roadmap-2026-11-03.md).
6. [WITD-002 — where does the memory's energy go?](WITD-002-Where-Does-the-Memorys-Energy-Go-2026-11-05.md).

*This working paper is a research proposal and software-methods account, not a claim of discovery, independent peer review, completed ontology compilation, or experimentally established unification.*
