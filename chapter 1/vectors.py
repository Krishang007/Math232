import numpy as np
import scipy as sp
import scipy.linalg as la

#define  vectors

def assignVal(u,v,w):
    u_in=input("Enter the values for vector u (x,y,z) separated by commas: ")  
    for i in u_in.replace(' ', '').split(','):
        print(i)

    v_in=input("Enter the values for a vector v(x,y,z) separated by commas: ")
    for i in v_in.replace(' ', '').split(','):
        print(i)
    w_in=input("Enter the values for a vector w(x,y,z) separated by commas: ")
    for i in w_in.replace(' ', '').split(','):
        print(i)
    u=np.array([int(i.strip()) for i in u_in.replace(' ', ',').split(',')])
    v=np.array([int(i.strip()) for i in v_in.replace(' ', ',').split(',')])
    w=np.array([int(i.strip()) for i in w_in.replace(' ', ',').split(',')])
    return u, v, w

u, v, w = assignVal(u, v, w)
#vector uv
#uv=v-u:vector subtraction
u_v=v-u
print('Vector v-u:', u_v)
#vector uw
#uw=w-u:vector subtraction
u_w=w-u
print('Vector w-u:', u_w)