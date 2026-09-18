#!/usr/bin/env python3
"""Read-only artifact, source-reference, domain, and numeric replay checks."""
from __future__ import annotations
import argparse, hashlib, json, math, re
from html.parser import HTMLParser
from pathlib import Path
from PIL import Image
from construction_checks import check_frame

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
REQUIRED={'area-max','bc-one','bc-two','bc-singleton','bc-ce1','bc-ce2','d-t3-one','d-t3-two','d-vd1-one','d-vd1-two','replacement-minus','replacement-plus','f-frontier','f-newton','f-disk','contact-ab','contact-bc','contact-tangent-a','contact-tangent-c','area-cyclic','area-ii','area-i-large','area-i-reflected','skeleton-budget','vd2-budget','n0-gap','n0-no-gap','raw-normalization','source-exact','source-difference'}
class Links(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.append(d['id'])
        for k in ['href','src','data-gif','data-poster']:
            if k in d:self.links.append(d[k])

def check(folder=HERE,require_live=False):
    cases=json.loads((folder/'cases.json').read_text());cap=json.loads((folder/'capture.json').read_text());records={s['id']:s for s in cap['scenes']}
    assert cap['provenance']['proofRevision']==cases['proofRevision'];assert cap['provenance']['visualizerRevision']==cases['visualizerRevision']
    if require_live:
        assert cap['provenance']['captureMode']=='live-surge-browser','Delivery must use the actual live website'
        assert cap['provenance'].get('sourceBuildMatch') is True,'Deployed JavaScript must match the pinned source build'
    assert cap['provenance']['pageErrors']==[]
    ids=[c['id'] for c in cases['cards']];assert len(ids)==len(set(ids));assert REQUIRED<=set(ids)
    assert len(records)==40 and len(cases['cards'])==48
    assert set(records)=={c['scene'] for c in cases['cards']}
    all_tex='\n'.join(p.read_text() for p in (ROOT/'arrange/paper_draft').rglob('*.tex'))
    parser=Links();parser.feed((folder/'index.html').read_text());assert len(parser.ids)==len(set(parser.ids))
    for link in parser.links:
        if link.startswith('#'):assert link[1:] in parser.ids,link
        elif not re.match(r'(https?:|data:|mailto:)',link):assert (folder/link).is_file(),link
    for c in cases['cards']:
        if not c['source'].startswith('VISUALIZER:'):assert (ROOT/c['source']).is_file()
        for lab in c['labels']:assert '\\label{'+lab+'}' in all_tex,(c['id'],lab)
    for s in records.values():
        gif=Image.open(folder/'assets'/f'{s["id"]}.gif');poster=Image.open(folder/'assets'/f'{s["id"]}.png')
        assert gif.size==poster.size==((960,900) if s.get('revision')==2 else (640,770))
        assert gif.n_frames==s['frameCount']
        assert (28<=s['frameCount']<=36) if s.get('revision')==2 else s['frameCount']==14
        assert gif.info.get('loop')==0
        assert s['canvasDistinctFrames']>=(1 if s.get('revision')==2 else 2)
        if s.get('revision')==2:
            assert s['visibleGeometryChange']>.003
            if s.get('motion'):
                v=s['motion'];assert v.get('endpointDisplacement',1)>.14 and v.get('inputDisplacement',1)>.45
        if require_live:
            provenance=s.get('captureProvenance',cap['provenance']);assert provenance['captureMode']=='live-surge-browser' and provenance['sourceBuildMatch'] is True
        duration=0;hashes=set()
        for i in range(gif.n_frames):gif.seek(i);duration+=gif.info['duration'];hashes.add(hashlib.sha256(gif.convert('RGB').tobytes()).hexdigest())
        assert len(hashes)>=2 and duration==s['durationMs']
        snap=json.loads((folder/'snapshots'/f'{s["id"]}.json').read_text())
        if s['snapshotKind']=='area-controls':assert snap['schema']==1 and snap['kind']=='hexagon-area-control-recipe' and 'version' not in snap
        else:assert snap['version']==(8 if s['snapshotKind']=='free' else 11)
        if s['id']=='bc-singleton':
            edge=snap['strategy3']['bc']['layouts']['seven'][0];assert edge['split'] and edge['left']==edge['right']
        for f in s['frames']:
            m=f['metrics']
            if s.get('revision')==2:check_frame(s,f)
            if s['mode'].startswith('strategy3-'):
                assert m['sourceCount']==6
                pts=[p for p in m['points'] if p['enabled']];assert len(pts)==m['enabled']
                full={'strategy3-bc':6,'strategy3-d':4,'strategy3-f':9}[s['mode']]
                if len(pts)==full:assert m['side']>=1-1e-8
                if s['id']=='f-disk':assert m['cStar']<=2/3 and 3*(1-m['cStar'])>=1
                if s['mode']=='strategy3-d':assert all(x['ok'] for x in m['conditions'])
                if s['id'].startswith('f-contact-'):
                    line=f['contact'];assert line['maxViolation']<1e-8
                    n,k=line['n'],line['k'];assert abs(n['x']**2+n['y']**2-1)<1e-8
                    assert m['diskRadius']<=k+1e-8
                    assert all(n['x']*p['point']['x']+n['y']*p['point']['y']<=k+1e-8 for p in m['points'][6:])
            if s['id']=='area-cyclic' and s.get('revision')!=2:
                assert m['actualNplus']==2 and m['actualNgap']==0 and min(m['overlaps'])>0
                assert m['totalNormalizedLoss']>1
            if s['id']=='skeleton-budget':assert m['actualNplus']+m['actualNsp']==3 and m['actualTotalTraceLength']<12 and m['centerMidpoints']==1
            if s['id'].startswith('replacement-'):assert m['epsilon']<m['minMargin'] and all(abs(r['A']+r['B']-.98)<1e-8 and r['n']==0 for r in m['roles'])
            if s['id'].startswith('supplier-'):assert m['c']<.5<m['u'] and abs(m['epsilon']+m['u']-1)<1e-10 and m['rescuerRatio']<=m['ratioBound']+1e-8
            if s['id']=='raw-normalization':assert abs(m['A']-2*m['traceCutL'])<1e-8 and abs(m['B']-2*m['traceCutL'])<1e-8
    print('PASS: 48 entries, 40 animated GIFs, 818 states; original checks plus actual radial endpoints, native Area Conj/Max Area, Vd1 inputs, Vd0 outputs and visible movement.')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--folder',type=Path,default=HERE);ap.add_argument('--require-live',action='store_true');a=ap.parse_args();check(a.folder,a.require_live)
