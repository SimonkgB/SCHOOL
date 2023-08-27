import numpy as np


def f(x):            # lager en funksjon
    y = np.sin(x)   
    return y

def fd(x):
    y = np.cos(x)
    return y

x = [3.14, 0, 0]    # ettersom man senere har en range som går til 3, må man ha 3 verdier i lista
print(x[0])     # printer første verdi i lista

for n in range(1,3):        
    x[n] = x[n-1]-(f(x[n-1])/fd(x[n-1]))        # funksjonen der man setter in n verdier man får i rangen
    print(x[n])

print(f"{np.pi:1.13f}")     # printer pi  med 13 decimaler 

"""
Terminal> python.exe finding_pi.py
3.14
3.1415926549364075
3.141592653589793
3.1415926535898
"""