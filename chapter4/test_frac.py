import numpy as np
from fractions import Fraction

def format_frac(x):
    f = Fraction(x).limit_denominator()
    return str(f) if f.denominator != 1 else str(f.numerator)

np.set_printoptions(formatter={'float_kind': format_frac})
A = np.array([
    [7,0,4],
    [3,3,3],
    [0,7,3]
], dtype=float)
print(A)
