import numpy as np
import os
import csv
import pandas as pd
from numba import jit
import matplotlib.pyplot as plt
import sys
import time

sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/1") 
import consts as cs
import ast2000tools.utils as utils

start_time = time.time() 

G =4*np.pi**2
M =cs.mass_sun
dt =0.001
years =1.28394067*3    # 3 years    INDEX = 128394067
N =int(years/dt)
initial_conditions =cs.initial_conditions[0]
csv_file_name ="plotting_orbits_p0.csv"

@jit(nopython=True)
def calculate_orbit(N, dt, initial_conditions, G, M):
    results =np.zeros((N, 4))
    x, y, vx, vy =initial_conditions
    for i in range(N):
        r =np.sqrt(x**2 + y**2)

        ax =-G*M*x/r ** 3
        ay =-G*M*y/r ** 3

        vx +=ax*dt
        vy +=ay*dt

        x +=vx*dt
        y +=vy*dt

        results[i] =[x, y, vx, vy]
        
    return results

def write_to_csv():
    results =calculate_orbit(N, dt, initial_conditions, G, M)
    with open(csv_file_name, "w", newline="") as f:
        writer =csv.writer(f)
        headers =["TimeStep", "Planet_0_x", "Planet_0_y", "Planet_0_vx", "Planet_0_vy"]
        writer.writerow(headers)
        for i in range(N):
            row =[i*dt]
            row.extend(results[i])
            writer.writerow(row)

def plot_from_csv(df):
    plt.figure(figsize=(10, 10))
    plt.plot(df["Planet_0_x"], df["Planet_0_y"], label="Planet 0")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Orbit of Planet 0")
    plt.legend()
    plt.grid(True)
    plt.show()

if os.path.exists(csv_file_name):
    print("CSV file exists. Plotting data.")
    df =pd.read_csv(csv_file_name)
    df =df.iloc[:, 1:]  # Skip the first column
    #plot_from_csv(df)
else:
    print("CSV file does not exist. Running integration.")
    write_to_csv()
    print("Integration complete. Plotting data.")
    df =pd.read_csv(csv_file_name)
    df =df.iloc[:, 1:]  # Skip the first column
    plot_from_csv(df)

"""
#Code for finding the year
a1 =initial_conditions[0]
a2 =np.array(df["Planet_0_x"].astype(float))
b1 =initial_conditions[1]
b2 =np.array(df["Planet_0_y"].astype(float))
a =0
tol =0.000000040  # set tolerance
print(utils.AU_to_m(tol))
for i in range(128_390_000,128_400_000):
    if abs(a1 - a2[i]) < tol and abs(b1 - b2[i]) < tol:
        index =i
        a += 1
        print(index)
print(a)

#index = 128394067
#print(dt*index)"""

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")

# calcualte energy from the csv file

