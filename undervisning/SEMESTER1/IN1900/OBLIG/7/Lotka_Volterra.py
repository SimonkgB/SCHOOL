import numpy as np
import matplotlib.pyplot as plt


n = 500
a = 0.04
b = 0.1
c = 0.005
e = 0.2
R_0 = 100
F_0 = 20
def Lotka_Volterra(R_0, F_0, n, a, b, c, e):    # lager en funksjon med mange variabler 

    R = np.zeros(n) # lager en liste med numpy med n antall nuller 
    F = np.zeros(n) # -----------""----------------------------

    R[0] = R_0  # sier at R_0 er R[0] og stter det som startpunkt
    F[0] = F_0  # ---------------------""------------------

    for i in range(0,n-1):  #for loop fra 0 til n-1
         R[i+1] = R[i] + a*R[i] - c*R[i]*F[i]   # bruker euler-crommer
         F[i+1] = F[i] + e*c*R[i]*F[i] - b*F[i]
    return R,F

t = np.linspace(0,n,500)

R, F = Lotka_Volterra(R_0, F_0, n, a, b, c, e)
plt.plot(t,R,"b-",t,F,"r-") # plotter en graf
plt.legend(["Rabbit","Fox"])    
plt.title("Rabbit and Fox population")      # navn på graf
plt.show()  # viser grafen

"""
Terminal> python.exe atm_moon.py
"""