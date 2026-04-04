"""
script to calculate the power of a matrix using diagonalization
"""
import sympy as sp
from diag import diagonalize

# Power of a matrix: k
k = sp.symbols('k')
k_val = 100

A = sp.Matrix([[0, -1,1], 
               [0, 2,0], 
               [-2,1,3]])

print(f"Goal: Calculate A^k where k = {k_val}")

# Step 1 & 2: Get P and D using diag.py
print("\n--- Step 1 & 2: Diagonalization ---")
P, D = diagonalize(A.tolist(), show_steps=True)

if P is not None:
    # Step 3: Find P^-1
    print("\n--- Step 3: Find P^-1 ---")
    P_inv = P.inv()
    sp.pprint(P_inv)

    # Step 4: Calculate D^k
    print(f"\n--- Step 4: Calculate D^{k} ---")
    # Get eigenvalues from diagonal entries of D
    eigenvalues = [D[i, i] for i in range(D.rows)]
    # Handle zero eigenvalue cleanly

    D_k = sp.diag(*[sp.Pow(val, k, evaluate=False) for val in eigenvalues])
    # Pretty print with clearer mathematical meaning
    print("D^k =")
    sp.pprint(D_k)
    
    # Step 5: Calculate A^k = P D^k P^-1
    D_k_subs = D_k.subs(k, k_val)
    sp.pprint(D_k_subs)
    sp.pprint(P*D_k_subs)
    sp.pprint(P*D_k_subs*P_inv)
    print(f"\n--- Step 5: Calculate A^{k} = P * D^{k} * P^-1 ---")
    A_k = P * D_k * P_inv
    A_k = sp.simplify(A_k)
    A_k = sp.factor(A_k)
    sp.pprint(A_k)

    # Final result for the given k_val
    print(f"\n--- Final Result: A^{k_val} ---")
    result = sp.simplify(A_k.subs(k, k_val))
    result = sp.factor(result)
    sp.pprint(result)
else:
    print("\nCannot calculate power using diagonalization because the matrix is not diagonalizable.")
