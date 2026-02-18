import numpy as np
from fractions import Fraction
from rref import rref# rref fucntion 
from gaussianElimination import gaussian_elimination# gaussian elimination function to compute the RREF of the matrix and show the steps of the process


def read_positive_int(prompt):
    """Read a positive integer from user input."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value <= 0:
                print("Please enter an integer greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def input_matrix():
    """Input matrix from user."""
    print("Input a matrix you want to analyze:")
    rows = read_positive_int("Enter the number of rows: ")
    cols = read_positive_int("Enter the number of columns: ")

    matrix = []
    for i in range(rows):
        while True:
            raw = input(f"Enter row {i + 1} (space-separated): ").strip()
            parts = raw.split()
            if len(parts) != cols:
                print(f"Please enter exactly {cols} values.")
                continue
            try:
                matrix.append([float(x) for x in parts])
                break
            except ValueError:
                print("Please enter valid numeric values.")

    return np.array(matrix, dtype=float)


def to_fraction_matrix(matrix):
    """Convert matrix entries to simplified fractions for display."""
    return np.array(
        [[Fraction(x).limit_denominator() for x in row] for row in matrix],
        dtype=object,
    )


def read_yes_no(prompt):
    """Read yes/no input."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please enter y/yes or n/no.")


def show_elimination_steps(matrix):
    """Show elimination steps using gaussian_elimination for square matrices."""
    #matrix shape=(rows, cols) if rows != cols then the matrix is not square and we cannot show the elimination steps
    if matrix.shape[0] != matrix.shape[1]:
        print("\nStep-by-step elimination is available only for square matrices.")
        return
    n = matrix.shape[0]
    b = np.zeros(n)
    print("\nGaussian elimination steps:")
    gaussian_elimination(matrix.copy(), b, n, show_steps=True)


def analyze_matrix(matrix):
    """Compute RREF, pivot columns, rank/nullity, and inverse information."""
    rref_matrix, pivot_columns = rref(matrix.copy())
    rank = len(pivot_columns)
    nullity = matrix.shape[1] - rank

    is_square = matrix.shape[0] == matrix.shape[1]
    is_full_rank_square = is_square and rank == matrix.shape[0]

    if is_full_rank_square:
        inverse_kind = "Inverse"
        inverse_value = np.linalg.inv(matrix)
        inverse_value = to_fraction_matrix(inverse_value)
    else:
        inverse_kind = "Inverse (not available)"
        inverse_value = "N/A - Matrix is singular or not square"

    return {
        "rref_matrix": rref_matrix,
        "pivot_columns": pivot_columns,
        "rank": rank,
        "nullity": nullity,
        "inverse_kind": inverse_kind,
        "inverse_value": inverse_value,
    }


def main():
    matrix = input_matrix()
    if read_yes_no("Show Gaussian elimination steps? (y/n): "):
        show_elimination_steps(matrix)

    result = analyze_matrix(matrix)

    print("\nOriginal Matrix:")
    print(matrix)
    print("Reduced Row Echelon Form:")
    print(result["rref_matrix"])
    print(f"Pivot Columns: {result['pivot_columns']}")
    print(f"Rank: {result['rank']}")
    print(f"Nullity: {result['nullity']}")
    print(f"{result['inverse_kind']}:")
    print(result["inverse_value"])


if __name__ == "__main__":
    main()
