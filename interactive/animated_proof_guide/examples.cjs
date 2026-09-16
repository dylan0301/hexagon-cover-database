#!/usr/bin/env node
/* Deterministic local examples using the pinned visualizer's compiled geometry.
 * Usage: node examples.cjs COMPILED_VISUALIZER_DIR OUTPUT_JSON
 * A scene is an illustration of local hypotheses, never a seven-triangle cover.
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const dir = path.resolve(process.argv[2] || '');
const mod = p => require(path.join(dir, p + '.js'));
const {createDefaultStrategy3State} = mod('strategy3/state');
const {checkStrategy3Feasibility} = mod('strategy3/feasibility');
const {evaluateStrategy3Boundary} = mod('strategy3/boundary');
const {evaluateNinePoint} = mod('strategy3/geometry');
const {createDefaultFreeState, triangleVertices} = mod('freeGeometry');
const {getCPerimeterIntersections} = mod('triangle');
const {findRestrictedAbSource} = mod('ab-union/feasibility');
const h=Math.sqrt(3)/2, O={x:0,y:0};
const V=Array.from({length:6},(_,i)=>({x:Math.cos(i*Math.PI/3),y:Math.sin(i*Math.PI/3)}));
const copy=x=>JSON.parse(JSON.stringify(x));
const cross=(a,b,c)=>(b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);
const dist=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
const verts=t=>triangleVertices(t.center,t.angle);
function clearance(p,t) { const vs=verts(t);return Math.min(...vs.map((a,i)=>cross(a,vs[(i+1)%3],p)/dist(a,vs[(i+1)%3]))); }
function insideH(p) {return Math.min(...V.map((a,i)=>cross(a,V[(i+1)%6],p)));}
function trace(t,a,b) {
 let lo=0,hi=1;const vs=verts(t);
 for(let i=0;i<3;i++) {const u=cross(vs[i],vs[(i+1)%3],a),w=cross(vs[i],vs[(i+1)%3],b)-u;
  if(Math.abs(w)<1e-12){if(u<0)return null;} else if(w>0)lo=Math.max(lo,-u/w);else hi=Math.min(hi,-u/w);
 }
 return lo<=hi?[Math.max(0,lo),Math.min(1,hi)]:null;
}
function role(t,i=0) {
 const vs=verts(t);const radial=[(i+5)%6,(i+1)%6].map(j=>trace(t,V[j],O));
 const n=radial.filter(x=>x && x[1]-x[0]>1e-7).length;
 const o=vs.filter(p=>insideH(p)<-1e-7).length;
 const ai=trace(t,V[i],V[(i+5)%6]),bi=trace(t,V[i],V[(i+1)%6]);
 return {o,n,type:n===0?'Vd0':o===1?(n===1?'Vd1':'Vd2'):'T3-like',
  A:ai?ai[1]:0,B:bi?bi[1]:0,radial,vertexMargin:clearance(V[i],t),
  midpoint1Margin:clearance({x:V[(i+1)%6].x/2,y:V[(i+1)%6].y/2},t)};
}
function perturb(t,z) {const r=copy(t);r.center.x+=.0025*Math.sin(2*Math.PI*z);r.angle+=.009*Math.sin(2*Math.PI*z);return r;}
function findPose(predicate, cRole=false) {
 // Search a fixed finite grid and prefer a robust neighborhood, not a one-frame coincidence.
 let best=null,score=-Infinity;
 const x0=cRole?.05:.53,x1=cRole?.48:1.43;
 for(let ai=0;ai<60;ai++)for(let xi=0;xi<=36;xi++)for(let yi=0;yi<=48;yi++){
  const t={center:{x:x0+(x1-x0)*xi/36,y:(yi-24)*.025},angle:ai*Math.PI/90};
  const margin=clearance(cRole?O:V[0],t);if(margin<.007)continue;
  if(!predicate(t))continue;
  if(![.25,.75].every(z=>predicate(perturb(t,z))&&clearance(cRole?O:V[0],perturb(t,z))>.005))continue;
  let sc=margin-(cRole?0:Math.abs(t.center.y-.18)*.08);
  if(sc>score){score=sc;best=t;}
 }
 assert(best,'No robust local example found');return best;
}
const poses={};
for(const [name,o,n,mid] of [['vd0-one',1,0,false],['vd0-two',2,0,false],['vd1',1,1,true],['vd2',1,2,true],['t3',2,1,true]]){
 console.log("Searching",name);
 poses[name]=findPose(t=>{const r=role(t);return r.o===o&&r.n===n&&(!mid||r.midpoint1Margin>.007);});
}
for(const kind of ['CE0','CE1','CE2']){
 poses[kind]=kind==='CE0'?{center:{x:.02,y:0},angle:0}:findPose(t=>getCPerimeterIntersections({position:t.center,angle:t.angle,controlPoint:O}).kind===kind && clearance({x:.5,y:0},t)>.005 && V.filter(v=>clearance({x:v.x/2,y:v.y/2},t)>=0).length===1,true);
}
function freeSnapshot(ts) {const s=createDefaultFreeState();s.target='S';s.tool='move';s.strictEps=1e-6;
 for(const t of s.triangles){t.hidden=true;t.fixed=true;}
 for(const [id,pose] of Object.entries(ts)){const t=s.triangles.find(t=>t.id===id);Object.assign(t,copy(pose),{hidden:false,fixed:true});}
 s.selectedTriangleId=Object.keys(ts)[0];return {...s,version:8};
}
const N=14, zs=Array.from({length:N},(_,i)=>i/(N-1));
const scenes=[];
function freeScene(id,poseName,extras={}) {
 const frames=zs.map(z=>{const pose=perturb(poses[poseName],z);return {free:freeSnapshot({V0:pose}),metrics:role(pose),caption:`Local ${role(pose).type}: (o,n)=(${role(pose).o},${role(pose).n}); A+B=${(role(pose).A+role(pose).B).toFixed(4)}`};});
 scenes.push({id,mode:'free',frames,...extras});
}
for(const kind of ['CE0','CE1','CE2']){
 scenes.push({id:kind.toLowerCase(),mode:'triangle',frames:zs.map(z=>{const t=perturb(poses[kind],z);const c=getCPerimeterIntersections({position:t.center,angle:t.angle,controlPoint:O});assert.equal(c.kind,kind);
 return {triangleState:{position:t.center,angle:t.angle,controlPoint:O},metrics:{kind:c.kind,intervals:c.intervals,originMargin:clearance(O,t)},caption:`${kind}: ${c.intervals.length} positive boundary trace(s); O remains strictly inside.`};})});
}
for(const id of ['vd0-one','vd0-two','vd1','vd2','t3'])freeScene(id,id);
// The two replacement charts are genuinely different unit-triangle geometries.
function chart(i,x,y){const v=V[i],a=V[(i+5)%6],b=V[(i+1)%6];return {x:v.x+x*(a.x-v.x)+y*(b.x-v.x),y:v.y+x*(a.y-v.y)+y*(b.y-v.y)};}
function poseFromVertices(vs){const center={x:vs.reduce((a,p)=>a+p.x,0)/3,y:vs.reduce((a,p)=>a+p.y,0)/3};return {center,angle:Math.atan2(vs[0].y-center.y,vs[0].x-center.x)-Math.PI/2};}
function replacement(i,p,eps){let xy=p<=.5?[[0,1-p],[1,1-p],[0,-p]].map(([x,y])=>[x-eps,y]):[[p,0],[p,1],[p-1,0]].map(([x,y])=>[x,y-eps]);return poseFromVertices(xy.map(([x,y])=>chart(i,x,y)));}
for(const [id,p0] of [['replacement-minus',.35],['replacement-plus',.65]]){
 scenes.push({id,mode:'free',frames:zs.map(z=>{
  const p1=.2,p2=p0+.02*Math.sin(2*Math.PI*z),eps=.02;
  const t0=replacement(0,p1,eps),t1=replacement(1,p2,eps);
  const r0=role(t0,0),r1=role(t1,1);assert(r0.vertexMargin>0&&r1.vertexMargin>0);assert(r0.n===0&&r1.n===0);
  assert(Math.abs(r0.A+r0.B-(1-eps))<1e-8&&Math.abs(r1.A+r1.B-(1-eps))<1e-8);
  const a=.1,c=.4,B=.2,r=.5;
  const margins=[p1-a,p2-p1,1-B-p2,1-p1-c,Math.max(p2,1-p2)-r];assert(Math.min(...margins)>eps);
  return {free:freeSnapshot({V0:t0,V1:t1}),metrics:{p1,p2,epsilon:eps,a,c,B,r,minMargin:Math.min(...margins),roles:[r0,r1]},caption:`${p2<=.5?'Minus':'Plus'} chart: p1=0.20, p2=${p2.toFixed(3)}, epsilon=0.02; both A+B=0.98.`};})});
}
const dots=xs=>xs.map(v=>Array.isArray(v)?{left:v[0],right:v[1],split:true}:{left:v,right:v,split:false});
function fDots(a,b){const ds=Array(6);[4,5,0,1,2,3].forEach((edge,j)=>ds[edge]={left:b+(1-a-b)*j/5,right:b+(1-a-b)*j/5,split:false});return ds;}
function addS3(id,mode,getDots,options={}) {
 const frames=zs.map((z,i)=>{
  const s=createDefaultStrategy3State(),ed=getDots(z),lay=options.layout||'seven';
  if(mode==='f'){s.f.edgeDots=ed;s.f.pointConstruction=typeof options.construction==='function'?options.construction(i):options.construction||'newton';s.f.showDisk=true;}
  else{s[mode].layout=lay;s[mode].layouts[lay]=ed;}
  const feasibility=checkStrategy3Feasibility(mode,ed);assert(feasibility.ok,`${id}: ${feasibility.reasons.join('; ')}`);
  const disabled=options.disabled?options.disabled(i):[];s[mode].disabledPointIds=disabled;
  const ev=evaluateStrategy3Boundary(mode,ed,disabled,s.f.pointConstruction).witness;
  assert(ev.domainOk,`${id}: domain`);assert(ev.side!==null&&Number.isFinite(ev.side));
  if(!disabled.length)assert(ev.side>=1-1e-8,`${id}: no enclosure obstruction`);
  if(options.range==='easy')assert(ev.cStar<=2/3);if(options.range==='hard')assert(ev.cStar>2/3);
  return {strategy3:s,metrics:{side:ev.side,enabled:ev.enabledPointCount,points:ev.points,parameters:ev.parameters||null,cStar:ev.cStar??null,diskRadius:ev.diskRadius??null,sourceCount:feasibility.sources.filter(Boolean).length,conditions:ev.conditions||[],construction:s.f.pointConstruction},
   view:options.view||'witness',layers:options.layers||null,demo:options.demo ? (i>=4 && i<11) : false, annotation:options.annotation||null,
   caption:mode==='f'?`${s.f.pointConstruction==='newton'?'Newton A,B,C':'Frontier Q-,Q0,Q+'}; c*=${ev.cStar.toFixed(4)}; ${ev.enabledPointCount}/9 points; numerical side=${ev.side.toFixed(4)}`:
   `${mode.toUpperCase()} ${lay==='seven'?'one':'two'}-gap layout; ${ev.enabledPointCount} selected points; numerical side=${ev.side.toFixed(4)}`};
 });
 scenes.push({id,mode:`strategy3-${mode}`,frames});
}
const defs=createDefaultStrategy3State();
for(const mode of ['bc','d'])for(const layout of ['seven','eight']){
 const base=defs[mode].layouts[layout];
 addS3(`${mode}-${layout}`,mode,z=>{let ds=copy(base);const e=mode==='bc'?2:3;const d=.007*Math.sin(2*Math.PI*z);ds[e].left+=d;ds[e].right+=d;return ds;},{layout});
}
addS3('bc-singleton','bc',z=>dots([[.55-.012*(1-Math.cos(2*Math.PI*z)),.55],.535,.52,.505,.49,.475]));
// Progressive reveal deliberately labels the changing subset; a fit of a subset is not a certificate.
addS3('bc-build','bc',()=>copy(defs.bc.layouts.seven),{disabled:i=>i<4?['D2','D3','D4']:i<8?['D3','D4']:[]});
addS3('d-build','d',()=>copy(defs.d.layouts.seven),{disabled:i=>i<4?['PT','G1']:i<8?['G1']:[]});
addS3('bc-source','bc',z=>{const ds=copy(defs.bc.layouts.seven);ds[2].left+=.003*Math.sin(z*Math.PI*2);ds[2].right=ds[2].left;return ds;},{view:'sources'});
addS3('source-difference','bc',()=>copy(defs.bc.layouts.seven),{view:'sources',demo:true});
addS3('f-frontier','f',z=>fDots(.55+.008*Math.sin(z*Math.PI*2),.58),{construction:'frontier',range:'hard'});
addS3('f-newton','f',z=>fDots(.55+.008*Math.sin(z*Math.PI*2),.58),{construction:'newton',range:'hard'});
addS3('f-inner-comparison','f',()=>fDots(.55,.58),{construction:i=>i<7?'frontier':'newton',range:'hard'});
// Four exposed contacts of disk + A,B,C. Lines are explanatory overlays on
// genuine visualizer captures; each normal is checked against the entire comparison set.
for (const contact of ['AB','BC','tangent-A','tangent-C']) {
 addS3('f-contact-'+contact.toLowerCase(),'f',z=>fDots(.55+.004*Math.sin(2*Math.PI*z),.58),
   {range:'hard',layers:{fills:false,outlines:false,hull:false,triangle:false},annotation:contact});
 const scene=scenes[scenes.length-1];
 for (const frame of scene.frames) {
  const pts=frame.metrics.points.slice(6).map(p=>p.point),rho=frame.metrics.diskRadius;
  let choices=[];
  if(contact==='AB'||contact==='BC') {
   const i=contact==='AB'?0:1,a=pts[i],b=pts[i+1],d=dist(a,b);
   for(const sign of [-1,1]){let n={x:sign*(a.y-b.y)/d,y:sign*(b.x-a.x)/d};choices.push({n,k:n.x*a.x+n.y*a.y});}
  } else {
   const a=pts[contact==='tangent-A'?0:2],d=a.x*a.x+a.y*a.y,w=Math.sqrt(d-rho*rho);
   for(const sign of [-1,1])choices.push({n:{x:(rho*a.x-sign*w*a.y)/d,y:(rho*a.y+sign*w*a.x)/d},k:rho});
  }
  const line=choices.find(({n,k})=>rho<=k+1e-8 && pts.every(p=>n.x*p.x+n.y*p.y<=k+1e-8));
  assert(line,'Contact is not exposed: '+contact);
  frame.contact={...line,name:contact,comparisonSet:'disk + Newton A,B,C',maxViolation:Math.max(rho-line.k,...pts.map(p=>line.n.x*p.x+line.n.y*p.y-line.k))};
  frame.caption=`Exposed ${contact}: annotation supports disk + A,B,C, not the full radial hexagon.`;
 }
}
let easy=null;
for(const a of [.53,.55,.85,.8,.75,.7,.65])for(const b of [.51,.5,.2,.25,.3,.35,.4,.45]){
 if(a+b<=1||a*a+a*b+b*b>=1)continue;let ev=evaluateNinePoint(a,b,[],'newton');if(ev.cStar<.64&&checkStrategy3Feasibility('f',fDots(a,b)).ok&&!easy)easy=[a,b];
}
assert(easy,'No easy-range F sample');
addS3('f-disk','f',z=>fDots(easy[0]+.002*Math.sin(2*Math.PI*z),easy[1]),{range:'easy'});
addS3('f-build','f',()=>fDots(.55,.58),{disabled:i=>i<4?['Q-','Q0','Q+']:i<8?['Q-','Q+']:[]});
for(const [id,a,b] of [['f-asymmetric-left',.64,.5],['f-asymmetric-right',.5,.64]])addS3(id,'f',z=>fDots(a+.0015*Math.sin(2*Math.PI*z),b));
// Explicit Type I/II charts, using the paper's shared 120-degree corner basis.
function orientationPose(kind,t,alpha,beta) {
 const D=1-t+t*t,z=Math.sqrt(D),m=kind==='I'?[[-t,1],[1,-(1-t)]]:[[1-t,t],[t,-1]];
 const det=m[0][0]*m[1][1]-m[0][1]*m[1][0];
 const ps=[[0,0],[z,0],[0,z]].map(([u,v])=>{
  u-=alpha;v-=beta;const x=(u*m[1][1]-m[0][1]*v)/det,y=(m[0][0]*v-u*m[1][0])/det;
  // Shared area chart uses x toward V1 and y toward V5, unlike replacement X0.
  return {x:1+x*(V[1].x-1)+y*(V[5].x-1),y:x*V[1].y+y*V[5].y};
 });
 return poseFromVertices(ps);
}
function clippedArea(t) {
 let p=verts(t);
 for(let i=0;i<6;i++) {const a=V[i],b=V[(i+1)%6],q=[];
  for(let j=0;j<p.length;j++){const u=p[j],v=p[(j+1)%p.length],cu=cross(a,b,u),cv=cross(a,b,v);
   if(cu>=-1e-12)q.push(u);if((cu>0)!==(cv>0)){let z=cu/(cu-cv);q.push({x:u.x+z*(v.x-u.x),y:u.y+z*(v.y-u.y)});}
  }p=q;
 }
 return Math.abs(p.reduce((sum,a,i)=>sum+a.x*p[(i+1)%p.length].y-a.y*p[(i+1)%p.length].x,0))/2/(Math.sqrt(3)/4);
}
for(const [id,a,b] of [['area-nonsupercritical',.3,.5],['area-supercritical',.55,.58],['area-reflected',.58,.55]]){
 scenes.push({id,mode:'free',frames:zs.map(z=>{
  const t=.5+.006*Math.sin(z*Math.PI*2),alpha=t*b+.001,beta=(1-t)*a+.001;
  const pose=orientationPose('I',t,alpha,beta),r=role(pose),loss=1-clippedArea(pose);
  assert(r.vertexMargin>0&&r.A>=a&&r.B>=b);assert(loss+1e-9>=(a+b>1?Math.max(a,b):Math.min(a,b))**2);
  return {free:freeSnapshot({V0:pose}),metrics:{...r,orientationType:'I',t,alpha,beta,normalizedLoss:loss},caption:`Type I: A=${r.A.toFixed(3)}, B=${r.B.toFixed(3)}; normalized outside area=${loss.toFixed(4)}.`};})});
}
scenes.push({id:'area-type-ii',mode:'free',frames:zs.map(z=>{
 const t=.4+.02*Math.sin(z*Math.PI*2),beta=.25,B=.35,alpha=Math.sqrt(1-t+t*t)-beta-B;
 const pose=orientationPose('II',t,alpha,beta),r=role(pose);assert(r.vertexMargin>0&&r.A+r.B<1);
 return {free:freeSnapshot({V0:pose}),metrics:{...r,orientationType:'II',t,alpha,beta,normalizedLoss:1-clippedArea(pose)},caption:`Type II: A=0.25, B=0.35; A+B=0.60 <= sqrt(1-t+t^2) <= 1.`};})});
scenes.push({id:'raw-normalization',mode:'free',frames:zs.map(z=>{
 const t=.5,sum=.65,L=Math.sqrt(.75)-sum,alpha=(1-z)*sum/2+z*L,beta=sum-alpha;
 const pose=orientationPose('I',t,alpha,beta),r=role(pose);assert(r.vertexMargin>0&&r.n===0);
 assert(alpha+1e-12>=L&&beta>=L);assert(Math.abs(r.A-2*L)<1e-8&&Math.abs(r.B-2*L)<1e-8);
 return {free:freeSnapshot({V0:pose}),metrics:{...r,t,alpha,beta,traceCutL:L,normalizedInsideArea:clippedArea(pose)},caption:`Raw (3,0) to normalized (2,0): translate outside H; both boundary reaches stay ${(2*L).toFixed(4)}.`};})});
scenes.push({id:'area-cyclic',mode:'free',frames:zs.map(z=>{
 const xs=[.45,.52+.007*Math.sin(2*Math.PI*z),.48,.55,.50,.46],ts={},roles=[];
 for(let i=0;i<6;i++) {
  const a=1-xs[(i+5)%6]+.003,b=xs[i]+.003;
  const points=findRestrictedAbSource({index:i,a,b,restriction:'both',criticality:a+b>1?'supercritical':'nonsupercritical',requiredInteriorPoints:[]});assert(points);
  const pose=poseFromVertices(points),r=role(pose,i);assert(r.vertexMargin>0);ts['V'+i]=pose;roles.push({...r,normalizedLoss:1-clippedArea(pose)});
 }
 const nplus=roles.filter(r=>r.A+r.B>1).length;assert.equal(nplus,2);
 const overlaps=roles.map((r,i)=>r.B+roles[(i+1)%6].A-1);assert(Math.min(...overlaps)>.0059);
 const loss=roles.reduce((s,r)=>s+r.normalizedLoss,0);assert(loss>1);
 return {free:freeSnapshot(ts),metrics:{handoffs:xs,actualNplus:nplus,actualNgap:0,overlaps,totalNormalizedLoss:loss,roles},caption:`Six V triangles really cover the boundary: N+=2, no gaps. Inside-area sum=${(6-loss).toFixed(4)} < 5.`};})});
for(const id of ['t3','vd1']){
 scenes.push({id:'supplier-'+id,mode:'free',frames:zs.map(z=>{
  const pose=perturb(poses[id],z),r=role(pose),[c,u]=r.radial[1],epsilon=1-u;
  const cap=(c+Math.sqrt(c*c-8*c+4))/2,ratio=r.A/(r.A+epsilon);
  assert(c<.5&&u>.5&&r.A+epsilon<=1&&ratio<=1-cap+1e-9);
  return {free:freeSnapshot({V0:pose}),supplier:{c,u,epsilon},metrics:{...r,c,u,epsilon,rescuerRatio:ratio,ratioBound:1-cap},caption:`Original ${r.type} supplier: c=${c.toFixed(4)}, u=${u.toFixed(4)}, epsilon=1-u=${epsilon.toFixed(4)}.`};})});
}
scenes.push({id:'skeleton-budget',mode:'free',frames:zs.map(z=>{
 const ts={C:perturb(poses.CE2,z)},roles=[];
 for(let i=0;i<6;i++){
  let pose;
  if(i%2===0){const a=.55+.003*Math.sin(z*Math.PI*2),b=.58;const ps=findRestrictedAbSource({index:i,a,b,restriction:'both',criticality:'supercritical',requiredInteriorPoints:[]});assert(ps);pose=poseFromVertices(ps);}
  else pose=replacement(i,.45,.02);
  ts['V'+i]=pose;roles.push(role(pose,i));
 }
 const nplus=roles.filter(r=>r.A+r.B>1).length,nsp=roles.filter(r=>r.n>0).length;assert.equal(nplus+nsp,3);
 function length(t){let sum=0;for(let i=0;i<6;i++)for(const [a,b] of [[V[i],V[(i+1)%6]],[V[i],O]]){const r=trace(t,a,b);if(r)sum+=(r[1]-r[0])*dist(a,b);}return sum;}
 const L=Object.values(ts).reduce((s,t)=>s+length(t),0);assert(L<12);
 const mids=V.filter(v=>clearance({x:v.x/2,y:v.y/2},ts.C)>=0).length;assert.equal(mids,1);
 return {free:freeSnapshot(ts),metrics:{actualNplus:nplus,actualNsp:nsp,centerMidpoints:mids,actualTotalTraceLength:L,upperBudget:12,roles},caption:`k=N+ + Nsp=3; sum of actual skeleton traces=${L.toFixed(4)} < 12. This is not a skeleton cover.`};})});
// Data checks are redundant with the app's feasibility tests on purpose.
for(const s of scenes){assert.equal(s.frames.length,N);for(const f of s.frames){if(f.free){for(const t of f.free.triangles.filter(t=>!t.hidden)){const v=verts(t);assert(v.every((p,i)=>Math.abs(dist(p,v[(i+1)%3])-1)<1e-9));}}}}
const output={schema:1,proofRevision:'3b927c996d7641b20887dc56c1fa741cac674256',visualizerRevision:'1cd468b26aed30d5ddcf1ffa501805bf9720482c',framesPerScene:N,poses,easyRangeParameters:easy,scenes};
fs.writeFileSync(process.argv[3],JSON.stringify(output,null,2)+'\n');
console.log(`Validated ${scenes.length} local scenes, ${scenes.length*N} states. Easy F: ${easy}.`);
