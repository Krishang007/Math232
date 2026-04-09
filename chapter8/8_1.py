import sys
from pathlib import Path

import sympy as sp


# Allow importing chapter6/eigen.py (and its helpers) without packaging the repo.
CHAPTER6_DIR = Path(__file__).resolve().parents[1] / "chapter6"
sys.path.append(str(CHAPTER6_DIR))

from eigen import eigen_solve  # noqa: E402


def _inner(u: sp.Matrix, v: sp.Matrix) -> sp.Expr:
    return (u.T * v)[0]


def _orthonormalize(vectors: list[sp.Matrix]) -> list[sp.Matrix]:
    """
    Gram–Schmidt orthonormalization in the standard inner product.
    Returns a list of unit (orthonormal) column vectors.
    """
    orthonormal: list[sp.Matrix] = []
    for v in vectors:
        w = sp.Matrix(v)
        for u in orthonormal:
            w = sp.simplify(w - _inner(u, w) * u)  # u is unit

        norm_sq = sp.simplify(_inner(w, w))
        if norm_sq == 0:
            continue
        orthonormal.append(sp.simplify(w / sp.sqrt(norm_sq)))
    return orthonormal


def orthogonal_diagonalize_symmetric(matrix_data, show_steps: bool = True):
    """
    For a real symmetric matrix A, find an orthogonal matrix P and diagonal D
    such that P^T A P = D.

    Method: eigen-decomposition + Gram–Schmidt normalization of eigenvectors.
    """
    A = matrix_data if isinstance(matrix_data, sp.Matrix) else sp.Matrix(matrix_data)

    if show_steps:
        print("Goal: find orthogonal P and diagonal D with P^T A P = D.\n")
        print("Matrix A:")
        #sp.pprint(A)

    if A.rows != A.cols:
        raise ValueError(f"A must be square; got shape {A.shape}.")

    symmetry_defect = sp.simplify(A - A.T)
    if symmetry_defect != sp.zeros(A.rows, A.cols):
        raise ValueError(
            "A must be symmetric for orthogonal diagonalization (A == A.T). "
            f"Got A - A.T = {symmetry_defect}."
        )

    eigen_results = eigen_solve(A.tolist(), show_steps=show_steps)
    if list(eigen_results.keys()) == ["eigenvalues"]:
        if show_steps:
            print("\nComplex eigenvalues detected; cannot orthogonally diagonalize over the reals.")
        return None, None

    n = A.cols

    # Collect eigenvectors (with labels) and orthonormalize.
    raw_vectors: list[sp.Matrix] = []
    labels: list[sp.Expr] = []

    for eigenvalue in sorted(eigen_results.keys(), key=lambda ev: sp.N(ev)):
        for vec in eigen_results[eigenvalue].get("basis", []):
            raw_vectors.append(vec)
            labels.append(eigenvalue)

    P_cols: list[sp.Matrix] = []
    D_diag: list[sp.Expr] = []

    # Gram–Schmidt, preserving eigenvalue labels for retained directions.
    for vec, eigenvalue in zip(raw_vectors, labels):
        w = sp.Matrix(vec)
        for u in P_cols:
            w = sp.simplify(w - _inner(u, w) * u)
        norm_sq = sp.simplify(_inner(w, w))
        if norm_sq == 0:
            continue
        u_new = sp.simplify(w / sp.sqrt(norm_sq))
        P_cols.append(u_new)
        D_diag.append(eigenvalue)
        if len(P_cols) == n:
            break

    if len(P_cols) != n:
        if show_steps:
            print("\nNot enough independent eigenvectors to form an orthonormal basis.")
        return None, None

    P = sp.Matrix.hstack(*P_cols)
    D = sp.diag(*D_diag)

    if show_steps:
        print("\nOrthogonal matrix P (orthonormal eigenvectors as columns):")
        sp.pprint(P)
        print("\nDiagonal matrix D (matching eigenvalues):")
        sp.pprint(D)

        print("\nCheck P^T P = I:")
        sp.pprint(sp.simplify(P.T * P))

        print("\nCheck P^T A P = D:")
        sp.pprint(sp.simplify(P.T * A * P))

        print("\n(Equivalent form) A = P D P^T:")
        sp.pprint(sp.simplify(P * D * P.T))

    return P, D


def main():
    A = sp.Matrix([[5, -1, 1], [-1, 5, 1],
                   [1, 1, 5]])
    orthogonal_diagonalize_symmetric(A, show_steps=True)


if __name__ == "__main__":
    main()
