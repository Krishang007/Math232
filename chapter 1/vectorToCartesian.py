import numpy as np
import scipy as sp
import scipy.linalg as la

#define  vectors
"""
u=np.array([6,3,2])
print("u=[6,3,2]")
v=np.array([4,3,3])
print("v=[4,3,3]")
w=np.array([9,2,6])

print("w=[9,2,6]")
"""
def assignVal():
    # Helper to clean and convert input
    def parse_input(prompt):
        #INPUT UPTO NTH DIMENSION
        raw = input(prompt)
        # Replaces spaces with commas, then splits to handle "1 2 3" or "1,2,3"
        cleaned = raw.replace(' ', ',').split(',')
        # Remove empty strings caused by double spaces/commas
        # this typecasts the string inputs to integers and creates a numpy array
        return np.array([int(i) for i in cleaned if i.strip()])

    u = parse_input("Enter vector u : ")
    v = parse_input("Enter vector v : ")
    w = parse_input("Enter vector w : ")
    
    return u, v, w
def dimentionCheck():
    u, v, w = assignVal()
    if u.ndim != v.ndim or u.ndim != w.ndim:
        print("Error: Vectors must have the same number of dimensions.")
        return False
    if u.size1 == 3:
        #call threeD_plane function1
        threeD_plane(u, v, w)
        return True
    else:
        print(f"Vectors are {u.size}D. Currently only 3D planes are supported.")
        return False
"""

print('Dimension:', u.ndim) # 
print('Shape:', u.shape) # 
print('Size:', u.size) # 

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
def threeD_plane(u, v, w):
    #find direction vectors 
    #vector uv
    #uv=v-u:vector subtraction
    u_v=v-u
    print('Vector v-u:', u_v)
    #vector uw
    #uw=w-u:vector subtraction
    u_w=w-u
    print('Vector w-u:', u_w)
    """normal=np.cross(u_v,u_w)
    #cross product of uv and uw
    print('Cross product of v-u and w-u:', normal)
    print("The cross product of uv and uw refers to the normal vector of the plane defined by the points u, v, and w")
    """
    # Use cross product to find normal vector - much simpler and more robust
    normal = np.cross(u_v, u_w)
    print('Normal vector to the plane defined by points u,v,w:', normal)
    #compute dot product of normal vector and point u to find d in the plane equation
    dot_product=np.dot(normal,u)# dot product of normal vector and point vector u
    print('Dot product of the normal vector and point u:', dot_product)
    #extract coeefficients a,b,c from normal vector
    a=normal[0]
    b=normal[1]
    c=normal[2]
    d=dot_product
    print("the cartesian equation of the plane: {}x + {}y + {}z = {}".format(a,b,c,d))

# Run the dimension check and plane calculation
dimentionCheck()
