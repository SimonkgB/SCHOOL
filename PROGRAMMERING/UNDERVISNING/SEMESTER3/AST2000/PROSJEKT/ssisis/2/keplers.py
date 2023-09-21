import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import pandas as pd

import sys
sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/2") 
import consts as cs
sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/2") 
import plot_orbits as po


# Example x and y coordinates at two time steps
x_initial, y_initial = cs.initial_conditions[[0],[0,1]]  # initial coordinates
x_final, y_final = po.planets[[0],[0,1]]  # final coordinates

# Calculate r
r_initial = np.sqrt(x_initial**2 + y_initial**2)
r_final = np.sqrt(x_final**2 + y_final**2)

# Calculate theta using arctan2
theta_initial = np.arctan2(y_initial, x_initial)
theta_final = np.arctan2(y_final, x_final)

# Calculate change in theta
delta_theta = theta_final - theta_initial

# Handle angle wrapping
if delta_theta < 0:
    delta_theta += 2*np.pi

print(f"Initial r: {r_initial}, Final r: {r_final}")
print(f"Delta theta: {delta_theta}")
