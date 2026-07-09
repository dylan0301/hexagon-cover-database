# 407X Computation Certificates

Status: Reference

This directory contains finite interval certificates used in the completed
`407X_T3_like_no_Vd1Vd2` proof package.

Both scripts use exact rational interval arithmetic.  Square roots are enclosed
by one-sided rational bounds obtained using integer arithmetic.  No floating
point comparison is used for certification.

## 1. Left-high/right-$T_-$ threshold

Script:

```bash
python proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py
```

Certified implication:

$$
S_0<{93\over200}\quad\Longrightarrow\quad B_5<{5657\over10000}.
$$

Recorded output:

```text
terminal boxes: 1174
max depth: 30
counts: {'B5_upper': 112, 'S0_lower': 290, 'domain_beta': 20, 'domain_cell': 752}
unresolved boxes: 0
B0 < (7-sqrt(13))/6 verified
```

## 2. Left-high/right-lower-sheet threshold

Script:

```bash
python proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407X_computation/407c_T_hi_Tlo_left_threshold_certificate.py
```

Certified implication:

$$
S_0<\sqrt{p^2-p+1}-p\quad\Longrightarrow\quad B_5<1-p.
$$

Recorded output:

```text
terminal boxes: 1459
max depth: 21
counts: {'B5_upper': 186, 'S0_lower': 365, 'domain_beta': 65, 'domain_cell': 648, 'domain_p': 195}
unresolved boxes: 0
```
