"""Preprocess ab_set_proofs.md for pandoc->tectonic PDF.

- strip the leading '# ...' title line (title comes from pandoc metadata);
- replace the stray U+2032 prime with an ASCII apostrophe (font coverage);
- break the one over-wide display (the sec.10 polynomial family) into two lines;
- wrap every display-math block containing \\tag{...} in a raw LaTeX
  equation* environment (\\tag is illegal inside pandoc's \\[...\\], and
  equation* avoids duplicate hyperref anchors while still showing the tag).
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
text = open(src).read()

# 1. drop the first-level title line
lines = text.split('\n')
if lines and lines[0].strip().startswith('# '):
    lines = lines[1:]
text = '\n'.join(lines)

# 2. stray Unicode prime -> ASCII apostrophe
text = text.replace('′', "'")

# 3. break the over-wide polynomial-family display (sec. 10)
poly = re.compile(r'\$\$\\Bigl\\\{R\^2-1,.*?a-b\\Bigr\\\}\.\$\$', re.DOTALL)
poly_new = (
    '\n\n\\begin{gather*}\n'
    r'\bigl\{\,R^2-1,\ 4\sigma^2-3,\ 4R^2-3,\ \sigma-1,\ a-\tfrac12,\ '
    r'b-\tfrac12,\ \sigma-\tfrac12,\ w_+,\ w_-,\\' '\n'
    r'\mathcal E(a,b),\ \mathcal E(b,a),\ \mathcal G(a,b),\ \mathcal G(b,a),\ '
    r'(3+a)R^2-3,\ (3+b)R^2-3,\ a-b\,\bigr\}.' '\n'
    '\\end{gather*}\n\n'
)
text, n_poly = poly.subn(lambda m: poly_new, text)

# 4. wrap \tag display blocks in equation*
def wrap(m):
    inner = m.group(1)
    if r'\tag{' in inner:
        return ('\n\n\\begin{equation*}\n' + inner.strip()
                + '\n\\end{equation*}\n\n')
    return m.group(0)


text = re.sub(r'\$\$(.*?)\$\$', wrap, text, flags=re.DOTALL)

open(dst, 'w').write(text)
print(f'wrote {dst}; poly-break applied: {n_poly}')
