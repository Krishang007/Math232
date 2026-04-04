import sympy as sp
from eigen import eigen_solve


def diagonalize(matrix_data, show_steps: bool = True):
    """
    Diagonalizes a matrix A, returning P and D such that A = P D P^-1.
    """
    A = matrix_data if isinstance(matrix_data, sp.Matrix) else sp.Matrix(matrix_data)
    
    if show_steps:
        print("Matrix A:")
        sp.pprint(A)

    # Get eigenvalues and eigenvectors from eigen.py
    eigen_results = eigen_solve(A.tolist(), show_steps=show_steps)

    # eigen.py returns {"eigenvalues": [...]} for complex eigenvalues
    if list(eigen_results.keys()) == ["eigenvalues"]:
        if show_steps:
            print("\nComplex eigenvalues detected; not diagonalizable over the reals.")
        return None, None

    # Collect an eigenvector basis until we have n independent columns
    chosen_vectors: list[sp.Matrix] = []
    chosen_eigenvalues: list[sp.Expr] = []
    target_cols = A.cols

    for eigenvalue, data in eigen_results.items():
        for vec in data.get("basis", []):
            candidate_vectors = chosen_vectors + [vec]
            P_try = sp.Matrix.hstack(*candidate_vectors)
            if P_try.rank() == len(candidate_vectors):
                chosen_vectors.append(vec)
                chosen_eigenvalues.append(eigenvalue)
            if len(chosen_vectors) == target_cols:
                break
        if len(chosen_vectors) == target_cols:
            break

    if len(chosen_vectors) != target_cols:
        if show_steps:
            print("\nMatrix is not diagonalizable (not enough independent eigenvectors).")
        return None, None

    P = sp.Matrix.hstack(*chosen_vectors)
    if P.det() == 0:
        if show_steps:
            print("\nMatrix is not diagonalizable (eigenvectors are dependent).")
        return None, None

    D = sp.diag(*chosen_eigenvalues)

    # Verify (optional)
    P_inv = P.inv()
    A_check = sp.simplify(P * D * P_inv)

    if show_steps:
        print("\nMatrix P (eigenvectors as columns):")
        sp.pprint(P)
        print("\nDiagonal Matrix D (eigenvalues on diagonal):")
        sp.pprint(D)
        print("\nP^-1:")
        sp.pprint(P_inv)
        
        print("\nCheck if A = P * D * P^-1")
        if A_check == A:
            print("Diagonalization verified: A == P * D * P^-1")
        else:
            print("Warning: Verification failed!")

    return P, D


def main():
    A = sp.Matrix([[-5, 2],
                   [2, -2]])
    diagonalize(A)


if __name__ == "__main__":
    main()
