import  numpy as np
import scipy as sp
import scipy.linalg as la
#projection
u=np.array([6,3,2])
print(u)
print('Dimension:', u.ndim) # dimention of the array
print('Shape:', u.shape) # returns a tuple of length of the number of array dimensions and has the number of elements in each dimension
print('Size:', u.size) # number of elemetns in the array
v=np.array ([7,8,9])
print(v)
print ('Dimension:', v.ndim) # 
print('Shape:', v.shape) # 
print('Size:', v.size) #

#dot product of u and v
dot_product=np.dot(u,v)
"""
or we can use 
dot_product= sum(u*v)    
or simply
dot_product=u@v
 """    
  
print('Dot product of u and v:', dot_product)
def lenght(u):
    #return la.norm(u)
    #return np.sqrt(sum(u*u))
    return np.sqrt(np.dot(u,u))
    
def lenght(v):
    #return la.norm(v)
    #return np.sqrt(sum(v*v))
    return np.sqrt(np.dot(v,v))

lenth_u=lenght(u)  #magnitude of u
lenth_v=lenght(v) #magnitude of v
print('Magnitude of v:', lenth_v)
#projection of u onto v
def projection(u,v):
    return ((np.dot(u,v)/np.dot(v,v))*v)

     
print('Projection of u onto v:', projection(u,v))