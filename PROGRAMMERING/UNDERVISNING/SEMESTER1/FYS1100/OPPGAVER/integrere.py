import numpy as np
import matplotlib.pylab as plt


x0 = 10
v0 = 0
g = 9.81
tmax = 10
dt = 0.01

n = int(tmax/dt)
dth = dt/2

t = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)
a = np.zeros(n)

x[0] = x0
v[0] = v0
a[0] = g
t[0] = 0


for i in range(n-1):
    t[i + 1] = t[i] + dt
    a[i + 1] = x[0]/(2*t[i]**2)
    v[i + 1] = v[i] - a[i]*dt
    x[i + 1] = x[i] + v[i]*dt

    i += 1



plt.plot(t,a, "r", label="acceleration")
plt.subplot(3,1,1)
plt.plot(t,v, "y", label="velocity")
plt.subplot(3,1,2)
plt.plot(t,x, "b", label="position")
plt.subplot(3,1,3)

plt.legend()
plt.show()
