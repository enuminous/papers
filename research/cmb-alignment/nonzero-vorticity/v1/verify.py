#!/usr/bin/env python3
"""Frozen local two-scalar construction; not a cosmology or CMB simulation.

The numerical path constructs T from field derivatives, solves its 4x4
eigensystem, and differentiates the resulting normalized four-velocity.
It does not use the proposed vorticity formula to generate the measured
vorticity. The formula is evaluated through a separate one-dimensional root.
"""
import argparse
import hashlib
import itertools
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import brentq
import sympy as sp

HERE = Path(__file__).resolve().parent
P = json.loads((HERE / "protocol.json").read_text())
ETA = np.diag([-1., 1., 1., 1.])
EPS = np.zeros((4, 4, 4, 4))
for perm in itertools.permutations(range(4)):
    inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
    EPS[perm] = (-1.) ** inversions
OFFSETS = np.array([P['parameters']['p'], P['parameters']['q']])
GRADS = np.array([[P['parameters']['alpha'], 0., 0.],
                  [0., P['parameters']['beta'], 0.]])


def freeze_check():
    for line in (HERE / "FREEZE.sha256").read_text().splitlines():
        expected, name = line.split("  ", 1)
        actual = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f"Immutable freeze mismatch: {name}")


def symbolic_check():
    t, x, y, z, p, q, a, b, r = sp.symbols('t x y z p q a b r', real=True)
    coords = [t, x, y, z]
    metric = sp.diag(-1, 1, 1, 1)
    fields = [t*(p+a*x), t*(q+b*y)]
    stress = sp.zeros(4)
    kg, frobenius = [], []
    for field in fields:
        d = sp.Matrix([sp.diff(field, c) for c in coords])
        up = metric*d
        norm = (d.T*up)[0]
        stress += up*up.T - metric*norm/2
        kg.append(sp.simplify(sum(metric[i, i]*sp.diff(field, coords[i], 2)
                                  for i in range(4))))
        # Covector u_mu = -partial_mu field / sqrt(-partial field squared).
        u = -d/sp.sqrt(-norm)
        for i, j, k in itertools.combinations(range(4), 3):
            wedge = (u[i]*(sp.diff(u[k], coords[j])-sp.diff(u[j], coords[k]))
                     + u[j]*(sp.diff(u[i], coords[k])-sp.diff(u[k], coords[i]))
                     + u[k]*(sp.diff(u[j], coords[i])-sp.diff(u[i], coords[j])))
            frobenius.append(sp.simplify(wedge))
    divergence = [sp.simplify(sum(sp.diff(stress[i, j], coords[i])
                                 for i in range(4))) for j in range(4)]
    f, g = p+a*x, q+b*y
    A = f*f + g*g
    d1, d2 = r+a*a*t*t, r+b*b*t*t
    vx, vy = -t*a*f/d1, -t*b*g/d2
    s = 1-vx*vx-vy*vy
    equation = r-A+t*t*(a*a*f*f/d1+b*b*g*g/d2)
    proposed_dr = {x: 2*a*f*r/(d1*s), y: 2*b*g*r/(d2*s),
                   t: -2*r*(1-s)/(t*s)}
    zero = lambda v: sp.factor(sp.together(v)) == 0
    root_checks = {'F_r_equals_s': zero(sp.diff(equation, r)-s)}
    dr = {}
    for c in [t, x, y]:
        dr[c] = -sp.diff(equation, c)/sp.diff(equation, r)
        root_checks[str(c)] = zero(dr[c]-proposed_dr[c])
    derivative = lambda expr, c: sp.diff(expr, c)+sp.diff(expr, r)*proposed_dr[c]
    curl = derivative(vy, x)-derivative(vx, y)
    cross = vx*derivative(vy, t)-vy*derivative(vx, t)
    curl_target = 2*t**3*a*b*f*g*r*(a*a-b*b)/(s*d1**2*d2**2)
    curl_ok, cross_ok = zero(curl-curl_target), zero(cross-curl_target)
    coefficient = sp.simplify((2*a*b*f*g*(a*a-b*b)/A**3).subs(
        {p: 1, q: 1, a: 1, b: 2, x: 0, y: 0}))
    identities = {'klein_gordon': all(v == 0 for v in kg),
                  'stress_conservation': all(v == 0 for v in divergence),
                  'individual_frobenius': all(v == 0 for v in frobenius),
                  'root_derivatives': all(root_checks.values()),
                  'curl_identity': curl_ok, 'time_cross_identity': cross_ok,
                  'origin_cubic_coefficient': coefficient == -sp.Rational(3, 2)}
    return {'identities': identities, 'kg_residuals': list(map(str, kg)),
            'stress_divergence': list(map(str, divergence)),
            'frobenius_residuals': list(map(str, frobenius)),
            'root_derivative_checks': root_checks, 'cubic_coefficient': str(coefficient)}


def stress_tensor(point, offsets=OFFSETS, grads=GRADS):
    """Contravariant T/(Phi_star/L)^2 directly from canonical fields."""
    values = offsets+grads@point[1:]
    d = np.column_stack([values, point[0]*grads])
    up = d@ETA
    return up.T@up-0.5*ETA*np.sum(d*up)


def landau(point, offsets=OFFSETS, grads=GRADS, details=False):
    T = stress_tensor(point, offsets, grads)
    vals, vecs = np.linalg.eig(T@ETA)
    candidates = []
    for i, val in enumerate(vals):
        vec = vecs[:, i]
        if abs(val.imag) > 1e-10 or np.max(abs(vec.imag)) > 1e-10:
            continue
        vec = vec.real
        norm = vec@ETA@vec
        if norm < -1e-10:
            u = vec/np.sqrt(-norm)
            if u[0] < 0:
                u = -u
            candidates.append((u, -float(val.real)))
    if len(candidates) != 1:
        raise ValueError(f"Expected one timelike energy eigenvector, got {len(candidates)}")
    u, rho = candidates[0]
    if details:
        return u, rho, float(np.linalg.norm(T@ETA@u+rho*u)/max(1., rho))
    return u


def scalar_flow(point, offsets, grads):
    value = float(offsets[0]+grads[0]@point[1:])
    d = np.r_[value, point[0]*grads[0]]
    norm = -d@ETA@d
    if norm <= 0:
        raise ValueError('Scalar gradient is not timelike')
    return -ETA@d/np.sqrt(norm)


def omega_numeric(point, h, offsets=OFFSETS, grads=GRADS, flow=landau):
    u_cov = ETA@flow(point, offsets, grads)
    derivatives = np.empty((4, 4))
    for k in range(4):
        delta = np.zeros(4)
        delta[k] = h
        deriv = (flow(point-2*delta, offsets, grads)
                 - 8*flow(point-delta, offsets, grads)
                 + 8*flow(point+delta, offsets, grads)
                 - flow(point+2*delta, offsets, grads))/(12*h)
        derivatives[k] = ETA@deriv
    return 0.5*np.einsum('mnrs,n,rs->m', EPS, u_cov, derivatives)


def analytical(point):
    t, x, y, _ = point
    p, q = OFFSETS
    a, b = GRADS[0, 0], GRADS[1, 1]
    f, g = p+a*x, q+b*y
    A = f*f+g*g
    equation = lambda r: r-A+t*t*(a*a*f*f/(r+a*a*t*t)+b*b*g*g/(r+b*b*t*t))
    r = A if t == 0 else brentq(equation, A/2, A, xtol=5e-15, rtol=1e-14)
    d1, d2 = r+a*a*t*t, r+b*b*t*t
    v = np.array([-t*a*f/d1, -t*b*g/d2, 0.])
    s = 1-v@v
    wz = 2*t**3*a*b*f*g*r*(a*a-b*b)/(s*s*d1*d1*d2*d2)
    return v, np.array([0., 0., 0., wz]), r


def quaternion_rotations(q):
    w, x, y, z = q.T
    rows = [[1-2*(y*y+z*z), 2*(x*y-z*w), 2*(x*z+y*w)],
            [2*(x*y+z*w), 1-2*(x*x+z*z), 2*(y*z-x*w)],
            [2*(x*z-y*w), 2*(y*z+x*w), 1-2*(x*x+y*y)]]
    return np.array(rows).transpose(2, 0, 1)


def evaluate():
    freeze_check()
    print('Checking exact symbolic identities...', flush=True)
    symbolic = symbolic_check()
    spec = P['verification']
    grid = spec['grid']
    points = np.array([[t, x, y, grid['zeta']] for t, x, y in
                       itertools.product(grid['tau'], grid['xi'], grid['eta'])])
    hs = spec['finite_difference_steps']
    fine = hs[-1]
    errors = {str(h): [] for h in hs}
    velocity_errors, unit_errors, eigen_errors, energies, margins = [], [], [], [], []
    records = []
    print(f'Checking {len(points)} spacetime points at {len(hs)} derivative steps...', flush=True)
    for point in points:
        u, rho, resid = landau(point, details=True)
        v, exact, root = analytical(point)
        velocity_errors.append(float(np.max(abs(u[1:]/u[0]-v))))
        unit_errors.append(abs(u@ETA@u+1))
        eigen_errors.append(resid)
        energies.append(rho)
        margins.extend((OFFSETS+GRADS@point[1:])**2-point[0]**2*np.sum(GRADS**2, axis=1))
        numerical = []
        for h in hs:
            numeric = omega_numeric(point, h)
            numerical.append(numeric.tolist())
            errors[str(h)].append(float(np.max(abs(numeric-exact))))
        records.append({'point': point.tolist(), 'velocity': v.tolist(),
                        'physical_root': root, 'energy_density': rho,
                        'omega_formula': exact.tolist(), 'omega_eigen_fd': numerical})
    print('Checking ablations, parity, time reversal, and component congruences...', flush=True)
    control_specs = {
        'homogeneous': (OFFSETS, np.zeros_like(GRADS), landau),
        'remove_chi': (OFFSETS[:1], GRADS[:1], landau),
        'remove_phi': (OFFSETS[1:], GRADS[1:], landau),
        'equal_gradient_magnitudes': (OFFSETS, np.array([[1., 0., 0.], [0., 1., 0.]]), landau),
        'phi_own_flow': (OFFSETS[:1], GRADS[:1], scalar_flow),
        'chi_own_flow': (OFFSETS[1:], GRADS[1:], scalar_flow)}
    controls = {}
    for name, (offsets, grads, flow) in control_specs.items():
        controls[name] = max(float(np.max(abs(omega_numeric(point, fine, offsets, grads, flow))))
                             for point in points)
    controls['initial_flow'] = max(float(np.max(abs(landau(point)[1:])))
                                    for point in points if point[0] == 0)
    controls['initial_vorticity'] = max(float(np.max(abs(omega_numeric(point, fine))))
                                       for point in points if point[0] == 0)
    time_error = 0.
    parity_error = 0.
    reflection = np.diag([-1., 1., 1.])
    for point in points:
        truth = analytical(point)[1]
        reversed_point = point.copy()
        reversed_point[0] *= -1
        time_error = max(time_error, float(np.max(abs(omega_numeric(reversed_point, fine)+truth))))
        reflected_point = np.r_[point[0], reflection@point[1:]]
        reflected = omega_numeric(reflected_point, fine, OFFSETS, GRADS@reflection.T)
        expected = np.r_[-truth[0], -reflection@truth[1:]]
        parity_error = max(parity_error, float(np.max(abs(reflected-expected))))
    small_t = []
    for t in spec['small_tau_origin']:
        point = np.array([t, 0., 0., 0.])
        exact = analytical(point)[1][3]
        numeric = omega_numeric(point, fine)[3]
        small_t.append({'tau': t, 'omega_formula': exact, 'omega_eigen_fd': float(numeric),
                        'formula_over_tau_cubed': exact/t**3,
                        'eigen_fd_over_tau_cubed': float(numeric/t**3)})
    orientation_spec = spec['orientation_null']
    n = orientation_spec['n']
    generator = np.random.Generator(np.random.PCG64(orientation_spec['seed']))
    raw = generator.standard_normal((n, 4))
    fingerprint = hashlib.sha256(raw.astype('<f8').tobytes()).hexdigest()
    quaternions = raw/np.linalg.norm(raw, axis=1)[:, None]
    rotations = quaternion_rotations(quaternions)
    origin = np.array([0.1, 0., 0., 0.])
    truth = analytical(origin)[1]
    axes = np.empty((n, 3))
    rotation_error = 0.
    max_omega_time = 0.
    print(f'Checking {n} full configurations with frozen Haar orientations...', flush=True)
    for i, R in enumerate(rotations):
        point = np.r_[origin[0], R@origin[1:]]
        # Actually rotate the field gradients, recompute T, solve for u and
        # differentiate. Do not construct the measured result by rotating omega.
        numeric = omega_numeric(point, fine, OFFSETS, GRADS@R.T)
        expected = np.r_[truth[0], R@truth[1:]]
        rotation_error = max(rotation_error, float(np.max(abs(numeric-expected))))
        max_omega_time = max(max_omega_time, abs(float(numeric[0])))
        axes[i] = numeric[1:]/abs(truth[3])
    means = axes.mean(axis=0)
    second_moment = axes.T@axes/n
    rms = float(np.sqrt(np.mean(np.sum(axes*axes, axis=1))))
    tol = spec['absolute_tolerances']
    checks = {
        'symbolic': all(symbolic['identities'].values()),
        'timelike_scalar_gradients': min(margins) > 0,
        'positive_landau_energy': min(energies) > 0,
        'independent_velocity': max(velocity_errors) < tol['eigenvector_vs_root_velocity'],
        'unit_timelike': max(unit_errors) < tol['unit_timelike_residual'],
        'stress_eigenvector': max(eigen_errors) < tol['stress_eigen_residual'],
        'independent_vorticity': max(errors[str(fine)]) < tol['finite_difference_vorticity_finest'],
        'zero_ablations': max(controls.values()) < tol['zero_controls_finest'],
        'proper_rotation_covariance': rotation_error < tol['rotation_reflection_vorticity_finest'],
        'reflection_axial_covariance': parity_error < tol['rotation_reflection_vorticity_finest'],
        'time_reversal': time_error < tol['rotation_reflection_vorticity_finest'],
        'origin_cubic_scaling': abs(small_t[-1]['eigen_fd_over_tau_cubed']+1.5) < tol['small_tau_cubic_coefficient_finest'],
        'orientation_mean_control': np.max(abs(means)) < 6/np.sqrt(3*n),
        'orientation_second_moment_control': np.max(abs(second_moment-np.eye(3)/3)) < 6/np.sqrt(n)}
    return {
        'id': P['id'], 'protocol_sha256': hashlib.sha256((HERE/'protocol.json').read_bytes()).hexdigest(),
        'freeze_commit': 'a135f5b88d6421a6edcfd08c6b91bf9d26431604',
        'execution_utc': datetime.now(timezone.utc).isoformat(),
        'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                        'scipy': scipy.__version__, 'sympy': sp.__version__},
        'checks': {key: bool(value) for key, value in checks.items()},
        'all_passed': bool(all(checks.values())), 'symbolic': symbolic,
        'grid_summary': {'n': len(points), 'smallest_scalar_timelike_margin': float(min(margins)),
                         'minimum_energy_density': float(min(energies)),
                         'max_velocity_error': max(velocity_errors),
                         'max_unit_error': float(max(unit_errors)),
                         'max_stress_eigen_residual': max(eigen_errors),
                         'max_vorticity_error_by_step': {key: max(value) for key, value in errors.items()}},
        'zero_controls_max_absolute_omega': controls,
        'symmetry_errors': {'time_reversal': time_error, 'reflection': parity_error,
                            'proper_rotations': rotation_error},
        'small_time_origin': small_t,
        'origin_at_tau_0_1': {'omega_formula': truth.tolist(),
                             'omega_eigen_fd': omega_numeric(origin, fine).tolist()},
        'orientation_null': {'n': n, 'seed': orientation_spec['seed'],
                             'normal_draws_sha256': fingerprint,
                             'mean_omega_divided_by_fixed_magnitude': means.tolist(),
                             'second_moment_divided_by_fixed_squared_magnitude': second_moment.tolist(),
                             'rms_divided_by_fixed_magnitude': rms,
                             'maximum_absolute_time_component': max_omega_time,
                             'physical_significance': 'Numerical covariance/calibration control only; no CMB p-value or cosmological rotation evidence.'},
        'grid_records': records,
        'interpretation': 'Conditional nonzero local vorticity of composite Landau energy flow. Each constituent scalar flow is irrotational. Prescribed inhomogeneous initial momenta supply spatial structure, not initial flow. No dynamical gravity, global axis, CMB transfer, or EFMW-specific force is demonstrated.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, help='Write complete machine-readable results')
    parser.add_argument('--check', action='store_true', help='Also compare with archived reproducibility records')
    args = parser.parse_args()
    result = evaluate()
    if args.check:
        saved = json.loads((HERE/'results.json').read_text())
        checks = result['checks']
        checks['archived_protocol'] = result['protocol_sha256'] == saved['protocol_sha256']
        checks['archived_random_draws'] = (result['orientation_null']['normal_draws_sha256'] ==
                                           saved['orientation_null']['normal_draws_sha256'])
        checks['archived_origin'] = bool(np.allclose(result['origin_at_tau_0_1']['omega_eigen_fd'],
                                                    saved['origin_at_tau_0_1']['omega_eigen_fd'], rtol=0, atol=2e-8))
        for key in ['mean_omega_divided_by_fixed_magnitude',
                    'second_moment_divided_by_fixed_squared_magnitude']:
            checks['archived_'+key] = bool(np.allclose(result['orientation_null'][key],
                                                       saved['orientation_null'][key], rtol=0, atol=2e-8))
        result['all_passed'] = all(checks.values())
    if args.out:
        args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: result[key] for key in ['all_passed', 'checks', 'grid_summary',
                                                  'origin_at_tau_0_1', 'orientation_null']}, indent=2))
    if not result['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
