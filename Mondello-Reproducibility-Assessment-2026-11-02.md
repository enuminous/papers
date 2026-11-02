# Mondello Lean proof: reproducibility assessment

Date: 2026-11-02. Status: UNRESOLVED. This is a follow-up to the October 26 Monolithic Zoo assessment, not a replacement.

## Pinned baseline (reported, not independently authenticated)

- Source commit: `ab26ce21e3b272eec73908d5ed2f8b10117f2e38`
- Lean: `4.28.0`
- Mathlib revision: `8f9d9cff6bd728b17a24e163c9402775d9e6a365`
- Original review: https://github.com/enuminous/papers/blob/main/Mondello-Separable-Jacobian-Full-Zoo-Audit.md

## Findings

- PASS (prior audit only): fifteen exact polynomial identity checks, three collision evaluations, two mutation controls, eighteen source-manifest hash comparisons, and review of the written argument. These were reported in the October 26 assessment; they were not rerun here.
- UNRESOLVED: latest authoritative proof source and source-to-receipt provenance; no newer package identified.
- UNRESOLVED: `CLOSURE_LEDGER.md`, `PRESERVATION_MANIFEST.md`, `source-solution.txt` absent in previously examined ancillary package; no newer files recovered.
- UNRESOLVED: fresh Lean kernel replay and `#print axioms` output; no Lean or Lake binary available in this environment.
- UNRESOLVED: original external CI/Aristotle receipt authentication.
- FAIL (environment capability only): direct source retrieval from arXiv did not work because DNS resolution failed; this is not a proof failure.

## Commands and observations

```sh
which lake || true
which lean || true
# neither command returned an executable path

git --version
# git version 2.47.3

curl -I -L --max-time 12 https://arxiv.org/src/2608.02634
# curl: (6) Could not resolve host: arxiv.org
```

Gmail search for `from:rmondello2629@gmail.com after:2026/11/01` returned zero emails at inspection. GitHub code search for `PRESERVATION_MANIFEST.md Mondello` found only the existing audit reference, not a new source package. These are limited searches, not proof that the files do not exist elsewhere.

## Required replay when package arrives

1. Obtain immutable source archive or repository commit, SHA-256 manifest, `lean-toolchain`, `lakefile.*`, and `lake-manifest.json` (or exact manifest filename supplied).
2. Compare every listed digest with `sha256sum -c <manifest>` using the manifest's actual format, and record source tree SHA and dirty-state.
3. Install the exact Lean toolchain in a network-enabled isolated environment and fetch pinned dependencies.
4. Execute `lake build` from the source root; capture exit code, stdout/stderr, and tool versions.
5. Run Lean `#print axioms` for the exact terminal theorem name from source; capture output and compare with declared trust boundary.
6. Verify execution receipts against original service run IDs, commit, toolchain and dependency revisions. Distinguish reported remote execution from independent local execution.

No build, theorem, or axiom check is represented as having run in this follow-up.

## Communication

A narrowly scoped artifact request was sent to Romy in the existing Boardy introduction thread on November 2, 2026, with Boardy copied. Awaiting the exact reproducibility inputs before the November 4 meeting.
