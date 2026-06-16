# Endpoint Taylor Remainder Proof

Status: Proven

This file proves the two reduced Pattern A inequalities on the endpoint range

$$
0<r\le \frac1{200}.
$$

It replaces interval arithmetic near the boundary, where active branch inequalities such as $Q_A\ge0$ become nearly sharp.

## 1. Reduced functions

Set $q=sr$.  The reduced functions are

$$
F_I(sr,r)=\rho_2(r,sr)+sr-\tau(sr,r),
$$

and

$$
F_{II}(sr,r)=r-\sigma(r)+\rho_2(\sigma(r),sr)-\tau(sr,r).
$$

For $0<r\le1/200$, the switch satisfies

$$
\frac23r<\sigma(r)<\frac{167}{250}r.
$$

Indeed,

$$
\Phi\left(r,\frac23r\right)=\frac{r^2(r^2-12r-9)}{81}<0,
$$

and

$$
\Phi\left(r,\frac{167}{250}r\right)= \frac{r(47458321r^3-571787000r^2-456562500r+15625000)}{3906250000}>0
$$

for $0<r\le1/200$.  Since $\Phi(r,B)$ is strictly increasing in $B$, the bound follows.

Thus it is enough to prove $F_I>0$ on

$$
\frac23\le s\le1, \qquad 0<r\le\frac1{200},
$$

and $F_{II}>0$ on

$$
\frac12\le s\le\frac{167}{250}, \qquad 0<r\le\frac1{200}.
$$

## 2. Taylor expansion of $\tau$

Substituting the fifth-order Taylor branches for $P_3$ and $P_5$ into

$$
\tau(q,r)=\frac{D-N_0}{\Delta v-\Delta u}
$$

gives

$$
\begin{aligned} \tau(sr,r)=&\left(2s-\frac12\right)r -\frac{32s^2-8s+5}{8}r^2\\ &+\frac{712s^3-888s^2+440s-69}{16}r^3\\ &-\frac{51072s^4-80288s^3+53424s^2-17392s+2397}{128}r^4\\ &+\frac{1575936s^5-3305472s^4+2955856s^3-1378608s^2+333104s-33375}{256}r^5 +O(r^6). \end{aligned}
$$

The coefficients are obtained by substituting Taylor ansatzes for the selected $A$- and $B$-branch roots into the exact branch equations $F_A=C_2=0$ and $F_B=C_5=0$ and solving coefficient-by-coefficient.

## 3. Region I Taylor polynomial

Write

$$
F_I(sr,r)=P_I^{(5)}(s,r)+E_I(s,r),
$$

where

$$
P_I^{(5)}(s,r)=\sum_{k=1}^5 A_k(s)r^k.
$$

The coefficients are

$$
A_1(s)=\frac{2s-1}{2},
$$

$$
A_2(s)=-\frac{24s^2-88s+35}{8},
$$

$$
A_3(s)=-\frac{200s^3+536s^2-872s+331}{16},
$$

$$
A_4(s)=\frac{29824s^4+608s^3-61776s^2+55312s-14755}{128},
$$

and

$$
A_5(s)=-\frac{1338880s^5-2162688s^4+755280s^3+736976s^2-682192s+161185}{256}.
$$

On $2/3\le s\le1$,

$$
A_1(s)\ge\frac16, \qquad A_2(s)>0, \qquad A_4(s)>0,
$$

and

$$
|A_3(s)|\le13, \qquad |A_5(s)|\le576.
$$

Therefore

$$
P_I^{(5)}(s,r)\ge r\left(\frac16-13r^2-576r^4\right)>0.1663r
$$

for $0<r\le1/200$.

## 4. Region II Taylor polynomial

Write

$$
F_{II}(sr,r)=P_{II}^{(5)}(s,r)+E_{II}(s,r),
$$

where

$$
P_{II}^{(5)}(s,r)=\sum_{k=1}^5 B_k(s)r^k.
$$

The coefficients are

$$
B_1(s)=\frac16,
$$

$$
B_2(s)=-\frac{648s^2-1512s+361}{216},
$$

$$
B_3(s)=-\frac{48600s^3+14904s^2-36504s+13793}{3888},
$$

$$
B_4(s)=\frac{65225088s^4-57643488s^3+3941136s^2+10555056s-2777345}{279936},
$$

and

$$
B_5(s)=-\frac{26353175040s^5-50065993728s^4+38811528432s^3-14526968976s^2+2402830224s-99661885}{5038848}.
$$

On $1/2\le s\le167/250$,

$$
B_1(s)=\frac16, \qquad B_2(s)>0, \qquad B_4(s)>0,
$$

and

$$
|B_3(s)|\le3, \qquad |B_5(s)|\le26.
$$

Therefore

$$
P_{II}^{(5)}(s,r)\ge r\left(\frac16-3r^2-26r^4\right)>0.1665r
$$

for $0<r\le1/200$.

## 5. Remainder lemma

The endpoint Taylor remainders satisfy

$$
|E_I(s,r)|\le4\cdot10^9r^6,
$$

and

$$
|E_{II}(s,r)|\le4\cdot10^9r^6.
$$

The proof is by residual correction for the selected branch equations.  Let $X_A^{(5)}$ and $X_B^{(5)}$ be the fifth-order approximants for the selected $A$- and $B$-branches.  Substitution into the exact branch systems gives

$$
\|G_A(X_A^{(5)})\|_\infty\le1.74\cdot10^7r^6,
$$

and

$$
\|G_B(X_B^{(5)})\|_\infty\le1.22\cdot10^6r^6.
$$

On the endpoint coordinate boxes

$$
|u_3|\le\frac1{50},\qquad |v_3-1|\le\frac3{100},
$$

and

$$
|u_5|\le\frac1{50},\qquad |v_5|\le\frac3{100},
$$

the inverse Jacobian bounds are

$$
\|J_A^{-1}\|_\infty\le3, \qquad \|J_B^{-1}\|_\infty\le6.
$$

The Newton--Kantorovich correction gives

$$
\|X_A-X_A^{(5)}\|_\infty\le1.1\cdot10^8r^6,
$$

and

$$
\|X_B-X_B^{(5)}\|_\infty\le1.6\cdot10^7r^6.
$$

In the same endpoint box,

$$
\Delta v-\Delta u\ge0.90, \qquad 0.90\le D\le1.10,
$$

and direct differentiation of $\tau$ gives

$$
\|\nabla\tau\|_1\le25.
$$

Thus the branch-root correction contributes at most $2.75\cdot10^9r^6$ to $|\tau-\tau_5|$.  The direct fifth-order truncation contributes at most $2.0\cdot10^8r^6$.

The explicit radial terms and the switch have smaller remainders:

$$
|\rho_2(r,sr)-\rho_{2,I}^{(5)}(s,r)|\le5.0\cdot10^6r^6,
$$

$$
|\rho_2(\sigma(r),sr)-\rho_{2,II}^{(5)}(s,r)|\le2.0\cdot10^7r^6,
$$

and

$$
|\sigma(r)-\sigma_5(r)|<0.12r^6.
$$

Combining these estimates gives

$$
|E_I(s,r)|\le4\cdot10^9r^6, \qquad |E_{II}(s,r)|\le4\cdot10^9r^6.
$$

## 6. Endpoint positivity

For Region I,

$$
F_I(sr,r)\ge0.1663r-4\cdot10^9r^6 =r(0.1663-4\cdot10^9r^5).
$$

Since $r\le1/200$,

$$
4\cdot10^9r^5\le0.0125.
$$

Hence $F_I(sr,r)>0$.

For Region II,

$$
F_{II}(sr,r)\ge0.1665r-4\cdot10^9r^6 =r(0.1665-4\cdot10^9r^5)>0.
$$

Thus both reduced inequalities are proved for $0<r\le1/200$.
