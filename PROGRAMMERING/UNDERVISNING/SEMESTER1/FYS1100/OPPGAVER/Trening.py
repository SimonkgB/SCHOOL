import numpy as np
import matplotlib.pyplot as plt
# Simons fantasi land med egenene fysiske regler

x0 = 0
v0 = 40
g = 10
cd = 0.5
r = 3
ar = np.pi*r**2
k = 0.23
dt = 0.01
tmax = 10
f0 = 400
m = 30



n = int(tmax/dt)

t = np.zeros(n)
a = np.zeros(n)
v = np.zeros(n)
x = np.zeros(n)


a[0] = g
v[0] = v0
x[0] = x0

i = 0

while i < n - 1 and x[i]>=0:
    a[i] = -g + k*v[i]/m
    v[i + 1] = v[i] + a[i]*dt
    x[i + 1] = x[i] + v[i]*dt
    t[i + 1] = t[i] + dt
    i += 1
t = t[:i]
a = a[:i]
v = v[:i]
x = x[:i]


plt.subplot(3,1,1)
plt.plot(t,a, "r", label="a(t)")
plt.xlabel("tid/[s]")
plt.ylabel("akselerasjon/[m/s**2]")
plt.subplot(3,1,2)
plt.plot(t,v, "b", label="v(t)")
plt.xlabel("tid/[s]")
plt.ylabel("hastighet/[m/s]")
plt.subplot(3,1,3)
plt.plot(t,x, "g", label="y(t)")
plt.xlabel("tid/[s]")
plt.ylabel("posisjon/[m]")

plt.legend()
plt.show()

