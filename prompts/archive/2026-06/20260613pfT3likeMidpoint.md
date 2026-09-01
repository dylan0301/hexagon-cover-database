# Lemma: A T3-like $V_i$-triangle cannot contain $M_i$

## Statement

Let $H$ be the regular hexagon of side length $1$ centered at $O$, with vertices $V_0,\dots,V_5$, and let

$$
M_i=\frac12V_i
$$

be the midpoint of the radius $OV_i$.

Let $T_i$ be a closed unit equilateral triangle containing $V_i$. Suppose $T_i$ is T3-like, meaning that

$$
(o,n)=(2,1),
$$

where $o$ is the number of vertices of $T_i$ outside the closed hexagon $H$, and $n$ is the number of adjacent radial rays among $r_{i-1},r_{i+1}$ having positive-length intersection with $T_i$.

Then

$$
M_i\notin T_i.
$$

Equivalently, if a closed unit equilateral $V_i$-triangle contains $M_i$, then it is not T3-like.

## Proof

By the dihedral symmetry of the regular hexagon, it suffices to prove the claim for $i=0$.

Use local coordinates based at $V_0$:

$$
X=V_0+uE_-+vE_+,
$$

where

$$
E_-=V_5-V_0,\qquad E_+=V_1-V_0.
$$

Then

$$
V_0=(0,0),\qquad M_0=\left(\frac12,\frac12\right).
$$

The metric in these coordinates is

$$
\|(u,v)\|^2=u^2+v^2-uv.
$$

The hexagon is

$$
H=\{(u,v):0\le u\le2,\ 0\le v\le2,\ -1\le v-u\le1\}.
$$

The adjacent radial rays are

$$
r_5=\{(1,t):0\le t\le1\},
\qquad
r_1=\{(t,1):0\le t\le1\}.
$$

Let $T$ be a closed unit equilateral triangle containing

$$
V_0=(0,0)
\qquad\text{and}\qquad
M_0=\left(\frac12,\frac12\right).
$$

Assume, toward proving the stronger obstruction, that exactly two vertices of $T$ lie outside $H$. We will prove that $T$ has no positive-length intersection with either $r_5$ or $r_1$. Hence $n=0$, so $T$ cannot be T3-like.

Let the two outside vertices be $A$ and $B$, and let the remaining vertex be $C$.

Because $T$ is a unit equilateral triangle, its diameter is $1$. Since $(0,0)\in T$, every vertex $Z=(u,v)$ of $T$ satisfies

$$
u^2+v^2-uv\le1.
$$

We first record a basic consequence.

If $Z=(u,v)$ is a vertex of $T$ outside $H$, then $u<0$ or $v<0$. Indeed, if $u>2$, then

$$
u^2+v^2-uv=\left(v-\frac u2\right)^2+\frac34u^2>1,
$$

a contradiction. Similarly $v>2$ is impossible. If $u,v\ge0$ and $v-u>1$, write $v=u+d$ with $d>1$. Then

$$
u^2+v^2-uv=u^2+ud+d^2>d^2>1,
$$

again a contradiction. The case $u-v>1$ is identical. Hence the only possible violated hexagon inequalities are $u<0$ or $v<0$.

Moreover, every outside vertex has both coordinates strictly less than $1$. If $u<0$ and $v\ge1$, then

$$
u^2+v^2-uv>v^2\ge1,
$$

contradicting the strict positivity of $u^2-uv$ when $u<0$. Hence $v<1$. Similarly, if $v<0$, then $u<1$. Therefore each outside vertex satisfies

$$
u<1,\qquad v<1.
$$

It remains to prove that the third vertex $C$ also satisfies

$$
C_u\le1,\qquad C_v\le1.
$$

Order the two outside vertices $A,B$ so that, writing

$$
B-A=(r,s),
$$

the third vertex is

$$
C=A+(s,s-r).
$$

This is possible because the two possible third vertices over the side $AB$ are obtained by the two $60^\circ$ rotations, and swapping $A$ and $B$ exchanges them.

The unit side condition is

$$
r^2+s^2-rs=1.
$$

Since $(0,0)\in T$, write

$$
(0,0)=A+\lambda(B-A)+\mu(C-A),
$$

where

$$
\lambda\ge0,\qquad \mu\ge0,\qquad \lambda+\mu\le1.
$$

Thus

$$
A=-\lambda(r,s)-\mu(s,s-r).
$$

Consequently,

$$
A_u=-\lambda r-\mu s,
$$

$$
A_v=-\lambda s-\mu(s-r),
$$

$$
B_u=(1-\lambda)r-\mu s,
$$

$$
B_v=(1-\lambda)s-\mu(s-r),
$$

$$
C_u=-\lambda r+(1-\mu)s,
$$

$$
C_v=-\lambda s+(1-\mu)(s-r).
$$

Now impose $M_0=(1/2,1/2)\in T$. Since

$$
\frac12(r,s)+\frac12(s-r)(s,s-r)
$$

is not the correct expression, we compute directly:

$$
\frac r2(r,s)+\frac{s-r}{2}(s,s-r)=\left(\frac12,\frac12\right),
$$

because

$$
r^2+s^2-rs=1.
$$

Therefore the barycentric coordinates of $M_0$ are obtained from those of $(0,0)$ by adding

$$
\frac r2
$$

to the $B$-coordinate and adding

$$
\frac{s-r}{2}
$$

to the $C$-coordinate. Hence $M_0\in T$ is equivalent to

$$
\lambda+\frac r2\ge0,
$$

$$
\mu+\frac{s-r}{2}\ge0,
$$

$$
\lambda+\mu+\frac s2\le1.
$$

Set

$$
t=s-r.
$$

Then

$$
r^2+rt+t^2=1.
$$

Also,

$$
C_u=A_u+s=B_u+t,
$$

and

$$
C_v=A_v+t=B_v-r.
$$

Since $A$ and $B$ are outside vertices, each of them has either negative $u$-coordinate or negative $v$-coordinate. We split into the four possible sign cases.

### Case 1: $A_u<0$ and $B_u<0$

First prove $C_u\le1$.

If $s\le1$, then

$$
C_u=A_u+s<1.
$$

Assume $s>1$. The unit equation, viewed as a quadratic equation in $r$, gives

$$
r=\frac{s\pm\sqrt{4-3s^2}}2.
$$

For $s>1$, both roots are positive, so

$$
r>0,\qquad t=s-r>0.
$$

Also $r^2+rt+t^2=1$, so $t<1$. Since

$$
B_u=A_u+r<0,
$$

we have $A_u<-r$. Therefore

$$
C_u=A_u+s=A_u+r+t<t<1.
$$

Thus $C_u\le1$.

Now prove $C_v\le1$.

If $r\ge0$, then

$$
C_v=B_v-r\le B_v<1,
$$

because $B$ is an outside vertex and every outside vertex has $v<1$.

Assume $r<0$. Since $A_u=-\lambda r-\mu s<0$, we must have $s>0$. Put

$$
x=-r>0,\qquad y=s>0.
$$

Then

$$
x^2+y^2+xy=1.
$$

The containment inequality

$$
\lambda+\frac r2\ge0
$$

gives

$$
\lambda\ge\frac x2.
$$

Now

$$
C_v=-\lambda s+(1-\mu)(s-r)\le -\lambda y+x+y.
$$

Hence

$$
C_v\le x+y-\frac{xy}{2}.
$$

Let

$$
q=x+y.
$$

Since

$$
x^2+y^2+xy=1,
$$

we have

$$
q^2-xy=1,
$$

so

$$
xy=q^2-1.
$$

Therefore

$$
x+y-\frac{xy}{2}
=q-\frac{q^2-1}{2}
=1-\frac{(q-1)^2}{2}
\le1.
$$

Thus $C_v\le1$.

So in Case 1,

$$
C_u\le1,\qquad C_v\le1.
$$

### Case 2: $A_v<0$ and $B_v<0$

This is the reflection of Case 1 under the symmetry

$$
u\leftrightarrow v.
$$

Therefore again

$$
C_u\le1,\qquad C_v\le1.
$$

### Case 3: $A_u<0$ and $B_v<0$

First prove $C_u\le1$.

Suppose, for contradiction, that $s>1$. As in Case 1, this implies

$$
r>0,\qquad t=s-r>0,\qquad t<s.
$$

Since

$$
B_v=(1-\lambda)s-\mu t<0,
$$

we get

$$
\mu t>(1-\lambda)s.
$$

Because $s>t>0$, this implies

$$
\mu>1-\lambda.
$$

Hence

$$
\lambda+\mu>1,
$$

contradicting

$$
\lambda+\mu\le1.
$$

Therefore $s\le1$. Since $A_u<0$,

$$
C_u=A_u+s<1.
$$

Now prove $C_v\le1$.

Since

$$
C_v=B_v-r
$$

and $B_v<0$, it is enough to prove $r\ge-1$.

Suppose, for contradiction, that $r<-1$. The unit equation, viewed as a quadratic equation in $s$, gives

$$
s=\frac{r\pm\sqrt{4-3r^2}}2.
$$

For $r<-1$, both roots are negative. Hence

$$
s<0.
$$

But then

$$
A_u=-\lambda r-\mu s>0,
$$

because $\lambda,\mu\ge0$, $-r>0$, and $-s>0$. This contradicts $A_u<0$.

Therefore

$$
r\ge-1.
$$

Thus

$$
C_v=B_v-r<-r\le1.
$$

So in Case 3,

$$
C_u\le1,\qquad C_v\le1.
$$

### Case 4: $A_v<0$ and $B_u<0$

This is the reflection of Case 3 under

$$
u\leftrightarrow v.
$$

Therefore again

$$
C_u\le1,\qquad C_v\le1.
$$

The four cases cover all possibilities because each outside vertex must have either negative $u$-coordinate or negative $v$-coordinate. Hence in every case,

$$
C_u\le1,\qquad C_v\le1.
$$

We already proved that the outside vertices $A$ and $B$ satisfy

$$
A_u<1,\quad A_v<1,\quad B_u<1,\quad B_v<1.
$$

Therefore all vertices of $T$ lie in the closed half-planes

$$
u\le1,\qquad v\le1,
$$

and the only possible vertex on either boundary line $u=1$ or $v=1$ is $C$.

Now consider the adjacent ray

$$
r_5=\{(1,t):0\le t\le1\}.
$$

Since all vertices of $T$ satisfy $u\le1$, the intersection of $T$ with the line $u=1$ is the convex hull of the vertices of $T$ lying on $u=1$. But $A$ and $B$ have $u<1$, so at most the single vertex $C$ can lie on $u=1$. Thus

$$
T\cap r_5
$$

has zero length.

Similarly, since all vertices of $T$ satisfy $v\le1$ and $A,B$ have $v<1$, the intersection

$$
T\cap r_1
$$

also has zero length.

Therefore, if a unit equilateral $V_0$-triangle contains $M_0$ and has two vertices outside $H$, then it has

$$
n=0,
$$

not $n=1$.

A T3-like triangle has

$$
(o,n)=(2,1).
$$

Hence a T3-like $V_0$-triangle cannot contain $M_0$.

By rotational symmetry, for every $i$,

$$
T_i\text{ T3-like}\quad\Longrightarrow\quad M_i\notin T_i.
$$

This proves the lemma.