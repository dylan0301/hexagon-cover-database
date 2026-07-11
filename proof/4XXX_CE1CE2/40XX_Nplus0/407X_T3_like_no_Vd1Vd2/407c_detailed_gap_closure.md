# Detailed Gap-Closure Lemmas for the 407X Completion

Status: Proven

This file supplies the expanded derivations used by

- [4078_left_L_family_completion.md](4078_left_L_family_completion.md),
- [4079_first_Full_and_lower_sheet_branches.md](4079_first_Full_and_lower_sheet_branches.md), and
- [407a_left_Thigh_branch_completion.md](407a_left_Thigh_branch_completion.md).

It is written to make [407b_final_assembly.md](407b_final_assembly.md) independent of abbreviated phrases such as “direct check”.  The common notation is that of [4073_boundary_loss_framework.md](4073_boundary_loss_framework.md).  In the CE2 overlap part put

$$
r=1-\lambda,
\quad
u=\gamma_5,
\quad
y=Y/\lambda,
\quad
\rho=\sqrt{r^2-r+1}.
$$

The Low function is

$$
\ell(\eta)=\frac{(1-\eta)\left(1-\sqrt{4(1-\eta)^2-3}\right)}{2},
\quad
0\le\eta\le\eta_0:=1-\sqrt{3}/2.
$$

## 1. Left-Low details

### Lemma 1.1: Low separation

If $0\le\eta\le\eta_0$, $z=\ell(\eta)$, and the Low candidate is realized for input $a=1-\beta$, then

$$
\beta\ge z+\eta.
$$

Proof.  The Low equation is

$$
z^2-(1-\eta)z+(1-\eta)^2(1-(1-\eta)^2)=0.
$$

Equivalently $P(\eta,z)=0$, where

$$
P(x,z)=x^4-4x^3+5x^2-(2+z)x+z-z^2.
$$

The Low domain contains $a+z\le1$ and

$$
(a+z)^4-(a+z)^2+az\le0.
$$

With $a=1-\beta$ and $h=\beta-z$, the first condition gives $h\ge0$, and the second becomes $P(h,z)\le0$.  On $0\le x\le\eta_0<1/7$,

$$
\partial P/\partial x=4x^3-12x^2+10x-(2+z)<0,
$$

because $4x^3+10x<4/343+10/7<2$.  Thus $P(\mathbin{\cdot},z)$ is strictly decreasing.  If $h<\eta$, then $P(h,z)>P(\eta,z)=0$, contradiction.  Hence $h\ge\eta$, proving $\beta\ge z+\eta$.

### Lemma 1.2: Non-overlap Low comparison

For $0<A<1/2$, set $r_A=\sqrt{1-A+A^2}$ and $g=r_A(1-r_A)$.  Then

$$
2g+5g^2<A.
$$

Proof.  Write $r_A=1-y$.  Then $0<y<1-\sqrt{3}/2<1/7$, and

$$
A=(1-\sqrt{1-8y+4y^2})/2.
$$

The target is equivalent to

$$
\sqrt{1-8y+4y^2}<1-4y-6y^2+20y^3-10y^4.
$$

The right side is positive because

$$
1-4y-6y^2-10y^4>1-4/7-6/49-10/2401>0.
$$

After squaring, the difference equals

$$
4y^3 Q(y),
$$

where

$$
Q(y)=25y^5-100y^4+130y^3-40y^2-36y+22.
$$

On $0<y<1/7$,

$$
Q(y)>22-36/7-40/49-100/2401>0.
$$

Thus $2g+5g^2<A$.

### Lemma 1.3: CE2 middle-overlap comparison

Let $0<A\le\lambda<1$, $\rho=\sqrt{1-\lambda+\lambda^2}$, and

$$
G_1=(A+\rho-1-\lambda^2)/(1-\lambda),
\quad
G_2=(\lambda-A)/\lambda,
\quad
G=\min\{G_1,G_2\}.
$$

If $G\ge0$, then $\ell(G)<A$.

Proof.  The crossing $G_1=G_2$ occurs at

$$
A_0=\lambda(2-\lambda+\lambda^2-\rho),
$$

and then

$$
G_1=G_2=g=\rho(1-\rho),
\quad
A_0=\lambda(1-g).
$$

Let $c=1-g$ and $b_0=A_0=\lambda c$.  The Low polynomial at radial loss $g$ is

$$
P_c(b)=b^2-cb+c^2(1-c^2).
$$

Substitution and $\rho^2=1-\lambda+\lambda^2$ give

$$
P_c(b_0)=-(\rho-1)^2(\rho^2+1)(\rho^2-\rho+1)^2<0.
$$

Since $P_c(0)>0$, $b_0$ is to the right of the smaller Low root, so $\ell(g)<A_0$.  If $G=G_2$, then $A\ge A_0$ and $G\le g$, so $\ell(G)<A$.  If $G=G_1$, then $A\le A_0$.  The function $F(A)=A-\ell(G_1(A))$ is concave on the relevant interval because $G_1$ is affine and $\ell$ is convex on $[0,1/8]$, while $g<1/8$.  At the endpoint $G_1=0$, $F(A)=A>0$, and at $A=A_0$, $F(A_0)>0$.  Hence $F>0$ throughout.

### Lemma 1.4: Center transfer

Let $0<u\le\eta_0$, $z=\ell(u)$, and $\lambda\ge z/(1-u)$.  Define

$$
S_\lambda(v)=u+\lambda/(1+\sqrt{1-\lambda+\lambda^2})+\lambda v/(1-\lambda).
$$

If either $v\ge\eta_0$, or $0\le v\le\eta_0$ and $S_\lambda(v)\le\ell(v)$, then $z<S_\lambda(v)$.

Proof.  Put $c=1-u$ and $\beta=z/c=(1-\sqrt{4c^2-3})/2$.  Then $c^2=1-\beta+\beta^2$, and $\lambda\ge\beta$.  Both $\delta(\lambda)=\lambda/(1+\sqrt{1-\lambda+\lambda^2})$ and $k(\lambda)=\lambda/(1-\lambda)$ are increasing, so $S_\lambda(v)\ge S_\beta(v)$.

At $\lambda=\beta$, $\sqrt{1-\beta+\beta^2}=c$, hence

$$
S_\beta(v)=u+\beta/(1+c)+\beta v/(1-\beta).
$$

If $S_\beta(0)\ge z$, the conclusion is immediate, except possibly equality at $v=0$, which is incompatible with $S_\lambda(0)\le\ell(0)=0$.  Otherwise define $v_0$ by $S_\beta(v_0)=z$.  A simplification gives

$$
v_0=((1-\beta)(\beta^2+c-1))/(1+c).
$$

Then $v_0>0$ and

$$
u-v_0=((1-\beta)(1+\beta-\beta^2-c))/(1+c)>0,
$$

because $(1+\beta-\beta^2)^2-c^2=\beta(\beta-1)(\beta^2-\beta-3)>0$ for $0<\beta\le1/2$.  Also $v_0<(1-\beta)\beta^2\le1/8$.  The function $H(v)=S_\beta(v)-\ell(v)$ is concave on $[0,v_0]$, with $H(0)>0$ and $H(v_0)=z-\ell(v_0)>0$.  Hence $H>0$ on this interval.  If $S_\lambda(v)\le z$, then $v\le v_0$ and $S_\lambda(v)\ge S_\beta(v)>\ell(v)$, contradiction to the second alternative.  If $v\ge\eta_0$, then $v>u>v_0$, so $S_\lambda(v)\ge S_\beta(v)>z$.

## 2. Left-lower-sheet details

### Lemma 2.1: Midpoint exit bound

In the normalized $407X$ branch, $\gamma_5<1/2$.

Proof.  The $C$-triangle contains exactly $M_0$ among the six radial midpoints.  Hence $M_5$ is not in $T_C$.  Since $T_C\cap r_5$ is closed and has endpoint $\gamma_5$, and $M_5$ is at coordinate $1/2$ on $r_5$, one must have $\gamma_5<1/2$.

### Lemma 2.2: Lower-sheet estimates

Assume $B_5=T_+^{lo}$ in the hard CE2 overlap region.  Then:

1. $0<r\le1/2$ and $r\ge r_0=(\sqrt{3}-1)/2$;
2. $y<1/4$;
3. if $0\le y<\eta_0$, then $S>\ell(y)$;
4. if $y\ge\eta_0$, then $S>7/16$ and $A_C>7/16$.

Proof.  The lower sheet has $A_5=r(1-u)$ and $C_5=1-u$.  Since $B_5\ge A_5$ and $B_5\le C_5/2$, Lemma 2.1 gives $r\le1/2$.  Write $B_5=(1-u)\beta$ with $r\le\beta\le1/2$.  The $T_+$ equation gives

$$
1-u=\sqrt{\beta^2-\beta+1}/(r+\beta).
$$

Because $1-u\le1$, existence of such a $\beta\le1/2$ forces $r+1/2\ge \sqrt{3}/2$, hence $r\ge r_0$.

Now

$$
S=u+(1-r)/(1+\rho)+(1-r)y/r.
$$

Here $(1-r)/(1+\rho)\ge2-\sqrt{3}$ and $(1-r)/r\ge1$.  Since $S<1/2$, one gets $y<\sqrt{3}-3/2<1/4$.

For $0\le x\le\eta_0$, set

$$
D(x)=u+(1-r)/(1+\rho)+(1-r)x/r-\ell(x).
$$

The Low function is convex on $[0,\eta_0]$, so $D$ is concave.  We have $D(0)>0$.  At $x=\eta_0$, the three-range estimate in $r\in[r_0,1/2]$ gives

$$
u+(1-r)/(1+\rho)+(1-r)\eta_0/r>7/16>\sqrt{3}/4=\ell(\eta_0).
$$

If the feasible endpoint is instead $S=1/2$, then $D=1/2-\ell(x)>0$.  Thus $D>0$ through the feasible interval, proving $S>\ell(y)$ when $y<\eta_0$.

For $y\ge\eta_0$, the same endpoint estimate gives $S>7/16$.  Finally, $S<1/2$ gives

$$
y<(1/2-u-(1-r)/(1+\rho))/((1-r)/r).
$$

Combining this with $1-u\le\rho/(2r)$ gives $A_C=(1-r)(1-y)>7/16$.  Explicitly, for $r\le7/16$,

$$
A_C>1-3r/2+r(1-r)/(1+\rho)\ge11/32+9(\sqrt{3}-1)/64>7/16,
$$

and for $7/16\le r\le1/2$,

$$
A_C>1-r/2+r(1-r)/(1+\rho)-\rho/2>(447-16\sqrt{193})/512>7/16.
$$

## 3. Left-high-sheet details

### Lemma 3.1: Left-high Cell-2 condition

Under a realized left branch $B_5=T_+^{hi}$,

$$
r\ge(1-\beta)(r+\beta)^2.
$$

Proof.  The left input is $a=rc$, output $b=\beta c$, and $a+b=c(r+\beta)=m$, with $m^2=\beta^2-\beta+1$.  The realized branch is in Cell 2, so

$$
\Delta=(a+b)^4-(a+b)^2+ab\ge0.
$$

Substitution gives $\Delta=m^4-m^2+r\beta c^2$.  Since $c^2=m^2/(r+\beta)^2$ and $m^2-1=-\beta(1-\beta)$,

$$
\Delta=m^2(-\beta(1-\beta)+r\beta/(r+\beta)^2).
$$

Because $m^2\beta>0$, this is equivalent to $r\ge(1-\beta)(r+\beta)^2$.

### Lemma 3.2: High-left envelope

Let

$$
y_*=(r/(1-r))(m/(r+\beta)-1/2-(1-r)/(1+\rho)),
\quad
b=\beta m/(r+\beta).
$$

Under the left-high hypotheses,

$$
y_*<1/8,
\qquad
3y_*\le1-b.
$$

Proof.  The estimate $y_*<1/8$ follows in three ranges.  Since $m/(r+\beta)$ is decreasing in $\beta$, use

$$
\beta_0=\max\left\{r,\frac12,\frac{1-r^2}{1+2r}\right\}.
$$

If $0<r\le(\sqrt{3}-1)/2$, then $m/(r+\beta)\le1$ and $(1-r)/(1+\rho)>(1-r)/2$, giving $y_*<r^2/(2(1-r))<1/8$.

If $(\sqrt{3}-1)/2\le r\le1/2$, then $m/(r+\beta)\le \sqrt{3}/(1+2r)$ and $(1-r)/(1+\rho)\ge2-\sqrt{3}+(1/2-r)/2$.  The inequality $y_*<1/8$ reduces to

$$
8r^3-10r^2+(8\sqrt{3}-9)r-1<0,
$$

whose derivative is positive on the interval and whose value at $1/2$ is $4\sqrt{3}-7<0$.

If $1/2\le r<1$, then $m/(r+\beta)\le\rho/(2r)$, giving $y_*\le(\rho+1-3r)/(2(\rho+1))<1/8$ because $\rho+1<4r$.

For the second estimate define $E_r(\beta)=1-b-3y_*$.  Direct differentiation gives

$$
\partial E_r/\partial\beta=N_r(\beta)/(2(\beta+r)^2(1-r)\sqrt{\beta^2-\beta+1}),
$$

where

$$
N_r(\beta)=2\beta^3r-2\beta^3+4\beta^2r^2-5\beta^2r+\beta^2-9\beta r^2+5r^2+4r.
$$

Moreover

$$
\partial N_r/\partial\beta=-6\beta^2(1-r)+2\beta(1-r)(1-4r)-9r^2<0
$$

on the allowed interval $\beta\ge1/2$.  Hence $E_r$ has no interior minimum.  At $\beta=1$,

$$
E_r(1)=r(6r-\rho+5)/(2(1+r)(1+\rho))>0.
$$

At the lower endpoint: if $0<r\le(\sqrt{3}-1)/2$, direct substitution gives a positive numerator bounded below by $r(7-10r-16r^2)>0$; if $(\sqrt{3}-1)/2\le r\le1/2$, then $\beta_0=1/2$, so $b\le1/2$ and $y_*<1/8$, giving $E_r>1/8$; if $1/2\le r<1$, then $\beta_0=r$ and

$$
E_r(r)=(10r-r^2-2\rho-2)/(2(1+\rho))>0.
$$

Thus $3y_*\le1-b$.

### Lemma 3.3: $S>3y$ and $A_C>3y$

Under the left-high hypotheses in the hard region,

$$
S>3y,
\qquad
A_C>3y.
$$

Proof.  Since $y<y_*<1/10$, $3y<3/10$.  If $(1-r)/r\ge3$, then $S>3y$.  Otherwise $S-3y$ decreases with $y$, and at $y=y_*$ one has $S=1/2$, so $S-3y>1/2-3/10>0$.

For $A_C$, first show $1-r>3/8$.  If $r\le1/2$ this is clear.  If $r>1/2$, then $y_*>0$ implies

$$
\rho/(2r)>1/2+(1-r)/(1+\rho),
$$

which simplifies to $3r<1+\rho$.  Squaring gives $r<5/8$.  Thus $1-r>3/8$.  Since $A_C=(1-r)(1-y)$ and $y<1/10$,

$$
A_C>(3/8)(9/10)=27/80>3/10>3y.
$$

### Lemma 3.4: Detailed $T_-$ bounds for the $q$ case

In the branch $B_1=T_-$ and $A_1=q$, set $C=1-y$, $q=tC$, and $B_1=b_1$. Then

$$
B_1\le\kappa:=(\sqrt{13}-1)/6,
$$

and

$$
q\le\tau<93/200,
$$

where $\tau\in(0,1/2)$ is the unique root of

$$
x^4-3x^3+3x^2-3x+1=0.
$$

Proof.  The $T_-$ equation gives

$$
q+b_1=\mu=\sqrt{t^2-t+1}.
$$

Since $b_1\le q$, $b_1\le\mu/2$ and $\mu\le2q\le2t$.  Thus $3t^2+t-1\ge0$, so $t\ge\kappa$.  Also $y<1/10$ and $q<1/2$ give $t<5/9$.  On $[\kappa,5/9]$, $\mu/2\le\kappa$, proving $B_1\le\kappa$.

For the $q$ bound, the realized Cell-2 condition gives

$$
(q+b_1)^4-(q+b_1)^2+qb_1\ge0.
$$

Substituting $q+b_1=\mu$ and $q=tC$ yields

$$
-tC^2+\mu C-(1-t)\mu^2\ge0.
$$

The case $t\ge1/2$ would force $C\le\mu<9/10$, contradicting $C>9/10$.  Hence $t<1/2$.  Then the quadratic gives $C\le\mu(1-t)/t$, and therefore

$$
q=tC\le \min\{t,\mu(1-t)\}.
$$

The maximum of the right side occurs at $t=\mu(1-t)$, which gives the quartic above.  Its unique root in $(0,1/2)$ is $\tau$, and direct evaluation gives $\tau<93/200$.

## 4. Certificate linkage

The certificate `407b_T_hi_Tminus_qright_threshold_certificate.py` uses Lemma 3.1 as a domain condition and proves

$$
S_0<93/200 \quad\Longrightarrow\quad B_5<5657/10000<(7-\sqrt{13})/6.
$$

The certificate `407c_T_hi_Tlo_left_threshold_certificate.py` uses Lemma 3.1 and the lower-sheet condition $3p^2+p-1\ge0$ and proves

$$
S_0<\sqrt{p^2-p+1}-p \quad\Longrightarrow\quad B_5<1-p.
$$

Both scripts use rational interval arithmetic with one-sided integer square-root bounds and have recorded runs with zero unresolved boxes.
