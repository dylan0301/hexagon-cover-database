#!/usr/bin/env python3
"""Protect the pre-review mathematics while allowing reader-facing exposition.

This is a source regression test, not a formal verification of the theorem.
It compares every formal statement and proof environment in both editions with
an authenticated baseline inventory and fingerprints the unchanged proof corpus.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
from collections import Counter
from verify_inline_proofs import expand, results, statement_body

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / 'arrange/paper_draft'
BASELINE = Path(__file__).with_name('readability_baseline.json')
PROOF = re.compile(r'\\begin\{proof\}(?:\[[^\]]*\])?.*?\\end\{proof\}', re.S)
AUDIT_ONLY = {'proof/check.py', 'proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/verify_paper_shortening.py'}
WORDING = {
 'prop:vertex-classification': ('in the exact dictionary of the introduction.', 'in the displayed type dictionary.'),
 'prop:vd0-exact-trace-normalization': ('all three actual maximal reaches and the inequality\n$A_i+B_i>1$ are unchanged.', 'all three actual maximal reaches, and whether the two boundary reaches\nhave sum greater than one, are unchanged.'),
}

def digest(text: str) -> str:
    return hashlib.sha256(re.sub(r'\s+', '', text).encode()).hexdigest()

def inventory(entry: Path, *, revised: bool = True) -> dict:
    text = expand(entry)
    statements = {}
    for item in results(text):
        key = item.labels[0]
        body = item.statement
        if revised and entry == PAPER / 'main.tex' and key in WORDING:
            old, new = WORDING[key]
            if body.count(new) != 1:
                raise ValueError(f'Unexpected editorial wording: {key}')
            body = body.replace(new, old)
        statements[key] = digest(statement_body(body))
    proofs = dict(sorted(Counter(digest(p) for p in PROOF.findall(text)).items()))
    full = {'statements': statements, 'proof_environments': proofs}
    return {'statements': len(statements), 'proof_environments': sum(proofs.values()),
            'sha256': hashlib.sha256(json.dumps(full, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}

def corpus_fingerprint(root: Path) -> dict:
    records = []
    for path in sorted((root / 'proof').rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
            continue
        name = path.relative_to(root).as_posix()
        if name not in AUDIT_ONLY:
            records.append([name, hashlib.sha256(path.read_bytes()).hexdigest()])
    data = json.dumps(records, separators=(',', ':')).encode()
    return {'files': len(records), 'sha256': hashlib.sha256(data).hexdigest()}

def main() -> None:
    baseline = json.loads(BASELINE.read_text())
    for name, entry in [('canonical', PAPER/'main.tex'), ('inline', PAPER/'inline_proofs/main.tex')]:
        current = inventory(entry)
        expected = baseline[name]
        if current != expected:
            raise SystemExit(f'{name}: formal source inventory changed: {current} != {expected}')
        print(f'{name}: {current["statements"]} statements and '
              f'{current["proof_environments"]} complete proof environments preserved')
    if corpus_fingerprint(ROOT) != baseline['proof_corpus']:
        raise SystemExit('Numbered proof / certificate corpus changed beyond the two documented audit files')
    print(f'Proof corpus: {baseline["proof_corpus"]["files"]} files byte-identical to {baseline["base_commit"]}')
    print('Readability preservation: PASS (only two declared nonmathematical statement phrasings normalized)')

if __name__ == '__main__':
    main()
