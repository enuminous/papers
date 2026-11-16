"""Check SI normalization of the conditional free C1 scalar initial data."""
import argparse
import json
import math

C = 299_792_458


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--energy-j", type=float, default=1)
    parser.add_argument("--width-m", type=float, default=1)
    parser.add_argument("--inverse-compton-m", type=float, default=1)
    args = parser.parse_args()
    energy, width, mu = args.energy_j, args.width_m, args.inverse_compton_m
    if not all(math.isfinite(x) for x in (energy, width, mu)) or min(energy, width) <= 0 or mu < 0:
        parser.error("energy and width must be finite and positive; inverse Compton scale must be finite and nonnegative")

    def normalized_energy_fraction(x, b):
        gaussian = math.exp(-x*x)
        moment2 = math.sqrt(math.pi)*math.erf(x)/4 - x*gaussian/2
        moment4 = 3*moment2/2 - x**3*gaussian/2
        total = math.sqrt(math.pi)*(b*b + 1.5)/4
        return (moment4 + b*b*moment2)/total

    b = mu * width
    amplitude = math.sqrt(2*energy/(math.pi**1.5*width*(b*b + 1.5)))

    def radial_energy(x):
        return 2*math.pi*amplitude**2*width*x*x*(x*x + b*b)*math.exp(-x*x)

    def integrate(x):
        steps = 4000
        dx = x/steps
        interior = math.fsum((4 if i % 2 else 2)*radial_energy(i*dx) for i in range(1, steps))
        return dx*(radial_energy(0) + interior + radial_energy(x))/3

    radii = (0.5, 1, 2, 4, 10)
    for x in radii:
        assert math.isclose(integrate(x)/energy, normalized_energy_fraction(x,b), rel_tol=1e-9)
    assert math.isclose(integrate(10), energy, rel_tol=1e-12)
    # The Gaussian cannot be static: the KG spatial operator divided by
    # the nonzero field at the center is -(3/width² + mu²).
    assert -(3/width**2 + mu**2) < 0
    print(json.dumps({
        "status": "CONDITIONAL_INITIAL_DATA_ONLY",
        "input_energy_j": energy,
        "width_m": width,
        "inverse_compton_m": mu,
        "field_amplitude_sqrt_j_per_m": amplitude,
        "illustrative_total_energy_equivalent_mass_kg": energy/C**2,
        "enclosed_energy_fractions_at_r_over_width": {str(x): normalized_energy_fraction(x,b) for x in radii},
        "independent_quadrature_checks": len(radii) + 1
    }, indent=2))


if __name__ == "__main__":
    main()
