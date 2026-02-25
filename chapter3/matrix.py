import sympy as sym
from sympy import pprint, Matrix


def get_input(prompt, type_func=str):
    """Loops until valid input of type `type_func` is received."""
    while True:
        try:
            val = input(prompt)
            if not val:
                return None
            return type_func(val)
        except ValueError:
            print(f"Invalid input. Please enter a valid {type_func.__name__}.")
        except EOFError:
            return None


def input_matrix(name):
    """Prompt the user to enter a matrix row by row. Returns a SymPy Matrix."""
    rows = get_input(f"Enter number of rows for {name}: ", int)
    if rows is None:
        return None
    cols = get_input(f"Enter number of columns for {name}: ", int)
    if cols is None:
        return None

    print(f"Enter {name} entries row by row (space-separated):")
    data = []
    for i in range(rows):
        while True:
            row_str = input(f"  Row {i + 1}: ")
            entries = row_str.split()
            if len(entries) != cols:
                print(f"  Expected {cols} values, got {len(entries)}. Try again.")
                continue
            try:
                data.append([sym.sympify(e.replace('^', '**')) for e in entries])
                break
            except Exception:
                print("  Could not parse entries. Use numbers or expressions like 1/2, sqrt(2).")
    return Matrix(data)


def print_section(title):
    """Print a section header."""
    print(f"\n--- {title} ---")


def show(label, value):
    """Pretty-print a labelled result."""
    print(f"\n{label}:")
    pprint(value)


def main():
    print("\n===  Matrix Operations  ===")

    # --- Input matrices ---
    use_default = input("Use default 3×3 matrices? (y/n): ").strip().lower()
    if use_default == 'y':
        A = Matrix([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
        B = Matrix([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])
    else:
        A = input_matrix("A")
        if A is None:
            return
        B = input_matrix("B")
        if B is None:
            return

    show("Matrix A", A)
    show("Matrix B", B)

    # --- Basic arithmetic (requires same dimensions) ---
    if A.shape == B.shape:
        print_section("Arithmetic")
        show("A + B", A + B)
        show("A - B", A - B)

        c = get_input("Enter a scalar to multiply A by (or press Enter to skip): ")
        if c is not None:
            try:
                c_val = sym.sympify(c.replace('^', '**'))
                show(f"{c_val} · A", c_val * A)
            except Exception:
                print("Could not parse scalar.")
    else:
        print("\n⚠  A and B have different dimensions — skipping addition/subtraction.")

    # --- Matrix multiplication ---
    print_section("Multiplication")
    if A.shape[1] == B.shape[0]:
        show("A × B", A * B)
    else:
        print(f"Cannot compute A × B: A is {A.shape[0]}×{A.shape[1]}, "
              f"B is {B.shape[0]}×{B.shape[1]} (need cols(A) = rows(B)).")

    if B.shape[1] == A.shape[0]:
        show("B × A", B * A)
    else:
        print(f"Cannot compute B × A: dimension mismatch.")

    # --- Transpose ---
    print_section("Transpose")
    show("Aᵀ", A.T)
    show("Bᵀ", B.T)

    # --- Square-matrix operations ---
    for name, M in [("A", A), ("B", B)]:
        if M.shape[0] != M.shape[1]:
            continue

        print_section(f"Properties of {name}  ({M.shape[0]}×{M.shape[1]})")

        det = M.det()
        show(f"det({name})", det)

        if det != 0:
            show(f"{name}⁻¹", M.inv())
        else:
            print(f"\n{name} is singular (det = 0) — no inverse exists.")

    # --- RREF ---
    print_section("Row-Reduced Echelon Form")
    rref_A, pivots_A = A.rref()
    show("rref(A)", rref_A)
    print(f"  Pivot columns: {list(pivots_A)}")

    rref_B, pivots_B = B.rref()
    show("rref(B)", rref_B)
    print(f"  Pivot columns: {list(pivots_B)}")


if __name__ == "__main__":
    main()
