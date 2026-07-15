# CE0 All-Vd0 Residual-Core Strategy

Status: Strategy

This note records an independent residual-core and forced-disk route for the
CE0, $N_+=1$, all-Vd0 branch. It does not close that branch. The original
research blueprint is preserved verbatim in
[`31031_original_residual_core_draft.md`](31031_original_residual_core_draft.md)
for provenance. Statements in that imported draft have no corpus status unless
they are proved here or in an explicitly linked numbered source.

## Branch target

Use the role notation from
[`1000_problem_statement.md`](../../../../1XXX_foundations/10XX_global_conventions/1000_problem_statement.md):

$$
T_C,T_0,\dots,T_5.
$$

Assume a hypothetical cover of $H$ by these seven open unit equilateral
triangles satisfies all of the following:

$$
T_C\text{ is CE0},\qquad N_+=1,
$$

and every vertex role $T_i$ is Vd0. The CE classification is proved in
[`1101_CE_classification.md`](../../../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md),
the vertex-role classification is proved in
[`1201_V_triangle_types.md`](../../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md),
and the row convention is recorded in
[`1212_vertex_rows_and_Nplus.md`](../../../../1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md).

The CE0 hypothesis forces the six vertex roles to cover $\partial H$. Indeed,
if a boundary point were covered only by the open triangle $T_C$, openness
would give a positive-length interval of an incident edge inside $T_C$, which
would contradict CE0.

Rotate indices so that the unique supercritical actual row is the $V_4$ row.
The branch target is to derive a compact set forced into $T_C$ whose minimum
enclosing equilateral side length is at least $1$.

## Strict handoffs and exact row unions

Distinguish the actual maximal incoming and outgoing reaches of $T_i$ from the
smaller handoff demands selected below. Apply the strict handoff construction
of
[`4104_all_boundary_transfer_to_310X.md`](../../../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4104_all_boundary_transfer_to_310X.md).
Although that note is stored in the combined CE1/CE2 branch, its transfer
theorem is independent of the center-role class.

Let

$$
X_i=V_i+x_i(V_{i+1}-V_i)
$$

be the selected handoff point on $e_{i,i+1}$, and set

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

The handoffs lie strictly inside the overlaps of the adjacent open vertex
roles. They preserve exactly one selected supercritical row and give

$$
x_3<x_2<x_1<x_0<x_5<x_4.
$$

Put

$$
a=a_4=1-x_3,\qquad b=b_4=x_4.
$$

Then

$$
a+b>1,\qquad a^2+ab+b^2<1.
$$

For each $i$, let $R_i(u,v)$ be the $V_i$-placed, corner-cone-clipped closed
$AB$-union determined by incoming demand $u$ and outgoing demand $v$. The
abstract union is recorded in
[`20090_ab_set_index.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20090_ab_set_index.md),
and its exact all-parameter caliper certificate is proved in
[`20095_exact_caliper_certificate.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20095_exact_caliper_certificate.md).

These sets are antitone in their demands:

$$
u'\ge u,\quad v'\ge v
\quad\Longrightarrow\quad
R_i(u',v')\subseteq R_i(u,v).
$$

The chain of handoff coordinates gives, for every $i\ne4$,

$$
a_i\ge1-b,\qquad b_i\ge1-a.
$$

Consequently,

$$
R_i(a_i,b_i)\subseteq R_i(1-b,1-a)
\qquad(i\ne4).
$$

This is the $N_+=1$ comparison that was missing from the unscoped source
draft; no adjacent-extrema conjecture is needed in this branch.

## Actual and model residual sets

Define the plane-interior residual left by the six actual row unions by

$$
\mathcal U_6^\circ
=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5\mathrm{int}\left(R_i(a_i,b_i)\right).
$$

The open/closed argument proved in `4104` gives

$$
\mathcal U_6^\circ\subseteq T_C.
$$

The use of $\mathrm{int}(H)$ and of the interiors of the closed row unions is
essential; an unqualified complement on all of $H$ would not justify this
containment.

Define the asymmetric two-parameter model core by

$$
\mathcal C_{\mathrm{asym}}(a,b)
=
\mathrm{int}(H)
\setminus
\left(
\mathrm{int}\left(R_4(a,b)\right)
\mathbin\cup
\bigcup_{i\ne4}\mathrm{int}\left(R_i(1-b,1-a)\right)
\right).
$$

The comparison inclusions imply

$$
\mathcal C_{\mathrm{asym}}(a,b)
\subseteq\mathcal U_6^\circ
\subseteq T_C.
$$

Replacing the distinguished row union by the same comparison union defines
the symmetric model core

$$
\mathcal C_{\mathrm{sym}}(a,b)
=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5\mathrm{int}\left(R_i(1-b,1-a)\right).
$$

Since $a>1-b$ and $b>1-a$, antitonicity gives

$$
\mathcal C_{\mathrm{sym}}(a,b)
\subseteq
\mathcal C_{\mathrm{asym}}(a,b).
$$

## Proven strict frontier

For the strict domain above, the non-axis frontier of $R_4(a,b)$ is not a
visual conjecture. The exact circle--line--line--circle decomposition, all
five junctions, and the $a^2+ab+b^2=1$ degeneration are proved in
[`20091_ab_union_curve_a_plus_b_gt_1.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).

The line--line junction from that theorem supplies a canonical middle witness
candidate $Q_0(a,b)$. Two further candidates $Q_-(a,b)$ and $Q_+(a,b)$ are to
be defined by exact contacts on the two line pieces. Frontier membership alone
does not prove that these points avoid the five comparison unions. The route
therefore requires separate proofs that

$$
Q_-,Q_0,Q_+\in\mathcal C_{\mathrm{asym}}(a,b).
$$

The stronger radial-depth claim from the imported draft is not used. The
proved midpoint self-cover lemma
[`2005_midpoint_self_cover_lemma.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md)
already gives the precise available consequence: a strictly supercritical
selected row cannot have its own radial midpoint in the corresponding open
vertex role. It does not by itself give a strict radial-depth bound below
$1/2$.

## Symmetric witnesses and forced disk

The symmetric-witness target is to construct an explicit point

$$
P(a,b)\in\mathcal C_{\mathrm{sym}}(a,b)\setminus\left\{O\right\}
$$

and certify its membership throughout the strict parameter domain. Put

$$
P_k=\mathrm{Rot}_{k\pi/3}P,\qquad k=0,\dots,5.
$$

Here $\mathrm{Rot}_\theta$ denotes rotation about $O$ through angle $\theta$.

Rotational invariance places all six points in
$\mathcal C_{\mathrm{sym}}\subseteq T_C$. Their convex hull is a regular
hexagon. Since $T_C$ is convex, it must also contain the centered disk

$$
\mathcal D(a,b)
=
\left\{x:\lVert x\rVert\le
\frac{\sqrt3}{2}\lVert P(a,b)\rVert\right\}.
$$

The disk is forced by the six points; it need not be a subset of either model
core.

Define the compact witness configuration

$$
K_{\mathrm{wit}}(a,b)
=
\mathcal D(a,b)\cup\left\{Q_-(a,b),Q_0(a,b),Q_+(a,b)\right\}.
$$

Once all six symmetric points and the three asymmetric points have certified
core membership, convexity gives

$$
K_{\mathrm{wit}}(a,b)\subseteq T_C.
$$

## Enclosing-triangle target

For a bounded set $K$, use the established enclosing-side functional

$$
\Lambda(K)
=
\inf_{\theta\in[0,2\pi/3)}
\frac{2}{\sqrt3}
\sum_{j=0}^2
\sup_{x\in K}\left\langle x,n_j(\theta)\right\rangle.
$$

The same convention and reduction are recorded in the proven
[`31012_core_graph_two_variable_relaxation.md`](../3101X_six_point/31012_core_graph_two_variable_relaxation.md).
A compact set contained in an open unit equilateral triangle has
$\Lambda<1$, by positive clearance from the three sides.

The terminal target of this route is therefore

$$
\boxed{
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1
}
$$

for every

$$
0<a,b<1,\qquad a+b>1,\qquad a^2+ab+b^2<1.
$$

Together with the certified witness memberships, this inequality would
contradict $K_{\mathrm{wit}}\subseteq T_C$ and close the `3103X` route.

## Status and remaining obligations

| Item | Recorded status | Role in this route |
|---|---|---|
| Strict boundary handoffs and interior-uncovered transfer in `4104` | Reduction | Supplies exact one-supercritical selected data and the containment in $T_C$. |
| Exact all-parameter $AB$-union certificate in `20095` | Proven | Justifies the row-union model without an empirical boundary catalog. |
| Strict four-piece frontier in `20091` | Proven | Supplies exact circle and line pieces and the middle junction. |
| Two-variable convex-hull reduction in `31012` | Proven | Supplies the established neighboring six-point reduction and chain comparison. |
| Symmetric witness construction and uniform core membership | Lemma target | Must produce the six points that force the central disk. |
| Exact definitions and core membership of $Q_-,Q_0,Q_+$ | Lemma target | Must certify the three asymmetric witnesses. |
| Uniform inequality $\Lambda(K_{\mathrm{wit}})\ge1$ | Lemma target | Final analytic obstruction. |
| Plotted core shapes and limiting behavior from the source draft | Empirical | May guide formulas but cannot be cited as proof. |

Until all three lemma targets are proved, this file and the `3103X` package
remain `Strategy`.
