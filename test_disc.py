import sympy as sp

lam = sp.symbols('lam')
det_expr = lam**2 - 9*lam + 29
print(sp.discriminant(det_expr, lam))
