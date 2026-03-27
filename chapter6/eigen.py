import numpy as np
import sympy as sp

from gaussianElimination import gaussian_elimination, parametric_solution

lam = sp.symbols('λ')


def numpy_to_sympy_matrix(matrix, tol=1e-10):
    cleaned = []
    for row in matrix:
        cleaned_row = []
        for value in row:
            cleaned_row.append(0 if abs(value) < tol else value)
        cleaned.append(cleaned_row)
    return sp.Matrix(cleaned)


def print_eigen_work(matrix, eigenvalue, show_steps=True):
    identity = sp.eye(matrix.rows)
    eigenspace_matrix = matrix - eigenvalue * identity

    print(f"\nStep 5: Eigenspace for λ = {eigenvalue}")
    print("\nA - λI:")
    sp.pprint(eigenspace_matrix)

    if eigenvalue.has(sp.I):
        print("\nRREF (using SymPy natively for complex values):")
        rref_matrix, _ = eigenspace_matrix.rref()
        sp.pprint(rref_matrix)
    else:
        print("\nRREF using gaussianElimination.py:")
        coeff_matrix = np.array(eigenspace_matrix.tolist(), dtype=float)
        zero_vector = np.zeros(coeff_matrix.shape[0], dtype=float)
        rref_with_augmented_col, _ = gaussian_elimination(
            coeff_matrix,
            zero_vector,
            coeff_matrix.shape[0],
            show_steps=show_steps
        )
        rref_matrix = numpy_to_sympy_matrix(rref_with_augmented_col[:, :-1])
        print("\nRREF coefficient matrix:")
        sp.pprint(rref_matrix)
    
        if show_steps:
            print("\nStep 6: Parameterization of the Null Space:")
            parametric_solution(rref_with_augmented_col, rref_with_augmented_col.shape[1] - 1)

    print("\nFinal Eigenvector basis:")
    basis = eigenspace_matrix.nullspace()
    for vector in basis:
        sp.pprint(vector)

    return {
        "matrix": eigenspace_matrix,
        "rref": rref_matrix,
        "basis": basis,
    }


def eigen_solve(matrix_data, show_steps=True):
    matrix = sp.Matrix(matrix_data)

    if show_steps:
        print("Matrix A:")
        sp.pprint(matrix)

    identity = sp.eye(matrix.rows)
    a_minus_lambda_i = matrix - lam * identity

    if show_steps:
        print("\nStep 1: A - λI")
        sp.pprint(a_minus_lambda_i)

        print("\nStep 2: det(A - λI)")
    determinant = sp.expand(a_minus_lambda_i.det())
    if show_steps:
        sp.pprint(determinant)

        print("\nStep 3: Characteristic Polynomial")
    factored = sp.factor(determinant)
    if show_steps:
        sp.pprint(factored)

        print("\nStep 4: Solve det(A-λI)=0")
    eigenvalues = sp.solve(determinant, lam)
    if show_steps:
        print("Eigenvalues:", eigenvalues)

    results = {}
    if any(val.has(sp.I) for val in eigenvalues):
        if show_steps:
            print("\nComplex eigenvalue detected! Matrix is not diagonalizable over Reals.")
            print("=> No need to find eigenvectors (for this type of question).")
        return {"eigenvalues": eigenvalues}

    for eigenvalue in eigenvalues:
        eigenspace_matrix = matrix - eigenvalue * identity
        basis = eigenspace_matrix.nullspace()
        results[eigenvalue] = {
            "matrix": eigenspace_matrix,
            "basis": basis,
        }
        if show_steps:
            details = print_eigen_work(matrix, eigenvalue, show_steps=show_steps)
            results[eigenvalue].update(details)

    return results


def main():
    matrix = [
        [-3, -1, 1],
        [58, 10, -58],
        [1, 0, -3],
    ]
    eigen_solve(matrix, show_steps=True)


if __name__ == "__main__":
    main()
