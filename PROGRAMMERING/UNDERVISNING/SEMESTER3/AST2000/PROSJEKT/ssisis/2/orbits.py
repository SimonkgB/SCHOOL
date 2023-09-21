import numpy as np
import csv
import pandas as pd
from numba import jit
import matplotlib.pyplot as plt
import sys

sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/1") 
import consts as cs


G =cs.GAU
M =cs.mass_sun
dt =1e-05   # og dt 0.00000001
years =cs.year    # 20 years  # /approx 1.28394067 1 year  INDEX = 128394067
N =int(years/dt)
initial_conditions =cs.initial_values  # Assuming this is a 2D array
num_planets =len(initial_conditions)
csv_file_name ="plotting_orbits_p0.csv"


@jit(nopython=True)
def calculate_orbit(N, dt, initial_conditions, G, M, num_planets):
    results =np.zeros((N, num_planets, 4))
    planets =np.copy(initial_conditions)
    for i in range(N):
        for j in range(num_planets):
            x, y, vx, vy =planets[j]

            r =np.sqrt(x**2+y**2)

            ax =-G*M*x/r**3
            ay =-G*M*y/r**3

            vx +=ax*dt
            vy +=ay*dt

            x +=vx*dt
            y +=vy*dt

            planets[j]=[x, y, vx, vy]
        results[i]=planets
    return results

def write_to_csv():
    results =calculate_orbit(N, dt, initial_conditions, G, M, num_planets)
    with open(csv_file_name, "w", newline="") as f:
        writer =csv.writer(f)
        headers =["TimeStep"]
        for i in range(num_planets):
            headers.extend([f"Planet_{i}_x", f"Planet_{i}_y", f"Planet_{i}_vx", f"Planet_{i}_vy"])
        writer.writerow(headers)
        for i in range(N):
            row =[i*dt] 
            row.extend(results[i].flatten())
            writer.writerow(row)





"""
#Code for finding the year
a1 =cs.initial_conditions[0,0]
a2 =np.array(df.iloc[:, 1].astype(float))
b1 =cs.initial_conditions[0,1]
b2 =np.array(df.iloc[:, 2].astype(float))
a =0
tol =0.000001  # set tolerance
print(us.AU_to_m(tol))
for i in range(len(a2)):
    if abs(a1 - a2[i]) < tol and abs(b1 - b2[i]) < tol:
        index =i
        a += 1
        print(index)
print(a)
"""