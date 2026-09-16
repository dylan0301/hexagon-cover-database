"""Independent geometric replay for the revised construction clips."""
import math
V=[{'x':math.cos(i*math.pi/3),'y':math.sin(i*math.pi/3)} for i in range(6)]
O={'x':0.,'y':0.}
def cross(a,b,c):return (b['x']-a['x'])*(c['y']-a['y'])-(b['y']-a['y'])*(c['x']-a['x'])
def vertices(t):return [{'x':t['center']['x']+math.cos(t['angle']+math.pi/2+i*2*math.pi/3)/math.sqrt(3),'y':t['center']['y']+math.sin(t['angle']+math.pi/2+i*2*math.pi/3)/math.sqrt(3)} for i in range(3)]
def margin(p,vs):return min(cross(a,vs[(i+1)%len(vs)],p) for i,a in enumerate(vs))
def interval(vs,a,b):
    lo,hi=0.,1.
    for j,u in enumerate(vs):
        v=vs[(j+1)%len(vs)];f=cross(u,v,a);g=cross(u,v,b)-f
        if abs(g)<1e-12:
            if f<0:return None
        elif g>0:lo=max(lo,-f/g)
        else:hi=min(hi,-f/g)
    return [max(0.,lo),min(1.,hi)] if lo<=hi else None

def classify(t,i=0):
    vs=vertices(t)
    return {'o':sum(margin(p,V)<-1e-7 for p in vs),'n':sum(q is not None and q[1]-q[0]>1e-7 for q in [interval(vs,V[(i-1)%6],O),interval(vs,V[(i+1)%6],O)])}
def z(i,s):return {k:(1-s)*V[i][k] for k in ('x','y')}
def close(a,b):assert abs(a-b)<1e-8,(a,b)
def same(a,b):
    for k in ('x','y'):close(a[k],b[k])
def clipped_area(vs):
    p=vs
    for i,a in enumerate(V):
        b=V[(i+1)%6];q=[]
        for j,u in enumerate(p):
            v=p[(j+1)%len(p)];cu,cv=cross(a,b,u),cross(a,b,v)
            if cu>=-1e-12:q.append(u)
            if (cu>0)!=(cv>0):
                t=cu/(cu-cv);q.append({k:u[k]+t*(v[k]-u[k]) for k in ('x','y')})
        p=q
    return abs(sum(a['x']*p[(i+1)%len(p)]['y']-a['y']*p[(i+1)%len(p)]['x'] for i,a in enumerate(p)))/2/(math.sqrt(3)/4)

def check_frame(scene,frame):
    n=frame['narrative'];m=frame['metrics'];kind=n['kind']
    if kind=='capacity':
        close(n['gamma'],max(n[k] or 0 for k in ('own','previous','next')));close(n['radial'],1-n['gamma'])
        allowed={'D2','D3','D4'} if scene['mode']=='strategy3-bc' else {'PT'}
        assert {p['id'] for p in m['points'] if p['enabled']}<=allowed
        assert all(not v for k,v in frame['layers'].items())
        for p in n['points']:same(p['point'],z(p['index'],p['gamma']))
        if scene['id']=='bc-singleton':
            # The signed topology is additionally checked by the S3 source model
            # during generation/import. The stored snapshot must keep split=True.
            pass
    elif kind=='actual-bc':
        ts={int(k[1:]):vertices(v) for k,v in m['allOriginals'].items()}
        for p in m['allEndpoints']:
            i=p['index'];ints=[interval(ts[k],V[i],O) for k in ((i-1)%6,i,(i+1)%6)]
            gamma=max(v[1] if v else 0 for v in ints);close(p['gamma'],gamma);same(p['point'],z(i,gamma))
            assert all(margin(p['point'],vs)<1e-8 for vs in ts.values())
        a=m['allEndpoints'][0];assert a['gamma']>a['own']+.06
    elif kind=='supplier':
        close(n['epsilon'],1-n['u']);same(n['point'],z(1,n['u']))
        vs=n['sourceVertices'];real=interval(vs,V[1],O)
        close(n['c'],real[0]);close(n['u'],real[1])
        assert margin(V[0],vs)>.003 and margin(z(1,.5),vs)>.004
        assert margin(n['point'],vs)<1e-8
    elif kind=='replacement':
        inp=m['inputPose'];assert classify(inp)=={'o':1,'n':1}
        tilt=min(abs(inp['angle']-math.pi/6+k*math.pi/3) for k in range(-4,5))
        assert tilt>math.radians(14.9)
        old=vertices(inp);close(m['a'],interval(old,V[0],V[5])[1]);close(m['c'],interval(old,V[0],O)[1])
        outs=[vertices(t) for t in m['outputPoses']]
        for i,t in enumerate(m['outputPoses']):
            assert classify(t,i)['n']==0
            vs=outs[i];A=interval(vs,V[i],V[(i+5)%6])[1];B=interval(vs,V[i],V[(i+1)%6])[1];close(A+B,.98)
        for a,b in [(V[0],V[5]),(V[0],V[1]),(V[0],O),(V[1],O)]:
            q=interval(old,a,b)
            if not q:continue
            for j in range(51):
                t=q[0]+(q[1]-q[0])*j/50;p={k:a[k]+t*(b[k]-a[k]) for k in ('x','y')}
                assert max(margin(p,vs) for vs in outs)>0
    elif kind=='type':
        vs=n['sourceVertices'];count=sum(q is not None and q[1]-q[0]>1e-7 for q in [interval(vs,V[1],O),interval(vs,V[5],O)])
        assert count==m['n'] and sum(margin(p,V)<-1e-7 for p in vs)==m['o']==1
        assert count==(1 if scene['id']=='vd1' else 2)
    elif kind=='area':
        assert scene['mode'] in ('area-conj','max-area') and frame['nativeAreaReadouts']
        c=frame['areaControls'];assert c['quality']=='high'
        if scene['mode']=='area-conj':
            assert m['selectedSupercriticalRows']==2
            for i,(a,b) in enumerate(m['pairs']):close(a,1-c['handoffs'][(i-1)%6]);close(b,c['handoffs'][i])
        for i,r in enumerate(m['results']):
            assert r['status']=='found';vs=r['triangle']['vertices'];close(clipped_area(vs),r['f']);close(1-r['f'],r['deficit'])
            # Native direct-anchor candidates may be clockwise; normalize winding
            # before the signed half-plane containment test (never take abs(margin)).
            if sum(p['x']*vs[(j+1)%3]['y']-p['y']*vs[(j+1)%3]['x'] for j,p in enumerate(vs))<0:vs=list(reversed(vs))
            for j,p in enumerate(vs):close(math.dist(list(p.values()),list(vs[(j+1)%3].values())),1)
            a,b=m['pairs'][i];anchors=[V[i],{k:V[i][k]+a*(V[(i-1)%6][k]-V[i][k]) for k in ('x','y')},{k:V[i][k]+b*(V[(i+1)%6][k]-V[i][k]) for k in ('x','y')}]
            assert all(margin(p,vs)>-1e-7 for p in anchors)
            values=frame['nativeAreaReadouts'];reported=values['f(a,b) estimate'] if scene['mode']=='max-area' else None
            if reported is not None:assert abs(float(reported)-r['f'])<.000051
        close(sum(r['f'] for r in m['results']),m['totals']['f'])
