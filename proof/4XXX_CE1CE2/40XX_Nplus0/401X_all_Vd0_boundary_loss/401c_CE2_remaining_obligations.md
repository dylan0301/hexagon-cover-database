# Exact CE2 Boundary-Loss Ledger After the One-Gap Completion

Status: Strategy

This note records the sole remaining obstruction in the CE2 half of `401X`.
The no-gap case is proved in `4014`, and the exactly-one-gap case is proved
analytically in `401d`. Only the two-gap case remains.

## Completed CE2 boundary states

Use the exact interval notation from `2106`:

$$
T_C\cap e_{5,0}=[x,U],
\qquad
T_C\cap e_{0,1}=[y,v].
$$

The boundary states are now:

1. Neither center interval contains a V-gap. The open-perimeter lemma in
   `4014`, Section 6 proves this case impossible, including every row-sum
   equality case.
2. Exactly one center interval contains a V-gap. The exact safe-map proof in
   [`401d_CE2_exact_branch_completion.md`](401d_CE2_exact_branch_completion.md)
   proves this case impossible in both orientations.
3. Both center intervals contain V-gaps. This is the remaining state.

## Direct two-gap endpoint reduction

Put

$$
S_0=x+y,
\qquad
R=\frac{x}{S_0},
$$

and define the far-end inputs

$$
p=1-U,
\qquad
q=1-v.
$$

The exact radial demands in `2106` simplify to

$$
c_5=\frac{p}{1-R},
\qquad
c_1=\frac qR.
$$

If both center intervals contain V-gaps, the endpoint roles satisfy

$$
b_5\ge p,
\qquad
a_1\ge q.
$$

Consequently their opposite boundary reaches are bounded by

$$
B_5\le\widehat B_{c_5}(p),
\qquad
B_1\le\widehat B_{c_1}(q).
$$

The center triangle has no boundary trace on

$$
e_{1,2}\cup e_{2,3}\cup e_{3,4}\cup e_{4,5}.
$$

Therefore the exact remaining target is

$$
\boxed{
\widehat B_{p/(1-R)}(p)
+
\widehat B_{q/R}(q)
<1.
}
$$

Indeed, this inequality would leave boundary length

$$
(1-B_1)+1+1+(1-B_5)
=4-(B_1+B_5)>3
$$

for $T_2,T_3,T_4$, contradicting their three nonsupercritical row caps.
This direct reduction avoids the common-$T_0$ realization issue in the older
two-gap propagation chain.

## Exact normalized endpoint domain

After reflection, assume

$$
0<w:=1-R\le\frac12,
\qquad
r:=R=1-w.
$$

Set

$$
K=\sqrt{1-wr},
\qquad
z=\frac{w}{1+K},
\qquad
\zeta=\frac{r}{1+K},
$$

and write

$$
p=w\alpha,
\qquad
q=r\beta.
$$

The strict CE2 midpoint and endpoint inequalities give

$$
\frac12<\alpha<1,
\qquad
\frac12<\beta<1,
$$

$$
\boxed{
\beta+p>1+z,
\qquad
\alpha+q>1+\zeta.
}
$$

Define the scaled safe map

$$
\Phi_s(c)=\widehat B_c(sc).
$$

For the small-weight map $\Phi_w$, a $T_-$ selector would require

$$
\alpha\le2w\alpha,
$$

and is therefore absent when $w<1/2$. For the large-weight map $\Phi_r$,
Full would require $\beta\le1/(1+r)$, whereas

$$
\beta>1+z-p>1+z-w
>\frac1{1+r}.
$$

Thus large-weight Full is absent. The exact $T_-$ and $T_+^{hi}$
parameterizations on the large side both give $\beta\le K$. If small-weight
Full were paired with either of them, then

$$
p>1+z-K=(1+r)z.
$$

But Full also gives $p\le w/(1+w)$, while

$$
(1+r)z>\frac{w}{1+w}.
$$

The last inequality follows from

$$
(1+r)(1+w)>1+K;
$$

after squaring its positive sides, the difference reduces to

$$
w(3-2w-2w^2+w^3)>0.
$$

Hence Full can pair only with $L$.

At the symmetric endpoint $w=r=1/2$, reflect the two endpoint roles when
necessary so that any single $T_-$ label is placed second. If both labels are
low, the low--low estimate below applies directly. Thus the same ordered list
also exhausts the equality case.

The four-label formula in `4015` reduces the possible ordered branch pairs
for

$$
\Phi_w(\alpha)+\Phi_r(\beta)
$$

to

$$
(\mathrm{Full},L),
\quad
(T_+^{hi},L),
\quad
(L,L),
\quad
(L,T_-),
\quad
(L,T_+^{hi}),
\quad
(T_+^{hi},T_-),
\quad
(T_+^{hi},T_+^{hi}).
$$

The pairs $(L,L)$ and $(L,T_-)$ have sum strictly below $K<1$. The
Full--$L$ pair is also excluded exactly. For completeness, if

$$
\beta=h(k):=\sqrt{1-k+k^2},
\qquad
0\le k\le w,
$$

put

$$
B_0=1+z-\frac{w}{1+w},
$$

and

$$
\kappa=\frac{w}{1+(1+w)z}.
$$

Full feasibility and the strict endpoint inequality $\beta+p>1+z$ give

$$
\beta>B_0.
$$

One has

$$
(1+\kappa)B_0=1+z.
$$

Using $K^2=1-w+w^2$, direct common-denominator reduction gives

$$
B_0^2-h(\kappa)^2
=
\frac{w^2\left(A(w)+K C(w)\right)}{D(w,K)},
$$

where $D(w,K)>0$ and

$$
A(w)=8-5w+22w^2+6w^3+5w^4+5w^5-w^6,
$$

$$
C(w)=8-w+14w^2+4w^3-2w^4+w^5.
$$

Here the denominator is explicitly

$$
D(w,K)
=
\left((1+w)(1+K)\right)^2
\left(1+K+w+w^2\right)^2>0.
$$

Both polynomials are positive on $0<w\le1/2$: the possibly negative terms
satisfy

$$
8-5w-w^6>0,
\qquad
8-w-2w^4>0,
$$

and all omitted terms are nonnegative. Hence

$$
h(\kappa)<B_0<\beta=h(k).
$$

Since $h$ decreases and $(1+t)h(t)$ increases on $[0,1/2]$, this gives

$$
(1+k)\beta<1+z.
$$

The first endpoint inequality now implies

$$
k\beta<p,
$$

which proves the Full--$L$ sum is less than one.

The exact pairs still requiring a proof are therefore

$$
\boxed{
(T_+^{hi},L),
\quad
(L,T_+^{hi}),
\quad
(T_+^{hi},T_-),
\quad
(T_+^{hi},T_+^{hi}).
}
$$

No numerical scan or unselected algebraic root proves these four cases.

## Simultaneous replacement fallback

The strengthened theorem in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2104_CE2_one_interval_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2104_CE2_one_interval_lemma.md)
constructs one complementary corner triangle $\Delta(U,v)$ that covers both
gaps and the $V_0$ radial demand. Exact unit enlargement makes it a
supercritical Vd0 row. Thus, at the skeleton level, the two-gap $401X$ state
reduces to the all-boundary-covered CE2, $N_+=1$, all-Vd0 state in `410X`.

That replacement does not preserve the full interior hexagon cover, so the
still-open all-boundary-covered transfer in `4101` cannot be used as a proof
of the original `401X` branch. The direct four-pair target above or a
full-cover-preserving replacement argument is still required.

## Exact remaining obligation

To promote the combined `4013` package to `Proven`, it is necessary and
sufficient within the recorded reduction to discharge the four high-label
endpoint pairs above. The CE1 matrix, CE2 no-gap case, CE2 one-gap case, and
arbitrary replacement-exit classification are no longer open items.
