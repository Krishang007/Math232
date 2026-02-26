import numpy as np
from rref import rref

"""
Script to find coordinates respecting a non-standard basis.
We will use the same matrix A as in the previous script,
but now we will treat its columns as a basis for the column space.
We will find the coordinates of the vector b with respect to this basis.
"""

A = np.array([
    [1, 1, 0],
    [1, 0, 1],
    [0, 3, 3],   
    [-3, 3, 6]
])

print("Original matrix A:")
print(A)

b = np.array([
    [-1],
    [1],
    [6],        
    [15]
])

# Augmented matrix
Ab = np.hstack((A, b))
print("\nAugmented matrix [A|b]:")
print(Ab)

rref_Ab, pivot_cols_Ab = rref(Ab)
print("\nRREF of the augmented matrix [A|b]:")
print(rref_Ab)

tol = 1e-10
lhs = rref_Ab[:, :-1]
rhs = rref_Ab[:, -1]

inconsistent = np.any(
    np.all(np.abs(lhs) < tol, axis=1) & (np.abs(rhs) > tol)
)

if inconsistent:
    print("\nSystem is inconsistent: no solution.")
else:
    n = A.shape[1]

    pivot_cols = []
    for c in pivot_cols_Ab:
        if c < n:
            pivot_cols.append(int(c))

    pivot_row_for_col = {col: i for i, col in enumerate(pivot_cols)}
    pivot_set = set(pivot_cols)

    free_cols = [j for j in range(n) if j not in pivot_set]

    print("\nSystem is consistent. Coordinates:")

    for j in range(n):
        pivot_row = pivot_row_for_col[j]
        const = rhs[pivot_row]

        terms = []
        for free_col in free_cols:
            coeff = -lhs[pivot_row, free_col]
            if abs(coeff) < tol:
                continue
            terms.append(f"({coeff:g})*t")

        expr = " + ".join(terms)

        if expr:
            expr = f"{const:g} + {expr}"
        else:
            expr = f"{const:g}"

        print(f"x{j+1} = {expr}")

# Rank
rank_A = len(pivot_cols)
print(f"\nRank of A: {rank_A}")

if rank_A == A.shape[1]:
    print("The columns of A are linearly independent.")
else:
    print("The columns of A are linearly dependent.")

print(f"Dimension of the column space of A: {rank_A}")