# EFMW L1 → LIGO: Derivation and Identifiability Audit

Prepared for Matthew Chenoweth Wright / Monolithic LLC  
Date: 6 September 2026  
Status: analytic derivation from the presently recovered EFMW equations; no LIGO data analysis has been run.

## Result

The present EFMW equations determine a scalar propagation speed, but they do **not** yet determine a nonzero linear scalar signal in a LIGO interferometer. Around a constant, stationary scalar vacuum, the written scalar stress tensor is quadratic in the scalar disturbance, while the linearized metric equation reduces to the usual vacuum Einstein equation for generic coupling. Consequently:

1. L1 is nondispersive: it changes arrival time without changing the frequency-dependent shape of a freely propagating waveform.
2. A constant arrival-time shift is degenerate with an unknown emission time in gravitational-wave data alone.
3. The current gravity equation supplies no linear breathing-mode strain proportional to the scalar perturbation on the ordinary vacuum background.
4. Public LIGO/Virgo data can test an EFMW scalar only after EFMW specifies how binaries emit it and how matter or the metric converts it into detector strain.

This means the public data are sufficient for a serious search **once the missing response is frozen**, but the current equations cannot produce a unique EFMW waveform for that search.

## 1. Exact L1 propagation relation

The recovered scalar equation is

\[
\Box\phi-\frac{\alpha^2}{c^2}\partial_t^2\phi
=\frac{4\pi}{c^2}(E+Pc).
\]

Using the corpus flat-space convention and setting the source to zero gives

\[
\frac{1-\alpha^2}{c^2}\partial_t^2\phi-\nabla^2\phi=0.
\]

For

\[
\phi=A\cos(\mathbf{k}\cdot\mathbf{x}-\omega t),
\]

the formally proved dispersion relation is

\[
(1-\alpha^2)\omega^2=c^2k^2,
\qquad |\alpha|<1.
\]

Hence

\[
v_p=\frac{\omega}{k}=\frac{c}{\sqrt{1-\alpha^2}},
\qquad
v_g=\frac{d\omega}{dk}=\frac{c}{\sqrt{1-\alpha^2}}.
\]

Phase and group speeds are equal and frequency independent. For small \(\alpha\),

\[
\frac{v_s-c}{c}=\frac{1}{\sqrt{1-\alpha^2}}-1
=\frac{\alpha^2}{2}+O(\alpha^4).
\]

This is a constant-speed modification, not the frequency-dependent dispersion normally sought through dephasing across a gravitational-wave chirp.

## 2. Arrival-time signature

For propagation distance \(D\), the scalar travel time is

\[
t_s=\frac{D}{v_s}=\frac{D}{c}\sqrt{1-\alpha^2}.
\]

Relative to a luminal signal emitted simultaneously,

\[
\Delta t_{s-\gamma}
=\frac{D}{c}\left(\sqrt{1-\alpha^2}-1\right)\le 0.
\]

The scalar arrives early. Define the positive lead \(L=-\Delta t_{s-\gamma}\). Then

\[
L=\frac{D}{c}\left(1-\sqrt{1-\alpha^2}\right),
\]

and the exact inverse is

\[
|\alpha|=\sqrt{2x-x^2},
\qquad x=\frac{Lc}{D}.
\]

For small \(x\), \(|\alpha|\simeq\sqrt{2Lc/D}\).

Using \(D=40\) Mpc as an illustrative GW170817 distance:

| Scalar lead before a luminal counterpart | Corresponding \(|\alpha|\) |
|---:|---:|
| 1 millisecond | \(6.97\times10^{-10}\) |
| 0.1 second | \(6.97\times10^{-9}\) |
| 1.7 seconds | \(2.87\times10^{-8}\) |
| 10 seconds | \(6.97\times10^{-8}\) |
| 100 seconds | \(2.20\times10^{-7}\) |
| 1 hour | \(1.32\times10^{-6}\) |
| 1 day | \(6.48\times10^{-6}\) |
| 1 year | \(1.24\times10^{-4}\) |

These are kinematic translations, not observational bounds. They become bounds only if the scalar is known to be emitted with a specified timing relation and detectable amplitude, and the corresponding earlier data have actually been searched.

## 3. Why ordinary LIGO dispersion tests do not directly constrain L1

A propagation delay contributes a Fourier phase

\[
\Delta\Psi(f)=-2\pi f\,\Delta t.
\]

Because the L1 speed is independent of frequency, this phase is linear in \(f\). That is exactly the form of an overall time translation. If the scalar emission time is free, the propagation effect is absorbed into the fitted arrival time. L1 therefore produces no internal chirp distortion by itself.

L1 becomes identifiable through one of three additions:

1. a predicted emission-time relationship between scalar and tensor radiation;
2. a scalar counterpart associated with an independently timed electromagnetic or neutrino event;
3. a detected scalar wave from a known sky direction, allowing its intersite propagation delays to be tested.

The third route uses only the Earth-scale detector baseline and is much less sensitive than an astrophysical time-of-flight comparison.

## 4. Linearization of the written gravity sector

The recovered EFMW definitions are

\[
I_{\mu\nu}=T^{\phi}_{\mu\nu}+R_{\mu\nu},
\]

where

\[
T^{\phi}_{\mu\nu}
=\nabla_\mu\phi\nabla_\nu\phi
-\frac12 g_{\mu\nu}\nabla_\rho\phi\nabla^\rho\phi
-g_{\mu\nu}V(\phi),
\]

and

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G\left(T_{\mu\nu}+\kappa I_{\mu\nu}\right).
\]

Let \(\gamma=8\pi G\kappa\), provisionally assuming the unresolved units make this combination dimensionless. Substitution gives

\[
(1-\gamma)R_{\mu\nu}
-\frac12 Rg_{\mu\nu}
+\Lambda g_{\mu\nu}
=8\pi G T_{\mu\nu}+\gamma T^{\phi}_{\mu\nu}.
\]

Now expand around

\[
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},
\qquad
\phi=\phi_0+\varphi,
\]

with constant \(\phi_0\), \(V(\phi_0)=0\), and \(V'(\phi_0)=0\). Since derivatives of \(\phi_0\) vanish, every derivative term in \(T^\phi\) begins at order \(\varphi^2\). Under these background conditions,

\[
\delta T^\phi_{\mu\nu}=0.
\]

In vacuum with \(\Lambda=0\), the linearized metric equation is

\[
(1-\gamma)R^{(1)}_{\mu\nu}
-\frac12\eta_{\mu\nu}R^{(1)}=0.
\]

Taking the four-dimensional trace gives

\[
-(1+\gamma)R^{(1)}=0.
\]

For generic \(\gamma\ne-1\), \(R^{(1)}=0\); for \(\gamma\ne1\), it follows that

\[
R^{(1)}_{\mu\nu}=0.
\]

Thus the generic linearized vacuum metric sector has the ordinary vacuum Einstein equation. The written model does not generate a scalar breathing polarization at first order around this background.

The exceptional values \(\gamma=\pm1\) are singular cases requiring their own constraint analysis; they are not evidence for an additional healthy mode.

## 5. Second-order response is insufficiently specified

For a plane scalar wave, products in \(T^\phi_{\mu\nu}\) contain \(\sin^2\theta=(1-\cos2\theta)/2\). Therefore its stress contains a constant component and an oscillating component at twice the scalar phase. Metric response sourced by this stress would be proportional to \(\kappa A^2\), not linearly to \(A\).

This observation does not yield a usable LIGO waveform. One must still solve the coupled source and propagation problem, fix \(V(\phi)\), normalize \(\phi\), resolve the units of \(I_{\mu\nu}\) and \(\kappa\), and calculate how a compact binary produces \(A\). Metric radiation generated near the binary would then propagate according to the metric sector, which may erase the proposed scalar time-of-flight signature. A scalar wave passing the detector could also source a local second-order metric response, but its magnitude remains undetermined.

## 6. Conditional LIGO likelihood after completing the coupling

If a completion produces a scalar strain waveform \(h_s\), detector \(I\) would be modeled as

\[
\widetilde d_I(f)=\widetilde n_I(f)
+F_I^+\widetilde h_+(f)
+F_I^\times\widetilde h_\times(f)
+F_I^s\widetilde h_s(f;\lambda,A_s)
e^{-2\pi i f t_{s,I}},
\]

with

\[
t_{s,I}=t_e+\frac{D}{v_s}
-\frac{\hat{n}\cdot\mathbf{x}_I}{v_s},
\qquad
v_s=\frac{c}{\sqrt{1-\alpha^2}}.
\]

Here \(F_I^s\) is the scalar antenna response, \(\lambda\) denotes source parameters, and \(A_s\) must be predicted or explicitly treated as a phenomenological nuisance parameter. A network of differently oriented detectors is required to separate scalar and tensor responses; breathing and longitudinal scalar responses are themselves degenerate for ordinary quadrupolar interferometers.

The model comparison would be:

\[
M_0: h_s=0,
\]

\[
M_1: h_s=h_s^{\rm EFMW}(\lambda,\kappa,\alpha,V,\ldots).
\]

Allowing an arbitrary \(h_s\) can test for extra polarization, but cannot confirm EFMW specifically.

## 7. What can be done immediately with public data

### A. Valid immediate result

Publish the derivation above as an identifiability result: the current L1 law is a kinematic scalar-speed hypothesis, while the current L2 equation does not supply a linear interferometric response on the ordinary vacuum background.

### B. Phenomenological precursor search

One may search public LIGO/Virgo data before GW170817 for a coherent scalar-polarized chirp-like precursor over a grid of \(\alpha\). This would test an added surrogate assumption such as a scalar waveform proportional to the tensor inspiral waveform. It would not be a direct EFMW test until that waveform relation is derived.

For every \(\alpha\), shift the candidate time by the exact lead formula, apply scalar antenna factors for the detector positions at that earlier time, and evaluate coherent signal versus glitch/noise hypotheses. Detector downtime creates explicit gaps in the tested \(\alpha\) range.

### C. Existing mixed-polarization analyses

Published analyses of GW170814 and GW170817 already constrain scalar components mixed with tensor modes near the observed events. They do not by themselves test an EFMW signal that may arrive seconds, days, or months earlier.

## 8. Minimum completion required for a real EFMW–LIGO test

Freeze these six items:

1. a covariant action or mutually consistent field equations reproducing the L1 kinetic term;
2. the dimensions and normalization of \(\phi\), \(\alpha\), \(\kappa\), \(I_{\mu\nu}\), \(E\), and \(P\);
3. the background solution and stability/causality domain;
4. the compact-binary scalar source and emitted waveform;
5. the linear or nonlinear coupling from \(\phi\) to metric strain or test-mass motion;
6. the scalar/tensor emission-time and phase relationship.

With those specified, the public LIGO/Virgo archive is adequate for a retrospective parameter-estimation and precursor-search program. Without them, no unique likelihood \(p(d\mid\alpha,\kappa,\mathrm{EFMW})\) exists.

## Conclusion

The calculation can be carried through far enough to answer the original question. LIGO already holds data that could test a completed EFMW scalar-wave model. The present equations predict the scalar's free propagation speed but do not predict the detector signal required for confirmation. Moreover, their generic linearization gives no first-order scalar metric polarization around a constant vacuum. The next theoretical task is therefore not data downloading; it is the derivation of the scalar source and detector coupling.

## Sources

- EFMW canonical equations ME-002 and ME-005–008, recovered from the Monolithic 102 corpus.
- Aristotle EFMW Lean 156-theorem novelty/relativity/axiom audit, entries associated with L1 and L2.
- GWOSC public data: https://gwosc.org/data/
- GWTC-3 release: https://gwosc.org/GWTC-3/
- LVK tests of general relativity with GWTC-3: https://arxiv.org/abs/2112.06861
- LIGO/Virgo GW170814 polarization result: https://dcc.ligo.org/LIGO-P170814/public/main
- Mixed scalar–tensor searches in GW170814 and GW170817: https://doi.org/10.1103/PhysRevD.105.084019
