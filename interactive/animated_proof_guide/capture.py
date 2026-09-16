#!/usr/bin/env python3
"""Capture the genuine deployed visualizer; never silently substitute a redraw.

pip install playwright==1.55.0 Pillow==11.3.0
playwright install chromium
python capture.py --examples /tmp/examples.json --output .
Offline source-bundle mode is only for development and is labeled in provenance.
"""
from __future__ import annotations
import argparse, copy, hashlib, io, json, math, re, textwrap
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

URL = 'https://hexagon-cover-visual.surge.sh/'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

def font(size):
    return ImageFont.truetype(FONT, size) if Path(FONT).exists() else ImageFont.load_default(size=size)

def wrap(draw, text, width, face):
    lines = []; line = ''
    for word in text.split():
        trial = (line + ' ' + word).strip()
        if draw.textlength(trial, font=face) > width and line:
            lines.append(line); line = word
        else: line = trial
    if line: lines.append(line)
    return lines

def decorate(image, scene, frame, index, total):
    # Only headers/captions and explicitly identified supporting-line annotations
    # are added. The geometry image itself comes from the deployed app canvas.
    image = image.convert('RGB').resize((600,600), Image.Resampling.LANCZOS)
    if frame.get('contact'):
        line = frame['contact']; n, k = line['n'],line['k']; dx,dy=-n['y'],n['x']
        pts=[(300+240*(k*n['x']+t*dx),300-240*(k*n['y']+t*dy)) for t in [-4,4]]
        d=ImageDraw.Draw(image);d.line(pts,fill='#a21caf',width=3)
        if line['name'].startswith('tangent'):
            p=(300+240*k*n['x'],300-240*k*n['y']);d.ellipse((p[0]-5,p[1]-5,p[0]+5,p[1]+5),fill='#a21caf')
    if frame.get('supplier'):
        d=ImageDraw.Draw(image);values=frame['supplier'];points=[]
        for t in [values['c'],values['u']]:
            points.append((300+.72*240*(1-t)*.5,300-.72*240*(1-t)*math.sqrt(3)/2))
        d.line(points,fill='#a21caf',width=5)
        for x,y in points:d.ellipse((x-4,y-4,x+4,y+4),fill='white',outline='#a21caf',width=2)
    out=Image.new('RGB',(640,770),'#ffffff');d=ImageDraw.Draw(out)
    d.rectangle((0,0,640,62),fill='#142c42')
    title=scene.get('title',scene['id'].replace('-',' ').title())
    for j,line in enumerate(wrap(d,title,595,font(20))[:2]):d.text((20,8+23*j),line,font=font(20),fill='white')
    out.paste(image,(20,66))
    d.line((20,673,620,673),fill='#cbd5e1',width=1)
    caption=frame['caption']
    if scene['id']=='source-difference':caption=('Isolated demo: a=3/4, b=1/8. Exact endpoints exclude an interior point.' if frame.get('demo') else 'Live BC role: compare endpoint-relaxed and endpoint-fixed source families.')
    for j,line in enumerate(wrap(d,caption,600,font(15))[:3]):d.text((20,683+19*j),line,font=font(15),fill='#142c42')
    footer='APP CAPTURE + LABELED GEOMETRY OVERLAY' if (frame.get('contact') or frame.get('supplier')) else 'LIVE APP CANVAS • LOCAL ILLUSTRATION, NOT A COVER'
    d.text((20,748),footer,font=font(11),fill='#526578')
    d.text((568,748),f'{index+1:02}/{total}',font=font(11),fill='#526578')
    return out

def set_json(page, selector, button, value):
    page.locator(selector).evaluate('(e,v)=>{e.value=JSON.stringify(v)}',value)
    page.locator(button).evaluate('(e)=>e.click()')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--examples',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--expected-dist',type=Path);ap.add_argument('--url',default=URL);ap.add_argument('--only',default='');ap.add_argument('--offline-root',type=Path);ap.add_argument('--offline-bundle',type=Path)
    args=ap.parse_args();data=json.loads(args.examples.read_text());out=args.output;out.mkdir(parents=True,exist_ok=True)
    for folder in ['assets','snapshots']: (out/folder).mkdir(exist_ok=True)
    catalog_path=Path(__file__).with_name('cases.json');catalog=json.loads(catalog_path.read_text()) if catalog_path.exists() else {'cards':[]}
    titles={c['scene']:c['title'] for c in reversed(catalog['cards'])}
    # Shared clips carry neutral geometry titles, never a supplier classification
    # that the capacity-only witness inputs do not establish.
    titles.update({'ce0':'Center class CE0','ce1':'Center class CE1','ce2':'Center class CE2',
      'bc-seven':'BC: one selected gap','bc-eight':'BC: two incident gaps',
      'd-seven':'D: one-gap four-point construction','d-eight':'D: two-gap four-point construction',
      'vd1':'Local Vd1: M1 lies inside','vd2':'Local Vd2: M1 lies inside',
      't3':'Local T3-like: M1 lies inside'})
    chosen=set(args.only.split(',')) if args.only else None
    scenes=[s for s in data['scenes'] if not chosen or s['id'] in chosen]
    errors=[];records=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(**({'executable_path':'/usr/bin/chromium','args':['--no-sandbox']} if args.offline_root else {}))
        page=browser.new_page(viewport={'width':1450,'height':1050},device_scale_factor=1)
        page.on('pageerror',lambda e:errors.append(str(e)))
        if args.offline_root:
            page.set_content((args.offline_root/'index.html').read_text().replace('<script type="module" src="/src/main.ts"></script>',''))
            page.add_style_tag(path=str(args.offline_root/'src/style.css'));page.add_script_tag(path=str(args.offline_bundle))
            provenance={'captureMode':'offline-pinned-source-development','url':None,'scripts':[]}
        else:
            response=page.goto(args.url,wait_until='networkidle',timeout=90000)
            assert response and response.status==200, 'Live app did not return HTTP 200'
            scripts=page.locator('script[src]').evaluate_all('(es)=>es.map(e=>e.src)')
            script_info=[]
            for url in scripts:
                r=page.request.get(url);assert r.status==200
                script_info.append({'url':url,'sha256':hashlib.sha256(r.body()).hexdigest()})
            provenance={'captureMode':'live-surge-browser','url':args.url,'status':response.status,'scripts':script_info}
            if args.expected_dist:
                built={hashlib.sha256(p.read_bytes()).hexdigest() for p in args.expected_dist.rglob('*.js')}
                assert built and all(s['sha256'] in built for s in script_info), 'Deployed JavaScript differs from the pinned source build'
                provenance['sourceBuildMatch']=True
        page.wait_for_timeout(200)
        baseline=json.loads(page.locator('#controller-state').input_value())
        assert baseline['version']==11,'Unsupported controller state version'
        provenance.update({'browser':browser.version,'capturedAt':datetime.now(timezone.utc).isoformat(),'proofRevision':data['proofRevision'],'visualizerRevision':data['visualizerRevision'],'viewport':[1450,1050],'canvas':[600,600]})
        for scene in scenes:
            scene['title']=titles.get(scene['id'],scene['id'].replace('-',' ').title())
            images=[];frame_records=[];canvas_hashes=[];snapshots=[]
            for i,frame in enumerate(scene['frames']):
                # Uniform capture-only zoom keeps whole Free-mode triangles inside the
                # fixed 600-pixel app viewport. No coordinates or geometry are altered.
                zoom=.72 if scene['mode']=='free' else 1
                page.locator('#canvas').evaluate('''(c,z)=>{const x=c.getContext('2d');
                  if(!x._atlasTransform){x._atlasTransform=x.setTransform.bind(x);
                    x.setTransform=function(a,b,c,d,e,f){const z=window._atlasZoom||1;this._atlasTransform(a*z,b*z,c*z,d*z,e+(1-z)*300,f+(1-z)*300);};}
                  window._atlasZoom=z;x._atlasTransform(1,0,0,1,0,0);x.clearRect(0,0,600,600);x.setTransform(1,0,0,1,0,0);
                }''',zoom)
                state=copy.deepcopy(baseline);state['shapeMode']=scene['mode'];state['showCoverOverlay']=False
                for key in ['triangleState','strategy3']:
                    if key in frame:state[key]=frame[key]
                set_json(page,'#controller-state','#controller-state-load',state)
                status=page.locator('#controller-state-status').inner_text()
                assert not re.search(r'error|invalid|reset.*boundar|failed',status,re.I),status
                if frame.get('free'):
                    set_json(page,'#free-state-json','#free-state-load',frame['free'])
                    restored=json.loads(page.locator('#free-state-json').input_value())
                    for requested,actual in zip(frame['free']['triangles'],restored['triangles']):
                        assert requested['hidden']==actual['hidden']
                        assert math.dist(list(requested['center'].values()),list(actual['center'].values()))<1e-10
                    snapshots.append({'kind':'free','state':restored})
                else:
                    restored=json.loads(page.locator('#controller-state').input_value());assert restored['shapeMode']==state['shapeMode']
                    if frame.get('strategy3'):
                        m=scene['mode'].split('-')[-1];wanted=state['strategy3'][m];actual=restored['strategy3'][m]
                        if m=='f':assert wanted['edgeDots']==actual['edgeDots'];assert wanted['pointConstruction']==actual['pointConstruction']
                        else:assert wanted['layout']==actual['layout'];assert wanted['layouts'][wanted['layout']]==actual['layouts'][wanted['layout']]
                        view=frame.get('view','witness');page.locator(f'[data-s3-view="{view}"]').evaluate('(e)=>e.click()')
                        layers=frame.get('layers') or {'fills':view=='sources','outlines':view=='sources','hull':True,'triangle':True,'triangleFill':False}
                        for key,value in layers.items():page.locator(f'[data-s3-layer="{key}"]').evaluate('(e,v)=>{if(e.checked!==v){e.checked=v;e.dispatchEvent(new Event("change",{bubbles:true}));}}',value)
                        if scene['id']=='source-difference':
                            is_demo='Return to live inputs' in page.locator('[data-s3-demo]').inner_text()
                            if is_demo!=bool(frame.get('demo')):page.locator('[data-s3-demo]').evaluate('(e)=>e.click()')
                        side=float(page.locator('[data-strategy3-side]').inner_text())
                        assert abs(side-frame['metrics']['side'])<1.1e-6,(scene['id'],side,frame['metrics']['side'])
                    snapshots.append({'kind':'controller','state':restored})
                page.wait_for_timeout(50)
                # Canvas pixels settle after the queued requestAnimationFrame render.
                page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
                if scene['id']=='source-difference':
                    image=Image.new('RGB',(600,600),'white');d=ImageDraw.Draw(image)
                    for j,label in enumerate(['Endpoint relaxed','Actual endpoint fixed']):
                        shot=Image.open(io.BytesIO(page.locator(f'[data-s3-comparison="{j}"]').screenshot())).convert('RGB').resize((294,294))
                        image.paste(shot,(j*302,35));d.text((10+j*302,8),label,font=font(15),fill='#142c42')
                    info=page.locator('[data-s3-presentation] fieldset').inner_text()
                    display=('a = 3/4, b = 1/8; query (19/40, 3/20).\nThe endpoint-relaxed family has a source.\nFor the exact family: lower-bound side > 1.\nAn interior difference, not just removed boundary.' if frame.get('demo') else 'Live BC source-family comparison.\nThe two panels use the same non-endpoint rules.\nOnly exact endpoint restrictions are relaxed.\nSwitching next to the isolated interior-difference demo.')
                    for j,line in enumerate(display.splitlines()):d.text((12,355+34*j),line,font=font(17),fill='#142c42')
                    if frame.get('demo'):assert '1.042' in info or '1.043' in info,info
                else:image=Image.open(io.BytesIO(page.locator('#canvas').screenshot())).convert('RGB');info=''
                canvas_hashes.append(hashlib.sha256(image.tobytes()).hexdigest())
                images.append(decorate(image,scene,frame,i,len(scene['frames'])))
                frame_records.append({'frame':i,'caption':frame['caption'],'metrics':frame['metrics'],'contact':frame.get('contact'),'supplier':frame.get('supplier'),'view':frame.get('view'),'layers':frame.get('layers'),'demo':frame.get('demo'),**({'inspectorText':info} if info else {})})
            assert len(set(canvas_hashes))>=2,f'{scene["id"]}: the captured geometry never changes'
            assert not errors,errors
            name=scene['id'];poster_index=len(images)-1
            if name=='source-difference':poster_index=7
            images[poster_index].save(out/'assets'/f'{name}.png',optimize=True)
            quantized=[im.quantize(colors=128,method=Image.Quantize.MEDIANCUT) for im in images]
            durations=[220]*len(images);durations[0]=800;durations[-1]=1000
            quantized[0].save(out/'assets'/f'{name}.gif',save_all=True,append_images=quantized[1:],duration=durations,loop=0,optimize=True,disposal=2)
            snap=snapshots[poster_index];(out/'snapshots'/f'{name}.json').write_text(json.dumps(snap['state'],indent=2)+'\n')
            records.append({'id':name,'mode':scene['mode'],'title':scene['title'],'snapshotKind':snap['kind'],'frameCount':len(images),'durationMs':sum(durations),'captureZoom':.72 if scene['mode']=='free' else 1,'canvasDistinctFrames':len(set(canvas_hashes)),'frames':frame_records})
            print(f'Captured {name}: {len(set(canvas_hashes))} geometry frames',flush=True)
        provenance['pageErrors']=errors
        browser.close()
    (out/'capture.json').write_text(json.dumps({'provenance':provenance,'scenes':records},indent=2)+'\n')

if __name__=='__main__':main()
