import numpy as np

from sympy import Matrix, Rational, pprint

# 1. Change-of-basis matrix (basis vectors as columns)
P = Matrix([
    [1,  1, 0],
    [1, -1, 0],
    [0,  0, 1]
])

# 2. Standard matrix of T
A = Matrix([
    [2,  3, 0],
    [1,  2, 1],
    [2, -2, 1]
])
# 1. Compute P^{-1}
P_inv = P.inv()
pprint("P^{-1} =")
pprint(P_inv)
# 2. Compute P*A
AP = A *P
pprint("A * p =")
pprint(AP)


# 3. [T]_B = P^{-1} * A * P
L_B = P.inv() * A * P

print("[T]_B =")
pprint(L_B)
#xvecor 
