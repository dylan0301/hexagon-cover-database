#!/usr/bin/env python3
"""Browser smoke/regression checks for the finite-caliper companion, not a proof."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--screenshots',type=Path);args=ap.parse_args()
    source=(ROOT/'interactive/bc_d_finite_calipers.html').read_text()
    errors=[]
    with sync_playwright() as p:
        exe=shutil.which('chromium') or shutil.which('google-chrome')
        browser=p.chromium.launch(headless=True,executable_path=exe,args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1280,'height':980})
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content(source)
        states=[]
        for mode,count in [('bc',5),('d',4)]:
            page.click('#'+mode+'-tab')
            state=page.evaluate('window.caliperState')
            assert state['mode']==mode and state['pointCount']==count,state
            assert state['minimum']>1,state
            edges=page.locator('#calipers tr').count()
            assert edges>=3
            for _ in range(edges+1):page.click('#next')
            assert page.locator('#calipers .selected').count()==1
            page.locator('#step').evaluate('(e)=>{e.value=1;e.dispatchEvent(new Event("input"))}')
            assert page.evaluate('caliperState.pointCount')==1
            page.locator('#step').evaluate('(e)=>{e.value=e.max;e.dispatchEvent(new Event("input"))}')
            if args.screenshots:
                args.screenshots.mkdir(parents=True,exist_ok=True)
                page.screenshot(path=str(args.screenshots/f'{mode}.png'),full_page=True)
            states.append(state)
        page.click('#bc-tab')
        page.evaluate("document.getElementById('x').value=.4;document.getElementById('y').value=.4;document.getElementById('z').value=.3;document.getElementById('y').dispatchEvent(new Event('input'))")
        assert page.evaluate('caliperState.minimum')>1
        page.set_viewport_size({'width':390,'height':844})
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+2')
        assert not errors,errors
        browser.close()
    print(json.dumps({'browser_errors':errors,'validated_examples':states,'singleton_gap':True,'mobile_width':390},indent=2))
    print('PASS: BC/D tabs, construction steps, calipers, singleton gap, mobile layout; numerical QA only.')
if __name__=='__main__':main()
