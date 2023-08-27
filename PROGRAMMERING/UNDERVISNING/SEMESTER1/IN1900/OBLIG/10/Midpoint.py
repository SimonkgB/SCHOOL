import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler


class ODESolver:
    def __init__(self, f):
        self.f = f

    def advance(self):
        raise NotImplementedError

    def set_initial_condition(self, U0):
        self.U0 = float(U0)

    def solve(self, time_points):
        self.t = np.asarray(time_points)
        N = len(self.t)
        self.u = np.zeros(N)
        self.u[0] = self.U0
        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        return self.u, self.t

class ExplicitMidpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        dt2 = dt/2.0
        k1 = f(u[n], t)
        k2 = f(u[n] + dt2*k1, t[n] + dt2)
        unew = u[n] + dt*k2
        return unew


f = lambda u, t : 0.2*np.cos(t) - t*np.sin(t)
time = np.linspace(0,4*np.pi, 20)



        # har forklart hva jeg gjør det som føles ut som 100 ganger før og føler bare at jeg gjentar meg, så skriver ikke overflødisk med kommentarer
f = lambda u, t: np.cos(t)-t*np.sin(t)
P2 = ForwardEuler(f)        # ForwardEuler er importert fra ODESolver
P2.set_initial_condition(0)
t = np.linspace(0, 4*np.pi, 20)
u,t = P2.solve(t)


t_exact = np.linspace(0,4*np.pi, 20)
g = t_exact*np.cos(t_exact)




P1 = ExplicitMidpoint(f)
P1.set_initial_condition(0)
u2,t2 = P1.solve(time)

plt.plot(t,u, "b", label="Forweard-euler")
plt.plot(t2, u2, "r", label="midpoint")
plt.plot(t_exact,g, "k", label="exact")
plt.legend()
plt.show()

"""
Terminal> python.exe Midpoint.py
# "Se plot"
"""