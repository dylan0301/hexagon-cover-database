# T3-like Loss Bound from the Tangent Envelope

Status: Proven analytic inequality conditional on local envelope

This file proves the analytic consequences of the full T3-like tangent-envelope
conjecture from `651_full_T3_like_tangent_envelope_conjecture.md`.

The local envelope itself is not proved here.  The statements below are rigorous
conditional consequences of that envelope.

## Notation

For the upper tangent branch, set

$$
A(s)=\frac{s(s^2-s+1)}{1-s^2},
\qquad
B(s)=\frac{s^2-s+1}{1+s},
\qquad
F(s)=\frac{(s^2-s+1)^2}{1-s^2},
$$

where

$$
0\le s\le\frac12.
$$

The reflected branch is obtained by swapping $A(s)$ and $B(s)$ while keeping the
same area value $F(s)$.

Write

$$
G(s)=1-F(s).
$$

For a T3-like row with required lower-bound data $(a,b)$, write

$$
G_{\mathrm{T3}}(a,b)=1-f_{\mathrm{T3}}(a,b).
$$

The smaller coordinate on either reflected tangent branch is $A(s)$.  Indeed,

$$
B(s)-A(s)
=\frac{(2s-1)(s^2-s+1)}{(s-1)(s+1)}\ge0
$$

for $0\le s\le1/2$.

## Lemma 652.1: branch rows are nonsupercritical

For every $s\in[0,1/2]$,

$$
A(s)+B(s)\le1.
$$

Consequently, under the tangent-envelope conjecture, every T3-like row satisfies

$$
a+b\le1.
$$

### Proof

First,

$$
B(s)=\frac{s^2-s+1}{1+s}
=\frac{(1-s)(s^2-s+1)}{1-s^2}.
$$

Therefore

$$
A(s)+B(s)
=\frac{s(s^2-s+1)+(1-s)(s^2-s+1)}{1-s^2}
=\frac{s^2-s+1}{1-s^2}.
$$

Thus $A(s)+B(s)\le1$ is equivalent to

$$
s^2-s+1\le1-s^2,
$$

which is equivalent to

$$
2s^2-s\le0.
$$

This holds exactly for $0\le s\le1/2$.  Hence every point on the upper branch is
nonsupercritical.  The reflected branch has the same sum, so the same conclusion
holds for it.

Now assume the tangent-envelope conjecture.  If a T3-like row with lower-bound
coordinates $(a,b)$ is dominated by the upper branch, then for some
$s\in[0,1/2]$,

$$
a\le A(s),
\qquad
b\le B(s).
$$

Hence

$$
a+b\le A(s)+B(s)\le1.
$$

If it is dominated by the reflected branch, then

$$
a\le B(s),
\qquad
b\le A(s),
$$

and the same sum bound gives $a+b\le1$.  Therefore every T3-like row is
nonsupercritical.  This proves the lemma.

## Lemma 652.2: pointwise small-coordinate branch loss bound

For every $s\in[0,1/2]$,

$$
G(s)\ge 2A(s)-4A(s)^2.
$$

This is the relevant bound for both reflected tangent branches, because $A(s)$
is the smaller of the two branch coordinates.

### Proof

A direct simplification gives

$$
G(s)-\bigl(2A(s)-4A(s)^2\bigr)
=
\frac{s^2\left(5s^4-8s^3+13s^2-8s+2\right)}{(1-s^2)^2}.
$$

The denominator is positive on $[0,1/2]$.  It remains to check that

$$
Q(s)=5s^4-8s^3+13s^2-8s+2
$$

is positive on $[0,1/2]$.

Since $0\le s\le1/2$, we have $8s^3\le4s^2$, and therefore

$$
-8s^3\ge -4s^2.
$$

Hence

$$
Q(s)
\ge
5s^4+9s^2-8s+2
\ge
9s^2-8s+2.
$$

The quadratic $9s^2-8s+2$ has its minimum at $s=4/9$, and

$$
9\left(\frac49\right)^2-8\left(\frac49\right)+2=\frac29>0.
$$

Thus $Q(s)>0$ on $[0,1/2]$, so

$$
G(s)\ge 2A(s)-4A(s)^2.
$$

This proves the lemma.

## Lemma 652.3: branch loss is at least $1/4$ past $A=1/4$

If $s\in[0,1/2]$ and $A(s)\ge1/4$, then

$$
G(s)\ge\frac14.
$$

### Proof

For $s=0$ the hypothesis $A(s)\ge1/4$ is false.  For $s>0$,

$$
\frac{A(s)}s=\frac{s^2-s+1}{1-s^2}.
$$

On $[0,1/2]$,

$$
\frac{s^2-s+1}{1-s^2}\le1
$$

is equivalent to

$$
2s^2-s\le0,
$$

which holds.  Thus $A(s)\le s$.  If $A(s)\ge1/4$, then $s\ge1/4$.

Now compute

$$
G(s)-\frac14
=
\frac{(1-2s)(2s^3-3s^2+6s-1)}{4(1-s^2)}.
$$

For $s\in[1/4,1/2]$, the factor $1-2s$ is nonnegative.  Also

$$
P(s)=2s^3-3s^2+6s-1
$$

is strictly increasing on all real $s$, because

$$
P'(s)=6s^2-6s+6=6\left(s^2-s+1\right)>0.
$$

At $s=1/4$,

$$
P\left(\frac14\right)=\frac{11}{32}>0.
$$

Therefore $P(s)>0$ on $[1/4,1/2]$, and hence

$$
G(s)\ge\frac14.
$$

This proves the lemma.

## Theorem 652.4: local T3-like loss bound from the envelope

Assume the full tangent-envelope conjecture from
`651_full_T3_like_tangent_envelope_conjecture.md`.

Let $0\le m\le1/2$.  If a T3-like row has lower-bound coordinates satisfying

$$
a\ge m,
\qquad
b\ge m,
$$

then

$$
\boxed{
G_{\mathrm{T3}}(a,b)\ge 2m-4m^2.
}
$$

### Proof

By the tangent-envelope conjecture, every T3-like candidate with local data
$(a,b)$ is dominated by either the upper branch or the reflected branch.

If it is dominated by the upper branch at parameter $s$, then

$$
A(s)\ge a\ge m.
$$

If it is dominated by the reflected branch at parameter $s$, then

$$
A(s)\ge b\ge m.
$$

Thus in either case the smaller tangent coordinate satisfies

$$
A(s)\ge m.
$$

Let

$$
\psi(u)=2u-4u^2.
$$

The function $\psi$ is increasing on $[0,1/4]$ and satisfies

$$
\psi(u)\le\frac14
$$

for every $u\in[0,1/2]$.

If $A(s)\le1/4$, then Lemma 652.2 gives

$$
G(s)\ge\psi(A(s)).
$$

Since $A(s)\ge m$ and $\psi$ is increasing on $[0,1/4]$,

$$
G(s)\ge\psi(m)=2m-4m^2.
$$

If $A(s)\ge1/4$, then Lemma 652.3 gives

$$
G(s)\ge\frac14.
$$

Since $m\in[0,1/2]$, we have $\psi(m)\le1/4$, and therefore

$$
G(s)\ge\psi(m)=2m-4m^2.
$$

Thus every tangent-envelope dominator has outside loss at least $2m-4m^2$.
Taking the supremum over all T3-like candidates gives

$$
G_{\mathrm{T3}}(a,b)\ge2m-4m^2.
$$

This proves the theorem.