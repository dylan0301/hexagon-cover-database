# Zero-Gap Cyclic Area-Loss Interface

Status: Proven

This source owns the multiple-ascent Strategy 2 route and the retained
one-ascent T3-like alternative proof. The active zero-gap $N_+=1$ route
is the type-independent nine-point terminal in `2610`. This source separates
the local loss profiles from the single cyclic aggregation used globally.

## 1. Inputs

Assume the six original open V roles cover $\partial H$. The strict handoff
theorem
[`1214`](../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
selects numbers $x_i\in(0,1)$ and lower-bound demands

$$
(a_i,b_i)=(1-x_{i-1},x_i).
\tag{1}
$$

Each closed actual V role realizes its selected pair. Selected role $i$ is
supercritical exactly when

$$
x_i>x_{i-1}.
\tag{2}
$$

Let $G_i$ be the normalized area of the part of $T_i$ outside $H$, where a
unit equilateral triangle has normalized area one. The unconditional local
square-loss theorem
[`3205`](../../3XXX_CE0/32XX_Nplus_ge2/3205_unconditional_local_square_loss.md)
gives

$$
G_i\ge\min(a_i,b_i)^2,
\tag{3}
$$

and for a selected supercritical role,

$$
G_i\ge\max(a_i,b_i)^2.
\tag{4}
$$

For a T3-like role, the direct theorem
[`3175`](../../3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3175_direct_T3_like_area_loss.md)
gives nonsupercriticality and, whenever $a_i,b_i\ge m$,

$$
G_i\ge2m-4m^2.
\tag{5}
$$

## 2. Cyclic normalization

Put

$$
m=\min_i x_i,
\qquad
M=\max_i x_i.
$$

The reflection

$$
y_i=1-x_{-i-1}
$$

exchanges the two coordinates of every selected pair, preserves feasibility,
the number of ascents, the Vd0/T3-like distinction, and the total loss. Hence
assume

$$
m\le1-M.
\tag{6}
$$

Then every selected coordinate is at least $m$:

$$
x_i\ge m,
\qquad
1-x_{i-1}\ge1-M\ge m.
\tag{7}
$$

Thus every role has baseline loss $G_i\ge m^2$.

## 3. Multiple-ascent row

### Theorem 3.1

If the selected cycle has at least two supercritical roles, then

$$
\sum_{i=0}^5G_i>1.
$$

### Proof

Choose an ascent leaving a minimum plateau, so $x_{p-1}=m<x_p$. By (4),

$$
G_p\ge(1-m)^2.
$$

Choose a second ascent $q\ne p$. Since
$(1-x_{q-1})+x_q>1$, one of its two coordinates is strictly larger than
$1/2$, and (4) gives

$$
G_q>\frac14.
$$

The other four roles have baseline loss at least $m^2$. Therefore

$$
\sum_iG_i
>
(1-m)^2+\frac14+4m^2
=
5\left(m-\frac15\right)^2+\frac{21}{20}
>1.
\qquad\square
$$

## 4. One-ascent exceptional-profile row

### Theorem 4.1

Suppose the selected cycle has exactly one supercritical role, every role is
Vd0 or T3-like, and at least one role is T3-like. Then

$$
\sum_{i=0}^5G_i>1.
$$

### Proof

Rotate so that the unique ascent leaves the global minimum $m$. The
supercritical role has loss at least $(1-m)^2$. A T3-like role is
nonsupercritical and hence distinct from it; by (5), its loss is at least
$2m-4m^2$. The remaining four roles have baseline loss at least $m^2$.
Consequently

$$
\sum_iG_i
\ge
(1-m)^2+(2m-4m^2)+4m^2
=1+m^2
>1.
\qquad\square
$$

## 5. Actual zero-gap consequences

### Corollary 5.1

The following actual configurations are impossible:

1. $N_{\rm gap}=0$ and $N_+\ge2$;
2. $N_{\rm gap}=0$, $N_+=1$, no V role is Vd1 or Vd2, and at least one V
   role is T3-like.

### Proof

Zero gaps are equivalent to boundary completeness. In the first row, the
at-least-two clause of `1214` supplies a strict selection with at least two
selected ascents, so Theorem 3.1 applies. In the second row, the exact-one
clause preserves the unique actual supercritical index for every strict
selection, so Theorem 4.1 applies.

In either row the six V roles have total normalized inside area strictly below
five. The C role has normalized area one, while $H$ has normalized area six.
Thus the seven roles cannot cover $H$. $\square$

The earlier detailed assemblies
[`3208`](../../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md)
and
[`3174`](../../3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3174_CE0_one_supercritical_T3_certificate.md)
remain Proven source-level derivations of the same two rows.
