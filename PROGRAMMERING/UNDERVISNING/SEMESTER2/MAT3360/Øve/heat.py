import numpy as np
import matplotlib.pyplot as plt

# Define the physical parameters
L = 1 # Length of the rod
T = 1 # Total time of simulation
k = 1 # Thermal conductivity
c = 1 # Specific heat capacity
rho = 1 # Density
alpha = k/(c*rho) # Thermal diffusivity
dx = 0.1 # Spatial step
dt = 0.01 # Time step
N = int(L/dx) # Number of spatial grid points
M = int(T/dt) # Number of time grid points

# Initialize the temperature distribution
T = np.zeros((N, M))

# Set the boundary conditions
T[0, :] = 0
T[N-1, :] = 0

# Set the initial condition
T[:, 0] = np.sin(np.pi*np.linspace(0, 1, N))

# Define the finite difference coefficients
a = alpha*dt/dx**2
b = 1 - 2*a

# Solve the heat equation using the finite difference method
for j in range(1, M):
    for i in range(1, N-1):
        T[i, j] = a*T[i-1, j-1] + b*T[i, j-1] + a*T[i+1, j-1]

# Plot the temperature distribution
x = np.linspace(0, L, N)
t = np.linspace(0, T, M)
X, T = np.meshgrid(x, t)
fig = plt.figure(figsize=(8, 6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, T, T.T, cmap='coolwarm')
ax.set_xlabel('Distance')
ax.set_ylabel('Time')
ax.set_zlabel('Temperature')
plt.show()
