# EFMW-GW-POL-002 reproducibility companion

**Paper:** [Extra Gravitational-Wave Polarizations](../../EFMW-GW-POL-002-Extra-Gravitational-Wave-Polarizations.md)  
**Experiment:** 30 October 2026. **Publication:** 31 October 2026.

## Download and reproduce

[Download the original results archive](EFMW-GW-POL-002-results.zip?raw=true).

SHA-256:

```text
29a65c122fb377221d15de9d847d651a6799f06f32ba268ccf550b979ed4e37a
```

Extract the archive and run from its root:

```sh
python -m pip install -r requirements.txt
python run.py
python build_report.py
```

Open `report.html` for the self-contained report. The archive has 31 files and retains the original public POL data, code, source snapshots, protocol, result tables, figures, and attribution. It excludes the downloaded collaboration manuscript itself. `MANIFEST.json` records file hashes.

The original run passed **32/32 executable checks**. These are numerical and reproduction checks. They are not 32 independent observational tests or a validation of EFMW.

## Main results

- Tensor-plus-scalar / tensor Bayes factor: **1.0185245928980107**.
- Numerical evidence uncertainty: log10 ratio **0.007971519768146251 ± 0.7130185308175359**, using the released 90% half-width convention.
- Synthetic noise-only threshold crossings: **930 / 100,000**, with nominal 1% per-template false-alarm probability.
- Five simulation arms reuse the same 100,000 Gaussian noise realizations.
- Conditional C1 coupling identity checked on 1,000 numerical inputs.
- No new observed-strain search, scalar-amplitude upper limit, or EFMW coupling bound.

![Aggregate evidence and separate synthetic response check](results.svg)

## Scope and provenance

The input products are from [LIGO-P2600410-v1](https://dcc.ligo.org/LIGO-P2600410-v1/public), associated with [LIGO-P2500781-v17](https://dcc.ligo.org/LIGO-P2500781-v17/public), manuscript dated 21 July 2026. They are aggregate evidences, not event likelihoods.

The EFMW candidate is pinned to [83f9d2ec03e055c6cd09aa6359189161ad1571f6](https://github.com/enuminous/EFMW-Lagrangian/tree/83f9d2ec03e055c6cd09aa6359189161ad1571f6). It is a hypothetical action. A specified matter coupling, viable background, binary scalar charges and waveform remain necessary for an observational bound.

LVK material retains its stated CC BY 4.0 terms unless otherwise specified. See `ATTRIBUTION.txt` inside the archive for the release-requested acknowledgment. No LVK endorsement is implied. AI assistance is disclosed in the paper. Neither a complete Zoo run nor a Lean proof is claimed.
