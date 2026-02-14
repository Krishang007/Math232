import numpy as np
from rref import rref
#print("ca1 package loaded successfully")
""""
Question 1:
Consider the following vectors in R5:
a) Create each of the 6 vectors in python as an np.array, and save them with the names v0 through v5.
Then, use the command np.column_stack to create the matrix with column vectors v0 through v5. Save it with the name A.
"""
#my code here
v0=np.array([1,1,2,3,-1])
v1=np.array([1,2,2,1,0])
v2=np.array([1,4,2,-3,2])
v3=np.array([1,7,2,-9,5])
v4=np.array([2,1,2,1,3])
v5=np.array([5,0,4,4,8])
A=np.column_stack((v0,v1,v2,v3,v4,v5))
#test code
"Verify v0 through v5 were created as arrays and have the correct size. (1 mark)"
assert isinstance(v0,np.ndarray) and v0.shape == (5,)
assert isinstance(v1,np.ndarray) and v1.shape == (5,)
assert isinstance(v2,np.ndarray) and v2.shape == (5,)
assert isinstance(v3,np.ndarray) and v3.shape == (5,)
assert isinstance(v4,np.ndarray) and v4.shape == (5,)
assert isinstance(v5,np.ndarray) and v5.shape == (5,)
print("Test 1: Success!")
"Verify matrix A is an array of the correct size. (1 mark)"
assert isinstance(A,np.ndarray)
assert A.shape == (5,6)
print("Test 2: Success!")
"Verify vector v0 has the correct entries. (1 mark)"
assert np.array_equal(v0, np.array([1,1,2,3,-1]))
print("Test 3: Success!")
"Verify the first and second column of A are correct. (1 mark)"
assert np.array_equal(A[:,0], np.array([1,1,2,3,-1]))
assert np.array_equal(A[:,1], np.array([1,2,2,1,0]))
print("Test 4: Success!")
"Verify vectors v1 through v5 have correct entries. This cell contains hidden tests. (1 mark)"
"Verify matrix A has correct entries. This cell contains hidden tests. (1 mark)"
#(b) Using the rref command, find the reduced row echelon form of A. Save the output of the rref command as RA.
RA = rref(A)
"Verify RA was computed from the rref command. (1 mark)"
assert isinstance(RA[0],np.ndarray)
assert isinstance(RA[1],tuple)
assert RA[0].shape == (5,6)
print("Test 5: Success!")
""""
(c) Which columns are the pivot columns? Give your answer in the form of a tuple of column indices, the same form that was output from the rref command: ( , , ). Save your answer as pivot_indices.
Hint: you should type in the cell below pivot_indices = ( , , ), with the three correct index numbers separated by the commas.
"""
pivot_indices = (0, 1, 4)
"Verify pivot_indices is a tuple of the correct size. (1 mark)"
assert isinstance(pivot_indices,tuple)
assert len(pivot_indices) == 3
print("Test 6: Success!")
"Verify all entries of pivot_indices are correct. This cell contains hidden tests. (1 mark)"
#(d) What is the rank of matrix A? Save it with the name rankA.
rankA = 3#rankA is the number of pivot columns, which is 3 in this case.
"Verify rank A is correct. This cell contains hidden tests. (1 mark)"
#(e) How many free variables are there in the system ? Save your answer as nullityA.
nullityA = 3#nullityA is the number of columns - rank, which is 6 - 3 = 3 in this case.
#(f) Create a new matrix containing only the pivot columns of A. Save this matrix with the name P
P = A[:,pivot_indices]
"Verify pivot columns matrix P is np.array and has correct correct size. (1 mark)"
assert isinstance(P,np.ndarray)
assert P.shape == (5,3)
print("Test 7: Success!")
"Verify pivot columns matrix P has correct entries. This cell contains hidden tests. (1 mark)"
#(g) Find a vector so that the product(Pw=v2) . Use an np.array to create w and save it with the name w.
w = np.array([-2,3,0])#since v2 is the second pivot column, w should be [0,1,0]
#w = RA[0][:3, 2].astype(int)
"Verify w is a vector of the correct size. (1 mark)"
assert isinstance(w,np.ndarray)
assert w.shape == (3,)
print("Test 8: Success!")
#"Verify w has the correct entries. This cell contains hidden tests. (1 mark)"
"""(h) Find a matrix 
 so that 
. Use an np.array to create 
 and save it with the name W.
 """
W = np.array([[-2,-5,1],
             [ 3, 6,-2],
              [ 0, 0, 3]])
#W = RA[0][:3, [2, 3, 5]].astype(int)
"Verify W is a matrix of the correct size. (1 mark)"
assert isinstance(W,np.ndarray)  # checking if W was constructed as an array
assert W.dtype == int   # checking if the entries in W are integers (no decimal points at all)
assert W.shape == (3,3) # checking if W is a 3x3 matrix
print("Test 8: Success!")
"Verify W has the correct entries. This cell contains hidden tests. (1 mark)"

