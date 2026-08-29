# CE1/CE2, $N_+=1$, Exactly One T3-Like: Direct Rescuer-Witness Proof

Status: Proven

This proof replaces the former adjacent-rescuer chain by one explicit radial
endpoint and a direct boundary-path budget.  No composition of local transfer
maps is used.

## Theorem

Assume the center is CE1 or CE2, exactly one actual V role is supercritical,
exactly one V role is T3-like, no V role is Vd1 or Vd2, the roles cover the
full skeleton, and at least one boundary edge contains a V-gap.  Then no such
configuration exists.

## 1. Midpoint reduction

Normalize the unique center midpoint to $M_0$.  The T3-like role cannot cover
its own midpoint, while a supercritical role covers none of its three local
midpoints.  A Vd0 role cannot rescue an adjacent midpoint.  Therefore, after
reflection,

$$
T_0\text{ is T3-like},
\qquad
M_1\in T_0,
$$

$$
T_1\text{ is uniquely supercritical},
$$

and $T_2,T_3,T_4,T_5$ are nonsupercritical Vd0 roles.  This is the direct
midpoint argument recorded in the former `4131` note; it uses no reach
propagation.

## 2. The finite radial witness

Use the normalized T3-like chart at $V_0$.  After the trace-dominating
translation, let

$$
T_0\cap e_{5,0}=[0,a]
$$

and let the positive trace on $r_1$, measured from $V_1$ toward $O$, be

$$
T_0\cap r_1=[c,u].
$$

The midpoint rescue gives

$$
c\le\frac12\le u.
$$

Put

$$
P_T=(1-u)V_1.
\tag{1}
$$

The point $P_T$ is the O-side endpoint of the T3-like interval.  It is not in
the open role $U_0$.  The supercritical role $U_1$ contains $V_1$ but misses
$M_1$, so convexity excludes every point on the O-side of $M_1$.  The four
remaining roles are Vd0 and have no positive adjacent support on $r_1$.
Hence all six V roles miss $P_T$, and skeleton coverage forces

$$
\boxed{P_T\in U_C.}
\tag{2}
$$

Thus the center reaches at least

$$
\varepsilon=1-u
$$

from $O$ on $r_1$.

## 3. T3-like local inequalities

The normalized T3-like form has parameters

$$
1\le D\le\frac2{\sqrt3},
\qquad
E=\sqrt{4-3D^2},
\qquad
R_{\rm loc}=\frac{D+E}{2},
$$

and

$$
\frac{E}{2D}
\le a\le
\frac{4-3D+E}{4D}.
$$

Its radial endpoints are

$$
c=\frac{D(1+a)-1}{R_{\rm loc}},
\qquad
u=1-\frac{R_{\rm loc}}D+a.
$$

Put

$$
x=\frac{aD}{R_{\rm loc}}.
$$

For $0\le c\le1/2$, let

$$
M_c^{\rm sup}
=
\frac{c+\sqrt{c^2-8c+4}}2
$$

be the free strict-supercritical outgoing envelope.  We prove

$$
\boxed{
a\le1-M_c^{\rm sup},
\qquad
\frac{a}{a+1-u}\le1-M_c^{\rm sup}.
}
\tag{3}
$$

Put

$$
\theta=\frac{D-1}{R_{\rm loc}}.
$$

The unit relation gives

$$
R_{\rm loc}=\frac{1-2\theta}{1-\theta+\theta^2},
\qquad
D=\frac{1-\theta^2}{1-\theta+\theta^2},
$$

and

$$
0\le\theta\le2-\sqrt3.
$$

Moreover

$$
c=x+\theta
$$

and the midpoint inequalities become

$$
\frac{1-4\theta+\theta^2}{2(1-2\theta)}
\le x\le\frac12-\theta.
\tag{4}
$$

For $0\le z\le1/2$, put

$$
\sigma(z)=\frac{z(2-z)}{1+z}.
$$

The defining relation for the strict-supercritical envelope is

$$
\sigma(1-M_c^{\rm sup})=c,
$$

and $\sigma$ is strictly increasing.  Thus it is enough to prove

$$
\sigma(x)\le x+\theta.
$$

After multiplication by $1+x$, this is

$$
Q_\theta(x):=2x^2+(\theta-1)x+\theta\ge0.
\tag{5}
$$

If $0\le\theta\le1/5$, the feasible interval in (4) lies to the right of the
vertex of $Q_\theta$, and substitution of its left endpoint gives

$$
Q_\theta(x)
\ge
\frac{\theta(1-5\theta+11\theta^2-\theta^3)}
{2(1-2\theta)^2}
\ge0.
$$

If $1/5\le\theta\le2-\sqrt3$, the vertex lies inside the feasible interval
and

$$
Q_\theta(x)
\ge
\frac{10\theta-1-\theta^2}{8}>0.
$$

This proves $x\le1-M_c^{\rm sup}$.  Since $D\ge R_{\rm loc}$,

$$
a\le x\le1-M_c^{\rm sup}.
$$

Also

$$
1-u=\frac{R_{\rm loc}}D-a,
$$

so

$$
\frac{a}{a+1-u}
=\frac{aD}{R_{\rm loc}}
=x
\le1-M_c^{\rm sup}.
$$

This proves (3).

## 4. The center cannot hide the boundary tail

Let the possible companion center trace on $e_{5,0}$ be

$$
J_L=\left[\frac{k}{W},R+\alpha\right]
$$

when it exists.  Let $h$ be the reach forced on $T_5$ from $V_5$ toward
$V_0$.

If the companion trace is absent, or does not hide the endpoint $a$, then

$$
h\ge1-a\ge M_c^{\rm sup}.
$$

In the only hiding configuration,

$$
\frac{k}{W}\le a<R+\alpha.
$$

The center contains the radial witness (1), so its exit on $r_1$ satisfies

$$
\frac\delta R\ge1-u.
$$

The left endpoint inequality gives $k\le Wa$.  Hence

$$
R(a+1-u)\le a,
\qquad
R\le\frac{a}{a+1-u}.
$$

The far center endpoint satisfies

$$
R+\alpha
\le
\frac{a}{a+1-u}
\le1-M_c^{\rm sup}.
$$

Therefore the remaining far-side boundary demand is again

$$
\boxed{h\ge M_c^{\rm sup}.}
\tag{6}
$$

## 5. Direct boundary-path contradiction

The strict-supercritical role $T_1$ has own-radial demand at least $c$, so the
free envelope gives

$$
\boxed{B_1<M_c^{\rm sup}.}
\tag{7}
$$

The four ordinary roles must cover the center-free boundary path from
$e_{1,2}$ to $e_{5,0}$.  Thus

$$
A_2\ge1-B_1,
$$

$$
B_2+A_3\ge1,
\qquad
B_3+A_4\ge1,
\qquad
B_4+A_5\ge1,
$$

and $B_5\ge h$.  Adding and using (6)--(7),

$$
\sum_{i=2}^5(A_i+B_i)
\ge4+h-B_1>4.
$$

But every $T_i$, $2\le i\le5$, is nonsupercritical, so the same sum is at
most four.  This contradiction proves the theorem.

The finite center witness is the radial endpoint $P_T$, together with the
actual boundary gap endpoints.  The proof uses only its forced center reach,
the local T3-like inequality, and one direct boundary-path sum.

$$
\Box
$$
