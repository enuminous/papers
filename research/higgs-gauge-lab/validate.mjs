#!/usr/bin/env node
// Reproduce the paper's numerical checks from the pinned, unedited HTML source.
// No npm dependencies. Usage: node validate.mjs /path/to/index.html > results.json
import fs from 'node:fs';
import vm from 'node:vm';
import crypto from 'node:crypto';

const PIN = '06056de25e0ad0f5306e6a5d272f983436e54126';
const BLOB = 'cf4482f77fe02086e884e6da905e472b77f3769c';
if (!process.argv[2]) throw new Error('Supply the pinned Higgs-Gauge-Lab index.html');
const bytes = fs.readFileSync(process.argv[2]);
const gitBlob = crypto.createHash('sha1').update(`blob ${bytes.length}\0`).update(bytes).digest('hex');
if (gitBlob !== BLOB) throw new Error(`Source mismatch: ${gitBlob}; expected ${BLOB}`);
const original = bytes.toString('utf8').match(/<script>\s*([\s\S]*?)<\/script>/)[1];
const SEED = 20261029;
function rng(seed) {
  return () => {
    seed |= 0; seed = seed + 0x6D2B79F5 | 0;
    let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}
function lab(dt = 0.045, seed = SEED) {
  const context2d = new Proxy({}, {get: (t, p) => p === 'createImageData'
    ? (w, h) => ({data:new Uint8ClampedArray(w*h*4)}) : () => {}});
  const elements = new Map();
  const element = () => ({clientWidth:640, clientHeight:300, width:640, height:300,
    classList:{toggle(){}}, addEventListener(){}, appendChild(){}, getContext:()=>context2d});
  const math = Object.create(Math); math.random = rng(seed);
  const window = {devicePixelRatio:1, addEventListener(){}};
  const context = vm.createContext({Math:math, window, devicePixelRatio:1,
    requestAnimationFrame(){}, document:{
      getElementById(id){if(!elements.has(id)) elements.set(id,element()); return elements.get(id);},
      createElement:element, querySelectorAll:()=>[]}});
  // Only DT, RNG, DOM/canvas stubs, and inspection exports differ from the app.
  // computeForces(), step(), sample(), and reset() are executed verbatim.
  let source = original.replace('DT=0.045', `DT=${dt}`);
  const end = source.lastIndexOf('})();');
  if (end < 0) throw new Error('Unexpected source structure');
  source = source.slice(0,end) + `window.__audit={params,pr,pi,vr,vi,ax,ay,ex,ey,
    fxr,fxi,fax,fay,bfield,density,xp,xm,yp,ym,computeForces,step,sample,reset,
    metrics:()=>({time,steps:stepnum,energy:lastEnergy,amplitude:lastAmp,gauss:lastGauss})};\n`
    + source.slice(end);
  vm.runInContext(source,context,{timeout:10000});
  return window.__audit;
}
const stateKeys=['pr','pi','vr','vi','ax','ay','ex','ey'];
function snapshot(a){return Object.fromEntries(stateKeys.map(k=>[k,Array.from(a[k])]));}
function stateRmsDifference(a,b){let s=0,n=0;for(const k of stateKeys)for(let i=0;i<a[k].length;i++){s+=(a[k][i]-b[k][i])**2;n++;}return Math.sqrt(s/n);}
function maxAbs(a){let m=0;for(const x of a)m=Math.max(m,Math.abs(x));return m;}
function run(name,dt=0.045,damping=0,T=45){
  const a=lab(dt); a.params.damping=damping; a.reset(name); const initial=a.metrics();
  const steps=Math.round(T/dt); let peakDrift=0,peakGauss=initial.gauss;
  for(let n=1;n<=steps;n++){
    a.step();
    if(n%10===0 || n===steps){a.sample();const m=a.metrics();
      peakDrift=Math.max(peakDrift,Math.abs(m.energy-initial.energy)/initial.energy);
      peakGauss=Math.max(peakGauss,m.gauss);
    }
  }
  return {a,record:{name,dt,damping,T,steps,samplingEverySteps:10,initial,final:a.metrics(),
    sampledMaxRelativeEnergyDeviation:peakDrift,sampledMaxGaussRms:peakGauss}};
}

const report={schemaVersion:1,source:{repository:'enuminous/Higgs-Gauge-Lab',commit:PIN,
  path:'index.html',gitBlob,sha256:crypto.createHash('sha256').update(bytes).digest('hex'),bytes:bytes.length},
  environment:{node:process.version,platform:process.platform,arch:process.arch},
  seed:SEED,parameters:{lambda:0.5,v:1.25,g:0.75,y:0.65,N:64,dx:1},
  methodology:'Unedited numerical functions executed in Node VM; DOM/canvas no-ops; seeded Math.random; added inspection exports; DT replaced only for refinement runs. Damping zero unless specified.'};

const vacuum=lab(); vacuum.params.damping=0;
for(const k of stateKeys)vacuum[k].fill(0);
vacuum.pr.fill(vacuum.params.v/Math.SQRT2);vacuum.computeForces();
const vacuumBefore=snapshot(vacuum);
for(let i=0;i<1000;i++)vacuum.step();vacuum.sample();
report.vacuum={steps:1000,stateRmsChange:stateRmsDifference(vacuumBefore,vacuum),...vacuum.metrics()};

const pulseRuns=[0.045,0.0225,0.01125].map(dt=>run('pulse',dt));
report.pulse=pulseRuns.map(x=>x.record);
const d01=stateRmsDifference(pulseRuns[0].a,pulseRuns[1].a);
const d12=stateRmsDifference(pulseRuns[1].a,pulseRuns[2].a);
report.temporalRefinement={T:45,norm:'RMS over all eight arrays at common final time',
  coarseMediumDifference:d01,mediumFineDifference:d12,ratio:d01/d12,observedOrder:Math.log2(d01/d12)};
report.vortex=run('vortices').record;
report.quench=run('quench').record;
report.dampedQuench=run('quench',0.045,0.028).record;

// Local time-independent gauge transformation with periodic site phases.
const a=lab();a.params.damping=0;a.reset('quench');
for(let n=0;n<100;n++)a.step();a.sample();
const s0=snapshot(a),f0={fxr:Array.from(a.fxr),fxi:Array.from(a.fxi),fax:Array.from(a.fax),fay:Array.from(a.fay)},b0=Array.from(a.bfield),m0=a.metrics();
const random=rng(SEED+1),alpha=Array.from({length:4096},()=>2*(random()-0.5));
for(let i=0;i<4096;i++){
  const c=Math.cos(alpha[i]),s=Math.sin(alpha[i]);
  a.pr[i]=c*s0.pr[i]-s*s0.pi[i];a.pi[i]=s*s0.pr[i]+c*s0.pi[i];
  a.vr[i]=c*s0.vr[i]-s*s0.vi[i];a.vi[i]=s*s0.vr[i]+c*s0.vi[i];
  a.ax[i]=s0.ax[i]+(alpha[a.xp[i]]-alpha[i])/a.params.g;
  a.ay[i]=s0.ay[i]+(alpha[a.yp[i]]-alpha[i])/a.params.g;
}
a.computeForces();a.sample();let scalarErr=0,gaugeErr=0,bErr=0,densityChargeErr=0;
for(let i=0;i<4096;i++){
  const c=Math.cos(alpha[i]),s=Math.sin(alpha[i]);
  scalarErr=Math.max(scalarErr,Math.hypot(a.fxr[i]-(c*f0.fxr[i]-s*f0.fxi[i]),a.fxi[i]-(s*f0.fxr[i]+c*f0.fxi[i])));
  gaugeErr=Math.max(gaugeErr,Math.abs(a.fax[i]-f0.fax[i]),Math.abs(a.fay[i]-f0.fay[i]));
  bErr=Math.max(bErr,Math.abs(a.bfield[i]-b0[i]));
  const oldCharge=2*a.params.g*(s0.pr[i]*s0.vi[i]-s0.pi[i]*s0.vr[i]);
  const newCharge=2*a.params.g*(a.pr[i]*a.vi[i]-a.pi[i]*a.vr[i]);
  densityChargeErr=Math.max(densityChargeErr,Math.abs(newCharge-oldCharge));
}
report.gaugeCovariance={scalarForceMaxAbsError:scalarErr,gaugeForceMaxAbsError:gaugeErr,
  magneticFluxMaxAbsError:bErr,chargeMaxAbsError:densityChargeErr,
  relativeEnergyError:Math.abs(a.metrics().energy-m0.energy)/m0.energy};

// Directional derivative of discrete Hamiltonian: scalar coordinates have
// kinetic energy vr^2+vi^2, hence dH/dpr=-2*fxr; gauge dH/dax=-fax.
const z=lab();z.params.damping=0;z.reset('quench');for(let i=0;i<50;i++)z.step();z.sample();
const coordinateKeys=['pr','pi','ax','ay'],forceKeys=['fxr','fxi','fax','fay'],weights=[2,2,1,1];
const q0=snapshot(z),randomDirection=rng(SEED+2),direction={};let analytic=0;
for(let j=0;j<4;j++){
  const key=coordinateKeys[j];direction[key]=Float64Array.from({length:4096},()=>randomDirection()-0.5);
  for(let i=0;i<4096;i++)analytic-=weights[j]*z[forceKeys[j]][i]*direction[key][i]/4096;
}
function energyAt(eps){for(const key of coordinateKeys)for(let i=0;i<4096;i++)z[key][i]=q0[key][i]+eps*direction[key][i];z.computeForces();z.sample();return z.metrics().energy;}
report.hamiltonianDerivative=[1e-4,1e-5,1e-6].map(eps=>{const measured=(energyAt(eps)-energyAt(-eps))/(2*eps);return{eps,analytic,measured,absoluteError:Math.abs(measured-analytic),relativeError:Math.abs(measured-analytic)/Math.abs(analytic)};});

// Small uniform radial displacement; measure the period from upward zero crossings.
const h=lab();h.params.damping=0;for(const key of stateKeys)h[key].fill(0);
const rho=h.params.v/Math.SQRT2,relativeAmplitude=1e-4;h.pr.fill(rho*(1+relativeAmplitude));h.computeForces();
let previous=h.pr[0]-rho;const crossings=[];
for(let n=1;n<=2000;n++){h.step();const current=h.pr[0]-rho;if(previous<0 && current>=0)crossings.push((n-1+(-previous)/(current-previous))*0.045);previous=current;}
const period=(crossings.at(-1)-crossings[0])/(crossings.length-1),measuredOmega=2*Math.PI/period;
const continuumOmega=Math.sqrt(2*h.params.lambda)*h.params.v;
const verletOmega=2/0.045*Math.asin(continuumOmega*0.045/2);
report.radialFrequency={relativeAmplitude,dt:0.045,T:90,crossingCount:crossings.length,
  measuredOmega,continuumOmega,verletOmega,relativeContinuumError:Math.abs(measuredOmega-continuumOmega)/continuumOmega,
  relativeVerletPredictionError:Math.abs(measuredOmega-verletOmega)/verletOmega};

report.checks={
  equilibrium:report.vacuum.stateRmsChange<1e-12,
  pulseEnergy:report.pulse[0].sampledMaxRelativeEnergyDeviation<0.005,
  vortexEnergy:report.vortex.sampledMaxRelativeEnergyDeviation<0.005,
  quenchEnergy:report.quench.sampledMaxRelativeEnergyDeviation<0.005,
  gauss:Math.max(report.vortex.sampledMaxGaussRms,report.quench.sampledMaxGaussRms,report.dampedQuench.sampledMaxGaussRms)<1e-10,
  gaugeCovariance:Math.max(scalarErr,gaugeErr,bErr,densityChargeErr,report.gaugeCovariance.relativeEnergyError)<1e-10,
  forceHamiltonian:report.hamiltonianDerivative.some(x=>x.relativeError<1e-5),
  temporalOrder:report.temporalRefinement.observedOrder>1.8 && report.temporalRefinement.observedOrder<2.2,
  radialFrequency:report.radialFrequency.relativeContinuumError<0.001,
  dampingLowersEndpointEnergy:report.dampedQuench.final.energy<report.dampedQuench.initial.energy
};
report.checkThresholdNote='Implementation sanity tolerances selected for this report, not an independently preregistered validation protocol or empirical acceptance criterion.';
console.log(JSON.stringify(report,null,2));
if(Object.values(report.checks).some(x=>!x))process.exitCode=1;
