# Exact One-Gap Five-Map Reductions

Status: Reduction

This note reduces the CE1 and CE2 exactly-one-gap subcases of `410X` to
explicit five-map inequalities. Those terminal inequalities are proved in
[`4106_CE1_one_gap_five_map_completion.md`](4106_CE1_one_gap_five_map_completion.md)
and
[`4107_CE2_one_gap_five_map_completion.md`](4107_CE2_one_gap_five_map_completion.md).
This note also records exact witnesses
showing that the two-adjacent-row shortcut inherited from `401X` is not a
valid global replacement for those targets.

## 1. Proof-safe maps

For every nonsupercritical row $i\ne0$, define

$$
F_i(a)=\min\left\{B_{c_i}(a),1-a\right\},
\qquad
G_i(a)=1-F_i(a).
$$

The exact unclassified map $B_c(a)$ is proved in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md).

The safe capped-map theorem in
[`../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4015_B_map_branch_realization.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4015_B_map_branch_realization.md)
proves that the actual outgoing reach is at most $F_i(a)$.
Every $G_i$ is nondecreasing because the exact demand map is nonincreasing in
its incoming argument. Consequently these lower maps may be composed in the
orders used below.

For the strict-supercritical row $T_0$, put

$$
S_+(c)=
\frac{c+\sqrt{c^2-8c+4}}2,
\qquad
0\le c<\frac12,
$$

and

$$
M_c^+(a)=\min\left\{B_c(a),S_+(c)\right\}.
$$

The unclassified exact map bounds the first term, while
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md)
bounds the second. Thus every actual strict-supercritical row with incoming
demand $a$ and radial demand $c$ has outgoing reach at most $M_c^+(a)$.

If $c_0\ge1/2$, `2010` says that the strict-supercritical feasible set is
empty. The remaining discussion therefore has $c_0<1/2$.

## 2. CE1 reduction

Use the exact CE1 variables from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md):

$$
T_C\cap e_{0,1}=[s,t],
\qquad
u=1-t.
$$

If this interval contains a V-gap, then

$$
b_0\ge s,
\qquad
a_1\ge u.
$$

### 2.1. Exact survivor split

Suppose first that

$$
a_0\le1-s.
$$

Coverage of $e_{5,0}$ gives

$$
b_5\ge1-a_0\ge s.
$$

The exact CE1 theorem in
[`../../40XX_Nplus0/401X_all_Vd0_boundary_loss/401b_CE1_exact_branch_completion.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/401b_CE1_exact_branch_completion.md)
then applies to the nonsupercritical rows $T_5$ and $T_1$. Its analytic map
inequality uses only these two row classes and the exact CE1 center domain
once the inputs $b_5\ge s$ and $a_1\ge u$ are supplied. It gives

$$
F_5(s)+F_1(u)<1.
$$

As in the proved boundary-loss reduction, this leaves boundary length greater
than three for $T_2,T_3,T_4$, a contradiction. Therefore every surviving
CE1 one-gap candidate satisfies

$$
\boxed{a_0>1-s.}
$$

Since the same row realizes the demands $a_0,s,c_0$, the survivor domain also
satisfies

$$
\boxed{B_{c_0}(s)>1-s.}
$$

### 2.2. Five-map target

Propagate from $T_1$ around the five nonsupercritical rows and put

$$
Z_{\mathrm{CE1}}
=
(G_5\circ G_4\circ G_3\circ G_2\circ G_1)(u).
$$

The actual reach $a_0$ is at least $Z_{\mathrm{CE1}}$. The same $T_0$ must
also have $b_0\ge s$ and radial reach at least $c_0$. Reflection of the exact
admissible set gives

$$
Z_{\mathrm{CE1}}\le B_{c_0}(s).
$$

The free strict-supercritical envelope also gives
$Z_{\mathrm{CE1}}<S_+(c_0)$, but the unclassified bound is the sharper target
needed below.

The resulting CE1 lemma target is therefore

$$
\boxed{
\text{Target 4103-CE1:}
\qquad
Z_{\mathrm{CE1}}>B_{c_0}(s)
}
$$

throughout the strict exact CE1 domain in `2105` restricted by
$B_{c_0}(s)>1-s$.

## 3. CE2 reduction

Use the exact CE2 intervals from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md):

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v].
$$

Assume first that the unique V-gap is in $[y,v]$.

### 3.1. Exact survivor split

The active gap gives

$$
b_0\ge y,
\qquad
a_1\ge1-v.
$$

If $a_0\le u$, coverage of the portion of $e_{5,0}$ beyond the center
interval gives

$$
b_5\ge1-u.
$$

These are exactly the far-end inputs in the proved endpoint theorem used by
[`4102_CE2_two_gap_completion.md`](4102_CE2_two_gap_completion.md). The proof
of that inequality does not require an actual gap in the left interval once
the input $b_5\ge1-u$ is known. It again leaves more than three boundary units
for $T_2,T_3,T_4$, a contradiction. The analytic inequality in Sections
2--5 of `401d` uses only the exact CE2 center domain and nonsupercriticality of
$T_5,T_1$ once its inputs are supplied. Thus it also gives a contradiction
when $a_0\le1-y$, because then $b_5\ge1-a_0\ge y$. Hence every surviving
right-gap configuration satisfies

$$
\boxed{a_0>\max\left\{u,1-y\right\}.}
$$

Reflection shows that every surviving left-gap configuration satisfies

$$
\boxed{b_0>\max\left\{v,1-x\right\}.}
$$

### 3.2. Five-map targets

For the right-gap orientation, put

$$
Z_{\mathrm{CE2}}^R
=
(G_5\circ G_4\circ G_3\circ G_2\circ G_1)(1-v).
$$

The common $T_0$ realization gives

$$
Z_{\mathrm{CE2}}^R\le B_{c_0}(y).
$$

The survivor split also forces

$$
B_{c_0}(y)>\max\left\{u,1-y\right\}.
$$

Thus the resulting right-gap target is

$$
\boxed{
\text{Target 4103-CE2-R:}
\qquad
Z_{\mathrm{CE2}}^R>B_{c_0}(y)
}
$$

on the exact right-gap domain restricted by
$B_{c_0}(y)>\max\left\{u,1-y\right\}$.

For the reflected left-gap orientation, put

$$
Z_{\mathrm{CE2}}^L
=
(G_1\circ G_2\circ G_3\circ G_4\circ G_5)(1-u).
$$

The common realization gives

$$
Z_{\mathrm{CE2}}^L\le B_{c_0}(x),
$$

and the reflected survivor domain has

$$
B_{c_0}(x)>\max\left\{v,1-x\right\}.
$$

The resulting reflected target is

$$
\boxed{
\text{Target 4103-CE2-L:}
\qquad
Z_{\mathrm{CE2}}^L>B_{c_0}(x)
}
$$

The two targets are exchanged by reflection, so one exact proof with all
inequality directions audited suffices.

## 4. Why the free supercritical bound does not finish the split

In CE1, $c_0=\lambda s$. If $s\ge1/2$, then

$$
S_+(c_0)>\frac12\ge1-s.
$$

If $s<1/2$, put

$$
\kappa(b)=\frac{1-b^2}{2-b}.
$$

Then

$$
\lambda s<s<\kappa(1-s)
=\frac{s(2-s)}{1+s},
$$

so again $S_+(c_0)>1-s$. Thus `2010` permits the CE1 survivor threshold.

In the CE2 right-gap orientation, the two center points at parameters $u$
and $y$ satisfy

$$
u^2+uy+y^2\le1.
$$

Also

$$
c_0=\frac{xy}{x+y}<\frac{uy}{u+y}.
$$

The complementary corner triangle with boundary reaches $u,y$ therefore
shows

$$
B_{c_0}(y)\ge u.
$$

If $u<1/2$, then $S_+(c_0)>1/2>u$. Suppose $u\ge1/2$ and put

$$
\kappa(u)=\frac{1-u^2}{2-u}.
$$

The diameter inequality above gives

$$
u(1-u^2)+y(1-2u)
\ge
y\left((1-u)^2+uy\right)>0.
$$

After multiplication by the positive denominators, this is exactly

$$
\frac{uy}{u+y}<\kappa(u).
$$

Thus $c_0<\kappa(u)$, and the inverse relation in `2010` gives
$S_+(c_0)>u$. The free factor alone therefore does not exclude the
$u$-threshold. The exact survivor restriction
$B_{c_0}(y)>\max\left\{u,1-y\right\}$ remains part of Target
`4103-CE2-R`.

## 5. Exact failure of the two-adjacent-row shortcut

A simpler sufficient contradiction would be

$$
F_5\left(1-M_{c_0}^+(s)\right)+F_1(1-t)<1
$$

in CE1, with $(s,t)$ replaced by $(y,v)$ in the CE2 right-gap orientation.
Neither inequality holds globally.

### 5.1. CE1 witness

Take

$$
\lambda=\frac45,
\qquad
s=\frac3{14},
\qquad
t=\frac14,
\qquad
\rho=\frac{\sqrt{21}}5.
$$

Direct substitution satisfies every strict exact-domain condition in `2105`.
The relevant demands are

$$
c_0=\frac6{35},
\qquad
c_1=\frac{15}{16},
\qquad
c_5=\frac{151}{28}-\sqrt{21}.
$$

The selected exact pieces in `2007` give

$$
B_{c_0}(s)
=
\frac{\sqrt{757}-3}{28}
=:\beta(s),
$$

with $\beta(s)<S_+(c_0)$,

$$
F_5(1-\beta(s))=\beta(s),
$$

and

$$
F_1\left(\frac34\right)
=
\frac{15(8-\sqrt{33})}{256}.
$$

Since

$$
\beta(s)>\frac78,
\qquad
\frac{15(8-\sqrt{33})}{256}>\frac18,
$$

the proposed two-row sum is greater than one.

### 5.2. CE2 witness

Take

$$
x=\frac78,
\qquad
y=\frac18,
\qquad
u=\frac{177}{200},
$$

and

$$
v=\frac{200\sqrt{57}-1241}{1600}.
$$

Direct substitution satisfies every strict exact-domain condition in `2106`.
The relevant demands are

$$
c_0=\frac7{64},
\qquad
c_5=\frac{23}{25},
\qquad
c_1=\frac{2841-200\sqrt{57}}{1400}.
$$

The exact map gives

$$
B_{c_0}(y)
=
\frac{\sqrt{253}-1}{16}
=:b,
$$

with

$$
b>\frac{93}{100},
\qquad
b<S_+(c_0).
$$

The left safe map is Full, so

$$
F_5(1-b)=b.
$$

Put $q=1-v$. The exact relations give

$$
c_1=\frac{8q}{7},
\qquad
\frac9{10}<c_1<\frac{951}{1000},
\qquad
c_1>q+\frac7{100}.
$$

For

$$
H_c(z)=z^2-zc+c^2-c^4,
$$

the derivative with respect to $c$ is negative for $c\ge9/10$ at
$z=7/100$. Therefore

$$
H_{c_1}\left(\frac7{100}\right)
>
H_{951/1000}\left(\frac7{100}\right)
=
\frac{24789831199}{10^{12}}>0.
$$

The displayed inequalities place $7/100$ in the selected low-$CB$ contact
range, and the diameter and nonsupercritical caps are also strict. Thus the
exact formula in `2007` gives

$$
F_1(1-v)\ge\frac7{100}.
$$

Therefore the proposed two-row sum is greater than

$$
\frac{93}{100}+\frac7{100}=1.
$$

These two witnesses are counterexamples to the shortcut inequality, not
covers of $H$. They prove that this two-row shortcut cannot discard the
intermediate maps $G_2,G_3,G_4$.

## 6. Discharged terminal targets

This file proves the reduction to exactly the three boxed targets
`4103-CE1`, `4103-CE2-R`, and `4103-CE2-L`. The exact selected-branch catalog
needed by all three targets is proved in
[`4105_selected_capped_map_catalog.md`](4105_selected_capped_map_catalog.md).
Target `4103-CE1` is proved in `4106`; Targets `4103-CE2-R` and
`4103-CE2-L` are proved in `4107`. Thus this reduction has no remaining
terminal obligation.
