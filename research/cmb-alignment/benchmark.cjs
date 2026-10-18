"use strict";
// Dependency-free scientific core, usable in Node.js and other ES2020+ engines.
// Protocol: EFMW-CMB-ALIGNMENT-NULL-001. No Math.random, network, clock or I/O.
(function(root) {
  const TAU = 2*Math.PI;
  const clamp = x => Math.max(-1,Math.min(1,x));
  const dot = (a,b) => a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
  const norm = a => Math.sqrt(dot(a,a));
  const unit = a => {const n=norm(a); if(!(n>0)) throw Error("Zero/nonfinite vector");return a.map(v=>v/n);};
  const rotl = (x,k) => ((x<<k)|(x>>>(32-k)))>>>0;
  function rng(seed) {
    let x=seed>>>0;
    function mix() {
      x=(x+0x9e3779b9)>>>0;
      let z=x;
      z=Math.imul(z^(z>>>16),0x21f0aaad);
      z=Math.imul(z^(z>>>15),0x735a2d97);
      return (z^(z>>>15))>>>0;
    }
    let a=mix(),b=mix(),c=mix(),d=mix(),spare=null;
    function uint32() {
      const result=Math.imul(rotl(Math.imul(b,5),7),9)>>>0;
      const t=b<<9;
      c^=a; d^=b; b^=c; a^=d; c^=t; d=rotl(d,11);
      return result;
    }
    const uniform=()=>(uint32()+0.5)/4294967296;
    function normal(){
      if(spare!==null){let z=spare;spare=null;return z;}
      const r=Math.sqrt(-2*Math.log(uniform())),p=TAU*uniform();
      spare=r*Math.sin(p);return r*Math.cos(p);
    }
    return {uint32,uniform,normal};
  }
  function sphere(r) {
    const z=2*r.uniform()-1,p=TAU*r.uniform(),s=Math.sqrt(1-z*z);
    return [s*Math.cos(p),s*Math.sin(p),z];
  }
  function galactic(l,b) {
    l*=Math.PI/180;b*=Math.PI/180;
    return [Math.cos(b)*Math.cos(l),Math.cos(b)*Math.sin(l),Math.sin(b)];
  }
  const alignment=(a,b)=>Math.abs(clamp(dot(unit(a),unit(b))));
  function alm(ell,r) {
    const re=Array(2*ell+1).fill(0),im=Array(2*ell+1).fill(0);
    re[ell]=r.normal();
    for(let m=1;m<=ell;m++){
      const u=r.normal()/Math.sqrt(2),v=r.normal()/Math.sqrt(2),sign=m%2?-1:1;
      re[ell+m]=u;im[ell+m]=v;re[ell-m]=sign*u;im[ell-m]=-sign*v;
    }
    return {re,im};
  }
  // In the m=-ell,...,ell basis:
  // (L+ a)_m=sqrt(ell(ell+1)-(m-1)m) a_(m-1),
  // (L- a)_m=sqrt(ell(ell+1)-(m+1)m) a_(m+1).
  function powerTensor(ell,a) {
    const n=2*ell+1;
    if(a.re.length!==n||a.im.length!==n)throw Error("alm length");
    const re=Array.from({length:3},()=>Array(n).fill(0));
    const im=Array.from({length:3},()=>Array(n).fill(0));
    for(let m=-ell;m<=ell;m++){
      const k=m+ell;
      const cp=m>-ell?Math.sqrt(ell*(ell+1)-(m-1)*m):0;
      const cm=m<ell?Math.sqrt(ell*(ell+1)-(m+1)*m):0;
      const pr=cp?(cp*a.re[k-1]):0,pi=cp?(cp*a.im[k-1]):0;
      const mr=cm?(cm*a.re[k+1]):0,mi=cm?(cm*a.im[k+1]):0;
      re[0][k]=(pr+mr)/2;im[0][k]=(pi+mi)/2;
      re[1][k]=(pi-mi)/2;im[1][k]=(mr-pr)/2;
      re[2][k]=m*a.re[k];im[2][k]=m*a.im[k];
    }
    const q=Array.from({length:3},()=>Array(3).fill(0));
    for(let i=0;i<3;i++)for(let j=i;j<3;j++){
      let s=0;for(let k=0;k<n;k++)s+=re[i][k]*re[j][k]+im[i][k]*im[j][k];
      q[i][j]=q[j][i]=s;
    }
    return q;
  }
  // Symmetric 3x3 Jacobi eigensolver. Eigenvectors are columns.
  function eigenSym(q) {
    const a=q.map(row=>row.slice()),v=[[1,0,0],[0,1,0],[0,0,1]];
    const scale=Math.max(...a.flat().map(Math.abs));
    if(!(scale>0))throw Error("Zero/nonfinite tensor");
    let residual=Infinity,iterations=0;
    for(;iterations<50;iterations++){
      let p=0,k=1;
      for(const [i,j] of [[0,2],[1,2]])if(Math.abs(a[i][j])>Math.abs(a[p][k])){p=i;k=j;}
      residual=Math.abs(a[p][k]);
      if(residual<=1e-14*scale)break;
      const theta=0.5*Math.atan2(2*a[p][k],a[k][k]-a[p][p]);
      const c=Math.cos(theta),s=Math.sin(theta),app=a[p][p],akk=a[k][k],apk=a[p][k];
      a[p][p]=c*c*app-2*s*c*apk+s*s*akk;
      a[k][k]=s*s*app+2*s*c*apk+c*c*akk;
      a[p][k]=a[k][p]=0;
      for(let i=0;i<3;i++)if(i!==p&&i!==k){
        const x=a[i][p],y=a[i][k];
        a[i][p]=a[p][i]=c*x-s*y;a[i][k]=a[k][i]=s*x+c*y;
      }
      for(let i=0;i<3;i++){
        const x=v[i][p],y=v[i][k];v[i][p]=c*x-s*y;v[i][k]=s*x+c*y;
      }
    }
    if(iterations===50)throw Error("Jacobi convergence failed");
    const order=[0,1,2].sort((i,j)=>a[j][j]-a[i][i]);
    return {values:order.map(i=>a[i][i]),vectors:order.map(i=>unit(v.map(row=>row[i]))),iterations,residual};
  }
  function axis(ell,a) {
    const e=eigenSym(powerTensor(ell,a));
    if(e.values[0]-e.values[1]<=1e-12*Math.max(1,Math.abs(e.values[0])))
      throw Error("Nonunique leading axis; do not assign an arbitrary direction");
    return e.vectors[0];
  }
  function wilson(k,n) {
    const z=1.959963984540054,z2=z*z,p=k/n,den=1+z2/n;
    const center=(p+z2/(2*n))/den,h=z*Math.sqrt(p*(1-p)/n+z2/(4*n*n))/den;
    return [Math.max(0,center-h),Math.min(1,center+h)];
  }
  function stats(xs) {
    let s=0,s2=0;const bins=Array(10).fill(0);
    for(const x of xs){s+=x;s2+=x*x;bins[Math.min(9,Math.floor(10*x))]++;}
    const n=xs.length,mean=s/n;
    const sorted=Array.from(xs).sort((a,b)=>a-b);
    let ks=0;
    for(let i=0;i<n;i++)ks=Math.max(ks,(i+1)/n-sorted[i],sorted[i]-i/n);
    return {n,mean,variance:(s2-n*mean*mean)/(n-1),decile_counts:bins,ks_distance_to_uniform:ks,
      reject_at_005_count:xs.reduce((s,x)=>s+(x>=.95),0)};
  }
  function tail(xs,t){
    const k=xs.reduce((s,x)=>s+(x>=t),0),n=xs.length;
    return {threshold:t,exceedances:k,n,p_mc:(k+1)/(n+1),wilson95:wilson(k,n)};
  }
  function matvec(m,v){return m.map(row=>dot(row,v));}
  function transpose(m){return m[0].map((_,i)=>m.map(r=>r[i]));}
  function matmul(a,b){const bt=transpose(b);return a.map(r=>bt.map(c=>dot(r,c)));}
  function selfTests() {
    const checks=[];function check(name,error,tol=1e-11){checks.push({name,error,tolerance:tol,pass:error<=tol});}
    check("Galactic x",norm(galactic(0,0).map((x,i)=>x-[1,0,0][i])));
    check("Galactic y",norm(galactic(90,0).map((x,i)=>x-[0,1,0][i])));
    check("Headless antipodes",Math.abs(alignment([1,2,3],[-1,-2,-3])-1));
    check("Orthogonal axes",alignment([1,0,0],[0,1,0]));
    const R=[[.36,-.48,.8],[.8,.6,0],[-.48,.64,.6]];
    check("Common rotation invariance",Math.abs(alignment([1,2,3],[2,5,-1])-alignment(matvec(R,[1,2,3]),matvec(R,[2,5,-1]))));
    const r=rng(901),spherical=sphere(r);check("Uniform sphere unit length",Math.abs(norm(spherical)-1));
    for(const l of [2,3]){
      const re=Array(2*l+1).fill(0),im=re.slice();re[0]=l%2?-1:1;re[2*l]=1;
      const a={re,im},q=powerTensor(l,a),n=axis(l,a);
      check("Planar m=+-ell axis l="+l,1-Math.abs(n[2]));
      check("Angular momentum trace l="+l,Math.abs(q[0][0]+q[1][1]+q[2][2]-l*(l+1)*2));
      const g=alm(l,r),Q=powerTensor(l,g),e=eigenSym(Q);
      const power=g.re.reduce((s,x,i)=>s+x*x+g.im[i]*g.im[i],0);
      check("Random alm trace l="+l,Math.abs(Q[0][0]+Q[1][1]+Q[2][2]-l*(l+1)*power),1e-10);
      check("Eigenpair residual l="+l,norm(matvec(Q,e.vectors[0]).map((x,i)=>x-e.values[0]*e.vectors[0][i])),1e-10);
      const rotated=eigenSym(matmul(matmul(R,Q),transpose(R)));
      check("Tensor rotation equivariance l="+l,1-Math.abs(dot(rotated.vectors[0],matvec(R,e.vectors[0]))));
      const phases=g.re.map((_,i)=>(i-l)*.731);
      const rz={re:g.re.map((x,i)=>x*Math.cos(phases[i])+g.im[i]*Math.sin(phases[i])),
        im:g.im.map((x,i)=>x*Math.cos(phases[i])-g.re[i]*Math.sin(phases[i]))};
      const n0=axis(l,g),nr=axis(l,rz),expected=[Math.cos(.731)*n0[0]-Math.sin(.731)*n0[1],Math.sin(.731)*n0[0]+Math.cos(.731)*n0[1],n0[2]];
      check("alm z rotation equivariance l="+l,1-Math.abs(dot(nr,expected)));
    }
    const r1=rng(2026101801),r2=rng(2026101801);
    const vector=Array.from({length:8},()=>r1.uint32());
    check("RNG deterministic repeat",Math.max(...vector.map(x=>Math.abs(x-r2.uint32()))),0);
    if(checks.some(c=>!c.pass))throw Error("Self tests failed: "+JSON.stringify(checks));
    return {checks,rng_first_uint32:vector};
  }
  function run(protocol,observations,recovered) {
    const verification=selfTests(),p=protocol,primary=new Float64Array(p.primary.n_null);
    const rp=rng(p.rng.seeds.axis_null);
    for(let i=0;i<primary.length;i++)primary[i]=Math.abs(clamp(dot(sphere(rp),sphere(rp))));
    const nh=p.sampling.harmonic_check_realizations,harmonic=new Float64Array(nh),rh=rng(p.rng.seeds.harmonic_check);
    const hz=[new Float64Array(nh),new Float64Array(nh)];
    for(let i=0;i<nh;i++){
      const a=axis(2,alm(2,rh)),b=axis(3,alm(3,rh));
      harmonic[i]=Math.abs(clamp(dot(a,b)));hz[0][i]=Math.abs(a[2]);hz[1][i]=Math.abs(b[2]);
    }
    const family=new Float64Array(p.multiplicity.n_null),rf=rng(p.rng.seeds.look_elsewhere);
    for(let i=0;i<family.length;i++){
      const axes=Array.from({length:9},()=>sphere(rf));let mx=0;
      for(let a=0;a<9;a++)for(let b=a+1;b<9;b++)mx=Math.max(mx,Math.abs(clamp(dot(axes[a],axes[b]))));
      family[i]=mx;
    }
    const rb=rng(p.rng.seeds.pbh_spin_control),spin=[];
    for(let k=0;k<64;k++){
      const s=[0,0,0];
      for(let j=0;j<100000;j++){const v=sphere(rb);for(let i=0;i<3;i++)s[i]+=v[i];}
      const n=norm(s);spin.push({realization:k,resultant:s,norm_over_sqrt_N:n/Math.sqrt(100000),cos_to_z:s[2]/n});
    }
    const result={protocol_id:p.id,protocol_version:p.version,verification,
      primary:stats(primary),gaussian_harmonic_check:stats(harmonic),
      harmonic_axes_abs_z:hz.map(stats),look_elsewhere:stats(family),
      observations:observations.measurements.map(o=>{
        const A=o.A??Math.cos(o.separation_degrees*Math.PI/180),half=o.A_rounding_halfwidth??0;
        return {...o,A,separation_degrees:Math.acos(clamp(A))*180/Math.PI,
          p_exact:1-A,p_rounding_range:[Math.max(0,1-A-half),Math.min(1,1-A+half)],
          single_pair:tail(primary,A),harmonic_check:tail(harmonic,A),any_36_pairs:tail(family,A),
          bonferroni36:Math.min(1,36*(1-A))};
      }),
      positive_control:{separation_degrees:5,A:Math.cos(5*Math.PI/180),p_exact:1-Math.cos(5*Math.PI/180),
        single_pair:tail(primary,Math.cos(5*Math.PI/180)),meaning:"Deliberately inserted alignment; sensitivity check only."},
      posthoc_single_axis:{A_max:1,p_correct_null:1,reason:"Fit the reference axis to each realization, including nulls."},
      spin_control:{n_objects:100000,n_realizations:64,unit:"dimensionless unit vectors",runs:spin,
        abs_cos_summary:stats(spin.map(v=>Math.abs(v.cos_to_z))),
        mean_resultant_squared_over_N:spin.reduce((s,v)=>s+v.norm_over_sqrt_N**2,0)/spin.length},
      fingerprint:{primary_first10:Array.from(primary.slice(0,10)),harmonic_first10:Array.from(harmonic.slice(0,10)),family_first10:Array.from(family.slice(0,10))}};
    if(recovered){
      const a=recovered.null_all_cos,t0=Math.abs(a[0]),rank=(1+a.slice(1).filter(x=>Math.abs(x)>=t0).length)/a.length;
      const mean=a.reduce((s,x)=>s+x,0)/a.length,meanabs=a.reduce((s,x)=>s+Math.abs(x),0)/a.length;
      const max=Math.max(...a.map(Math.abs));
      result.recovered_universe003={source_status:"summary arithmetic recomputed from preserved output; original Python merger code not rerun here",
        n:a.length,cos_mean:mean,abs_cos_mean:meanabs,first_fixed_axis_p:1-t0,first_empirical_rank_p:rank,
        maximum_abs_cos:max,minimum_single_run_p:1-max,
        probability_any_of_128_at_least_this_aligned:1-Math.pow(max,a.length),
        summary_errors:{cos_mean:mean-recovered.null_cos_mean,abs_cos_mean:meanabs-recovered.null_abs_cos_mean,
          fixed_p:(1-t0)-recovered.first_run_exact_fixed_axis_p,rank_p:rank-recovered.first_run_empirical_rank_p}};
    }
    return result;
  }
  const api={rng,sphere,galactic,alignment,alm,powerTensor,eigenSym,axis,wilson,stats,tail,selfTests,run};
  if(typeof module!=="undefined"&&module.exports)module.exports=api;
  root.CMBAlignment=api;
})(globalThis);
