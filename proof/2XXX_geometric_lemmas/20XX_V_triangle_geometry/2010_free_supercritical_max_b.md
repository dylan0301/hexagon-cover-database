# Free Strict-Supercritical Outgoing Envelope

Status: Proven

This note records the free-input outgoing envelope for the strict demand
component

$$
a+b>1.
$$

It corrects the former closed-envelope statement. The maximum over
$a+b\ge1$ is a different quantity.

## Definitions

For $0\le c\le1$, define

$$
B^{\mathrm{free},+}(c)
=
\sup\left\{
b:\exists a\in[0,1]
\text{ with }(a,b,c)\in\mathcal A
\text{ and }a+b>1
\right\}.
$$

The corresponding closed-demand envelope is

$$
\overline B^{\mathrm{free},+}(c)
=
\max\left\{
b:\exists a\in[0,1]
\text{ with }(a,b,c)\in\mathcal A
\text{ and }a+b\ge1
\right\}.
$$

## Theorem

For the strict component,

$$
\boxed{
B^{\mathrm{free},+}(c)
=
\frac{c+\sqrt{c^2-8c+4}}2,
\qquad
0\le c<\frac12.
}
$$

The strict feasible set is empty for $c\ge1/2$, and the displayed supremum is
not attained.

For the closed-demand envelope,

$$
\boxed{
\overline B^{\mathrm{free},+}(c)=1,
\qquad
0\le c\le1.
}
$$

Indeed, $(0,1,c)$ is contained in

$$
\mathrm{conv}\left\{0,e_B,e_R\right\},
$$

and no boundary coordinate exceeds $1$.

## Proof of the strict formula

By the midpoint self-cover lemma, $c\ge1/2$ is impossible together with
$a+b>1$. For $c=0$, downward closure and the positive-$c$ cases proved below
give outgoing values arbitrarily close to $1$, while $b\le1$. Thus the formula
holds at $c=0$. Fix

$$
0<c<\frac12.
$$

Only outgoing values $b\ge1/2$ matter for the supremum. Put

$$
a=1-b,
\qquad
\kappa(b)=\frac{1-b^2}{2-b},
\qquad
\frac12\le b<1.
$$

We prove that the boundary triple $(a,b,c)$ has strict support slack, and
hence remains feasible after increasing $a$ slightly into $a+b>1$, exactly
when

$$
c<\kappa(b).
$$

Take the outer-normal angle modulo $120$ degrees between $-30$ degrees and
$90$ degrees, and put

$$
h=\frac{\sqrt3}{2}.
$$

Between $-30$ degrees and $30$ degrees, the three-point support sum for
$0,a e_A,b e_B$ is

$$
\cos\phi\ge h.
$$

Between $30$ degrees and $90$ degrees, put

$$
p=\cos\phi,
\qquad
q=\cos(120\text{ degrees}-\phi),
\qquad
t=\frac qp.
$$

Then

$$
p^2+pq+q^2=h^2.
$$

After division by $p$, the four-point support sum is

$$
N(t)=a+bt+\max\left\{at,b,c(1+t)\right\}.
$$

Set

$$
t_*=rac{2b-1}{1-b^2}.
$$

Whenever the maximum in $N$ is $b$,

$$
(1+bt)^2-(1+t+t^2)
=
t\left((2b-1)-(1-b^2)t\right).
$$

Thus strict slack occurs for $t>t_*$. The conditions

$$
at\le b,
\qquad
c(1+t)\le b
$$

allow such a value exactly when

$$
t_*<\frac bc-1.
$$

The other bound is automatic because $t_*<b/a$. The displayed inequality is
equivalent to

$$
c<\kappa(b).
$$

Therefore $c<\kappa(b)$ gives an orientation whose support sum is strictly
less than $h$. Continuity permits a small increase of $a$, producing a strict
supercritical demand triple.

Conversely, suppose

$$
c\ge\kappa(b).
$$

For $t\le t_*$, the term $b$ gives

$$
N(t)\ge\sqrt{1+t+t^2}.
$$

For $t\ge t_*$, it is enough by monotonicity in $c$ to take
$c=\kappa(b)$. Put

$$
A=a+\kappa(b),
\qquad
B=b+\kappa(b).
$$

Then $A<1<B$ for $b>1/2$, and

$$
(A+Bt)^2-(1+t+t^2)
$$

has negative constant term, positive leading coefficient, and positive root
$t=t_*$. The last identity follows from

$$
\kappa(b)(1+t_*)=b.
$$

Hence the expression is nonnegative for $t\ge t_*$. The endpoint $b=1/2$
is immediate. The boundary support minimum is therefore $h$, not below $h$.

Increasing $a$ by $\varepsilon>0$ changes the first-range support sum to

$$
(1+\varepsilon)\cos\phi>h.
$$

On the second range it strictly increases the positive-$p$ support
expressions. At the endpoint $p=0$, the support sum is already strict for
$b>1/2$ because $b+c>1$. Hence no strict triple with this $b$ exists.
Consequently the attainable strict
outgoing values approach exactly the values with

$$
c<\kappa(b).
$$

The function $\kappa$ decreases from $1/2$ to $0$. The supremum solves

$$
c=\kappa(b),
$$

or

$$
b^2-cb+2c-1=0.
$$

Taking the larger root proves the formula. Equality is not strict-feasible,
so it is a supremum rather than a maximum.

## Use in the proof tree

The radical above is the closure value of the strict component. It is not the
closed-demand maximum. Files using it as an upper bound for a genuinely
supercritical row may keep the radical, but should call it the free strict
supercritical supremum.
