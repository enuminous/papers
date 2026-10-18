"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),assert=require("node:assert/strict");
const root=__dirname;
const sha=file=>crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
const read=file=>JSON.parse(fs.readFileSync(path.join(root,file),"utf8"));

function check(){
  let count=0;
  for(const line of fs.readFileSync(path.join(root,"SHA256SUMS"),"utf8").trim().split("\n")){
    const match=line.match(/^([0-9a-f]{64})  (.+)$/);
    assert(match,"Malformed checksum record");
    assert(!path.isAbsolute(match[2])&&!match[2].split("/").includes(".."),"Unsafe checksum path");
    assert.equal(sha(path.join(root,match[2])),match[1],"Changed locked file: "+match[2]);
    count++;
  }
  const lock=read("lock.json"),model=read("source/C1Q-model.json"),freeze=read("source/C1Q-FREEZE.json");
  assert.equal(lock.id,"EFMW-CMB-PRED-001");
  assert.equal(lock.version,"1.0.0");
  assert.equal(model.version,"1.0.0");
  assert.equal(model.model_id,lock.source_model.id);
  for(const field of ["curvature_K","primordial_tensor_ratio","primordial_non_gaussianity","independent_isocurvature"])
    assert.equal(model[field],0,"Unexpected C1Q branch assumption: "+field);
  assert.match(fs.readFileSync(path.join(root,"source/C1Q-class.ini"),"utf8"),/^modes\s*=\s*s\s*$/m);
  for(const s of lock.source_model.snapshots){
    assert.equal(sha(path.join(root,s.snapshot)),s.sha256,"Source snapshot mismatch");
    const original=s.archive_path.replace("EFMW-Cosmology-C1Q-v1.0.0/","");
    if(original!=="FREEZE.json")assert.equal(freeze.specification_sha256[original],s.sha256,"Original model freeze mismatch");
  }
  assert.equal(sha(path.resolve(root,lock.implementation.core)),lock.implementation.core_sha256,"Core changed");
  assert.equal(sha(path.resolve(root,lock.implementation.pinned_parent_protocol)),lock.implementation.parent_protocol_sha256,"Parent protocol changed");
  assert.equal(lock.predictions[0].value,0);
  assert.equal(lock.predictions[1].distribution,"Uniform(0,1)");
  const t=lock.new_computational_test;
  assert.equal(t.n,100000);assert.equal(t.seed_uint32,2026101810);
  assert.equal(t.alpha,0.01);assert.equal(t.formal_test_count,1);
  assert(Math.abs(t.threshold-Math.sqrt(Math.log(2/t.alpha)/(2*t.n)))<1e-15);
  assert.equal(lock.observational_readiness.enabled,false);
  for(const key of ["evaluation_file_manifest","likelihood_revision","nuisance_pipeline","joint_selection_calibration","independence_attestation"])
    assert.equal(lock.observational_readiness[key],null,"A new empirical specification requires a new lock version");
  for(const key of ["rotation_amplitude","absolute_axis","vorticity_evolution","CMB_transfer_operator"])
    assert.equal(lock.rotating_extension[key],null,"A rotating extension requires a new model and lock version");
  return {lock,sha,checksum_count:count};
}
module.exports={check};
if(require.main===module){
  const x=check();
  console.log(JSON.stringify({status:"PASS",id:x.lock.id,version:x.lock.version,checksum_count:x.checksum_count,
    lock_sha256:x.sha(path.join(root,"lock.json")),observational_ready:false,new_seed_executed:false},null,2));
}
