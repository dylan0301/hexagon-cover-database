# Lower-Sheet $T_+$ Completion Proofs

Status: Reference

Dependency warning: the sheet called $T_+^{lo}$ below is the fake high-$c$
component removed by the exact audit in `2007` and `4015`. The analytic
inequalities are retained as historical relaxation calculations, not as a
proof of realized geometric branch completeness.

This file records the formal lower-sheet $T_+$ calculations that were left
open in the historical branch inventory.

The notation is inherited from the old setup and branch-realization notes. On
the main $r>1$ center-triangle branch,
write

$$
R={1\over r},\qquad S=\sqrt{1-R+R^2},\qquad \delta={R\over1+S},\qquad 0<R<1.
$$

The active boundary interval is

$$
[s,t],\qquad u=1-t,\qquad w=t-s,\qquad s=1-u-w,\qquad w>0.
$$

The two radial exits are

$$
\gamma_1=1-ru,
$$

and

$$
\gamma_5=u-\delta-{R\over1-R}w.
$$

The boundary-loss objective is

$$
F=B(s,1-\gamma_5)+B(u,1-\gamma_1)=B_5+B_1.
$$

The intended demand-coordinate relaxation was

$$
B(a,c)=
\max_{\substack{
0\le b\le1-a\\
{}(a,b,c)\in\mathcal A
}}b.
$$

That sentence in the former version was false for $T_+^{lo}$. The corrected
component selectors remove this sheet, so every calculation involving it
below is historical algebra rather than a realized maximal branch.

## 1. Sheet notation

For a $T_+$ branch, write

$$
\mu=a+b,\qquad \beta={b\over c}.
$$

The $T_+$ equation is

$$
((a+b)^2-1)c^2+bc-b^2=0,
$$

or equivalently

$$
\beta^2-\beta+1-\mu^2=0.
$$

Thus

$$
\beta_\pm(\mu)={1\pm\sqrt{4\mu^2-3}\over2}.
$$

The two sheets are

$$
T_+^{hi}: b=c\beta_+(\mu),
$$

and

$$
T_+^{lo}: b=c\beta_-(\mu).
$$

On the lower sheet,

$$
\beta_-(\mu)\le {1\over2},
$$

so every lower-sheet output satisfies

$$
B_{T_+^{lo}}(a,c)\le {c\over2}.
$$

## 2. The branch $(T_+^{lo},T_-)$

### Lemma

If

$$
B_5=T_+^{lo},\qquad B_1=T_-,
$$

then

$$
F<1.
$$

### Proof

Since the left branch is lower sheet,

$$
B_5\le {1-\gamma_5\over2}\le {1\over2}.
$$

On the right $T_-$ branch, let $b_1=B_1$ and put

$$
c_1=1-\gamma_1=ru.
$$

The $T_-$ equation is

$$
((u+b_1)^2-1)c_1^2+uc_1-u^2=0.
$$

Since $c_1=ru=u/R$, division by $u^2$ gives

$$
{(u+b_1)^2-1\over R^2}+{1-R\over R}=0.
$$

Hence

$$
(u+b_1)^2=1-R+R^2=S^2.
$$

All quantities are nonnegative, so

$$
B_1=b_1=S-u.
$$

The right $T_-$ branch has output no larger than its input coordinate, so

$$
B_1\le u.
$$

Therefore

$$
S-u\le u,\qquad B_1=S-u\le {S\over2}.
$$

Because $0<R<1$, one has $S<1$.  Thus

$$
B_1<{1\over2}.
$$

Consequently

$$
F=B_5+B_1<{1\over2}+{1\over2}=1.
$$

This proves the branch.

## 3. The branch $(T_+^{lo},T_+^{lo})$

### Lemma

If

$$
B_5=T_+^{lo},\qquad B_1=T_+^{lo},
$$

then

$$
F<1.
$$

### Proof

The lower-sheet estimate gives

$$
B_5\le {1-\gamma_5\over2},\qquad B_1\le {1-\gamma_1\over2}.
$$

Therefore

$$
F=B_5+B_1\le 1-{\gamma_1+\gamma_5\over2}\le1.
$$

It remains to rule out equality.  Equality would require

$$
\gamma_1=\gamma_5=0,
$$

and equality in both lower-sheet estimates.  Hence both lower-sheet parameters
must satisfy

$$
\mu_1=\mu_5={\sqrt3\over2},\qquad B_1=B_5={1\over2}.
$$

Thus the right input coordinate and the left input coordinate are both

$$
h={\sqrt3\over2}-{1\over2}={\sqrt3-1\over2}.
$$

So

$$
u=h,\qquad s=h.
$$

Since $\gamma_1=0$, the identity $\gamma_1=1-ru$ gives

$$
R=u=h.
$$

Also

$$
w=1-u-s=1-2h=2-\sqrt3.
$$

Substitute these values into the $C$-geometry formula for $\gamma_5$:

$$
\gamma_5=h-{h\over1+S_h}-{h\over1-h}(1-2h), \qquad S_h=\sqrt{1-h+h^2}.
$$

Equivalently,

$$
\gamma_5 =h\left({S_h\over1+S_h}-{1-2h\over1-h}\right).
$$

Now

$$
{1-2h\over1-h}=1-{\sqrt3\over3}.
$$

Therefore $\gamma_5>0$ is equivalent to

$$
{S_h\over1+S_h}>1-{\sqrt3\over3},
$$

which is equivalent to

$$
S_h>\sqrt3-1.
$$

This last inequality holds because

$$
S_h^2-(\sqrt3-1)^2 = \left({5\over2}-\sqrt3\right)-(4-2\sqrt3) =\sqrt3-{3\over2}>0.
$$

Thus $\gamma_5>0$, contradicting the equality requirement $\gamma_5=0$.
Therefore equality in $F\le1$ is impossible, and

$$
F<1.
$$

This proves the branch.

## 4. The branch $(T_+^{lo},T_+^{hi})$

### Lemma

If

$$
B_5=T_+^{lo},\qquad B_1=T_+^{hi},
$$

then

$$
F<1.
$$

### Proof

Set

$$
k={\sqrt{13}-1\over6}.
$$

Then

$$
3k^2+k-1=0,\qquad 0<k<{1\over2},\qquad \sqrt{1-k+k^2}=2k.
$$

#### Step 1.  The left lower sheet forces $s\le k$.

For the left branch, write

$$
a=s,\qquad c=1-\gamma_5,\qquad b=B_5,\qquad \mu=a+b,\qquad \beta={b\over c}.
$$

Because the branch is $T_+^{lo}$,

$$
\beta=\beta_-(\mu)={1-\sqrt{4\mu^2-3}\over2}.
$$

Since this is a $T_+$ branch,

$$
b\ge a.
$$

Since $c\le1$,

$$
b=c\beta\le\beta.
$$

Thus

$$
\mu=a+b\le2b\le2\beta=1-\sqrt{4\mu^2-3}.
$$

The right side is nonnegative, so squaring is valid.  We get

$$
4\mu^2-3\le1-2\mu+\mu^2,
$$

hence

$$
3\mu^2+2\mu-4\le0.
$$

The positive root of $3x^2+2x-4$ is $2k$.  Therefore

$$
\mu\le2k.
$$

Since $a=s\le\mu/2$, we obtain

$$
\boxed{s\le k.}
$$

#### Step 2.  The left bound gives a lower bound for $c_1=1-\gamma_1$.

Put

$$
c_1=1-\gamma_1=ru={u\over R}.
$$

Then

$$
u=Rc_1.
$$

Solving

$$
\gamma_5=u-\delta-{R\over1-R}w
$$

for $w$, and using $s=1-u-w$, gives

$$
s=1-c_1+{1-S\over R}+{1-R\over R}\gamma_5.
$$

Indeed, the identity

$$
{1-R\over1+S}={1-S\over R}
$$

has been used.  Since $s\le k$ and $\gamma_5\ge0$, this gives

$$
c_1\ge 1+{1-S\over R}-k.
$$

Define

$$
L(R)=1+{1-S\over R}-k.
$$

Then

$$
\boxed{c_1\ge L(R).}
$$

#### Step 3.  The right high sheet gives $c_1\le S$.

For the right branch, write

$$
a=u=Rc_1,\qquad c=c_1,\qquad b=B_1,\qquad \mu=a+b,\qquad \beta={b\over c}.
$$

Then

$$
\mu=c_1(R+\beta).
$$

On $T_+$,

$$
\mu^2=\beta^2-\beta+1.
$$

Because this is a high sheet with $\mu\le1$,

$$
{1\over2}\le\beta\le1.
$$

Because it is a $T_+$ branch,

$$
b\ge a,\qquad\text{so}\qquad \beta\ge R.
$$

The Cell 2 condition contains

$$
\Delta=\mu^4-\mu^2+ab\ge0.
$$

Substituting $c_1=\mu/(R+\beta)$ and
$\mu^2=\beta^2-\beta+1$ gives

$$
\Delta= {\beta(\beta^2-\beta+1)(R+\beta-1)(R\beta-R+\beta^2)\over(R+\beta)^2}.
$$

All factors except possibly $R+\beta-1$ are nonnegative.  The only non-obvious
one is

$$
R\beta-R+\beta^2=\beta^2-R(1-\beta) \ge\beta^2-\beta(1-\beta)=\beta(2\beta-1)\ge0,
$$

using $R\le\beta$ and $\beta\ge1/2$.  Hence $\Delta\ge0$ implies

$$
R+\beta-1\ge0.
$$

Next,

$$
S^2(R+\beta)^2-\mu^2 =(R+\beta-1)(R^3+R^2\beta-R\beta+R+1).
$$

The second factor is positive, because

$$
R^3+R^2\beta-R\beta+R+1 =1+R+R^3-R\beta(1-R) \ge1+R^2+R^3>0.
$$

Therefore

$$
S(R+\beta)\ge\mu.
$$

Since $c_1=\mu/(R+\beta)$, we get

$$
\boxed{c_1\le S.}
$$

#### Step 4.  Hence $R\ge k$.

Combining the previous two bounds gives

$$
L(R)\le S.
$$

That is,

$$
1+{1-S\over R}-k\le S.
$$

Equivalently,

$$
S(1+R)\ge1+R(1-k).
$$

Both sides are positive.  Squaring and using $S^2=1-R+R^2$ gives

$$
(1-R+R^2)(1+R)^2-(1+R(1-k))^2\ge0.
$$

Using $3k^2+k-1=0$, the left side factors as

$$
R(R-k)\left(R^2+(1+k)R+{1-2k\over k}\right).
$$

The last factor is positive for $0<R<1$.  Therefore

$$
\boxed{R\ge k.}
$$

#### Step 5.  The right high-sheet ratio satisfies $\beta\le1-k$.

For fixed $R$, define

$$
g_R(\beta)={\sqrt{\beta^2-\beta+1}\over R+\beta}.
$$

On the right $T_+^{hi}$ branch,

$$
c_1=g_R(\beta).
$$

Differentiate:

$$
g_R'(\beta)=g_R(\beta)\left({2\beta-1\over2(\beta^2-\beta+1)}-{1\over R+\beta}\right).
$$

The sign is the sign of

$$
(2\beta-1)(R+\beta)-2(\beta^2-\beta+1) =(2\beta-1)R+\beta-2.
$$

Since $0<R<1$ and $1/2\le\beta\le1$,

$$
(2\beta-1)R+\beta-2\le(2\beta-1)+\beta-2=3\beta-3\le0.
$$

Thus $g_R$ is nonincreasing on the high-sheet interval.

Set

$$
\beta_0=1-k.
$$

Then

$$
\sqrt{\beta_0^2-\beta_0+1}=2k,
$$

so

$$
g_R(\beta_0)={2k\over R+\beta_0}.
$$

We claim

$$
g_R(\beta_0)\le L(R)\qquad(k\le R\le1).
$$

Let

$$
q={1-S\over R}.
$$

For $k\le R\le1$, one has

$$
0\le q\le q_0:={\sqrt{13}-3\over2},
$$

and

$$
R={1-2q\over1-q^2},\qquad L(R)=\beta_0+q.
$$

Then

$$
L(R)-g_R(\beta_0)\ge0
$$

is equivalent to

$$
(\beta_0+q)(R+\beta_0)-2k\ge0.
$$

Substitution of $R=(1-2q)/(1-q^2)$ gives the exact factorization

$$
(\beta_0+q)(R+\beta_0)-2k = {(7-\sqrt{13})(q_0-q)\left(q^2+{\sqrt{13}+5\over3}q+{\sqrt{13}-3\over6}\right) \over6(1-q^2)}.
$$

Every factor is nonnegative on $0\le q\le q_0$, and the denominator is
positive.  Thus

$$
g_R(\beta_0)\le L(R).
$$

Since

$$
c_1=g_R(\beta)\ge L(R)\ge g_R(\beta_0),
$$

and $g_R$ is nonincreasing, it follows that

$$
\boxed{\beta\le\beta_0=1-k.}
$$

#### Step 6.  Therefore $B_1<1/2$.

The right branch is $T_+$, so

$$
\beta\ge R.
$$

Together with $\beta\le1-k$, this gives

$$
R\le1-k.
$$

Since Step 4 gave $R\ge k$, we have

$$
k\le R\le1-k.
$$

On this interval,

$$
S^2=1-R+R^2
$$

is convex and symmetric about $R=1/2$.  Hence its maximum on
$[k,1-k]$ occurs at the endpoints, where $S=2k$.  Therefore

$$
S\le2k.
$$

Now

$$
B_1=b=\beta c_1\le(1-k)S\le2k(1-k).
$$

Finally

$$
{1\over2}-2k(1-k)={29-8\sqrt{13}\over18}>0,
$$

because

$$
29^2-13\cdot8^2=9>0.
$$

Hence

$$
\boxed{B_1<{1\over2}.}
$$

The left lower sheet gives

$$
B_5\le {1-\gamma_5\over2}\le{1\over2}.
$$

Therefore

$$
F=B_5+B_1<1.
$$

This proves the branch $(T_+^{lo},T_+^{hi})$.

## 5. Completion of the lower-sheet obligations

The three lower-sheet branches formerly left open were

$$
(T_+^{lo},T_-),\qquad (T_+^{lo},T_+^{hi}),\qquad (T_+^{lo},T_+^{lo}).
$$

Sections 2, 3, and 4 prove $F<1$ in all three cases.  Thus no lower-sheet
$T_+$ branch remains open in the CE1/CE2 all-Vd0 boundary-loss reduction.
