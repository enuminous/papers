"""Exact integer search for matched histories. No participant data used."""
import csv
import sys
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

def numerators(seq):
    weights = [2**j for j in range(len(seq))]
    return tuple(sum(w * fn(x) for w, x in zip(weights, seq))
                 for fn in (lambda x:x, lambda x:x*x, abs))

def check(a, b):
    assert sorted(a)==sorted(b) and a[-1]==b[-1]
    m,q,ba=numerators(a)
    m2,q2,bb=numerators(b)
    assert m==m2 and q==q2 and ba>bb and m!=0
    den=2**len(a)
    return [str(Fraction(x,den)) for x in (m,q,ba,bb)]+[str(Fraction(abs(m),x)) for x in (ba,bb)]

def write_bank(output):
    groups=defaultdict(list)
    for length in (5, 6):
        for seq in product(range(-3,4), repeat=length):
            m,q,b=numerators(seq)
            if m>0:
                groups[(tuple(sorted(seq)),seq[-1],m,q)].append((b,seq))
    source=((3,0,-1,2,1),(-1,2,3,0,1))
    assert check(*source)==['31/32','61/32','39/32','33/32','31/39','31/33']
    rows=[]
    for group in groups.values():
        for (b1,a),(b2,b) in combinations(sorted(group,reverse=True),2):
            if b1==b2: continue
            for sign in (1,-1):
                # Append a common zero to match both final observations.
                x=tuple(sign*v for v in a)+(0,)
                y=tuple(sign*v for v in b)+(0,)
                assert x[-2:]==y[-2:]
                rows.append([' '.join(map(str,x)),' '.join(map(str,y)),*check(x,y)])
    assert rows
    with output.open('w',newline='') as f:
        out=csv.writer(f,lineterminator='\n')
        out.writerow(['A_oldest_first','B_oldest_first','common_m','common_Q','abs_A','abs_B','R_A','R_B'])
        out.writerows(sorted(rows))
    print(len(rows),'verified pairs (including mirrors)')
if __name__=='__main__':
    write_bank(Path(sys.argv[1]))
