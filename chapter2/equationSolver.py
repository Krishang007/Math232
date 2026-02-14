"""Solve systems of linear equations."""

import numpy as np
import scipy.linalg as la
import sympy as sp
from sympy import pprint, sympify



"""
Data structure used in this program:
Tuples are used to store multiple items in a single variable.
numpy are used to create and manipulate arrays.
scipy.linalg is used to perform linear algebra operations.
"""


def get_system():
    """Collect coefficients and constants from user input."""
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
    # create a matrix of zeros
    A = np.zeros((var, var))
    # create a vector of zeros
    b = np.zeros(var)
    """
    Nested loop through the matrix and fill it with user input
    loop iterates from 0 to var-1
    first loop iterates through the rows
    second loop iterates through the columns
    number of columns is equal to the number of variables
    """
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


def main():
    # creates a matrix of coefficients and a vector of constants
    # get_system() returns a tuple of the matrix of coefficients and the vector of constants
    A, b, var = get_system()

    # to check for consistency in the system use concepts from linear algebra
    # A system is consistent if the system has at least one solution 
    # in consistent if the system has no solution
    # Apply Rank and Consistency Theorem :
    # Rank(A)= the number of pivots (leading ones)
    # if Rank(A)= Rank(A|b) then the system is consistent
    # if Rank(A) != Rank(A|b) then the system is inconsistent
    # if Rank(A)= Rank(A|b)= number of variables then the system has a unique solution
    # if Rank(A)= Rank(A|b) < number of variables then the system has infinitely many solutions
    # if Rank(A) != Rank(A|b) then the system has no solution
    
    # Create augmented matrix [A|b] by adding b as a column to A
    # now the the number of columns is var+1
    augmented = np.column_stack((A, b))

    # Check consistency using rank theorem
    rank_A = np.linalg.matrix_rank(A)
    rank_augmented = np.linalg.matrix_rank(augmented)

    if rank_A == rank_augmented:
        print("The system is consistent")
        if rank_A == var:
            print("The system has a unique solution")
            # solve the system
            x = la.solve(A, b)  # returns the solution vector
            # prints the solution
            print("\nSolution vector:")
            print(x)
        else:
            print("The system has infinitely many solutions")
            print("Cannot compute a unique solution for this system")
    else:
        print("The system is inconsistent (no solution)")
        print(f"Rank(A) = {rank_A}, Rank([A|b]) = {rank_augmented}")


if __name__ == "__main__":
    main()
