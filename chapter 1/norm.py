import numpy as np
import scipy as sp
import scipy.linalg as la

#define  vectors

u=np.array([1,0,0])
print("u=[1,0,0]")
v=np.array([0,1,0])
print("v=[0,1,0]")
w=np.array([0,0,1])
print("w=[0,0,1]")
print('Dimension:', u.ndim) # 
print('Shape:', u.shape) # 
print('Size:', u.size) # 
"""
magnitude=np.sqrt(np.dot(u,u))  #magnitude of u
print('Magnitude using standard formula:', magnitude)
magnitude=la.norm(u)  #another way to compute magnitude of u this is slower
print ('Magnitude using la.norm:', magnitude)
#compute the dot product of u and v

dot_product=np.dot(u,v)
print('Dot product of u and v:', dot_product)
if dot_product==0:
    print('u and v are orthogonal')
else:
    print('u and v are not orthogonal')
"""
#find direction vectors 
#vector uv
#uv=v-u:vector subtraction
u_v=v-u
print('Vector v-u:', u_v)
#vector uw
#uw=w-u:vector subtraction
u_w=w-u
print('Vector w-u:', u_w)

#cross product of uv and uw
normal=np.cross(u_v,u_w)
print('Cross product of v-u and w-u:', normal)
print("The cross product of uv and uw refers to the normal vector of the plane defined by the points u, v, and w")
dot_product=np.dot(normal,u)# dot product of normal vector and point vector u
print('Dot product of the normal vector and point u:', dot_product)
#extract coeefficients a,b,c from normal vector
a=normal[0]
b=normal[1]
c=normal[2]
d=-dot_product
print(" the cartesian equation of the plane: {}x + {}y + {}z + {} = 0".format(a,b,c,d))
