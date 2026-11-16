# Physlib Maxwell audit — evidence companion

[Read the full audit](../../Physlib-Maxwell-Full-Zoo-Audit-2026-11-16.md) · [Papers index](../../README.md) · [Publication record](PUBLICATION_NOTICE.md)

**Bounded Physlib proof audit: PASS. Zoo release integrity: FAIL (stale README checksum). EFMW physical validation: not established.**

All 53 accounted-for animal names are recorded: 1 provenance PASS, 1 audit-tool integrity FAIL, 7 UNRESOLVED, 44 NOT_APPLICABLE. Three fixed operations ran on target or audit records; a full-roster assessment does not mean every statistical pipeline executed.

## Complete replay package

[Download Physlib-Full-Zoo-Audit-2026-11-16.zip](Physlib-Full-Zoo-Audit-2026-11-16.zip) — the original 367-file archive, including its bundle manifest, with code, source snapshots, licenses, successful and failed logs, quarantined rejection controls, and replay instructions.

SHA-256: `208d49c988bbef3c38affb118a12713c95c9168fbbd6046fe72f78be10aa1560`.

After extracting, run `python3 report/replay.py --check-only` to check bundled bytes. To reproduce the audit, install Git, Python 3.10+ and elan, then run `python3 report/replay.py`. The known Zoo checksum failure remains an expected failed integrity check; it is not silently repaired.

## Browse the evidence

- [Original report](Physlib_Full_Zoo_Audit_2026-11-16.md)
- [Full roster](FULL_ROSTER.md) · [CSV](FULL_ROSTER.csv) · [Machine-readable schemas and decisions](FULL_ROSTER.json)
- [Frozen audit plan](AUDIT_PLAN.md) · [Local execution freeze](FREEZE.json)
- [Final checks](FINAL_CHECKS.json) · [Source and dependency integrity](FINAL_INTEGRITY.json) · [Source pins](SOURCE_PINS.json)
- [Zoo manifest failure](ZOO_MANIFEST_CHECK.json) · [Final CIRCUS gate](CIRCUS-final-result.json)
- [Preserved corrections and failed attempts](AMENDMENTS.md)
- [Four-root axiom/dependency harness](Audit.lean) · [Nonvacuity witness](ZeroWitness.lean)
- [Proposed README manifest repair](ZOO_README_MANIFEST.patch) — not applied to the audited Zoo checkout.
- [Original bundle file hashes](BUNDLE_SHA256.json)

These browsable files are copies from the delivered package. Relative workspace paths in the original plan and result records describe the extracted archive; use the ZIP for execution. The complete proof traces and logs are in the archive.

This is an uncommissioned AI-assisted source review and local replay, not independent human certification or Physlib endorsement. Cached upstream dependencies were used, and the Maxwell source was freshly elaborated. No new physical measurement or EFMW-specific prediction is established.
