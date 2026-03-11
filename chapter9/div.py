
import numpy as np
import matplotlib.pyplot as plt
# Define the complex numbers as NumPy arrays
#(3-i)(1+3i)
z1 = np.array([3, 5])  # Represents 3+5i
z2 = np.array([-2, 1])   # Represents -2+i
# Perform the division (z1 / z2)
denominator = z2[0]**2 + z2[1]**2
real_part = (z1[0] * z2[0] + z1[1] * z2[1]) / denominator  # Real part: (ac + bd)
imaginary_part = (z1[1] * z2[0] - z1[0] * z2[1]) / denominator  # Imaginary part: (bc - ad)
result = np.array([real_part, imaginary_part])
print("The result of (3 + 5i) / (-2 + i) is:")
print(f"{result[0]} + {result[1]}i")
# Plotting the complex numbers with lines connecting them to the origin