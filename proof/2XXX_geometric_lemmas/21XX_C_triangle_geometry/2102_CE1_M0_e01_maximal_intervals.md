# CE1, Exact Midpoint $M_0$, Edge $e_{0,1}$: Maximal Intervals

Status: Proven

This note proves the normalized CE1 subcase in which

$$
T_C\cap \{M_0,\dots,M_5\}=\{M_0\}
$$

and the unique positive-length overlap with the hexagon boundary is on

$$
e_{0,1}.
$$

Write

$$
T_C\cap e_{0,1}=[s,t]
$$

in the edge parameter $e_{0,1}(b)=V_0+b(V_1-V_0)$.

## Theorem

The maximal feasible intervals are exactly

$$
\boxed{\displaystyle [s,t]=[s,\sqrt{s^2-s+1}-(1-s)^2],\quad 0\lt s\lt 1}
$$

Maximality is interval inclusion:

$$
[s,t]\preceq [s',t'] \quad\Longleftrightarrow\quad s'\le s,\quad t'\ge t.
$$

The endpoints $s=0$ and $s=1$ are not feasible maximal intervals. They are limiting degeneracies.

## Coordinates

Use the affine coordinates based at $V_0$

$$
X=V_0+b(V_1-V_0)+a(V_5-V_0).
$$

Then

$$
V_0=(0,0),\quad V_1=(1,0),\quad V_5=(0,1),
$$

and the remaining vertices are

$$
V_2=(2,1),\quad V_3=(2,2),\quad V_4=(1,2).
$$

The center and radial midpoints are

$$
O=(1,1),
$$

$$
M_0=\left(\frac12,\frac12\right),\quad M_1=\left(1,\frac12\right),\quad M_2=\left(\frac32,1\right),
$$

$$
M_3=\left(\frac32,\frac32\right),\quad M_4=\left(1,\frac32\right),\quad M_5=\left(\frac12,1\right).
$$

The target edge $e_{0,1}$ is $a=0,\ 0\le b\le1$, so its edge parameter is $b$.

## Unit-triangle side model

Let $\lambda>0$ and

$$
\rho=\sqrt{1-\lambda+\lambda^2}.
$$

Define three affine functions

$$
F_1=\lambda b+(1-\lambda)a-\lambda s,
$$

$$
F_2=-b+\lambda a+t,
$$

$$
F_0=(1-\lambda)b-a+\rho+\lambda s-t.
$$

Their sum is constant:

$$
F_0+F_1+F_2=\rho.
$$

In these affine coordinates, if $F=pb+ra+c$, then its physical gradient satisfies

$$
\|\nabla F\|^2=\frac43(p^2+pr+r^2).
$$

For each of $F_0,F_1,F_2$, the quantity $p^2+pr+r^2$ equals $\rho^2$. After multiplying by

$$
\kappa=\frac{\sqrt3}{2\rho},
$$

the gradients of $\kappa F_0,\kappa F_1,\kappa F_2$ are unit vectors. Since $F_0+F_1+F_2$ is constant, those three gradients sum to zero and are therefore separated by $120^\circ$. Therefore

$$
T(\lambda,s,t)=\{F_0\ge0,\ F_1\ge0,\ F_2\ge0\}
$$

is a closed unit equilateral triangle.

On $e_{0,1}$, where $a=0$,

$$
F_1=\lambda(b-s),\qquad F_2=t-b,
$$

and

$$
F_0=\rho+\lambda s-t+(1-\lambda)b.
$$

Thus $F_1$ cuts the left endpoint and $F_2$ cuts the right endpoint.

Every CE1 candidate of this normalized type has such a representation after labeling the two side-lines that cut $e_{0,1}$. The ratio of the two edge slopes is $\lambda:1$. The signs of the $a$-coefficients are the signs for which the triangle lies toward $O$, and the third side is forced by the unit-equilateral relation.

## Excluding $\lambda\ge1$

If $\lambda=1$, then $\rho=1$. The condition $O\in T$ gives

$$
F_0(O)=s-t\ge0,
$$

contradicting the positive-length condition $s<t$.

Now assume $\lambda>1$. The conditions $O\in T$ and $s<t$ imply

$$
s< t\le \rho-\lambda(1-s),
$$

hence

$$
s>\frac{\lambda-\rho}{\lambda-1}.
$$

The exclusion of $M_1$ must occur through $F_2(M_1)<0$: indeed $F_1(M_1)>0$ follows from $M_0\in T$, and $F_0(M_1)=F_0(O)+1/2\ge0$. Hence

$$
t<1-\frac{\lambda}{2}.
$$

Since $s<t$,

$$
s<1-\frac{\lambda}{2}.
$$

But

$$
\frac{\lambda-\rho}{\lambda-1} \ge 1-\frac{\lambda}{2}.
$$

Indeed, this is equivalent to

$$
\frac{\lambda^2-\lambda+2}{2}\ge \rho,
$$

and after squaring,

$$
\left(\frac{\lambda^2-\lambda+2}{2}\right)^2-\rho^2 = \frac{(\lambda^2-\lambda)^2}{4}\ge0.
$$

Thus $\lambda>1$ is impossible. Hence every feasible target interval is represented with

$$
0<\lambda<1.
$$

## Exact inequalities for the target

For $0<\lambda<1$, the target is equivalent to the following system:

$$
0<\lambda<1,\qquad 0\le s<t\le1,
$$

$$
t+\lambda(1-s)\le \rho,
$$

$$
t\ge1-\lambda,
$$

$$
\lambda s\le \frac12,
$$

$$
t<1-\frac{\lambda}{2},
$$

$$
t>\rho+\lambda s-\frac{1+\lambda}{2},
$$

$$
t\ge \rho-\frac{\lambda^2}{1-\lambda}s.
$$

The first three nontrivial inequalities are $O\in T$:

$$
F_0(O)=\rho+\lambda s-t-\lambda\ge0,
$$

$$
F_1(O)=1-\lambda s\ge0,
$$

$$
F_2(O)=t+\lambda-1\ge0.
$$

The stronger midpoint condition $M_0\in T$ replaces $F_1(O)\ge0$ by

$$
F_1(M_0)=\frac12-\lambda s\ge0,
$$

so

$$
\lambda s\le \frac12.
$$

The other two inequalities for $M_0$ follow from $O\in T$ and $t\ge1-\lambda$.

The exclusion of $M_1$ is equivalent to

$$
F_2(M_1)=t-1+\frac{\lambda}{2}<0,
$$

so

$$
t<1-\frac{\lambda}{2}.
$$

The exclusion of $M_5$ is equivalent to

$$
F_0(M_5)= \rho+\lambda s-t-\frac{1+\lambda}{2}<0,
$$

so

$$
t>\rho+\lambda s-\frac{1+\lambda}{2}.
$$

Then $M_2,M_3,M_4$ are automatically excluded:

* $M_1\notin T$ forces $M_2\notin T$, because
  $$
  F_2(M_2) = t+\lambda-\frac32 < -\frac{1-\lambda}{2}<0.
  $$

* $M_5\notin T$ forces $M_4\notin T$, because
  $$
  F_0(M_4) = F_0(M_5)-\frac{\lambda}{2}<0.
  $$

* If $\lambda\le\frac12$, then
  $$
  F_2(M_3) = t-\frac32+\frac{3\lambda}{2} < \lambda-\frac12 \le0,
  $$
  with strict negativity coming from $t<1-\lambda/2$. If $\lambda\ge\frac12$, then
  $$
  F_0(M_3) = F_0(M_5)+\frac{1-2\lambda}{2}<0.
  $$

It remains to encode the CE1 boundary-edge condition.

### The target edge

On $e_{0,1}$, $a=0$. Since $F_1=\lambda(b-s)$ and $F_2=t-b$, and since the $O$-constraint gives $F_0(0)\ge\lambda>0$,

$$
T\cap e_{0,1}=[s,t].
$$

### The adjacent edge $e_{5,0}$

On the edge from $V_0$ to $V_5$, write $b=0$ and $0\le a\le1$. Then

$$
F_1=(1-\lambda)a-\lambda s,
$$

$$
F_2=t+\lambda a>0,
$$

$$
F_0=\rho+\lambda s-t-a.
$$

Thus $T\cap e_{5,0}$ has positive length exactly when

$$
\frac{\lambda s}{1-\lambda} < \rho+\lambda s-t.
$$

Therefore no positive-length overlap with $e_{5,0}$ is equivalent to

$$
t\ge \rho-\frac{\lambda^2}{1-\lambda}s.
$$

Equality is allowed: it is a single boundary point, not a positive-length edge overlap.

### The other boundary edges

The remaining edges have no positive-length overlap automatically.

On $e_{1,2}$, write $b=1+u,\ a=u,\ 0\le u\le1$. Then

$$
F_2=t-1-(1-\lambda)u<0,
$$

because $t<1-\lambda/2<1$.

On $e_{2,3}$, write $b=2,\ a=1+u,\ 0\le u\le1$. Here $F_1>0$, while $F_2\ge0$ requires

$$
u\ge \frac{2-\lambda-t}{\lambda},
$$

and $F_0\ge0$ requires

$$
u\le \rho+\lambda s-t+1-2\lambda.
$$

The upper endpoint minus the lower endpoint is strictly less than

$$
\frac{-3\lambda^2+2\lambda\rho+2\lambda-2}{2\lambda} \le \frac{-3\lambda^2+4\lambda-2}{2\lambda}<0,
$$

using $\rho\le1$. Hence no interval exists.

On $e_{3,4}$, write $a=2,\ 1\le b\le2$. The simultaneous conditions $F_0\ge0$ and $F_2\ge0$ would require

$$
\frac{2-\rho-\lambda s+t}{1-\lambda} \le b \le 2\lambda+t.
$$

The right endpoint minus the left endpoint is at most

$$
\frac{\rho+\lambda-\lambda^2-\frac32}{1-\lambda}<0.
$$

The strict inequality follows from

$$
\rho<\frac32-\lambda+\lambda^2,
$$

because

$$
\left(\frac32-\lambda+\lambda^2\right)^2-\rho^2 = \frac{4\lambda^4-8\lambda^3+12\lambda^2-8\lambda+5}{4}>0.
$$

On $e_{4,5}$, write $a=b+1,\ 0\le b\le1$. Then

$$
F_0=\rho+\lambda s-t-1-\lambda b.
$$

Using the strict $M_5$-exclusion inequality,

$$
F_0 < \frac{1+\lambda}{2}-1-\lambda b = -\frac{1-\lambda}{2}-\lambda b<0.
$$

Thus all non-target boundary edges have zero positive-length overlap.

## Maximal interval derivation

From $O\in T$,

$$
t+\lambda(1-s)\le \rho,
$$

so

$$
t\le \rho-\lambda(1-s).
$$

From the no-positive-overlap condition on $e_{5,0}$,

$$
t\ge \rho-\frac{\lambda^2}{1-\lambda}s.
$$

The two inequalities are compatible only if

$$
\rho-\frac{\lambda^2}{1-\lambda}s \le \rho-\lambda(1-s).
$$

Since $0<\lambda<1$, this is equivalent to

$$
\lambda\ge1-s.
$$

Let

$$
a=1-s.
$$

Then $0<a<1$, and every feasible interval satisfies $\lambda\ge a$. The upper bound becomes

$$
t\le \sqrt{1-\lambda+\lambda^2}-a\lambda.
$$

For $\lambda\in[a,1)$, write $\lambda=a+d$, with $d\ge0$. Let

$$
R_a=\sqrt{1-a+a^2}.
$$

We claim

$$
\sqrt{1-\lambda+\lambda^2}-a\lambda \le R_a-a^2.
$$

Equivalently,

$$
\sqrt{1-\lambda+\lambda^2} \le R_a+ad.
$$

After squaring, this becomes

$$
d(1-a^2)\le 1-2a+2aR_a.
$$

Since $0\le d\le1-a$,

$$
d(1-a^2)\le (1-a)(1-a^2).
$$

Also,

$$
1-2a+2aR_a-(1-a)(1-a^2) = a(2R_a-1+a-a^2) = aR_a(2-R_a)>0.
$$

Therefore the desired inequality holds, and it is strict unless $d=0$. Hence every feasible interval satisfies

$$
t\le R_a-a^2 = \sqrt{s^2-s+1}-(1-s)^2.
$$

So every feasible interval $[s,t]$ is contained in

$$
\left[ s,\, \sqrt{s^2-s+1}-(1-s)^2 \right].
$$

## Feasibility of the frontier

Fix $0<s<1$, and set

$$
\lambda=1-s, \qquad \rho=\sqrt{s^2-s+1},
$$

$$
t=\rho-(1-s)^2.
$$

Then the $O$-constraint

$$
t+\lambda(1-s)\le\rho
$$

holds with equality. Thus $O$ lies on one side of the triangle.

The no-positive-overlap condition on $e_{5,0}$ also holds with equality:

$$
t = \rho-\frac{\lambda^2}{1-\lambda}s.
$$

Thus $T\cap e_{5,0}$ is a single point.

The target overlap has positive length because

$$
t-s = \rho-(s^2-s+1) = \rho-\rho^2 = \rho(1-\rho)>0,
$$

as $0<s<1$ implies $\sqrt3/2<\rho<1$.

The strict midpoint exclusions hold. For $M_1$,

$$
\rho-(1-s)^2 < 1-\frac{1-s}{2},
$$

because this is equivalent, after putting $a=1-s$, to

$$
\sqrt{1-a+a^2}<1-\frac a2+a^2,
$$

and the square of the right side exceeds $1-a+a^2$ by

$$
\frac{a^2(4a^2-4a+5)}{4}>0.
$$

For $M_5$, the strict margin is

$$
t-\left(\rho+\lambda s-\frac{1+\lambda}{2}\right) = \frac{s}{2}>0.
$$

Thus every interval

$$
\left[ s,\, \sqrt{s^2-s+1}-(1-s)^2 \right], \qquad 0<s<1,
$$

is feasible.

## Mutual incomparability

Let

$$
f(s)=\sqrt{s^2-s+1}-(1-s)^2.
$$

Then

$$
f'(s)=2-2s+\frac{2s-1}{2\sqrt{s^2-s+1}}>0
$$

for $0<s<1$.

If $s\ge1/2$, this is immediate. If $s<1/2$, then
$$
\sqrt{s^2-s+1}>1-s,
$$
so
$$
4(1-s)\sqrt{s^2-s+1}+2s-1 > 4(1-s)^2+2s-1 = 4s^2-6s+3>0.
$$

Therefore $f$ is strictly increasing. If $s_1<s_2$, then

$$
s_1<s_2,\qquad f(s_1)<f(s_2),
$$

so neither frontier interval contains the other. This proves maximality by interval inclusion.

## Boundary cases and degeneracies

At $s=0$, the inequalities are incompatible. The no-$e_{5,0}$-overlap condition gives

$$
t\ge\rho,
$$

while $O\in T$ gives

$$
t\le\rho-\lambda,
$$

which is impossible for $\lambda>0$.

At $s=1$, the formula gives

$$
t=1,
$$

so the overlap has zero length.

The endpoint $t=1$ is impossible for any nondegenerate feasible interval: if $V_1\in T_C$, then convexity and $O\in T_C$ imply

$$
M_1=\frac12V_1\in T_C,
$$

contradicting the exact midpoint subset $\{M_0\}$.

On every maximal interval, two boundary degeneracies occur and are allowed:

$$
O\in\partial T_C,
$$

and

$$
T_C\cap e_{5,0}
$$

is one point. Neither violates CE1, because CE1 excludes only positive-length overlap with any boundary edge other than $e_{0,1}$.

## Numerical verification

The numerical check used the vertex/determinant containment predicates rather than the symbolic inequalities above.

For each sampled unit equilateral triangle $Q_0Q_1Q_2$, the test:

1. checked $O\in T_C$ and $M_0\in T_C$;
2. rejected the triangle if any of $M_1,\dots,M_5$ was contained;
3. intersected the triangle with each hexagon edge by substituting the edge parameter into the three determinant inequalities;
4. retained only those triangles with positive-length overlap on $e_{0,1}$ and zero positive-length overlap on every other boundary edge;
5. checked the inequality
   $$
   t\le \sqrt{s^2-s+1}-(1-s)^2.
   $$

The sampling was intentionally concentrated near the Pareto front. The front triangles are realized by the two tight conditions

$$
O\in\partial T_C, \qquad T_C\cap e_{5,0}\text{ is a single point}.
$$

The run used seed `20260506`.

| source | tested | retained feasible | retention rate |
|---|---:|---:|---:|
| exact predicted frontier | 8,000 | 7,970 | 0.996250 |
| center-angle perturbations near frontier | 90,000 | 12,635 | 0.140389 |
| half-plane biased samples near frontier constraints | 90,000 | 84,906 | 0.943400 |
| uniform center-angle baseline | 50,000 | 56 | 0.001120 |

Total retained feasible samples:

$$
105567.
$$

The exact-front reconstruction error was

$$
\max |s_{\rm recomputed}-s_{\rm source}|=2.18\cdot10^{-11},
$$

$$
\max |t_{\rm recomputed}-f(s_{\rm source})|=4.44\cdot10^{-16}.
$$

Across all retained feasible samples,

$$
\max(t-f(s))=6.44\cdot10^{-14}.
$$

The number of retained samples with

$$
t>f(s)+10^{-9}
$$

was zero, and the number with

$$
t>f(s)+10^{-7}
$$

was also zero.

The finite-sample nondominated set contained $17,866$ intervals. Its median slack below the analytic frontier was

$$
4.40\cdot10^{-9},
$$

and the worst slack was

$$
2.37\cdot10^{-4}.
$$

The $30$ rejected exact-front cases were all extremely close to the degenerate endpoint $s=1$, where the strict exclusion of $M_1$ has vanishing numerical margin. They are numerical tolerance rejections, not mathematical counterexamples.

A compact version of the check is:

```python
def f(s):
    return (s*s - s + 1.0)**0.5 - (1.0 - s)**2

def accept(Q):
    if not contains_triangle(Q, O):
        return None
    if not contains_triangle(Q, M[0]):
        return None
    if any(contains_triangle(Q, M[i]) for i in range(1, 6)):
        return None

    intervals = [triangle_edge_interval(Q, i) for i in range(6)]
    if intervals[0] is None:
        return None
    s, t = intervals[0]
    if t - s <= 1e-8:
        return None

    for i in range(1, 6):
        if intervals[i] is not None:
            u, v = intervals[i]
            if v - u > 1e-8:
                return None

    return s, t

max_overshoot = -float("inf")
for Q in targeted_frontier_and_perturbation_samples(seed=20260506):
    interval = accept(Q)
    if interval is None:
        continue
    s, t = interval
    max_overshoot = max(max_overshoot, t - f(s))

assert max_overshoot <= 1e-9
```

This numerical test supports both the analytic upper envelope and the interval-inclusion maximality statement.
