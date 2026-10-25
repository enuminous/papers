#!/usr/bin/env python3
import numpy as np

BASELINE_THRESHOLD=0.045550202720286898
EFMW_THRESHOLD=0.0083479153574375076
SUSTAINED_K=3

def residuals(y,u):
    y=np.asarray(y,dtype=float)
    u=np.asarray(u,dtype=float)
    prev=np.r_[0.0,y[:-1]]
    return y-(0.82*prev+u)

def baseline_score(y,u):
    r=residuals(y,u)
    b=np.zeros_like(r)
    for t in range(1,len(r)):
        b[t]=0.90*b[t-1]+0.10*abs(r[t])
    return b

def efmw_score(y,u):
    r=residuals(y,u)
    m=np.zeros_like(r)
    c=np.zeros_like(r)
    for t in range(1,len(r)):
        m[t]=0.97*m[t-1]+0.03*r[t]
        c[t]=abs(m[t])
    return c

def first_sustained_after(score,threshold,start,k=SUSTAINED_K):
    above=np.asarray(score)>threshold
    for t in range(start,len(score)-k+1):
        if bool(np.all(above[t:t+k])):
            return t
    return None

