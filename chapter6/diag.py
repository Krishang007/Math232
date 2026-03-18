import sympy as sp
from eigne import print_eigen_steps, print_inverse_steps

# Define matrices
# Define matrices
A = sp.Matrix([[4, 1],
               [-9, 5]])

P = sp.Matrix([[1, 4],
               [-1, 1]])


print("\n--- Eigenvalues and Eigenvectors of A ---")
print_eigen_steps(A)

print("\n--- Diagonalization Verification ---")
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

# Check if columns are eigenvectors
print("\nCheck Av = λv")

for i, v in enumerate([v1, v2], start=1):
    Av = A * v
    print(f"\nA * v{i} =")
    sp.pprint(Av)

    # Try to find lambda
    if v[0] != 0:
        lam = Av[0] / v[0]
    else:
        lam = Av[1] / v[1]

    print(f"λ for v{i} =", lam)
    print("λ * v =")
    sp.pprint(lam * v)

# Compute P^{-1} A P
print("\n--- P^{-1} Computation ---")
P_inv = print_inverse_steps(P)

print("\nP^{-1} A P:")
D = P_inv * A * P
sp.pprint(D)