#!/bin/sh
# Build ab_set_proofs.pdf from ab_set_proofs.md.
#
# Toolchain: pandoc + a LaTeX engine (tectonic, XeTeX-based). Install with:
#     brew install pandoc tectonic      # macOS
# The preprocessing step (pdf_preprocess.py) is required: it wraps the
# \tag{...} display equations in equation* environments (\tag is illegal in
# pandoc's \[...\]), breaks the one over-wide display, and fixes a stray
# Unicode prime — without it the raw pandoc call fails / overflows.
set -e
cd "$(dirname "$0")"

PRE="$(mktemp -t ab_set_proofs_pre).md"
python3 pdf_preprocess.py ab_set_proofs.md "$PRE"

pandoc "$PRE" -o ab_set_proofs.pdf \
    --pdf-engine=tectonic \
    --shift-heading-level-by=-1 \
    --toc --toc-depth=2 \
    -H pdf_header.tex \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V colorlinks=true -V linkcolor=blue -V urlcolor=blue \
    -M title="The ab-set: proofs" \
    -M date="July 7, 2026" \
    --standalone

rm -f "$PRE"
echo "wrote ab_set_proofs.pdf"
