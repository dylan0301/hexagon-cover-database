# Statements-and-figures reading edition

This directory is generated from the canonical paper in the parent directory.
It retains the explanatory prose, definitions, formal statements, remarks, and
figures while omitting proof environments and explicitly marked calculation-only
material. Do not edit generated files directly.

Regenerate from the repository root:

```bash
python tools/generate_statements_only_paper.py
```

Build from this directory:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

The complete manuscript and authenticated certificates remain the proof authority.
