# CL33 release-review companion

This directory accompanies [CL33 Under Review: Operator-Only Language Modeling and a Documented Reproducibility Repair](../../CL33-Review-and-Reproducibility-Repair.md), by Matthew Chenoweth Wright, 25 October 2026.

## Frozen scope

Compare Hugging Face `mirrorethic/cl33-oplm` revisions:

- Before repair: `0f7d63c4551a15a9bb5b2f35c8d4fe6b111dc2bf`.
- After repair: `b081c1c8888a857d5dfdd1ec4f1d94b497834473`.

This is static release verification. The verifier never imports the upstream model, downloads .pt checkpoints, deserializes model weights, or runs inference. It fetches files no larger than 1 MiB and uses NumPy with `allow_pickle=False` for the evaluation fixture.

## Run

Requires Python 3.10+ and NumPy. The exact Python and NumPy versions used for the recorded run are in `verification.json`.

```bash
python verify_release.py --cache /tmp/cl33-release-review --output verification-rerun.json
```

Internet access to Hugging Face and its file-serving endpoints is required. This program only reads from the source service and writes its cache and result file locally. Re-running will overwrite the selected output path.

## Recorded observations

- Old manifest: 8 downloaded-file passes, 2 byte-hash mismatches, 3 missing paths.
- New manifest: 13 downloaded-file passes; 3 checkpoint entries not downloaded.
- All three checkpoint manifest hashes match the API's published storage hashes, which are unchanged across revisions. This is a metadata check, not a fresh hash of checkpoint bytes.
- Six model-definition files have identical downloaded bytes.
- Five existing files changed; one held-out fixture was added.
- All three checkpoint-loading calls changed from `weights_only=False` to `weights_only=True`.
- The new fixture has 108 rows of 1024 token IDs; six sources contribute 18 rows each.

## Files

| File | Purpose |
|---|---|
| `verify_release.py` | Read-only upstream downloader and static verifier |
| `verification.json` | Per-file hashes, fixture shapes, comparison, and runtime |
| `provenance.json` | Revision chronology and observation boundaries |

The performance numbers discussed in the paper remain publisher-reported. Training/evaluation disjointness is not independently established by merely inspecting an evaluation file. The new upstream held-out evaluator prints comparisons but does not enforce a tolerance through a failing exit code.

The published verifier intentionally records findings rather than using a single success/failure label that would obscure unperformed checks. A network or parsing error raises an exception; successful process completion means inspection completed, not that every scientific claim passed.

