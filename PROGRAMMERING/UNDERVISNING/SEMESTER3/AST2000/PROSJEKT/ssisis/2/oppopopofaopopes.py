import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/1")  # HUSK!!!! Add the directory containing the script
import consts as cs

import ast2000tools.constants as ast_c
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem
import ast2000tools.space_mission as sm
seed = utils.get_seed("skgberg_mariutor")
system = SolarSystem(seed)
sam = sm.SpaceMission(seed)

a = sam.star_doppler_shifts_at_sun
print(a)
print(sam.reference_wavelength)
t = np.linspace(0, 2, 15)




















lumin = np.array([1,1,1,0.8,0.6,0.5,0.5,0.5,0.5,0.7,0.8,0.9,1,1,1])

indexx = []
last_one_index = np.where((lumin[:-1] == 1) & (lumin[1:] < 1))[0][-1] # Find the last occurrence of 1 before it drops


first_half_index = np.where(lumin == 0.5)[0][0] # Find the first occurrence of 0.5


last_half_index = np.where(lumin == 0.5)[0][-1] # Find the last occurrence of 0.5


next_one_index = np.where((lumin[last_half_index:] == 1))[0][0] + last_half_index # Find the next occurrence of 1 after the last 0.5

indexx.append(last_one_index)
indexx.append(first_half_index)
indexx.append(last_half_index)
indexx.append(next_one_index)

values = lumin[[last_one_index, first_half_index, last_half_index, next_one_index]] # Extract the values

print("Values:", values)
print("Indexes:", indexx)
print("t:", t[indexx])
print("speed", (lumin[indexx[1]] - lumin[indexx[0]]) / (t[indexx[1]] - t[indexx[0]])) # 2R = v*t
