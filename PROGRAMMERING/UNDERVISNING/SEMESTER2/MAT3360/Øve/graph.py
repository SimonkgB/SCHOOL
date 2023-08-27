import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 2*np.pi*2, 0.008)


def f(g):
    y = 0
    for k in range(1,g):
        y += (2*np.sin(2*k*x))/(2*k)
    return y





plt.plot(x,f(100), "b", label="graph")
plt.legend()
plt.show()