from __future__ import annotations

from pathlib import Path

ROOT = Path('.')


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding='utf-8')


def write(relative: str, text: str) -> None:
    (ROOT / relative).write_text(text, encoding='utf-8')


def replace_section(text: str, start: str, end: str, replacement: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + replacement.rstrip() + '\n\n' + text[j:]


# Remove the legacy convention in which lowercase letters could sometimes mean
# actual reaches. Uppercase is now actual everywhere; lowercase is selected.
relative = 'proof/1XXX_foundations/12XX_V_triangle/1212_vertex_V_triangles_and_Nplus.md'
text = read(relative)
text = replace_section(
    text,
    'When no smaller handoff demands are present, a branch may write',
    'The main branch folders are:',
    r'''Actual maximal incoming and outgoing boundary reaches are always denoted

$$
(A_i,B_i).
$$

Selected lower-bound handoff demands are always denoted

$$
(a_i,b_i).
$$

The two alphabets are never interchanged. A vertex V triangle is
supercritical exactly when its actual reaches satisfy

$$
A_i+B_i>1.
$$

Accordingly the proof-tree count is always

$$
N_+
=
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert.
$$

A selected demand pair with $a_i+b_i>1$ may witness a selected strict ascent,
but it never defines or redefines $N_+$.
''',
)
write(relative, text)

relative = 'proof/1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md'
text = read(relative).replace('a_i', 'A_i').replace('b_i', 'B_i')
write(relative, text)

# Complete the geometric terminology migration, including singular forms.
terminology = [
    ('vertex row', 'vertex V triangle'),
    ('ordinary row', 'ordinary V triangle'),
    ('remaining row', 'remaining V triangle'),
    ('selected rows', 'selected V triangles'),
    ('selected row', 'selected V triangle'),
    ('unique row', 'unique V triangle'),
    ('supercritical row', 'supercritical V triangle'),
    ('row $i$', 'V triangle $i$'),
]
for path in list((ROOT / 'proof').rglob('*.md')) + list((ROOT / 'arrange/paper_draft').rglob('*.tex')):
    text = path.read_text(encoding='utf-8')
    for old, new in terminology:
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

# Tighten the permanent linter: reject only an actual lowercase N_+ definition,
# not nearby explanatory mentions of selected strict ascents.
relative = 'tools/proof_lint.py'
text = read(relative)
old = '''    (r"\\b(?:Vd1/Vd2|T3-like|vertex|ordinary|remaining) rows?\\b", "geometric row terminology"),
    (r"\\brows below\\b", "geometric row terminology"),
    (r"\\brow (?:interface|propagation|coordinates|map|completion)\\b", "geometric row terminology"),
'''
new = '''    (r"\\b(?:Vd1/Vd2|T3-like|vertex|ordinary|remaining|selected|unique|supercritical) rows?\\b", "geometric row terminology"),
    (r"\\brows below\\b", "geometric row terminology"),
    (r"\\brow \\$i\\$", "geometric row terminology"),
    (r"\\brow (?:interface|propagation|coordinates|map|completion|sums?)\\b", "geometric row terminology"),
'''
if old not in text:
    raise RuntimeError('proof_lint terminology block not found')
text = text.replace(old, new)
old = '''    compact = re.sub(r"\\s+", "", text)
    if re.search(r"N_\\+=.{0,180}a_i\\+b_i>1", compact):
        fail(f"N_+ is defined from selected lowercase reaches in {relative}")
'''
new = '''    compact = re.sub(r"\\s+", "", text)
    lowercase_nplus_tokens = (
        r"N_+=\\left\\lvert\\left\\lbracei:a_i+b_i>1",
        r"N_+=\\left\\lvert\\left\\{i:a_i+b_i>1",
    )
    if any(token in compact for token in lowercase_nplus_tokens):
        fail(f"N_+ is defined from selected lowercase reaches in {relative}")
'''
if old not in text:
    raise RuntimeError('proof_lint N_+ block not found')
text = text.replace(old, new)
write(relative, text)
