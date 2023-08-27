import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x, y = sp.symbols("x, y")

points = np.linspace(0,10,150)

def f(x):
    return sp.sin(x)

sol = sp.diff(f(x),x)
print(sol)

arr = sp.lambdify(x, sol)
a = sp.integrate(f(x))
print(a)
plt.plot(points, arr(points))
plt.show()
