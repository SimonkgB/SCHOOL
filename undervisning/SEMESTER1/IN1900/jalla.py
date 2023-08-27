import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def f(t):
    return np.cos(t)

x = np.linspace(0, np.pi, 0.1)
sol = solve_ivp(f(x),t_eval=t_eval)

plt.subplot(2,1,1)
plt.plot(sol, x)
plt.subplot(2,1,2)
plt.plot(sol, x)
plt.legend()
plt.show()