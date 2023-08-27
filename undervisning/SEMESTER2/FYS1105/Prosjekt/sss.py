import numpy as np
import matplotlib.pyplot as plt

# Define the constants
m1 = 1
m2 = 1
l1 = 1
l2 = 2
g = 9.81

# Define the initial conditions
theta_0 = np.pi/4
phi_0 = np.pi/6
dtheta_0 = 0
dphi_0 = 0
y0 = np.array([theta_0, phi_0, dtheta_0, dphi_0])

# Define the time step and the time span of the simulation
T = 100
dt = 0.001
t = np.arange(0, T+dt, dt)

# Define the matrix b
b = np.array([[m2*l2**2, m2*l2*l1*np.cos(theta_0-phi_0)], [m2*l1*l2*np.cos(theta_0-phi_0), m2*l1**2]])

# Define the function f(y, t) that describes the differential equation
def f(y, t):
    theta, phi, dtheta, dphi = y
    dd = np.linalg.solve(b, np.array([-m2*l1*l2*dphi*np.sin(theta-phi)*(dphi-dtheta)-m2*l1*l2*dtheta*dphi*np.sin(theta-phi)-(m1+m2)*g*l1*np.sin(theta), -m2*l1*l2*dtheta*np.sin(theta-phi)*(dtheta-dphi)+m2*l1*l2*dtheta*dphi*np.sin(theta-phi)-m2*g*l2*np.sin(phi)]))
    return np.array([dtheta, dphi, dd[0], dd[1]])

# Use the Euler-Chromer method to solve the differential equation
y = np.zeros((len(t), 4))
y[0, :] = y0
for i in range(len(t)-1):
    y[i+1, :] = y[i, :] + dt * f(y[i, :], t[i])

# Plot the results
plt.plot(t, y[:, 0], label='theta')
plt.plot(t, y[:, 1], label='phi')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.show()
