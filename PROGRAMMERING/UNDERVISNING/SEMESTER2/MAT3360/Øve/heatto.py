import numpy as np
import matplotlib.pyplot as plt

# Set the parameters
L = 1        # length of the rod
T = 0.6        # total time
alpha = 1    # thermal diffusivity
n = 10       # number of terms in the series

# Define the initial condition
def initial_condition(x):
    return np.sin(3*np.pi*x)

# Define the boundary conditions
def boundary_condition(t):
    return 0

# Set the number of points in the spatial and temporal grids
N = 500   # number of spatial points
M = 90  # number of temporal points

# Set the spatial and temporal steps
dx = L/(N-1)
dt = T/(M-1)

# Set up the spatial and temporal grids
x = np.linspace(0, L, N)
t = np.linspace(0, T, M)

# Set up the solution array
u = np.zeros((N, M))

# Set the initial condition
u[:, 0] = initial_condition(x)

# Compute the coefficients
c = np.zeros(n)
for i in range(n):
    c[i] = 2/L*np.trapz(u[:, 0]*np.sin((i+1)*np.pi*x/L), x)

# Compute the solution
for k in range(1, M):
    for i in range(n):
        u[:, k] += c[i]*np.sin((i+1)*np.pi*x/L)*np.exp(-alpha*(i+1)**2*np.pi**2/L**2*t[k])
    u[0, k] = boundary_condition(t[k])
    u[-1, k] = boundary_condition(t[k])

    # Animate the plot
    plt.clf()
    plt.plot(x, u[:, k])
    plt.xlabel('x')
    plt.ylabel('u')
    plt.ylim(0, 1)
    plt.title('Temperature Distribution at t = {:.2f}'.format(t[k]))
    plt.pause(0.02)

# Show the final plot
plt.show()
