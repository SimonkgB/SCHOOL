import numpy as np
import matplotlib.pyplot as plt


class ForwardEuler_v1:                  # kopierer inn classen fra en bok
    def __init__(self, f, U0, T, N):    # konstruktør 
        self.f, self.U0, self.T, self.N = f, U0, T, N       # attributter
        self.dt = T/N
        self.u = np.zeros(self.N+1)     # array med N+1 antall 0'er
        self.t = np.zeros(self.N+1)

    def solve(self):    #funksjon for å løse diff likningen
        self.u[0] = float(self.U0)  # initial betingelsen
        for n in range(self.N):
            self.n = n
            self.t[n+1] = self.t[n] + self.dt
            self.u[n+1] = self.advance()
        return self.u, self.t

    def advance(self):
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t
        unew = u[n] + dt*f(u[n], t[n])
        return unew

#c)
f = lambda u, t: 0.2*u
P1 = ForwardEuler_v1(f, 0.1, 20, 5) # setter in variabler
u,t = P1.solve()

#d)
t_exact = np.linspace(0, 20, 400)   # eksakt verdi
exact = 0.1*np.exp(0.2*t_exact)

plt.plot(t, u, "r", label="numerical")   # plotter
plt.plot(t_exact, exact, "b", label="exact")
plt.legend()
plt.show()

# jeg legger ikke in for oppgave e i E1 ettersom man bare endrer på variabler 



"""
Terminal> python.exe Simple_ODE_class.py
# "Se plot"
"""