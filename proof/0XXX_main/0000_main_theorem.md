# Main Theorem

Status: Proven

## Theorem

The regular side-$1$ hexagon $H$ cannot be covered by seven open unit
equilateral triangles. Equivalently, for every $L>1$, the regular side-$L$
hexagon $H_L$ cannot be covered by seven closed unit equilateral triangles.

The equivalence is proved in
[`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

## Proof

Assume that seven open unit equilateral triangles cover $H$. Denote the
original open roles by

$$
U_C,U_0,\ldots,U_5,
$$

where $O\in U_C$ and $V_i\in U_i$, and put

$$
T_C=\overline{U_C},
\qquad
T_i=\overline{U_i}.
$$

The seven distinguished points $O,V_0,\ldots,V_5$ are pairwise at distance at
least one, while two points in one open unit triangle are at distance strictly
below one. Hence the seven roles are distinct. Apply the exact-trace
normalization and classifications in
[`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) and
[`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md). The
closed C triangle is exactly one of CE0, CE1, CE2, and each normalized closed
V triangle is exactly one of Vd0, Vd1, Vd2, and T3-like. We retain the open
roles whenever openness or endpoint ownership is used.

Let $(A_i,B_i,C_i)$ be the actual maximal reaches of $T_i$ and define

$$
N_+=\left|\{i:A_i+B_i>1\}\right|.
$$

Let $d$ count Vd1/Vd2 roles, let $t$ count T3-like roles, and put
$N_{\rm sp}=d+t$. A boundary gap is the nonempty closed complement between
the two incident open V traces on one edge; equality of their closed endpoints
therefore gives a singleton gap. Let $N_{\rm gap}$ be the number of gap edges.
Boundary locality and openness give

$$
N_{\rm gap}=0
\quad\Longleftrightarrow\quad
U_0,\ldots,U_5\text{ cover }\partial H.
\tag{1}
$$

Every gap belongs to the open C role, so the center classification gives
$N_{\rm gap}=0$ in CE0, at most one in CE1, and at most two in CE2. The strict
handoff theorem
[`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
passes from the actual reaches to strict selected lower bounds without changing
the exact-one supercritical index and, when $N_+\ge2$, permits a selection with
at least two selected supercritical roles.

The reusable proof interfaces are:

- the zero-gap cyclic area interface
  [`2400`](../2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md);
- the complete length dispatcher
  [`2531`](../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md);
- the terminal-first finite-enclosure interface
  [`2610`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md).

The reader catalog
[`0003`](0003_reusable_lemma_catalog.md) records their detailed source
ownership but is not itself a proof dependency.

### Zero boundary gaps

By (1), the six V roles cover the perimeter and the center type is irrelevant.
The following disjoint rows are exhaustive.

| $N_+$ | Vertex refinement | Closing interface |
|---:|---|---|
| $0$ | arbitrary | `2531`, row Z0 |
| $1$ | $d\ge1$ | `2531`, row Z1 |
| $1$ | $d=0$, $t\ge1$ | `2400`, one-ascent exceptional-loss row |
| $1$ | $(d,t)=(0,0)$ | `2610`, Terminal F |
| at least $2$ | arbitrary | `2400`, multiple-ascent row |

Thus every zero-gap state is impossible.

### Nonzero boundary gaps

A nonzero gap forces CE1 or CE2. The signed normal form
[`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md)
shows that the C role contains exactly one radial midpoint. If $N_+\ge2$, a
supercritical role away from that midpoint misses its own midpoint; diameter
locality forces a distinct adjacent positive-support rescuer. Hence
$N_{\rm sp}\ge1$, and `2531`, row S1, applies. More generally `2531`, row S0,
removes every state with

$$
N_++N_{\rm sp}\ge3.
$$

It remains that $N_+\in\{0,1\}$ and $N_++d+t\le2$. The surviving rows are
exactly the following.

| $N_+$ | $(d,t)$ | Center | Closing interface |
|---:|---:|---|---|
| $0$ | $(0,0)$ | CE1/CE2 | `2610`, Terminal A or B according to the gap rank |
| $0$ | $d\ge1$ | CE1/CE2 | `2531`, row P0 |
| $0$ | $(0,1)$ or $(0,2)$ | CE1/CE2 | `2610`, Terminal A or B |
| $1$ | $(0,0)$ | CE1/CE2 | `2610`, Terminal C for one gap and B for two gaps |
| $1$ | $(0,1)$ | CE1/CE2 | `2610`, Terminal D for one gap and B for two gaps |
| $1$ | $(1,0)$ | CE1 | `2531`, row P1 |
| $1$ | $(1,0)$ | CE2 | `2610`, one-Vd assembly, using D, E, a length row, or the replacement router |

The rows are mutually exclusive and exhaustive after the two preceding count
reductions. Every row is impossible, contradicting the assumed cover. The
open--closed scaling equivalence in `1003` gives the expanded closed
formulation. $\square$
