import numpy as np
#from sympy import *
import matplotlib.pyplot as plt
from numpy import linalg as la

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-8, 3)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

vectors = np.array([[3,4],[1,1],[1,-2],[-2,2]]) # four vectors to plot

for i in range(len(vectors)):
    ax.arrow(0, 0, vectors[i][0], vectors[i][1], head_width=0.2, head_length=0.2, fc='red', ec='black')

ax.quiver([0, 0, 0], [0, 0, 0], [1, -2, 4], [1, 2, -7], color=['r','b','g'], angles='xy', scale_units='xy', scale=1)
plt.show()

    