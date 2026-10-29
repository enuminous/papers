# EFMW-CX-001 reproducibility package

[Read the full paper](../../EFMW-CX-001-Complexity-of-EFMW-and-Physical-Frameworks.md) · [Original HTML report](report.html) · [Original archive](EFMW-CX-001-reproducible-study.zip)

Executed on 29 October 2026. A pinned 102-entry EFMW corpus audit and a descriptive
comparison of sixteen selected physical frameworks, including EFMW. This is an
exploratory study, not a universal ranking, exhaustive literature census, or test
of physical truth.

## Reproduce

From this directory:

```sh
python analyze.py
python -m pip install -r requirements.txt
python render_report.py
```

The audit uses the Python standard library. The original environment was Python
3.12.14, NumPy 2.3.5, and Matplotlib 3.10.8. Rendering regenerates the report and
figures; figure metadata can vary between runs. The original archived package and
its `MANIFEST_SHA256.txt` retain the exact delivered bytes. The original manifest
covers the original 21 companion files, not this added guide or the archive copy.

## Contents

- [Frozen protocol](protocol.json), [analysis code](analyze.py), and [rendering code](render_report.py).
- [Metrics](results/metrics.json), [102-row extraction](results/entry_metrics.csv), and [execution record](results/execution.json).
- [Sixteen framework profiles](comparisons.json) and [nineteen-source manifest](source_manifest.json).
- [Pinned EFMW source snapshots](sources/) and [source SHA256s](results/source_hashes.json).
- [Figure (PNG)](results/benchmark.png), [figure (SVG)](results/benchmark.svg), and [original file hashes](MANIFEST_SHA256.txt).
- [Original package instructions](README.txt).

## Findings and limits

The catalogue contains 102 records and 2,196 lexical tokens. These counts do not
establish 102 independent physical laws. The frozen review categories are 53
structural encodings, 15 analytic models, one partial specialization, and 33 open
entries; they are not validation rates. Two equivalent response formulas differ
by 46.0% in Python syntax-tree size and agree to a maximum relative difference of
3.77e-16 over 3,003 sampled points. Syntax size is representation-dependent.

No scalar cross-theory ranking or whole-theory parameter count is established.
Literature coding has one analyst. Dependency diagnostics and the ME-102 exclusion
are explicitly post-inspection additions. No new Lean build or laboratory
experiment was performed. Prepared for Matthew Chenoweth Wright / Monolithic LLC;
AI-assisted research and coding by Codex.
