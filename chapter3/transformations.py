#propgram to compute and visualize matrix transformations
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
#reffer to formulas in transfomations.md file

def rotation(theta):
   
    theta_rad = np.radians(theta)
    #rotation matrix
    R = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                  [np.sin(theta_rad), np.cos(theta_rad)]])
    return R
