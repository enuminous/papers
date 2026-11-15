# EFMW-C1-REL-001: a conditional photon-response relation

Research date: November 14, 2026 (Pacific). Version 1.0.0.

**A quantitative consistency test survives. A distinctive proof of EFMW does not.**

Starting from the frozen C1 action, this audit derives a relationship between scalar masses, scalar–photon couplings, and the scalar contribution to low-frequency magnetic birefringence. It also gives explicit counterexamples to a mandatory mass–coupling law and to an unrestricted rank-one relation between gauge responses.

For one canonically normalized, positive-mass scalar with interaction

\[
\mathcal L_{\rm int}=-\frac{g}{4}\sigma F_{\mu\nu}F^{\mu\nu},
\]

the leading local, classical low-energy electromagnetic coefficient is

\[
\mathcal L_{\rm eff}=-\frac14X+a_X X^2+\cdots,
\qquad X=F_{\mu\nu}F^{\mu\nu},\qquad
\boxed{a_X=\frac{g^2}{32m^2}}.
\]

For a constant transverse magnetic field, in the weak-field and low-frequency limit,

\[
\boxed{\Delta n_{\rm scalar}\equiv n_{\perp}-n_{\parallel}
=16a_X B^2+\cdots=\frac{g^2B^2}{2m^2}+\cdots.}
\]

Here the polarization directions refer to the electric field of the probe relative to the external magnetic field. These are the scalar contributions after separately accounting for other optical responses.

With several positive-mass canonical modes, the leading coefficient instead obeys

\[
\boxed{a_X=\sum_i\frac{g_i^2}{32m_i^2}
\ \geq\ \sum_{i\in S}\frac{g_i^2}{32m_i^2}}
\]

for any independently resolved subset of modes \(S\). This follows in the stated flat-vacuum, classical C1 branch. An independent local \(X^2\) operator, quantum corrections, massless modes, an inappropriate energy regime, or additional backgrounds require a different analysis.

This is **demonstrated conditional mathematics**, not a measurement. Ordinary scalar effective field theories with the same action have exactly the same relation. Agreement could support the selected scalar model; it would not identify EFMW uniquely.

Read [REPORT.md](REPORT.md) for the findings, [DERIVATIONS.md](DERIVATIONS.md) for the proofs and counterexamples, and [TEST_CONTRACT.md](TEST_CONTRACT.md) for an independent measurement design. [AUDIT.md](AUDIT.md) records the evidence boundaries.

## Reproduce

Use Python 3.12 with the versions in `requirements.txt`:

```sh
python -m pip install -r requirements.txt
python verify_package.py
python check_relations.py
```

The supplied run passed **33 mathematical checks**. The maximum difference between direct matrix elimination and numerical spectral matching was **6.94 × 10⁻¹⁸**. These checks include symbolic variation, independent constitutive differentiation, exact countermodels, basis invariance, and four spectral cases with 1, 2, 3 and 8 scalar modes. They are not 33 experiments or independent replications.

Source snapshots are pinned by Git blob and SHA-256 hashes. `SCOPE_LOCK.json` freezes the inputs and verification criteria after exploratory source screening and candidate discovery, before the check script ran. This is not an external preregistration. No original EFMW equation or earlier experimental record was changed.

Previous publication: [EFMW-C1-OBS-001](https://github.com/enuminous/papers/blob/c18b8f0aa3feba6477b828690d6be04bfa879e8b/EFMW-C1-OBS-001-From-Action-to-Observable-2026-11-14.md).
