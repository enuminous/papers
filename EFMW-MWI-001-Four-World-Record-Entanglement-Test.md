# EFMW–MWI-001: A Four-World Record-Entanglement Test and Its Interpretational Limits

**Matthew Chenoweth Wright**  
Monolithic LLC · October 18, 2026  
**Research status:** Analytic reconstruction of a deterministic finite toy-model checkpoint; neither a test of physically existing parallel universes nor independent experimental verification.

## Abstract

We investigate whether the recorded reduced-world purity in the finite four-world EFMW *Carried Record* simulator can be explained by an elementary quantum entanglement construction. At normalized simulation time \(t=1.5\), the source dossier reports four world weights \(p=(0.064944511,0.186794757,0.561686559,0.186574174)\), a toggled binary record associated with world 1, and reduced-world purity \(0.696195049\). We construct a pure state on \(\mathbb C^4\otimes\mathbb C^2\) with a controlled record flip and derive the reduced-world purity \(P=(1-p_1)^2+p_1^2=0.6961950485\), agreeing at the precision of the reported data. We also consider two **hypothetical additional controls**: reversing the controlled flip restores purity 1 in this constructed state; complete dephasing of the world labels instead yields diagonal-world purity \(\sum_i p_i^2=0.389411784\). These identities show that a standard quantum-information model reproduces one simulator checkpoint. They neither reconstruct the full recorded dynamics nor distinguish Everettian Many-Worlds from other interpretations of ordinary quantum mechanics. The work identifies an exact correspondence hypothesis for a future code-level audit and a properly specified objective-collapse comparison.

## 1. Provenance and scope

The supplied *Carried Record* dossier describes a deterministic finite simulation with **run ID** \`run-5722a7cb\`, 20,000 steps, step size 0.025, and terminal normalized time 500. It names four world populations, a one-bit record, and diagnostic quantities including global purity, reduced-world purity, coherence, and mutual information. The dossier labels its outputs *deterministic measurements of a finite toy model*; the EFMW feedback interpretation is a model postulate, not independent evidence of Many-Worlds or an empirical result.

The scripted record operation occurs at step 60, \(t=1.5\): “Record bit toggled in world 1.” A swap of world labels 1 and 3 follows at step 160, \(t=4\), **with the record preserved**. Subsequent checkpoints extend to \(t=500\). Our detailed reconstruction applies to the **first post-toggle checkpoint only**. No individual travel route or wavefunction-collapse event was sampled. The dominant world label is an ensemble statistic, not a realized history.

## 2. Reconstructed Hilbert-space state

Let \(\{|i\rangle\}_{i=0}^3\) be orthonormal labels for the four worlds and \(\{|0\rangle,|1\rangle\}\) an orthonormal two-state record register. Treat the reported populations as normalized weights \(p_i\ge 0,\sum_i p_i=1\), up to printed rounding. Choose amplitudes \(\sqrt{p_i}\) with zero relative phase *as a reconstruction convention, not an inferred simulator phase*.

Immediately after the controlled bit flip, define
\[
|\Psi\rangle=\sum_{i\ne1}\sqrt{p_i}|i\rangle|0\rangle+\sqrt{p_1}|1\rangle|1\rangle.
\]
This is a state in \(\mathbb C^4\otimes\mathbb C^2\). Its norm is \(\langle\Psi|\Psi\rangle=\sum_i p_i=1\) in exact normalized arithmetic. Put \(q=p_1\), and let \(|A\rangle=(1-q)^{-1/2}\sum_{i\ne1}\sqrt{p_i}|i\rangle\) if \(q\ne1\). Since \(\langle A|1\rangle=0\),
\[
|\Psi\rangle=\sqrt{1-q}|A\rangle|0\rangle+\sqrt q|1\rangle|1\rangle.
\]
The reduced density matrix after tracing out the record is
\[
\rho_W=\operatorname{Tr}_{R}|\Psi\rangle\langle\Psi|
=(1-q)|A\rangle\langle A|+q|1\rangle\langle1|.
\]
The nonzero eigenvalues are \(1-q\) and \(q\), hence
\[
\boxed{P_W=\operatorname{Tr}(\rho_W^2)=(1-q)^2+q^2=1-2q(1-q).}
\]
The result is independent of the three other population weights separately (given their sum \(1-q\)), which makes this checkpoint a sharply specified correspondence test.

## 3. Numerical comparison

The dossier reports, at \(t=1.5\):
- \(p_0=0.064944511\)
- \(p_1=0.186794757\)
- \(p_2=0.561686559\)
- \(p_3=0.186574174\)
- reduced-world purity \(P_{\mathrm{dossier}}=0.696195049\)

Substitution gives
\[
P_{\mathrm{reconstructed}}=(1-0.186794757)^2+(0.186794757)^2
=0.696195048485378.
\]
Thus the discrepancy at displayed precision is about \(5.15\times10^{-10}\), smaller than the rounding inherent in the listed population and purity digits. **The calculation reproduces the checkpoint's purity, not the simulator's state or implementation.** The near-equality could reflect a shared underlying binary-record model; establishing this requires examining the actual simulation equations and state-update code.

The dossier's near-unit global purity and trace should be read as floating-point numerical outputs. Neither values very near 1 nor slightly above 1 are exact proofs of normalization or purity.

## 4. Two counterfactual controls on the reconstructed state

The following are analytic interventions on **our constructed state**. They did **not** occur in the supplied dossier and must not be misreported as historical simulator output.

### 4.1 Coherent uncomputation

Apply the inverse of the controlled bit flip to the combined **world-plus-record** state. The state becomes
\[
|\Psi_{\mathrm{undo}}\rangle=
\left(\sum_i\sqrt{p_i}|i\rangle\right)\otimes|0\rangle.
\]
The world marginal is then a rank-one projector:
\[
P_{\mathrm{undo}}=1.
\]
This requires coherent access to both subsystems and an exact inverse. Simply resetting, measuring, or discarding the record is not equivalent to reversing a joint unitary interaction. Environmental coupling or inaccessible systems could prevent the assumed reversal.

### 4.2 Full dephasing in the world-label basis

Apply a complete dephasing channel to the world labels (without changing diagonal weights):
\[
\Delta_W(\rho_W)=\sum_i p_i|i\rangle\langle i|.
\]
Consequently,
\[
P_{\mathrm{dephased}}=\sum_i p_i^2\approx0.389411784.
\]
No population is deleted by this operation. It suppresses interference between the chosen labels. It must not be interpreted as empirical annihilation or selection of physical worlds.

| Constructed condition | Reduced-world purity |
|---|---:|
| Recorded post-toggle checkpoint, reproduced by model | 0.696195049 |
| Counterfactual inverse controlled flip | 1.000000000 |
| Counterfactual full world-basis dephasing | 0.389411784 |

## 5. What is—and is not—tested about Many-Worlds

Everettian quantum mechanics reads the universal state as evolving without a fundamental stochastic collapse, with decoherence contributing to effectively autonomous branches. The mathematics of a reduced density matrix, entanglement, and coherence loss is, however, used across multiple interpretations of the same quantum formalism. **No choice between interpretations follows solely from reproducing a reduced-state purity.**

A distinct experiment would need to contrast physically distinct **dynamical** models, for example specified objective-collapse theories versus ordinary unitary evolution, using interference recovery or other observables with computed parameter-dependent predictions. Even observing standard unitary quantum behavior does not single out the Everett interpretation over all other interpretations that make the same operational predictions.

The toy model does not establish actual other universes, traveler histories, observer experiences, consciousness, moral conclusions, or the events of any fictional television narrative. Its record is a **one-bit subsystem**, not a human autobiographical memory.

The dossier's labels such as “world purity,” “coherence,” “mutual information,” and “outside” must not be assigned extra physical meanings without their implementation-level definitions.

## 6. Next audit and falsification steps

1. **Code correspondence:** inspect the simulator's density-matrix representation, record flip, partial trace, and purity routines; compare the actual complex matrix with the reconstructed \(\rho_W\) for all relevant timestamps, not only the \(t=1.5\) scalar purity.
2. **Precision tests:** retain full-precision weights and report absolute/relative residuals, finite-precision errors, and normalization drift.
3. **Coherence-revival control:** implement reversible controlled flip on the actual joint state and check whether purity revival matches predictions when *all* entangled degrees of freedom are accessible.
4. **Controlled dephasing:** explicitly define a CPTP dephasing channel, confirm diagonal weights persist, and verify coherence and purity changes at several dephasing strengths.
5. **No-peek model discrimination:** predefine at least one objective-collapse dynamics, its physical parameters, likelihood, and held-out discriminatory statistic. Do not describe competing interpretations with identical operational predictions as experimentally distinguished.
6. **Independent verification:** freeze the code, seed/configuration, exact reference outputs, tests and hashes; reproduce in a clean environment, optionally complementing numeric tests with Lean matrix/state invariants.

## 7. Zoo-style disposition

| Obligation | Finding |
|---|---|
| Four-world/one-bit state can be constructed | PASS (mathematical construction) |
| Post-toggle world purity reproduced | PASS (analytic reconstruction, within reported rounding) |
| Coherent uncomputation restores purity | PASS (constructed-state identity) |
| Dephasing preserves populations | PASS (defined quantum channel) |
| Exact simulator-code correspondence | OPEN |
| Full-run quantum-state reconstruction | OPEN |
| New EFMW-specific mechanism | NOT ESTABLISHED |
| Everettian ontological branching confirmed | NOT ESTABLISHED |
| Discrimination of physically distinct collapse models | NOT TESTED |

## 8. Conclusion

The recorded checkpoint from the EFMW finite four-world model is exactly what a conventional controlled-record entanglement construction would predict, to the available numerical precision. The result is useful because it supplies a simple and reproducible benchmark for auditing the simulator's interpretation of reduced-world purity. It does not establish a new physical law or that Many-Worlds is true; its strongest contribution is a clearly formulated bridge between a reported toy-model quantity and standard quantum-information mathematics.

## References and related material

- [EFMW Multiverse Simulator](https://github.com/enuminous/Multiverse-Simulator) — source project for code-level verification.
- [EFMW boundary of established physics](EFMW_Boundary_of_Established_Physics.md) — separation of established results and proposed physics.
- H. Everett III, “Relative State” Formulation of Quantum Mechanics, *Reviews of Modern Physics* **29**, 454–462 (1957), DOI: [10.1103/RevModPhys.29.454](https://doi.org/10.1103/RevModPhys.29.454).
- W. H. Zurek, Decoherence, einselection, and the quantum origins of the classical, *Reviews of Modern Physics* **75**, 715–775 (2003), DOI: [10.1103/RevModPhys.75.715](https://doi.org/10.1103/RevModPhys.75.715).
- M. Schlosshauer, Decoherence, the measurement problem, and interpretations of quantum mechanics, *Reviews of Modern Physics* **76**, 1267–1305 (2005), DOI: [10.1103/RevModPhys.76.1267](https://doi.org/10.1103/RevModPhys.76.1267).

**Reproducibility statement:** Arithmetic identities were evaluated from the displayed eight-to-nine-digit dossier populations. No independent full simulator replay, Lean run, experimental quantum hardware run, or measurement of cosmological branching is represented by this paper.
