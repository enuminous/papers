#!/usr/bin/env python3
"""Secondary WMAP DR5 ILC low-ell measurement; see raw-map-protocol.json."""
import argparse
import hashlib
import json
import platform
import urllib.request
from pathlib import Path

import astropy
import healpy as hp
import numpy as np
import scipy
from astropy.io import fits
from scipy.special import sph_harm_y

HERE = Path(__file__).resolve().parent
EXPECTED_SHA256 = "4501090f824f9140e916339f9e8e490333f6ffe4257a6ee6a02526c8640099a9"


def axis_from_alm(ell, a):
    """Independent Hermitian-operator implementation, m increasing from -ell."""
    m = np.arange(-ell, ell + 1)
    lp = np.diag(np.sqrt(ell * (ell + 1) - m[:-1] * (m[:-1] + 1)), -1)
    lm = lp.T
    operators = [(lp + lm) / 2, (lp - lm) / (2j), np.diag(m)]
    b = np.array([op @ a for op in operators])
    q = (b.conj() @ b.T).real
    values, vectors = np.linalg.eigh(q)
    if values[-1] - values[-2] <= 1e-12 * max(1, abs(values[-1])):
        raise ValueError("Nonunique axis")
    n = vectors[:, -1]
    if n[2] < 0:
        n = -n
    return {
        "axis": n.tolist(),
        "l_deg": float(np.degrees(np.arctan2(n[1], n[0])) % 360),
        "b_deg": float(np.degrees(np.arcsin(np.clip(n[2], -1, 1)))),
        "eigenvalues": values.tolist(),
        "eigenpair_relative_residual": float(np.linalg.norm(q @ n - values[-1] * n) / np.linalg.norm(q)),
        "alm_re_m_minus_l_to_l": a.real.tolist(),
        "alm_im_m_minus_l_to_l": a.imag.tolist(),
    }


def full_alm(packed, ell, lmax=10):
    pos = packed[hp.Alm.getidx(lmax, ell, np.arange(ell + 1))]
    return np.concatenate([np.array([(-1) ** k * pos[k].conjugate() for k in range(ell, 0, -1)]), pos])


def measurement(packed, correction=None):
    all_axes = {}
    for ell in range(2, 11):
        a = full_alm(packed, ell)
        if ell == 2 and correction is not None:
            a = a - correction
        all_axes[str(ell)] = axis_from_alm(ell, a)
    pairs = []
    for l in range(2, 11):
        for k in range(l + 1, 11):
            A = min(1.0, abs(float(np.dot(all_axes[str(l)]["axis"], all_axes[str(k)]["axis"]))))
            pairs.append({"ell_pair": [l, k], "A": A})
    A23 = pairs[0]["A"]
    return {
        "A23": A23, "angle23_deg": float(np.degrees(np.arccos(A23))),
        "p23_ideal_exact": 1 - A23,
        "all_axes": all_axes, "all_36_pairs": pairs, "max_pair": max(pairs, key=lambda v: v["A"]),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads((HERE / "raw-map-protocol.json").read_text())
    if not args.data.exists():
        args.data.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(plan["input"]["url"], timeout=60) as response:
            data = response.read()
        args.data.write_bytes(data)
    sha = hashlib.sha256(args.data.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA256:
        raise ValueError("Input SHA256 differs from the frozen WMAP file")
    with fits.open(args.data) as hdus:
        header = hdus[0].header
        if header["NSIDE"] != 512 or header["ORDERING"].strip() != "NESTED" or header["SKYCOORD"].strip() != "Galactic":
            raise ValueError("Unexpected input coordinates/pixelization")
        if hdus[1].header["TUNIT1"].strip() != "mK, thermodynamic":
            raise ValueError("Unexpected temperature unit")
    sky = hp.read_map(str(args.data), field=0, dtype=np.float64, nest=False)
    if not np.isfinite(sky).all() or np.any(hp.mask_bad(sky)) or sky.size != 12 * 512**2:
        raise ValueError("Invalid or masked map")
    sky *= 1000.0  # mK -> microkelvin, after checking native missing-pixel values
    clean, monopole, dipole = hp.remove_dipole(sky, gal_cut=0, fitval=True, copy=True)
    dq = plan["treatments"][1]
    theta = np.deg2rad(90 - dq["b_degrees"])
    phi = np.deg2rad(dq["l_degrees"])
    correction = np.array([dq["T0_K"] * 1e6 * dq["beta"]**2 * (8 * np.pi / 15) *
                           np.conj(sph_harm_y(2, m, theta, phi)) for m in range(-2, 3)])
    runs = {}
    for it in [3, 0, 5]:
        packed = hp.map2alm(clean, lmax=10, mmax=10, iter=it, pol=False, use_weights=False, use_pixel_weights=False)
        runs[str(it)] = {
            "uncorrected": measurement(packed),
            "DQ_corrected": measurement(packed, correction),
        }
    out = {
        "plan_id": plan["id"], "source": plan["input"],
        "input_sha256": sha, "input_bytes": args.data.stat().st_size,
        "analysis_temperature_unit": "microkelvin",
        "removed_monopole_microK": float(monopole), "removed_dipole_cartesian_microK": dipole.tolist(),
        "DQ_alm_microK_re": correction.real.tolist(), "DQ_alm_microK_im": correction.imag.tolist(),
        "runs_by_iteration": runs,
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
                     "healpy": hp.__version__, "astropy": astropy.__version__},
        "scope": "Full-sky ILC summary and specified DQ sensitivity; ideal directional-null p only. Not end-to-end instrument/foreground significance.",
    }
    args.out.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "runs_by_iteration"}, indent=2))
    for it, treatments in runs.items():
        for name, v in treatments.items():
            print(it, name, json.dumps({k: v[k] for k in ["A23", "angle23_deg", "p23_ideal_exact", "max_pair"]}))


if __name__ == "__main__":
    main()

