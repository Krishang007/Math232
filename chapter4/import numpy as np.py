import numpy as np

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

# 3. Solve for [L]_B such that P * [L]_B = A
# This is equivalent to [L]_B = inv(P) * A
L_B = np.linalg.solve(P, A)

print("The matrix [L]_B is:")
print(np.round(L_B).astype(int)) # Rounding to handle floating point precision