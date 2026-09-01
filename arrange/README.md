
# Manuscripts and publication support

`arrange/` contains two presentations of the same proof.

## Canonical manuscript

`paper_draft/main.tex` is the self-contained publication source. Its body has
three proof methods:

1. trace length;
2. area loss;
3. direct finite enclosure.

The appendix `A_zero_gap_exact_certificate.tex` records the exact
mixed-overlap certificate required by the zero-gap nine-point theorem.

## Reader-oriented manuscript

`readable_paper/main.tex` reorganizes the same mathematics for navigation. It
separates the local finite-enclosure toolkit, the universal nonzero-gap
terminals, the named nonzero-gap cases, and the zero-gap nine-point
obstruction.

The numbered files under `proof/` remain the authority for theorem status and
hypotheses. The two manuscripts are publication layers, not competing proof
owners.

## Section-to-proof map

| Manuscript component | Principal proof material |
|---|---|
| Introduction and routing | `0000`, `1003`, `1101`, `1201`, `1214`, `2530` |
| Common geometry | `1001`-`1214`, `2004`, `2008`, `2100`, `2109` |
| Trace-length method | `2500`, `2510`, `2520`, `2530` and routed terminals |
| Area-loss method | `317X`, `320X` |
| Nonzero-gap finite enclosure | `2608`, `4013_new`, `4070_new`, `4101_new`, `4102_new`, `4130_new`, `4140_new` |
| Zero-gap nine-point theorem | `31050`-`31059` and `3105X_computation` |
| Exhaustive completion | `0000` |

## Commands

```bash
python -m pip install -r arrange/_support/requirements.txt
python arrange/build.py --canonical
python arrange/build.py --readable
python arrange/build.py --all
arrange/_support/build_proof_free_paper.sh
```

The build command uses a temporary source copy, so LaTeX intermediates do not
pollute the source directories. The tracked PDFs are publication artifacts.
CI compares clean rebuilds against them by stable PDF semantics and rendered
pixels.
