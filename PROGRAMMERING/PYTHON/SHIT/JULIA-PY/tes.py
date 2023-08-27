



# Importing the necessary Julia packages

def exponential_growth(du, u, p, t):
    aa = p
    du[1] = aa * u[1]


# Set initial condition, parameter, and time span
u0 = [1.0]
tspan = (0.0, 5.0)
aa = 0.5

# Call Julia's solver from Python






"""

# Now, you can use 't' and 'u' in Python, for example, to plot the solution.

import matplotlib.pyplot as plt

u_values = [val[0] for val in u]

plt.plot(t, u_values, label=f'aa={aa}')
plt.legend()
plt.xlabel('Time')
plt.ylabel('u(t)')
plt.title('Exponential Growth')
plt.show()
"""