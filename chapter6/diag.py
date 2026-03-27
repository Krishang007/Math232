import sympy as sp
from eigen import eigen_solve

A = sp.Matrix([[1, 2],
               [3, 2]])

P = sp.Matrix([[6, -3],
               [9,  3]])

print("Matrix A:")
sp.pprint(A)

print("\nMatrix P:")
sp.pprint(P)

# Columns of P
v1 = P[:, 0]
v2 = P[:, 1]

print("\nColumn vectors of P:")
print("v1 =")
sp.pprint(v1)
print("v2 =")
sp.pprint(v2)

# Get eigenvalues and eigenvectors from eigen.py
print("\nSteps from eigen.py:")
eigen_results = eigen_solve(A.tolist(), show_steps=True)

print("\nEigenvalues from eigen.py:")
eigenvalues = list(eigen_results.keys())
sp.pprint(eigenvalues)

print("\nEigenvectors from eigen.py:")
for i, eigenvalue in enumerate(eigenvalues, start=1):
    print(f"For λ = {eigenvalue}")
    basis = eigen_results[eigenvalue]["basis"]
    for vector in basis:
        sp.pprint(vector)

# Check if columns are eigenvectors
print("\nCheck Av = λv")

for i, v in enumerate([v1, v2], start=1):
    Av = A * v
    print(f"\nA * v{i} =")
    sp.pprint(Av)

    if v[0] != 0:
        lam = sp.simplify(Av[0] / v[0])
    else:
        lam = sp.simplify(Av[1] / v[1])

    print(f"λ{i} = {lam}")
    print(f"λ{i} * v{i} =")
    sp.pprint(lam * v)

    print(f"A * v{i} - λ{i} * v{i} =")
    sp.pprint(sp.simplify(Av - lam * v))

# Compute P^{-1} A P
print("\nP^{-1}:")
P_inv = P.inv()
sp.pprint(P_inv)

print("\nP^{-1} A P:")
D = (P_inv * A * P).applyfunc(sp.simplify)
sp.pprint(D)
