# SYNC-71113-001 reproducibility companion

Companion to [From Synchronicity to Synchronization: The 7–11–13 Structure in Modular Recurrence and Barker Coding](../../From-Synchronicity-to-Synchronization-7-11-13.md), Matthew Chenoweth Wright, 25 October 2026.

**Version:** 1.0.0. **Scope:** exact finite calculations and elementary proofs. The selection of the triple and 31-position budget is exploratory. No physical or noisy-detection experiment is reported.

## Reproduce

Python 3.9 or later, with no third-party dependencies:

~~~sh
python research/sync-71113/verify.py --check
~~~

This recomputes all numerical outputs and compares them with the checked-in files. A successful run prints "result": "PASS" and exits zero. It was run locally with Python 3.12.14.

The [GitHub Actions workflow](../../.github/workflows/sync-71113.yml) runs the same command on changes to this package. Its run record reports the remote outcome separately from the local result.

To regenerate the outputs intentionally:

~~~sh
python research/sync-71113/verify.py --write
~~~

Regeneration overwrites the five generated numerical files in this directory. It does not change the paper or figure.

## Files

| File | Contents |
|---|---|
| [verify.py](verify.py) | Input sign sequences, deterministic calculations, independent indexing/enumeration checks, and publication-output checks |
| [results.json](results.json) | Definitions, maxima, peak lags, periodic multiplicities, and neighboring-budget optima |
| [sequences.csv](sequences.csv) | All 1,001 entries of each of the six nested orders and the CRT product |
| [correlations.csv](correlations.csv) | Lags 0–1,000, six nested aperiodic correlations, CRT aperiodic and periodic correlations |
| [triples_budget31.csv](triples_budget31.csv) | All 865 unordered positive-integer triples with sum at most 31, including noncoprime cases |
| [checksums.json](checksums.json) | SHA-256 digests of the verifier and four numerical output files |
| [plot.py](plot.py) | Optional publication-figure renderer; requires Matplotlib |
| [autocorrelation.svg](autocorrelation.svg) | Figure embedded in the paper |

## Signal conventions

Indexing is zero-based. The code vectors are the representatives in Schmidt and Willms, [arXiv:1501.06035v1](https://arxiv.org/abs/1501.06035v1). Aperiodic correlation uses zero extension; periodic correlation wraps modulo the signal length. The CSV contains only nonnegative lags because these real autocorrelations determine the negative-lag values by symmetry.

For an order $(p,q,r)$, the nested sequence is

~~~text
B_p[n // (q*r)] * B_q[(n // r) % q] * B_r[n % r].
~~~

The CRT product is

~~~text
B_7[n % 7] * B_11[n % 11] * B_13[n % 13].
~~~

These order the same tensor entries differently. They are not assumed to have the same aperiodic correlations. The reported CRT aperiodic maximum is for the specific origin $n=0$, not an optimization over cyclic origins.

## Verified outputs

- The common-clock phase orbit has 1,001 distinct states and period 1,001.
- Each individual Barker code has maximum absolute aperiodic sidelobe 1.
- Every one of the six standard nested orders has maximum absolute aperiodic sidelobe 143.
- The specified CRT product has aperiodic maximum 122 and periodic maximum 143.
- All periodic CRT correlations equal the product of the three component periodic correlations.
- The unique unordered maximizing triple for $a+b+c\le31$ is $(7,11,13)$, with LCM 1,001.
- At budgets 30 and 32, the respective optima are $(9,10,11)$ with 990 and $(9,10,13)$ with 1,170.

All of these checks passed locally. They are not evidence of an empirical advantage, independent replication, mathematical priority, or proof-assistant verification.

## Optional figure

The figure was generated with Matplotlib from the published CSV:

~~~sh
python research/sync-71113/plot.py
~~~

Matplotlib is only needed for this optional rendering step. The core verification is standard-library-only. Figure bytes can vary across Matplotlib versions; the figure is not part of the deterministic numerical checksum set.

## Next experiment

The paper gives an outline for a separately frozen, equal-energy, equal-length detection benchmark with conventional controls and noise/offset perturbations. Numerical trial counts, seeds, thresholds, and decision rules still need to be fixed before execution. No future experiment has been run or registered by publishing this note.
