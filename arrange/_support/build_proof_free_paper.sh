#!/usr/bin/env bash

# Re-typeset the canonical manuscript while discarding formal proof bodies.
# Calculations and prose outside a proof environment remain unchanged.

set -euo pipefail

fail() {
  printf 'build_proof_free_paper: %s\n' "$*" >&2
  exit 1
}

if (( $# != 0 )); then
  fail "this command takes no arguments"
fi

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd -P)"
PAPER_SOURCE="$REPO_ROOT/arrange/paper_draft"
OUTPUT_PDF="$PAPER_SOURCE/proof_free.pdf"

[[ -f "$PAPER_SOURCE/main.tex" ]] || fail "missing paper entry point"
command -v latexmk >/dev/null 2>&1 || fail "latexmk is required"
command -v xelatex >/dev/null 2>&1 || fail "xelatex is required"

TEMP_WORKSPACE=""
cleanup() {
  local exit_status=$?
  trap - EXIT INT TERM
  set +e
  if [[ -n "$TEMP_WORKSPACE" \
    && "$TEMP_WORKSPACE" == /tmp/hexagon-cover-proof-free.* \
    && "$TEMP_WORKSPACE" != / \
    && -d "$TEMP_WORKSPACE" \
    && -f "$TEMP_WORKSPACE/.proof-free-workspace" ]]; then
    rm -rf -- "$TEMP_WORKSPACE"
  fi
  exit "$exit_status"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

TEMP_WORKSPACE="$(mktemp -d -t hexagon-cover-proof-free.XXXXXXXX)"
[[ "$TEMP_WORKSPACE" == /tmp/hexagon-cover-proof-free.* \
  && "$TEMP_WORKSPACE" != / \
  && -d "$TEMP_WORKSPACE" ]] || fail "unexpected temporary workspace"
touch "$TEMP_WORKSPACE/.proof-free-workspace"

PAPER_WORKSPACE="$TEMP_WORKSPACE/paper_draft"
cp -a -- "$PAPER_SOURCE" "$PAPER_WORKSPACE"
cd -- "$PAPER_WORKSPACE"

rm -f proof_free.pdf proof_free.aux proof_free.fdb_latexmk proof_free.fls \
  proof_free.log proof_free.out proof_free.toc proof_free.xdv \
  proof_free.synctex.gz

export SOURCE_DATE_EPOCH=946684800
export FORCE_SOURCE_DATE=1
export TZ=UTC

latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -jobname=proof_free \
  -usepretex='\AtBeginDocument{\RenewDocumentEnvironment{proof}{o +b}{}{}}' \
  main.tex

[[ -s proof_free.pdf ]] || fail "the proof-free PDF was not created"
if grep -Eq 'LaTeX Warning: (Reference .* undefined|There were undefined references|Label .* multiply defined)' proof_free.log; then
  fail "undefined or multiply-defined references found"
fi
if grep -Eq 'Overfull \\hbox|Overfull \\vbox' proof_free.log; then
  fail "overfull horizontal or vertical boxes found"
fi

OUTPUT_TEMP="$PAPER_SOURCE/.proof_free.pdf.tmp.$$"
install -m 0644 proof_free.pdf "$OUTPUT_TEMP"
mv -f -- "$OUTPUT_TEMP" "$OUTPUT_PDF"

printf 'Created %s\n' "$OUTPUT_PDF"
