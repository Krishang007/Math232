import sympy as sp
import numpy as np
from gaussianElimination import gaussian_elimination

lam = sp.symbols('λ')

def print_eigen_steps(A_matrix):
    print("Matrix A:")
    sp.pprint(A_matrix)

    # Step 1: A - λI
    I = sp.eye(A_matrix.shape[0])
    A_lam = A_matrix - lam*I

    print("\nStep 1: A - λI")
    sp.pprint(A_lam)

    # Step 2: determinant
    print("\nStep 2: det(A - λI)")
    det_expr = sp.expand(A_lam.det())
    sp.pprint(det_expr)

    # Step 3: factor polynomial
    print("\nStep 3: Characteristic Polynomial")
    factored = sp.factor(det_expr)
    sp.pprint(factored)

    poly = sp.Poly(det_expr, lam)
    discriminant = sp.simplify(sp.discriminant(det_expr, lam))
    print("\nDiscriminant Check:")
    print(f"Discriminant = {discriminant}")
    if poly.degree() == 2:
        if sp.is_negative(discriminant):
            print("Since the discriminant is negative, the characteristic polynomial has complex roots.")
        else:
            print("Since the discriminant is non-negative, the characteristic polynomial does not have complex roots.")
    else:
        print("Discriminant computed. The sign test for complex roots applies directly only to quadratic characteristic polynomials.")

    # Step 4: eigenvalues
    print("\nStep 4: Solve det(A-λI)=0")
    eigenvalues = sp.solve(det_expr, lam)
    print("Eigenvalues:", eigenvalues)

    # Step 5: eigenspaces
    for val in eigenvalues:
        print(f"\nStep 5: Eigenspace for λ = {val}")

        M = A_matrix - val*I

        print("\nA - λI:")
        sp.pprint(M)

        print("\nRREF steps (Gaussian Elimination):")
        M_np = np.array(M.tolist(), dtype=complex)
        b_zero = np.zeros(M_np.shape[0], dtype=complex)
        gaussian_elimination(M_np, b_zero, M_np.shape[0], show_steps=True)

        print("\nEigenvector basis (Exact using Sympy):")
        basis = M.nullspace()
        for v in basis:
            sp.pprint(v)
            
def print_inverse_steps(A_matrix):
    print("\nFinding Inverse of matrix:")
    sp.pprint(A_matrix)
    
    n = A_matrix.shape[0]
    A_np = np.array(A_matrix.tolist(), dtype=float)
    I_np = np.eye(n)
    
    print("\nRREF steps to find inverse (Augmented with Identity):")
    # Using gaussian_elimination with Identity matrix as `b`
    R, _ = gaussian_elimination(A_np, I_np, n, show_steps=True)
    
    inverse_np = R[:, n:]
    inverse_sp = sp.nsimplify(sp.Matrix(inverse_np), rational=True)
    print("\nCalculated Inverse (Exact):")
    sp.pprint(inverse_sp)
    
    return inverse_sp

# Keep original behavior if run directly
if __name__ == "__main__":
    A_test = sp.Matrix([
        [1 ,3,3],
        [3 ,1,3],
        [3,3,1]
    ])
    print_eigen_steps(A_test)
