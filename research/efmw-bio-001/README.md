# EFMW-BIO-001 — public research companion

[Read the paper](../../EFMW-BIO-001-Cellular-Memory-Negative-Result.md).

**Result:** on 70,987 retained MCF10A cells from three experimental replicates,
the fixed EFMW-inspired memory feature reduced primary log10 Fra-1 MSE by 3.62%
relative to its summary ablation, but had 1.19% higher MSE than the conventional
comparator selected using training data. An ordinary EWMA produced the same
predictions. The practical screen failed on all eight nuclear readouts.

This is exploratory reanalysis of processed public data. The authors normalized
outcomes across replicates; our split does not undo that upstream dependence.
There is no independent laboratory replication or validation of a physical field law.

## Included evidence

- [Frozen protocol](PROTOCOL.md), [protocol freeze](protocol_freeze.json), and [code hashes](code_freeze.json).
- [All results](results/benchmark.json), [240 fold scores](results/fold_metrics.csv), and [inner tuning](results/inner_tuning.json).
- [Data audit](results/data_audit.json), [numerical verification](results/verification.json), and [archive recovery record](results/archive_recovery.json).
- [Source checksums](source/source_file_hashes.json), [Figshare metadata](source/figshare_metadata.json), and [the authors' README](source/README_author.txt).
- [Original monitor](source/monitors_original.py), [comparison figure](primary_comparison.svg), and executable scripts.

## Reproduce from public data

Use Python 3.12. The recorded execution used Python 3.12.14 and the package versions
in `requirements.txt`. From the repository root:

```bash
cd research/efmw-bio-001
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python fetch_public_data.py
python prepare_data.py
python reproduce.py
```

The shell activation command above is for Linux/macOS. Use the equivalent virtual
environment activation on other platforms. Allow roughly 1 GB of free working space
and several GB of RAM. Network access is required only to install dependencies and
retrieve the source files. Timing and resource use depend on the local machine.

`fetch_public_data.py` retrieves the exact public archive members using HTTP byte
ranges and checks CRC values. `prepare_data.py` regenerates the retained numeric
archive. `reproduce.py` runs the unchanged frozen numerical runner in a temporary
directory, verifies scores and complete prediction output, then copies results
back atomically. The output overwrites corresponding local result files.

The large original spreadsheets, `data/analysis_data.npz`, and
`results/held_out_predictions.npz` are **not committed to this repository**.
The commands regenerate all three. Public reproduction does not require access
to a private ChatGPT file or account. `verify_results.py` can also be run directly
after regeneration; original-spreadsheet spot checks run when those files exist.

The source ZIP download has a 581,981,223-byte total size, but the fetcher retrieves
selected members rather than downloading the entire source-data archive. It also
retrieves selected author code for provenance. Complete outer-archive MD5 verification
is not claimed. Member hashes are recorded before our preprocessing.

## Definitions and provenance

The recurrence is `m[t] = 0.97*m[t-1] + 0.03*x[t]`, with `m[0]=0`,
`t=1,...,189`, and terminal feature `abs(m[189])`. Here `x` is observed ERK activity.
This replaces the synthetic plant residual used in the original monitor, an explicit
adaptation recorded before evaluation. The recurrence is mathematically an EWMA.

Data: Ram and colleagues, Figshare, DOI
[10.6084/m9.figshare.27047617.v1](https://doi.org/10.6084/m9.figshare.27047617.v1),
licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Original article: [10.1038/s41467-025-58348-7](https://doi.org/10.1038/s41467-025-58348-7).
The paper supplies full author attribution and describes our transformations.

`PUBLICATION_MANIFEST.json` records SHA256 digests of committed companion files.
`code_freeze.json` separately preserves the original protocol and analysis-code hashes.
The freeze is local and timestamped, not an externally registered preregistration.
