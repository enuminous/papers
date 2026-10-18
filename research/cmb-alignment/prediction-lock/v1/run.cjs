#!/usr/bin/env node
"use strict";
const fs=require("node:fs"),path=require("node:path");
const {check}=require("./check.cjs");
if(process.argv.length!==4||process.argv[2]!=="--execute"){
  console.error("Use: node prediction-lock/v1/run.cjs --execute NEW_OUTPUT.json");
  process.exit(2);
}
const {lock,sha}=check();
const core=require(path.resolve(__dirname,lock.implementation.core));
const output=path.resolve(process.argv[3]);
// Reserve the path before drawing, so a previous result cannot be silently replaced.
const fd=fs.openSync(output,"wx");
const started=new Date().toISOString();
const t=lock.new_computational_test;
const record={
  lock_id:lock.id,lock_version:lock.version,
  lock_sha256:sha(path.join(__dirname,"lock.json")),
  runner_sha256:sha(__filename),
  core_sha256:lock.implementation.core_sha256,
  node:process.version,v8:process.versions.v8,started_utc:started,
  seed_uint32:t.seed_uint32,n:t.n,
  classification:"Numerical distribution check; not an observational EFMW test",
  status:"STARTED"
};
fs.writeFileSync(fd,JSON.stringify(record,null,2)+"\n");
let failure=null;
try{
  core.selfTests();
  const r=core.rng(t.seed_uint32),sample=new Float64Array(t.n);
  for(let i=0;i<t.n;i++){
    const a2=core.alm(2,r),a3=core.alm(3,r);
    sample[i]=core.alignment(core.axis(2,a2),core.axis(3,a3));
  }
  record.summary=core.stats(sample);
  record.first_ten=Array.from(sample.slice(0,10));
  record.angular_diagnostics=lock.fixed_probability_predictions.map(v=>{
    const threshold=Math.cos(v.angle_degrees*Math.PI/180);
    return {...v,exceedances:sample.reduce((n,a)=>n+(a>=threshold),0),
      expected_count:t.n*v.probability_separation_at_most_angle};
  });
  record.primary={D_N:record.summary.ks_distance_to_uniform,threshold:t.threshold,alpha:t.alpha,
    dkw_tail_probability_upper_bound:Math.min(1,2*Math.exp(-2*t.n*record.summary.ks_distance_to_uniform**2))};
  record.status=record.primary.D_N<=t.threshold?t.compatible_label:t.failure_label;
}catch(error){
  failure=error;record.status="EXECUTION_FAILURE";record.error=String(error.stack||error);
}finally{
  record.completed_utc=new Date().toISOString();
  const text=JSON.stringify(record,null,2)+"\n";
  fs.ftruncateSync(fd,0);fs.writeSync(fd,text,0,"utf8");fs.closeSync(fd);
}
console.log(JSON.stringify(record,null,2));
if(failure||record.status===t.failure_label)process.exitCode=1;
