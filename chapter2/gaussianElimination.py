# program to solve systems of linear equations using gaussian elimination
#importing necessary libraries
import numpy as np
import scipy.linalg as la

"""
Parametric solution function to express the solution in terms of free variables
R: RREF matrix
var: number of variables
eps: tolerance for identifying pivot elements,
1e-10 is a common choice to avoid issues with floating-point precision
"""
def parametric_solution(R, var, eps=1e-10):
    # Identify pivot and free variables
    pivot_cols = []
    for i in range(R.shape[0]):
        for j in range(R.shape[1] - 1):
            if abs(R[i, j]) > eps:
                pivot_cols.append(j)
                break

    free_vars = [j for j in range(var) if j not in pivot_cols]
    num_free = len(free_vars)

    if num_free == 0:
        print("Unique solution:", R[:, -1])
        return

    print(f"Free variables: {free_vars}")
    print("Expressing solution in terms of free variables:")

    # Create a solution vector with parameters for free variables
    solution = np.zeros(var)
    for i in range(len(pivot_cols)):
        col = pivot_cols[i]
        solution[col] = R[i, -1]
        for j in free_vars:
            solution[col] -= R[i, j] * f"x{j + 1}"

    print("Parametric form of the solution:")
    print(solution)




def add_row(A, k, i, j):
    "row j <- k times row i added to row j in matrix A."
    n = A.shape[0]
    E = np.eye(n)
    if i == j:
        E[j, j] = k + 1
    else:
        E[j, i] = k
    return E @ A


def scale_row(A, k, i):
    "row i <- k times row i in matrix A"
    n = A.shape[0]
    E = np.eye(n)
    E[i, i] = k
    return E @ A


def swap_row(A, i, j):
    "row i <-> row j in matrix A"
    n = A.shape[0]
    E = np.eye(n)
    if i != j:
        E[i, i], E[i, j], E[j, i], E[j, j] = 0, 1, 1, 0
    return E @ A


"""
Function to input the coefficients of the equations
and the constants
Returns: a tuple of the matrix of coefficients and the vector of constants
"""


def get_system():
    # ask user for number of variables
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

    # define and initialize coefficient and constant matrices
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


# get_system() returns a tuple of the matrix of coefficients and the vector of constants
A, b, var = get_system()

# After coefficients and constants are parsed we can perform gaussian elimination
b = np.reshape(b, (var, 1))
aug_mat = np.hstack([A, b])
print(aug_mat)

# Gaussian elimination for n x n system using row operations
R = aug_mat.copy()
step = 0

def print_step(label, mat):
    global step
    step += 1
    print(f"\nStep {step}: {label}")
    print(mat)


# Forward elimination
for col in range(var):
    pivot = col
    while pivot < var and abs(R[pivot, col]) < 1e-10:
        pivot += 1
    if pivot == var:
        continue

    if pivot != col:
        R = swap_row(R, col, pivot)
        print_step(f"swap_row(R, {col}, {pivot})", R)

    pivot_val = R[col, col]
    if pivot_val != 0:
        R = scale_row(R, 1 / pivot_val, col)
        print_step(f"scale_row(R, {1 / pivot_val}, {col})", R)

    for row in range(col + 1, var):
        if R[row, col] != 0:
            R = add_row(R, -R[row, col], col, row)
            print_step(f"add_row(R, {-R[row, col]}, {col}, {row})", R)


# Back substitution to reduced row echelon form
for col in range(var - 1, -1, -1):
    for row in range(col - 1, -1, -1):
        if R[row, col] != 0:
            R = add_row(R, -R[row, col], col, row)
            print_step(f"add_row(R, {-R[row, col]}, {col}, {row})", R)


print("\nFinal RREF:")
print(R)

# Check consistency using rank theorem
augmented = aug_mat
rank_A = np.linalg.matrix_rank(A)
rank_augmented = np.linalg.matrix_rank(augmented)

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
