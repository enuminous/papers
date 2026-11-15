# Evidence and reproducibility audit

## Frozen target

Determine whether the reviewed EFMW corpus entails a mass–coupling law or a quantitative relationship between observables that goes beyond the matching generic scalar effective theory. The snapshot, branch assumptions, five operations and verification criteria are in `scope.json` and `SCOPE_LOCK.json`.

Source screening and exploratory algebra preceded the verification lock. This order is disclosed; the lock does not turn exploratory work into an independent preregistered study.

## Operations actually run

These are ordinary mathematical operations with explicit inputs and criteria. No newly invented Zoo animal was used, and no claim of a full Zoo roster run is made.

| Operation | Input and transformation | Criterion | Outcome |
| --- | --- | --- | --- |
| O1: parameter non-entailment | Independent C1 mass/coupling slots; construct local nonzero countermodels | Same mass, different nonzero couplings, with a common positive kinetic domain | Demonstrated counterexample to a universal mass–coupling function |
| O2: low-energy matching | Differentiate and eliminate scalars; compare inverse-matrix and spectral forms; differentiate electromagnetic constitutive relations | Exact symbolic identities; spectral comparisons within frozen numerical tolerances | Conditional matching, subset bound and birefringence slope demonstrated |
| O3: rank stress test | Include the existing direct gauge-pair slot and an additional scalar mode | Rank-one equality must survive every claimed allowed extension | Unrestricted rank-one claim rejected |
| O4: kinetic domain | Evaluate the linear kinetic factor on all real fields and a bounded interval | Strict positivity in the declared domain | Global condition permits only zero coupling; local condition gives a bound |
| O5: normalization and propagation | Vary the arbitrary-Z root action; substitute a plane wave in ME-002/004/005 | Preserve branch conventions and do not import alpha from a different equation | Normalization ambiguity and conditional dispersion demonstrated |

## Proof obligations

| Obligation | Status and boundary |
| --- | --- |
| Fixed input definitions | Demonstrated for the chosen action snapshots; whole-program identification is unresolved |
| Canonical normalization and dimensions | Demonstrated within the selected C1 branch |
| Stable scalar vacuum | Explicit assumption: the full mass-squared Hessian is positive definite; not proved for arbitrary C1 coefficients |
| Positive gauge kinetic response | Local domain required; no unrestricted global nonzero-coupling claim |
| Low-energy and weak-field approximations | Stated analytically; an actual experiment must verify its numerical margins |
| Mapping to measurements | Conditional derivation supplied; apparatus, backgrounds and sensitivity unresolved |
| Non-entailment counterexamples | Demonstrated by exact parameter choices; not global ultraviolet-completion proofs |
| Novelty relative to the scalar baseline | Equivalent/reparameterized action; no EFMW-exclusive result established |
| Machine-checked formal proof | Not performed; symbolic and numerical Python verification is not Lean kernel certification |
| Physical test | Not performed; no new data or physical confirmation |
| Independent replication | Not performed; all checks belong to this analysis |

## Anti-circularity

No mass, coupling or optical response was fitted to observations here. The countermodels are explicitly chosen mathematical examples. The source's declaration that coefficients are independent is not replaced by a favorable fitted relation.

The same model predicts both channels, so agreement between two calculations is an internal consistency check, not two independent observations. A future response measurement must remain independent of the mass/coupling inference used to predict it. The test contract distinguishes these requirements.

The canonical alpha symbol is not silently equated with the electromagnetic fine-structure constant. C1Q's chosen cosmological mass scale is not treated as a derived optical mass. Abstract register dimensions and algebraic constant identities are not promoted to physical parameter determinations.

The direct \(XY\) slot and additional scalar modes were retained when challenging the rank-one claim. Its negative result remains in the report. A new restriction that sets those terms to zero would be a new restricted target.

## Verification

`check_relations.py` passed 33 checks, with results in `results/verification.json`. The inverse-matrix and spectral computations agreed to a maximum absolute difference of 6.938893903907228 × 10⁻¹⁸ over the four declared mode-count cases. Exact identities simplified to zero. These finite computations support the accompanying general derivation; a four-case grid alone would not prove it.

Input files were checked against their Git blob IDs and locked SHA-256 values. Exact source line endings were preserved. Early snapshot packaging introduced a trailing-newline mismatch, caught and corrected before the source lock and calculation run. C1 citation paths were also corrected to the `candidate/` directory before verification. No scientific output was selected on the basis of those packaging corrections.

The reproducibility environment is recorded in the output JSON. `verify_package.py` validates archived bytes before rerunning calculations; a rerun on a different Python release may change the software metadata in the regenerated result without changing the mathematics.

## Surviving and unresolved claims

**Demonstrated:** the conditional matching formula, its positive-mode subset bound, its leading optical consequence, the stated non-entailment counterexamples, the kinetic-domain result and the separate-branch dispersion calculation.

**Rejected within the audited assumptions:** a mandatory single-valued C1 mass–coupling function; a general full-C1 rank-one gauge response; the idea that global positivity determines a nonzero linear coupling; the idea that the root PDE alone fixes a canonical source strength.

**Unresolved:** a physically realized scalar, the quantitative apparatus mapping and sensitivity, any EFMW-specific extra restriction, physical identification of the alpha branch, and confirmation of the broader EFMW program.

The negative finding is bounded to the sources listed in `sources/CONNECTOR_SOURCES.json`; README screening is identified as such and is not described as exhaustive inspection of those repositories. Earlier frozen experiments and published results were not rerun or modified.
