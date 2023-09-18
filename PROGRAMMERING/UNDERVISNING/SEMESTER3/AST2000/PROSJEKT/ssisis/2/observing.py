
import numpy as np
import os
import csv
import pandas as pd
from numba import jit
import matplotlib.pyplot as plt
import sys

sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/1") 
import consts as cs

sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/2") 
#import orbits as ob
import numpy as np
import matplotlib.pyplot as plt


# Constants
G =cs.GAU  # Gravitational constant (m^3 kg^-1 s^-2)
M_star= cs.conditions[0,0]  # Mass of the star (kg)
M_planet =cs.conditions[1,0]  # Mass of the planet (kg)

# Parameters
peculiar_velocity= 5.0  # Peculiar velocity of the center of mass (m/s)
line_of_sight=0  # Line of sight angle (radians)
inclination=0.001  # Inclination angle (radians)

T= cs.year
N =1000
t =np.linspace(0, T, N)
dt =T/N

v_star =np.zeros(N)

for i in range(N):  # Calculate the velocity of the star
    v_star[i] =20*np.sin(2*np.pi*t[i]/T)

v_star += peculiar_velocity # Add peculiar velocity

# Noise
noise_std_dev =np.max(v_star)/5
noise =np.random.normal(0, noise_std_dev, N)
v_star += noise


v_star_observed =v_star * np.cos(line_of_sight)*np.sin(inclination)# line of sight velocity


plt.figure(figsize=(10, 6))
plt.plot(t, v_star_observed, label='Observed Radial Velocity')
plt.xlabel('Time (yr)')
plt.ylabel('Velocity (AU/yr)')
plt.title('Radial Velocity Curve with Noise')
plt.legend()
plt.show()