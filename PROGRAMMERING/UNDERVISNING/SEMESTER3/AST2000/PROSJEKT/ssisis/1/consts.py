#ikke kodemal
import scipy.constants as scp_c
import numpy as np

#########################################################
############# Denne koden er for blogg 1 ################
#########################################################

box_length =10e-6  # Length of the cubic box in meters
temperature =4e3   # Temperature in Kelvin
num_particles =10000 # number of particles
boltzmann_constant =scp_c.Boltzmann  # Boltzmann constant in J/K
hydrogen2_mass= 3.34e-27  # Mass of a particle in kg
Gc =scp_c.gravitational_constant

rocket_payload =4000 # kg
rocket_fuel_mass  =200_000 #kg   can be updated from the rocket_calculations.py
rocket_mass_fixed =rocket_payload+rocket_fuel_mass # kg 5_000_000

totaltime =10e-9
num_time_steps =1000
time_step =totaltime/num_time_steps # length of a time step for the simulation
time_to_v_esc =20*60 # 20min

hole_radius =np.sqrt(((0.25*box_length**2)/np.pi))  # radius of the hole in meters
hole_center =np.array([box_length/2, box_length/2])  # center of the hole


import ast2000tools.constants as ast_c
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem

seed = utils.get_seed("skgberg_mariutor")
system = SolarSystem(seed)

home_planet_idx = 0 # The home planet always has index 0
#print(f"My mission starts on planet {home_planet_idx}, which has a radius of {mission.system.radii[home_planet_idx]} kilometers")

#print(f"My system has a {system.star_mass} solar mass star with a radius of {system.star_radius} kilometers.")

#################
# INERTIAL FRAME #
mass_p0 =system.masses[home_planet_idx]*ast_c.m_sun    # mass of the planet in kg
radius_p0 =system.radii[home_planet_idx]*1000          # radius of the planet in m
radius_p0_au = utils.m_to_AU(radius_p0)                     # radius of the planet in AU






#########################################################
############# Denne koden er for blogg 2 ###############
#########################################################

# EXTERNAL FRAME #
initial_positions =np.transpose(system.initial_positions)  # Transpose to get a 3xn matrix for position
initial_velocities =np.transpose(system.initial_velocities)    # Transpose to get a 3xn matrix for velocity
initial_values =np.concatenate((initial_positions, initial_velocities), axis=1)   #merge the two matrices into one 6xn matrix

mass_sun =system.star_mass   # mass of the sun  
mass_planets =system.masses  # mass of the planets
# make into a matrix mass x y vx vy
conditions_planets =np.concatenate((np.transpose([mass_planets]),initial_values), axis=1)   #merge the two matrices into one 6xn matrix
#do the same for the sun
conditions =np.concatenate((np.array([[mass_sun, 0, 0, 0, 0]]), conditions_planets), axis=0)   #merge the two matrices into one 6xn matrix
# merge the sun and the planets into one matrix

a_axis = system.semi_major_axes
#b_axis = system.semi_major_axes
eccentricity = system.eccentricities
aphelion_angles = system.aphelion_angles
GAU = 4*np.pi**2

year =1.28394067
dt =1e-05

color_dic = {
    0: "black",
    1: "red",
    2: "blue",
    3: "green",
    4: "orange",
    5: "purple",
    6: "brown",
    7: "olive",
}

print(conditions)