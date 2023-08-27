import numpy as np
import matplotlib.pyplot as plt

# Define the ODE function
def ode_function(t, y):
    return (y-1)*(y-2)

# Define the range of t and y values
t_range = np.linspace(-1, 5, 20)  # Range of t values
y_range = np.linspace(-1, 5, 20)   # Range of y values

# Create a meshgrid for t and y
t_mesh, y_mesh = np.meshgrid(t_range, y_range)

# Calculate the slopes using the ODE function
slopes = ode_function(t_mesh, y_mesh)

x= np.linspace(0.3,5,100)

def f(x):
    return (np.exp(x)-2)/(np.exp(x)-1)



# Create a slope field plot using streamplot
plt.figure(figsize=(8, 6))
plt.plot(x,f(x))
plt.streamplot(t_mesh, y_mesh, np.ones_like(slopes), slopes, density=1.5)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Slope Field for the ODE dy/dt = y - t^2 + 1')
plt.grid()
plt.show()
