# Detailed Gap-Closure Lemmas for the 407X Completion

Status: Proven

This file supplies the expanded derivations used by

- [4078_left_L_family_completion.md](4078_left_L_family_completion.md),
- [4079_first_Full_and_lower_sheet_branches.md](4079_first_Full_and_lower_sheet_branches.md), and
- [407a_left_Thigh_branch_completion.md](407a_left_Thigh_branch_completion.md).

It is written to make [407b_final_assembly.md](407b_final_assembly.md) independent of abbreviated phrases such as “direct check”.  The common notation is that of [4073_boundary_loss_framework.md](4073_boundary_loss_framework.md).  In the CE2 overlap part put

$$
r=1-λ,
\quad
u=γ_5,
\quad
y=Y/λ,
\quad
ρ=sqrt(r^2-r+1).
$$

The Low function is

$$
ℓ(η)=((1-η)(1-sqrt(4(1-η)^2-3)))/2,
\quad
0≤η≤η_0:=1-sqrt(3)/2.
$$

## 1. Left-Low details

### Lemma 1.1: Low separation

If $0≤η≤η_0$, $z=ℓ(η)$, and the Low candidate is realized for input $a=1-β$, then

$$
β≥z+η.
$$

Proof.  The Low equation is

$$
z^2-(1-η)z+(1-η)^2(1-(1-η)^2)=0.
$$

Equivalently $P(η,z)=0$, where

$$
P(x,z)=x^4-4x^3+5x^2-(2+z)x+z-z^2.
$$

The Low domain contains $a+z≤1$ and

$$
(a+z)^4-(a+z)^2+az≤0.
$$

With $a=1-β$ and $h=β-z$, the first condition gives $h≥0$, and the second becomes $P(h,z)≤0$.  On $0≤x≤η_0<1/7$,

$$
∂P/∂x=4x^3-12x^2+10x-(2+z)<0,
$$

because $4x^3+10x<4/343+10/7<2$.  Thus $P(·,z)$ is strictly decreasing.  If $h<η$, then $P(h,z)>P(η,z)=0$, contradiction.  Hence $h≥η$, proving $β≥z+η$.

### Lemma 1.2: Non-overlap Low comparison

For $0<A<1/2$, set $r_A=sqrt(1-A+A^2)$ and $g=r_A(1-r_A)$.  Then

$$
2g+5g^2<A.
$$

Proof.  Write $r_A=1-y$.  Then $0<y<1-sqrt(3)/2<1/7$, and

$$
A=(1-sqrt(1-8y+4y^2))/2.
$$

The target is equivalent to

$$
sqrt(1-8y+4y^2)<1-4y-6y^2+20y^3-10y^4.
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

Let $0<A≤λ<1$, $ρ=sqrt(1-λ+λ^2)$, and

$$
G_1=(A+ρ-1-λ^2)/(1-λ),
\quad
G_2=(λ-A)/λ,
\quad
G=min(G_1,G_2).
$$

If $G≥0$, then $ℓ(G)<A$.

Proof.  The crossing $G_1=G_2$ occurs at

$$
A_0=λ(2-λ+λ^2-ρ),
$$

and then

$$
G_1=G_2=g=ρ(1-ρ),
\quad
A_0=λ(1-g).
$$

Let $c=1-g$ and $b_0=A_0=λc$.  The Low polynomial at radial loss $g$ is

$$
P_c(b)=b^2-cb+c^2(1-c^2).
$$

Substitution and $ρ^2=1-λ+λ^2$ give

$$
P_c(b_0)=-(ρ-1)^2(ρ^2+1)(ρ^2-ρ+1)^2<0.
$$

Since $P_c(0)>0$, $b_0$ is to the right of the smaller Low root, so $ℓ(g)<A_0$.  If $G=G_2$, then $A≥A_0$ and $G≤g$, so $ℓ(G)<A$.  If $G=G_1$, then $A≤A_0$.  The function $F(A)=A-ℓ(G_1(A))$ is concave on the relevant interval because $G_1$ is affine and $ℓ$ is convex on $[0,1/8]$, while $g<1/8$.  At the endpoint $G_1=0$, $F(A)=A>0$, and at $A=A_0$, $F(A_0)>0$.  Hence $F>0$ throughout.

### Lemma 1.4: Center transfer

Let $0<u≤η_0$, $z=ℓ(u)$, and $λ≥z/(1-u)$.  Define

$$
S_λ(v)=u+λ/(1+sqrt(1-λ+λ^2))+λv/(1-λ).
$$

If either $v≥η_0$, or $0≤v≤η_0$ and $S_λ(v)≤ℓ(v)$, then $z<S_λ(v)$.

Proof.  Put $c=1-u$ and $β=z/c=(1-sqrt(4c^2-3))/2$.  Then $c^2=1-β+β^2$, and $λ≥β$.  Both $δ(λ)=λ/(1+sqrt(1-λ+λ^2))$ and $k(λ)=λ/(1-λ)$ are increasing, so $S_λ(v)≥S_β(v)$.

At $λ=β$, $sqrt(1-β+β^2)=c$, hence

$$
S_β(v)=u+β/(1+c)+βv/(1-β).
$$

If $S_β(0)≥z$, the conclusion is immediate, except possibly equality at $v=0$, which is incompatible with $S_λ(0)≤ℓ(0)=0$.  Otherwise define $v_0$ by $S_β(v_0)=z$.  A simplification gives

$$
v_0=((1-β)(β^2+c-1))/(1+c).
$$

Then $v_0>0$ and

$$
u-v_0=((1-β)(1+β-β^2-c))/(1+c)>0,
$$

because $(1+β-β^2)^2-c^2=β(β-1)(β^2-β-3)>0$ for $0<β≤1/2$.  Also $v_0<(1-β)β^2≤1/8$.  The function $H(v)=S_β(v)-ℓ(v)$ is concave on $[0,v_0]$, with $H(0)>0$ and $H(v_0)=z-ℓ(v_0)>0$.  Hence $H>0$ on this interval.  If $S_λ(v)≤z$, then $v≤v_0$ and $S_λ(v)≥S_β(v)>ℓ(v)$, contradiction to the second alternative.  If $v≥η_0$, then $v>u>v_0$, so $S_λ(v)≥S_β(v)>z$.

## 2. Left-lower-sheet details

### Lemma 2.1: Midpoint exit bound

In the normalized $407X$ branch, $γ_5<1/2$.

Proof.  The $C$-triangle contains exactly $M_0$ among the six radial midpoints.  Hence $M_5$ is not in $T_C$.  Since $T_C∩r_5$ is closed and has endpoint $γ_5$, and $M_5$ is at coordinate $1/2$ on $r_5$, one must have $γ_5<1/2$.

### Lemma 2.2: Lower-sheet estimates

Assume $B_5=T_+^{lo}$ in the hard CE2 overlap region.  Then:

1. $0<r≤1/2$ and $r≥r_0=(sqrt(3)-1)/2$;
2. $y<1/4$;
3. if $0≤y<η_0$, then $S>ℓ(y)$;
4. if $y≥η_0$, then $S>7/16$ and $A_C>7/16$.

Proof.  The lower sheet has $A_5=r(1-u)$ and $C_5=1-u$.  Since $B_5≥A_5$ and $B_5≤C_5/2$, Lemma 2.1 gives $r≤1/2$.  Write $B_5=(1-u)β$ with $r≤β≤1/2$.  The $T_+$ equation gives

$$
1-u=sqrt(β^2-β+1)/(r+β).
$$

Because $1-u≤1$, existence of such a $β≤1/2$ forces $r+1/2≥sqrt(3)/2$, hence $r≥r_0$.

Now

$$
S=u+(1-r)/(1+ρ)+(1-r)y/r.
$$

Here $(1-r)/(1+ρ)≥2-sqrt(3)$ and $(1-r)/r≥1$.  Since $S<1/2$, one gets $y<sqrt(3)-3/2<1/4$.

For $0≤x≤η_0$, set

$$
D(x)=u+(1-r)/(1+ρ)+(1-r)x/r-ℓ(x).
$$

The Low function is convex on $[0,η_0]$, so $D$ is concave.  We have $D(0)>0$.  At $x=η_0$, the three-range estimate in $r∈[r_0,1/2]$ gives

$$
u+(1-r)/(1+ρ)+(1-r)η_0/r>7/16>sqrt(3)/4=ℓ(η_0).
$$

If the feasible endpoint is instead $S=1/2`, then $D=1/2-ℓ(x)>0$.  Thus $D>0$ through the feasible interval, proving $S>ℓ(y)$ when $y<η_0$.

For $y≥η_0`, the same endpoint estimate gives $S>7/16$.  Finally, $S<1/2` gives

$$
y<(1/2-u-(1-r)/(1+ρ))/((1-r)/r).
$$

Combining this with $1-u≤ρ/(2r)$ gives $A_C=(1-r)(1-y)>7/16$.  Explicitly, for $r≤7/16$,

$$
A_C>1-3r/2+r(1-r)/(1+ρ)≥11/32+9(sqrt(3)-1)/64>7/16,
$$

and for $7/16≤r≤1/2$,

$$
A_C>1-r/2+r(1-r)/(1+ρ)-ρ/2>(447-16sqrt(193))/512>7/16.
$$

## 3. Left-high-sheet details

### Lemma 3.1: Left-high Cell-2 condition

Under a realized left branch $B_5=T_+^{hi}$,

$$
r≥(1-β)(r+β)^2.
$$

Proof.  The left input is $a=rc$, output $b=βc$, and $a+b=c(r+β)=m$, with $m^2=β^2-β+1$.  The realized branch is in Cell 2, so

$$
Δ=(a+b)^4-(a+b)^2+ab≥0.
$$

Substitution gives $Δ=m^4-m^2+rβc^2$.  Since $c^2=m^2/(r+β)^2$ and $m^2-1=-β(1-β)$,

$$
Δ=m^2(-β(1-β)+rβ/(r+β)^2).
$$

Because $m^2β>0`, this is equivalent to $r≥(1-β)(r+β)^2$.

### Lemma 3.2: High-left envelope

Let

$$
y_*=(r/(1-r))(m/(r+β)-1/2-(1-r)/(1+ρ)),
\quad
b=βm/(r+β).
$$

Under the left-high hypotheses,

$$
y_*<1/8,
\qquad
3y_*≤1-b.
$$

Proof.  The estimate $y_*<1/8$ follows in three ranges.  Since $m/(r+β)$ is decreasing in $β$, use $β_0=max(r,1/2,(1-r^2)/(1+2r))$.

If $0<r≤(sqrt(3)-1)/2$, then $m/(r+β)≤1$ and $(1-r)/(1+ρ)>(1-r)/2`, giving $y_*<r^2/(2(1-r))<1/8$.

If $(sqrt(3)-1)/2≤r≤1/2`, then $m/(r+β)≤sqrt(3)/(1+2r)$ and $(1-r)/(1+ρ)≥2-sqrt(3)+(1/2-r)/2`.  The inequality $y_*<1/8` reduces to

$$
8r^3-10r^2+(8sqrt(3)-9)r-1<0,
$$

whose derivative is positive on the interval and whose value at $1/2$ is $4sqrt(3)-7<0$.

If $1/2≤r<1`, then $m/(r+β)≤ρ/(2r)`, giving $y_*≤(ρ+1-3r)/(2(ρ+1))<1/8$ because $ρ+1<4r$.

For the second estimate define $E_r(β)=1-b-3y_*$.  Direct differentiation gives

$$
∂E_r/∂β=N_r(β)/(2(β+r)^2(1-r)sqrt(β^2-β+1)),
$$

where

$$
N_r(β)=2β^3r-2β^3+4β^2r^2-5β^2r+β^2-9βr^2+5r^2+4r.
$$

Moreover

$$
∂N_r/∂β=-6β^2(1-r)+2β(1-r)(1-4r)-9r^2<0
$$

on the allowed interval $β≥1/2`.  Hence $E_r$ has no interior minimum.  At $β=1`,

$$
E_r(1)=r(6r-ρ+5)/(2(1+r)(1+ρ))>0.
$$

At the lower endpoint: if $0<r≤(sqrt(3)-1)/2`, direct substitution gives a positive numerator bounded below by $r(7-10r-16r^2)>0$; if $(sqrt(3)-1)/2≤r≤1/2`, then $β_0=1/2`, so $b≤1/2` and $y_*<1/8`, giving $E_r>1/8`; if $1/2≤r<1`, then $β_0=r` and

$$
E_r(r)=(10r-r^2-2ρ-2)/(2(1+ρ))>0.
$$

Thus $3y_*≤1-b$.

### Lemma 3.3: $S>3y$ and $A_C>3y`

Under the left-high hypotheses in the hard region,

$$
S>3y,
\qquad
A_C>3y.
$$

Proof.  Since $y<y_*<1/10`, $3y<3/10`.  If $(1-r)/r≥3`, then $S>3y`.  Otherwise $S-3y` decreases with $y`, and at $y=y_*` one has $S=1/2`, so $S-3y>1/2-3/10>0`.

For $A_C`, first show $1-r>3/8`.  If $r≤1/2` this is clear.  If $r>1/2`, then $y_*>0` implies

$$
ρ/(2r)>1/2+(1-r)/(1+ρ),
$$

which simplifies to $3r<1+ρ`.  Squaring gives $r<5/8`.  Thus $1-r>3/8`.  Since $A_C=(1-r)(1-y)` and $y<1/10`,

$$
A_C>(3/8)(9/10)=27/80>3/10>3y.
$$

### Lemma 3.4: Detailed $T_-$ bounds for the $q$ case

In the branch $B_1=T_-$ and $A_1=q`, set $C=1-y`, $q=tC`, and $B_1=b_1`. Then

$$
B_1≤κ:=(sqrt(13)-1)/6,
$$

and

$$
q≤τ<93/200,
$$

where $τ∈(0,1/2)` is the unique root of

$$
x^4-3x^3+3x^2-3x+1=0.
$$

Proof.  The $T_-$ equation gives

$$
q+b_1=μ=sqrt(t^2-t+1).
$$

Since $b_1≤q`, $b_1≤μ/2` and $μ≤2q≤2t`.  Thus $3t^2+t-1≥0`, so $t≥κ`.  Also $y<1/10` and $q<1/2` give $t<5/9`.  On $[κ,5/9]`, $μ/2≤κ`, proving $B_1≤κ`.

For the $q` bound, the realized Cell-2 condition gives

$$
(q+b_1)^4-(q+b_1)^2+qb_1≥0.
$$

Substituting $q+b_1=μ` and $q=tC` yields

$$
-tC^2+μC-(1-t)μ^2≥0.
$$

The case $t≥1/2` would force $C≤μ<9/10`, contradicting $C>9/10`.  Hence $t<1/2`.  Then the quadratic gives $C≤μ(1-t)/t`, and therefore

$$
q=tC≤min(t, μ(1-t)).
$$

The maximum of the right side occurs at $t=μ(1-t)`, which gives the quartic above.  Its unique root in $(0,1/2)` is $τ`, and direct evaluation gives $τ<93/200`.

## 4. Certificate linkage

The certificate `407b_T_hi_Tminus_qright_threshold_certificate.py` uses Lemma 3.1 as a domain condition and proves

$$
S_0<93/200 \quad⇒\quad B_5<5657/10000<(7-sqrt(13))/6.
$$

The certificate `407c_T_hi_Tlo_left_threshold_certificate.py` uses Lemma 3.1 and the lower-sheet condition $3p^2+p-1≥0` and proves

$$
S_0<sqrt(p^2-p+1)-p \quad⇒\quad B_5<1-p.
$$

Both scripts use rational interval arithmetic with one-sided integer square-root bounds and have recorded runs with zero unresolved boxes.
