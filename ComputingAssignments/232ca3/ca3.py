import numpy as np
import scipy.linalg as la   # package with addtional linear algebra tool: for example matrix inverse
from rref import *
## Problem 1: Change of Basis + Linear Transformations
"""
uses conceps from chapter 4
4.2 Bases and Dimension 
4.3 Coordinates 
4.4 General Linear Mappings 
4.5 Matrix of a Linear Mapping    
""" 
### 1a) Change-of-coordinates matrices
#Define the vectors 
v1 = np.array([0, 1, 2,1])#v1
v2 = np.array([1, 5, 0,1])#v2
v3 = np.array([2, 3, 6,4])#v3
v4 = np.array([1, 3, -1,-1])#v4
# P_SB: columns ARE the basis vector in standard basis
PSB = np.column_stack([v1, v2, v3, v4])
print("P_SB:\n", PSB)
PBS = la.inv(PSB)#command to compute the inverse of a matrix
print("P_BS:\n", PBS)
print(f"First col (1 d.p.): {np.round(PBS[:,0], 1)}")
# ── Problem 1b ────────────────────────────────
# [x]_B = P_{B←S} @ x
x = np.array([1, 2, 3, 4])#vector x in standard coordinates
xB = PBS @ x#multiply the change of basis matrix with the vector x to get the coordinates of x in the basis B
print(f"xB = {xB}")
print(f"xB[0] (1 d.p.) = {round(xB[0], 1)}")
# ── Problem 1c ────────────────────────────────
#linear transformation L: R^4 → R^4 defined by
# L(x1,x2,x3,x4) = (x2+5x4,  x1-x3,  x1+x2+x3+x4,  0)

LS = np.array([[0, 1, 0, 5],
               [1, 0,-1, 0],
               [1, 1, 1, 1],
               [0, 0, 0, 0]])
print(LS)
#from the fact[L]_B = P_{B←S} @ [L]_S @ P_{S←B} 
LB = PBS @ LS @ PSB
print(LB)
# ── Problem 1d ────────────────────────────────
#from the fact that [L(x)]_B = [L]_B @ [x]_B
##composition of the linear transformation L and the vector x in the basis B 
LxB = LB @ xB
print(LxB)

## Problem 2: Power Method (Dominant Eigenvalue/Eigenvector)
"""
uses conceps from chapter 6
6.1 Eigenvalues and Eigenvectors
power method is an iterative algorithm to find the dominant eigenvalue and its corresponding eigenvector of a matrix.
The dominant eigenvalue is the eigenvalue with the largest absolute value, and its corresponding eigenvector is called the dominant eigenvector.
The power method works by repeatedly multiplying a vector by the matrix and normalizing the result. As the iterations progress, the vector converges to the dominant eigenvector, and the Rayleigh quotient of the vector converges to the dominant eigenvalue.
  
""" 
A = np.array([[1,2,0,0],
              [1,1,1,1],
              [0,1,1,5],
              [0,0,1,1]])

# our initial unit vector
x0 = np.array([1,0,0,0]) 

y1 = A@x0                         # compute next vector y1
x1 = y1/(np.sqrt(np.dot(y1,y1)))  # normalize the vector y1 to form x1
print(f"x1 = {x1}")

y2 = A@x1                         # compute next vector y2
x2 = y2/(np.sqrt(np.dot(y2,y2)))  # normalize the vector y2 to form x2
print(f"x2 = {x2}")
# Problem 2a: compute x3
y3 = A@x2
x3 = y3/(np.sqrt(np.dot(y3,y3)))
print(f"x3 = {x3}")
x0 = np.array([1,0,0,0])
evec_approx_list = [x0]  # this will be the list of approximations to the dominant eigenvector
eval_approx_list = [np.dot(A@x0,x0)]  # this will be the list of approximations to the dominant eigenvalue

x0 = np.array([1,0,0,0])
evec_approx_list = [x0]  # this will be the list of approximations to the dominant eigenvector
eval_approx_list = [np.dot(A@x0,x0)]  # this will be the list of approximations to the dominant eigenvalue

# Increased upper bound to 30 for convergence to 4 decimal places
for i in range(1,30):  
    new_vec = A@evec_approx_list[-1]                                 # pick last vector in evec_approx_list, and apply A to it
    evec_approx_list.append(new_vec/np.sqrt(np.dot(new_vec,new_vec)))            # add the new normalized vector to evec_approx_list
    eval_approx_list.append(np.dot(A@evec_approx_list[-1],evec_approx_list[-1])) # add updated approx. for lambda to eval_approx_list  
    print(f"x_{i:<2} = {evec_approx_list[i]}, and \u03bb^({i:<2}) = {eval_approx_list[i]}")  # print the new approximations to the screen

# Dominant eigenvector (truncated to 4 decimal places)
x_d = np.array([0.3953, 0.5206, 0.7074, 0.2685])
# Dominant eigenvalue (truncated to 2 decimal places)
lambda_d = 3.63