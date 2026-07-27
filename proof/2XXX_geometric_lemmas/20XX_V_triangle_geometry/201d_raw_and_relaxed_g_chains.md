# Raw and Relaxed $g$-Composition Chains

Status: Proven

This note gives one notation for the transfer arguments used throughout the
CE1/CE2 proof.  The raw transfer is defined for every vertex row.  The
nonsupercritical cap, the free strict-supercritical envelope, center intervals,
selected-$T_+$ chords, threshold jumps, and Vd radial estimates are then
proof-safe relaxations or specializations of the same transfer scheme.

The distinction between supercritical and nonsupercritical rows remains useful
for choosing an envelope, but it is not built into the definition of a
$g$-composition chain.

## 1. Raw and capped transfers

For $0\le a,c\le1$, let $B_c(a)$ be the exact maximal outgoing demand proved in
[`2007`](2007_max_b_map.md).  Define

$$
\boxed{g_c(a)=1-B_c(a).}
$$

Coordinatewise down-closedness of the admissible set makes $B_c$ nonincreasing
in $a$, so $g_c$ is nondecreasing.

Let an actual vertex role have incoming reach at least $a$, radial reach at
least $c$, and outgoing reach $B$.  The same triangle realizes the demand
triple $(a,B,c)$, and therefore

$$
B\le B_c(a).
$$

If no center interval intervenes on the next edge, coverage forces

$$
\boxed{A_{\mathrm{next}}\ge g_c(a).}
$$

This statement applies to every row.

If the row is known to be nonsupercritical, then also $B\le1-a$.  With

$$
F_c(a)=\min\{B_c(a),1-a\},
\qquad
G_c(a)=1-F_c(a),
$$

one has the exact identity

$$
\boxed{G_c(a)=\max\{g_c(a),a\}.}
$$

Thus the usual capped map is obtained from the raw graph by adjoining the
identity lower bound.  In particular,

$$
G_c(a)\ge a.
$$

## 2. Center-assisted transfers

Let $\mathcal R_J$ be the residual-demand operator of
[`2019`](2019_interval_component_and_path_budget.md), where $J$ is empty or a
closed center interval.  Define

$$
\boxed{
\mathfrak g_{c,J}(a)=\mathcal R_J(B_c(a)),
\qquad
\mathcal G_{c,J}(a)=\mathcal R_J(F_c(a)).
}
$$

The edge-handoff lemma and the fact that $\mathcal R_J$ is nonincreasing give

$$
A_{\mathrm{next}}\ge\mathfrak g_{c,J}(a)
$$

for every row, and

$$
A_{\mathrm{next}}\ge\mathcal G_{c,J}(a)
$$

when the nonsupercritical cap is available.  For $J=\varnothing$,

$$
\mathfrak g_{c,\varnothing}=g_c,
\qquad
\mathcal G_{c,\varnothing}=G_c.
$$

## 3. Envelope-transfer form

Let $U$ be any proved upper envelope for the outgoing reach of a specified row
on the relevant input domain.  Put

$$
\boxed{
\mathsf T_{U,J}(a)=\mathcal R_J(U(a)),
\qquad
\mathsf T_U(a)=\mathsf T_{U,\varnothing}(a)=1-U(a).
}
$$

If $U\le V$, then residual monotonicity gives

$$
\boxed{\mathsf T_{U,J}\ge\mathsf T_{V,J}.}
$$

Hence replacing an exact outgoing envelope by a larger and simpler envelope
produces a smaller proof-safe transfer.  The basic dictionary is

| outgoing upper envelope | induced transfer | role in a chain |
|---|---|---|
| $B_c(a)$ | $g_c(a)$ | raw transfer for every row |
| $F_c(a)$ | $G_c(a)$ | capped transfer |
| $1-a$ | $\mathrm I(a)=a$ | identity relaxation |
| $B_{\rm sc}(c)$ | $\mathsf S_c(a)=A_{\rm sc}(c)$ | free strict-supercritical relaxation |

Here

$$
B_{\rm sc}(c)
=
\frac{c+\sqrt{c^2-8c+4}}2,
\qquad
A_{\rm sc}(c)=1-B_{\rm sc}(c),
\qquad
0\le c<\frac12,
$$

and the strict outgoing inequality is

$$
B<B_{\rm sc}(c).
$$

Consequently a following center-free boundary demand is strictly larger than
$\mathsf S_c=A_{\rm sc}(c)$.

## 4. $A_{\rm sc}$ and $B_{\rm sc}$ as envelopes of the raw graph

For fixed $0\le c<1/2$, the strict-supercritical region is exactly

$$
\left\{a:g_c(a)<a\right\}.
$$

Indeed,

$$
g_c(a)<a
\quad\Longleftrightarrow\quad
B_c(a)>1-a,
$$

and the interval-fiber property then permits an outgoing demand
$b>1-a$.

The free strict-supercritical theorem
[`2010`](2010_free_supercritical_max_b.md) therefore has the equivalent form

$$
\boxed{
B_{\rm sc}(c)
=
\sup_{\substack{0\le a\le1\\ g_c(a)<a}}B_c(a),
\qquad
A_{\rm sc}(c)
=
\inf_{\substack{0\le a\le1\\ g_c(a)<a}}g_c(a).
}
$$

Thus $A_{\rm sc}$ and $B_{\rm sc}$ are envelopes of the ordinary raw
$g_c$ graph, rather than a separate transfer mechanism.

At $c=0$, the exact boundary formula is

$$
B_0(a)=\frac{-a+\sqrt{4-3a^2}}2,
\qquad
g_0(a)=1-B_0(a),
$$

and the free envelopes are

$$
A_{\rm sc}(0)=0,
\qquad
B_{\rm sc}(0)=1.
$$

Moreover,

$$
4-3a^2-(2-a)^2=4a(1-a)\ge0,
$$

so $B_0(a)\ge1-a$ and hence

$$
G_0(a)=\max\{g_0(a),a\}=a.
$$

Therefore the literal identification of $A_{\rm sc}$ or $B_{\rm sc}$ with the
capped map $G_0$ is false.  The correct unification is the free-envelope
identity for the raw graph displayed above.

## 5. Relaxed composition

For maps $\Phi_1,\ldots,\Phi_r$, write the chain in row order as

$$
\boxed{
[\Phi_1\mid\cdots\mid\Phi_r](x)
=
(\Phi_r\circ\cdots\circ\Phi_1)(x).
}
$$

Thus the leftmost slot acts first.  Write $\mathrm I^k$ for $k$ consecutive
identity slots.

For branch summaries, write

$$
\boxed{
\mathscr C[
\text{seed};\,
\Phi_1\mid\cdots\mid\Phi_r;\,
\text{terminal}
].
}
$$

This is a chain signature rather than a new function: it records the exact
seed data, the proof-safe lower transfers used in geometric order, and the
final capacity or separation certificate.  The seed and terminal entries may
be tuples when an endpoint-loss argument retains two exact endpoint maps.

### Relaxed-composition lemma

Suppose the actual demands satisfy

$$
x_j\ge\Phi_j(x_{j-1})
\qquad(1\le j\le r),
$$

where every $\Phi_j$ is nondecreasing.  If proof-safe lower transfers satisfy

$$
\underline\Phi_j\le\Phi_j,
$$

then

$$
\boxed{
x_r
\ge
[\underline\Phi_1\mid\cdots\mid\underline\Phi_r](x_0).
}
$$

#### Proof

Put

$$
y_0=x_0,
\qquad
y_j=\underline\Phi_j(y_{j-1}).
$$

If $x_{j-1}\ge y_{j-1}$, then monotonicity and the lower-transfer inequality
give

$$
x_j
\ge
\Phi_j(x_{j-1})
\ge
\Phi_j(y_{j-1})
\ge
\underline\Phi_j(y_{j-1})
=
y_j.
$$

Induction proves the claim.

## 6. Reusable lower transfers

For $0<d<1-\sqrt3/2$, let $e(d)$ be the low-root threshold from
[`2012`](2012_high_radial_low_root_bounds.md).  Define

$$
\boxed{
\Theta_d(x)
=
\begin{cases}
x,&x\le e(d),\\
1-e(d),&x>e(d).
\end{cases}
}
$$

Extensivity and the high-demand threshold give

$$
\boxed{\Theta_d(x)\le G_{1-d}(x).}
$$

For a selected-$T_+$ chord with deficit $d$ and a proved coefficient
$\lambda>-1$, put

$$
\boxed{\mathsf L_{d,\lambda}(x)=x+\lambda(x-d).}
$$

Whenever the corresponding chord estimate has been verified on the selected
arc,

$$
\mathsf L_{d,\lambda}(x)\le G_{1-d}(x).
$$

The CE1 one-gap proof uses

$$
\mathsf L_{\alpha,1-4\alpha},
\qquad
\mathsf L_{m,1-5m}.
$$

The quarter-radial and Vd-corner estimates are used in exactly the same way:
they replace a terminal exact row transfer by a simpler lower transfer on the
branch-specific domain.  The branch tables record which slots are retained
and which are replaced.
