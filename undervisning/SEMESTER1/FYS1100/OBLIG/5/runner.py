import numpy as np
import matplotlib.pyplot as plt


def plot(v0=0, x0=0, m=80, f=400, p=1.293, ar=0.45, cd=1.2, w=0, dt=0.01, tmax=10):
    n = int(tmax / dt) + 1
    x = np.zeros(n + 1)
    v = np.zeros(n + 1)
    d = np.zeros(n + 1)
    t = np.zeros(n + 1)
    
    i = 0
    d[0] = 0
    v[0] = v0
    x[0] = x0
    t[0] = 0
    
    
    while i < n:
        a = (f-d)/m
        v[i + 1] = v[i] + a * dt
        x[i + 1] = x[i] + v[i + 1] + a * dt
        d[i + 1] = 1/2 * p * cd * ar * (v[i]-w)**2
        t[i + 1] = i * dt + t[0]
        i += 1
    plt.subplot(3,1,1)
    plt.plot(t, a, label="Acceleration")
    plt.xlabel("t [s]")
    plt.ylabel("a(t) [m/s**2]")
    plt.title("oppgave e")

    plt.subplot(3,1,2)
    plt.plot(t, v, label="Velocity")
    plt.xlabel("t [s]")
    plt.ylabel("v(t) [m/s]")

    plt.subplot(3,1,3)
    plt.plot(t,x, label="postion")
    plt.xlabel("t [s]")
    plt.ylabel("x(t) [m]")

    plt.legend()
    plt.show()

plot()