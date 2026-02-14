#program to help students perform basic matrix operations
def matrix_subtraction(A, B):
    if A.shape != B.shape:
        print("Error: Matrices must have the same dimensions for subtraction.")
        return None
    return A - B  
import numpy as np
def userInput():
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(row):
        row_data = list(map(float, input(f"Enter the elements of row {i+1} separated by space: ").split()))
        matrix.append(row_data)
    return np.array(matrix)
def matrix_addition(A, B):
    if A.shape != B.shape:
        print("Error: Matrices must have the same dimensions for addition.")
        return None
    return A + B
def start():
    print("Welcome to the Matrix Operation Program!")
    print("Please choose an operation:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of a Matrix")
    print("5. Inverse of a Matrix")
    
    choice = int(input("Enter your choice (1-5): "))
    
    if choice in [1, 2, 3]:
        print("Matrix A:")
        A = userInput()
        print("Matrix B:")
        B = userInput()
        
        if choice == 1:
            result = matrix_addition(A, B)
            print("Result of A + B:")
            print(result)
        elif choice == 2:
            result = matrix_subtraction(A, B)
            print("Result of A - B:")
            print(result)
        elif choice == 3:
            result = matrix_multiplication(A, B)
            print("Result of A * B:")
            print(result)
    
    elif choice in [4, 5, 6]:
        print("Matrix A:")
        A = userInput()
        
        if choice == 4:


            result = matrix_transpose(A)
            print("Transpose of A:")
            print(result)
        elif choice == 5:
            result = matrix_inverse(A)
            print("Inverse of A:")
            print(result)
        elif choice == 6:           
            result = matrix_determinant(A)
            print("Determinant of A:")
            print(result)
    else:
        