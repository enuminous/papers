# TRISPHERE-INT-001 — Stability is not computational memory

Monolithic LLC · November 26, 2026 · Exploratory negative result, not peer reviewed.

## Question
Can the TriSphere interacting-packet dynamics act as a reservoir for temporal memory and nonlinear logic? Physical stability does not imply recoverable information. The candidate is a one-dimensional numerical system, not a physical device or general intelligence.

## Method
48 particles; 3000 iid binary input symbols per sequence, seeds 42,43,44 (input seed +100); 20 substeps per symbol at dt=.05. Central energy kick J=3+2u, u in {-1,+1}; damping .08; 48 local mixing cells; beta=1 unless ablated. Inner shelf [3.5,4.5], outer shelf [11,12]. Readout: 12 normalized occupancy bins plus 12 normalized sums of velocity (not cell mean velocity). Compare full model, beta=0, inner shelf removed, 24-unit echo-state network and 24 linear taps. Ridge penalty .01; intercept unpenalized; scaling learned only on training data. Washout 200, training indices 200–1999, held-out indices 2000–2999. Targets: delays 1,3,5; XOR current and previous bit; parity of current and previous two bits; AND of current and lag-2 bit. Circular rolls do not contaminate scored indices. Three seeds x five models x six tasks =90 scores; 25,920,000 TriSphere particle substeps. Feature counts matched, compute costs not matched. No hyperparameter search or preregistration.

## Mean held-out scores
Memory metrics R²; logic metrics accuracy as proportions.
| Model | Delay 1 | Delay 3 | Delay 5 | XOR | Parity3 | AND |
|---|---:|---:|---:|---:|---:|---:|
| TriSphere | -0.0241 | 0.0131 | -0.0004 | 0.5053 | 0.5053 | 0.7390 |
| No coupling | 0.0622 | 0.1167 | 0.0691 | 0.5003 | 0.5023 | 0.7293 |
| No inner shelf | 0.0035 | 0.0057 | 0.0002 | 0.5143 | 0.5133 | 0.7413 |
| ESN | 0.9812 | 0.5286 | 0.3853 | 0.5307 | 1.0000 | 0.9887 |
| Linear taps | 1.0000 | 1.0000 | 1.0000 | 0.5317 | 0.5043 | 1.0000 |

The always-false AND baseline is .738, .733, .753 on the three test sequences (mean .74133), exceeding full TriSphere's .739 mean. No reliable nonlinear logic or competitive memory demonstrated. Removing coupling improves all three mean memory scores, consistent with a synchronization-memory tradeoff, not a proof of the mechanism. The ESN and linear taps substantially outperform the full candidate on memory. The parity result for the ESN is task-specific; no general intelligence inference.

## Verdict
Operational input-dependent reservoir and trained readout: demonstrated in this implementation. Competitive memory and logic: negative result for this tested configuration, not a universal impossibility theorem. Criteria retrospective. Heterogeneous damping, richer input encoding, phase-sensitive readout and controlled coupling ablations are proposed for INT-002. Preserve the original negative results.

## Reproduce
Install NumPy and run `python experiments/TRISPHERE-INT-001/run.py` from the repository root. It overwrites the local results.json, so use a clean checkout or preserve the original first. The score records were transcribed from the original local JSON; the source was copied from the executed local file. Publication turn did not rerun the benchmark. Original local SHA256 run.py 47d098ba3abc2fe473e44ae660ad354ce289a41fc07f718195f36c2eaf473484; results.json df986695d2762343d67c7edeabbe09c8aa55d22ef6aae962019894629d1e629b. Serialization may differ. Independent reproduction outstanding.

Prior dynamical work: https://github.com/enuminous/trisphere/tree/eff6c4b1d35e7df4d37031e8b1ffb7cf41c332aa

Pinned package: https://github.com/enuminous/trisphere/tree/86115e01fdde06df9f06ecadfb3b576a6288121b/experiments/TRISPHERE-INT-001
