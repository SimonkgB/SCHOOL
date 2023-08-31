import numpy as np

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED")  # Add the directory containing the script
import goated as w 
import rocket_calculations as r_cal
import rocket_capabilities as r_cap
import consts as cs 


import matplotlib.pyplot as plt

# Constants and initial conditions
G =cs.Gc
m =cs.mass_p0
r0= cs.radius_p0

# Launch phase
v_launch =np.sqrt(2*G*m/r0) 

# Orbital phase
r_orbit= r0+r_cap.escape_vel(m, r0)*cs.time_to_v_esc
v_orbit =np.sqrt(G*m/r_orbit)

# Time settings
dt =5
t =24*3600
n =int(t/dt)

r_values =np.zeros(n)
theta_values =np.zeros(n)
r_values[0] = r0
theta_values[0] =0


def eliptical_orbit(theta_v, a, b):
    e = np.sqrt(1-(b/a)**2)
    p = a*(1-e**2)
    r = p/(1+e*np.cos(theta_v))
    return r
theta = np.linspace(0,2*np.pi, 1000)

x = eliptical_orbit(theta, 10, 5)*np.cos(theta)
y = eliptical_orbit(theta, 10, 5)*np.sin(theta)

plt.plot(x,y)
plt.scatter(0,0,color="r")
plt.show()

"""
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
"""
"""
plt.figure(figsize=(10, 10))
plt.scatter(0, 0, s =66500)
plt.plot(x_values,y_values, color="r")

plt.show()
"""