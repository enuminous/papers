#!/usr/bin/env node
"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const core=require("./benchmark.cjs");
const root=__dirname,read=p=>JSON.parse(fs.readFileSync(path.join(root,p),"utf8"));
const result=core.run(read("protocol.json"),read("observations.json"),read("recovered/recursion_run3_results.json"));
if(process.argv.includes("--check")){
 const expected=read("results.json");
 const walk=(a,b,p="")=>{
  if(typeof a==="number"&&typeof b==="number"){
   const tol=1e-10*Math.max(1,Math.abs(b));
   if(!Number.isFinite(a)||Math.abs(a-b)>tol)throw Error("Mismatch "+p+": "+a+" vs "+b);
  }else if(a&&typeof a==="object"){
   if(!b||Object.keys(a).join("|")!==Object.keys(b).join("|"))throw Error("Keys "+p);
   for(const k of Object.keys(a))walk(a[k],b[k],p+"."+k);
  }else if(a!==b)throw Error("Mismatch "+p);
 };
 walk(result,expected);
 // Calibration checks use deliberately broad fixed six-standard-error tolerances.
 for(const s of [result.primary,result.gaussian_harmonic_check,...result.harmonic_axes_abs_z]){
  if(Math.abs(s.mean-.5)>6/Math.sqrt(12*s.n))throw Error("Null mean calibration");
  if(s.ks_distance_to_uniform>1.95/Math.sqrt(s.n))throw Error("Null KS diagnostic");
 }
 for(const o of result.observations){
  const err=Math.abs(o.single_pair.exceedances/o.single_pair.n-o.p_exact);
  const se=Math.sqrt(o.p_exact*(1-o.p_exact)/o.single_pair.n);
  if(err>6*se+1/o.single_pair.n)throw Error("Tail calibration "+o.id);
 }
 console.log("PASS: saved results reproduced; numerical invariants and fixed null calibration checks passed.");
}else{
 const dest=process.argv[2];
 if(!dest)throw Error("Use: node run.cjs OUTPUT.json, or node run.cjs --check");
 fs.writeFileSync(dest,JSON.stringify(result,null,2)+"\n");
 console.log("Wrote "+dest);
}
const hashes={};for(const file of ["protocol.json","observations.json","benchmark.cjs","results.json","recovered/recursion_run3_results.json"]){
 hashes[file]=crypto.createHash("sha256").update(fs.readFileSync(path.join(root,file))).digest("hex");
}
console.log(JSON.stringify({node:process.version,v8:process.versions.v8,hashes},null,2));
