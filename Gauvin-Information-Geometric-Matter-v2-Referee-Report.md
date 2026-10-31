# Referee report on information-geometric matter dynamics and gravitational response

**Date:** 31 October 2026  
**Prepared for publication by:** Matthew Chenoweth Wright / Monolithic LLC, with AI-assisted analysis and numerical reproduction.  
**Manuscript author:** Shoshauna Gauvin.  
**Version reviewed:** *Information-Geometric Matter Dynamics and a Dimension-Matched Gravitational Response*, Preprints.org 202609.2275, **version 2**, posted **8 October 2026**. [DOI](https://doi.org/10.20944/preprints202609.2275.v2).  
**Review status:** Public technical commentary in referee-report form; not a journal-appointed review or an editorial decision.

> **Version boundary:** Version 3, titled *Information-Geometric Matter and a Constrained Gravitational Response*, was posted on **30 October 2026**. This report evaluates the specifically selected v2 and its accompanying supplement. It does not evaluate v3's revised construction or claim that the concerns below remain unresolved there. Any formal submission of this report should reconcile it against v3 first. Both versions are identified as preprints, not peer-reviewed articles. [1, 3]

## Assessment and scope

**Recommendation for v2: major revision.** The strongest contribution is a conditional matter model with linked interactions and a defined response relation. The galaxy results do not establish the proposed microscopic explanation of gravity.

The manuscript distinguishes mathematical construction, physical assumptions and observational comparisons with considerable care. It reports failed controls and acknowledges unresolved connections. The recommendation is therefore to preserve and sharpen the conditional theoretical contribution, while narrowing the observational claim and making the numerical work independently executable.

This review covers selected foundational and matching arguments, the interpretation of the SPARC comparisons, and bounded independent arithmetic checks. It is not a verification of every theorem, numerical solver, stability calculation or cosmological result. It does not establish EFMW's superiority or physical validation; the checks use ordinary mathematical and statistical methods.

## 1. The conditional mathematical construction is worth retaining

The author distinguishes three objects that must remain separate: a statistical state manifold, physical spacetime, and fields mapping spacetime into that manifold. The paper supplies a Lorentzian metric and chooses an Einstein-coupled nonlinear sigma-model action. It acknowledges that relative entropy alone does not uniquely determine this physical action. It also recognizes that a positive, rank-at-most-two statistical pullback cannot itself be the four-dimensional Lorentzian metric. These are substantive strengths. [1, sections 2.3–2.6]

The resulting nonrelativistic contacts satisfy

$$\Lambda_p+3\Lambda_\times-4\Lambda_2=0.$$

The internal-response coefficients satisfy a further potentially discriminating relation,

$$192\mathcal P-45\mathcal S^2+40\mathcal S+100=0.$$

Exact rational spot checks at four reference-state ratios, $r_*=7/10,4/5,9/10,99/100$, reproduce both identities. Twelve exact rational checks of the quartic positive-completion formula also pass. These support the printed algebra; they are not a general symbolic proof or verification of every truncation assumption. [1, equations 35, 38 and 54]

The important scientific opportunity is that linked contacts restrict a model more than an arbitrary fitted density profile. An empirical test must actually constrain those contacts or their response relation. A successful fit to an insensitive observable does not accomplish that.

**Requested revision:** Make the linked interaction and dispersion relations the primary theoretical claims, with their finite-amplitude, nonrelativistic and occupied-state assumptions attached to each proposed observable.

## 2. The extreme null bound reproduces, but has a narrow interpretation

The supplement defines

$$T=\max(0,Q_0-Q_1),$$

where $Q_0$ measures standardized residuals against fixed baryon-only predictions and $Q_1$ measures residuals against the alternative. Assuming each standardized null residual has a standard Gaussian marginal, it derives

$$p_G(t)=\min\left\{1,n\,\operatorname{erfc}\!\left(\sqrt{\frac{t}{2n}}\right)\right\}.$$

This is a valid union-bound construction under its premises: $T\ge t$ implies $Q_0\ge t$, which requires at least one standardized squared residual to be at least $t/n$. It does **not** require independent residuals or joint Gaussianity. Because the only essential property of the alternative is $Q_1\ge0$, fitting that alternative does not by itself invalidate this particular conservative inequality. It also does not turn the alternative into an independently validated prediction. [2, section S16 D, equations S134–S136]

Using the reported aggregate values $n=3389$, $Q_0=1960465.195407$ and $Q_1=20805.852268$ reproduces:

| Calculation | Independent evaluation |
|---|---:|
| Gaussian-marginal probability bound | $5.89435\times10^{-123}$ |
| Two-sided normal-equivalent bound | $Z_G=23.5820$ |
| Bound using only null means and variances | $0.00174721$ |
| Alternative standardized residual RMS | $2.47775$ |

These are **aggregate arithmetic reproductions**, not an independent rerun of 175 galaxy fits or an audit of all underlying observations and predictions. The first two values reproduce the supplement's conservative rounding.

The warranted conclusion is that the specified fixed baryon-only model and error assumptions fail badly. It does not identify the alternative's microscopic mechanism. Rejecting baryon-only gravity is not rejecting GR with dark matter, nor demonstrating superiority over a dark-matter halo model. The enormous Gaussian-equivalent number depends strongly on the assumed marginal tails and fixed source calibration; arbitrary residual dependence is allowed, but uncertain null means and incorrect marginal error scales are not thereby covered.

The author states these limitations explicitly in the supplement and discussion. The opening abstract should give them equal prominence and avoid allowing a reader to interpret $Z\ge23$ as a discovery significance for the information-geometric mechanism. The alternative standardized RMS above is a residual diagnostic, not a calibrated goodness-of-fit probability. [1, abstract and section 7; 2, Table S2]

**Requested revision:** Lead with the conditional null being rejected, distinguish this bound from model preference and predictive validation, and propagate source-calibration and error-model uncertainty in the comparative analysis.

## 3. The connection from matter dynamics to modified gravity remains open

The paper contains two distinct constructions: an information-geometric matter model coupled to Einstein gravity, and an additional AQUAL-like gravitational response motivated by separate symmetry, horizon and entropy assumptions. The first does not yet derive the second. The manuscript appropriately identifies missing ingredients: an occupied state, an acceleration observable, response normalization, and a consistent gravitational completion. [1, sections 5.5–5.8]

Its Gaussian calculation produces a cubic entropy cost at criticality, with a quadratic correction at finite correlation length. Three independent numerical substitutions reproduce the stated Legendre-transform expression. This is useful mathematical evidence for the specified continuum example.

But a one-sided scalar variance-deficit cost is not automatically a local gravitational action. The identification

$$d_v=q_*\,|\nabla\Phi|/a_*$$

is an additional physical map. Establishing it, including its normalization and local regime of validity, is a central research obligation. The manuscript itself recognizes this distinction. Its required subtraction of the existing Einstein quadratic gradient term also needs a physical derivation within a common conserving completion; simply adding a cubic cost to unchanged Einstein gravity would give a different low-field response. [1, equations 97 and 104–109]

The conformally invariant $p=d$ field equation has established antecedents in Milgrom's work. Recovering its flat spherical rotation curves is a correspondence result. The possible novelty lies in deriving a physical origin or a discriminating correction, and should be presented in those terms. [4]

**Requested revision:** Either derive the matter-to-gravity map in a specified state or present the two constructions as separate conditional results, without using the galaxy fit as evidence that the missing map has been established.

## 4. The galaxy calculations scarcely constrain the distinctive contact interaction

With the selected matter-model states held fixed, switching off the contact interaction changes mean outer loss from approximately

$$54.057382\quad\text{to}\quad54.057392.$$

The reported relative change is only **0.0000178%**. Doubling the interaction produces a similarly small change in the opposite direction. These are controls of the original matter-state comparison, not the separate infrared comparison with outer loss near seven. The supplement explicitly concludes that the present rotation comparison does not identify the contact coefficient or linked internal stiffnesses. [2, Table S3 and section S17 A]

This is a major identifiability limitation because those linked interactions are among the most distinctive theoretical results. A fit that scarcely changes when the interaction is removed cannot validate that interaction. The author deserves credit for retaining this control rather than presenting fit improvement alone as microscopic evidence.

A stronger test would measure enough of the internal dispersion relation to constrain its polynomial coefficients, with density and normalization independently determined. The manuscript also reports that its illustrative maximal distinction lies at a scale and period outside a local galactic interpretation, so practical observability needs a separate assessment. [1, sections 3.4 and 6.1]

**Requested revision:** State prominently that the existing rotation data do not identify the proposed contact structure, and prioritize a feasible observable with demonstrated sensitivity to that structure.

## 5. The response floor is useful mathematically but unestablished observationally

For the finite-floor spherical response, the paper derives

$$\max_R\frac{d\log v_c}{d\log R}=-\frac{\sqrt{\epsilon}}2.$$

Five substitutions at positive floor values reproduce the formula at its proposed extremum. It describes an approximately flat interval followed eventually by a Keplerian decline, under the stated isolated compact spherical-source assumptions. This is not a statement about arbitrary disks or external fields. [1, equations 110–112]

The observational gain is negligible:

- Outer velocity RMS changes from **11.4126 to 11.4042 km/s**, about **0.074%**.
- The conditional paired comparison gives **$p=0.9242$**.
- Allowing a separate floor for each galaxy improves the inner fit but worsens outer prediction.

The manuscript reports these adverse outcomes clearly. They support retaining the floor as a theoretical possibility, not claiming its detection. [1, section 6.4]

**Requested revision:** Preserve the null result and distinguish the mathematical regularization from evidence for a nonzero physical correlation gap.

## 6. Geometry, outer mass and computational reproducibility

The galaxy calculation uses an algebraic radial-force surrogate. The author correctly explains why it generally does not solve the nonlinear disk field equation: the algebraic candidate can have nonzero curl. Full disk and environmental boundary-value calculations are needed before attributing residual differences to the constitutive law. The stated galactic interpolation also requires a separate high-field completion before planetary extrapolation. [1, section 5.5]

The matter-model extrapolations require additional scrutiny: **14 selected states have total inventories above $10^{14}M_\odot$**. Some place almost all their mass beyond the observed rotation-curve interval. These are reported model extrapolations, not measured halo masses. Independent lensing, satellite, escape-speed and environmental constraints are essential. [2, section S17 B]

The supplement describes substantial computational work, but this review did not locate a public executable archive in the inspected materials. This is an access/reproducibility limitation, not an assertion that no code exists. A reviewable release should contain fitted nuisance parameters, row-level predictions, masks, input hashes, solver settings and commands reproducing each principal table. The original SPARC catalogue is public, but access to the source catalogue alone does not reproduce the author's fitted pipeline. [2; 5]

**Requested revision:** Release the computational record, quantify disk-surrogate error, and test the inferred outer inventories against independent observations.

## Reproduction materials and limits

- [Independent check script](Gauvin-Information-Geometric-Matter-v2-Checks.py)
- [Recorded numerical output](Gauvin-Information-Geometric-Matter-v2-Checks.json)

Run with Python 3 and its standard library:

```bash
python3 Gauvin-Information-Geometric-Matter-v2-Checks.py
```

The script includes exact rational spot checks of the two coefficient relations and quartic completion, floating-point checks of the Gaussian Legendre expression and floor slope, and recomputation of the reported aggregate probability bound. It also reproduces the horizon acceleration normalization at the stated $H_0$. No new SPARC fit, full dynamical simulation, general theorem proof or empirical mechanism test is performed.

## Editorial conclusion

Retain the conditional matter theory and its testable interaction relations; narrow the observational claim. Before acceptance, require a reproducible computational release and a clearer separation between established AQUAL behavior, the proposed information-geometric origin, and what SPARC actually constrains.

The willingness to report failed controls and unresolved connections is a strength. The next decisive step is to test a prediction that changes when the distinctive microscopic structure changes, rather than obtain another improvement over a baryon-only baseline. This recommendation is specific to v2 and should not be read as an assessment of the already-posted v3.

## References

1. Shoshauna Gauvin. *Information-Geometric Matter Dynamics and a Dimension-Matched Gravitational Response*. Preprints.org 202609.2275, version 2, posted 8 October 2026. [Version-specific page](https://www.preprints.org/manuscript/202609.2275/v2); [DOI](https://doi.org/10.20944/preprints202609.2275.v2).
2. Gauvin. *Supplemental Material: Information-geometric matter dynamics and a dimension-matched gravitational response*. [Supplement associated with v2](https://www.preprints.org/frontend/manuscript/893d84776e7805e03f0fb46f9d32f88e/download_pub/supplementary), 50 pages. This report uses the supplement's printed section numbering, including S16 D and S17; several main-text supplement cross-references use different numbering and should be reconciled.
3. Gauvin. *Information-Geometric Matter and a Constrained Gravitational Response*. Version 3, posted 30 October 2026. [Version-specific page](https://www.preprints.org/manuscript/202609.2275/v3). Cited only for version awareness; its revised construction is outside this review.
4. Mordehai Milgrom. *Nonlinear conformally invariant generalization of the Poisson equation to D > 2 dimensions*. Physical Review E **56**, 1148–1159 (1997). [DOI](https://doi.org/10.1103/PhysRevE.56.1148); [author preprint](https://arxiv.org/abs/gr-qc/9705003).
5. Federico Lelli, Stacy S. McGaugh and James M. Schombert. *SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves*. Astronomical Journal **152**, 157 (2016). [DOI](https://doi.org/10.3847/0004-6256/152/6/157); [author preprint](https://arxiv.org/abs/1606.09251).
