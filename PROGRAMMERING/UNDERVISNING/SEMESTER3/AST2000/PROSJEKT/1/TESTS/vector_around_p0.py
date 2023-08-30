import numpy as np
import scipy.constants as scp_c
import ast2000tools.constants as ast_c

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1")  # Add the directory containing the script
import goated as w 
import rocket_calculations as r_cal
import rocket_capabilities as r_cap

import ast2000tools.utils as utils
seed = utils.get_seed("simm")

from ast2000tools.solar_system import SolarSystem
system = SolarSystem(seed)

from ast2000tools.space_mission import SpaceMission
mission = SpaceMission(seed)



import matplotlib.pyplot as plt

# Constants and initial conditions
G =scp_c.gravitational_constant 
m =r_cap.mass_p0
r0= r_cap.radii0

# Launch phase
r_launch =r0
v_launch =np.sqrt(2*G*m/r0) 

# Orbital phase
r_orbit= r0+r_cap.escape_vel(m, r0)*r_cap.time_to_v_esc
v_orbit =np.sqrt(G*m/r_orbit)

# Time settings
dt =5
t =24*3600
n =int(t/dt)

r_values =np.zeros(n)
theta_values =np.zeros(n)
r_values[0] =r_launch
theta_values[0] =0


for i in range(1, n):
    if r_values[i-1] < r_orbit:
        r_values[i] =r_values[i-1]+v_launch*dt
        v = v_launch
    else:
        r_values[i] =r_orbit
        v =np.sqrt(G*m/+r_values[i-1])

    theta_values[i] =theta_values[i-1]+v*dt/r_values[i-1]

x_values = r_values*np.cos(theta_values)
y_values =r_values*np.sin(theta_values)
plt.figure(figsize=(10, 10))
plt.scatter(0, 0, s =4000)
plt.plot(x_values,y_values)

plt.show()
