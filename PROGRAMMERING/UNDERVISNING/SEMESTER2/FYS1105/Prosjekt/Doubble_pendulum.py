import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the initial conditions
theta1_0 = np.pi / 2
theta2_0 = np.pi / 2
theta3_0 = np.pi / 2
omega1_0 = 0
omega2_0 = 0
omega3_0 = 0

# Set up the physical parameters
g = 9.81
m1 = 1
m2 = 1
m3 = 1
L1 = 1
L2 = 1
L3 = 1

# Define the system of ODEs
def f(t, y):
    theta1, theta2, theta3, omega1, omega2, omega3 = y
    
    dtheta1_dt = omega1
    dtheta2_dt = omega2
    dtheta3_dt = omega3
    
    domega1_dt = (-g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * m2 * (omega2 ** 2 * L2 + omega1 ** 2 * L1 * np.cos(theta1 - theta2))) / (L1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))
    domega2_dt = (2 * np.sin(theta1 - theta2) * (omega1 ** 2 * L1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + omega2 ** 2 * L2 * m2 * np.cos(theta1 - theta2))) / (L2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))
    domega3_dt = (2 * np.sin(theta2 - theta3) * (omega2 ** 2 * L2 * (m2 + m3) + g * (m2 + m3) * np.cos(theta2) + omega3 ** 2 * L3 * m3 * np.cos(theta2 - theta3))) / (L3 * (2 * m2 + m3 - m3 * np.cos(2 * theta2 - 2 * theta3)))
    
    return [dtheta1_dt, dtheta2_dt, dtheta3_dt, domega1_dt, domega2_dt, domega3_dt]

# Solve the system of ODEs
y0 = [theta1_0, theta2_0, theta3_0, omega1_0, omega2_0, omega3_0]
t_span = [0, 5]
sol = solve_ivp(f, t_span, y0, max_step=0.05)

# Compute x and y coordinates of the pendulum
theta1 = sol.y[0]
theta2 = sol.y[1]
theta3 = sol.y[2]

x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)

x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

x3 = x2 + L3 * np.sin(theta3)
y3 = y2 - L3 * np.cos(theta3)

fig, ax = plt.subplots()

# Set up the plot
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
line, = ax.plot([], [], lw=2)

# Define the initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Define the update function for the animation
def update(i):
    line.set_data([0, x1[i], x2[i], x3[i]], [0, y1[i], y2[i], y3[i]])
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(sol.t), init_func=init, blit=True, interval=0.1)

plt.show()
