# Notation and Proof-Package Migration

Date: 2026-08-16  
Branch: `agent/notation-proof-package-consolidation`  
Base: `main` at `ee0fdf4410f844e84348b84d0dfe3359035c60ce`

## Scope

- Standardized the paper on the established terms V triangle and C triangle.
- Made $M_c$, $\overline M_c$, and $\Phi_c$ the public propagation interface.
- Enforced uppercase indexed actual reaches and lowercase indexed selected
  lower bounds in the active semantic interfaces.
- Replaced the auxiliary short-role count by $N_++N_{\rm sp}$.
- Aligned Lean names with the paper while preserving stable theorem IDs.

## Conservative consolidation audit

Deleted only two Markdown files:

1. `1100_C_triangle_overview.md`, merged into `1101_CE_classification.md`;
2. `1200_V_triangle_overview.md`, merged into `1201_V_triangle_types.md`.

Both deleted files were navigation-only shells, had no mathematical proof not
already present in the destination source, and had no inbound dependency edge
outside the generated manifest.  The migration intentionally retained:

- all route indexes;
- all active Definition, Reduction, and Proven sources;
- all 407X provenance-bound files;
- all Strategy 4 certificate sources and data;
- all historical and failed-route archives.

## Provenance policy

The 407X exact-cell files remain byte-for-byte unchanged.  Their older
$g/B/F/G$ and Full/L/$T_-$/$T_+$ symbols are treated as authenticated internal
aliases through the canonical dictionary.  The Strategy 4 computation sources
also remain byte-for-byte unchanged.
