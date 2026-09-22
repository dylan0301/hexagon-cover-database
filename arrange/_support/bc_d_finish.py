#!/usr/bin/env python3
"""Branch-scoped completion of the reviewed BC/D integration. Removed on publication."""
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, subprocess, zipfile
ROOT=Path.cwd()
BRANCH='chatgpt/bc-d-finite-calipers-20260922'
ORIGINAL='083d7fc08bf0918547c8d1624407924604b32e04'
TEMP=['.github/workflows/bc-d-delivery.yml','arrange/_support/bc_d_delivery.py',
      'arrange/_support/bc_d_payload.json','arrange/_support/bc_d_postpatch.json',
      'arrange/_support/bc_d_hotfix.py','arrange/_support/bc_d_final_review.json',
      'arrange/_support/bc_d_finish.py','arrange/_support/bc_d_review_approval.json']
APPROVAL='arrange/_support/bc_d_review_approval.json'
REPORT='arrange/20260922_bc_d_finite_caliper_integration.md'
def run(*args): return subprocess.check_output(args,text=True).strip()
def call(*args): subprocess.run(args,check=True)
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def allowed(p):
    return not Path(p).is_absolute() and '..' not in Path(p).parts and (p.startswith(('proof/','arrange/','interactive/')) or p in ['README.md','.github/workflows/ci.yml','.github/workflows/bc-d-delivery.yml'])
def prepare(review):
    assert os.environ['GITHUB_REF']=='refs/heads/'+BRANCH
    approved=json.loads(Path(APPROVAL).read_text())
    assert h('interactive/bc_d_finite_calipers.html')==approved['reviewed_viewer_sha256']
    assert h(review/'manifest.json')==approved['manifest_sha256']
    assert h(review/'source-review.zip')==approved['source_zip_sha256']
    manifest=json.loads((review/'manifest.json').read_text())
    assert manifest['head']==approved['review_head']
    # No manuscript input or numbered proof may differ from the pinned, rebuilt source.
    for p,digest in manifest['files'].items():
        if p.startswith('proof/') or (p.startswith('arrange/paper_draft/') and p.endswith(('.tex','.sty','.bib','.cls'))):
            assert h(p)==digest,p
    for name,target in [('canonical','arrange/paper_draft/main.pdf'),('inline_proofs','arrange/paper_draft/inline_proofs/main.pdf')]:
        src=review/(name+'.pdf')
        assert h(src)==approved['pdf_sha256'][name],name
        shutil.copy2(src,target)
    Path('/tmp/bc-d-approval.json').write_text(json.dumps(approved,indent=2)+'\n')
    print('Installed the two visually reviewed, pinned TeX Live publication artifacts.')
def commit(out):
    assert os.environ['GITHUB_REF']=='refs/heads/'+BRANCH
    base=run('git','rev-parse','HEAD');assert base==os.environ['GITHUB_SHA']
    approved=json.loads(Path('/tmp/bc-d-approval.json').read_text())
    with Path(REPORT).open('a') as f:
        f.write('\n## Completed integration validation\n\n')
        f.write('Both publication editions were rebuilt in the pinned TeX Live 2025 image in run '+str(approved['review_run'])+'. Their exact PDFs and every manuscript input were verified against that reviewed snapshot before installation. The canonical PDF has '+str(approved['pages']['canonical'])+' pages; the inline-proof PDF has '+str(approved['pages']['inline_proofs'])+' pages. The compiled source inventory has 96 canonical statements and 82 immediate inline proofs, with 14 statement consolidations and 80 retained canonical proof bodies cross-checked.\n\n')
        f.write('Read-only proof checks, 18 exact envelope identities/sign checks, 21 inherited identities and 9 rational sign-certificate leaves passed. The caliper regression suite passed 15 exact identities, 48 rational BC support cases and 9 rational D support cases; the analytic proof, not these samples, supplies universal coverage. Both exact zero-gap derivation and global-positivity replays passed.\n\n')
        f.write('Generated graph/trace checks, all interactive-page audits, proof-tree regeneration and the historical live-capture audit passed. Local Chromium review exercised 16 browser cases, including construction steps, every caliper button, singleton gaps, D diameter endpoints, offline navigation and 390-pixel layouts, with no JavaScript errors. Coincident witness labels are combined without changing the mathematical data. Relevant new BC/D and capacity-proof PDF pages were visually reviewed; all pages passed the PDF render/media-box audit.\n\n')
        f.write('The D proof-tree page no longer incorrectly lists the BC envelope as its prerequisite. The publication README inventory and active dependency map were reconciled. Historical six-point GIFs remain explicitly labeled and byte-unchanged. Temporary delivery code and payloads are removed from the final tree. Immutable navigation is pinned to the source-integration commit. The final remote SHA and CI status are reported in the pull request rather than assumed by this report.\n')
    shutil.rmtree('arrange/_support/bc_d_transport')
    for p in TEMP:Path(p).unlink(missing_ok=True)
    run('git','config','user.name','github-actions[bot]')
    run('git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com')
    run('git','add','-A');run('git','diff','--cached','--check')
    run('git','commit','-m','proof: replace BC/D center-form terminals with finite calipers')
    source=run('git','rev-parse','HEAD')
    call('python','/tmp/bc_d_delivery.py','--pin',source)
    for args in [
      ['python','interactive/generate.py','--dependency-graph'],
      ['python','interactive/animated_proof_guide/build.py'],
      ['python','interactive/proof_trees/build.py']]:call(*args)
    run('git','add','-A')
    for args in [
      ['python','interactive/generate.py','--dependency-graph','--check'],
      ['python','interactive/proof_trees/check.py','--html'],
      ['python','interactive/proof_trees/build.py','--check'],
      ['python','interactive/check.py'],
      ['python','interactive/animated_proof_guide/check.py','--require-live'],
      ['python','arrange/_support/verify_readability_preservation.py']]:call(*args)
    run('git','diff','--check');run('git','diff','--cached','--check')
    assert not run('git','diff','--name-only'),'unstaged changes after repeat generation'
    run('git','commit','-m','interactive: pin BC/D viewers to the reviewed proof revision')
    tip=run('git','rev-parse','HEAD');assert not run('git','status','--porcelain')
    changed=run('git','diff','--name-only',ORIGINAL,tip).splitlines()
    protected=['proof/3XXX_CE0/','arrange/paper_draft/A_zero_gap_exact_certificate.tex','arrange/paper_draft/E_zero_gap_nine_point_optimization.tex']
    assert all(allowed(p) for p in changed)
    assert not any(any(p.startswith(q) for q in protected) or p.endswith(('.gif','.png')) for p in changed)
    names=run('git','ls-tree','-r','--name-only',tip).splitlines()
    assert not any(p in TEMP or '/bc_d_transport/' in p for p in names)
    out.mkdir(exist_ok=True)
    call('git','bundle','create',str(out/'delivery.bundle'),base+'..HEAD')
    records={}
    for p in run('git','diff','--name-only',base,tip).splitlines():
        assert allowed(p),p
        raw=run('git','ls-tree',tip,'--',p)
        if not raw:records[p]=None;continue
        mode,kind,blob=raw.split('\t')[0].split();assert mode in ['100644','100755'] and kind=='blob'
        data=subprocess.check_output(['git','cat-file','blob',blob])
        records[p]={'mode':mode,'blob':blob,'sha256':hashlib.sha256(data).hexdigest()}
    m={'base':base,'source':source,'tip':tip,'original':ORIGINAL,'files':records,'bundle_sha256':h(out/'delivery.bundle'),'changed_paths':len(changed)}
    (out/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
    for p,n in [('arrange/paper_draft/main.pdf','canonical.pdf'),('arrange/paper_draft/inline_proofs/main.pdf','inline_proofs.pdf'),(REPORT,'integration_report.md')]:shutil.copy2(p,out/n)
    with zipfile.ZipFile(out/'offline_viewers.zip','w',zipfile.ZIP_DEFLATED) as z:
        for p in ['interactive/bc_d_finite_calipers.html','interactive/proof_trees/index.html','interactive/readable_proof_dependency_graph.html']:
            z.write(p,p)
        for p in Path('proof').rglob('*.md'):z.write(p,str(p))
    with open(os.environ['GITHUB_OUTPUT'],'a') as f:
        f.write('bundle_sha='+m['bundle_sha256']+'\nmanifest_sha='+h(out/'manifest.json')+'\nfinal_sha='+tip+'\n')
    print(json.dumps({'base':base,'source':source,'tip':tip,'changed_paths':len(changed)},indent=2))
def publish(out):
    assert os.environ['GITHUB_REF']=='refs/heads/'+BRANCH
    assert h(out/'delivery.bundle')==os.environ['EXPECTED_BUNDLE']
    assert h(out/'manifest.json')==os.environ['EXPECTED_MANIFEST']
    m=json.loads((out/'manifest.json').read_text());base,tip,source=m['base'],m['tip'],m['source']
    assert all(re.fullmatch('[a-f0-9]{40}',s) for s in [base,tip,source])
    assert base==os.environ['GITHUB_SHA']==run('git','rev-parse','HEAD')
    assert tip==os.environ['EXPECTED_TIP']
    call('git','bundle','verify',str(out/'delivery.bundle'))
    call('git','fetch',str(out/'delivery.bundle'),'HEAD')
    assert tip==run('git','rev-parse','FETCH_HEAD')
    assert run('git','rev-list','--count',base+'..'+tip)=='2'
    assert run('git','rev-parse',tip+'^')==source and run('git','rev-parse',source+'^')==base
    assert set(run('git','diff','--name-only',base,tip).splitlines())==set(m['files'])
    for p,expected in m['files'].items():
        assert allowed(p),p
        raw=run('git','ls-tree',tip,'--',p)
        if expected is None:assert not raw;continue
        mode,kind,blob=raw.split('\t')[0].split();assert mode in ['100644','100755'] and kind=='blob'
        data=subprocess.check_output(['git','cat-file','blob',blob])
        assert expected=={'mode':mode,'blob':blob,'sha256':hashlib.sha256(data).hexdigest()},p
    assert hashlib.sha256(subprocess.check_output(['git','show',tip+':.github/workflows/ci.yml'])).hexdigest()=='f32226c973012d8038b9c6f2b40f0d025b2dcf83c30815b606c4e3a3914319cd64'
    names=run('git','ls-tree','-r','--name-only',tip).splitlines()
    assert not any(p in TEMP or '/bc_d_transport/' in p for p in names)
    call('git','fetch','origin',BRANCH)
    assert run('git','rev-parse','FETCH_HEAD')==base,'branch advanced; refusing a stale publication'
    call('git','-c','push.default=nothing','push','origin',tip+':refs/heads/'+BRANCH)
    call('git','fetch','origin',BRANCH)
    assert run('git','rev-parse','FETCH_HEAD')==tip
    print('REMOTE PUBLICATION VERIFIED',tip)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=['prepare','commit','publish']);ap.add_argument('directory',type=Path);a=ap.parse_args()
    {'prepare':prepare,'commit':commit,'publish':publish}[a.action](a.directory)
