import numpy as np
import matplotlib.pyplot as plt
def f(x):
    k = 1
    a = k*np.exp(-(1)/(1-x**2))
    return a
k = np.linspace(-2,2)
x = np.linspace(-1,1)
plt.plot(k,f(x))
plt.show()