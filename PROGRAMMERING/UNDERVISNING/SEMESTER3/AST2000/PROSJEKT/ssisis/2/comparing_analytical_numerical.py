
import numpy as np
import os
import csv
import pandas as pd
from numba import jit
import matplotlib.pyplot as plt
import sys

sys.path.append("C:/Users/simon/Skrivebord/ssisis/1") 
import consts as cs

sys.path.append("C:/Users/simon/Skrivebord/ssisis/2") 
import orbits as ob

csv_file_name = "plotting_orbits_1.csv"
initial_conditions = cs.initial_values  # Assuming this is a 2D array
num_planets = len(initial_conditions)


@jit(nopython=True)
def plot_analytical_solution(a, e, theta_0, num_points=1000):
    theta = np.linspace(0, 2*np.pi, num_points)
    theta = np.pi-theta
    r = a*(1-e**2)/(1+e*np.cos(theta-theta_0))
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y

def plotting(df):
    plt.figure(figsize=(10, 10))
    for i in range(num_planets):
        plt.plot(df[f"Planet_{i}_x"], df[f"Planet_{i}_y"],label=f"Planet {i} num.", color=cs.color_dic[i], alpha=0.5)

    for i in range(num_planets):
        x, y =plot_analytical_solution(cs.a_axis[i], cs.eccentricity[i], cs.aphelion_angles[i])
        plt.plot(x, y, label=f"Planet {i} anl.", color=cs.color_dic[i], linestyle='--', alpha=1)
    plt.xlabel("x (AU)")
    plt.ylabel("y (AU)")
    plt.title("Orbits of Planets")
    plt.legend()
    plt.show()


if os.path.exists(csv_file_name):
    print("CSV file exists. Plotting data.")
    df =pd.read_csv(csv_file_name)
    plotting(df)
else:
    print("CSV file does not exist. Please run orbits.py first.")
