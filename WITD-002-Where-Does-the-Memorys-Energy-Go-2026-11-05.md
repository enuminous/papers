# Where Does the Memory's Energy Go?
## WITD–002: Energy Accounting, Tensor Mismatch and Conventional Memory Equivalence in the Wrightian Laboratory

**Matthew Chenoweth Wright · Monolithic LLC / EFMW research program**  
**5 November 2026 · Research report v1.0**  
**Evidence class:** conditional mathematical derivation and reproducible numerical study. AI-assisted implementation, analysis and drafting. No physical measurement, Lean kernel proof, journal peer review or independent-investigator replication is claimed.

**Laboratory:** [Information-Tensor](https://github.com/enuminous/Information-Tensor)  
**Frozen source audited:** [WITD–001 at 694b3f1](https://github.com/enuminous/Information-Tensor/tree/694b3f132e0cd451295a5dbba346859e9e070dd1)  
**Published research package:** [Derivation, protocol, implementation and receipts](https://github.com/enuminous/Information-Tensor/tree/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002)

## Abstract

The Wrightian Informational Tensor Dynamics laboratory evolves a scalar field, a tracking-memory variable, a global coherence parameter and a discrete Scalar-23 map. Its original display adds a weighted scalar-style memory stress to the field stress, without a joint action for the dissipative system. This study derives an explicit storage functional and separates damping, relaxation, coherence modulation, applied forcing and discrete-update work. It proves that, for positive scalar mass squared and positive fixed memory coupling, no constant weight makes the original displayed energy density equal this storage for all homogeneous states. The fixed-coherence memory force is exactly equivalent to a conventional exponential velocity-memory kernel. A separate Python implementation agrees with JavaScript to approximately 3.05×10⁻¹⁶ in the prescribed comparison. The frozen numerical study records eleven passing and two failing gate groups; both failures concern predeclared cumulative-energy-residual refinement ratios and are retained. The result is an energy-accounting correction and a bounded representation obstruction, not a new force, a completed covariant theory or empirical validation of EFMW.

## 1. The question behind the animation

The laboratory makes memory visible: a field moves, a second field follows it with a lag, and feedback changes what happens next. But a moving picture cannot by itself explain where the energy comes from. When memory changes a field's acceleration, the model needs a defined place to store exchanged energy and an account of what damping removes. When an algorithm abruptly changes a coupled state, that update can also supply work.

The preceding [journalistic account](A-Field-That-Remembers-Inside-the-Wrightian-Tensor-Laboratory-2026-11-04.md) described these mechanisms and their limits. WITD–002 asks a narrower question: **does the tensor being displayed represent the stored energy of the dynamics actually being evolved?** Its answer is generally no for the specified tensor, while an alternative, explicitly named storage functional does admit a useful balance law.

The original engine was preserved byte for byte. Its Git blob is `9d014bb047efd67f5273d88296619c230ced1ed5`. The added diagnostic wrapper observes the actual integration stages and evaluates endpoint storage; exact snapshot comparisons confirm that it leaves the tested trajectories unchanged. The existing browser tensor remains the original diagnostic. The new energy is not silently substituted for a gravitational source.

## 2. An explicit energy account

Write r=q−m, g(t)=κΦ(t), c=κ23 and V(q)=μ²q²/2+λq⁴/4. Between discrete updates the implemented equations are

\[
q_t=p,\qquad p_t=\Delta q-V'(q)-\gamma p-gr-c(q-h)+s,
\qquad m_t=\alpha r.
\]

The study uses a flat periodic domain with no z dependence. All quantities are normalized computational variables; length, field, action and detector calibrations are not supplied by this result. Parameters μ²,λ,γ,α,c are nonnegative. Nonnegative memory storage additionally requires g≥0, which must be checked rather than inferred for arbitrary restored states or noisy coherence trajectories.

Define

\[
e=\frac{p^2}{2}+\frac{|\nabla q|^2}{2}+V(q)
+\frac g2(q-m)^2+\frac c2(q-h)^2,
\qquad \mathbf J=-p\nabla q.
\]

Direct differentiation gives, while h is held fixed,

\[
\boxed{\partial_t e+\nabla\cdot\mathbf J
=-\gamma p^2-g\alpha(q-m)^2
+\frac{\kappa\Phi_t}{2}(q-m)^2+ps.}
\]

The two negative terms represent damping and tracking-relaxation losses when g≥0. The remaining terms are work from changing the coupling and from the applied source. For fixed g≥0, fixed h and no source, integrated storage is nonincreasing. This is a conditional Lyapunov statement; it does not establish a unique final state or general nonlinear stability.

A scalar reservoir account u_t=γp²+gα(q−m)² closes the energy balance in the passive case. It does not furnish reservoir momentum, temperature, an entropy law or a covariant stress tensor. A full relativistic completion remains a distinct problem.

The finite-difference implementation uses forward-bond gradient energy, which matches its five-point Laplacian under periodic summation by parts. It does not use the display's central-gradient tensor as a proxy for that discrete energy. Full algebra and boundary assumptions are recorded in the [derivation](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/DERIVATION.md).

## 3. The displayed tensor fails a simple representation test

The original tensor is I_ab=T_ab[q]+βT_ab[m], where m_t=α(q−m) and the memory potential is μ²m²/2. For homogeneous states with p=0 and the map coupling disabled,

\[
I_{00}=V(q)+\frac\beta2[\alpha^2(q-m)^2+\mu^2m^2],
\qquad e=V(q)+\frac g2(q-m)^2.
\]

Assume μ²>0 and g>0. If the expressions were equal for every state at one constant β, choosing q=m=a≠0 would require β=0. Choosing q=0,m=a would then leave e=ga²/2>0 but I00=0. This contradiction proves the stated obstruction.

Two numerical examples make the mismatch explicit. With unit area, μ=0.5, α=0.3, g=0.15, β=0.2 and λ=0:

| State | Derived storage | Displayed tensor energy | Display minus storage |
|---|---:|---:|---:|
| q=m=1, p=0 | 0.125 | 0.150 | +0.025 |
| q=0, m=1, p=0 | 0.075 | 0.034 | −0.041 |

At the second state, the analytic displayed energy rate is −0.0204, while the derived storage rate is −0.045 in the frozen-coherence model. Homogeneity eliminates spatial-gradient and flux ambiguities. This is a failure of a specific tensor-to-storage identification. It is not a theorem that no alternative informational stress or enlarged action can exist. Dissipation itself is not inconsistent: it requires an explicit environment account.

## 4. What supplies the energy in the full laboratory?

The original numerical step updates h before integrating the field and adds stochastic coherence forcing afterward. These changes contribute exact endpoint work:

\[
W_{\rm map}=\frac c2\int[(q-h^+)^2-(q-h^-)^2],d^2x,
\qquad
W_{\rm noise}=\frac\kappa2\Delta\Phi\int(q-m)^2,d^2x.
\]

The first expression uses the pre-field-step q. The second uses the final q,m at the noise update. The four smooth work/loss terms are integrated at the engine's actual RK4 stages. Omitting a prescribed map or coherence update produces a detectable imbalance in the rejection controls; including its work closes the corresponding endpoint account to the prescribed tolerance.

For the specified noise-free hybrid run, n=8, dx=0.5, dt=0.01 and T=1:

| Energy-accounting quantity | Normalized value |
|---|---:|
| Initial storage | 0.961988095183 |
| Final storage | 1.536468303597 |
| Scalar-23 map work | +0.619322371701 |
| Coherence-modulation work | +0.005048314992 |
| Applied-source work | +0.001221943497 |
| Damping loss | −0.040828794131 |
| Relaxation loss | −0.010283627768 |
| Unaccounted endpoint defect | +1.2410×10⁻¹⁰ |

The map supplies most of the energy increase through its changing coupling potential. This is work performed by an algorithmic update; no physical energy source or spontaneous creation has been observed. Two additional deterministic seeds give the same trajectory because no random term is active. They are recorded for completeness, not counted as independent replications. Three prescribed noise=0.1 runs have absolute ledger defects below 1.24×10⁻¹⁰, with stochastic work separately reported.

![WITD–002 work budget, spatial convergence and failed time-ratio gates](https://raw.githubusercontent.com/enuminous/Information-Tensor/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/figure.svg)

*Figure 1. The energy budget is for a specified synthetic run. Spatial refinement passes its frozen criterion. Both cumulative-balance time-ratio gates fail; their absolute defects nevertheless decrease. No panel depicts measured physical data.*

## 5. Conventional memory and numerical evidence

For fixed g, the difference variable obeys r_t+αr=p, hence

\[
r(t,x)=e^{-\alpha t}r(0,x)+\int_0^t e^{-\alpha(t-u)}p(u,x)\,du.
\]

The force −gr is therefore an exponentially fading velocity-memory term, including initial memory. The equivalent local representation evolves q,p,r and reconstructs m=q−r. Exponential-memory embeddings are established mathematical machinery [1,2]; the derivation here specifies their exact application to this lab. It does not establish thermal fluctuation–dissipation consistency for the lab's separate coherence-noise prescription.

An independently written Python standard-library implementation uses q,p,r coordinates. At n=8, dt=0.01 and T=2, its maximum q,p,m difference from JavaScript is 3.0531×10⁻¹⁶. This supports implementation equivalence in the prescribed case. It is not independent-investigator replication, and the conventional equivalence supplies no uniquely EFMW physical signature.

The local protocol was fixed before numerical execution, then published with results. It was not externally preregistered. Its thirteen numerical gate groups yielded eleven PASS and two FAIL outcomes:

| Check | Outcome |
|---|---|
| Pinned engine bytes | PASS |
| Fixed-coherence cumulative-balance time ratios | **FAIL:** 5.9928, 9.4819; both required in [8,32] |
| Dynamic-coherence cumulative-balance time ratios | **FAIL:** 2.7710, 11.3206; both required in [8,32] |
| Independent conventional-model implementation | PASS |
| Manufactured spatial convergence | PASS: error ratios 3.9451, 3.9862 |
| Six prescribed hybrid ledger cases | PASS within the 10⁻⁶ absolute defect threshold |
| Tensor counterexamples | PASS as counterexamples |
| Trajectory preservation and rejection-control group | PASS |

The manufactured spatial errors are 0.0017702132, 0.0004487113 and 0.0001125655 on n=8,16,32 grids, with a fixed physical domain, dt=0.001 and an analytically prescribed source. These are verification data, not observations of a new interaction.

All absolute time-balance defects decrease with refinement, but their reduction factors miss the frozen rule. In the fixed arm the signed defect changes sign. Exploratory follow-up compared trajectories with a dt=0.000625 reference and found state-error halving ratios of approximately 15.99–16.06. This supports fourth-order smooth trajectory convergence in those examples, while cancellation and preasymptotic behavior plausibly explain the balance-ratio sensitivity. The follow-up is marked post-outcome; neither failed original gate has been relabeled. A full hybrid continuum-order claim would be inappropriate because the original algorithm changes the number of Scalar-23 updates when dt changes.

## 6. Reproduction, provenance and limitations

The [version-pinned package](https://github.com/enuminous/Information-Tensor/tree/b02b04897743d34cdb846e9fac2518cd8faa4399) supplies the protocol, full derivation, ledger, independent comparator, raw results, diagnostic follow-up and figure generator. Every frozen arm and work component is retained. Research-source SHA-256 values are embedded in the receipt. Execution used Node v24.22.1 and Python 3.12.14. All 35 original tests and five additional ledger regression tests passed; this software-test count is separate from the thirteen research gate groups.

```sh
npm test
node scripts/verify.cjs
node research/witd-002/run.cjs
# Expected exit 1: two frozen research gates FAIL.
node research/witd-002/replay.cjs
# Expected exit 0: the archived mixed PASS/FAIL results reproduce.
node research/witd-002/diagnostics.cjs
```

A green replay means that the recorded outcomes reproduce, including their failures. The execution notes disclose the initial syntax repair and later receipt/configuration clarification; thresholds and numerical parameters were not retuned.

The closest earlier corpus result, [TOE-001](TOE-001-Unified-Action-and-Correspondence-Test.md), derived conditional conservation for a distinct conventional two-scalar covariant construction. WITD–002 does not identify that construction with the lab's tracking closure. Its contribution is the explicit account and obstruction for the actual executable model. Like the [density-gradient closure review](EFMW-Physical-Validation-Recursive-Closure-2026-11-03.md), it treats conventional equivalence as a substantive result rather than a discovery claim.

**Established within scope:** an energy identity, passive storage conditions, a scalar reservoir account, a constant-weight representation obstruction and conventional exponential-memory equivalence. **Unresolved:** a joint covariant action for the full lab, total momentum and reservoir stress, physical unit calibration, phi-specific advantage, a discriminating observable and external physical validation. The broader EFMW research program is neither proved nor disproved by this bounded study.

## References

1. Wiśniewski, M., Łuczka, J. and Spiechowicz, J. (2024). *Memory corrections to Markovian Langevin dynamics*. [arXiv:2405.11370](https://arxiv.org/abs/2405.11370).
2. Lei, H., Baker, N. and Li, X. (2016). *Data-driven parameterization of the generalized Langevin equation*. [arXiv:1606.02596](https://arxiv.org/abs/1606.02596); [PNAS DOI](https://doi.org/10.1073/pnas.1609587113).
3. Wright / Monolithic (2026). [WITD–001 implemented model](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/docs/THEORY.md) and [original experiment protocol](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/docs/EXPERIMENTS.md).
4. WITD–002 (2026). [Frozen local protocol](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/PROTOCOL.md), [results receipt](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/results.json) and [post-outcome diagnostics](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/diagnostics.json).
