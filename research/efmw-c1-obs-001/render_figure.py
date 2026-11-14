#!/usr/bin/env python3
"""Render conditional formulas. No measured or simulated observations are plotted."""
from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from calculate import HBARC_EV_M, H_SI, C_SI, EV_J
ROOT=Path(__file__).resolve().parent
example=json.loads((ROOT/'scope.json').read_text())['example']
L=example['L_m']/HBARC_EV_M
omega=H_SI*C_SI/(example['wavelength_nm']*1e-9*EV_J)
mass=np.geomspace(1e-5,2e-3,12000)
d=mass**2*L/(4*omega)
normalized=np.sinc(d/math.pi)**4
scale=np.linspace(0,1.2,400)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
    'axes.spines.top':False,'axes.spines.right':False})
fig,(ax,bx)=plt.subplots(1,2,figsize=(13,6.5))
fig.patch.set_facecolor('#f8fafc')
for a in (ax,bx):
    a.set_facecolor('#f8fafc');a.grid(alpha=.2)
    a.spines['left'].set_color('#a4b3c0');a.spines['bottom'].set_color('#a4b3c0')
    a.tick_params(colors='#344b60')
ax.semilogx(mass*1000,normalized,color='#176a83',lw=2.5)
ax.set_ylim(-.03,1.06);ax.set_xlim(.01,2)
ax.set_xlabel('Scalar mass (meV)');ax.set_ylabel('Signal / coherent-limit signal')
ax.set_title('Mass changes the interference pattern',loc='left',fontsize=13,pad=15,color='#173147')
node=math.sqrt(4*math.pi*omega/L)*1000
ax.axvline(node,color='#b26841',ls='--',lw=1)
ax.annotate(f'First zero: {node:.3f} meV',xy=(node,.015),xytext=(.065,.36),
            arrowprops={'arrowstyle':'->','color':'#b26841'},color='#995232',fontsize=11)
bx.plot(scale,scale**4,color='#176a83',lw=2.5)
bx.scatter([.5,1],[.5**4,1],color=['#b26841','#176a83'],s=45,zorder=4)
bx.annotate('Half both fields → 1/16 signal',xy=(.5,.5**4),xytext=(.12,.7),
            arrowprops={'arrowstyle':'->','color':'#b26841'},color='#995232',fontsize=11)
bx.set_xlim(0,1.2);bx.set_ylim(0,2.15)
bx.set_xlabel('Scale applied to both magnetic fields')
bx.set_ylabel('Signal / reference signal')
bx.set_title('Field strength fixes a count ratio',loc='left',fontsize=13,pad=15,color='#173147')
fig.suptitle('What the selected C1 branch predicts',x=.06,y=.97,ha='left',
             fontsize=22,fontweight='bold',color='#173147')
fig.text(.06,.905,'CALCULATED RESPONSE  ·  No measured signal  ·  Shared with the generic scalar–photon model',
         fontsize=10.5,color='#526779')
fig.text(.06,.075,'Left: two uniform 14.3 m regions, 532 nm light; weak conversion. Right: fixed mass, geometry and input power.',
         fontsize=10,color='#526779')
fig.text(.06,.035,'A chosen coupling sets the absolute signal size. C1 does not fix it. Real backgrounds and calibration are additional requirements.',
         fontsize=9.5,color='#526779')
fig.subplots_adjust(left=.09,right=.97,bottom=.21,top=.78,wspace=.30)
fig.savefig(ROOT/'predictions.png',dpi=160,facecolor=fig.get_facecolor())
print(ROOT/'predictions.png')

