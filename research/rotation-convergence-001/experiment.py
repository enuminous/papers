"""RC-001 baseline: EXACT ordinary scalar wave; diagnostic flux, not physical vorticity.

phi_tt = phi_xx + phi_yy, c=1
initial phi=x*x*y/2, phi_t=0
exact phi=(x*x+t*t)*y/2; pi=t*y
diagnostic j = pi * grad(phi)
curl_2(j)=partial_x(j_y)-partial_y(j_x)=-t*x*y

A nonzero diagnostic flux curl is NOT a proof of vorticity for a Landau-frame
energy velocity and is not evidence for EFMW-specific physics.
"""
import numpy as np

def run_grid(n, t=0.4):
    xvals = np.linspace(-1, 1, n)
    dx = xvals[1] - xvals[0]
    x, y = np.meshgrid(xvals, xvals, indexing="xy")
    pi = t * y
    jx = pi * x * y
    jy = pi * (x*x + t*t)/2
    curl = np.gradient(jy, dx, axis=1) - np.gradient(jx, dx, axis=0)
    expected = -t*x*y
    interior = np.s_[2:-2, 2:-2]
    err = float(np.max(np.abs(curl[interior]-expected[interior])))
    return err, float(np.max(np.abs(curl[interior])))

if __name__ == "__main__":
    print("n,interior_max_abs_error,interior_max_abs_curl")
    for n in (21, 41, 81, 161):
        err, magnitude = run_grid(n)
        print(f"{n},{err:.12g},{magnitude:.12g}")
        assert err < 1e-10
    err0, mag0 = run_grid(81, 0.0)
    print(f"t=0 control: err={err0}, magnitude={mag0}")
    assert mag0 == 0.0
