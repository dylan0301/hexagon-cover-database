#!/usr/bin/env python3
"""Exercise local-file/static-server HTML navigation and manual animation controls."""
import argparse, json, threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass

ap=argparse.ArgumentParser();ap.add_argument('--folder',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--inline',type=Path);a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True)
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(a.folder)))
threading.Thread(target=server.serve_forever,daemon=True).start()
errors=[];failed=[]
with sync_playwright() as p:
    b=p.chromium.launch(**({'executable_path':'/usr/bin/chromium','args':['--no-sandbox']} if a.inline else {}))
    page=b.new_page(viewport={'width':1440,'height':1100})
    page.on('pageerror',lambda e:errors.append(str(e)));page.on('requestfailed',lambda r:failed.append(r.url))
    if a.inline:page.set_content(a.inline.read_text(),wait_until='load')
    else:page.goto(f'http://127.0.0.1:{server.server_address[1]}/index.html',wait_until='networkidle')
    assert page.locator('details.case').count()==47
    page.locator('#image-bc-one').wait_for(state='visible');page.wait_for_function('document.getElementById("image-bc-one").naturalWidth>0')
    page.screenshot(path=str(a.output/'desktop.png'))
    page.locator('#bc-one').screenshot(path=str(a.output/'bc-card.png'))
    play=page.locator('#bc-one button.play');play.click();assert play.get_attribute('aria-pressed')=='true'
    page.locator('#pause').click();assert play.get_attribute('aria-pressed')=='false'
    page.locator('#search').fill('singleton');assert 0<page.locator('details.case:not([hidden])').count()<47
    page.locator('#search').fill('');page.locator('#group').select_option('D');assert page.locator('details.case:not([hidden])').count()==7
    page.evaluate('location.hash="d-vd1-two"');page.wait_for_timeout(100);assert page.locator('#d-vd1-two').evaluate('(e)=>e.open')
    page.locator('#d-vd1-two').screenshot(path=str(a.output/'d-card.png'))
    page.evaluate('location.hash="contact-tangent-a"');page.wait_for_timeout(100)
    page.locator('#contact-tangent-a').screenshot(path=str(a.output/'contact-card.png'))
    page.set_viewport_size({'width':390,'height':844});page.evaluate('location.hash="route"');page.wait_for_timeout(100)
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),'Mobile horizontal overflow'
    page.screenshot(path=str(a.output/'mobile.png'))
    page.evaluate('location.hash="bc-one"');page.wait_for_timeout(100)
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
    page.locator('#bc-one').screenshot(path=str(a.output/'mobile-card.png'))
    assert not errors,errors;assert not failed,failed
    report={'passed':True,'entries':47,'desktop':[1440,1100],'mobile':[390,844],'tests':['images resolve','manual play/pause','search','chapter filter','hash opens correct case','mobile has no horizontal overflow'],'pageErrors':errors,'failedRequests':failed,'browser':b.version}
    (a.output/'browser-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report));b.close()
server.shutdown()
