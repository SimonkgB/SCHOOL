import numpy as np
import matplotlib.pyplot as plt
def f(x,N):     # lager en funskjon
    k = 1
    s = 0
    for k in range(k,N+1):              # lager en range fra 1 til variabelen N
        s += np.cos((2*k-1)*x)/(2*k-1)**2   # summeringadelen av funksjonen
    f = (np.pi/2) - (4/np.pi)*s             # resten av funksjonen
    return f

x = np.linspace(-np.pi, np.pi, 100)     # lager en arrey med 100 verdier mellom -pi og pi
N=4
for N in range(1,N+1):      # for å få riktig antall 
    y = f(x,N)
    plt.plot(x,y, label = f"N = {N}")   # plotter in tallene i grafen og gir de navn
plt.legend()
plt.xlabel("x")     # navngir x grafen
plt.ylabel("y")     # navngir y grafen
plt.show()          # viser grafen



 
# [a, b] = [-np.pi, np.pi]