
# Manuscript and publication support

`paper_draft/main.tex` is the self-contained publication source. Its body gives
the exact geometric and set-theoretic definitions and the compact interfaces
for three proof methods:

1. trace length;
2. area loss;
3. direct finite enclosure.

Appendix A gives the solved structural, shared-local, and signed-center
optimizations; Appendices B--E give the trace-length, area-loss, nonzero-gap,
and zero-gap optimization modules. Appendix F, whose source retains the
historical filename `A_zero_gap_exact_certificate.tex`, records the exact
mixed-overlap certificate required by the zero-gap nine-point theorem. The
illustrative trace-exact atlas remains available in the repository but is not
part of the canonical manuscript. The numbered files under `proof/` remain the
authority for theorem status and hypotheses; the manuscript is the publication
layer.

## Section-to-proof map

| Manuscript component | Principal proof material |
|---|---|
| Introduction and routing | `0000`; `1001` (Definition); `1003`, `1101`, `1201`, `1214` (Proven) |
| Common geometry and Appendix A | `2004`, `2005`, `2100`, `2109` (Proven) |
| Trace-length method and Appendix B | `2500`, `2510`, `2530`, `2531` (Proven), plus routed terminals |
| Area-loss method and Appendix C | `2400`, `3175`, `3205` (Proven) |
| Nonzero-gap finite enclosure and Appendix D | `2008`; `2608`-`2610`, `4013_new`, `4070_new`, `4101_new`, `4102_new`, `4103`, `4130_new`, `4140_new`, `4144_new` (Proven) |
| Zero-gap nine-point theorem and Appendix E | `31050` (Reference); `31051`-`31059` (Proven); `3105X_computation` |
| Exact polynomial certificate, Appendix F | `3105X_computation` and its provenance manifest |
| Exhaustive completion | `0000` |

## Commands

```bash
python -m pip install -r arrange/_support/requirements.txt
python arrange/build.py --canonical
python arrange/build.py --all
arrange/_support/build_proof_free_paper.sh
```

The canonical build is written to `arrange/_build/canonical.pdf`. The
proof-free command writes `arrange/paper_draft/proof_free.pdf`; it removes
formal proof environments while retaining prose and calculations outside
those environments.

Both commands use a temporary source copy, so LaTeX intermediates do not
pollute the source directory. The tracked canonical PDF is a publication
artifact. CI compares clean rebuilds against it by stable PDF semantics and
rendered pixels.
