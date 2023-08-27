import numpy as np
import matplotlib.pyplot as plt

x0 = 0
v0 = 0
t = 0

g = 9.81
k = 1.0
m = 1.0
c = k/m

dt = 0.01
tmax = 8
n = int(tmax/dt)

v = v0
x = x0

x = np.zeros(n)
v = np.zeros(n)
a = np.zeros(n)
t = np.zeros(n)

i = 0
while i < n-1:
    a[i] = g
    v[i + 1] = v[i] + a[i]*dt
    x[i + 1] = x[i] + v[i+1]*dt     # Euler-Cromer
    t[i + 1] = t[i] + dt
    i = i + 1

plt.plot(t,x, "b", label="position")
plt.subplot(3,1,1)
plt.plot(t,v, "y", label="velocity")
plt.subplot(3,1,2)
plt.plot(t,a, "r", label="acceleration")
plt.subplot(3,1,3)

plt.legend()
plt.show()





