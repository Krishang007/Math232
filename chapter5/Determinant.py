import numpy as np
import sympy as sp
from gaussianElimination import gaussian_elimination

def det(matrix):
    matrix = sp.Matrix(matrix)
    return matrix.det()

def main():
    matrix = sp.Matrix([
        [2, 5, -3, -2],
        [-2, -3, 2, -5],
        [1, 3, -2, 2],
        [-1, -6, 4, 3]
    ])
    print("Matrix A:")
    sp.pprint(matrix)
    print("Determinant of A:")
    #using gaussian elimination to find the determinant
    sp.pprint(det(matrix))#print the determinant of A in box form symbollically
    #determinant using cofactor expansion
    print("\n")
    

if __name__ == "__main__":
    main()