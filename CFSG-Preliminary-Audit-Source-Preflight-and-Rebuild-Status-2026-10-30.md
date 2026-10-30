# Preliminary Audit of the CFSG Lean Formalization: Source Preflight and Outstanding Rebuild Obligations

**Matthew Chenoweth Wright** · Monolithic LLC / eNuminous

30 October 2026 · Preliminary technical report · Version 0.1  
**Audit:** CFSG-ZOO-001, source-preflight checkpoint  
**Evidence cutoff:** Repository and GitHub Actions records inspected on 30 October 2026  
**Overall status:** **SOURCE PREFLIGHT PASSED; INDEPENDENT FULL REBUILD PENDING**

## Abstract

This report documents the preliminary independent audit of the Axiom Math-originated Classification of Finite Simple Groups (CFSG) formalization preserved in `enuminous/CFSG`. The audit has identified a frozen mathematical source, traced the visible theorem entry points, and established a working source-provenance preflight. A GitHub Actions run on 28 October records fourteen passing source checks, five passing tests of an axiom-output parser, and successful shell-syntax validation of the proposed rebuild script. Those results concern the verification setup and selected source properties. They do not establish that the complete Lean project has been independently rebuilt or that the final theorems have the declared axiom dependencies. Actual theorem axiom reports, a complete transitive import and certificate inventory, and independent statement-alignment review remain outstanding. The earlier forty-six-operation Zoo intake remains entirely unresolved because those operations were not executed. The present contribution is a documented, inspectable audit checkpoint with explicit acceptance conditions for the next stage; it is neither a new proof of CFSG nor a refutation of the submitted formalization.

**Keywords:** classification of finite simple groups; Lean 4; formal verification; reproducibility; provenance; dependency audit; Monolithic Zoo.

## 1. Scope, attribution, and method

The original mathematical formalization belongs to the authors and contributors credited by the Axiom Math project and its `formalization.yaml`, including the underlying Mathlib, TauCeti, and related formalization projects. Monolithic's contribution at this stage consists of source inspection, evidence classification, and verification instrumentation. No CFSG theorem is attributed to EFMW or to the Zoo. The upstream metadata describes its review as self-assessed; this report does not convert that declaration into external peer review. [1]

The October 30 review read the fork's current files and commit history, inspected its branch and open-pull-request listings, and examined the latest successful Actions job and its logs. It also compared the tested revision with the current head. No complete Lean build, new axiom-probe execution, or Zoo operation was performed while preparing this report. The test counts below are verified observations of the October 28 hosted record, not fresh local test results.

Three kinds of evidence are kept separate:

- **Direct observations:** repository contents, commit differences, workflow steps, and recorded log results.
- **Project declarations:** claims such as zero proof holes and a specified permitted-axiom list.
- **Pending obligations:** evidence that requires compilation, recursive dependency analysis, or independent semantic review.

A missing result is classified as **UNRESOLVED**, rather than treated as either a mathematical failure or a successful verification.

## 2. Frozen source and audited revisions

| Item | Recorded identity |
|---|---|
| Upstream origin | `AxiomMath/CFSG` |
| Audit fork | `enuminous/CFSG` |
| Frozen original mathematical source | `69cb972f587a3ecc035e092253167ff2e303c962` |
| Fork head inspected on October 30 | `df6242e23368e81f4be97dc02998e53ad2d41224` |
| Revision of the latest successful preflight | `e46ef02c378dbe1665566bd77a24037fb46ee840` |
| Lean toolchain pin | `leanprover/lean4:v4.35.0-rc3` |
| Mathlib revision | `b63f6e8a68d220e3b3bc4f3792bb53650d375f24` |
| TauCeti revision | `6e0c6acab5f4c6f42e5f5bab9bd5e4e84f74c380` |

The original source revision and the fork's audit revision serve different purposes: the first identifies the mathematical target, while the second includes the added inspection scripts and documentation. The latest passing preflight establishes ancestry from the original revision and unchanged protected proof paths at its tested commit. [2, 3]

The inspected head is two commits beyond that passing run. Their combined changes affect only `README.md` and the added `audit/EFMW_CFSG_OPTIMIZATION_NOTE.md`. The comparison therefore supplies evidence that those subsequent commits did not alter the protected proof files or the preflight implementation. It is not a separate CI execution at the head revision. [4]

At the cutoff, `main` was the only listed branch, no pull requests were open, and its last commit was dated October 28. The complete returned Actions listing contained eight runs, all for source preflight: three earlier failures followed by five successes. It contained no full-rebuild run. These are observations about this fork's visible records, not claims about builds performed privately or by upstream.

## 3. What the passing checkpoint establishes

The latest successful run is **40733668783**, with job **122976365640**. Its recorded output contains fourteen passing source checks and zero failing source checks. The parser suite records five tests passing, and the shell-syntax step completes successfully. The workflow uploads a source-preflight report. [3]

| Evidence item | Result | Boundary of the result |
|---|---|---|
| Source/provenance preflight | **PASS: 14/14** | Selected text checks, fixed pins, ancestry, and committed protected-path comparison |
| Axiom-output parser fixtures | **PASS: 5/5** | Synthetic strings exercising selected acceptance and rejection cases |
| Rebuild shell syntax | **PASS** | Bash accepts the script's syntax |
| Entire project compilation | **UNRESOLVED** | No independent full-build result in the inspected audit record |
| Actual final-theorem axioms | **UNRESOLVED** | No executed axiom-probe output supplied |
| Complete dependency and certificate review | **UNRESOLVED** | Recursive closure has not been independently established |
| Statement alignment | **UNRESOLVED** | Full intended semantics have not been independently confirmed |
| Forty-six Zoo operations | **UNRESOLVED: 46/46** | No operation-specific execution evidence |

The fourteen checks in `verify_cfsg_source.py` cover the Lean pin, two dependency pins, comparator target text, literal absence of `sorry` in the submitted solution, separation of the challenge template, the visible wrapper and assembly references, presence of the second milestone, the configured permitted axioms, self-assessed review metadata, probe target names, original-commit ancestry, and unchanged protected paths. Several are substring checks. They are useful guards against source drift and configuration mistakes, but they do not elaborate Lean expressions or validate the transitive mathematical proof. [2]

The five parser tests exercise axiom-free output, standard-axiom output, rejection of an unexpected `sorryAx`, rejection of a missing target, and rejection of duplicate output. Passing these fixtures does not establish that an actual Lean run produced acceptable output, nor does it exhaustively validate the parser against every possible log format.

The earlier October 27 report recorded **ten bounded static passes and three unresolved larger questions**. Those observations overlap in purpose with the later automated preflight and must not be added to it as twenty-four independent proof checks. Neither set counts as executed Zoo animal operations. [5]

## 4. The theorem path and its remaining trust boundary

The frozen comparator source declares:

```lean
theorem CFSGComparator.classification : TauCeti.ClassificationStatement.{u}
```

Its supplied proof term refers through the certified wrapper to the project's classification theorem. The earlier source review traced the visible route from `CFSGComparator.classification`, through `CFSG.Certified.classification_finite_simple_groups` and `CFSG.classification_finite_simple_groups`, to the classification assembly. This establishes a concrete source-level proof route, while leaving the full imported corpus to be verified. [5, 6]

The separate `Comparator/Challenge.lean` file contains a `sorry` as a challenge template. Its existence alone is not evidence of a hole in the submitted `Comparator/Solution.lean`. Conversely, the absence of that literal token in the solution is insufficient to establish the axiom dependencies of everything reachable from it.

The checked-in probe requests actual axiom output for two final declarations:

1. `CFSGComparator.classification`.
2. `CFSG.Milestones.cfsg_classification_native_and_realization`.

The intended allowed set is `propext`, `Quot.sound`, and `Classical.choice`, with subsets acceptable to the parser. At this checkpoint the configured set is known; the actual reported dependencies are not. The second declaration's name does not itself demonstrate use of a native evaluator. Any such trust dependency must be established from the reachable implementation and compiled evidence. [7]

A successful build and acceptable axiom output would still leave a semantic question: whether the formal statements, definitions, hypotheses, universe handling, and classification catalogue express the intended CFSG claim. That review is an explicit outstanding obligation.

## 5. Rebuild readiness and limitations

The repository contains a rebuild script, a manually dispatchable workflow, the Lean probe, and an axiom-log parser. The script is intended to record the environment, run source preflight, build the entire project, invoke the probe, and classify the resulting axiom output. Its completed-phase status would certify only the build-and-parser stage; it would not automatically complete semantic review or execute the Zoo. [7, 8]

The full-build workflow requests a self-hosted Linux x64 runner labeled `cfsg-large`. No completed or queued full-build run appears in the inspected run listing. Runner availability has not been independently verified.

The reconstruction plan proposes **64 GB RAM, 150–200 GB free disk, and capacity for a day or more of execution** as a starting allocation. These are planning estimates, not measured minimum requirements. The upstream README reports that a build below twenty-four hours used open Lake changes and optimizations. Their exact requirements and reproducibility remain to be resolved before treating the proposed environment as validated. GitHub repository-size metadata also does not directly measure build disk requirements. [8, 9]

Two limitations deserve explicit attention before execution:

- **Clean-checkout enforcement:** the script records `git status --porcelain`, but does not itself reject a dirty working tree. The preflight compares committed revisions. Manual execution therefore needs an explicit check for uncommitted or untracked inputs that could affect compilation.
- **Unexecuted command path:** shell syntax and parser fixtures do not validate the Lake command options, dependency retrieval, memory behavior, or Lean probe against the pinned toolchain. Any required adjustment must be recorded and reviewed rather than silently absorbed into a claim that the original procedure ran unchanged.

The EFMW-inspired optimization note proposes operational monitoring and conservative reuse of artifacts tied to exact inputs. It supplies no measured speed-up and cannot substitute for Lean verification. [10]

## 6. Next-stage work and acceptance evidence

The nearest source-analysis milestone is a **complete transitive import inventory**. The current preflight does not implement recursive import traversal, and no such inventory deliverable was present in the inspected audit directory or scripts directory.

That inventory should start from both final theorem entry modules, resolve imports against pinned project and dependency sources, retain module identities and hashes, identify generated certificate modules, and report every missing or ambiguous resolution. It should distinguish modules imported into an environment from declarations actually used by the final proof terms. An import graph is an audit aid; its existence alone does not prove logical dependency closure.

The remaining sequence is:

| Stage | Evidence required before recording completion |
|---|---|
| Dependency inventory | Pinned roots and dependencies; reproducible edges and hashes; explicit unresolved entries and completeness criteria |
| Clean full rebuild | Recorded environment and any Lake patch; clean source state; complete build logs and exit status; all intended project targets built |
| Final axiom inspection | Successful probe execution; exact output for both target declarations; parser result and retained raw logs |
| Certificate and statement review | Reachable proof/certificate provenance; any trust-sensitive mechanisms accounted for; independently checked statement alignment |
| Zoo operation review | Separate operation-specific inputs, applicability decisions, outputs, and evidence for each claimed result |

A timeout or resource exhaustion establishes a failed execution attempt under the recorded environment, not a contradiction in finite-group theory. A compiler error would require diagnosis against the exact source and toolchain. An unexpected axiom in a final declaration would challenge the stated axiom claim and must be investigated explicitly.

The existing forty-six-entry Zoo intake remains frozen at zero passes, zero failures, forty-six unresolved entries, and zero N/A entries. Its reported limiter category is **QUALIFIED**, reflecting incomplete evidence. This paper does not claim to rerun that limiter or any animal kernel. [5]

## 7. Preliminary assessment

The audit has reached a useful engineering checkpoint: its mathematical target is identified, its selected-source checks are implemented, its test results can be inspected, and its remaining proof obligations are explicit. The successful CI record supports confidence in those bounded preflight observations.

Independent reproduction of the full formalization remains pending. The correct public claim is that **Monolithic has completed and checked a source-preflight stage of the CFSG audit, with the complete build, actual axiom closure, dependency/certificate review, and statement alignment still unresolved**. No mathematical refutation has been established by this stage.

**Disclosure:** This report was prepared with AI-assisted repository inspection and drafting. The October 28 hosted logs were reviewed rather than independently rerun for publication. The original formalization and its mathematical authorship remain credited to the upstream contributors.

## Evidence and references

All source links below are pinned to an inspected commit. Actions records document the specific hosted run; they are not a substitute for retaining evidence in a future reproducibility release.

1. [Original formalization metadata, authorship, dependencies, and declared review status](https://github.com/enuminous/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/formalization.yaml).
2. [Source-preflight implementation](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/scripts/verify_cfsg_source.py).
3. [Latest successful source-preflight run](https://github.com/enuminous/CFSG/actions/runs/40733668783), [job and step logs](https://github.com/enuminous/CFSG/actions/runs/40733668783/job/122976365640), and [uploaded source-preflight artifact](https://github.com/enuminous/CFSG/actions/runs/40733668783/artifacts/12836452360). Tested revision: `e46ef02c378dbe1665566bd77a24037fb46ee840`.
4. [Comparison of the passing revision with the inspected fork head](https://github.com/enuminous/CFSG/compare/e46ef02c378dbe1665566bd77a24037fb46ee840...df6242e23368e81f4be97dc02998e53ad2d41224).
5. [October 27 bounded Zoo evidence audit](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/audit/CFSG_ZOO_2026-10-27.md) and [machine-readable intake](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/audit/CFSG_ZOO_INTAKE_2026-10-27.json).
6. [Frozen comparator solution](https://github.com/enuminous/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/Comparator/Solution.lean), [certified wrapper](https://github.com/enuminous/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Certified/Classification.lean), and [classification statement](https://github.com/enuminous/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Statement.lean).
7. [Final-theorem probe](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/audit/CFSGChainCheck.lean), [axiom-output parser](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/scripts/verify_cfsg_axioms.py), and [parser fixture tests](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/scripts/test_verify_cfsg_axioms.py).
8. [Full rebuild script](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/scripts/rebuild_cfsg_full.sh), [manual full-build workflow](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/.github/workflows/cfsg-full-rebuild.yml), and [reconstruction plan](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/audit/CFSG_REBUILD_PLAN.md).
9. [Original README and upstream build description](https://github.com/enuminous/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/README.md), [toolchain pin](https://github.com/enuminous/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/lean-toolchain), and [dependency manifest](https://github.com/enuminous/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/lake-manifest.json).
10. [EFMW-inspired optimization note and its stated limits](https://github.com/enuminous/CFSG/blob/df6242e23368e81f4be97dc02998e53ad2d41224/audit/EFMW_CFSG_OPTIMIZATION_NOTE.md).
