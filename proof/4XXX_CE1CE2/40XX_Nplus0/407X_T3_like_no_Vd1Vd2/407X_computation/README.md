# 407X Computation Certificates

Status: Reference

This directory contains the finite interval certificate used in the completed
`407X_T3_like_no_Vd1Vd2` proof package.

The script uses exact rational interval arithmetic.  Square roots are enclosed
by one-sided rational bounds obtained using integer arithmetic.  No floating
point comparison is used for certification.

## Left-high/right-$T_-$ threshold

Script:

```bash
python proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py
```

Certified implication:

$$
S_0<\frac{93}{200}\quad\Longrightarrow\quad B_5<\frac{5657}{10000}.
$$

Recorded output:

```text
terminal boxes: 1174
max depth: 30
counts: {'B5_upper': 112, 'S0_lower': 290, 'domain_beta': 20, 'domain_cell': 752}
unresolved boxes: 0
B0 < (7-sqrt(13))/6 verified
```
