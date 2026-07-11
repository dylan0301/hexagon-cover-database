# CE1 / CE2 Exactly-One-Midpoint Lemma

Status: Proven

## Correct statement

Let $T_C$ be a closed unit equilateral triangle with

$$
O\in\mathrm{int}(T_C).
$$

If $T_C$ has a positive-length intersection with a boundary edge of the unit
regular hexagon, then

$$
\boxed{
\left\lvert
\left\{
i:M_i\in T_C
\right\}
\right\rvert=1.
}
$$

In particular, the conclusion holds for every nondegenerate CE1 or CE2 center
role obtained by closing an open center triangle that contains $O$.

The interior hypothesis is necessary. The closed unit triangle

$$
\mathrm{conv}\left\{O,V_0,V_1\right\}
$$

has a positive-length overlap with $e_{0,1}$ and contains both $M_0$ and
$M_1$, while $O$ lies on its boundary.

## Edge normal form

Normalize a positive-length overlap to

$$
T_C\cap e_{0,1}=[s,t],
\qquad
0\le s<t\le1.
$$

Use the affine coordinates

$$
X=V_0+b(V_1-V_0)+a(V_5-V_0).
$$

After reflecting the hexagon across the perpendicular bisector of
$e_{0,1}$ if needed, the two side slopes have ratio

$$
0<\lambda<1.
$$

Set

$$
\rho=\sqrt{1-\lambda+\lambda^2}.
$$

The three side slacks can be written

$$
F_1=\lambda b+(1-\lambda)a-\lambda s,
$$

$$
F_2=-b+\lambda a+t,
$$

and

$$
F_0=(1-\lambda)b-a+\rho+\lambda s-t.
$$

They satisfy

$$
F_0+F_1+F_2=\rho,
$$

and

$$
T_C=\left\{F_0\ge0,F_1\ge0,F_2\ge0\right\}.
$$

This is the standard unit-equilateral edge-cut normal form: the first two
sides cut $e_{0,1}$ at $s,t$, their positive slope ratio is $\lambda$, and the
third side is forced by the unit side-length relation. The case $\lambda=1$
would give $F_0(O)=s-t<0$, so the displayed inequality is strict.

Define the center slacks

$$
C_j=F_j(O).
$$

Explicitly,

$$
C_0=\rho+\lambda s-t-\lambda,
$$

$$
C_1=1-\lambda s,
$$

and

$$
C_2=t+\lambda-1.
$$

Because $O$ is interior,

$$
C_0>0,
\qquad
C_1>0,
\qquad
C_2>0,
\qquad
C_0+C_1+C_2=\rho.
$$

The positive-length condition is

$$
C_1+\lambda C_2
=
\rho^2+\lambda(t-s)
>\rho^2.
$$

Equivalently,

$$
C_0+(1-\lambda)C_2<P,
\qquad
P=\rho(1-\rho).
$$

Since

$$
1-\rho^2=\lambda(1-\lambda),
$$

we have

$$
P=\frac{\lambda(1-\lambda)\rho}{1+\rho}.
$$

In particular,

$$
P<\frac{\lambda(1-\lambda)}2,
\qquad
P<\frac{1-\lambda}{2}.
$$

## Midpoint criteria

Substitution of the six radial midpoints gives the following exact tests:

| midpoint | necessary and sufficient additional inequalities |
|---|---|
| $M_0$ | $C_1\ge1/2$ |
| $M_1$ | $C_1\ge(1-\lambda)/2$ and $C_2\ge\lambda/2$ |
| $M_2$ | $C_2\ge1/2$ |
| $M_3$ | $C_0\ge\lambda/2$ and $C_2\ge(1-\lambda)/2$ |
| $M_4$ | $C_0\ge1/2$ |
| $M_5$ | $C_0\ge(1-\lambda)/2$ and $C_1\ge\lambda/2$ |

All omitted side slacks are automatically positive because the corresponding
slack at $O$ is positive.

## Exactly one midpoint

First,

$$
C_0+C_2
<
\frac{P}{1-\lambda}.
$$

Therefore

$$
C_1
>
\rho-\frac{P}{1-\lambda}
=
\frac{\rho(\rho-\lambda)}{1-\lambda}
>\frac12.
$$

For the last inequality, use

$$
2\rho(\rho-\lambda)-(1-\lambda)
=
\frac{(1-\lambda)(\rho-\lambda)}{\rho+\lambda}>0.
$$

Thus $M_0\in T_C$.

Next,

$$
C_2<\frac{P}{1-\lambda}<\frac\lambda2,
$$

so neither $M_1$ nor $M_2$ lies in $T_C$.

Also

$$
C_0<P<\frac\lambda2,
$$

so $M_3\notin T_C$. Certainly $C_0<1/2$, so $M_4\notin T_C$. Finally,

$$
C_0<P<\frac{1-\lambda}{2},
$$

so $M_5\notin T_C$.

Hence, in the reflected normalization, $M_0$ is the unique radial midpoint
in $T_C$. Undoing the reflection and the cyclic normalization proves the
theorem.
