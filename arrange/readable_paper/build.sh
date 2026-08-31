#!/usr/bin/env bash
set -euo pipefail
rm -f main.aux main.fdb_latexmk main.fls main.log main.out main.toc main.xdv main.synctex.gz
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
if grep -Eq 'LaTeX Warning: (Reference .* undefined|There were undefined references|Label .* multiply defined)' main.log; then
  echo 'Undefined or multiply-defined references found.' >&2
  exit 1
fi
if grep -Eq 'Overfull \\hbox|Overfull \\vbox' main.log; then
  echo 'Overfull box found.' >&2
  grep -E 'Overfull \\hbox|Overfull \\vbox' main.log >&2
  exit 1
fi

rm -f main.aux main.fdb_latexmk main.fls main.log main.out main.toc main.xdv main.synctex.gz
