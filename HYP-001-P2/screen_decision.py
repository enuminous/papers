#!/usr/bin/env python3
"""Arithmetic for the HYP-001 P2 v0.5 eight-pair noise screen.

Usage:
    python screen_decision.py a1 a2 a3 a4 a5 a6 a7 a8
    python screen_decision.py --self-test

Inputs are eight paired force amplitudes in microNewtons, extracted with the
prospectively frozen template. The bound is conditional on independent normal
pair amplitudes with constant variance. This calculator verifies neither that
noise model nor calibration, nuisance limits, data provenance or model release.
An arithmetic PASS is not an overall screen pass or a Stage-two authorization.

Reference: NIST/SEMATECH e-Handbook, 7.2.3.1, upper one-sided confidence interval
for a standard deviation: https://www.itl.nist.gov/div898/handbook/prc/section2/prc231.htm
The lower-tail chi-square(7) 0.05 quantile is 2.167349909298057.
No measurements are bundled with this script; self-test values are synthetic.
"""

import argparse
import json
import math
import statistics

N = 8
DF = N - 1
Q05_DF7 = 2.167349909298057
CEILING_UN = 2.0
FACTOR = math.sqrt(DF / Q05_DF7)


def upper95_from_sd(sd):
    if not math.isfinite(sd) or sd < 0:
        raise ValueError("SD must be finite and nonnegative")
    # Round outward at the final operation, so equality cannot round to a pass.
    return math.nextafter(sd * FACTOR, math.inf)


def calculate(amplitudes):
    if len(amplitudes) != N or not all(math.isfinite(x) for x in amplitudes):
        raise ValueError("Supply exactly eight finite paired amplitudes in microNewtons")
    sd = statistics.stdev(amplitudes)
    upper = upper95_from_sd(sd)
    return {
        "protocol": "HYP-001 P2 v0.5",
        "input_units": "microNewton",
        "pairs": N,
        "sample_mean": statistics.mean(amplitudes),
        "sample_sd": sd,
        "degrees_of_freedom": DF,
        "lower_tail_quantile_probability": 0.05,
        "chi_square_quantile": Q05_DF7,
        "upper_one_sided_95_sd": upper,
        "ceiling": CEILING_UN,
        "strictly_below_ceiling": upper < CEILING_UN,
        "conditional_noise_rule": "PASS" if upper < CEILING_UN else "STOP",
        "overall_screen_decision": "NOT DETERMINED BY THIS CALCULATOR",
        "stage_two_authorized": False,
        "conditions": "Independent normal pair amplitudes with stable variance; calibration, nuisance limits and data quality require separate evidence",
    }


def self_test():
    def sample(sd):
        a = sd * math.sqrt(7 / 8)
        return [-a] * 4 + [a] * 4
    low = calculate(sample(1.0))
    high = calculate(sample(2.0))
    assert low["conditional_noise_rule"] == "PASS"
    assert high["conditional_noise_rule"] == "STOP"
    assert abs(high["upper_one_sided_95_sd"] - 3.594301463303081) < 1e-12
    cutoff = CEILING_UN / FACTOR
    assert upper95_from_sd(cutoff) >= CEILING_UN
    assert upper95_from_sd(cutoff * .99) < CEILING_UN
    assert upper95_from_sd(cutoff * 1.01) > CEILING_UN
    assert calculate(list(reversed(sample(1.0))))["sample_sd"] == low["sample_sd"]
    assert abs(calculate([x + 10 for x in sample(1.0)])["sample_sd"] - 1) < 1e-12
    for bad in ([0.0] * 7, [0.0] * 9, [float("nan")] * 8, [float("inf")] * 8):
        try:
            calculate(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid sample accepted")
    assert not high["stage_two_authorized"] and not low["stage_two_authorized"]
    return {"self_test": "PASS", "data": "synthetic", "factor": FACTOR,
            "strict_sd_cutoff": cutoff, "physical_measurements": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("amplitudes", nargs="*", type=float)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            if args.amplitudes:
                parser.error("Do not combine self-test with amplitudes")
            result = self_test()
        else:
            result = calculate(args.amplitudes)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
