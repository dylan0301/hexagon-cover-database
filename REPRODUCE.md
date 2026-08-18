# Reproducing the proof checks

Two permanent GitHub Actions workflows are authoritative:

- `.github/workflows/paper-rebuild.yml` builds the consolidated manuscript and
  its generated statements-only reading edition, then commits both paper
  artifacts and the canonical verification summary to `main`;
- `.github/workflows/proof-ci.yml` independently verifies the active proof-reference graph,
  exact certificates, Lean scalar-statement elaboration, both semantic paper
  rebuilds, and the archival bundle.

Both workflows pin GitHub Actions by commit, use TeX Live 2025, pin Python
dependencies, and pin Lean and Mathlib.

## Proof-source and certificate checks

```bash
python -m pip install -r requirements-proof.txt
python tools/generate_active_dependency_graph.py --check
python tools/generate_proof_manifest.py --check
python tools/proof_lint.py
python tools/verify_strategy2_pure_algebra.py
python tools/verify_strategy2_spec_sync.py

cd proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/\
3105X_self_contained_direct_Vd0_nine_point/3105X_computation
python verify_mixed_overlap_core_derivation.py
python verify_global_core_positivity.py
```

## Paper

### Canonical GitHub Actions update

Commit manuscript source changes to `main`. The paper-rebuild workflow:

1. runs the proof and source-interface linter;
2. replays the exact Strategy 4 certificate;
3. regenerates `arrange/paper_draft/statements_only/` from the canonical TeX;
4. builds both papers twice in the pinned TeX Live 2025 image;
5. rejects unresolved or duplicate references and overfull boxes;
6. checks stable semantics and rendering for both papers, while applying the
   84--104 page target interval only to the canonical paper;
7. regenerates `arrange/CURRENT_VERIFICATION_SUMMARY.txt` for the canonical PDF;
8. commits both PDFs, the generated statements-only source, and the summary to
   `main`.

The write-enabled workflow itself runs every check asserted before it commits
the generated artifacts. GitHub does not recursively trigger the read-only
push workflow from a commit made with the workflow token; ordinary user pushes
and pull requests run that independent verifier.

For a review branch, dispatch the same workflow manually with that branch as
its ref. After checking that the branch has not advanced during the build, the
workflow commits both paper artifacts and the canonical summary back to that
branch. It then
dispatches the read-only proof workflow explicitly on the resulting artifact commit, so the
post-build verification does not rely on workflow-token pushes recursively
triggering another workflow.

### One-command local update

From a repository checkout:

```bash
tools/rebuild_paper_pinned.sh
```

The helper uses the same pinned TeX Live image, performs two clean builds,
checks stable PDF semantics and rendering, and refreshes the tracked PDF and
summary only after every check succeeds. This helper updates the canonical
paper only; use the commands below to regenerate and build the derived reading
edition locally.

In VS Code, run **Tasks: Run Task** and select
**Paper: Update canonical main.pdf (TeX Live 2025)**. The ordinary LaTeX
Workshop recipe is a preview and does not update the tracked PDF.

### Manual build

```bash
export SOURCE_DATE_EPOCH=946684800
export FORCE_SOURCE_DATE=1
export TZ=UTC

cd arrange/paper_draft
rm -f main.pdf main.aux main.fdb_latexmk main.fls main.log main.out \
  main.toc main.xdv main.synctex.gz
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -file-line-error main.tex
cd ../..

python tools/verify_pdf_render.py arrange/paper_draft/main.pdf
python tools/generate_verification_summary.py
```

The build must have no unresolved references and no `Overfull \\hbox` or
`Overfull \\vbox` diagnostics. The canonical workflow additionally elaborates
the pinned Lean scalar statements, performs two clean TeX builds, compares
their stable PDF semantics and exact rendered pixels, and checks the target
page interval.

### Statements-only reading edition

The reading-edition source is generated from the canonical TeX. Do not edit
files under `arrange/paper_draft/statements_only/` by hand. From the repository
root, synchronize and build it with:

```bash
python tools/generate_statements_only_paper.py

export SOURCE_DATE_EPOCH=946684800
export FORCE_SOURCE_DATE=1
export TZ=UTC

cd arrange/paper_draft/statements_only
rm -f main.pdf main.aux main.fdb_latexmk main.fls main.log main.out \
  main.toc main.xdv main.synctex.gz
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -file-line-error main.tex
cd ../../..

python tools/verify_pdf_render.py \
  arrange/paper_draft/statements_only/main.pdf
python tools/generate_statements_only_paper.py --check
```

The `--check` mode is read-only and fails when the tracked generated source or
its required figures are stale. The read-only workflow additionally compares
two clean pinned reading-edition rebuilds and verifies the rebuilt rendering.

### Semantic rebuild audit

Raw XeTeX/xdvipdfmx bytes can differ in document identifiers and compressed
object serialization. The proof workflow therefore compares the tracked
canonical PDF with two clean canonical builds and compares two clean
statements-only builds by stable semantics: page geometry, outlines, page
labels, extracted words and coordinates, hyperlinks, annotations, widgets,
embedded-file names, and exact RGB raster pixels at 144 DPI.

The raw SHA-256 in `arrange/CURRENT_VERIFICATION_SUMMARY.txt` identifies the
canonical tracked artifact; it is not asserted to equal every clean build's raw
byte stream.

## Lean scalar-statement elaboration

```bash
cd formalization/strategy2_optimization
lake update
lake exe cache get
lake build
```

The current Lean milestone elaborates the scalar statements needed for the
long calculation layer. Its ten theorem bodies are intentional `sorry`
admissions. This is a statement check, not a proof or formalization of the
geometric argument; the complete mathematical proofs remain in the paper and
numbered proof corpus.

## Archival bundle

```bash
python tools/build_release_bundle.py \
  --output /tmp/hexagon-cover-proof-bundle.zip
```

The bundle contains both compiled paper editions and their complete TeX/figure
sources, the complete proof-source tree, current verification metadata,
dependency and provenance manifests, exact certificate code and data,
permanent workflows and all verification/rebuild scripts, and the pinned Lean
scalar-statement elaboration project. The permanent workflow extracts the ZIP
in a clean directory and reruns its source-level checks there.
