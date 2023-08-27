import numpy as np
import matplotlib.pyplot as plt

tmax = 10
dt = 0.05
n = int(tmax/dt)
t = np.zeros(n)
xrad = np.zeros(n)
vrad = np.zeros(n)
arad = np.zeros(n)


xrad = np.pi/4 # rad/s
l = 1 # m
g = 9.81 # m/s**2
m = 3 # kg
b = 0.5 # kg/s
G = m*g


t[0] = 0
xrad[0] = 3.14
vrad[0] = 0
arad[0] = 0

# rad/t[i]  


i = 0

while i < n-1:
    Fd = -b*vrad[i]
    arad[i+1] = (G + Fd) / m
    vrad[i+1] = rad/t[i] + arad[i]/(rad[i])**2 * dt
    xrad[i+1] = xrad[i] + vrad[i+1] * dt
    t[i+1] = t[i] + dt
    i += 1

plt.plot(t,x)
plt.plot(t,v)
plt.plot(t,a)
plt.show()