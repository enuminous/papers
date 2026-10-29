EFMW-CX-001 — Complexity of EFMW in a 16-framework comparison
29 October 2026

START: report.html. It is self-contained and opens offline.

This is an executed corpus audit and an exploratory literature benchmark.
It is not an exhaustive census, a scalar ranking, or a test of physical truth.
All 16 comparison entries have an explicitly selected variant and source.

REPRODUCE:
  python analyze.py
  python render_report.py

analyze.py uses only Python's standard library and checks the frozen protocol.
render_report.py uses NumPy 2.3.5 and Matplotlib 3.10.8 for the figure.
The original run used Python 3.12.14.

CONTENTS:
protocol.json — frozen before measurement/coding, after initial source discovery.
sources/ — exact EFMW source snapshots; Git blob hashes checked.
source_manifest.json — primary/authored literature and pinned GitHub references.
comparisons.json — six-dimensional descriptive profiles of 16 selected variants.
analyze.py — executable counts, duplicate checks, representation control and
             explicitly supplementary documentation-dependency diagnostics.
render_report.py — generates the figure and the self-contained report.
narrative.html — report's authored analysis, linked to generated result values.
results/metrics.json — complete quantitative outputs and limitations.
results/entry_metrics.csv — all 102 rows, with literal extraction rules.
results/source_hashes.json — SHA256 of each local EFMW source snapshot.
results/benchmark.png — scientific summary figure, not a theory leaderboard.
MANIFEST_SHA256.txt — package file hashes, excluding this manifest itself.

The recorded review categories are 53 structural encodings, 15 analytic models,
1 partial specialization and 33 open entries. They are NOT validation rates.
The source's 102 fields include definitions, expansions and operational prose.
No number of independent physical laws, primitive entities or free parameters
is inferred from this entry count.

The dependency-graph analysis and ME-102-exclusion sensitivity are explicitly
post-inspection additions. Literature coding has one analyst and no measured
inter-rater reliability. There was no new Lean build or experiment in this study.
