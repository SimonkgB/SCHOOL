import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, x):
    dydx = 3 * x**2 * (y**2 + 1)
    return dydx

# Initial condition
y0 = 0

# Create an array of x values
x = np.linspace(-1, 1, 100)

# Solve the ODE
y = odeint(model, y0, x)

# Plot the solution
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of dy/dx = 3*x**2 * (y**2 + 1)')
plt.grid(True)
plt.show()
