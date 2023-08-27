from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import Eq, solve_linear_system, Matrix
from numpy import linalg
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

dx = 0.001
t = np.linspace(0,10,1000)

def g(x):
    return np.e**(-(x+dx)**2)

def f(x):
    d = 0
    d += (np.e**(-(x+dx)**2) - np.e**(-(x)**2))/dx
    return d

def midpoint(a, b, n):
	res = 0
	h = (b - a) / n
	x = a + (h / 2)
	for _ in range(n):
		res += np.e**(-(x)**2)
		x += h
	return h * res

print(midpoint(0,1000,100))

plt.plot(t,f(t))
plt.plot(t,g(t))

plt.show()
print(3/np.sqrt(3*np.pi))