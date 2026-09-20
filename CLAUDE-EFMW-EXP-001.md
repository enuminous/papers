# CLAUDE-EFMW-EXP-001

## Preliminary AI-Assisted Review and Conditional GW170817 Coupling Constraint

| Field | Record |
|---|---|
| Record ID | CLAUDE-EFMW-EXP-001 |
| Session date | September 20, 2026 |
| Report version | 1.0 |
| Framework originator | Matthew Chenoweth Wright, Monolithic LLC; `enuminous` |
| Reviewing system reported in session notes | Claude, Anthropic; exact model/version not supplied |
| Report preparation | ChatGPT-assisted synthesis of user-supplied Claude session notes, with additional source inspection and numerical verification |
| Study type | Retrospective review and secondary application of a published observational constraint |
| Overall outcome | Conditional bound calculated; physical applicability unresolved; no EFMW detection established |

> **Scope:** This is a record of a preliminary AI-assisted assessment. The `EXP` identifier is an internal tracking label, not a claim that a new physical experiment was performed. This record is not scientific peer review, independent experimental replication, or endorsement by Anthropic or OpenAI.

## 1. Summary

According to session notes supplied by Matthew Chenoweth Wright, Claude examined selected EFMW materials, including a Lean 4 development identified as `Aristotle_EFMW_Lean`. Claude distinguished formal mathematical derivation from physical validation and applied a reported coupling inequality to the published GW170817 gravitational-wave speed constraint.

Claude reported a conservative upper bound of approximately `7.7 × 10⁻⁸` on the coupling parameter. The arithmetic is reproducible under the assumptions specified below. A subsequent calculation in preparing this record gives:

$$
|\alpha|\leq 7.7459666924\times10^{-8}
$$

using a conservative fractional speed tolerance of `3 × 10⁻¹⁵`.

The decisive limitation is that a bound on the observed gravitational-wave speed does not automatically constrain a separate scalar-field propagation speed. The required physical connection has not been established in the materials inspected for this report. Consequently, the calculation is a **conditional observational constraint**, not evidence of a nonzero EFMW effect.

## 2. Review provenance and evidence boundary

The source record is a user-supplied summary titled “Session Notes: EFMW, reviewed with Claude (Anthropic),” dated September 20, 2026. It describes one conversation, not a discovery report. The complete underlying Claude transcript, prompts, tool logs, and exact model identifier were not supplied.

This report separates three sources of information:

1. **Reported by the Claude session notes:** repository review, a quoted project status statement, and use of a Lean-proved coupling inequality.
2. **Directly inspected in the subsequent ChatGPT review:** the supplied `ActionsAndFluids.lean` source file.
3. **Checked during report preparation:** the published GW170817 interval and numerical evaluation of the stated inequality.

The report does not independently certify the full Lean repository or attribute the subsequent corrections to Claude. Public repository counts, publication history, biographical details, and the absence of prior human review were not independently audited here.

Claude provides an external AI critique in the limited sense of a separate system assessing selected project materials. The review was initiated by the framework's originator and was not blinded or institutionally commissioned. Different AI systems can share errors; their agreement is not equivalent to independent measurement or specialist peer review.

## 3. Question examined

**Given the proposed scalar-wave speed relation, what coupling bound follows if the published GW170817 speed constraint applies to that mode?**

The working relation is:

$$
v_\phi=\frac{c}{\sqrt{1-\alpha^2}},
\qquad c>0,\quad \alpha\in\mathbb{R},\quad |\alpha|<1.
$$

Here `α` is dimensionless. For real `α` in this domain, the proposed speed is at least `c` and equals `c` when `α = 0`.

The session notes report the inequality:

$$
\alpha^2(c+p)^2\leq p^2+2pc,
$$

where `p ≥ 0` is an **absolute speed tolerance**, with the same units as `c`. If the observational tolerance is fractional, `ε`, the substitution is `p = εc`, not `p = ε` in dimensional units.

The exact Lean theorem declaration, its assumptions, its file, and its repository commit were not supplied. The derivation below verifies the algebra under the explicit working assumptions; it is not a verification of that unprovided Lean declaration.

## 4. Observational input

The LIGO/Virgo/Fermi/INTEGRAL study of GW170817 and GRB 170817A reports a gamma-ray arrival delay of `1.74 ± 0.05 s` and constrains the fractional difference between gravitational-wave speed and light speed to:

$$
-3\times10^{-15}\leq\frac{v_{\rm GW}-c}{c}\leq7\times10^{-16}.
$$

Source: [Abbott et al. (2017), *Gravitational Waves and Gamma-Rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A*](https://arxiv.org/abs/1710.05834), *Astrophysical Journal Letters* **848**, L13; [DOI: 10.3847/2041-8213/aa920c](https://doi.org/10.3847/2041-8213/aa920c).

This is a published inference with astrophysical emission-timing assumptions, not a direct laboratory measurement of an EFMW scalar mode. This report uses the published interval; it does not reanalyze detector strain data or reconstruct its likelihood.

## 5. Conditional derivation

Assume that the mode described by the working speed relation is subject to an upper speed limit `c + p`. Then:

$$
\frac{c}{\sqrt{1-\alpha^2}}\leq c+p.
$$

The stated domain permits multiplication and squaring without changing the inequality direction:

$$
c^2\leq(c+p)^2(1-\alpha^2).
$$

Rearrangement gives:

$$
\alpha^2(c+p)^2\leq(c+p)^2-c^2=p^2+2pc.
$$

With `ε = p/c`:

$$
|\alpha|\leq\sqrt{\frac{2\epsilon+\epsilon^2}{(1+\epsilon)^2}}.
$$

For small positive `ε`, the leading approximation is `|α| ≲ √(2ε)`.

| Interpretation | Fractional upper tolerance | Calculated bound |
|---|---:|---:|
| Conservative envelope used to reproduce Claude's reported result | `3 × 10⁻¹⁵` | `|α| ≤ 7.7459666924 × 10⁻⁸` |
| Positive endpoint, applicable to the necessarily superluminal working relation if it governs the observed mode | `7 × 10⁻¹⁶` | `|α| ≤ 3.7416573868 × 10⁻⁸` |

The conservative value is a valid but weaker consequence of the published interval under the same mode-identification assumption. The tighter value is a subsequent clarification, not a claim about what Claude originally calculated. Absolute-value notation makes the sign symmetry explicit; writing `α ≤ ...` alone requires a convention that `α ≥ 0`.

## 6. Reproduce the arithmetic

The following uses only Python's standard library. Decimal arithmetic avoids cancellation and binary floating-point precision issues near unity.

```python
from decimal import Decimal, getcontext

getcontext().prec = 60

def alpha_bound(epsilon):
    e = Decimal(epsilon)
    return ((2 * e + e * e) / (1 + e) ** 2).sqrt()

for epsilon in ("3e-15", "7e-16"):
    print(epsilon, alpha_bound(epsilon))
```

Output verified during preparation of this report:

```text
3e-15 7.74596669241481634193347286623892263701310269705068837564349E-8
7e-16 3.74165738677393942121362067599863963524883978815966980079552E-8
```

This reproduces the parameter transformation only. It does not reproduce the astrophysical observation or validate the physical model.

## 7. Lean source inspection

The supplied `ActionsAndFluids.lean` imports `RequestProject.EFMW.GoldenScaling`. Its SHA-256 fingerprint is:

```text
2125d979a27b3a92ce7c7b3912aef4855960f3f45af0758509cc753b47957693
```

The file contains six theorem declarations:

| Declaration | Scope of the proposition |
|---|---|
| `action_decomposition` | Linearity of the interval integral over five integrable sector terms. |
| `semiclassicalEq_no_efmw_sources` | Reduction of the defined field equation when the two added sources vanish. |
| `relNavierStokes_inviscid` | Algebraic reduction when viscous and external-force terms vanish. |
| `density_stationary_of_uniform_flux` | Zero time derivative of density, given the defined continuity equation and zero spatial flux derivative. |
| `fluidStress_symm` | Symmetry of the defined stress components under symmetry assumptions on the metric and shear components. |
| `torus888_mem_torus` | Unit-circle membership of both coordinate pairs of the defined mapping. |

No `sorry` placeholders are visible in this file. It was inspected as source, not compiled during this review, and imported dependencies were not audited. In particular:

- The file does not contain the quoted speed-bound theorem.
- It does not derive field equations by varying the action.
- It does not establish the relationship between scalar propagation and the observed gravitational-wave mode.
- Its density theorem establishes a zero derivative; interpreting this as time-independent density requires suitable regularity and domain conditions.

These propositions are mainly standard identities or reductions of the supplied definitions. Their formalization can be useful without constituting new physical laws. Successful checking of selected propositions would establish those propositions relative to Lean's foundations and their dependencies, not the consistency or empirical truth of all EFMW claims.

The Claude notes quote the broader project's status document as stating: “Nothing in this development asserts that EFMW describes nature.” That quotation is retained here as reported provenance, not as a fresh inspection of `EFMW_STATUS.md`.

## 8. Findings and limitations

| Claim | Status | Basis |
|---|---|---|
| The conservative number follows from the stated speed law and tolerance. | Demonstrated mathematically | Algebra and numerical evaluation above. |
| The positive endpoint gives a tighter bound for the superluminal working relation. | Demonstrated conditionally | Same derivation, smaller applicable upper tolerance. |
| The quoted inequality is a checked theorem in the full Lean repository. | Reported; not independently verified here | Exact declaration, commit, build, and dependency audit absent. |
| GW170817 constrains this EFMW scalar parameter. | Unresolved | Requires a derivation connecting the scalar mode to the observational constraint. |
| A nonzero EFMW effect was detected. | Not established | An upper bound includes `α = 0`; no detection statistic was computed. |
| EFMW was confirmed or falsified as a framework. | Not established | Only a conditional constraint on a specified speed relation was evaluated. |
| An external AI-assisted critique occurred. | Documented through supplied session notes | Full transcript and exact model metadata not supplied. |
| Scientific peer review or independent experimental replication occurred. | Not established by this record | Neither process was performed here. |

No new experiment, simulation, raw-data fit, p-value, Bayes factor, or detection significance is reported. No claim of novelty is made for converting a speed tolerance into a model-parameter bound.

The notes report that no other EFMW prediction was compared with real data during that Claude conversation. This statement concerns that session only and does not assess the full history of EFMW work.

## 9. Independence and anti-circularity

The published observational interval is external to EFMW. The parameter bound nevertheless depends on the proposed speed law and its applicability to the measured mode. Assuming that applicability and then citing the resulting bound as evidence for the assumption would be circular.

A parameter value selected after seeing the interval is not an independently successful prediction. The admissibility of zero coupling does not favor EFMW over a baseline predicting propagation at `c`. Conversely, an upper bound can be scientifically useful if its applicability is derived and it excludes meaningful, previously allowed parameter space. That additional value has not been demonstrated here.

This record is retrospective. No preregistration is claimed, and the original session's material-selection process cannot be reconstructed from the supplied notes alone.

## 10. Next derivation and acceptance criteria

The immediate technical task is to derive the propagation of observable perturbations from a fully specified EFMW action or field-equation system.

Before another empirical comparison:

1. Pin the equations, conventions, background solution, parameter domain, and repository commit.
2. Identify physical propagating modes and derive their characteristic speeds, including any mixing.
3. Establish how the relevant mode is generated, detected, and related to the gravitational-wave signal used in the published analysis.
4. Specify the observational assumptions and applicable frequency and distance regime.
5. Recover the appropriate zero-coupling limit and audit the mathematical and physical assumptions independently.

**Acceptance condition for applying the present bound:** the derivation establishes that the observed mode is governed by the stated speed relation, or gives an explicit justified mapping from the measured speed to `α`, under the assumptions of the observational analysis.

**Failure condition:** the observed mode is unaffected by this scalar speed, the proposed mapping is invalid, or the derived dynamics contradict the assumed propagation law. In that case, withdraw this parameter constraint or replace it with the one actually implied by the derived model.

**Unresolved condition:** insufficient dynamics or mode analysis to decide applicability. Retain the arithmetic as conditional and make no empirical claim about `α`.

These are proposed criteria for subsequent work, not a preregistration of the completed conversation. A future discriminating test should freeze its prediction, baseline, nuisance assumptions, dataset, and decision rule before evaluating results.

## 11. Reproducibility items still needed

- Full Claude transcript or export, including exact model/version and tool activity where available.
- Repository URL and immutable commit for the reviewed Lean development.
- Exact declaration and assumptions of the reported coupling theorem.
- Lean toolchain, dependency manifest, successful build log, and theorem-axiom audit.
- Derivation connecting the proposed scalar speed to the observable constrained by GW170817.

## 12. Public description

EFMW underwent a preliminary AI-assisted review using Anthropic's Claude on September 20, 2026, according to session notes supplied by Matthew Chenoweth Wright. The review distinguished formal mathematical work from physical validation and reported a conservative coupling bound derived conditionally from the published GW170817 speed constraint. The arithmetic is reproducible, but its application to EFMW requires a physical connection between the proposed scalar mode and the observed gravitational-wave mode. No nonzero EFMW effect, scientific peer review, or institutional endorsement is established by this record.

## References and attribution

1. Matthew Chenoweth Wright, user-supplied *Session Notes: EFMW, reviewed with Claude (Anthropic)*, September 20, 2026. Primary session summary; full transcript not supplied.
2. B. P. Abbott et al., *Gravitational Waves and Gamma-Rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A*, 2017. [arXiv:1710.05834](https://arxiv.org/abs/1710.05834). [Journal DOI](https://doi.org/10.3847/2041-8213/aa920c).
3. `ActionsAndFluids.lean`, user-supplied source artifact, fingerprint recorded above. Its original repository revision and license were not established in this review.

Framework attribution: Matthew Chenoweth Wright / Monolithic LLC. Claude and Anthropic are identified solely to describe the reported reviewing system and provider. This report was prepared with ChatGPT assistance and includes subsequent analysis beyond the supplied Claude notes. No license is assigned here to third-party source material.
