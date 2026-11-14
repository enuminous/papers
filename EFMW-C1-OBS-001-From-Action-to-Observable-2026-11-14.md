# EFMW-C1-OBS-001: from the C1 action to an optical observable

**Publication:** [Preserved research package](research/efmw-c1-obs-001/README.md) · [Code and results](research/efmw-c1-obs-001/) · [Download ZIP](research/efmw-c1-obs-001/EFMW-C1-Observable-2026-11-14.zip) · [Publication record](research/efmw-c1-obs-001/PUBLICATION_NOTICE.md)

Version 0.1.0 • 14 November 2026  
Prepared for Matthew Chenoweth Wright / Monolithic LLC with AI assistance.

**Outcome:** a conditional optical prediction has been derived from an existing C1 coupling. The restricted model is identical to an established scalar–photon model. This is a mathematical bridge and a translation of an existing experimental constraint, not a new physical detection or a unique EFMW prediction.

## 1. Source and scope

The source is EFMW-LAGRANGIAN-C1 v1.0.0 at commit:

$$
\texttt{83f9d2ec03e055c6cd09aa6359189161ad1571f6}.
$$

The three archived source files match their upstream Git blob hashes. The scope was locked locally after initial source and literature screening and before the symbolic checks and numerical calculation. It was not registered with an independent custodian.

C1 uses signature $(-+++)$, $\hbar=c=1$, and

$$
\Box=\nabla^2-\partial_t^2.
$$

Its scalar fields are neutral real fields. Its pair couplings are independent constants, not measured values or numerical predictions.

The source-free C1 action does not itself describe laboratory coils, laser preparation, charged detector matter, an opaque barrier or calibration electronics. Here these are explicitly characterized external apparatus. Identifying its M-sector gauge field with ordinary laboratory electromagnetism is an additional physical interpretation.

The result is therefore a **bulk-action-to-field prediction plus an assumed calibrated readout**, not a derivation of a complete detector from C1.

## 2. The coherence-memory branch does not close

The earlier hypothesis was

$$
\tau_M\dot M=C-M,\qquad R=\kappa CM.
$$

C1 supplies neither this relaxation law nor an operational map from its fields to these C and M variables. Its conventions explicitly exclude relaxation equations without a defined action. The source-free action also supplies no force-transducer matter action.

There is a direct obstruction to claiming that C1 requires a nonzero extra force: its independent couplings may all be zero. With the additional scalars unexcited, that allowed restriction produces ordinary source-free Maxwell dynamics on the prescribed background. C1 therefore cannot entail a nonzero new coupling for every allowed parameter choice.

This does not prove that no extension could produce a memory law. A bath, coarse-graining or further interaction could do so, but its definitions and approximation would have to be supplied and audited. They cannot be added after the fact and called consequences of the pinned action.

**Decision:** the claim that the existing CM force law has been derived from C1 is unsupported. Its physical possibility remains unresolved. We retained this failed route and examined a coupling actually present in the action.

## 3. Restrict C1 before variation

Keep the M-sector gauge field $F_{\mu\nu}$ and one scalar

$$
\sigma=\varphi_W.
$$

Set the other fields and all other pair/triple couplings to zero, keep a positive scalar mass $m$, and work on fixed Minkowski space. This is an explicitly chosen subfamily of C1, not an added interaction.

Write $c_{MW}$ for the source coefficient named $g_{MW}$, to avoid confusing it with the conventional photon coupling. Since $Q_M=X=F_{\mu\nu}F^{\mu\nu}$ and $Q_W=\sigma$, the retained potential is

$$
U=\frac12m^2\sigma^2+c_{MW}\sigma X.
$$

Define

$$
g=4c_{MW}.
$$

Then

$$
\boxed{\mathcal L
=-\frac14(1+g\sigma)F_{\mu\nu}F^{\mu\nu}
-\frac12\partial_\mu\sigma\,\partial^\mu\sigma
-\frac12m^2\sigma^2.}
$$

No numerical value for g or m follows from this restriction.

In four dimensions the mass dimensions are
$[\sigma]=1,\ [F_{\mu\nu}]=2,\ [m]=1,\ [g]=[c_{MW}]=-1$.
Every displayed Lagrangian term has dimension four.

## 4. Vary the action

For compactly supported variations, integration by parts gives

$$
\delta_\sigma S
=\int d^4x\left[
\Box\sigma-m^2\sigma-\frac g4F_{\mu\nu}F^{\mu\nu}
\right]\delta\sigma.
$$

Thus

$$
\boxed{(\Box-m^2)\sigma=\frac g4F_{\mu\nu}F^{\mu\nu}.}
$$

Gauge variation gives

$$
\boxed{\partial_\mu[(1+g\sigma)F^{\mu\nu}]=0,}
\qquad
\partial_{[\lambda}F_{\mu\nu]}=0.
$$

The coefficient factor of four is important: comparison with a published limit on g requires $c_{MW}=g/4$, not $c_{MW}=g$.

The source's prescribed-current exclusion is respected. The applied magnetic field is a background maintained by apparatus outside the source-free interaction region; arbitrary currents are not inserted into these equations to obtain a desired answer.

## 5. Background and validity conditions

Use a static transverse magnetic field $\mathbf B_{\rm ext}=B\hat x$. A nonzero magnetic field sources a static scalar background. It is inconsistent to call $\sigma=0$ an exact background when $gB\ne0$.

For a homogeneous reference region and $m>0$,

$$
-m^2\sigma_0=\frac g2B^2,\qquad
\sigma_0=-\frac{gB^2}{2m^2}.
$$

A finite magnet requires the solution of the corresponding boundary-value problem. The homogeneous expression is a local reference, not an exact solution for a finite apparatus.

We work to leading order in small coupling and weak optical perturbations, with

$$
|g\sigma_0|\ll1,\qquad 1+g\sigma>0,
\qquad m/\omega\ll1,\qquad |gB|/\omega\ll1.
$$

The positive gauge factor is essential. On that branch, the classical energy density can be written as positive scalar terms plus
$(1+g\sigma)(E^2+B^2)/2$.
The action is not globally stable over unrestricted scalar values: for example, $\sigma=-2/g$ gives a negative gauge factor. We do not repair that by silently replacing the source action.

All original scalar cubic couplings are zero in this restriction. That removes those particular cubic instabilities, but does not establish global stability of the full C1 family or a quantum ultraviolet completion.

Terms proportional to $g\sigma_0$ change the quadratic photon normalization at higher order. They are neglected only in the stated weak-background expansion. A real apparatus must validate the boundary solution and corrections before using a precision prediction.

## 6. Polarization and the quadratic wave equations

Let light propagate along $+\hat z$. For the interacting polarization take the wave potential $A_y=A(t,z)$. Its electric field is along y and its wave magnetic field is along x:

$$
E_y=-\dot A,\qquad b_x=-A'.
$$

Here prime means $\partial_z$. Write $\sigma=\sigma_0+s$. After subtracting the background equation and retaining quadratic optical terms at leading order in the weak-background expansion,

$$
\mathcal L_2
=\frac12(\dot A^2-A'^2)
+\frac12(\dot s^2-s'^2-m^2s^2)
+gB(z)sA'.
$$

The two equations are

$$
\ddot A-A''+g[B(z)s]'=0,
$$

$$
\ddot s-s''+m^2s-gB(z)A'=0.
$$

The derivative of B must be retained at field fringes. Omitting it in a nonuniform-field calculation would alter the matching problem.

For the other photon polarization, the wave magnetic field is orthogonal to the applied magnetic field and the displayed scalar mixing term vanishes. Therefore the scalar channel selects

$$
\boxed{\mathbf E_{\rm light}\perp\mathbf B_{\rm ext}.}
$$

This is the scalar selection rule. The frequently discussed pseudoscalar interaction uses the dual field strength and has a different polarization rule; that operator is not the selected C1 term.

## 7. Bulk dispersion check

For constant B, substitute $A,s\propto e^{i(kz-\omega t)}$. The equations become

$$
\begin{pmatrix}
\omega^2-k^2 & -igBk\\
igBk & \omega^2-k^2-m^2
\end{pmatrix}
\begin{pmatrix}A\\s\end{pmatrix}=0.
$$

The bulk dispersion relation is

$$
\boxed{(\omega^2-k^2)(\omega^2-k^2-m^2)-g^2B^2k^2=0.}
$$

This check keeps the spatial derivative characteristic of scalar mixing. It is performed before making the relativistic forward-wave approximation.

## 8. Forward propagation

Write the slowly varying amplitudes as

$$
A=a(z)e^{i(\omega z-\omega t)},\qquad
s=s_e(z)e^{i(\omega z-\omega t)}.
$$

Neglect the second derivatives of the envelopes and subleading relativistic corrections. Rephase the scalar amplitude by $\chi=i s_e$. Then

$$
i\frac d{dz}
\begin{pmatrix}a\\\chi\end{pmatrix}
=
\begin{pmatrix}
0&\Delta_B\\
\Delta_B&q
\end{pmatrix}
\begin{pmatrix}a\\\chi\end{pmatrix},
\qquad
\Delta_B=\frac{gB}{2},\quad q=\frac{m^2}{2\omega}.
$$

This matrix is Hermitian. The sum of the two forward-mode flux fractions is conserved within this approximation. It is not a solution of the full nonlinear C1 equations at arbitrary frequency or field strength.

For a uniform length L and initial state $(1,0)$, diagonalization yields

$$
P_{\gamma\to\sigma}
=\frac{4\Delta_B^2}{q^2+4\Delta_B^2}
\sin^2\!\left(\frac L2\sqrt{q^2+4\Delta_B^2}\right).
$$

This expression is exact for the displayed two-mode equation. It is only approximate relative to the original field theory.

In the weak-conversion limit,

$$
\boxed{
P_{\gamma\to\sigma}
\simeq
\left(\frac{gBL}{2}\right)^2
\operatorname{sinc}^2\!\left(\frac{m^2L}{4\omega}\right),
\qquad \operatorname{sinc}x=\frac{\sin x}{x}.}
$$

Equivalently, the leading conversion amplitude is proportional to

$$
\frac g2\int_0^L B(z)e^{iqz}\,dz.
$$

This form shows why measured field profiles, gaps and reversals matter. The uniform-field sinc factor is not universal for an arbitrary magnet.

The exact free kinematic mismatch is
$q_{\rm kin}=m^2/(\omega+\sqrt{\omega^2-m^2})$.
Using $m^2/(2\omega)$ also requires that the accumulated mismatch error $|q_{\rm kin}-q|L$ be small. That error is recorded for every point in the numerical scan.

## 9. From conversion to a detector prediction

Consider two separated magnetic regions with lengths $L_1,L_2$ and fields $B_1,B_2$. An opaque barrier removes the ordinary photon beam between them. Assume that the scalar is transmitted through the barrier and remains coherent over the path.

The first region produces a scalar amplitude and the second regenerates light. For a single pass,

$$
P_{\rm reg}\simeq P_1P_2.
$$

Let $\theta$ be the input electric-polarization angle relative to $\mathbf B_1$. A detector collecting the regenerated polarization, without an additional analyzer, has expected signal

$$
\boxed{
N_{\rm sig}=
\eta N_{\rm in}\sin^2\theta
\left(\frac{gB_1L_1}{2}\right)^2
\left(\frac{gB_2L_2}{2}\right)^2
\operatorname{sinc}^2\!\left(\frac{m^2L_1}{4\omega}\right)
\operatorname{sinc}^2\!\left(\frac{m^2L_2}{4\omega}\right).}
$$

Here $N_{\rm in}=P_{\rm laser}T/\omega$ in natural units and η is the probability that a regenerated photon is recorded. In SI calculations the photon energy in the denominator is $\omega_{\rm eV}\times1.602176634\,10^{-19}$ joule.

An output analyzer would add its own projection factor. The stated sin² law does not include one.

This gives falsifiable relations in the regime of validity:

- At fixed mass and apparatus, doubling the coupling multiplies the signal by 16.
- Halving both magnetic fields reduces it to 1/16.
- Halving just the production field reduces it to 1/4.
- Rotating the input from perpendicular to 45 degrees halves it; parallel input suppresses this leading scalar signal.
- The weak-limit coherence nodes occur at $m_n^2L/(4\omega)=n\pi$ for equal magnets.

These are conditional predictions of the selected model. They are not unique EFMW signatures.

## 10. A numerical illustration

The illustration uses magnetic/optical geometry reported by OSQAR: 9 T and 14.3 m per region, 532 nm light and 18.5 W input power. We independently choose

$$
g=10^{-8}\ {\rm GeV}^{-1},\qquad m=10^{-4}\ {\rm eV}.
$$

These parameter values were not derived from EFMW and are not asserted to be allowed by every existing constraint. Assume perpendicular input, one hour, unit detection efficiency and no optical enhancement.

The calculation gives:

| Quantity | Conditional value |
| --- | ---: |
| Photon energy | 2.33053 eV |
| Single conversion probability | $4.05031\times10^{-13}$ |
| Regeneration probability | $1.64050\times10^{-25}$ |
| Ideal expected signal per hour | 0.0292608 recorded photons |
| First weak-limit coherence zero | $6.35708\times10^{-4}$ eV |
| Homogeneous-reference $|g\sigma_0|$ | $1.55\times10^{-20}$ |

A mean of three ideal signal photons would require about 102.5 hours at this chosen point. This is not a discovery exposure: it omits real background, detector inefficiency, acquisition loss and nuisance uncertainty.

The program also reports the ideal one-sided Poisson upper bound for zero counts with known zero background. That is a mathematical illustration, not a reconstruction of OSQAR's detector or likelihood.

The unit conversion was checked from energy density:
$B_{\rm nat}^2/2=B_{\rm SI}^2( \hbar c)^3/(2\mu_0\,{\rm eV}_{J})$.
The code uses the explicitly stated approximation $\mu_0=4\pi10^{-7}$, giving $1\,{\rm T}\simeq195.353\,{\rm eV}^2$.

## 11. Comparison with existing physics

The interaction $-g\sigma F_{\mu\nu}F^{\mu\nu}/4$ is the standard scalar–photon operator. Substituting $g=4c_{MW}$ makes the restricted C1 Lagrangian identical to that model. The symbolic checker verifies the identity.

Consequently, any experiment confined to this restricted model, with the same apparatus assumptions, has the same predictions under both names. It cannot identify the EFMW label as the cause. This equivalence is a positive mathematical result and a negative uniqueness result.

A primary theoretical comparison is the scalar section of Biggio, Massó and Redondo [B]. Their analysis also distinguishes the scalar spatial-derivative mixing from the pseudoscalar case. We retain the relativistic scope instead of treating the simpler formula as universally exact.

## 12. An existing experimental constraint already applies conditionally

Ballou et al. [O] report a scalar coupling limit $g<3.2\times10^{-8}\ {\rm GeV}^{-1}$ at their reported 95% level for $m<2\times10^{-4}$ eV. Their published inference uses a posterior construction; we preserve their confidence label without claiming to recompute it.

Under the one-scalar, unscreened, matching-apparatus assumptions above, the C1 parameter mapping gives

$$
\boxed{|c_{MW}|<8.0\times10^{-9}\ {\rm GeV}^{-1}.}
$$

This is a translation of the published result, not new data analysis, not a claim about today's strongest bound, and not an exclusion of the full C1 family.

## 13. What is established

| Statement | Status | Evidence |
| --- | --- | --- |
| The selected C1 term gives scalar–photon mixing | Demonstrated under stated restrictions | Variation and quadratic wave equations |
| The displayed optical formula follows in the stated approximation | Demonstrated conditionally | Diagonalization, amplitude integral and numerical agreement |
| The selected branch is equivalent to the known scalar–photon model | Demonstrated | Exact Lagrangian identity |
| The chosen illustrative signal exists in nature | Unresolved | No physical data were acquired |
| C1 predicts the chosen g or m | Rejected | These remain independent input parameters |
| The original CM force law follows from the supplied C1 specification | Unsupported / unresolved bridge | Missing variables, source and relaxation derivation |
| This is a uniquely EFMW observable | Rejected for this restricted branch | An identical comparator has identical predictions |
| The full C1 family is disproved by the published scalar limit | Rejected | Zero/smaller couplings and other sectors remain in the family |

The derivation milestone is complete for this branch. A distinctive EFMW claim would need additional, independently justified quantitative restrictions that are absent from the pinned family—for example a predicted mass–coupling relation or a linked observable not shared by the comparator. Inventing such a restriction to fit an outcome would not establish it.

## References

[C1] [Pinned candidate action](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md), with conventions and derivation archived in this package.

[O] Ballou et al., OSQAR Collaboration, *Physical Review D* **92**, 092002 (2015), [doi:10.1103/PhysRevD.92.092002](https://doi.org/10.1103/PhysRevD.92.092002), [versioned preprint](https://arxiv.org/abs/1506.08082v2). Used for interaction convention, geometry and the published limit.

[B] Biggio, Massó and Redondo, [hep-ph/0604062v2](https://arxiv.org/pdf/hep-ph/0604062), section 2. Used for comparison with the established scalar model and approximation scope.

Numerical outputs are in [the results directory](research/efmw-c1-obs-001/results/). No full Zoo executable, Lean proof, hardware experiment or independent replication was run.

