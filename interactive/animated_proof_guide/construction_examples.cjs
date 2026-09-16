/* Large, staged construction clips. All geometry is evaluated by the pinned
 * visualizer; scan markers are explicitly labeled annotations, not witnesses.
 * Called by examples.cjs after the common examples have been built.
 */
'use strict';
module.exports = function revise(h) {
 const {scenes,mod,copy,V,O,trace,role,verts,clearance,dist,freeSnapshot,replacement,poseFromVertices}=h;
 const assert=require('node:assert/strict');
 const {createDefaultStrategy3State}=mod('strategy3/state');
 const {evaluateStrategy3Boundary}=mod('strategy3/boundary');
 const {checkStrategy3Feasibility}=mod('strategy3/feasibility');
 const {computeAreaConjResult,areaConjTotals}=mod('areaConjecture');
 const defaults=createDefaultStrategy3State();
 const dots=xs=>xs.map(v=>Array.isArray(v)?{left:v[0],right:v[1],split:true}:{left:v,right:v,split:false});
 const rotate=(p,i)=>({x:p.x*V[i].x-p.y*V[i].y,y:p.x*V[i].y+p.y*V[i].x});
 const poseAt=(t,i)=>({center:rotate(t.center,i),angle:t.angle+i*Math.PI/3});
 const Z=(i,s)=>({x:(1-s)*V[i].x,y:(1-s)*V[i].y});
 const put=s=>{const j=scenes.findIndex(x=>x.id===s.id);s.revision=2;s.presentation='construction';s.posterIndex=s.posterIndex??s.frames.length-1;if(j<0)scenes.push(s);else scenes[j]=s;};
 const ramp=(i,n)=>Math.min(1,Math.max(0,i/(n-1)));
 // This supplier is tilted 15 degrees away from the nearest hex-axis orientation.
 // Classification is checked by outside vertices and positive adjacent traces,
 // not inferred from its angle. The short crossing is shown in a magnified inset.
 const vd1={center:{x:.632,y:.036},angle:Math.PI/4};
 const vd2={center:{x:.48,y:.044},angle:22*Math.PI/180};
 const t3={center:{x:.66,y:.42},angle:99*Math.PI/180};
 for(const [t,name,n,o] of [[vd1,'Vd1',1,1],[vd2,'Vd2',2,1],[t3,'T3-like',1,2]]) {
  const r=role(t);assert.equal(r.type,name);assert.equal(r.n,n);assert.equal(r.o,o);
  assert(r.vertexMargin>.003&&r.midpoint1Margin>.004);
 }
 const bcEnds={seven:dots([[.55,.84],.80,.76,.72,.68,.64]),eight:dots([[.50,.80],.76,.72,.68,.64,[.45,.72]])};
 const dEnds={seven:dots([.6374493693653495,.7030166770750658,.6262294015614317,.5494421260477976,.4726548505341635,[.21576677529141308,.9699526521260851]]),eight:dots([[.7126622967701406,.7816668845806272],.83,.7984641669946723,.7669283339893445,.7353925009840168,[.15137865700758996,.91835754935164]])};
 // Capacity clips retain genuine Strategy 3 inputs, but hide every off-diagonal
 // witness and all enclosing triangles. The first half constructs with fixed
 // data. The second half explicitly changes input and recomputes the witnesses.
 function capacityClip(id,mode,layout,base,end) {
  const targets=mode==='bc'?[2,3,4]:[1],frames=[];
  for(let j=0;j<32;j++){
   const q=j<16?0:ramp(j-16,16),ed=base.map((v,i)=>({left:(1-q)*v.left+q*end[i].left,right:(1-q)*v.right+q*end[i].right,split:v.split}));
   const f=checkStrategy3Feasibility(mode,ed);assert(f.ok,`${id} ${j}: ${f.reasons}`);
   const state=createDefaultStrategy3State();state[mode].layout=layout;state[mode].layouts[layout]=ed;
   const hidden=mode==='bc'?['M0','G0','G1']:['O','G0','G1'];
   const ids=mode==='bc'?['D2','D3','D4']:['PT'];
   if(j<10)hidden.push(...ids);
   state[mode].disabledPointIds=hidden;
   const all=evaluateStrategy3Boundary(mode,ed,hidden),ev=all.witness;
   assert(ev.domainOk);
   const i=targets[0],cp=all.capacities[i],phase=j<5?'own':j<10?'neighbors':j<16?'maximum':'new-input';
   const scan=j<10?ramp(j,10)*cp.gamma:cp.gamma;
   const pts=targets.map(k=>({index:k,point:Z(k,all.capacities[k].gamma),gamma:all.capacities[k].gamma,radial:all.capacities[k].radial}));
   frames.push({strategy3:state,view:'witness',layers:{fills:false,outlines:false,hull:false,triangle:false,triangleFill:false},
    metrics:{side:ev.side,enabled:ev.enabledPointCount,points:ev.points,parameters:ev.parameters||null,cStar:null,diskRadius:null,sourceCount:f.sources.filter(Boolean).length,conditions:ev.conditions||[],construction:state.f.pointConstruction},
    narrative:{kind:'capacity',phase,target:i,scan,own:cp.own,previous:cp.previous,next:cp.next,gamma:cp.gamma,radial:cp.radial,points:pts,inputFraction:q,diagonalOnly:true},
    caption:phase==='own'?`1. Fix the boundary data. Bound the own triangle on r${i}.`:phase==='neighbors'?`2. Check BOTH neighboring capacities on r${i}; scanning markers are not witness points.`:phase==='maximum'?`3. Gamma = max(own, previous, next); place D${i} = (1-Gamma) V${i}.`:`NEW INPUT (${Math.round(q*100)}% of sweep): recompute ${mode==='bc'?'D2, D3, D4':'the radial point on r1'}. No enclosing triangle is drawn.`});
  }
  const motion=Math.max(...targets.map((_,k)=>dist(frames[0].narrative.points[k].point,frames.at(-1).narrative.points[k].point)));
  assert(motion>.14,`${id}: endpoint motion must be conspicuous`);
  put({id,mode:`strategy3-${mode}`,frames,motion:{endpointDisplacement:motion,scanRange:frames[9].narrative.scan},posterIndex:15});
 }
 for(const m of ['bc','d'])for(const l of ['seven','eight'])capacityClip(`${m}-${l}`,m,l,defaults[m].layouts[l],(m==='bc'?bcEnds:dEnds)[l]);
 // Singleton remains a genuine two-handle topology. The whole clip retains
 // equality rather than calling an ordinary shared handoff a singleton gap.
 const singleA=dots([[.55,.55],.535,.52,.505,.49,.475]);
 const singleB=dots([[.76,.76],.745,.73,.715,.70,.685]);
 capacityClip('bc-singleton','bc','seven',singleA,singleB);
 // Actual BC endpoints: six original local triangles, not independent capacity
 // maxima. One neighbor dominates r2, so using only the own triangle is wrong.
 const originals={};
 for(let i=0;i<6;i++)originals['V'+i]=poseAt({center:{x:1.12,y:0},angle:Math.PI/6},i);
 originals.V1=poseAt(vd1,1);
 const actual=[];
 for(const i of [2,3,4]){
  const intervals=[(i+5)%6,i,(i+1)%6].map(k=>({role:k,interval:trace(originals['V'+k],V[i],O)}));
  const own=intervals[1].interval[1],gamma=Math.max(...intervals.map(x=>x.interval?x.interval[1]:0)),point=Z(i,gamma);
  assert(Object.values(originals).every(t=>clearance(point,t)<1e-8));
  assert(Object.values(originals).every(t=>clearance(Z(i,gamma+1e-5),t)<0));
  actual.push({index:i,intervals,own,gamma,radial:1-gamma,point});
 }
 assert(actual[0].gamma>actual[0].own+.06);
 put({id:'bc-build',mode:'free',posterIndex:10,frames:Array.from({length:36},(_,j)=>{
  const k=Math.min(2,Math.floor(j/12)),a=actual[k],v=j%12,phase=v<4?'own':v<8?'neighbors':'maximum';
  const visible={};for(const row of a.intervals)if(row.role===a.index||v>=4)visible['V'+row.role]=originals['V'+row.role];
  return {free:freeSnapshot(visible),metrics:{actualEndpoint:true,allOriginals:originals,allEndpoints:actual,roles:Object.entries(originals).map(([id,t])=>({index:+id.slice(1),...role(t,+id.slice(1))}))},
   narrative:{kind:'actual-bc',phase,target:a.index,scan:ramp(v,9)*a.gamma,...a,diagonalOnly:true,points:actual.slice(0,k+(v>=8?1:0))},
   caption:v<4?`r${a.index}: first find the OWN radial endpoint C${a.index}=${a.own.toFixed(3)}.`:v<8?`r${a.index}: now include both adjacent V triangles and their actual trace endpoints.`:`r${a.index}: gamma=${a.gamma.toFixed(3)}; fixed point P-hat${a.index}=(1-gamma)V${a.index}. ${k===0?'The NEIGHBOR reaches farther than the own triangle.':'Only diagonal witness points are shown.'}`};
 })});
 // Actual D supplier: start at V1, enter at c, leave at u, then measure from O.
 function supplierClip(id,t,name){
  const r=role(t),[c,u]=r.radial[1],epsilon=1-u;
  const bound=1-(c+Math.sqrt(c*c-8*c+4))/2,ratio=r.A/(r.A+epsilon);
  assert(c<.5&&u>.5&&r.A+epsilon<=1&&r.A<=epsilon&&ratio<=bound+1e-9);
  put({id,mode:'free',posterIndex:27,frames:Array.from({length:32},(_,j)=>{
   const phase=j<8?'enter':j<16?'exit':j<24?'epsilon':'witness';
   const scan=j<8?ramp(j,8)*c:j<16?c+ramp(j-8,8)*(u-c):j<24?1-ramp(j-16,8)*epsilon:u;
   return {free:freeSnapshot({V0:t}),supplier:{c,u,epsilon},
    metrics:{...r,c,u,epsilon,rescuerRatio:ratio,ratioBound:bound,actualSupplier:true},
    narrative:{kind:'supplier',phase,target:1,c,u,epsilon,scan,point:Z(1,u),diagonalOnly:true,sourceType:name,sourceVertices:verts(t)},
    caption:phase==='enter'?`1. Move from V1 toward O. Enter the actual ${name} triangle at c=${c.toFixed(4)}.`:phase==='exit'?`2. The open supplier covers c < s < u. Its inward stopping endpoint is u=${u.toFixed(4)}.`:phase==='epsilon'?`3. Change origin: measure from O back to the endpoint. epsilon=1-u=${epsilon.toFixed(4)}.`:`4. Place P_T=epsilon V1. This endpoint is NOT in the open supplier; the covering argument forces it into U_C.`};
  })});
 }
 supplierClip('supplier-vd1',vd1,'Vd1');supplierClip('supplier-t3',t3,'T3-like');supplierClip('d-build',t3,'T3-like');
 // Explicit type clips highlight actual intersections, and retain a large native
 // canvas inset. Vd2 is a diagnostic/perimeter case, never a Vd1 replacement.
 for(const [id,t] of [['vd1',vd1],['vd2',vd2]]) {
  const r=role(t);
  put({id,mode:'free',posterIndex:20,frames:Array.from({length:28},(_,j)=>({free:freeSnapshot({V0:t}),metrics:r,
   narrative:{kind:'type',phase:j<9?'first-ray':j<18?'second-ray':'classification',target:j<9?1:5,scan:(j%9)/8,sourceType:r.type,sourceVertices:verts(t),intervals:r.radial.map((interval,k)=>({role:0,index:k?1:5,interval}))},
   caption:`${r.type}: exactly ${r.o} outside vertex; ${r.n} positive adjacent-diagonal trace${r.n===1?'':'s'}. ${j<9?'Inspect r1.':j<18?'Inspect r5.':'Count the highlighted crossings; angle alone does not define the type.'}`}))});
 }
 for(const [id,p2] of [['replacement-minus',.33],['replacement-plus',.67]]) {
  const r0=role(vd1),a=r0.A,c=trace(vd1,V[0],O)[1],B=.20,r=.52,p1=.20,epsilon=.02;
  const out0=replacement(0,p1,epsilon),out1=replacement(1,p2,epsilon),rr=[role(out0,0),role(out1,1)];
  const margins=[p1-a,p2-p1,1-B-p2,1-p1-c,Math.max(p2,1-p2)-r];
  assert(Math.min(...margins)>epsilon);assert(rr.every(x=>x.n===0&&x.vertexMargin>0));
  assert(Math.abs(rr[0].A+rr[0].B-.98)<1e-9&&Math.abs(rr[1].A+rr[1].B-.98)<1e-9);
  // Preserve the actual old supplier's traces on the affected five pieces.
  for(const [s,e] of [[V[0],V[5]],[V[0],V[1]],[V[0],O],[V[1],O]]) {
   const old=trace(vd1,s,e);if(!old)continue;
   for(let j=0;j<=100;j++){const q=old[0]+(old[1]-old[0])*j/100,p={x:s.x+q*(e.x-s.x),y:s.y+q*(e.y-s.y)};assert(Math.max(clearance(p,out0),clearance(p,out1))>0);}
  }
  put({id,mode:'free',posterIndex:8,frames:Array.from({length:32},(_,j)=>{
   const before=j<12,first=j>=12&&j<18,ts=before?{V0:vd1}:first?{V0:out0}:{V0:out0,V1:out1};
   return {free:freeSnapshot(ts),metrics:{p1,p2,epsilon,a,c,B,r,minMargin:Math.min(...margins),roles:rr,inputRole:r0,inputOwnReach:c,inputPose:vd1,outputPoses:[out0,out1],oldTracesPreserved:true},
    narrative:{kind:'replacement',phase:before?'original':first?'first-replacement':'both-replacements',target:1,scan:before?ramp(j,12):ramp(j-18,14),sourceType:before?'Vd1':'Vd0',sourceVertices:before?verts(vd1):[],intervals:[{role:0,index:1,interval:r0.radial[1]}],p1,p2,epsilon},
    caption:before?'BEFORE: genuine Vd1 supplier, tilted 15 degrees from the nearest hex-axis orientation. One adjacent crossing is magnified.':first?'REPLACE the original supplier. The new first triangle is intentionally axis-aligned and has no adjacent support.':`AFTER: two nonsupercritical Vd0 replacements; p2=${p2.toFixed(2)} uses the ${p2<=.5?'MINUS':'PLUS'} chart. Neither output is claimed to be Vd1.`};
  })});
 }
 // The requested Area Conj / Max Area modes are controlled through the real UI.
 // Their own finite-search estimates are checked against the pinned algorithm.
 // These closed local optimizers are not six original open covering triangles.
 function areaClip(id,mode,make){
  const frames=[];
  for(let j=0;j<28;j++){
   const q=j/27,controls=make(q),pairs=mode==='area-conj'?controls.handoffs.map((x,i)=>[1-controls.handoffs[(i+5)%6],x]):[[controls.a,controls.b]];
   const results=pairs.map(([a,b],i)=>computeAreaConjResult(i,a,b,'high',false));
   assert(results.every(x=>x.status==='found'));
   const totals=areaConjTotals(results),selected=pairs.filter(([a,b])=>a+b>1+1e-9).length;
   if(mode==='area-conj')assert.equal(selected,2);
   frames.push({areaControls:{mode,quality:'high',...controls},metrics:{pairs,results,totals,selectedSupercriticalRows:selected,estimateDirection:'f found <= true maximum; 1-f found >= true minimum loss'},
    narrative:{kind:'area',phase:mode==='area-conj'?'cyclic':'single',inputFraction:q},
    caption:mode==='area-conj'?`AREA CONJ: all six handoffs move by ${(controls.handoffs[0]-.16).toFixed(2)}. Two selected sums exceed 1. Read the native six-row estimates.`:`MAX AREA: a=${controls.a.toFixed(3)}, b=${controls.b.toFixed(3)}; best-found f=${results[0].f.toFixed(4)}, loss=${results[0].deficit.toFixed(4)}. These are numerical estimates.`});
  }
  const moves=mode==='area-conj'?Math.abs(frames.at(-1).areaControls.handoffs[0]-frames[0].areaControls.handoffs[0]):Math.max(Math.abs(frames.at(-1).areaControls.a-frames[0].areaControls.a),Math.abs(frames.at(-1).areaControls.b-frames[0].areaControls.b));
  assert(moves>.45);put({id,mode,frames,motion:{inputDisplacement:moves},posterIndex:mode==='area-conj'?13:27});
 }
 areaClip('area-cyclic','area-conj',q=>({handoffs:[0,.04,.02,.06,.03,.01].map(x=>.16+.58*q+x)}));
 areaClip('area-max','max-area',q=>({a:.08+.49*q,b:.12+.44*q}));
 return scenes;
};
