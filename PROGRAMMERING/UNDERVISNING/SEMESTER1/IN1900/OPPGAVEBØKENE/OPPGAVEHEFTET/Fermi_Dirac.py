import numpy as np
import matplotlib.pyplot as plt
"""
def Fermi(energy, temp):
    k = 8.6E-5
    eV = 1.6E-19
    mui = 4.74
    keV = k*eV
    muiev = mui*eV
    energyev = energy*eV
    func = (1)/(1+np.exp((energyev-muiev)/keV*temp))
    return func

energy = 10
for i in range(0,energy):
    plt.plot(energy,Fermi(i,0.1))
plt.show()
"""
k = 8.6E-5
eV = 1.6E-19
mui = 4.74
keV = k*eV
muiev = mui*eV

    
for i in range(0,10):
    func = (1)/(1+np.exp((i*eV-muiev)/(keV*0.1)))
print