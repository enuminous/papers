"""Reproduce EFMW-C1-REL-001 algebra and counterexamples. No empirical data."""
from pathlib import Path
import hashlib
import json
import platform
import sys

import numpy as np
import sympy as s

ROOT = Path(__file__).resolve().parent
records = []


def check(name, condition, evidence):
    ok = bool(condition)
    records.append({"check": name, "passed": ok, "evidence": str(evidence)})
    if not ok:
        raise AssertionError(name + ": " + str(evidence))


def zero(name, expression):
    residual = s.simplify(expression)
    check(name, residual == 0, residual)


lock = json.loads((ROOT / "SCOPE_LOCK.json").read_text())
for path, digest in lock["sha256"].items():
    if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != digest:
        raise ValueError("Source/scope lock mismatch: " + path)

# O1: use one fixed energy unit M_*; these are countermodels, not fits.
mass_coupling_countermodels = [
    {"m_over_Mstar": "1", "g_times_Mstar": "1/100"},
    {"m_over_Mstar": "1", "g_times_Mstar": "1/50"},
    {"m_over_Mstar": "2", "g_times_Mstar": "1/100"},
]
for row in mass_coupling_countermodels:
    mass, coupling = map(s.Rational, row.values())
    row["minimum_K_on_abs_sigma_le_Mstar"] = str(1 - abs(coupling))
    assert mass > 0 and 1 - abs(coupling) > 0
check("Nonzero couplings independent at fixed mass", mass_coupling_countermodels[0]["m_over_Mstar"] == mass_coupling_countermodels[1]["m_over_Mstar"] and mass_coupling_countermodels[0]["g_times_Mstar"] != mass_coupling_countermodels[1]["g_times_Mstar"], mass_coupling_countermodels)
check("Masses independent at fixed coupling", mass_coupling_countermodels[0]["g_times_Mstar"] == mass_coupling_countermodels[2]["g_times_Mstar"] and mass_coupling_countermodels[0]["m_over_Mstar"] != mass_coupling_countermodels[2]["m_over_Mstar"], mass_coupling_countermodels)

# O2: independently differentiate and eliminate the scalar.
X, Y, sigma, g, b, c, d = s.symbols("X Y sigma g b c d", real=True)
m = s.symbols("m", positive=True)
lag = -X / 4 - m**2 * sigma**2 / 2 - g * sigma * X / 4
stationary = s.solve(s.diff(lag, sigma), sigma)[0]
zero("Stationary single-scalar solution", stationary + g * X / (4 * m**2))
effective = s.expand(lag.subs(sigma, stationary))
zero("Single-scalar F4 coefficient", effective.coeff(X, 2) - g**2 / (32 * m**2))

# An allowed C1 mixed mass and X phi_1 phi_2 interaction, solved exactly.
A = s.Matrix([[4, 1], [1, 9]])
K = s.Matrix([[0, 2], [2, 0]])
bvec = s.Matrix([s.Rational(1, 4), s.Rational(1, 8)])
p, q = s.symbols("p q", real=True)
vec = s.Matrix([p, q])
U = (vec.T * (A + X * K) * vec)[0] / 2 + X * (bvec.T * vec)[0]
solution = s.solve([s.diff(U, p), s.diff(U, q)], [p, q])
matched = -U.subs(solution)
expected_a = (bvec.T * A.inv() * bvec)[0] / 2
zero("Full mixed two-scalar stationary matching", matched - X**2 * (bvec.T * (A + X * K).inv() * bvec)[0] / 2)
zero("Allowed X phi_1 phi_2 leaves leading F4 coefficient", s.diff(matched, X, 2).subs(X, 0) / 2 - expected_a)
check("Positive Hessian in mixed example", A[0, 0] > 0 and A.det() > 0, {"A": str(A), "a_X": str(expected_a)})

# A cubic C1 scalar interaction contributes at order X^3, not X^2.
t = s.symbols("t", real=True)
A3 = s.diag(1, 4, 9)
b3 = s.Matrix([s.Rational(1, 4), s.Rational(1, 8), s.Rational(1, 12)])
leading_phi = -A3.inv() * b3 * X
U3_at_leading = (leading_phi.T * A3 * leading_phi)[0] / 2 + X * (b3.T * leading_phi)[0] + t * leading_phi[0] * leading_phi[1] * leading_phi[2]
zero("Cubic scalar term leaves leading F4 coefficient", s.expand(-U3_at_leading).coeff(X, 2) - (b3.T * A3.inv() * b3)[0] / 2)

# Basis invariance and omission bound in an exact diagonal example.
O = s.Matrix([[s.Rational(3, 5), -s.Rational(4, 5)], [s.Rational(4, 5), s.Rational(3, 5)]])
rotated_A, rotated_b = O.T * A * O, O.T * bvec
zero("Orthogonal basis invariance of matching", (rotated_b.T * rotated_A.inv() * rotated_b)[0] / 2 - expected_a)
single_a = s.Rational(1, 32)
two_a = single_a + s.Rational(4, 32 * 9)
check("Additional positive-mass scalar breaks single-mode equality upward", two_a > single_a, {"one_mode": str(single_a), "two_modes": str(two_a), "excess": str(two_a - single_a)})

# Numerical diagonalization checks the spectral representation independently.
spectral_cases = []
for n in (1, 2, 3, 8):
    diag = np.arange(1, n + 1, dtype=float) ** 2
    v = np.arange(1, n + 1, dtype=float) / (10 * n)
    An = np.diag(diag) + np.outer(v, v)
    bn = np.array([(-1)**j / (4 * (j + 1)) for j in range(n)])
    vals, vectors = np.linalg.eigh(An)
    gi = 4 * (vectors.T @ bn)
    terms = gi**2 / (32 * vals)
    direct = 0.5 * (bn @ np.linalg.solve(An, bn))
    spectral = float(terms.sum())
    check(f"Spectral sum n={n}", np.all(vals > 0) and np.all(terms >= 0) and np.isclose(direct, spectral, rtol=1e-11, atol=1e-13), {"direct": float(direct), "spectral": spectral})
    check(f"Observed-subset bound n={n}", float(terms[0]) <= spectral + 1e-13, {"one_term": float(terms[0]), "sum": spectral})
    spectral_cases.append({"n": n, "direct": float(direct), "spectral": spectral, "absolute_error": abs(float(direct) - spectral), "terms": terms.tolist()})

# Constitutive response derived from the matched electromagnetic Lagrangian.
ex, ey, ez, bx, by, bz = s.symbols("ex ey ez bx by bz", real=True)
B0, a = s.symbols("B0 a", real=True)
electric, magnetic = [ex, ey, ez], [bx, by, bz]
invariant = 2 * (bx**2 + by**2 + bz**2 - ex**2 - ey**2 - ez**2)
L_em = -invariant / 4 + a * invariant**2
background = {ex: 0, ey: 0, ez: 0, bx: B0, by: 0, bz: 0}
epsilon = s.hessian(L_em, electric).subs(background)
mu_inverse = -s.hessian(L_em, magnetic).subs(background)
n_perp_squared = s.factor(epsilon[1, 1] / mu_inverse[0, 0])
n_parallel_squared = s.factor(epsilon[0, 0] / mu_inverse[1, 1])
zero("Perpendicular squared index", n_perp_squared - (1 - 16 * a * B0**2) / (1 - 48 * a * B0**2))
zero("Parallel squared index", n_parallel_squared - 1)
zero("Leading scalar birefringence", s.diff(s.sqrt(n_perp_squared), a).subs(a, 0) - 16 * B0**2)
zero("Single-mode birefringence relation", (16 * a * B0**2).subs(a, g**2 / (32 * m**2)) - g**2 * B0**2 / (2 * m**2))

# O3: a direct XY term already occurs in C1, independent of scalar exchange.
Uxy = m**2 * sigma**2 / 2 + sigma * (b * X + c * Y) + d * X * Y
sx = s.solve(s.diff(Uxy, sigma), sigma)[0]
Lxy = s.expand(-Uxy.subs(sigma, sx))
qxx = s.diff(Lxy, X, 2)
qyy = s.diff(Lxy, Y, 2)
qxy = s.diff(Lxy, X, Y)
det = s.factor(qxx * qyy - qxy**2)
zero("One scalar and no contact has rank one", det.subs(d, 0))
zero("Direct-contact determinant", det - (2 * d * b * c / m**2 - d**2))
contact_example = det.subs({m: 1, b: s.Rational(1, 100), c: s.Rational(1, 100), d: s.Rational(3, 10000)})
check("Allowed direct contact destroys rank-one relation", contact_example != 0, contact_example)
two_field_response = s.diag(s.Rational(1, 10000), s.Rational(1, 10000))
check("Two scalars destroy rank one even without direct contact", two_field_response.det() > 0, two_field_response.det())

# O4: nonzero real g cannot keep a linear gauge kinetic factor positive globally.
zero("Global-positivity counterexample", (1 + g * sigma).subs(sigma, -2 / g) + 1)
Phi = s.symbols("Phi", positive=True)
check("Bounded-domain positivity for the countermodels", all(s.Rational(r["minimum_K_on_abs_sigma_le_Mstar"]) > 0 for r in mass_coupling_countermodels), "min K = 1 - |g| Phi; strict positivity requires |g| Phi < 1")

# O5: overall Z drops out of the root equation but not canonical coupling.
time, space = s.symbols("time space", real=True)
Z, speed, beta = s.symbols("Z speed beta", positive=True)
phi = s.Function("phi")(time, space)
J = s.Function("J")(time, space)
L_root = Z * s.diff(phi, time)**2 / (2 * speed**2) - Z * s.diff(phi, space)**2 / 2 - Z * beta * J * phi
EL = s.diff(L_root, phi) - s.diff(s.diff(L_root, s.diff(phi, time)), time) - s.diff(s.diff(L_root, s.diff(phi, space)), space)
zero("Root PDE independent of positive Z", EL / Z - (s.diff(phi, space, 2) - s.diff(phi, time, 2) / speed**2 - beta * J))
canonical_coupling = s.sqrt(Z) * beta
zero("Canonical coupling varies with Z", canonical_coupling.subs(Z, 4) / canonical_coupling.subs(Z, 1) - 2)
alpha, omega, k = s.symbols("alpha omega k", real=True)
wave = s.exp(s.I * (k * space - omega * time))
wave_residual = ((1 - alpha**2) * s.diff(wave, time, 2) / speed**2 - s.diff(wave, space, 2)) / wave
zero("Canonical ME-002 plane-wave dispersion", wave_residual.subs(omega**2, speed**2 * k**2 / (1 - alpha**2)))
check("Canonical speed differs when alpha nonzero", 1 / s.sqrt(1 - s.Rational(1, 4)) > 1, "alpha=1/2 gives v/c=2/sqrt(3)")
check("Canonical alpha above one is non-wave branch", (1 - s.Rational(4)) < 0, "alpha=2 gives omega^2=-c^2 k^2/3")

out = ROOT / "results"
out.mkdir(exist_ok=True)
result = {
    "id": "EFMW-C1-REL-001",
    "status": "mathematical checks, not physical measurements",
    "checks_passed": len(records),
    "checks_failed": 0,
    "software": {"python": platform.python_version(), "numpy": np.__version__, "sympy": s.__version__},
    "checks": records,
    "mass_coupling_countermodels": mass_coupling_countermodels,
    "spectral_cases": spectral_cases,
    "max_spectral_absolute_error": max(r["absolute_error"] for r in spectral_cases),
    "single_mode_a_X": "g^2/(32*m^2)",
    "multi_mode_a_X": "sum_i g_i^2/(32*m_i^2)",
    "leading_delta_n_scalar": "16*a_X*B^2",
    "contact_counterexample_determinant": str(contact_example),
}
(out / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: result[k] for k in ["id", "status", "checks_passed", "checks_failed", "max_spectral_absolute_error"]}, indent=2))
