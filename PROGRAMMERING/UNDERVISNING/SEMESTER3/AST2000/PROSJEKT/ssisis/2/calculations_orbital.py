
import numpy as np
import os
import csv
import pandas as pd
from numba import jit
import matplotlib.pyplot as plt
import sys
import time

sys.path.append("C:/Users/simon/Skrivebord/ssisis/1") 
import consts as cs

sys.path.append("C:/Users/simon/Skrivebord/ssisis/2") 
import orbits as ob

start_time =time.time() 





G = cs.GAU
M = cs.mass_sun

csv_file_name ="plotting_orbits_1.csv"
df =pd.read_csv(csv_file_name)



@jit(nopython=True)
def calculate_energy(df):
    x =np.array(df["Planet_0_x"].astype(float))
    y =np.array(df["Planet_0_y"].astype(float))
    vx =np.array(df["Planet_0_vx"].astype(float))
    vy =np.array(df["Planet_0_vy"].astype(float))
    r =np.sqrt(x**2 + y**2)
    v =np.sqrt(vx**2 + vy**2)
    E =0.5*v**2 - G*M/r
    return E
# plot energy
def plot_energy(df):
    E =calculate_energy(df)
    plt.plot(df["TimeStep"], E)
    plt.xlabel("Time [years]")
    plt.ylabel("Energy [AU^2/year^2]")
    plt.title("Energy of Planet 0")
    plt.grid(True)
    plt.show()


@jit(nopython=True)
def calculate_area(r1, theta1, r2, theta2):
    return 1/2*(r1**2+r2**2)*np.abs(theta2-theta1)

@jit(nopython=True)
def calculate_distance(r, delta_theta):
    return r*delta_theta

@jit(nopython=True)
def calculate_mean_velocity(distance, delta_t):
    return distance/delta_t

@jit(nopython=True)
def third_law(a, T):
    if np.abs(T**2- a**3/cs.mass_sun)<=1e-5:
        return True
    else:
        return False  

def year_per_planet(major_axis,mass_planet):
    return np.sqrt((4*np.pi**2 * major_axis**3)/(cs.GAU*(cs.mass_sun+mass_planet)))
year_per_planet =year_per_planet(cs.a_axis, cs.mass_planets)

# set r1, theta1, r2, theta2
def kk(a,b):
    r1 = np.sqrt(df.iloc[a, 1]**2 + df.iloc[a, 2]**2)
    r2 = np.sqrt(df.iloc[b, 1]**2 + df.iloc[b, 2]**2)

    theta1 = np.arctan2(df.iloc[a, 2], df.iloc[a, 1])
    theta2 = np.arctan2(df.iloc[b, 2], df.iloc[b, 1])
    return r1, r2, theta1, theta2

dt = ob.dt
k_0 = int((cs.year/dt))   # 1 year in the whole systems dt
perhelion = int(k_0/2)
aphelion = 0
a_perhelion, b_perhelion = perhelion, perhelion+100
a_aphelion, b_aphelion = aphelion, aphelion+100
#print(b_0-a_0/k_0)    # time in years

r1, r2, theta1, theta2 = kk(a_perhelion, b_perhelion)
area_per = calculate_area(r1, theta1, r2, theta2)
r1, r2, theta1, theta2 = kk(a_aphelion, b_aphelion)
area_aph = calculate_area(r1, theta1, r2, theta2)

print(f"Area swept out close to perhelion: {area_per} AU^2")
print(f"Area swept out close to aphelion: {area_aph} AU^2")
# Calculate distance
distance = calculate_distance(r1, np.abs(theta2 - theta1))
print(f"Distance traveled between t1 and t2: {distance} AU")

# Calculate mean velocity
mean_velocity = calculate_mean_velocity(distance, dt)
print(f"Mean velocity between t1 and t2: {mean_velocity} AU/yr")

# Check Kepler's 3rd law
a = cs.a_axis[cs.home_planet_idx]  # semi-major axis in AU
T = cs.year  # period in years
print(f"Is the orbit consistent with Kepler's 3rd law? {third_law(a, T)}")


if os.path.exists(csv_file_name):
    print("CSV file exists. Running program.")
    #df =pd.read_csv(csv_file_name)
    #plot_energy(df)
else:
    print("CSV file does not exist. Please run the plot_orbits script first.")




end_time =time.time()
elapsed_time =end_time-start_time
print(f"The code took {elapsed_time} seconds to run.")
