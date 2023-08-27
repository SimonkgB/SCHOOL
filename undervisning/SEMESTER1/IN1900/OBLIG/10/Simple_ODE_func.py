# a) u' = 0.2 * u , separabel difflikning

# b)
def f(u,t):
    return 0.2 * u          # funksjonen 


# c) / d)
import numpy as np
import matplotlib.pyplot as plt



def ForwardEuler(f, u0, T, N):      # bruker ForwardEuler fra forelesningen
    t = np.zeros(N+1)       # lager en array med nuller med andtall N+1
    u = np.zeros(N+1)       
    u[0] = u0           # setter initialbetingelsen  = u0
    t[0] = 0
    dt = T/N            # unbrukelig å ha ettersom den første allerede er satt som 0
    for n in range(N):
        t[n+1] = t[n] + dt      # den faktiske euler metoden    
        u[n+1] = u[n] + dt*f(u[n], t[n])
    return u, t 


u,t = ForwardEuler(f, u0=0.1, T=20, N=5)     # setter in variablene i Funksjonen forwardeuler

exact = 0.1*np.exp(0.2*t)   # den faktiske verdien til den deriverte

plt.plot(t,u, "r", label = "Forward metoden")
plt.plot(t,exact, "b", label =" den eksakte verdien")

#e)

# ved å endre på N får man enten en mer nøyaktig  eller en mer unøyaktig verdi, høyere N gir mer eksakt verdi
u,t = ForwardEuler(f, u0=0.1, T=20, N=3)
plt.plot(t,u, "k", label = "Større dt verdi")
u,t = ForwardEuler(f, u0=0.1, T=20, N=1000)
plt.plot(t,u, "g", label ="Lavere dt verdi")

# som man kan se så ser man at den laver dt verdien følger den eksakte verdien nesten helt korrekt
# samtidig man ser hvor unnøyaktige de lave verdiene er 

plt.legend()
plt.show()




"""
Terminal> python.exe class_dif.py
# "Se plot"
"""