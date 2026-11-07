# Reproduce the predictive-inference reanalysis

The analysis uses the anonymized public trial files from A. M. Loosen, T. X. F. Seow and T. U. Hauser, [original study](https://doi.org/10.3758/s13428-024-02427-y), [data repository](https://osf.io/hakq9/), [authors’ code](https://github.com/amloosen/A-Psychometric-Investigation-of-the-Predictive-Inference-Task). Only aggregate results and constructed stimuli are redistributed.

From this directory, using Bash, Python 3.12 and the pinned libraries in requirements.txt:

```sh
set -eu
mkdir -p data reproduced
curl --fail --location --retry 2 https://osf.io/download/v89g7/ -o data/t1.csv
curl --fail --location --retry 2 https://osf.io/download/59py4/ -o data/t2.csv
python -m pip install -r requirements.txt
export OPENBLAS_NUM_THREADS=1
python analyze.py data reproduced/results.json
python sensitivity.py data reproduced/sensitivity.json
python matched.py reproduced/pairs.csv
```

The scripts verify published OSF SHA-256 digests before fitting. The source filenames are Table_gamePIT_pt1.csv and Table_gamePIT_t2.csv (OSF file identifiers 631f3cb9d88c0704de9d14fc and 631f3cbd753784051dd9a8bc). Data downloads totaled 72,910,078 bytes. The inputs in the commands above are aliases for those two files.

`analyze.py` predicts the current raw confidence rating and the signed change in bucket placement. Its first contrast adds weighted absolute error, B. Fraction R is a separate secondary contrast, not an extra term on top of B. `results.json` gives participant-weighted loss, paired changes, conditional bootstrap intervals, and fold-specific coefficients. `sensitivity.py` adds nonlinear normalized signed memory, then the current adjustment magnitude and randomly initialized rating-slider position; it reports confidence only. `matched.py` checks the original five-error example and writes the exact constructed pairs with both recent errors held equal. Fractions are exact. Column abs_A is the weighted absolute error for the first history and abs_B the corresponding quantity for the second.

The first analysis decisions are recorded in [design.md](design.md). Exact floating-point output can depend on the numerical runtime. Compare numerical fields with a tolerance if replaying on a different platform.
