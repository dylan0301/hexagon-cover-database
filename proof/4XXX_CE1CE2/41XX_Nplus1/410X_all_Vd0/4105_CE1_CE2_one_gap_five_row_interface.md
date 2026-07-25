# Common CE1/CE2 One-Gap Five-Row Interface

Status: Proven

This note isolates the geometric and logical part shared by the CE1 and CE2
one-gap proofs. After this reduction, the two center classes differ only in
the scalar proof of one three-map inequality.

## 1. Signed center data

Use the common center normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad
W=1-R,
$$

$$
E=\sqrt{1-RW},
\qquad
\eta=1-E,
\qquad
P=E(1-E),
$$

$$
k=\eta+\alpha+\delta.
$$

The normalized right center trace is

$$
I_R=
\left[\frac{k}{R},W+\delta\right].
$$

Put

$$
X=1-(W+\delta)=R-\delta,
$$

$$
H=\frac{k}{2R},
$$

and

$$
m=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\}.
$$

The five nonsupercritical radial demands are

$$
\boxed{
\begin{aligned}
c_1&=1-\frac{\delta}{R},\\
c_2&=1-\delta,\\
c_3&=1-m,\\
c_4&=1-\alpha,\\
c_5&=1-\frac{\alpha}{W}.
\end{aligned}
}
$$

The row-$0$ radial demand is

$$
c_0=k.
$$

For $1/2<c<1$, write

$$
F_c(a)=\min\{B_c(a),1-a\},
\qquad
G_c(a)=1-F_c(a).
$$

The exact capped-map theorem
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md)
proves that every $G_c$ is nondecreasing and extensive and that

$$
\boxed{
G_c(a)\le z
\quad\Longleftrightarrow\quad
G_c(1-z)\le1-a.
}
$$

## 2. Geometric hypotheses

Assume the `410X` branch:

- the center role is CE1 or CE2 and has exact midpoint set $\{M_0\}$;
- all six vertex roles are Vd0;
- $N_+=1$;
- the trace $I_R$ contains a V-gap, possibly a singleton;
- in the CE2 case, the companion trace contains no V-gap.

As proved in
[`4101`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md), rows $T_1,\ldots,T_5$
contain their own midpoints and are nonsupercritical. Thus $T_0$ is the
unique supercritical row.

Let $a_i,b_i$ be the actual incoming and outgoing boundary reaches and let
$\widehat c_i$ be the actual own-radial reach. The gap containment gives

$$
b_0\ge\frac{k}{R},
\qquad
a_1\ge X.
$$

Radial coverage and `2109` give

$$
\widehat c_i\ge c_i
\qquad(i=0,\ldots,5).
$$

## 3. Actual-row propagation

Define

$$
z_0=X,
\qquad
z_i=G_{c_i}(z_{i-1})
\quad(1\le i\le5).
$$

We prove inductively that the actual incoming reach at each row dominates the
corresponding formal input. The initial inequality is $a_1\ge z_0$. Suppose
$a_i\ge z_{i-1}$ for some $1\le i\le5$. Since row $T_i$ is
nonsupercritical and $\widehat c_i\ge c_i$, the proof-safe capped-map bound
gives

$$
b_i\le F_{c_i}(z_{i-1}).
$$

For $i=1,\ldots,4$, the next edge has no center trace, so boundary coverage
gives

$$
a_{i+1}\ge1-b_i
\ge1-F_{c_i}(z_{i-1})
=G_{c_i}(z_{i-1})
=z_i.
$$

For $i=5$, the CE1 center has no positive companion trace, while in CE2 the
companion trace contains no V-gap. The final handoff therefore gives

$$
a_0\ge1-b_5
\ge G_{c_5}(z_4)
=z_5.
$$

Consequently

$$
\boxed{
a_0\ge Z,
}
$$

where

$$
\boxed{
Z=
\left(
G_{c_5}\circ G_{c_4}\circ G_{c_3}\circ G_{c_2}\circ G_{c_1}
\right)(X).
}
$$

The same row $T_0$ has outgoing reach $b_0\ge k/R$ and actual radial reach at
least $k$. Reflection of the local admissible set and coordinatewise
down-closedness give

$$
\left(\frac{k}{R},a_0,k\right)\in\mathcal A.
$$

Therefore

$$
\boxed{
a_0\le B_k\left(\frac{k}{R}\right).}
$$

The diameter-transfer lemma
[`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md)
gives

$$
B_k\left(\frac{k}{R}\right)
\le
\beta\left(\frac{k}{R}\right)
<
1-\frac{k}{2R}
=1-H.
$$

Thus the one-gap branch is impossible once

$$
\boxed{Z>1-H}
$$

is proved.

## 4. Common three-map reduction

The first and fifth maps are extensive, and the middle maps are
nondecreasing. Hence

$$
Z
\ge
\left(G_{c_4}\circ G_{c_3}\circ G_{c_2}\right)(X).
$$

It is therefore enough to prove

$$
\left(G_{c_4}\circ G_{c_3}\circ G_{c_2}\right)(X)>1-H.
$$

Three applications of capped-map duality show that the negation of this
inequality is equivalent to

$$
\left(G_{c_2}\circ G_{c_3}\circ G_{c_4}\right)(H)
\le1-X.
$$

Thus the scalar target common to CE1 and CE2 is

$$
\boxed{
\left(
G_{1-\delta}
\circ
G_{1-m}
\circ
G_{1-\alpha}
\right)(H)
>
W+\delta.
}
$$

The CE1 proof of this target uses the selected-$T_+$ chord argument in
[`4106`](4106_CE1_one_gap_five_map_completion.md). The CE2 proof uses the
two-threshold argument in
[`4107`](4107_CE2_one_gap_five_map_completion.md). No geometric or
actual-row step is duplicated between those two scalar proofs.

## 5. Reflected orientation

Reflection across the axis through $V_0$ exchanges

$$
R\longleftrightarrow W,
\qquad
\alpha\longleftrightarrow\delta,
$$

and reverses rows $1,2,3,4,5$. Therefore the left-gap chain is obtained by
the exact map order

$$
G_{c_1}\circ G_{c_2}\circ G_{c_3}\circ G_{c_4}\circ G_{c_5},
$$

starting from the reflected far-end input. The preceding proof applies after
this explicit substitution.
