"""Shared Gaussian elimination utilities for the Math232 repo."""

import numpy as np
import scipy.linalg as la

EPS = 1e-10


def parametric_solution(R, var, eps=EPS):
    """Print a parametric solution for an RREF augmented matrix."""
    pivot_cols = []
    for i in range(R.shape[0]):
        for j in range(R.shape[1] - 1):
            if abs(R[i, j]) > eps:
                pivot_cols.append(j)
                break

    free_vars = [j for j in range(var) if j not in pivot_cols]

    print(f"Free variables: {[f'x{j+1}' for j in free_vars]}")

    for i, p_col in enumerate(pivot_cols):
        constant = R[i, -1]
        terms = [f"{constant:.2f}"]
        for f_col in free_vars:
            coef = -R[i, f_col]
            if abs(coef) > eps:
                terms.append(f"{'+' if coef > 0 else ''}{coef:.2f}*x{f_col+1}")
        print(f"x{p_col+1} = {' '.join(terms)}")

    for f_col in free_vars:
        print(f"x{f_col+1} = x{f_col+1} (free)")


def add_row(A, k, i, j):
    """Row j <- k times row i added to row j in matrix A."""
    n = A.shape[0]
    E = np.eye(n)
    if i == j:
        E[j, j] = k + 1
    else:
        E[j, i] = k
    return E @ A


def scale_row(A, k, i):
    """Row i <- k times row i in matrix A."""
    n = A.shape[0]
    E = np.eye(n)
    E[i, i] = k
    return E @ A


def swap_row(A, i, j):
    """Row i <-> row j in matrix A."""
    n = A.shape[0]
    E = np.eye(n)
    if i != j:
        E[i, i], E[i, j], E[j, i], E[j, j] = 0, 1, 1, 0
    return E @ A


def get_system():
    """Collect coefficients and constants from user input."""
    while True:
        try:
            var_input = input("Enter the number of variables: ")
            if not var_input.strip():
                print("Error: Please enter a number.")
                continue
            var = int(var_input)
            if var <= 0:
                print("Error: Number of variables must be positive.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")

    A = np.zeros((var, var))
    b = np.zeros(var)

    for i in range(var):
        print(f"\nEquation {i + 1}:")
        for j in range(var):
            while True:
                try:
                    coef_input = input(f"Enter coefficient of x{j + 1}: ")
                    if not coef_input.strip():
                        print("Error: Please enter a number.")
                        continue
                    A[i, j] = float(coef_input)
                    break
                except ValueError:
                    print("Error: Please enter a valid number.")

        while True:
            try:
                const_input = input("Enter the constant: ")
                if not const_input.strip():
                    print("Error: Please enter a number.")
                    continue
                b[i] = float(const_input)
                break
            except ValueError:
                print("Error: Please enter a valid number.")

    return A, b, var


def gaussian_elimination(A, b, var, eps=EPS, show_steps=True):
    """Perform Gaussian elimination and return RREF.

    ``b`` may be either a length-``var`` vector or a ``(var, k)`` matrix, so
    the same function can solve ``Ax = b``, row-reduce ``[A | 0]``, or reduce
    ``[A | I]`` when computing inverses.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)

    if b.ndim == 1:
        b = np.reshape(b, (var, 1))
    elif b.ndim == 2 and b.shape[0] == var:
        pass
    else:
        raise ValueError(
            f"Right-hand side must have shape ({var},) or ({var}, k); got {b.shape}."
        )

    aug_mat = np.hstack([A, b])
    if show_steps:
        print(aug_mat)

    R = aug_mat.copy()
    step = 0

    def print_step(label, mat):
        nonlocal step
        step += 1
        print(f"\nStep {step}: {label}")
        print(mat)

    for col in range(var):
        pivot = col
        while pivot < var and abs(R[pivot, col]) < eps:
            pivot += 1
        if pivot == var:
            continue

        if pivot != col:
            R = swap_row(R, col, pivot)
            if show_steps:
                print_step(f"swap_row(R, {col}, {pivot})", R)

        pivot_val = R[col, col]
        if abs(pivot_val) > eps:
            R = scale_row(R, 1 / pivot_val, col)
            if show_steps:
                print_step(f"scale_row(R, {1 / pivot_val}, {col})", R)

        for row in range(col + 1, var):
            if abs(R[row, col]) > eps:
                factor = -R[row, col]
                R = add_row(R, factor, col, row)
                if show_steps:
                    print_step(f"add_row(R, {factor}, {col}, {row})", R)

    for col in range(var - 1, -1, -1):
        for row in range(col - 1, -1, -1):
            if abs(R[row, col]) > eps:
                factor = -R[row, col]
                R = add_row(R, factor, col, row)
                if show_steps:
                    print_step(f"add_row(R, {factor}, {col}, {row})", R)

    if show_steps:
        print("\nFinal RREF:")
        print(R)

    return R, aug_mat


def main():
    A, b, var = get_system()
    R, aug_mat = gaussian_elimination(A, b, var)

    rank_A = np.linalg.matrix_rank(A)
    rank_augmented = np.linalg.matrix_rank(aug_mat)

    if rank_A == rank_augmented:
        print("The system is consistent")
        if rank_A == var:
            print("The system has a unique solution")
            x = la.solve(A, b)
            print("\nSolution vector:")
            print(x)
        else:
            print("The system has infinitely many solutions")
            parametric_solution(R, var)
    else:
        print("The system is inconsistent (no solution)")
        print(f"Rank(A) = {rank_A}, Rank([A|b]) = {rank_augmented}")


if __name__ == "__main__":
    main()
