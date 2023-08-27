import numpy as np
import matplotlib.pyplot as plt

x = 20
v = 0
a = 9.81
t = 0
a = 9.81
g = a
r = 0.39
m = 0.623
p = 1.2 #kg/m**3
d = 0.3 



ar = 4*np.pi*(r)**2


tmax = 10
dt = 0.01




n = int(tmax/dt)

x = np.zeros(n)
v = np.zeros(n)
a = np.zeros(n)
t = np.zeros(n)


# a = g - (1/2*p*D*A*v**2)


v[0] = 0
x[0] = 20

i=0

while i < n - 1 and x[i]>=0:
    a[i] = -g + ((1/2)*p*d*ar*(v[i])**2)/m
    v[i + 1] = v[i] + a[i]*dt
    x[i + 1] = x[i] + v[i]*dt
    t[i + 1] = t[i] + dt
    i += 1
t = t[:i]
a = a[:i]
v = v[:i]
x = x[:i]


plt.subplot(3,1,1)
plt.plot(t,a, "r", label="acceleration")
plt.subplot(3,1,2)
plt.plot(t,v, "y", label="velocity")
plt.subplot(3,1,3)
plt.plot(t,x, "b", label="position")


plt.legend()
plt.show()
