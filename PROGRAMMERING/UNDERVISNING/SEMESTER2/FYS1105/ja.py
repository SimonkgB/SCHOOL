import numpy as np
import matplotlib.pyplot as plt

# Define the masses of the planets
m1 = 1
m2 = 2
m3 = 3

# Define the initial positions and velocities of the planets
q0 = np.array([1, 0, 0, 0.5, 0, 0, -1, 0, 0])
v0 = np.array([0, 1, 0, 0, 1.5, 0, 0, -1.5, 0])

# Define the function that calculates the derivatives of q and v
def f(t, y):
    q = y[:9]
    v = y[9:]
    r12 = np.sqrt((q[0]-q[3])**2 + (q[1]-q[4])**2 + (q[2]-q[5])**2)
    r13 = np.sqrt((q[0]-q[6])**2 + (q[1]-q[7])**2 + (q[2]-q[8])**2)
    r23 = np.sqrt((q[3]-q[6])**2 + (q[4]-q[7])**2 + (q[5]-q[8])**2)
    a1 = G * m2 * (q[3]-q[0]) / r12**3 + G * m3 * (q[6]-q[0]) / r13**3
    a2 = G * m1 * (q[0]-q[3]) / r12**3 + G * m3 * (q[6]-q[3]) / r23**3
    a3 = G * m1 * (q[0]-q[6]) / r13**3 + G * m2 * (q[3]-q[6]) / r23**3
    dq = v
    dv = np.array([a1, a1, a1, a2, a2, a2, a3, a3, a3])
    return np.concatenate((dq, dv))

# Define the time step and the duration of the simulation
dt = 0.01
t_max = 10

# Define the gravitational constant
G = 1

# Initialize the arrays for storing the positions and velocities of the planets
q = np.zeros((int(t_max/dt)+1, 3, 3))
v = np.zeros((int(t_max/dt)+1, 3, 3))

# Set the initial positions and velocities
q[0] = np.reshape(q0, (3, 3))
v[0] = np.reshape(v0, (3, 3))

# Perform the simulation using the Runge-Kutta method
for i in range(1, int(t_max/dt)+1):
    k1 = f(i*dt, np.concatenate((q[i-1].flatten(), v[i-1].flatten())))
    k2 = f(i*dt+0.5*dt, np.concatenate((q[i-1].flatten(), v[i-1].flatten()))+0.5*dt*k1)
    k3 = f(i*dt+0.5*dt, np.concatenate((q[i-1].flatten(), v[i-1].flatten()))+0.5*dt*k2)
    k4 = f(i*dt+dt, np.concatenate((q[i-1].flatten(), v[i-1].flatten())))
