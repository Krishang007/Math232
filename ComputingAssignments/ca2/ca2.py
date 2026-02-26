import os
import numpy as np
import matplotlib.pyplot as plt  # used for plotting points in a graph

# load points
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'points.csv')
points = np.loadtxt(csv_path, delimiter=',')


# plot points
plt.scatter(points[0,:],points[1,:],s=2,c=[[0.75,0,0,1]])
plt.axis('equal'), plt.grid(True)
plt.show()


"""
after packages are installed and data is loaded, the first plot will show the original points.
and the code for the transformation has been written.The next step is to strat working on the 
practice questions.

"""
#practice problem 

# YOUR CODE HERE
#vertical reflection


# construct some matrices that might contribute to the final image
F = np.array([[-1,0],
              [0,1]])  # reflect across y-axis
S = np.array([[1,0],
             [1.5,1]]) # vertical shear by a factor of 1.5
T = S@F

# apply the matrix product to the collection of points
points6 = T@points

# plot the collection of points
plt.scatter(points[0,:],points[1,:],s=2,c=[[0.75,0,0,0.05]])
plt.scatter(points6[0,:],points6[1,:],s=2,c=[[0.75,0,0,1]])
plt.axis('equal'), plt.grid(True)
plt.show()

#problem 1a
# YOUR CODE HERE
#ther is a relfection 

# apply the matrix to the points with matrix multiplication:
points7 = T1a @ points

# plot the collection of points
plt.scatter(points[0,:],points[1,:],s=2,c=[[0.75,0,0,0.1]])
plt.scatter(points7[0,:],points7[1,:],s=2,c=[[0.75,0,0,1]])
plt.axis('equal'), plt.grid(True)
plt.show()
