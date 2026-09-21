#!/usr/bin/env python3
"""Render the linked Markdown trees as one offline, MathML-enabled HTML file.

Build-time dependencies: requirements.txt and Node's mathjax-full@3.2.2.
The generated HTML needs neither a server nor external scripts or fonts.
"""
from __future__ import annotations
import argparse
import html
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
MATH = re.compile(r'\$\$(.+?)\$\$|(?<!\\)\$([^\n$]+?)(?<!\\)\$', re.S)
NODE_MATH = r"""
const fs = require('fs');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {STATE} = require('mathjax-full/js/core/MathItem.js');
const {SerializedMmlVisitor} = require('mathjax-full/js/core/MmlTree/SerializedMmlVisitor.js');
RegisterHTMLHandler(liteAdaptor());
const doc=mathjax.document('', {InputJax:new TeX({packages:AllPackages.filter(p=>p!=='bussproofs')})});
const visitor=new SerializedMmlVisitor();
const rows=JSON.parse(fs.readFileSync(0,'utf8'));
const result=rows.map(([tex,display])=>{
  const node=doc.convert(tex,{display,end:STATE.CONVERT});
  const mml=visitor.visitTree(node);
  if(mml.includes('<merror'))throw Error('Invalid TeX: '+tex);
  return mml;
});
process.stdout.write(JSON.stringify(result));
"""

def render_pages() -> dict:
    try:
        from markdown_it import MarkdownIt
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise SystemExit('Install the pinned requirements.txt before building.') from exc
    files = sorted(p for p in ROOT.rglob('*.md') if 'node_modules' not in p.parts)
    texts = {p.relative_to(ROOT).as_posix():p.read_text(encoding='utf-8') for p in files}
    ids = {}
    for name,text in texts.items():
        match=re.match(r'# \[([^]]+)\] (.+)',text)
        if not match:
            raise ValueError(f'{name}: expected a bracketed page ID in the first heading')
        if match[1] in ids.values():
            raise ValueError(f'duplicate page ID: {match[1]}')
        ids[name]=match[1]
    expressions=[]
    slots={}
    def collect(m):
        pair=((m[1] if m[1] is not None else m[2]).strip(),m[1] is not None)
        if pair not in slots:
            slots[pair]=len(expressions);expressions.append(pair)
    for text in texts.values():
        for m in MATH.finditer(text): collect(m)
    try:
        proc=subprocess.run(['node','-e',NODE_MATH],input=json.dumps(expressions),
                            text=True,capture_output=True,check=True,timeout=120,cwd=ROOT)
    except (OSError,subprocess.CalledProcessError,subprocess.TimeoutExpired) as exc:
        detail=getattr(exc,'stderr','')
        raise SystemExit('MathML build failed; install mathjax-full@3.2.2 for Node.\n'+str(detail)) from exc
    mathml=json.loads(proc.stdout)
    parser=MarkdownIt('commonmark',{'html':False})
    pages={}
    for name,text in texts.items():
        replacements={}
        def protect(m):
            pair=((m[1] if m[1] is not None else m[2]).strip(),m[1] is not None)
            key=f'MATHPLACEHOLDER{len(replacements)}END'
            tag='div' if pair[1] else 'span'
            cls='math-display' if pair[1] else 'math-inline'
            formula=mathml[slots[pair]].replace('<math ', '<math aria-label="'+html.escape(pair[0],quote=True)+'" ',1)
            replacements[key]=f'<{tag} class="{cls}">{formula}</{tag}>'
            return '\n\n'+key+'\n\n' if pair[1] else key
        rendered=parser.render(MATH.sub(protect,text))
        for key,value in replacements.items():
            if value.startswith('<div'):
                rendered=rendered.replace('<p>'+key+'</p>',value)
            else: rendered=rendered.replace(key,value)
        soup=BeautifulSoup(rendered,'html.parser')
        for a in soup.find_all('a',href=True):
            parsed=urlsplit(a['href'])
            if parsed.scheme:
                a['class']='external';a['target']='_blank';a['rel']='noopener noreferrer'
                continue
            path=(ROOT/Path(name).parent/unquote(parsed.path)).resolve()
            if parsed.path.endswith('.md'):
                rel=path.relative_to(ROOT).as_posix()
                if rel not in ids: raise ValueError(f'{name}: missing page {rel}')
                a['href']='#/'+ids[rel]
                a['class']='node-link'
            elif parsed.path:
                # Local source files are accessed in the repository/folder, not embedded pages.
                a['href']=parsed.path
        for ul in soup.find_all('ul'):
            if not ul.find_parent('ul'):ul['class']='proof-tree'
        for li in reversed(soup.find_all('li')):
            children=li.find('ul',recursive=False)
            if children is None:continue
            details=soup.new_tag('details',open='')
            summary=soup.new_tag('summary')
            for item in list(li.contents):
                if item is children:break
                summary.append(item.extract())
            details.append(summary)
            for item in list(li.contents):details.append(item.extract())
            li.append(details)
        # Definitions are open by default, but can be folded once learned.
        for heading in list(soup.find_all('h2')):
            if heading.get_text()!='Terms used here':continue
            box=soup.new_tag('details',attrs={'class':'local-terms','open':''})
            summary=soup.new_tag('summary');summary.string='Terms used here';box.append(summary)
            sibling=heading.next_sibling
            # Only the first definition paragraph/list belongs to this section.
            while sibling is not None and getattr(sibling,'name',None) is None:
                nxt=sibling.next_sibling;sibling.extract();sibling=nxt
            if sibling is not None:box.append(sibling.extract())
            heading.replace_with(box)
        title=re.match(r'# \[[^]]+\] (.+)',text)[1]
        group='Calculation leaves' if name.startswith('details/') else 'Reference' if name in {'START.md','GLOSSARY.md','NOTATION.md','USING.md'} else 'Proof trees'
        pages[ids[name]]={'id':ids[name],'file':name,'title':title,'group':group,'html':str(soup)}
    return pages

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=ROOT/'index.html')
    ap.add_argument('--check',action='store_true',help='compare output without modifying it')
    args=ap.parse_args()
    pages=render_pages()
    options=[]
    for group in ('Proof trees','Calculation leaves','Reference'):
        options.append('<optgroup label="'+group+'">')
        ordered=sorted((p for p in pages.values() if p['group']==group),key=lambda p:(p['id']!='MAIN',p['id']))
        for p in ordered:options.append(f'<option value="{html.escape(p["id"])}">[{html.escape(p["id"])}] {html.escape(p["title"])}</option>')
        options.append('</optgroup>')
    template=(ROOT/'viewer.html.in').read_text(encoding='utf-8')
    payload=json.dumps(pages,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
    output=template.replace('__PAGE_OPTIONS__',''.join(options)).replace('__PAGE_COUNT__',str(len(pages))).replace('__PAGE_DATA__',payload)
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding='utf-8')!=output:
            raise SystemExit(f'{args.output}: absent or stale; run build.py')
    else:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(output,encoding='utf-8')
    print(f'{len(pages)} pages rendered; {args.output}; '+('up to date' if args.check else 'written'))

if __name__=='__main__':
    main()
