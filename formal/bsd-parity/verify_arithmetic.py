#!/usr/bin/env python3
"""Independent exact arithmetic cross-check. Standard library only.

The Lean files carry the formal proofs. This script is a second, readable
implementation and records a negative check on a proposed extra generator.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

POINTS = [(6, -1), (4, 3), (5, -2), (7, 3)]
CASES = [(5, 10, (1, 0), [9, 5, 8, 7]),
         (13, 20, (0, 4), [6, 8, 17, 10]),
         (19, 28, (0, 2), [9, 21, 5, 25])]


def curve_equation(P, p=None):
    x,y = P
    delta = y*y+x*y - (x*x*x-x*x-79*x+289)
    return delta == 0 if p is None else delta % p == 0


def add(P, Q, p=None):
    if P is None:
        return Q
    if Q is None:
        return P
    x,y = P; u,v = Q
    red = (lambda a: a % p) if p else (lambda a: a)
    if x == u and red(y+v+x) == 0:
        return None
    num, den = (3*x*x-2*x-79-y, 2*y+x) if P == Q else (v-y, u-x)
    slope = red(num*pow(den,-1,p)) if p else Fraction(num,den)
    X = red(slope*slope+slope+1-x-u)
    Y = red(-(slope+1)*X-y+slope*x)
    return X,Y


def negate(P, p=None):
    x,y = P
    return (x,(-y-x)%p) if p else (x,-y-x)


def main():
    assert all(curve_equation(P) for P in POINTS)
    rows = []
    for p,N,g,expected in CASES:
        table = {}; P = None
        for n in range(N):
            assert P not in table
            table[P] = n
            P = add(P,g,p)
        assert P is None
        all_points = {None} | {(x,y) for x,y in product(range(p),repeat=2)
                               if curve_equation((x,y),p)}
        assert set(table) == all_points
        logs = [table[(x%p,y%p)] for x,y in POINTS]
        assert logs == expected
        rows.append(dict(prime=p, curve_order=N, generator=g, point_logs=logs,
                         extra_point_8_7_log=table[(8%p,7%p)]))

    moduli = [10,20,28]
    columns = list(zip(*(r['point_logs'] for r in rows)))
    seen = {(0,0,0)}; queue = [(0,0,0)]
    for P in queue:
        for g in columns:
            Q = tuple((a+b)%N for a,b,N in zip(P,g,moduli))
            if Q not in seen:
                seen.add(Q); queue.append(Q)
    expected_image = {v for v in product(*(range(N) for N in moduli)) if sum(v)%2 == 0}
    assert seen == expected_image
    for a,b,c in expected_image:
        t = (c-a-b)//2
        word = [5*a+3*b+5*t, 5*a+9*b, 3*b, 3*a+2*b+5*t]
        assert tuple(sum(x*g[j] for x,g in zip(word,columns))%moduli[j]
                     for j in range(3)) == (a,b,c)

    # Exploratory alternative rejected: this point is already in the same frame.
    Q = (Fraction(8),Fraction(7))
    assert curve_equation(Q)
    assert Q == add(negate(POINTS[0]),negate(POINTS[3]))
    qlogs = [r['extra_point_8_7_log'] for r in rows]
    assert sum(qlogs)%2 == 0
    assert tuple(qlogs) in seen

    result = dict(curve_coefficients=[1,-1,0,-79,289], named_points=POINTS,
                  finite_curves=rows, joined_image_card=len(seen),
                  product_card=10*20*28, image_equals_even_parity_kernel=True,
                  every_compatible_triple_has_verified_constructive_preimage=True,
                  alternative_point_check=dict(point=[8,7], logs=qlogs,
                    rational_identity='Q = -P1 - P4', enlarges_joined_image=False),
                  proves_BSD=False, proves_analytic_rank=False,
                  proves_global_frame_saturation=False)
    out = Path(__file__).with_name('verification') / 'arithmetic.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: finite curves, logarithms, exact parity image, all 2800 preimages, and extra-point check.')


if __name__ == '__main__':
    main()
