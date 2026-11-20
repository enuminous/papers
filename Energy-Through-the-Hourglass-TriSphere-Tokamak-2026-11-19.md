# Energy Through the Hourglass

## A diverted-tokamak analogue for A. Beth Jones’s TriSphere

Matthew Chenoweth Wright · Monolithic LLC · November 19, 2026

### Abstract

A. Beth Jones’s *Universal 13-Layer Tri-Sphere Blueprint* describes a toroidal circulation, an hourglass waist that divides paths, and a return loop that puts material back into circulation. A diverted tokamak offers a physical analogue for those three features. Its magnetic separatrix divides a region of nested toroidal flux surfaces from open field lines that can carry exhaust toward a divertor. This paper turns the comparison into two explicit balances, one for particles and one for energy. The balances show how fuel can return to the plasma while much of the energy carried out with it still leaves as heat or radiation. An illustrative calculation gives a 90% particle inventory after one routing step while retaining 77.5% of the initial energy under the stated assumptions. The result concerns the model and its chosen parameters. It supplies a way to test proposed return mechanisms without assigning physical meaning to the full thirteen-layer geometry.

### 1. The geometry and its source

**TriSphere is the work of A. Beth Jones.** Jones’s blueprint supplies the hourglass, the toroidal circulation, and the Filter–Product–Compost–Recycler sequence that motivate this paper. The tokamak correspondence and the energy balances are the present paper’s interpretation. [Jones, *The Universal 13-Layer Tri-Sphere Blueprint*](https://docs.google.com/document/d/1I5enZeXyvjFy0pVPHwT70JTCAn0XXgt0/edit)

In a diverted tokamak, a cross-section through the device shows nested magnetic flux contours inside a boundary called the separatrix. The separatrix passes through an X-point, a saddle of the poloidal magnetic flux. Its lower branches extend toward material targets. A plasma particle can be transported across the boundary and then travel along an open field line toward a target. The X-point organizes these paths through magnetic geometry. The rate at which particles or energy cross depends on transport. [ITER Technical Basis, §1.3.6](https://www-pub.iaea.org/MTCD/Publications/PDF/ITER-EDA-DS-24.pdf)

The accompanying lab uses the dimensionless flux

$$
\psi(x,z)=\frac{x^2}{2}+\frac{z^2}{2}+\frac{z^3}{3}.
$$

The minimum at $(0,0)$ represents the magnetic axis in cross-section. The saddle at $(0,-1)$ has flux $1/6$. The contour through it has an upper closed lobe and lower branches. The model provides a simple realization of the hourglass crossing. The X-point sits at the edge of confinement, and the toroidal field can remain nonzero there. The plotted contours illustrate one flux topology with adjustable particle accounting. The blueprint’s exact layer count and its Time, Space, and Phase tori remain open as physical mappings. [Tri-Sphere / Tokamak Lab source](https://github.com/enuminous/Tokamak)

### 2. What comes back?

At a divertor target, energy carried by incident particles can become heat that is removed by cooling. Recycled fuel can return as neutrals and later reionize. The returning neutral population can carry a different amount of energy per particle from the outgoing population. A particle budget therefore leaves the energy budget undetermined. [ITER Divertor](https://www.iter.org/machine/divertor) · [ITER Technical Basis, §1.3.6](https://www-pub.iaea.org/MTCD/Publications/PDF/ITER-EDA-DS-24.pdf)

Let $N_0$ be the initial number of fuel nuclei tracked in a confined region and $W_0$ its initial tracked energy. For a single, idealized routing step, let $\ell_N$ and $\ell_W$ be the fractions of each inventory sent into the exhaust circuit. Let $r_N$ and $r_W$ be the fractions of the respective outgoing inventories returned by the end of the step. All fractions are between zero and one. In this step there is no externally supplied fuel or heat, no fusion source or burnup, and no residual inventory in the circuit at the end.

$$
\frac{N_1}{N_0}=1-\ell_N(1-r_N),\qquad
\frac{W_1}{W_0}=1-\ell_W(1-r_W).
$$

With $\ell_N=\ell_W=0.25$, $r_N=0.60$, and $r_W=0.10$, the circuit returns $0.15N_0$ and $0.025W_0$. The updated inventories are $0.90N_0$ and $0.775W_0$. The return fractions are illustrative inputs. The equal outgoing fractions isolate the effect of differing return fractions in this example. The browser lab implements the particle equation. The energy calculation is the extension developed here. [Lab implementation](https://github.com/enuminous/Tokamak/blob/main/model.js)

### 3. An energy balance with a finite return time

To allow energy to remain in the exhaust circuit between steps, let $W_c$ be the stored energy in the confined region and $W_e$ the energy in the exhaust circuit. Define transfers at a consistent boundary, with $P_{ce}$ flowing outward and $P_{ec}$ returning. Let $P_{\rm in}$ be power deposited in the confined region, $P_{c,\rm loss}$ be its direct losses outside both regions, and $P_{e,\rm loss}$ be losses from the circuit to sinks outside both regions. All powers are in watts and the stored energies are in joules. A given flux of energy appears in only one channel.

$$
\begin{aligned}
\dot W_c &= P_{\rm in}-P_{c,\rm loss}-P_{ce}+P_{ec},\\
\dot W_e &= P_{ce}-P_{ec}-P_{e,\rm loss},\\
\frac{d}{dt}(W_c+W_e)&=P_{\rm in}-P_{c,\rm loss}-P_{e,\rm loss}.
\end{aligned}
$$

A larger return transfer can increase the energy held in the core for a given outward transfer. In the combined balance it cancels exactly. At steady state, deposited power matches the net losses. In a burning deuterium–tritium plasma, deposited alpha-particle power can contribute to $P_{\rm in}$ if the model treats fusion as a source to the tracked energy reservoirs. That power comes from fusion and is accounted for separately from recycling. Fusion neutrons carry a distinct share of the reaction energy. [ITER Engineering Basis Handbook, Vol. 1, Ch. 4](https://www.iter.org/sites/default/files/media/2026-01/vol.1_ch.04_role_and_distinctive_feature_dv4qgd_v2_0.pdf)

A minimal closure is $P_{ec}=aW_e$ and $P_{e,\rm loss}=bW_e$, with nonnegative rates $a,b$ in inverse seconds and $a+b>0$. For an energy pulse $E_0$ placed in the circuit, with zero background and no further outward input, $W_e(t)=E_0e^{-(a+b)t}$. Integrating the return and loss powers yields the fractions $a/(a+b)$ and $b/(a+b)$. The decay time is $1/(a+b)$. These are predictions of the proposed constant-rate closure. The rates would have to be measured or estimated independently to make a physical prediction.

### 4. What would test the idea?

A transport study could use a pulse or transient in a fixed divertor configuration. Predefine the core boundary and measure or estimate the change in both inventories, core heating, exhaust heat, radiated power, and the fuel return flux. Evaluate particle and energy return over the same interval, including inventories that have yet to return at the end. Particle diagnostics need a calibration or transport model to turn signals into a return flux. Energy diagnostics need uncertainty estimates and a check for double counting across radiative, wall and target channels.

The smallest comparison is against a no-return model and a model that forces the same fraction to return in both budgets. Fit the constant-rate closure on one set of transients and test it on held-out transients. If the measured heat and particle budgets resolve different return fractions beyond their joint uncertainty, the common-fraction model fails for that regime. If the energy balance residual exceeds the propagated uncertainties, the balance needs a missing-channel or calibration investigation before drawing a physical conclusion. If the pulse return and loss do not share one decay time, the constant-rate closure fails even when the integrated energy balance closes. No device measurements were analyzed for this paper.

### Conclusion

Jones’s TriSphere poses a concrete question when read through the tokamak analogue. After material leaves a circulating region, what returns, how long does it take, and how much of its energy comes back with it? The separatrix gives the question a physical boundary. Particle and energy balances give it distinct observables. That distinction lets the return loop preserve some fuel while the divertor removes heat, and makes any stronger claim about energy recirculation testable.
