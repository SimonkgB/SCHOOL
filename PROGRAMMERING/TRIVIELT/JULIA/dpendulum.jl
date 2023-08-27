using Plots
using DifferentialEquations



l1, l2 = 1, 1
m1, m2 = 1, 1
g = 9.81

theta1_0, theta2_0 = π/4, π/4
omega1_0, omega2_0 = 0, 0

# Define the time range and time step
t_range = (0, 20)
dt = 0.01