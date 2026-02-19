import numpy as np
from rref import rref

#array of row vectors of A
A = np.array([
    [1, 3, 0, 2],
    [0, 1, -1, 2],
    [2, 7, -1, 1]
])


print("Original matrix A:")
print(A)
# b is a zero vector.
b = np.zeros(3)

# Compute RREF of the augmented matrix [A|b].
Ab = np.hstack((A, b.reshape(-1, 1)))
print("\nAugmented matrix [A|b]:")
print(Ab)
rref_Ab, pivot_cols_Ab = rref(Ab)
print("\nRREF of the augmented matrix [A|b]:")
print(rref_Ab)

# The solution to Ax = 0 is represented in the augmented form above.
# If the system is consistent, the last column of rref_Ab is all zeros.
# If the last column has any nonzero entry, the system is inconsistent.
tol = 1e-10
lhs = rref_Ab[:, :-1]
rhs = rref_Ab[:, -1]
inconsistent = np.any(np.all(np.abs(lhs) < tol, axis=1) & (np.abs(rhs) > tol))

if inconsistent:
    print("\nSystem is inconsistent: no solution.")
else:
    n = A.shape[1]
    pivot_cols = []
    for c in np.asarray(pivot_cols_Ab, dtype=object).ravel():
        if np.isscalar(c):
            ci = int(c)
        else:
            c_arr = np.asarray(c).ravel()
            if c_arr.size == 0:
                continue
            ci = int(c_arr[0])
        if ci < n:
            pivot_cols.append(ci)
    pivot_row_for_col = {col: i for i, col in enumerate(pivot_cols)}
    pivot_set = set(pivot_cols)
    free_cols = [j for j in range(n) if j not in pivot_set]
    param_names = [f"t{k + 1}" for k in range(len(free_cols))]
    free_to_param = dict(zip(free_cols, param_names))

    print("\nSystem is consistent. Parameterization:")
    for j in range(n):
        if j in free_to_param:
            print(f"x{j + 1} = {free_to_param[j]}")
        else:
            pivot_row = pivot_row_for_col[j]
            terms = []
            for free_col in free_cols:
                coeff = -lhs[pivot_row, free_col]
                if abs(coeff) < tol:
                    continue
                terms.append(f"({coeff:g})*{free_to_param[free_col]}")
            rhs_expr = " + ".join(terms) if terms else "0"
            print(f"x{j + 1} = {rhs_expr}")
#linear independece 
rank_A = len(pivot_cols)
print(f"\nRank of A: {rank_A}")
if rank_A == A.shape[1]:
    print("The columns of A are linearly independent.")
else:    print("The columns of A are linearly dependent.")
dim_col_space = rank_A
print(f"Dimension of the column space of A: {dim_col_space}")
