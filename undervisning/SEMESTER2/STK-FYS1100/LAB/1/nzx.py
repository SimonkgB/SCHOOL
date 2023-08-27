
import numpy as np


"""
Lasermåler
La = 1196 +- 2 mm
Lb = 1406 +- 2 mm

Meterstokk
La = 1.20
Lb = 1.1955
6 Ledd (?)



Skyvelæret
delta a - b
2 +- 0.05 mm

"""

#B1
ms_Utotal = np.sqrt(6 * 0.5**2 + 0.5**2 + 0.8**2)
print("Meterstokk total usikkerhet [mm]")
print(ms_Utotal)

ms_La = 1.20
ms_Lb = 1.1955
delta_ms = ms_La - ms_Lb
print("Meterstokk delta a - b [m]")
print(delta_ms)

lm_La = 1196
lm_Lb = 1406
delta_lm = abs(lm_La - lm_Lb)
print("Lasermåler delta a - b")
print(delta_lm)

#B2
delta_meterstokk = 2
delta_skyve = 2
delta_a_minus_b = delta_meterstokk - delta_skyve
print("Delta a-b med meterstokk og skyvelære")
print(delta_a_minus_b)
#Usikkerhet meterstokk på delta
delta_msU = np.sqrt(1*0.5**2 + 0.5**2 + 0.8**2)
print("Usikkerhet til meterstokk delta a-b")
print(delta_msU)