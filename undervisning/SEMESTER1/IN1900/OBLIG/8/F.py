import numpy as np
import matplotlib.pyplot as plt
class F:
    def __init__(self, n, m):
        self.n = n
        self.m = m


    def __call__(self,x):
        self.x = x
        return np.sin(self.n*x)*np.cos(self.m*x)

x = np.linspace(0,2*np.pi,1000) 

n = F(1,9)
m = F(9,1)

plt.plot(n(x),m(x))
plt.show()

"""
Terminal> python.exe F.py
Plot
"""