# Admissible Set

Status: Computational formula

Let $\mathcal A\subset[0,1]^3$ be the set of possible local triples
$(a,b,c)$.

It is symmetric:

$$
(a,b,c)\in\mathcal A\iff (b,a,c)\in\mathcal A.
$$

In this file, $c(a,b)$ means the maximum radial coordinate attainable by an
admissible local triple whose edge coordinates contain at least the points
prescribed by $a$ and $b$:

$$
c(a,b)=\max\{c': \exists (a',b',c')\in\mathcal A\text{ with }a'\ge a,\ b'\ge b\}.
$$

Thus $a$ and $b$ are lower-bound point-containment constraints, not
necessarily the exact edge coordinates of the maximizing triple.

Let

$$
s=a+b, \qquad m=\min(a,b), \qquad M=\max(a,b),
$$

and

$$
q=(a+b)^4-(a+b)^2+ab.
$$

The branch closure inequalities below are written in the ordered half $a\le b$.
The reflected half is obtained by swapping $a$ and $b$. Each branch records
both the admissibility inequalities for $\mathcal A$ and the corresponding
solved boundary value for $c(a,b)$. The formula convention assigns $q=0$ to the
$q\ge0$ branch.

If

$$
a^2+ab+b^2>1,
$$

then $c(a,b)$ is undefined.

## Branch $s<1$ and $q<0$

The corresponding branch closure in $\mathcal A$ is

$$
s\le1,\qquad a^2+ab+b^2\le1,\qquad q\le0,\qquad c^4-c^2+ac-a^2\le0.
$$

The boundary value $c(a,b)$ is the unique root in $(0,1]$ of

$$
c^4-c^2+mc-m^2=0.
$$

## Branch $s<1$ and $q\ge0$

The corresponding branch closure in $\mathcal A$ is

$$
s\le1,\qquad a^2+ab+b^2\le1,\qquad q\ge0,\qquad (s^2-1)c^2+bc-b^2\le0.
$$

The boundary value is

$$
c=\frac{2M}{1+\sqrt{4s^2-3}}.
$$

## Boundary $s=1$

The value on the shared boundary is

$$
c=M.
$$

## Branch $s>1$

The corresponding branch closure in $\mathcal A$ is

$$
s\ge1,\qquad a^2+ab+b^2\le1,\qquad (a^2-1)c^2+(2ab^2+b)c+(b^4-b^2)\le0,\qquad c\le\frac12.
$$

The boundary value is

$$
c=\frac{M(2mM+1)-\sqrt{M^2((2mM+1)^2-4(1-m^2)(1-M^2))}}{2(1-m^2)}.
$$

This is a computational boundary formula. Branch completeness and
uniqueness are separate proof obligations. In particular, do not invert
these equations into a definition of $B_c(a)$, $b(a,c)$, or $b(c,a)$
without checking the relevant admissible-cell inequalities and the intended
branch; otherwise an algebraic root may be a fake geometric solution.
