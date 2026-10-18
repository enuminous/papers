#!/usr/bin/env node
"use strict";
const fs=require("node:fs"),path=require("node:path"),core=require("./benchmark.cjs");
const read=f=>JSON.parse(fs.readFileSync(path.join(__dirname,f),"utf8"));
const p=read("protocol.json"),raw=read("raw-map-results.json");
const primary=new Float64Array(p.primary.n_null),r=core.rng(p.rng.seeds.axis_null);
for(let i=0;i<primary.length;i++)primary[i]=core.alignment(core.sphere(r),core.sphere(r));
const family=new Float64Array(p.multiplicity.n_null),rf=core.rng(p.rng.seeds.look_elsewhere);
for(let i=0;i<family.length;i++){
 const axes=Array.from({length:9},()=>core.sphere(rf));let max=0;
 for(let a=0;a<9;a++)for(let b=a+1;b<9;b++)max=Math.max(max,core.alignment(axes[a],axes[b]));
 family[i]=max;
}
const out={input_sha256:raw.input_sha256,plan:raw.plan_id,
 null_reuse:"Same frozen seeds, draw order and N as results.json. No extra or selected Monte Carlo seed.",
 source_level:"New WMAP9 ILC pixel measurement; ideal isotropic-Gaussian directional-null calibration.",
 cross_implementation:{maximum_axis_antipodal_difference:0,maximum_A23_difference:0},
 treatments:{}};
for(const [name,measurement] of Object.entries(raw.runs_by_iteration["3"])){
 const js={};
 for(const [ell,v] of Object.entries(measurement.all_axes)){
  const n=core.axis(Number(ell),{re:v.alm_re_m_minus_l_to_l,im:v.alm_im_m_minus_l_to_l});
  const c=core.alignment(n,v.axis);
  out.cross_implementation.maximum_axis_antipodal_difference=Math.max(out.cross_implementation.maximum_axis_antipodal_difference,Math.abs(1-c));
  js[ell]=n;
 }
 const delta=Math.abs(core.alignment(js["2"],js["3"])-measurement.A23);
 out.cross_implementation.maximum_A23_difference=Math.max(out.cross_implementation.maximum_A23_difference,delta);
 const iterA=["0","3","5"].map(i=>raw.runs_by_iteration[i][name].A23);
 out.treatments[name]={
  A23:measurement.A23,separation_degrees:measurement.angle23_deg,
  n2_galactic_degrees:[measurement.all_axes["2"].l_deg,measurement.all_axes["2"].b_deg],
  n3_galactic_degrees:[measurement.all_axes["3"].l_deg,measurement.all_axes["3"].b_deg],
  p23_ideal_exact:measurement.p23_ideal_exact,
  single_pair:core.tail(primary,measurement.A23),
  scan_max_pair:measurement.max_pair,
  any_36_pairs:core.tail(family,measurement.max_pair.A),
  bonferroni36:Math.min(1,36*measurement.p23_ideal_exact),
  iteration_A_range:[Math.min(...iterA),Math.max(...iterA)],
  note:name==="uncorrected"?"DQ not removed: p is nominal, not a fully specified observation-level null.":"Leading blackbody DQ correction; uncertainty, foregrounds, masks and instrumental systematics not marginalized."
 };
}
if(out.cross_implementation.maximum_axis_antipodal_difference>1e-10||out.cross_implementation.maximum_A23_difference>1e-10)throw Error("Independent implementations disagree");
const saved=read("results.json");
for(let i=0;i<10;i++){
 if(Math.abs(primary[i]-saved.fingerprint.primary_first10[i])>1e-12||
    Math.abs(family[i]-saved.fingerprint.family_first10[i])>1e-12)throw Error("Frozen stream differs");
}
if(process.argv.includes("--check")){
 const old=read("raw-map-significance.json");
 for(const name of Object.keys(out.treatments)){
  for(const kind of ["single_pair","any_36_pairs"]){
   if(out.treatments[name][kind].exceedances!==old.treatments[name][kind].exceedances)throw Error("Tail mismatch");
  }
 }
 console.log("PASS: raw map independent axes and frozen-null tail counts.");
}else{
 fs.writeFileSync(path.join(__dirname,"raw-map-significance.json"),JSON.stringify(out,null,2)+"\n");
 console.log(JSON.stringify(out,null,2));
}

