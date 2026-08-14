#!/usr/bin/env bash

set -euo pipefail

fail() {
  printf 'rebuild_paper_pinned: %s\n' "$*" >&2
  exit 1
}

if (( $# != 0 )); then
  fail "this command takes no arguments"
fi

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd -P)"
PAPER_SOURCE="$REPO_ROOT/arrange/paper_draft"
CANONICAL_PDF="$PAPER_SOURCE/main.pdf"
CANONICAL_SUMMARY="$REPO_ROOT/arrange/CURRENT_VERIFICATION_SUMMARY.txt"
REQUIREMENTS_FILE="$REPO_ROOT/requirements-proof.txt"
VENV_DIR="$REPO_ROOT/.venv-paper-audit"
VENV_MARKER="$VENV_DIR/.requirements-proof.sha256"
TEXLIVE_IMAGE="ghcr.io/xu-cheng/texlive-historic-debian:2025@sha256:d3e42adc0c8d84bc913bfc33571feaf7037616260a771bb6f027504661568bf6"

[[ -d "$PAPER_SOURCE" ]] || fail "missing paper source directory: $PAPER_SOURCE"
[[ -f "$PAPER_SOURCE/main.tex" ]] || fail "missing paper entry point: $PAPER_SOURCE/main.tex"
[[ -f "$REQUIREMENTS_FILE" ]] || fail "missing pinned requirements: $REQUIREMENTS_FILE"
[[ -f "$SCRIPT_DIR/compare_pdfs_semantically.py" ]] || fail "missing semantic PDF comparator"
[[ -f "$SCRIPT_DIR/verify_pdf_render.py" ]] || fail "missing PDF render verifier"
[[ -f "$SCRIPT_DIR/generate_verification_summary.py" ]] || fail "missing summary generator"
[[ ! -L "$VENV_DIR" ]] || fail "refusing to use symlinked audit environment: $VENV_DIR"
[[ ! -L "$CANONICAL_PDF" ]] || fail "refusing to replace symlinked canonical PDF"
[[ ! -L "$CANONICAL_SUMMARY" ]] || fail "refusing to replace symlinked verification summary"

command -v git >/dev/null 2>&1 || fail "git is required"
GIT_ROOT="$(git -C "$REPO_ROOT" rev-parse --show-toplevel 2>/dev/null)" \
  || fail "the helper must be run from a Git worktree"
[[ "$(cd -- "$GIT_ROOT" && pwd -P)" == "$REPO_ROOT" ]] \
  || fail "resolved repository root does not match the Git worktree"

PYTHON_BIN="$(command -v python3 || true)"
[[ -n "$PYTHON_BIN" ]] || fail "python3 is required"
PYTHON_VERSION="$("$PYTHON_BIN" -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')"
"$PYTHON_BIN" -c 'import sys; raise SystemExit(sys.version_info[:2] != (3, 12))' \
  || fail "Python 3.12 is required; found $PYTHON_VERSION"

command -v flock >/dev/null 2>&1 || fail "flock is required"
LOCK_ID="$("$PYTHON_BIN" -c \
  'import hashlib, sys; print(hashlib.sha256(sys.argv[1].encode()).hexdigest()[:16])' \
  "$REPO_ROOT")"
LOCK_FILE="/tmp/hexagon-cover-paper-$LOCK_ID.lock"
exec 9>"$LOCK_FILE"
flock -n 9 || fail "another canonical paper build is already running"

command -v docker >/dev/null 2>&1 || fail "Docker is required"
docker info >/dev/null 2>&1 \
  || fail "cannot reach the Docker daemon; start Docker or grant this user access"

REQUIREMENTS_HASH="$("$PYTHON_BIN" -c \
  'import hashlib, pathlib, sys; print(hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest())' \
  "$REQUIREMENTS_FILE")"

prepare_audit_environment() {
  printf 'Preparing pinned PDF-audit environment...\n'
  "$PYTHON_BIN" -m venv --clear "$VENV_DIR"
  "$VENV_DIR/bin/python" -m pip install --disable-pip-version-check --no-input \
    -r "$REQUIREMENTS_FILE"
  "$VENV_DIR/bin/python" -c 'import fitz, sympy'
  local marker_tmp="$VENV_MARKER.tmp.$$"
  printf '%s\n' "$REQUIREMENTS_HASH" > "$marker_tmp"
  mv -- "$marker_tmp" "$VENV_MARKER"
}

AUDIT_ENV_CURRENT=0
if [[ -x "$VENV_DIR/bin/python" && -f "$VENV_MARKER" ]]; then
  INSTALLED_HASH="$(<"$VENV_MARKER")"
  if [[ "$INSTALLED_HASH" == "$REQUIREMENTS_HASH" ]] \
    && "$VENV_DIR/bin/python" -c \
      'import fitz, sympy, sys; raise SystemExit(sys.version_info[:2] != (3, 12))' \
      >/dev/null 2>&1; then
    AUDIT_ENV_CURRENT=1
  fi
fi
if (( AUDIT_ENV_CURRENT == 0 )); then
  prepare_audit_environment
fi
AUDIT_PYTHON="$VENV_DIR/bin/python"

TEMP_WORKSPACE=""
PUBLISH_STARTED=0
PUBLISH_COMPLETE=0
PDF_EXISTED=0
SUMMARY_EXISTED=0

cleanup() {
  local exit_status=$?
  trap - EXIT INT TERM
  set +e

  if (( PUBLISH_STARTED == 1 && PUBLISH_COMPLETE == 0 )); then
    printf 'Paper update did not complete; restoring canonical artifacts...\n' >&2
    if (( PDF_EXISTED == 1 )); then
      install -m 0644 "$TEMP_WORKSPACE/original.main.pdf" "$CANONICAL_PDF"
    else
      rm -f -- "$CANONICAL_PDF"
    fi
    if (( SUMMARY_EXISTED == 1 )); then
      install -m 0644 "$TEMP_WORKSPACE/original.verification-summary.txt" \
        "$CANONICAL_SUMMARY"
    else
      rm -f -- "$CANONICAL_SUMMARY"
    fi
  fi

  if [[ -n "$TEMP_WORKSPACE" \
    && "$TEMP_WORKSPACE" == /*/hexagon-cover-paper.* \
    && "$TEMP_WORKSPACE" != "/" \
    && -d "$TEMP_WORKSPACE" \
    && -f "$TEMP_WORKSPACE/.hexagon-cover-paper-workspace" ]]; then
    rm -rf -- "$TEMP_WORKSPACE"
  elif [[ -n "$TEMP_WORKSPACE" ]]; then
    printf 'Refusing to clean unvalidated temporary path: %s\n' "$TEMP_WORKSPACE" >&2
  fi

  exit "$exit_status"
}

trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

TEMP_WORKSPACE="$(mktemp -d -t hexagon-cover-paper.XXXXXXXX)"
[[ "$TEMP_WORKSPACE" == /*/hexagon-cover-paper.* \
  && "$TEMP_WORKSPACE" != "/" \
  && -d "$TEMP_WORKSPACE" ]] \
  || fail "mktemp returned an unexpected workspace path"
touch "$TEMP_WORKSPACE/.hexagon-cover-paper-workspace"

PAPER_WORKSPACE="$TEMP_WORKSPACE/paper_draft"
BUILD1_PDF="$TEMP_WORKSPACE/main.rebuilt1.pdf"
BUILD1_LOG="$TEMP_WORKSPACE/main.rebuilt1.log"
BUILD2_PDF="$TEMP_WORKSPACE/main.rebuilt2.pdf"
BUILD2_LOG="$TEMP_WORKSPACE/main.rebuilt2.log"
TEMP_SUMMARY="$TEMP_WORKSPACE/CURRENT_VERIFICATION_SUMMARY.txt"

paper_source_digest() {
  "$PYTHON_BIN" - "$PAPER_SOURCE" <<'PY'
import hashlib
import os
from pathlib import Path
import sys

root = Path(sys.argv[1])
excluded = {
    "main.aux",
    "main.fdb_latexmk",
    "main.fls",
    "main.log",
    "main.out",
    "main.pdf",
    "main.synctex.gz",
    "main.toc",
    "main.xdv",
}
digest = hashlib.sha256()

for path in sorted(root.rglob("*"), key=lambda item: os.fsencode(item.relative_to(root))):
    relative = path.relative_to(root)
    if len(relative.parts) == 1 and relative.name in excluded:
        continue

    relative_bytes = os.fsencode(relative)
    if path.is_symlink():
        kind = b"L"
        payload = os.fsencode(os.readlink(path))
    elif path.is_dir():
        kind = b"D"
        payload = b""
    elif path.is_file():
        kind = b"F"
        payload = path.read_bytes()
    else:
        raise SystemExit(f"unsupported paper source entry: {relative}")

    for field in (kind, relative_bytes, payload):
        digest.update(len(field).to_bytes(8, "big"))
        digest.update(field)

print(digest.hexdigest())
PY
}

SOURCE_DIGEST_BEFORE="$(paper_source_digest)"
cp -a -- "$PAPER_SOURCE" "$PAPER_WORKSPACE"
SOURCE_DIGEST_AFTER_COPY="$(paper_source_digest)"
[[ "$SOURCE_DIGEST_AFTER_COPY" == "$SOURCE_DIGEST_BEFORE" ]] \
  || fail "paper sources changed while they were being staged; rerun the task"

HOST_UID="$(id -u)"
HOST_GID="$(id -g)"

run_clean_build() {
  local pdf_copy="$1"
  local log_copy="$2"

  docker run --rm \
    --user "$HOST_UID:$HOST_GID" \
    --env SOURCE_DATE_EPOCH=946684800 \
    --env FORCE_SOURCE_DATE=1 \
    --env TZ=UTC \
    --env XDG_CACHE_HOME=/tmp/xdg-cache \
    --volume "$PAPER_WORKSPACE:/paper" \
    --workdir /paper \
    "$TEXLIVE_IMAGE" \
    bash -euo pipefail -c '
      rm -f main.pdf main.aux main.fdb_latexmk main.fls main.log \
        main.out main.toc main.xdv main.synctex.gz
      latexmk -xelatex -interaction=nonstopmode -halt-on-error \
        -file-line-error main.tex
      if grep -Eq '\''LaTeX Warning: (Reference .* undefined|There were undefined references|Label .* multiply defined)'\'' main.log; then
        echo '\''Undefined or multiply-defined references found.'\'' >&2
        exit 1
      fi
      if grep -Eq '\''Overfull \\hbox|Overfull \\vbox'\'' main.log; then
        echo '\''Overfull horizontal or vertical boxes found.'\'' >&2
        grep -E '\''Overfull \\hbox|Overfull \\vbox'\'' main.log >&2
        exit 1
      fi
    '

  cp -- "$PAPER_WORKSPACE/main.pdf" "$pdf_copy"
  cp -- "$PAPER_WORKSPACE/main.log" "$log_copy"
}

printf 'Building paper with pinned TeX Live 2025 (1/2)...\n'
run_clean_build "$BUILD1_PDF" "$BUILD1_LOG"
printf 'Building paper with pinned TeX Live 2025 (2/2)...\n'
run_clean_build "$BUILD2_PDF" "$BUILD2_LOG"

printf 'Auditing rebuilt paper...\n'
"$AUDIT_PYTHON" "$SCRIPT_DIR/compare_pdfs_semantically.py" \
  "$BUILD1_PDF" "$BUILD2_PDF" --dpi 144
"$AUDIT_PYTHON" "$SCRIPT_DIR/verify_pdf_render.py" "$BUILD2_PDF" --dpi 144
"$AUDIT_PYTHON" "$SCRIPT_DIR/generate_verification_summary.py" \
  --pdf "$BUILD2_PDF" --output "$TEMP_SUMMARY"
"$AUDIT_PYTHON" "$SCRIPT_DIR/generate_verification_summary.py" \
  --pdf "$BUILD2_PDF" --output "$TEMP_SUMMARY" --check
git -C "$REPO_ROOT" diff --check

SOURCE_DIGEST_BEFORE_PUBLISH="$(paper_source_digest)"
[[ "$SOURCE_DIGEST_BEFORE_PUBLISH" == "$SOURCE_DIGEST_BEFORE" ]] \
  || fail "paper sources changed during the build; canonical artifacts were not updated"

if [[ -f "$CANONICAL_PDF" ]]; then
  cp -- "$CANONICAL_PDF" "$TEMP_WORKSPACE/original.main.pdf"
  PDF_EXISTED=1
fi
if [[ -f "$CANONICAL_SUMMARY" ]]; then
  cp -- "$CANONICAL_SUMMARY" "$TEMP_WORKSPACE/original.verification-summary.txt"
  SUMMARY_EXISTED=1
fi

PUBLISH_STARTED=1
install -m 0644 "$BUILD2_PDF" "$CANONICAL_PDF"
install -m 0644 "$TEMP_SUMMARY" "$CANONICAL_SUMMARY"

"$AUDIT_PYTHON" "$SCRIPT_DIR/generate_verification_summary.py" --check
git -C "$REPO_ROOT" diff --check
PUBLISH_COMPLETE=1

printf 'Updated arrange/paper_draft/main.pdf\n'
printf 'Updated arrange/CURRENT_VERIFICATION_SUMMARY.txt\n'
