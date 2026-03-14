
from fractions import Fraction

import numpy as np
import matplotlib.pyplot as plt
# Define the complex numbers as NumPy arrays
#8/4-i
z1 = np.array([5 , -2])  # Represents 8 + 0i
z2 = np.array([8, 9])   # Represents 4 - 1i
# Perform the division (z1 / z2)
denominator = z2[0]**2 + z2[1]**2
real_part = (z1[0] * z2[0] + z1[1] * z2[1]) / denominator  # Real part: (ac + bd)
imaginary_part = (z1[1] * z2[0] - z1[0] * z2[1]) / denominator  # Imaginary part: (bc - ad)
#if result has decimal then convert to fraction
real_part = Fraction(real_part).limit_denominator()
imaginary_part = Fraction(imaginary_part).limit_denominator()   
result = np.array([real_part, imaginary_part])
print("The result of (8 + 0i) / (4 - 1i) is:")
print(f"{result[0]} + {result[1]}i")
# Plotting the complex numbers with lines connecting them to the origin