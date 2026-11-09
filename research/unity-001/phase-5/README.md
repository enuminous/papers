# UNITY-001 / Phase 5 — Identifiability before physical prediction

**Executed 2026-11-09.** Bounded synthetic model screening succeeded, but **no EFMW-specific physical prediction is ready for confirmatory testing**.

[Executed research report](PHASE5_REPORT.md) · [PREDICTION-001 candidate](PREDICTION_001.md) · [Frozen protocol](PROTOCOL.json) · [Exact rational evaluator](predict.py) · [25 tests](test_predict.py) · [Execution receipt](EXECUTION.json) · [CI-generated result artifact](https://github.com/enuminous/papers/actions/runs/42633977283/artifacts/13682645693).

Results: **4 PASS / 1 FAIL / 6 UNRESOLVED** among 11 Phase 5 findings; **25/25 software tests PASS**. A strong conventional co-located-matter comparator has **zero profile Fisher information** for the proposed signal. An almost matching conventional comparator inflates nominal uncertainty by **567.2×** relative to the deliberately narrow baseline. These are *hypothetical dimensionless models*, not physical instruments or real measurements.

From the repository root:

~~~bash
python3 -m unittest discover -s research/unity-001/phase-5 -p 'test_*.py' -v
python3 research/unity-001/phase-5/predict.py --out research/unity-001/phase-5/build/results.json
~~~

**Important:** The protocol is a frozen *simulation* specification; no actual EFMW mass density, conserved stress, empirical comparator, experiment or confirmatory preregistration has been completed. The original MOC-001 historical finding counts and earlier Unity phases remain unchanged.
