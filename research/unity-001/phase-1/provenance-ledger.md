# UNITY-001 Phase 1 — Provenance and authorship ledger

Source repository commits and all Git blob IDs are preserved in [sources.lock.json](sources.lock.json). This ledger tracks provenance scope and operational limitations; no original repo is modified here.

## Source chain

| Candidate corpus | Frozen archival representation | Original upstream source boundary |
|---|---|---|
| Geometry ME-006/007 | `enuminous/Geometry@285b95551ca11c487eb6c0c13f8dde86b702df71:Geometry.lean` | Component-level formal analogue, not original fully covariant tensor derivation |
| Information-Tensor WITD-001/002 | `enuminous/Information-Tensor@b02b04897743d34cdb846e9fac2518cd8faa4399:docs/THEORY.md` and `research/witd-002/DERIVATION.md` | Model closures authored in lab; canonical 102 copy from `Monolithic-102-Zoo-Lean4` with **blob** pinned but original repo commit now pinned to `6e85c9e558652f5033c55d70f33077eff7a9fd89` |
| EFMW-Lagrangian C1 and triplets | `enuminous/EFMW-Lagrangian@83f9d2ec03e055c6cd09aa6359189161ad1571f6:candidate/CANDIDATE.md`, `sources/EFMW_165_field_equations.txt`, `audit/equations.csv` | Original FieldSpace upstream revisions cited by embedded `audit/source_manifest.json`; independent upstream commit pin is outside this freeze |
| Standard-Model-Reduction | `enuminous/Standard-Model-Reduction@aa569b13a594735774c7b643d44aebff4d5ad17c:three_line_standard_model_geometric_reduction.md` | Conventional SM mathematical reference; 39-strata extension is conjectural |

The archived EFMW original copies have Git blob IDs in the lock. The EFMW `audit/source_manifest.json` also retains SHA-256 values for those historical source bytes, **from the upstream project's own archival manifest**; this audit did not independently recompute those hashes.

## Licenses and rights

The Information-Tensor `LICENSE.md` states no public software license is selected. EFMW-Lagrangian `LICENSE_NOTICE.md` likewise grants no new redistribution license. The Geometry and Standard-Model-Reduction trees have no root `LICENSE` file. These records do not imply the absence of all rights, and publishing an index or a formula pointer is not a grant to redistribute complete upstream source files. The Phase-1 deliverables publish metadata, citations, reference statements and source pointers, not entire third-party source trees.

## Integrity findings

1. **585/585 archived FieldSpace source rows matched their precise historical source lines.** This confirms the audit CSV's transcription field and source-line coordinates against the text archived in the same pinned repository, not that the external historical upstream was independently reconciled.
2. **102/102 IDs are present** in each of two archived canonical representations. A literal first-formula-line comparison gives 98 matches. The four multiline entries remain to compare as full blocks, and are not presumed physically or semantically different.
3. **Source equations and normalized candidates are separate.** C1's reports expressly retain 360 literal scalar source sign failures and 90 gauge statements with underdefined/nonvariational currents; do not erase them because the normalized action has conditional matching magnitudes.
4. The SM’s three-line formulation is a conventional classical rewrite, not a proven parameter-free physical mechanism.

## Missing actions

- Pin original upstream repository commits for the historical canonical 102 and FieldSpace source snapshots and independently recheck bytes.
- Run **fresh** deterministic source-hash validation or SHA-256 checks from independently fetched raw blobs.
- Replay Lean and specified numerical verification in a clean environment, save exact commands/exits/outputs.
- Complete exact provenance mapping for every canonical equation into MOC-001's typed registry, including any ambiguities.
- Preserve scientific uncertainty: zero new EFMW-specific experimentally validated physical results.

Owner's work program: [UNITY-001 action plan](../../../UNITY-001-Pathway-to-Physical-Unification-Action-Plan-2026-11-08.md).

## Upstream origin verification addendum (2026-11-09)

Directly fetched the original upstream at immutable commits and checked Git blob IDs against the locked archival copies:

- `Monolithic-102-Zoo-Lean4@6e85c9e558652f5033c55d70f33077eff7a9fd89:canonical/equations.json` = `5e68eec5ebfed0764d0c55404249de082ce02f03`.
- `Monolithic_102_EFMW@4129cc6e86396b6752433c80a78439662b441836:CANONICAL_102.md` = `a328e4ce7c0b80565148ad28fa63eb3337e69335`.
- `FieldSpace@4f994c45c319b44eaa43133280a7671e768da87c:fieldspace_master_action.md` = `337339a42259bee4d9956a76acc23880fb97d07b`.
- Same FieldSpace commit, `EFMW_165_field_equations.txt` = `ac6313fe4a2b02a28ac8fb34519c5f96f6ea2bd8`.

**Identity checks 4/4 PASS.** Full 102-entry formula-block text compares 102/102 exact. These findings resolve the identified archived-copy provenance questions; independent model validity, source licenses, and broader ontology links still have open obligations.
