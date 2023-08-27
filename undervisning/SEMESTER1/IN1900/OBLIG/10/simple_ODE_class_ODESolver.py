from ODESolver import ForwardEuler
import numpy as np
import matplotlib.pyplot as plt

#c)
        # har forklart hva jeg gjør det som føles ut som 100 ganger før og føler bare at jeg gjentar meg, så skriver ikke overflødisk med kommentarer
f = lambda u, t: 0.2*u
P1 = ForwardEuler(f)        # ForwardEuler er importert fra ODESolver
P1.set_initial_condition(0.1)
t = np.linspace(0, 20, 5)
u,t = P1.solve(t)

# d)
t_exact = np.linspace(0, 20, 400)
exact = 0.1*np.exp(0.2*t_exact)

plt.plot(t,u, "r", label = "Forward metoden")
plt.plot(t_exact,exact, "b", label="exact")
plt.legend()
plt.show()

# jeg legger ikke in for oppgave e i E1 ettersom man bare endrer på variabler 

"""
Terminal> python.exe simple_ODE_class_ODESolver.py
# "Se plot"
"""