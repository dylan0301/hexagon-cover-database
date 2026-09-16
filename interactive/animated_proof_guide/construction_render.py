"""Narrated overlays on genuine app captures; no independent triangle rendering.

The 600-pixel geometry panel always comes from the app. Highlighted intervals,
scan markers, capacity rulers, and magnified crops are explanatory annotations.
Area readouts and optimizer tables are actual DOM screenshots, not invented data.
"""
from __future__ import annotations
import io, math
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

INK='#173047'; TEAL='#087f8c'; PURPLE='#ac168e'; ORANGE='#c06406'
COLORS=[ORANGE,TEAL,'#5c49b6']
FONT=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
def font(n):return ImageFont.truetype(str(FONT),n)
def lines(draw,text,width,face):
    result=[];line=''
    for word in text.split():
        trial=(line+' '+word).strip()
        if draw.textlength(trial,font=face)>width and line:result.append(line);line=word
        else:line=trial
    return result+[line]
def text(draw,xy,message,width=290,size=17,fill=INK):
    x,y=xy
    for line in lines(draw,message,width,font(size)):
        draw.text((x,y),line,font=font(size),fill=fill);y+=size+6
    return y

def draw_narrative(image,scene,frame,index,total,panels=None):
    n=frame['narrative'];kind=n['kind'];zoom=.72 if scene['mode']=='free' else .74 if kind=='area' else 1
    image=image.convert('RGB').resize((600,600),Image.Resampling.LANCZOS)
    native=image.copy();d=ImageDraw.Draw(image)
    def xy(p):return (300+240*zoom*p['x'],300-240*zoom*p['y'])
    def z(i,s):return {'x':(1-s)*math.cos(i*math.pi/3),'y':(1-s)*math.sin(i*math.pi/3)}
    def segment(i,a,b,color,width=5):d.line([xy(z(i,a)),xy(z(i,b))],fill=color,width=width)
    def dot(p,label='',color=PURPLE,r=6):
        x,y=xy(p);d.ellipse((x-r,y-r,x+r,y+r),fill='white',outline=color,width=3)
        if label:d.text((x+9,y-18),label,font=font(15),fill=color,stroke_width=2,stroke_fill='white')
    def scanner(i,s):
        x,y=xy(z(i,s));d.ellipse((x-7,y-7,x+7,y+7),fill=ORANGE,outline='white',width=2)
        d.text((x+10,y+4),'scan',font=font(14),fill=ORANGE,stroke_width=2,stroke_fill='white')
    def show_interval(i,a,b,label,color=TEAL):
        segment(i,a,b,color)
        for s in [a,b]:
            x,y=xy(z(i,s));d.ellipse((x-2,y-2,x+2,y+2),fill='white',outline=color,width=1)
    focus=None
    if kind in ('capacity','actual-bc'):
        i=n['target'];segment(i,0,1,'#c2cdd7',2)
        if kind=='actual-bc':
            rows=n['intervals'];entries=[(f'T{r["role"]}',r['interval'][1] if r['interval'] else None,r['interval']) for r in rows]
            if n['phase']=='own':entries=[entries[1]]
            for k,(label,value,interval) in enumerate(entries):
                if interval:show_interval(i,*interval,label,COLORS[k%3]);dot(z(i,value),label,COLORS[k%3],5)
        else:
            entries=[('own',n['own']),('previous',n['previous']),('next',n['next'])]
            if n['phase']=='own':entries=entries[:1]
            for k,(label,value) in enumerate(entries):
                if value is not None:dot(z(i,value),label,COLORS[k],5)
        scanner(i,n['scan'])
        if n['phase'] in ('maximum','new-input'):
            for p in n['points']:dot(p['point'],('P^' if kind=='actual-bc' else 'D')+str(p['index']),PURPLE,8)
        focus=z(i,n['gamma'])
    elif kind=='supplier':
        i=1;segment(i,0,1,'#aabcca',2);segment(i,0,n['scan'],'#eac389',12);scanner(i,n['scan'])
        if n['phase']!='enter':show_interval(i,n['c'],n['u'],'supplier')
        if n['phase'] in ('epsilon','witness'):
            segment(i,n['u'],1,PURPLE,4);dot(n['point'],'P_T',PURPLE,8);dot(z(i,1),'O',INK,4)
        dot(z(i,.5),'M1','#846321',4);focus=z(1,(n['c']+n['u'])/2)
    elif kind in ('replacement','type'):
        before=kind=='type' or n['phase']=='original'
        if before:segment(n['target'],0,n['scan'],'#eac389',12)
        for row in n['intervals']:
            if before and row['interval']:
                show_interval(row['index'],*row['interval'],'supplier')
        for p in n.get('sourceVertices',[]):
            # Only vertex markers are drawn here; triangle edges remain app pixels.
            outside=any((math.cos((k+1)*math.pi/3)-math.cos(k*math.pi/3))*(p['y']-math.sin(k*math.pi/3))-(math.sin((k+1)*math.pi/3)-math.sin(k*math.pi/3))*(p['x']-math.cos(k*math.pi/3)) < -1e-8 for k in range(6))
            dot(p,'OUT' if outside else '','#ba2525' if outside else '#1765a2',5)
        if before:
            scanner(n['target'],n['scan'])
            active=next((row for row in n['intervals'] if row['index']==n['target'] and row['interval']),None)
            focus=z(n['target'],sum(active['interval'])/2 if active else .5)
        else:
            # Five affected skeleton pieces; no additional coverers are drawn.
            for i in (0,1):segment(i,0,.80 if i==0 else max(n['p2'],1-n['p2']),TEAL,3)
    out=Image.new('RGB',(960,900),'white');draw=ImageDraw.Draw(out)
    draw.rectangle((0,0,960,68),fill=INK)
    title=scene.get('title',scene['id'].replace('-',' ').title())
    text(draw,(20,12),title,850,23,'white')
    out.paste(image,(15,82))
    draw.rounded_rectangle((628,82,945,736),radius=10,fill='#f0f5f8',outline='#d1dee7')
    phase=n.get('phase','').replace('-',' ').upper();text(draw,(645,99),phase,285,20,TEAL)
    def ruler(y,label,value,color=TEAL,start=0,end=None):
        if value is None:return text(draw,(645,y),label+': no term',285,15)
        text(draw,(645,y),f'{label} = {value:.4f}',285,16,color)
        x=650;y+=29;draw.line((x,y,x+267,y),fill='#c7d4df',width=3)
        if end is not None:draw.line((x+267*start,y,x+267*end,y),fill=color,width=7)
        else:draw.line((x,y,x+267*value,y),fill=color,width=5)
        draw.ellipse((x+267*value-5,y-5,x+267*value+5,y+5),fill=color)
        return y+17
    if kind in ('capacity','actual-bc'):
        y=text(draw,(645,144),'ACTUAL ENDPOINTS' if kind=='actual-bc' else 'CAPACITY BOUNDS',285,17)
        if kind=='capacity':
            for label,key,color in [('own','own',COLORS[0]),('previous','previous',COLORS[1]),('next','next',COLORS[2])]:
                y=text(draw,(645,y+7),label+': inspect next',285,16) if n['phase']=='own' and key!='own' else ruler(y+7,label,n[key],color)
        else:
            for k,r in enumerate(n['intervals']):
                y=text(draw,(645,y+7),f'T{r["role"]}: inspect next',285,16) if n['phase']=='own' and r['role']!=n['target'] else ruler(y+7,f'T{r["role"]} inward end',r['interval'][1] if r['interval'] else None,COLORS[k])
        y=text(draw,(645,y+10),f'max = {n["gamma"]:.4f} / Distance from O = {n["radial"]:.4f}' if n['phase'] in ('maximum','new-input') else 'Next: compare the endpoints and take their maximum.',285,18,PURPLE)
        text(draw,(645,y+16),'Take the maximum from V_i. Subtract from 1 to locate the point from O.',285,17)
        text(draw,(645,654),'Only radial witnesses. No boundary witnesses or fitted enclosure.',285,15)
        if kind=='actual-bc' and n['target']==2:text(draw,(645,554),'NEIGHBOR WINS: the own endpoint alone is not the required point.',285,18,PURPLE)
    elif kind=='supplier':
        y=text(draw,(645,148),n['sourceType']+' ORIGINAL TRIANGLE',285,17)
        y=ruler(y+14,'entry c',n['c'],ORANGE);y=ruler(y+6,'exit u',n['u'],TEAL)
        y=ruler(y+6,'epsilon = 1-u',n['epsilon'],PURPLE)
        text(draw,(645,y+18),'P_T = epsilon V1',285,22,PURPLE)
        text(draw,(645,y+56),'The scan is not the witness. The witness is the fixed inward stopping endpoint.',285,16)
    elif kind in ('replacement','type'):
        before=kind=='type' or n['phase']=='original'
        label=n['sourceType'] if before else 'Vd0 + Vd0 OUTPUT'
        y=text(draw,(645,151),label,285,28,PURPLE)
        if before:
            r=frame['metrics'].get('inputRole',frame['metrics']);y=text(draw,(645,y+10),f'Outside vertices o = {r["o"]}; adjacent traces n = {r["n"]}.',285,20)
            text(draw,(645,y+18),'Green is positive adjacent support; the amber band is only the scan path. Blue vertices are inside H; the red OUT vertex is outside H.',285,17)
        else:
            y=text(draw,(645,y+18),f'p1 = {n["p1"]:.2f}; p2 = {n["p2"]:.2f}; epsilon = 0.02',285,19)
            y=text(draw,(645,y+18),'Both new boundary sums are 0.98. Both adjacent-support counts are 0.',285,19)
            text(draw,(645,y+18),'The outputs are intentionally hex-axis aligned. They replace, not depict, the Vd1 input.',285,18,PURPLE)
    elif kind=='area':
        # Native DOM screenshots retain the displayed optimizer values and rows.
        y=144
        for panel in panels or []:
            w=285;hh=round(panel.height*w/panel.width);panel=panel.resize((w,hh),Image.Resampling.LANCZOS)
            if y+hh>655:hh=max(10,655-y);panel=panel.resize((w,hh),Image.Resampling.LANCZOS)
            out.paste(panel,(644,y));y+=hh+12
        text(draw,(645,666),'Best found, not a certified maximum. Loss estimates are not proof bounds.',285,15,PURPLE)
    if focus and kind in ('supplier','replacement','type'):
        # A crop of native app pixels, with the same analytic interval annotation.
        x,y=xy(focus);box=(int(x-26),int(y-19),int(x+26),int(y+19))
        # Magnify only native pixels, NOT oversized scan labels or endpoint rings.
        # Reapply thin trace/endpoint annotations at the inset's final resolution.
        inset=native.crop(box).resize((280,198),Image.Resampling.LANCZOS)
        di=ImageDraw.Draw(inset)
        ray=1 if kind=='supplier' else n['target']
        interval=[n['c'],n['u']] if kind=='supplier' else next((row['interval'] for row in n['intervals'] if row['index']==ray),None)
        def inset_xy(s):
            px,py=xy(z(ray,s));return ((px-box[0])*280/(box[2]-box[0]),(py-box[1])*198/(box[3]-box[1]))
        if interval:
            points=[inset_xy(v) for v in interval]
            di.line(points,fill=TEAL,width=5)
            for (px,py),label,sign in zip(points,['c','u'],[1,-1]):
                di.ellipse((px-4,py-4,px+4,py+4),fill='white',outline=TEAL,width=2)
                tx=max(8,min(248,px+sign*26));ty=max(8,min(169,py+sign*18))
                di.line(((px,py),(tx+5,ty+7)),fill=TEAL,width=1)
                di.text((tx,ty),label,font=font(18),fill=TEAL,stroke_width=3,stroke_fill='white')
        out.paste(inset,(646,475));draw.rectangle((645,474,927,674),outline=PURPLE,width=2)
        text(draw,(645,681),f'Magnified r{ray}: '+('actual covered interval (c, u)' if interval else 'no positive adjacent trace'),285,13)
    draw.line((20,754,940,754),fill='#c8d6df',width=2)
    text(draw,(22,770),frame['caption'],911,20)
    draw.rectangle((20,874,20+int(920*(index+1)/total),881),fill=TEAL)
    draw.text((22,849),'LIVE APP + NATIVE OPTIMIZER READOUTS   |   NUMERICAL ESTIMATES, NOT PROOF BOUNDS' if kind=='area' else 'LIVE APP + LABELED CONSTRUCTION OVERLAYS   |   SCAN MARKERS ARE NOT WITNESSES',font=font(12),fill='#526578')
    draw.text((875,849),f'{index+1:02}/{total}',font=font(12),fill=INK)
    return out


def set_value(page,selector,value):
    page.locator(selector).first.evaluate('(e,v)=>{e.value=String(v);e.dispatchEvent(new Event("change",{bubbles:true}));}',value)

def apply_area_controls(page,frame):
    """Use actual native controls and pointer interaction, not hidden model access."""
    c=frame['areaControls'];mode=c['mode']
    if mode=='max-area':
        set_value(page,'[data-max-area-quality]','high')
        set_value(page,'input[type=number][data-max-area-param="a"]',c['a'])
        set_value(page,'input[type=number][data-max-area-param="b"]',c['b'])
    else:
        page.locator('[data-area-preset="midpoint"]').evaluate('(e)=>e.click()')
        set_value(page,'[data-area-quality]','high')
        canvas=page.locator('#canvas');canvas.scroll_into_view_if_needed()
        # Real pointerdown registers capture. The last pointermove uses subpixel
        # coordinates so the prescribed handoff is not quantized to whole pixels.
        for i,value in enumerate(c['handoffs']):
            box=canvas.bounding_box()
            def pos(t):
                x=(1-t)*math.cos(i*math.pi/3)+t*math.cos((i+1)*math.pi/3)
                y=(1-t)*math.sin(i*math.pi/3)+t*math.sin((i+1)*math.pi/3)
                return [box['x']+box['width']*(.5+.4*x),box['y']+box['height']*(.5-.4*y)]
            start,end=pos(.5),pos(value)
            page.mouse.move(*start);page.mouse.down();page.mouse.move(*end,steps=2)
            canvas.evaluate('(e,p)=>e.dispatchEvent(new PointerEvent("pointermove",{bubbles:true,pointerId:1,pointerType:"mouse",buttons:1,clientX:p[0],clientY:p[1]}))',end)
            page.mouse.up()
        rows=page.locator('#ab-union-controls table').nth(1).locator('tbody tr').evaluate_all('(rs)=>rs.map(r=>[...r.cells].map(c=>c.textContent.trim()))')
        assert all(abs(float(r[2])-v)<.000051 for r,v in zip(rows,c['handoffs'])),(rows,c)
    # Read the displayed results, independently of the generator's expectations.
    values=page.locator('#ab-union-controls .ab-union-readout').evaluate('''e=>{let r={};for(let s of e.querySelectorAll(':scope > span'))r[s.textContent.trim()]=s.nextElementSibling.textContent.trim();return r;}''')
    if mode=='max-area':
        got=float(values['f(a,b) estimate']);expected=frame['metrics']['results'][0]['f']
        assert abs(got-expected)<.000051,(got,expected)
    else:
        got=float(values['Σ f_i estimate']);expected=frame['metrics']['totals']['f']
        assert abs(got-expected)<.000051,(got,expected)
        assert values['rows with a_i+b_i > 1']=='2'
        rows=page.locator('#ab-union-controls table').first.locator('tbody tr').evaluate_all('(rs)=>rs.map(r=>[...r.cells].map(c=>c.textContent.trim()))')
        assert all(abs(float(row[10])-result['f'])<.000051 for row,result in zip(rows,frame['metrics']['results'])),rows
    assert 'stale' not in values['status'] and 'unavailable' not in values['status'],values
    return values

def area_panels(page,mode):
    # Capture only the relevant native readout rows. Styling is presentational:
    # numeric content is never changed or replaced by a reconstructed table.
    old=page.locator('#atlas-area-css')
    if old.count():old.evaluate('(e)=>e.remove()')
    page.add_style_tag(content='''#ab-union-controls .ab-union-readout{width:360px!important;box-sizing:border-box!important;grid-template-columns:160px minmax(0,1fr)!important;column-gap:8px!important;padding:6px!important;font-size:16px!important;}
    #ab-union-controls .ab-union-table{width:360px!important;font-size:14px!important;}
    #ab-union-controls .ab-union-table:first-of-type th:nth-child(n+2):nth-child(-n+7),#ab-union-controls .ab-union-table:first-of-type td:nth-child(n+2):nth-child(-n+7),#ab-union-controls .ab-union-table:first-of-type th:last-child,#ab-union-controls .ab-union-table:first-of-type td:last-child{display:none!important;}''').evaluate('(e)=>e.id="atlas-area-css"')
    read=page.locator('#ab-union-controls .ab-union-readout')
    # Unimportant rows would make the numeric panel unreadably tall.
    read.evaluate('''(e,mode)=>{let keep=mode==='max-area'?['a','b','a+b','f(a,b) estimate','1-f(a,b) estimate','quality']:['Σ f_i estimate','Σ (1-f_i) estimate','rows with a_i+b_i > 1','quality'];for(let s of e.querySelectorAll(':scope > span'))if(!keep.includes(s.textContent.trim())){s.style.display='none';s.nextElementSibling.style.display='none';}}''',mode)
    assert read.evaluate('''e=>{const b=e.getBoundingClientRect();return [...e.querySelectorAll(':scope > span,:scope > strong')].filter(x=>getComputedStyle(x).display!=='none').every(x=>{const r=document.createRange();r.selectNodeContents(x);const q=r.getBoundingClientRect();return q.left>=b.left && q.right<=b.right-2;});}'''), 'Native area readout text is clipped'
    result=[Image.open(io.BytesIO(read.screenshot())).convert('RGB')]
    if mode=='area-conj':result.append(Image.open(io.BytesIO(page.locator('#ab-union-controls table').first.screenshot())).convert('RGB'))
    return result
