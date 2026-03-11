import numpy as np
A=np.array([[37,-6], [216,-35]])
B=np.array([[1,1], [6 ,5]])
print("The matrix A is:")
print(A)
print("The matrix B is:")
print(B)
#AB=np.dot(A,B)
AB=A@B
print("The product AB is:")
print(AB)
#INVER OF B
B_inv=np.linalg.inv(B)
print("The inverse of B is:")
print(B_inv)
#BINVERSE*AB
result=B_inv@AB
ROUND_RESULT=np.round(result).astype(int)
print("The result of B^-1 * AB is:")
print(ROUND_RESULT)
X_VECTOR=np.array([[1], [2]])
#result*X_VECTOR
final_result=result@X_VECTOR
print("The result of (B^-1 * AB) * X is:")
print(final_result)
