import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the parameters
l1, l2 = 1, 1
m1, m2 = 1, 1
g = 9.81

# Define the initial conditions
theta1_0, theta2_0 = np.pi/4, np.pi/4
omega1_0, omega2_0 = 0, 0

# Define the time range and time step
t_range = (0, 20)
dt = 0.01
t_eval = np.arange(*t_range, dt)

# Define the equations of motion
def equations_of_motion(t, y):
    theta1, theta2, omega1, omega2 = y
    c = np.cos(theta1 - theta2)
    s = np.sin(theta1 - theta2)
    theta1_dot = omega1
    theta2_dot = omega2
    omega1_dot = (m2*g*np.sin(theta2)*c - m2*s*(l1*omega1**2*c + l2*omega2**2) -
                  (m1 + m2)*g*np.sin(theta1)) / (l1*(m1 + m2*s**2))
    omega2_dot = ((m1 + m2)*(l1*omega1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) +
                  m2*l2*omega2**2*s*c) / (l2*(m1 + m2*s**2))
    return theta1_dot, theta2_dot, omega1_dot, omega2_dot

# Solve the equations of motion
y0 = [theta1_0, theta2_0, omega1_0, omega2_0]
sol = solve_ivp(equations_of_motion, t_range, y0, t_eval=t_eval)

# Plot the results
plt.plot(sol.t, sol.y[0], label='theta1')
plt.plot(sol.t, sol.y[1], label='theta2')
plt.legend()
plt.show()
