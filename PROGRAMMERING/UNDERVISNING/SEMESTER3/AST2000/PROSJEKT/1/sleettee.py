import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 8.99e9  # Coulomb's constant

# Rod properties
rod_length = 1.0
rod_charge = 1.0e-6

# Grid for plotting
x_vals = np.linspace(-2, 2, 20)
y_vals = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# Calculate electric field components
def electric_field(x, y, rod_charge, rod_length):
    r1 = np.sqrt((x - rod_length/2)**2 + y**2)
    r2 = np.sqrt((x + rod_length/2)**2 + y**2)
    Ex = k * rod_charge * (1/r1**2 - 1/r2**2) * (x - rod_length/2) / r1**3
    Ey = k * rod_charge * (1/r1**2 - 1/r2**2) * y / r1**3
    return Ex, Ey

Ex, Ey = electric_field(X, Y, rod_charge, rod_length)

# Normalize the electric field vectors for arrow plotting
norm = np.sqrt(Ex**2 + Ey**2)
Ex_norm = Ex / norm
Ey_norm = Ey / norm

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
ax.quiver(X, Y, Ex_norm, Ey_norm, norm)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Electric Field of Two Parallel Charged Rods')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Colorbar
cbar = plt.colorbar()
cbar.set_label('Normalized Electric Field Magnitude')

plt.show()
