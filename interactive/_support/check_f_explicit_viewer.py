#!/usr/bin/env python3
"""Viewer regressions; numerical diagnostics, not a universal proof."""
from pathlib import Path
import re,subprocess,tempfile
p=Path(__file__).resolve().parents[1]/'f_explicit_comparison.html'
s=p.read_text(); code=re.search(r'<script id="f-model">(.*?)</script>',s,re.S).group(1)
tests=r'''
let count=0;for(let i=1;i<50;i++)for(let j=1;j<50;j++){
 const z=model(i/100,j/50);
 const ok=z.a>=z.b-1e-12&&z.rho<1&&z.a+z.b>1&&z.ks<.5&&z.kb>.5&&z.ka>.5&&z.kb<z.km&&z.ka<z.kp&&z.e0<=z.es+1e-11;
 if(!ok)throw Error('Construction mismatch '+JSON.stringify(z));
 if(z.e0<=1/3&&(z.qA<-1e-10||z.qC<-1e-10))throw Error('Residual diagnostic');
 if(Math.min(...z.contacts)<1-1e-10)throw Error('Contact diagnostic'); count++;
}
console.log('F viewer: '+count+' construction/contact diagnostics passed (not a proof)');
'''
with tempfile.NamedTemporaryFile('w',suffix='.cjs') as f:
 f.write(code+tests);f.flush();subprocess.run(['node',f.name],check=True)
