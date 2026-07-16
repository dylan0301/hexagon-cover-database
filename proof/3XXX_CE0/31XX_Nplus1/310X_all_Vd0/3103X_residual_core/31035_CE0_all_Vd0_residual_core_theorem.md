# CE0, $N_+=1$, All-Vd0 Residual-Core Theorem

Status: Proven

This note gives the statement and a concise complete proof of the `3103X`
route. The exact witness constructions and the terminal enclosure estimate
remain in the linked technical notes.

## Theorem

Let $H$ be the regular hexagon of side length $1$ from
[`1000_problem_statement.md`](../../../../1XXX_foundations/10XX_global_conventions/1000_problem_statement.md).
There is no cover of $H$ by seven open unit equilateral triangles

$$
T_C,T_0,\dots,T_5
$$

for which

$$
T_C\text{ is CE0},
\qquad
N_+=1,
$$

and all six vertex roles $T_0,\dots,T_5$ are Vd0. Equivalently, the CE0,
$N_+=1$, all-Vd0 branch cannot occur.

## Proof

Assume that such a cover exists.

Because $T_C$ is CE0, the six vertex roles cover $\partial H$. Indeed, if a
boundary point were covered only by the open triangle $T_C$, then an interval
of an incident side of $H$ would lie in $T_C$, contrary to the CE0 condition.
The strict handoff theorem
[`4104_all_boundary_transfer_to_310X.md`](../../../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4104_all_boundary_transfer_to_310X.md)
therefore applies.

After a cyclic relabeling, the unique supercritical row is the $V_4$ row. The
handoff theorem supplies numbers $x_i\in(0,1)$ such that

$$
x_3<x_2<x_1<x_0<x_5<x_4.
$$

Put

$$
a=1-x_3,
\qquad
b=x_4.
$$

Then

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
\tag{1}
$$

For each row, let $R_i(u,v)$ be the exact closed row union with incoming demand
$u$ and outgoing demand $v$. If

$$
a_i=1-x_{i-1},
\qquad
b_i=x_i,
$$

then the handoff theorem gives

$$
\mathcal U_6^\circ
=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5\mathrm{int}\left(R_i(a_i,b_i)\right)
\subseteq T_C.
\tag{2}
$$

For every $i\ne4$, the displayed ordering of the $x_i$ gives

$$
a_i\ge1-b,
\qquad
b_i\ge1-a.
$$

By definition, the row unions are antitone in both demands:

$$
u'\ge u,
\quad
v'\ge v
\quad\Longrightarrow\quad
R_i(u',v')\subseteq R_i(u,v).
\tag{3}
$$

Define

$$
\mathcal C_{\mathrm{asym}}(a,b)
=
\mathrm{int}(H)
\setminus
\left(
\mathrm{int}\left(R_4(a,b)\right)
\cup
\bigcup_{i\ne4}\mathrm{int}\left(R_i(1-b,1-a)\right)
\right)
$$

and

$$
\mathcal C_{\mathrm{sym}}(a,b)
=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5\mathrm{int}\left(R_i(1-b,1-a)\right).
$$

The comparison above and (3) give

$$
\mathcal C_{\mathrm{asym}}(a,b)
\subseteq
\mathcal U_6^\circ.
$$

Moreover, $a+b>1$ gives $a>1-b$ and $b>1-a$, so (3) also gives

$$
\mathcal C_{\mathrm{sym}}(a,b)
\subseteq
\mathcal C_{\mathrm{asym}}(a,b).
$$

Together with (2),

$$
\mathcal C_{\mathrm{sym}}(a,b)
\subseteq
\mathcal C_{\mathrm{asym}}(a,b)
\subseteq
\mathcal U_6^\circ
\subseteq
T_C.
\tag{4}
$$

Now put

$$
p=1-b,
\qquad
q=1-a,
\qquad
c_*=c_{\max}(p,q).
$$

The symmetric-witness theorem
[`31032_symmetric_witness_construction.md`](31032_symmetric_witness_construction.md)
proves that

$$
P_k=(1-c_*)V_k
\in
\mathcal C_{\mathrm{sym}}(a,b)
\qquad(k=0,\dots,5).
$$

By (4), all six points lie in the convex triangle $T_C$. Their convex hull is a
regular hexagon, so $T_C$ contains its centered incircle

$$
\mathcal D_\eta
=
\left\{x:\lVert x\rVert\le\eta\right\},
\qquad
\eta=\frac{\sqrt3}{2}(1-c_*).
\tag{5}
$$

The asymmetric-witness theorem
[`31033_asymmetric_witness_construction.md`](31033_asymmetric_witness_construction.md)
defines exact points $Q_-,Q_0,Q_+$ and proves

$$
Q_-,Q_0,Q_+
\in
\mathcal C_{\mathrm{asym}}(a,b)
\subseteq T_C.
$$

Consequently the compact set

$$
K_{\mathrm{wit}}
=
\mathcal D_\eta\cup\{Q_-,Q_0,Q_+\}
$$

satisfies

$$
K_{\mathrm{wit}}\subseteq T_C.
\tag{6}
$$

Let $\Lambda(K)$ denote the minimum side length of an equilateral triangle
containing a compact set $K$. The terminal enclosure theorem
[`31034_witness_enclosure_inequality.md`](31034_witness_enclosure_inequality.md)
proves, for every $(a,b)$ satisfying (1), that

$$
\Lambda\left(K_{\mathrm{wit}}\right)\ge1.
\tag{7}
$$

On the other hand, (6) places the compact set $K_{\mathrm{wit}}$ inside the open
unit equilateral triangle $T_C$. Its three side margins are therefore positive.
Moving all three sides of $T_C$ inward by a common sufficiently small amount
produces an equilateral triangle of side length strictly less than $1$ that
still contains $K_{\mathrm{wit}}$. Thus

$$
\Lambda\left(K_{\mathrm{wit}}\right)<1,
$$

contradicting (7). Hence the assumed cover does not exist. $\square$
