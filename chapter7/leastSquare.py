"""
Chapter 7: Least Squares (Polynomial Regression)

What this script does:
1) Builds a Vandermonde matrix A for a polynomial fit to data (t, y).
   For degree=d, the model is: y ≈ c0 + c1 t + ... + cd t^d.
2) Forms the normal equations: (A^T A) x = (A^T b), where x are the coefficients.
3) Solves the normal-equations system using the repo's `gaussian_elimination`
   function so you can see the row-operation steps (like the other chapter files).
4) Prints the final regression equation using fractions (not decimals).
5) Predicts y-values at t-values you enter (optional).
6) Plots the original points and the fitted curve.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from fractions import Fraction

try:
    from common.gaussian_elimination import gaussian_elimination
except ModuleNotFoundError:
    # Allows running this script from inside `chapter7/`.
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from common.gaussian_elimination import gaussian_elimination


def predict(t, coeffs):
    """Evaluate y(t) = sum_{k=0}^d coeffs[k] * t^k for scalar/array t."""
    t_arr = np.asarray(t, dtype=float)
    y = np.zeros_like(t_arr, dtype=float)
    for power, coef in enumerate(coeffs):
        y += coef * (t_arr ** power)
    return y


def least_squares_fit(t, y, degree=1, show_steps=True):
    """
    Fits a polynomial of a given degree to data points (t, y)
    using the Normal Equations: (A.T @ A) @ x = A.T @ b
    """
    # 1. Construct Vandermonde Matrix A: [1, t, t^2, ...]
    A = np.vander(t, degree + 1, increasing=True)
    
    # 2. Vector b (our target values)
    b = y
    
    # 3. Calculate A^T * A and A^T * b to form the Normal Equations
    # This projects the problem into a space where an exact solution exists.
    ATA = A.T @ A
    ATb = A.T @ b
    
    # 4. Solve the system ATA * x = ATb using our repo's Gaussian elimination,
    # printing row-operation steps like the other files.
    var = degree + 1
    R, aug = gaussian_elimination(ATA, ATb, var, show_steps=show_steps)
    rank_left = np.linalg.matrix_rank(ATA)
    rank_aug = np.linalg.matrix_rank(aug)
    if rank_left != rank_aug:
        raise ValueError("Normal equations are inconsistent (unexpected numerically).")
    if rank_left != var:
        raise ValueError("Normal equations do not have a unique solution (rank deficient).")
    coefficients = R[:, -1]
    
    return coefficients

def _format_fraction(x, max_denominator=1000):
    frac = Fraction(float(x)).limit_denominator(max_denominator)
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"


def _format_polynomial_equation(coeffs, variable="t", max_denominator=1000):
    fracs = [Fraction(float(c)).limit_denominator(max_denominator) for c in coeffs]
    parts = []
    for power, frac in enumerate(fracs):
        if frac == 0:
            continue

        sign = "-" if frac < 0 else "+"
        abs_frac = -frac if frac < 0 else frac

        if power == 0:
            term = _format_fraction(abs_frac, max_denominator=max_denominator)
        else:
            var = variable if power == 1 else f"{variable}^{power}"
            if abs_frac == 1:
                term = var
            else:
                term = f"{_format_fraction(abs_frac, max_denominator=max_denominator)}{var}"

        parts.append((sign, term))

    if not parts:
        return "y = 0"

    first_sign, first_term = parts[0]
    eq = f"y = {'-' if first_sign == '-' else ''}{first_term}"
    for sign, term in parts[1:]:
        eq += f" {sign} {term}"
    return eq

# --- Data Setup ---
t_points = np.array([-2, -1, 0, 1, 2])
y_points = np.array([4, 2, 1, 3, 6])

# --- Perform Fit ---
while True:
    degree_in = input("Enter polynomial degree (press Enter for 2): ").strip()
    if degree_in == "":
        degree = 2
        break
    try:
        degree = int(degree_in)
        if degree < 0:
            print("Degree must be >= 0.")
            continue
        break
    except ValueError:
        print("Please enter an integer degree (e.g. 0, 1, 2, 3).")

coeffs = least_squares_fit(t_points, y_points, degree=degree)

# --- Output Results ---
print("Calculated Equation (fractions):", _format_polynomial_equation(coeffs, variable="t"))

# --- Prediction (optional) ---
pred_in = input("Enter t value(s) to predict (space-separated, Enter to skip): ").strip()
if pred_in:
    try:
        t_query = [float(x) for x in pred_in.split()]
        y_query = predict(t_query, coeffs)
        print("\nPredictions:")
        for t_val, y_val in zip(t_query, y_query):
            print(f"  t = {t_val}: y ≈ {y_val} (≈ {_format_fraction(y_val)})")
    except ValueError:
        print("Could not parse t values; skipping prediction.")

# --- Visualization ---
t_fine = np.linspace(min(t_points) - 0.5, max(t_points) + 0.5, 100)
y_fine = predict(t_fine, coeffs)

plt.figure(figsize=(8, 5))
plt.scatter(t_points, y_points, color='red', label='Original Data')
plt.plot(t_fine, y_fine, color='blue', linewidth=2, label='Least Squares Fit')

# Formatting the graph
plt.xlabel('t')
plt.ylabel('y')
plt.title(f'Least Squares Regression (degree={degree})')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.show()
