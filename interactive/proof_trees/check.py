#!/usr/bin/env python3
"""Check local links, page definitions, and an optional generated offline viewer.

This audits the presentation, not the numbered proofs or exact certificates.
Uses only the Python standard library. Run with --html after build.py.
"""
from __future__ import annotations
import argparse
from collections import deque
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
PIN = 'f7fe2f89cde04903cba8ba347bd0645abee9b905'

class ViewerParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.math=0; self.errors=[]; self.targets=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='math': self.math+=1
        if tag=='merror': self.errors.append('MathML error')
        if tag=='script' and 'src' in a: self.errors.append('external runtime script')
        if tag in {'img','iframe'} and a.get('src','').startswith(('http:','https:')):
            self.errors.append('external runtime image/frame')
        if tag=='a' and a.get('href','').startswith('#/'):
            self.targets.append(a['href'][2:])

def check(with_html: bool=False) -> dict:
    paths=sorted(p for p in ROOT.rglob('*.md') if 'node_modules' not in p.parts)
    names={p.relative_to(ROOT).as_posix():p for p in paths}
    ids={}; graph={n:set() for n in names}; local=0; sources=0; errors=[]
    for name,p in names.items():
        text=p.read_text(encoding='utf-8')
        title=re.match(r'# \[([^]]+)\] ',text)
        if not title: errors.append(name+': missing page ID'); continue
        if title[1] in ids: errors.append('duplicate ID '+title[1])
        ids[title[1]]=name
        if '## Terms used here' not in text: errors.append(name+': missing local definitions')
        if '## Tree' not in text: errors.append(name+': missing tree')
        if name!='README.md' and not re.search(r'\]\((?:\.\./)?README\.md\)',text):
            errors.append(name+': missing Main link')
        if any(line.rstrip()!=line for line in text.splitlines()): errors.append(name+': trailing whitespace')
        if not text.endswith('\n'): errors.append(name+': missing final newline')
        for url in re.findall(r'\]\(([^\s)]+)\)',text):
            u=urlsplit(url)
            if u.scheme:
                if 'github.com/dylan0301/hexagon-cover-database/blob/' in url:
                    sources+=1
                    if '/blob/'+PIN+'/' not in url: errors.append(name+': unpinned proof source')
                continue
            if not u.path: continue
            target=(p.parent/unquote(u.path)).resolve()
            if not target.is_relative_to(ROOT): errors.append(name+': local link escapes bundle'); continue
            if not target.exists(): errors.append(name+': broken local link '+url); continue
            local+=1
            rel=target.relative_to(ROOT).as_posix()
            if rel in names: graph[name].add(rel)
    reached={'README.md'};todo=deque(reached)
    while todo:
        for dest in graph[todo.popleft()]-reached: reached.add(dest);todo.append(dest)
    if reached!=set(names):errors.append('unreachable pages: '+', '.join(sorted(set(names)-reached)))
    # Regression guard for the distinction that prompted this revision.
    for name in ['README.md','SUPPLIER.md','D.md','MIDPOINTS.md']:
        t=names[name].read_text()
        if 'positive support alone does not imply supplying that midpoint' not in t:
            errors.append(name+': missing support/supplier distinction')
    if 'M_1\\in U_0' not in names['SUPPLIER.md'].read_text():errors.append('missing concrete supplier example')
    for name in ['C-MIDPOINT.md','SELF-MIDPOINT.md','T3-MIDPOINT.md']:
        if 'CALCULATION LEAF' in names[name].read_text():errors.append(name+': midpoint proof hidden behind cutoff')
    math=0
    if with_html:
        path=ROOT/'index.html'
        if not path.exists():errors.append('run build.py before --html')
        else:
            text=path.read_text()
            match=re.search(r'<script id="proof-pages" type="application/json">(.*?)</script>',text,re.S)
            if not match:errors.append('missing embedded pages')
            else:
                pages=json.loads(match[1]);parser=ViewerParser()
                if set(pages)!=set(ids):errors.append('viewer/Markdown page IDs differ')
                for key,page in pages.items():
                    if page['file']!=ids[key]:errors.append('viewer filename differs: '+key)
                    if 'MATHPLACEHOLDER' in page['html']:errors.append('unexpanded math placeholder: '+key)
                    if 'Terms used here' not in page['html']:errors.append('viewer local definitions missing: '+key)
                    parser.feed(page['html'])
                parser.feed(text[:match.start()]+text[match.end():])
                errors.extend(parser.errors);math=parser.math
                errors.extend('broken viewer route '+target for target in parser.targets if target not in pages)
    if errors:raise SystemExit('\n'.join(errors))
    return {'markdown_pages':len(paths),'local_links':local,'pinned_source_links':sources,
            'reachable_pages':len(reached),'mathml_expressions':math,'html_checked':with_html}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--html',action='store_true')
    result=check(ap.parse_args().html)
    print(json.dumps(result,indent=2))
