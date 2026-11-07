# Conventional multiscale competitors: exploratory extension

Publication authorized by Matthew Chenoweth Wright on 7 November 2026 after delivery of the executed extension. **Exploratory; not independently reviewed.** No further contact with Professor Saito was made.

Read [TECHNICAL_SUPPLEMENT.md](TECHNICAL_SUPPLEMENT.md) for results and qualifications, and [PLAN.md](PLAN.md) for the specification recorded before the new comparisons. All original source files, the experimental design, and published results remain unchanged. The frozen plan and execution logs retain their original review-stage wording and hashes; [PUBLICATION.md](PUBLICATION.md) records the subsequent publication authorization.

The original bank contains 362 constructed pairs, or 181 modulo global sign. Ordinary fast/slow exponential contrasts distinguish every pair. This demonstrates that matching the original controls does not isolate B. The eight-feature signed contrast bank does **not** improve held-out confidence prediction in either session; this particular behavioral explanation is unsupported. Alternative absolute-error time scales have small gains comparable to B, while conditional B gains remain. None identifies a uniquely EFMW human mechanism.

## Files

| File | Purpose |
|---|---|
| `multiscale.py` | Exact pair analysis, causal features, participant-held-out fits and shifted-history controls |
| `test_multiscale.py` | Seven signal/causality/scaling checks |
| `verify.py` | Source preservation, generator identity and published-result reproduction |
| `reproduce.py` | One-command replay into a new output directory, recording commands, outputs and hashes |
| `source_snapshot.json` | Exact upstream commit and original Git blob digests |
| `results/pair-features.csv` | All exact rational feature values and pair differences |
| `results/pair-results.json` | Constructed-pair summary |
| `results/behavior-results.json` | All prespecified model comparisons and conditional bootstrap intervals |
| `results/fold-results.csv` | Aggregate model losses and dimensions by fold |
| `results/shift-controls.csv` | Every one of the 20 shifts per bank and session, with offset digests |
| `results/shift-control-results.json` | Shift diagnostic summary; no permutation p-values |
| `execution/` | Final replay logs and provenance; original data are not redistributed |

## Reproduce

Use Python 3.12 and the parent directory's pinned requirements. The execution environment already had those exact versions installed. From `research/metacognition-matched-histories`:

```bash
python -m pip install -r requirements.txt
mkdir -p data
curl --fail --location --retry 2 https://osf.io/download/v89g7/ -o data/t1.csv
curl --fail --location --retry 2 https://osf.io/download/59py4/ -o data/t2.csv
python exploratory-multiscale/reproduce.py --data data --out exploratory-multiscale/reproduced-local
```

`--out` must not exist. The runner forces BLAS/OpenMP thread counts to one for its subprocesses, checks the original data digests, executes both original scripts and the unchanged pair generator, runs the new analysis with all 20 shifts, and verifies the original results. New results are written under the chosen directory. The source patch contains no raw participant data and changes no original file. The package's source snapshot is sufficient for replay; a full repository clone is not needed.

The archived final replay is evidence of execution. The commands above are portable replay instructions; installing packages was not necessary in the recorded environment. Exact floating-point results can depend on platform, so verification permits absolute and relative tolerance of 1e-9. The recorded original numerical outputs agreed exactly.

## Earlier review package

The separately delivered review ZIP includes `multiscale-exploratory.patch`, checked against upstream commit `65f50f6710efa6801169429e5a5ad567f4d567d8`. For an unpatched checkout at that commit, the commands are:

```bash
git apply --check /path/to/multiscale-exploratory.patch
git apply /path/to/multiscale-exploratory.patch
```

The earlier patch adds only `research/metacognition-matched-histories/exploratory-multiscale/` and retains its private-review status text. Do not reapply it to a checkout that already contains this extension. This published version updates status wording and the repository navigation while preserving the executed code, frozen plan, numerical outputs and logs.
