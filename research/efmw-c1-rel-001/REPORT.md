# What the next derivation established

EFMW-C1-REL-001 · November 14, 2026 (Pacific)

The reviewed EFMW sources do not force a numerical mass–coupling law. They do support a conditional relation between two independently measurable aspects of a scalar–photon model: its on-shell interaction and its low-energy optical response. The relation is shared with established scalar effective field theory.

The practical advance is a way to cross-check the selected model without fitting both effects independently. It does not supply evidence that the scalar exists, establish the broader EFMW framework, or distinguish this branch from an ordinary scalar model with the same action.

## Results

| Candidate | Result | Evidence status |
| --- | --- | --- |
| Mass uniquely fixes photon coupling | Two allowed nonzero couplings at the same mass violate that implication. Both have positive scalar mass and a common local positive gauge-kinetic domain. | Rejected for the audited C1 assumptions |
| One scalar links photon coupling to a low-energy photon response | \(a_X=g^2/(32m^2)\); leading scalar birefringence is \(\Delta n=16a_XB^2\). | Demonstrated, conditional, known-model overlap |
| The one-mode equality survives all C1 scalar modes | Positive-mass modes contribute additively: \(a_X=\sum_i g_i^2/(32m_i^2)\). A resolved subset supplies a lower bound. | Demonstrated, conditional |
| Two gauge responses must have rank one | An allowed direct \(XY\) coupling breaks the relation; two independently coupled scalar modes also break it. | Rejected as an unrestricted C1 claim |
| Global positivity selects a nonzero coupling | \(1+g\sigma>0\) for every real \(\sigma\) forces \(g=0\). A bounded field domain gives an inequality, not a unique nonzero value. | Demonstrated mathematical obstruction |
| The root equation fixes canonical interaction strength | Its arbitrary positive action normalization \(Z\) cancels from the PDE but changes the canonical source coupling by \(\sqrt Z\). | Rejected without additional normalization/source information |
| The original alpha equation fixes a distinct wave speed | With ME-004's operator convention and alpha treated as a real constant, \(v=c/\sqrt{1-\alpha^2}\) for \(|\alpha|<1\). Neither a physical value of alpha nor its identification with the C1 photon-coupled scalar is supplied by the reviewed text. | Demonstrated dispersion; physical identification unresolved |

## The relation that survives

Write the scalar mass-squared Hessian at the flat vacuum as \(A\), with \(A\) positive definite, and the coefficients of \(X\varphi_i\) as a vector \(b\). The canonical C1 scalars have unit kinetic normalization. Eliminating their low-energy response gives

\[
a_X=\frac12 b^T A^{-1}b.
\]

Diagonalizing \(A\) gives positive eigenvalues \(m_i^2\), with physical couplings \(g_i=4(O^Tb)_i\). Therefore

\[
a_X=\sum_i\frac{g_i^2}{32m_i^2}.
\]

This expression accounts for the scalar mass mixing already allowed by C1. Its cubic scalar terms and \(X\varphi_i\varphi_j\) interactions do not change the leading \(X^2\) coefficient around the origin; they enter at higher field order. The stated result uses a flat, fixed metric and vanishing second-gauge-field background.

For a slowly varying probe in a transverse magnetic field, the scalar part of the difference between the perpendicular and parallel refractive indices is

\[
\Delta n_{\rm scalar}=16a_XB^2+\text{higher-order terms}.
\]

Thus a real measurement of a resolved scalar's mass and coupling would predict an equality for a one-mode model, or a lower bound on the leading coefficient for the positive-mass multimode branch. In practice, that comparison must include uncertainty and account for ordinary quantum-electrodynamic, material and instrumental responses. A raw measured refractive-index difference is not automatically the scalar contribution.

The regimes must be kept separate. Producing an on-shell scalar in photon regeneration requires probe energy above its mass. Replacing the scalar with a local \(X^2\) interaction requires the relevant frequencies and momentum transfers well below the masses integrated out. The same optical run cannot simply be described by both approximations at once.

## Why this does not establish EFMW-specific physics

The scalar action used here occurs in the prior literature. Biggio, Massó and Redondo, Section 2, equations (1)–(3), write the same kinetic, mass and scalar–photon terms, with convention differences. The OSQAR paper uses the same scalar interaction in its equation (2) and the corresponding conversion probability in equation (3). See [the first paper](https://arxiv.org/pdf/hep-ph/0604062) and [the OSQAR paper](https://arxiv.org/pdf/1506.08082).

Our matching and birefringence relation are consequences of that shared action. They cannot discriminate two theories that specify identical dynamics, boundary conditions and observables in this domain. This is an equivalence conclusion about an explicit comparison class, not a claim to have ruled out every conceivable alternative or every future EFMW formulation.

Free parameters do not make a model untestable. Measurements can constrain them, and independent observables can test relationships such as the one derived here. The missing step for a distinctive EFMW claim is an independently justified additional restriction or physical structure that changes a prediction relative to the matching scalar baseline.

## What the wider source check found

| Source examined | Relevant content | Limitation for the present target |
| --- | --- | --- |
| C1 action and its historical predecessor | Explicit independent coupling slots; canonical fields and a versioned action | No equation ties a scalar mass to its photon coupling |
| Canonical 102 equations and ME-002 record | A separate alpha-dependent scalar equation; recursive and gravitational proposals | Parameter names do not establish a physical normalization or identify this scalar with the C1 optical mode |
| EFMW-Constants-Problem README, dependency map, boundary record and Lean core | Standard constant identities and conditional algebraic theorems | No independent derivation of the target numerical constant; the Lean file was read, not newly compiled |
| Base888-Quantum-Geometry README | Finite geometry implementation and explicit boundaries on physical claims | README screening did not establish a map from its register structure to C1 mass and coupling |
| Standard-Model-Reduction README | Standard Model rewriting with parameters retained and limitations recorded | No reduction supplies the missing C1 mass–coupling condition |
| C1Q model record | A separately selected quadratic cosmology branch | Its selected mass scale is a model assumption, not an EFMW derivation of the optical coupling |

This is a bounded source audit. It is not an exhaustive theorem about everything ever written under the EFMW name. Complete file identities and the degree of review are in [the source manifest](sources/CONNECTOR_SOURCES.json).

## Status after this work

We have a sharper, falsifiable conditional model relationship and explicit proofs that several appealing shortcuts do not follow from the present inputs. We have no new physical observation, no new independent replication, and no EFMW-exclusive prediction from this audit. The gap to physical confirmation therefore remains open.

The next evidential step is to obtain independently calibrated measurements that can test the surviving relation, or to derive and freeze an additional restriction from a specified new model before examining test data. Choosing a favorable numerical relation and calling it derived would not close the gap.
