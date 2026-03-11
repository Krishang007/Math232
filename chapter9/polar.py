#complex numbers
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
   


# define using Euler identity to get exact √ form


z_sym = 2 * (sp.cos(sp.pi/4) + sp.I * sp.sin(sp.pi/4))

# simplify to rectangular form with √ symbols
z_rect = sp.simplify(z_sym)

# modulus and argument (symbolic)
r_sym = sp.Abs(z_sym)
theta_sym = sp.arg(z_sym)

print("The complex number z =")
sp.pprint(z_rect)

print("The modulus |z| =")
sp.pprint(r_sym)

print("The argument θ of z =")
sp.pprint(theta_sym)

# convert to numeric values for plotting
z = complex(z_rect.evalf())
r = abs(z)
theta = np.angle(z)

# Plot the complex number in polar form
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r, 'ro', label=f'z = {z.real:.2f} + {z.imag:.2f}i')
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted point
ax.grid(True)
ax.set_title('Polar Plot of Complex Number z')
ax.legend()
plt.show()
