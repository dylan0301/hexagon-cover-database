#!/usr/bin/env python3
"""Source and provenance contracts for the active F integration, not a geometry prover."""
from pathlib import Path
import hashlib,json,re
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'AGENTS.md').is_file())
PAPER=ROOT/'arrange/paper_draft'
HERE=Path(__file__).resolve().parent
record=json.loads((ROOT/'arrange/_support/f_explicit_integration_manifest.json').read_text())
assert hashlib.sha256((HERE/'verify_explicit_stage.py').read_bytes()).hexdigest()==record['active_program_sha256']
for name,sha in record['protected_legacy'].items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha, name
for path in [PAPER/'E_zero_gap_nine_point_optimization.tex',PAPER/'inline_proofs/06_zero_gap.tex']:
    s=path.read_text()
    for token in ['k_b','k_a','lem:F-normal-pair-bounds','1/\\sqrt3<\\lambda_-',
                  'fixed-start','eq:reader-newton-reduction','prop:technical-four-contact-geometry']:
        assert token in s,(path.name,token)
    assert 'proves the unchanged eight' not in s
    assert r'\widehat\xi_*=\xi_*-\frac' not in s
body=(PAPER/'explicit_comparison/certificate_body.tex').read_text()
for token in ['21500','20000','1063/1700','383','113','208','thm:paper-exact-mixed-certificate',
              'lem:paper-residual-to-tangency','lem:f-boundary-comparisons',r'\ell(m):=\frac{1+5m}{2}']:
    assert token in body,token
radius=(PAPER/'explicit_comparison/radius_lemmas.tex').read_text()
assert '3\\omega^2-4\\omega+4' in radius
assert '3q^2-4q+4' not in radius
for path in [PAPER/'A_zero_gap_exact_certificate.tex',PAPER/'inline_proofs/06_zero_gap.tex']:
    assert r'\input{explicit_comparison/certificate_body}' in path.read_text()
assert not list(HERE.glob('*sos_certificates.json')), 'Do not add discovery-stage SOS witness dependencies'
ci=(ROOT/'.github/workflows/ci.yml').read_text()
assert 'verify_explicit_stage.py' in ci
assert (ROOT/'interactive/f_explicit_comparison.html').is_file()
# Do not reinterpret the historical demo as the active point model.
assert 'Historical junction-start' in (ROOT/'interactive/zero_gap_nine_point_demo.html').read_text()
print('F explicit interfaces: PASS; shared paper proof, fixed-start formulas, exact program hash, and historical bytes checked')
