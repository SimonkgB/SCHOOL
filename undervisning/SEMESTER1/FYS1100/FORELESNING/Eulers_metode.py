from this import d
import numpy as np
import matplotlib.pyplot as plt

x0 = 1
dt = 0.001
tMax = 50

n = int(tMax/dt)
t = np.zeros(n)
dx = np.zeros(n)
x = np.zeros(n)

x[0] = x0
t[0] = 0

for i in range(n-1):
    t[i+1] = t[i] + dt
    dx[i] = np.cos(t[i])*x[i]
    x[i+1] = x[i] + dx[i]*dt

plt.plot(t,x)
plt.plot(t,x0*np.exp(np.sin(t)))
plt.show()