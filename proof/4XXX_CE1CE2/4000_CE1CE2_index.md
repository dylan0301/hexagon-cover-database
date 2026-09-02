# CE1/CE2 Branch

Status: Reference

The common signed center form is
[`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
The active branch is organized by reusable length rows and six
finite-enclosure terminals, not by the former composed endpoint-propagation
chains.

## 1. Meaning of the `_new` case directories

The suffix `_new` marks the finite-enclosure replacement of a former
Strategy 2 package.  It does **not** mean “index only.”  Every such directory
contains its active `Status: Proven` proof source:

| Directory | Active proof contents |
|---|---|
| `401X_all_Vd0_boundary_loss_new` | complete \(N_+=0\), all-Vd0 one-gap and two-gap finite-enclosure proof |
| `407X_T3_like_no_Vd1Vd2_new` | complete type-aware T3-like one-gap and two-gap finite-enclosure proof |
| `410X_all_Vd0_new` | all-Vd0 \(N_+=1\) assembly, CE1 direct certificate, and transverse seven-point enclosure |
| `413X_exactly_one_T3_like_new` | complete T3-like supported-endpoint and two-gap proof |
| `414X_CE2_exactly_one_Vd1_Vd2_new` | complete one-Vd placement package: four detailed proofs, replacement, audit, and assembly |

The unsuffixed 401X, 407X, and 410X siblings retain historical Strategy 2
sources.  They are not copies of the finite-enclosure proofs.  In 414X, the
active detailed proof bodies have been moved into the `_new` package; the old
4143, 4144, 4146, 4147, 4148, and 414b paths are now compatibility pointers.

## 2. Common preprocessing

The length dispatcher
[`2531`](../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md)
removes every state with

\[
N_++N_{\rm sp}\ge3
\]

and every nonzero-gap state with \(N_+\ge2\).  The surviving placement rows
have \(N_+\in\{0,1\}\) and \(N_++d+t\le2\).

## 3. Strategy 1 rows

| Row | Branch |
|---|---|
| P0 | \(N_+=0\) with at least one Vd1/Vd2 role, CE1 or CE2 |
| P1 | CE1, \(N_+=1\), at least one Vd1/Vd2 role |
| P2 | CE2, \(N_+=1\), at least two Vd1/Vd2 roles |
| P3 | CE2 one-Vd2 neighboring-midpoint hybrid |
| S0 | \(N_++N_{\rm sp}\ge3\) |
| S1 | \(N_+\ge2\) |

The historical files `4040`, `4041`, `4110`, `4111`, `4123`, `4149`,
`414a`, and `4200` are compatibility wrappers around these rows.

## 4. Strategy 3 terminal map

The terminal-first interface is
[`2610`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md).

| Active package | Adapter responsibility | Terminal |
|---|---|---|
| [`4013_new`](40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | all-Vd0 common pair | A or B |
| [`4070_new`](40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | T3-like neighboring-capacity domination | A or B |
| [`4101_new`](41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md), [`4103`](41XX_Nplus1/410X_all_Vd0_new/4103_transverse_seven_point_enclosure.md) | actual transverse endpoints | C or B |
| [`4130_new`](41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | T3-like supported endpoint | D or B |
| [`4140_new`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | exhaustive one-Vd placements | D, E, Strategy 1, or replacement routing |

## 5. One-Vd package

The active CE2 one-Vd package is self-contained at

[`414X_CE2_exactly_one_Vd1_Vd2_new`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md).

Its internal dependency order is

\[
4141_{\rm new},4142_{\rm new},4143_{\rm new},4144_{\rm new}
\longrightarrow
4145_{\rm new}
\longrightarrow
4140_{\rm new}.
\]

The corrected replacement recomputes the output gap rank: zero routes to
Strategy 1 row Z0, one to Terminal A, and two to Terminal B.  It makes no
input-gap-rank preservation claim.

## 6. Historical material

The old composed boundary-transfer packages remain for provenance and
comparison.  They own no active case.  Their status does not substitute for
the active finite-enclosure sources listed above.
