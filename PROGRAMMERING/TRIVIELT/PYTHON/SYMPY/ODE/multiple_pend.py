import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp
from sympy import *

l_1, l_2, m_1, m_2, g = symbols("l_1 l_2 m_1 m_2 g", real=True)
t = symbols("t")
theta_1, theta_2 = symbols("theta_1 theta_2", cls=Function, real=True)

theta_1 = theta_1(t)
theta_2 = theta_2(t)

x_1 = l_1 * sin(theta_1)
y_1 = -l_1 * cos(theta_1)

x_2 = l_1 * sin(theta_1) + l_2 * sin(theta_2)
y_2 = -l_1 * cos(theta_1) - l_2 * cos(theta_2)

sol_x_1 = diff(x_1, t)
sol_y_1 = diff(y_1, t)
sol_x_2 = diff(x_2, t)
sol_y_2 = diff(y_2, t)

T = (1 / 2) * m_1 * ((sol_x_1) ** 2 + (sol_y_1) ** 2) + (1 / 2) * m_2 * ((sol_x_2) ** 2 + (sol_y_2) ** 2)
U = m_1 * g * l_1 * (1 - cos(theta_1)) + m_2 * g * (l_1 * (1 - cos(theta_1)) + l_2 * (1 - cos(theta_2)))
L = T - U

theta_1_diff = diff(theta_1, t)
theta_2_diff = diff(theta_2, t)

dLdtheta_1 = diff(L, theta_1)
dLdtheta_2 = diff(L, theta_2)

dLddtheta_1 = diff(L, theta_1_diff)
dLddtheta_2 = diff(L, theta_2_diff)

dLddtheta_1dt = diff(dLddtheta_1, t)
dLddtheta_2dt = diff(dLddtheta_2, t)

diffl_t1 = dLddtheta_1dt - dLdtheta_1
diffl_t2 = dLddtheta_2dt - dLdtheta_2

solutions = solve([diffl_t1, diffl_t2], [diff(theta_1, t, 2), diff(theta_2, t, 2)])

theta_1_double_diff_func = lambdify((theta_1, diff(theta_1, t), theta_2, diff(theta_2, t), l_1, l_2, m_1, m_2, g), solutions[diff(theta_1, t, 2)])
theta_2_double_diff_func = lambdify((theta_1, diff(theta_1, t), theta_2, diff(theta_2, t), l_1, l_2, m_1, m_2, g), solutions[diff(theta_2, t, 2)])

def pendulum_equations(t, state, l_1, l_2, m_1, m_2, g):
    theta_1, omega_1, theta_2, omega_2 = state
    alpha_1 = theta_1_double_diff_func(theta_1, omega_1, theta_2, omega_2, l_1, l_2, m_1, m_2, g)
    alpha_2 = theta_2_double_diff_func(theta_1, omega_1, theta_2, omega_2, l_1, l_2, m_1, m_2, g)
    return [omega_1, alpha_1, omega_2, alpha_2]

t_span = (0, 40)
t_eval = np.linspace(0, 40, 2000)

l_1, l_2, m_1, m_2, g = 1, 1, 1, 1, 10


n = int(input("input number of pendulums: "))

p = np.zeros((n, 4))
a = np.pi / 2
for i in range(len(p)):
    p[i][0] = np.pi / 2
    p[i][1] = 0
    a += 0.0001
    p[i][2] = np.pi / 2 + a
    p[i][3] = 0

l = np.zeros((n,len(t_eval),4))

for k in range(len(p)):
    state = p[k]
    sol = solve_ivp(pendulum_equations, t_span, state, args=(l_1, l_2, m_1, m_2, g), t_eval=t_eval, method='Radau')
    l[k] = np.array(np.transpose(sol.y))


fig, ax = plt.subplots()  # create a new figure with a default 111 subplot
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
ax.grid()

lines = []
for i in range(n):
    line, = ax.plot([], [], 'o-', lw=2)
    lines.append(line)

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    for k in range(n):
        theta_1 = l[k][i, 0]
        theta_2 = l[k][i, 2]

        x1 = l_1 * np.sin(theta_1)
        y1 = -l_1 * np.cos(theta_1)
        x2 = x1 + l_2 * np.sin(theta_2)
        y2 = y1 - l_2 * np.cos(theta_2)
        lines[k].set_data([0, x1, x2], [0, y1, y2])
    return lines

ani = animation.FuncAnimation(fig, animate, frames=len(l[0]), 
                              interval=8, blit=True, init_func=init)

plt.show()



"""
plt.figure(figsize=(8, 4))



    plt.plot(t_eval, solution[:,0], "b", label=r"$\theta_1$")
    plt.plot(t_eval, solution[:,2], "g", label=r"$\theta_2$")
    plt.plot(t_eval, solution[:,1], "r", label=r"SPPEEED")


plt.xlabel("t")
plt.grid()
plt.show()
"""