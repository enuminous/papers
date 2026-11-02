"""Independent numerical checks for UCRM v1.2 Appendix 2.
NOT the authors' coupled ODE simulation; NOT a physical experiment.
Outputs are the manuscript's stipulated labels, not measured effects.
Python 3 with numpy. Seed 42. 5000 independent random-phase samples.
"""
import numpy as np

N = 128
M = 5000
rng = np.random.default_rng(42)
K = rng.uniform(0.8, 2.2, M)
phases = rng.uniform(0, 2 * np.pi, (M, N))
r = np.abs(np.exp(1j * phases).mean(axis=1))
beta = 0.45

inertial_percent = 100 * beta * r**2
thrust_label = 4.9 * K * r
zpe_fraction_label = 0.22 * r
defensive_prob = 0.92 * r
defensive_bernoulli = rng.random(M) < defensive_prob
mc_half_life_multiplier_label = 1 / (1 - beta * r)

for name, data in [
    ("r", r),
    ("inertial_percent_label", inertial_percent),
    ("thrust_N_per_kg_label", thrust_label),
    ("zpe_fraction_label", zpe_fraction_label),
    ("defensive_bernoulli_percent", 100 * defensive_bernoulli),
    ("defensive_expected_percent", 100 * defensive_prob),
    ("mc_half_life_multiplier_label", mc_half_life_multiplier_label),
]:
    print(f"{name:35s} mean={data.mean():.6f} std={data.std():.6f}")

sigma = 0.05e6
Kc = 2 * np.sqrt(2 * np.pi) * sigma / np.pi
print("Gaussian standard-Kuramoto Kc", Kc)
print("Kc / max sampled K", Kc / 2.2)
print("1.094e6 rad/s expressed in Hz", 1.094e6 / (2 * np.pi))
print("Maximum inertial percent", 100 * beta)
print("Minimum r for >90% assumed defense", 0.90 / 0.92)
print("Maximum ZPE fraction label", 0.22)
print("Maximum Mc lifetime multiplier label", 1 / (1 - beta))
print("Fraction remaining at 1 s if t_half = 0.65 s", 2 ** (-1 / 0.65))
print("Time for 99% loss if t_half = 0.65 s", 0.65 * np.log2(100))

# Stoichiometry: grams of Mc required per kg Bi, assuming atomic fraction.
NA = 6.02214076e23
molar_Bi = 208.9804
molar_Mc = 290.0
for fraction in (0.001, 0.05):
    grams = (1000 / molar_Bi) * fraction / (1 - fraction) * molar_Mc
    atoms = (grams / molar_Mc) * NA
    print(f"Mc at {fraction * 100:g} at.% per kg Bi: {grams:.4f} g; {atoms:.3e} atoms")
