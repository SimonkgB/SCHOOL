import numpy as np
import matplotlib.pyplot as plt

# Define constants
g = 9.81  # acceleration due to gravity (m/s^2)
L1 = 1.0  # length of first pendulum (m)
L2 = 1.0  # length of second pendulum (m)
m1 = 1.0  # mass of first pendulum (kg)
m2 = 1.0  # mass of second pendulum (kg)

# Define initial conditions
theta1_0 = np.pi  # initial angle of first pendulum (rad)
theta2_0 = np.pi  # initial angle of second pendulum (rad)
omega1_0 = 0.0  # initial angular velocity of first pendulum (rad/s)
omega2_0 = 0.0  # initial angular velocity of second pendulum (rad/s)

# Define time step and duration of simulation
dt = 0.01  # time step (s)
t_max = 100.0  # duration of simulation (s)
n_steps = int(t_max/dt)  # number of time steps

# Define arrays to store results
t = np.zeros(n_steps)  # time array
theta1 = np.zeros(n_steps)  # angle of first pendulum array
theta2 = np.zeros(n_steps)  # angle of second pendulum array

# Define function to calculate derivatives
def derivatives(state, t):
    theta1, theta2, omega1, omega2 = state
    
    dtheta1_dt = omega1
    dtheta2_dt = omega2
    
    domega1_dt = (-g*(2*m1 + m2)*np.sin(theta1) - m2*g*np.sin(theta1 - 2*theta2) - 2*np.sin(theta1 - theta2)*m2*(omega2**2*L2 + omega1**2*L1*np.cos(theta1 - theta2))) / (L1*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2)))
    domega2_dt = (2*np.sin(theta1 - theta2)*(omega1**2*L1*(m1 + m2) + g*(m1 + m2)*np.cos(theta1) + omega2**2*L2*m2*np.cos(theta1 - theta2))) / (L2*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2)))
    
    return [dtheta1_dt, dtheta2_dt, domega1_dt, domega2_dt]

# Set initial state
state = [theta1_0, theta2_0, omega1_0, omega2_0]

# Perform simulation using Euler-Chromer method
for i in range(n_steps):
    t[i] = i*dt
    
    # Calculate derivatives at current state
    derivs = derivatives(state, t[i])
    
    # Update state using Euler-Chromer method
    state[0] += derivs[0]*dt
    state[1] += derivs[1]*dt
    state[2] += derivs[2]*dt
    state[3] += derivs[3]*dt
    
    # Store results
    theta1[i] = state[0]
    theta2[i] = state[1]

# Plot results
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

ax1.plot(t, theta1, 'b-', label='Pendulum 1')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Angle (rad)')
ax1.legend()

ax2.plot(t, theta2, 'r-', label='Pendulum 2')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Angle (rad)')
ax2.legend()

plt.show()