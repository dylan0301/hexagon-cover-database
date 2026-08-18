# Common CE1/CE2 One-Gap Five-V triangle Interface

Status: Proven

This note isolates the geometric and logical part shared by the CE1 and CE2
one-gap proofs. After this reduction, the two center classes differ only in
the scalar relaxation of one three-map chain.

The canonical notation is from
[`201d`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).
All five nonsupercritical radial demands below are strictly above $1/2$.
The exact outgoing cap is therefore the raw high-radial envelope $M_c$, and
the following-edge incoming transfer is the canonical propagation map
$\Phi_c=1-\overline M_c$. No second transfer family is used.

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
h_0=\frac{k}{2R},
$$

and

$$
m_3=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\}.
$$

The five nonsupercritical radial demands are

$$
\boxed{
\begin{aligned}
c_1&=1-\frac{\delta}{R},\\
c_2&=1-\delta,\\
c_3&=1-m_3,\\
c_4&=1-\alpha,\\
c_5&=1-\frac{\alpha}{W}.
\end{aligned}
}
$$

The V triangle-$0$ radial demand is

$$
c_0=k.
$$

The exact branchwise-output theorem
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md)
proves that every high-radial $\Phi_c$ is nondecreasing and extensive and that

$$
\boxed{
\Phi_c(a)\le z
\quad\Longleftrightarrow\quad
\Phi_c(1-z)\le1-a.
}
$$

This is the technical $\Phi_c$ duality rewritten in the canonical family.

## 2. Geometric hypotheses

Assume the `410X` branch:

- the closed C triangle $T_C$ is CE1 or CE2 and has exact midpoint set
  $\{M_0\}$;
- all six closed V triangles $T_i$ are Vd0;
- $N_+=1$;
- the trace $I_R$ contains a boundary gap, possibly a singleton;
- in the CE2 case, the companion trace contains no boundary gap.

As proved in
[`4101`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md), V triangles $T_1,\ldots,T_5$
contain their own midpoints and are nonsupercritical. Thus $T_0$ is the
unique supercritical V triangle.

Let $A_i,B_i$ be the actual incoming and outgoing boundary reaches and let
$C_i$ be the actual own-radial reach. Gap containment gives

$$
B_0\ge\frac{k}{R},
\qquad
A_1\ge X.
$$

Radial coverage and `2109` give

$$
C_i\ge c_i
\qquad(i=0,\ldots,5).
$$

## 3. Actual-V triangle propagation

Define

$$
z_0=X,
\qquad
z_i=\Phi_{c_i}(z_{i-1})
\quad(1\le i\le5).
$$

We prove inductively that the actual incoming reach at each V triangle dominates the
corresponding formal input. The initial inequality is $A_1\ge z_0$. Suppose

$$
A_i\ge z_{i-1}
$$

for some $1\le i\le5$. Since V triangle $T_i$ is nonsupercritical and $C_i\ge c_i$,
the raw high-radial outgoing bound gives

$$
B_i
\le
M_{c_i}(z_{i-1}).
$$

For $i=1,\ldots,4$, the next edge has no center trace, so boundary coverage
gives

$$
\begin{aligned}
A_{i+1}
&\ge1-B_i\\
&\ge
1-M_{c_i}(z_{i-1})\\
&=
\Phi_{c_i}(z_{i-1})\\
&=
z_i.
\end{aligned}
$$

For $i=5$, the CE1 C triangle has no positive companion trace, while in CE2
the companion trace contains no boundary gap. The final handoff therefore gives

$$
A_0
\ge
1-B_5
\ge
\Phi_{c_5}(z_4)
=
z_5.
$$

Consequently

$$
\boxed{A_0\ge Z,}
$$

where

$$
\boxed{
Z=
[\Phi_{c_1}
\mid
\Phi_{c_2}
\mid
\Phi_{c_3}
\mid
\Phi_{c_4}
\mid
\Phi_{c_5}](X).
}
$$

The same V triangle $T_0$ has outgoing reach at least $k/R$ and actual radial reach
at least $k$. Reflection of the admissible set and coordinatewise
down-closedness give

$$
\left(\frac{k}{R},A_0,k\right)\in\mathcal A.
$$

In the canonical defect notation,

$$
\boxed{
A_0
\le
M_k\left(\frac{k}{R}\right).
}
$$

The diameter-transfer lemma
[`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md)
gives

$$
M_k\left(\frac{k}{R}\right)
\le
M_0\left(\frac{k}{R}\right)
<
1-\frac{k}{2R}
=
1-h_0.
$$

Thus the one-gap branch is impossible once

$$
\boxed{Z>1-h_0}
$$

is proved.

## 4. Common three-map reduction

The first and fifth maps are extensive, and the middle maps are
nondecreasing. Hence

$$
Z
\ge
[\Phi_{c_2}
\mid
\Phi_{c_3}
\mid
\Phi_{c_4}](X).
$$

It is therefore enough to prove

$$
[\Phi_{c_2}
\mid
\Phi_{c_3}
\mid
\Phi_{c_4}](X)
>
1-h_0.
$$

Three applications of high-radial duality show that the negation of this
inequality is equivalent to

$$
[\Phi_{c_4}
\mid
\Phi_{c_3}
\mid
\Phi_{c_2}](h_0)
\le
1-X.
$$

Thus the scalar target common to CE1 and CE2 is

$$
\boxed{
[\Phi_{1-\alpha}
\mid
\Phi_{1-m_3}
\mid
\Phi_{1-\delta}](h_0)
>
W+\delta.
}
$$

The CE1 proof uses the two affine superscript relaxations and one threshold
superscript in
[`4106`](4106_CE1_one_gap_five_map_completion.md). The CE2 proof uses the
one-hit/two-threshold argument in
[`4107`](4107_CE2_one_gap_five_map_completion.md). No geometric or actual-V triangle
step is duplicated.

## 5. Reflected orientation

Reflection across the axis through $V_0$ exchanges

$$
R\longleftrightarrow W,
\qquad
\alpha\longleftrightarrow\delta,
$$

and reverses V triangles $1,2,3,4,5$. Therefore the left-gap chain is obtained by the
exact reversed V-triangle order, starting from the reflected far-end input. The
preceding proof applies after this explicit substitution.
