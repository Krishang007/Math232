import numpy as np
from gaussianElimination import gaussian_elimination

# 1. Define the basis vectors as columns of matrix P
P = np.array([
    [-3, -2, -1],
    [ 3, -2,  0],
    [ 0, -2,  2]
])

# 2. Define the transformed vectors L(v1), L(v2), L(v3) as columns of matrix A
A = np.array([
    [ 2, -5, -1],
    [ 2,  1, 18],
    [ 2, -2, -4]
])

# 3. Solve for [L]_B column-by-column from P * x_j = A[:, j]
n = P.shape[0]
L_B = np.zeros_like(A, dtype=float)

for j in range(A.shape[1]):
    print(f"\nSolving for column {j + 1} of [L]_B:")
    R, _ = gaussian_elimination(P.copy(), A[:, j].copy(), n, show_steps=True)
    L_B[:, j] = R[:, -1]


print("The matrix [L]_B is:")
print(np.round(L_B).astype(int))  # Rounded for clean integer display
