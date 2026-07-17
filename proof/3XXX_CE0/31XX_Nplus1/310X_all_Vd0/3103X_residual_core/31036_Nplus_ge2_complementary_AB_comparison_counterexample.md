# $N_+\ge2$ Complementary $AB$ Comparison Counterexample

Status: Proven

## 1. Purpose and conclusion

This note isolates the uniform $AB$-set comparison used in
[`31035_center_independent_all_boundary_obstruction.md`](31035_center_independent_all_boundary_obstruction.md).
It answers the following question.

Choose row $4$, put

$$
s=a_4,
\qquad
t=b_4,
$$

and replace the other five row unions by the common comparison union with
demands

$$
(1-t,1-s).
$$

Since $AB$-unions are antitone in both demands, can the same construction be
used when $N_+\ge2$?

The answer is:

- this is exactly the comparison used in `31035`;
- antitonicity proves the five required inclusions precisely when the selected
  handoff at row $4$ goes from the global minimum cut to the global maximum
  cut;
- exact-one guarantees that extreme-jump condition;
- general $N_+\ge2$ does not guarantee it, even after the strict handoffs are
  reselected;
- in an explicit feasible multi-ascent example, the proposed $AB$-set
  inclusion itself is false, not merely unproved by monotonicity.

This is a limitation of the complementary two-parameter reduction. It is not
a counterexample to the seven-triangle theorem and does not rule out a new
four-parameter or multi-row residual-core proof.

All indices below are modulo $6$.

## 2. Selected rows and the proposed uniformization

Let

$$
0<x_i<1
$$

be strict boundary handoffs, and define the selected demands

$$
(a_i,b_i)=(1-x_{i-1},x_i).
\tag{1}
$$

Thus row $i$ is selected supercritical exactly when

$$
a_i+b_i>1
\quad\Longleftrightarrow\quad
x_{i-1}<x_i.
\tag{2}
$$

Let $R_i(u,v)$ be the corner-cone-clipped closed $AB$-union at $V_i$:
the union of all closed unit equilateral triangles containing $V_i$ and the
two boundary anchors at demands $u,v$, intersected with the local corner
cone. Its exact definition and certificate are in
[`20090_ab_set_index.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20090_ab_set_index.md)
and
[`20095_exact_caliper_certificate.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20095_exact_caliper_certificate.md).

The union is antitone in both demands:

$$
u'\ge u,
\qquad
v'\ge v
\quad\Longrightarrow\quad
R_i(u',v')\subseteq R_i(u,v).
\tag{3}
$$

Assume row $4$ is selected supercritical and put

$$
s=a_4=1-x_3,
\qquad
t=b_4=x_4.
\tag{4}
$$

Then $x_3<x_4$. The complementary comparison pair is

$$
p_0=1-t=1-x_4,
\qquad
q_0=1-s=x_3.
\tag{5}
$$

The residual defined by the six selected rows is

$$
\begin{aligned}
\mathcal U_6^\circ
&=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5\mathrm{int}R_i(a_i,b_i).
\end{aligned}
\tag{6}
$$

The proposed one-distinguished-row model is

$$
\begin{aligned}
\mathcal C_{\mathrm{asym}}(s,t)
&=
\mathrm{int}(H)
\setminus
\left(
\mathrm{int}R_4(s,t)
\cup
\bigcup_{i\ne4}\mathrm{int}R_i(p_0,q_0)
\right).
\end{aligned}
\tag{7}
$$

To prove

$$
\mathcal C_{\mathrm{asym}}(s,t)
\subseteq
\mathcal U_6^\circ
\tag{8}
$$

by rowwise antitonicity, one needs

$$
R_i(a_i,b_i)
\subseteq
R_i(p_0,q_0)
\qquad(i\ne4).
\tag{9}
$$

This is exactly the strategy described in the question.

## 3. Exact criterion for the five monotone comparisons

**Lemma 3.1.** The coordinatewise inequalities used with (3),

$$
a_i\ge p_0,
\qquad
b_i\ge q_0
\qquad(i\ne4),
\tag{10}
$$

hold if and only if

$$
\boxed{
x_3=\min_jx_j,
\qquad
x_4=\max_jx_j.
}
\tag{11}
$$

*Proof.* Equations (1) and (5) give

$$
\begin{aligned}
a_i\ge p_0
&\quad\Longleftrightarrow\quad
1-x_{i-1}\ge1-x_4
\quad\Longleftrightarrow\quad
x_{i-1}\le x_4,\\
b_i\ge q_0
&\quad\Longleftrightarrow\quad
x_i\ge x_3.
\end{aligned}
\tag{12}
$$

As $i\ne4$ varies, the indices $i-1$ cover every index except $3$. Since
$x_3<x_4$, the first family in (12) holds exactly when $x_4$ is a global
maximum.

Likewise, the indices $i$ with $i\ne4$ cover every index except $4$. Since
$x_3<x_4$, the second family holds exactly when $x_3$ is a global minimum.
This proves (11). $\square$

Under (11), antitonicity gives all five inclusions (9), and hence (8). Also

$$
s>p_0,
\qquad
t>q_0,
$$

so

$$
R_4(s,t)\subseteq R_4(p_0,q_0).
$$

Therefore the symmetric core

$$
\begin{aligned}
\mathcal C_{\mathrm{sym}}(s,t)
&=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5\mathrm{int}R_i(p_0,q_0).
\end{aligned}
$$

satisfies

$$
\mathcal C_{\mathrm{sym}}(s,t)
\subseteq
\mathcal C_{\mathrm{asym}}(s,t)
\subseteq
\mathcal U_6^\circ.
\tag{13}
$$

This is the comparison chain used by `31032`--`31035`.

## 4. Why exact-one gives the extreme jump

Suppose row $4$ is the unique selected supercritical row. Every other row is
strictly nonsupercritical, so

$$
x_i<x_{i-1}
\qquad(i\ne4).
$$

Reading these five inequalities cyclically gives

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{14}
$$

Thus $x_3$ is the global minimum and $x_4$ is the global maximum. Lemma 3.1
applies.

The exact logical condition needed by the uniform comparison is therefore
not uniqueness by itself, but the extreme-jump condition (11). A selected
sequence may have other ascents and still satisfy (11), in which case the
same comparison remains valid.

For actual $N_+\ge2$, however, the strict-handoff theorem
[`1214_strict_boundary_handoff_selection.md`](../../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
guarantees only a selection with at least two selected ascents. It does not
assert that one ascent joins the global minimum directly to the global
maximum.

## 5. An exact feasible multi-ascent counterexample

Consider the strict cuts

$$
\begin{aligned}
(x_0,\ldots,x_5)
&=
\left(
\frac{37}{100},
\frac12,
\frac{31}{50},
\frac7{10},
\frac{39}{50},
\frac14
\right).
\end{aligned}
\tag{15}
$$

Rows $0,1,2,3,4$ are selected supercritical, while row $5$ is selected
nonsupercritical. The selected pairs and their feasibility values are

| $i$ | $(a_i,b_i)$ | $a_i^2+a_ib_i+b_i^2$ |
|---:|---:|---:|
| $0$ | $(3/4,37/100)$ | $9769/10000$ |
| $1$ | $(63/100,1/2)$ | $9619/10000$ |
| $2$ | $(1/2,31/50)$ | $2361/2500$ |
| $3$ | $(19/50,7/10)$ | $2251/2500$ |
| $4$ | $(3/10,39/50)$ | $2331/2500$ |
| $5$ | $(11/50,1/4)$ | $1659/10000$ |

Every row is strictly feasible.

Choose row $4$ as the distinguished row. Then

$$
s=\frac3{10},
\qquad
t=\frac{39}{50},
$$

and the proposed common background pair is

$$
\begin{aligned}
(p_0,q_0)
&=(1-t,1-s)\\
&=
\left(
\frac{11}{50},
\frac7{10}
\right).
\end{aligned}
\tag{16}
$$

But row $5$ has

$$
\begin{aligned}
(a_5,b_5)
&=
\left(
\frac{11}{50},
\frac14
\right).
\end{aligned}
$$

so

$$
b_5=\frac14<\frac7{10}=q_0.
\tag{17}
$$

Antitonicity therefore points in the opposite direction:

$$
R_5\left(\frac{11}{50},\frac7{10}\right)
\subseteq
R_5\left(\frac{11}{50},\frac14\right).
\tag{18}
$$

The desired reverse inclusion in (9) does not follow. The next section proves
that it is actually false.

## 6. Exact $AB$-set noninclusion

Take the radial demand

$$
c=\frac9{10}
$$

at row $5$, and let

$$
P=V_5+c(O-V_5)=\frac1{10}V_5.
\tag{19}
$$

For a subcritical demand pair $(u,v)$, put

$$
\sigma=u+v,
\qquad
m=\min\left\{u,v\right\},
\qquad
M=\max\left\{u,v\right\},
$$

$$
\chi=\sigma^4-\sigma^2+uv,
$$

and define the two exact radial-cell polynomials from
[`2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md):

$$
F_L(c)=c^4-c^2+mc-m^2,
$$

$$
F_T(c)=(\sigma^2-1)c^2+Mc-M^2.
$$

For the actual row-$5$ pair

$$
\begin{aligned}
(u,v)
&=
\left(
\frac{11}{50},
\frac14
\right).
\end{aligned}
$$

one has

$$
\chi=-\frac{11710319}{100000000}<0,
$$

and

$$
F_L\left(\frac9{10}\right)
=-\frac{43}{10000}<0.
\tag{20}
$$

The remaining $L$-cell inequalities are also strict:

$$
u^2+uv+v^2=\frac{1659}{10000}<1,
\qquad
u+v=\frac{47}{100}<1.
$$

Hence

$$
P\in
\mathrm{int}R_5\left(\frac{11}{50},\frac14\right).
\tag{21}
$$

For the proposed uniform pair

$$
\begin{aligned}
(p_0,q_0)
&=
\left(
\frac{11}{50},
\frac7{10}
\right).
\end{aligned}
$$

one instead has

$$
\chi=\frac{37489}{1562500}>0,
$$

The remaining $T$-cell conditions hold:

$$
\sigma=\frac{23}{25}<1,
\qquad
p_0^2+p_0q_0+q_0^2=\frac{1731}{2500}<1,
\qquad
c\le2\max\left\{p_0,q_0\right\}.
$$

but its defining polynomial satisfies

$$
F_T\left(\frac9{10}\right)
=\frac{487}{31250}>0.
\tag{22}
$$

Thus $c=9/10$ is not radially admissible for the uniform pair, and

$$
P\notin
R_5\left(\frac{11}{50},\frac7{10}\right).
\tag{23}
$$

Equations (21) and (23) prove the strict noninclusion

$$
\boxed{
R_5\left(\frac{11}{50},\frac14\right)
\not\subseteq
R_5\left(\frac{11}{50},\frac7{10}\right).
}
\tag{24}
$$

Therefore the proposed rowwise comparison is not merely unavailable from
monotonicity; it is false.

### Stronger total-union failure

The same point also shows that the other five rotated uniform unions do not
repair the failed rowwise inclusion.

The exact radial maximum for the uniform pair is

$$
\begin{aligned}
c_{\max}
\left(
\frac{11}{50},
\frac7{10}
\right)
&=
\frac{35}{25+\sqrt{241}}
<
\frac9{10}.
\end{aligned}
\tag{25}
$$

The last inequality is equivalent to $125<9\sqrt{241}$, whose square is the
strict inequality $15625<19521$.

The exact neighboring-ray capacities from
[`2008_neighbor_ray_max_c_formula.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md)
are

$$
C_+\left(\frac7{10},\frac{11}{50}\right)
=\frac{39}{50},
$$

and

$$
C_+\left(\frac{11}{50},\frac7{10}\right)
=\frac{36-\sqrt{241}}{50}.
\tag{26}
$$

Both are below $9/10$. For the second formula, the cubic transition root lies
strictly between $7/10$ and $3/4$. Indeed, for $a=11/50$, the cubic from
`2008` has values

$$
\begin{aligned}
f_a\left(\frac7{10}\right)
&=-\frac{23}{625}<0,\\
f_a\left(\frac34\right)
&=\frac1{320}>0.
\end{aligned}
$$

and is strictly increasing on the relevant interval. If its root is $\pi$,
then

$$
\left(\pi-\frac{11}{50}\right)(1-\pi)>\frac{12}{100}.
$$

Therefore the final-branch threshold

$$
1-\frac{11}{50}
-\left(\pi-\frac{11}{50}\right)(1-\pi)
$$

is below $66/100<7/10$. Substitution into the final branch gives (26).

Consequently $P$ lies outside the two uniform neighboring-row unions. It lies
outside the cyclic-distance-two and opposite uniform unions because their
assigned vertices are at distance greater than $1$ from $P$; explicitly, the
relevant squared distance is

$$
c^2-3c+3=1+(1-c)(2-c)>1,
$$

or the opposite distance is $2-c>1$.

Together with (25), these exclusions give

$$
P\notin
\bigcup_{i=0}^5
R_i\left(\frac{11}{50},\frac7{10}\right).
\tag{27}
$$

Combining (21) and (27),

$$
P
\in
R_5(a_5,b_5)
\setminus
\bigcup_{i=0}^5R_i(p_0,q_0).
\tag{28}
$$

Thus even total-union containment fails. Cross-row coverage cannot rescue the
proposed complementary uniformization.

## 7. The valid global-floor comparison

For an arbitrary selected sequence, define

$$
m_x=\min_i x_i,
\qquad
M_x=\max_i x_i,
$$

and the global floor pair

$$
p=1-M_x,
\qquad
q=m_x.
\tag{29}
$$

Every selected row satisfies

$$
a_i=1-x_{i-1}\ge p,
\qquad
b_i=x_i\ge q.
\tag{30}
$$

Thus the following four-parameter comparison is valid:

$$
\begin{aligned}
\mathcal C_4(s,t;p,q)
&=
\mathrm{int}(H)
\setminus
\left(
\mathrm{int}R_4(s,t)
\cup
\bigcup_{i\ne4}\mathrm{int}R_i(p,q)
\right)\\
&\subseteq
\mathcal U_6^\circ.
\end{aligned}
\tag{31}
$$

This proves the part of the proposed monotonicity argument that remains true
for general $N_+\ge2$.

The existing witness package, however, is proved only on the complementary
two-parameter slice

$$
(p_0,q_0)=(1-t,1-s).
$$

For a general selected ascent,

$$
p\le p_0,
\qquad
q\le q_0.
$$

Therefore

$$
R_i(p_0,q_0)\subseteq R_i(p,q),
$$

and taking complements gives the wrong direction for transferring the old
witnesses: the valid four-parameter core is smaller than the certified old
core.

This mismatch is rigid. Suppose one tries to place a certified complementary
core with distinguished pair $(A,B)$ inside (31) using coordinatewise
antitonicity. The distinguished row requires

$$
A\le s,
\qquad
B\le t,
\tag{32}
$$

while the five background rows require

$$
1-B\le p,
\qquad
1-A\le q.
\tag{33}
$$

Equations (33) give

$$
A\ge1-q,
\qquad
B\ge1-p.
$$

But the definitions give

$$
s\le1-q,
\qquad
t\le1-p.
$$

Combining these inequalities with (32) forces

$$
A=s=1-q,
\qquad
B=t=1-p.
\tag{34}
$$

Equation (34) is exactly

$$
x_3=m_x,
\qquad
x_4=M_x.
$$

Hence a direct monotone reduction to the existing complementary
two-parameter certificate is possible exactly in the extreme-jump case.

## 8. Reselection does not solve the general case

The preceding fixed-cut counterexample shows that an arbitrary multi-ascent
selection need not work. We now show that actual $N_+\ge2$ does not always
permit a different strict selection that restores an extreme jump.

Put

$$
\begin{aligned}
(y_0,\ldots,y_5)
&=
\frac1{1000}
(450,500,460,520,470,510),\\
\delta&=\frac1{1000}.
\end{aligned}
\tag{35}
$$

and prescribe actual maximal reaches

$$
A_i=1-y_{i-1}+\delta,
\qquad
B_i=y_i+\delta.
\tag{36}
$$

The six actual pairs are

$$
\begin{aligned}
(A_i,B_i)
&=
\frac1{1000}
\left(
(491,451),
(551,501),
(501,461),
(541,521),
(481,471),
(531,511)
\right).
\end{aligned}
\tag{37}
$$

Their strict handoff intervals are

$$
\begin{aligned}
I_i
&=(1-A_{i+1},B_i)\\
&=(y_i-\delta,y_i+\delta).
\end{aligned}
\tag{38}
$$

They have the fixed order

$$
I_0<I_2<I_4<I_1<I_5<I_3.
\tag{39}
$$

Therefore every possible strict selection $x_i\in I_i$ has its unique global
minimum at index $0$, its unique global maximum at index $3$, and selected
ascents exactly at rows $1,3,5$. No ascent joins the global minimum directly
to the global maximum.

It remains to verify that (37) consists of actual reaches of genuine unit
$Vd0$ roles rather than abstract demand pairs.

Use local physical unit edge directions

$$
\begin{aligned}
u
&=
\left(
\frac12,
\frac{\sqrt3}{2}
\right),\\
v
&=
\left(
\frac12,
-\frac{\sqrt3}{2}
\right).
\end{aligned}
$$

and outward unit normals

$$
\begin{aligned}
n_A
&=
\left(
-\frac12,
\frac{\sqrt3}{2}
\right),\\
n_B
&=
\left(
-\frac12,
-\frac{\sqrt3}{2}
\right),\\
n_C&=(1,0).
\end{aligned}
$$

For row $i$, define the open triangle

$$
\begin{aligned}
T_i
&=
\left\{
z:
n_A\mathbin{\cdot}z<\frac{A_i}{2},
\quad
n_B\mathbin{\cdot}z<\frac{B_i}{2},
\quad
n_C\mathbin{\cdot}z<
\frac{\sqrt3-A_i-B_i}{2}
\right\}.
\end{aligned}
\tag{40}
$$

The three support numbers in (40) sum to $\sqrt3/2$. For three outward unit
normals separated by $120$ degrees, the side length is $2/\sqrt3$ times the
support sum. Hence $T_i$ is an open unit equilateral triangle. All three
support numbers are positive because

$$
0<A_i+B_i\le\frac{1062}{1000}<\sqrt3.
$$

Thus the local vertex $0$ lies in $T_i$.

Along the incoming ray $ru$, the two positive cutoffs in (40) are

$$
A_i
\quad\text{and}\quad
\sqrt3-A_i-B_i.
$$

Along the outgoing ray $rv$, they are

$$
B_i
\quad\text{and}\quad
\sqrt3-A_i-B_i.
$$

For every pair in (37),

$$
\begin{aligned}
A_i&>B_i,\\
2A_i+B_i&\le\frac{1603}{1000}<\sqrt3.
\end{aligned}
\tag{41}
$$

Since $A_i>B_i$, equation (41) also gives

$$
A_i+2B_i<2A_i+B_i<\sqrt3.
$$

Thus both $A_i$ and $B_i$ occur before the third cutoff. They are exactly the
maximal incoming and outgoing reaches of $T_i$.

In corner-cone coordinates $z=xv+yu$, the third inequality in (40) becomes

$$
x+y<\sqrt3-A_i-B_i.
$$

Also every pair in (37) satisfies

$$
A_i+B_i\ge\frac{942}{1000}>\sqrt3-1.
\tag{42}
$$

Hence $x+y<1$. The triangle meets neither adjacent half-diagonal $x=1$ nor
$y=1$, so it is Vd0 by
[`1201_V_triangle_types.md`](../../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).

The actual row sums are

$$
\frac1{1000}
(942,1052,962,1062,952,1042).
$$

Thus the actual supercritical rows are $1,3,5$, and

$$
N_+=3.
$$

Finally, on edge $i$, the endpoint-role traces are

$$
[0,B_i)
\quad\text{and}\quad
(1-A_{i+1},1].
$$

They overlap strictly on $I_i$, so the six roles cover the entire boundary.
This is a genuine all-Vd0, full-boundary, actual-$N_+=3$ configuration for
which no strict handoff selection has the extreme-jump property.

It is not claimed that these six roles, together with a center triangle,
cover the whole hexagon.

## 9. Final scope

The comparison

$$
R_i(a_i,b_i)
\subseteq
R_i(1-t,1-s)
\qquad(i\ne4)
$$

used in `31035` is valid by antitonicity exactly when

$$
x_3=\min_jx_j,
\qquad
x_4=\max_jx_j.
$$

Exact-one guarantees this condition. General $N_+\ge2$ does not, even after
arbitrary strict-handoff reselection, and the explicit radial point (19)
shows that the proposed $AB$-set inclusion can actually fail.

The valid general monotonicity reduction is the four-parameter core (31).
The witnesses in `31032`--`31034` have not been proved for that core. A new
four-parameter or multi-asymmetric theorem may still exist.

The CE0, $N_+\ge2$ branch is independently closed by
[`3205_unconditional_local_square_loss.md`](../../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md)
and
[`3208_CE0_conditional_area_certificate.md`](../../../32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md).
