#complex numbers
import numpy as np
import matplotlib.pyplot as plt
# Define the complex numbers as NumPy arrays
#(3-i)(1+3i)
z1 = np.array([3, -1])  # Represents 3 - i
z2 = np.array([1, 3])   # Represents 1 + 3i
# Perform the multiplication (z1 * z2)
real_part = z1[0] * z2[0] - z1[1] * z2[1]  # Real part: ac - bd
imaginary_part = z1[0] * z2[1] + z1[1] * z2[0]  # Imaginary part: ad + bc
result = np.array([real_part, imaginary_part])
print("The result of (3 - i)(1 + 3i) is:")
print(f"{result[0]} + {result[1]}i")
# Plotting the complex numbers with lines connecting them to the origin
plt.figure(figsize=(6, 6))
# Plot z1
plt.plot([0, z1[0]], [0, z1[1]], 'r-', alpha=0.5)
plt.plot(z1[0], z1[1], 'ro', label='z1 (3 - i)')
# Plot z2
plt.plot([0, z2[0]], [0, z2[1]], 'b-', alpha=0.5)
plt.plot(z2[0], z2[1], 'bo', label='z2 (1 + 3i)')
# Plot the result
plt.plot([0, result[0]], [0, result[1]], 'g-', alpha=0.5)
plt.plot(result[0], result[1], 'go', label='Result (3 - i)(1 + 3i)')
# Set the axes
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')        
plt.legend()
plt.title('Complex Number Multiplication')
plt.grid(True)
plt.show()
