# Terminal Nine-Point Enclosure Theorem

Status: Proven

## Theorem

Assume

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
\tag{1}
$$

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
c_*=c_{\max}(p,q),
\qquad
h=\frac{\sqrt3}{2},
$$

$$
\eta=h(1-c_*),
\qquad
\mathcal D_\eta
=
\left\{X:\left\lVert X\right\rVert\le\eta\right\}.
$$

Let $Q_-(a,b),Q_0(a,b),Q_+(a,b)$ be the exact asymmetric witnesses defined
in
[`31053_direct_asymmetric_witness_forcing.md`](31053_direct_asymmetric_witness_forcing.md),
and set

$$
K_{\mathrm{wit}}(a,b)
=
\mathcal D_\eta
\mathbin\cup
\left\{Q_-(a,b),Q_0(a,b),Q_+(a,b)\right\}.
\tag{2}
$$

Then

$$
\boxed{
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1,
}
\tag{3}
$$

where $\Lambda(K)$ is the least side length of a closed equilateral triangle
containing the compact set $K$.

## Proof

The forced disk gives $\Lambda(K_{\mathrm{wit}})\ge3(1-c_*)$, so the
claim is immediate if $c_*\le2/3$. Assume $c_*>2/3$ and hence
$0<\eta<h/3$.

The exact Newton construction in
[`31054`](31054_four_cap_enclosure_reduction.md) gives

$$
A\in(Q_0,Q_-),\qquad B=Q_0,\qquad C\in(Q_0,Q_+),
$$

$$
\widehat K=\operatorname{conv}(\mathcal D_\eta\cup\{A,B,C\})
\subseteq\operatorname{conv}(K_{\mathrm{wit}}).
$$

The same note verifies the ordered convex chain in an open $120$-degree
cone and the supporting-line distances

$$
d_{AB},d_{BC}\ge h-2\eta>\eta.
$$

By the four-contact theorem in [`2611`](../../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2611_four_contact_disk_enclosure.md), a minimizing enclosing triangle
has one of four relevant side contacts: $AB$, $BC$, or an exposed disk
tangent through $A$ or $C$. At either point--point contact the support sum
is at least $d+2\eta\ge h$.

For the two tangencies let

$$
\Delta=\operatorname{cross}(C,\mathsf RA)>0,
\quad \nu=\langle C,\mathsf RA\rangle,
$$

$$
P_X(\eta)=(\|X\|^2-\eta^2)\Delta^2-
\bigl((h-2\eta)\|X\|^2-\eta\nu\bigr)^2
\quad(X=A,C).
$$

The rational-envelope and Gram calculation in
[`31055`](31055_rational_radial_envelopes_and_mixed_reduction.md) reduces the
paired residual signs at $\bar\eta=h(1-\bar c)\le\eta$ to the unchanged
eight integer-polynomial signs. The exact three-chart proof in
[`31056`](31056_global_analytic_mixed_positivity.md) establishes those signs
by twenty global Bernstein identities. Paired radius transfer in `2611`
then gives $P_A(\eta),P_C(\eta)\ge0$ at the actual radius.

The two tangent support sums are consequently at least $h$ by Corollary 2.1
of `2611`. All four contacts have support sum at least $h$, so

$$
\Lambda(K_{\mathrm{wit}})
\ge\Lambda(\widehat K)\ge1.
$$

This proves (3). $\square$

## Certificate character

The two supporting-line bounds are analytic. The two paired tangent
residuals use the existing rational upper envelopes, exact elimination, and
twenty global positive-basis identities on three fixed charts. The Newton
points and authenticated polynomial data are unchanged. No numerical
sampling, interval subdivision, or branch-and-bound replaces the certificate.
The terminal geometry no longer uses a Minkowski sum or support-cap covering.
