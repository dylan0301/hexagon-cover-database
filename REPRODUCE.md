# Reproducing the proof checks

The permanent GitHub Actions workflow is the authoritative reproducible build.
It pins GitHub Actions by commit, uses TeX Live 2025, pins Python dependencies,
and pins Lean and Mathlib.

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

Use TeX Live 2025 and the fixed environment:

```bash
export SOURCE_DATE_EPOCH=946684800
export FORCE_SOURCE_DATE=1
export TZ=UTC

cd arrange/paper_draft
cp main.pdf /tmp/main.tracked.pdf

rm -f main.pdf main.aux main.fdb_latexmk main.fls main.log main.out \
  main.toc main.xdv main.synctex.gz
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -file-line-error main.tex
cp main.pdf /tmp/main.rebuilt1.pdf

rm -f main.pdf main.aux main.fdb_latexmk main.fls main.log main.out \
  main.toc main.xdv main.synctex.gz
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -file-line-error main.tex
cp main.pdf /tmp/main.rebuilt2.pdf
cp /tmp/main.tracked.pdf main.pdf
cd ../..

python tools/compare_pdfs_semantically.py \
  /tmp/main.tracked.pdf /tmp/main.rebuilt1.pdf --dpi 144
python tools/compare_pdfs_semantically.py \
  /tmp/main.rebuilt1.pdf /tmp/main.rebuilt2.pdf --dpi 144
python tools/verify_pdf_render.py arrange/paper_draft/main.pdf
python tools/generate_verification_summary.py --check
```

The builds must have no unresolved references and no `Overfull \\hbox` or
`Overfull \\vbox` diagnostics.

Raw PDF bytes are not compared. XeTeX and xdvipdfmx can vary document IDs and
compressed-object serialization even between consecutive clean builds. The
semantic checker instead requires equality of page geometry, outlines, page
labels, extracted words and coordinates, hyperlinks, annotations, widgets,
embedded-file names, and exact RGB raster pixels at 144 DPI.

The raw SHA-256 in `arrange/CURRENT_VERIFICATION_SUMMARY.txt` identifies the
canonical tracked PDF artifact; it is not asserted to be the byte output of
every clean rebuild.

## Lean statement project

```bash
cd formalization/strategy2_optimization
lake update
lake exe cache get
lake build
```

The present Lean milestone checks only the exact optimization statements.
The ten theorem proofs intentionally contain `sorry`.

## Archival bundle

```bash
python tools/build_release_bundle.py \
  --output /tmp/hexagon-cover-proof-bundle.zip
```

The bundle contains the paper, current verification metadata, dependency and
provenance manifests, exact certificate code/data, permanent workflow and
verification scripts, and the pinned Lean statement project.
