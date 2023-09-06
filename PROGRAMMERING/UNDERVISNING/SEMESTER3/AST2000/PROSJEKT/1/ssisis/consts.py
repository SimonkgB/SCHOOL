import scipy.constants as scp_c
import numpy as np

box_length =10e-6  # Length of the cubic box in meters
temperature =4e3   # Temperature in Kelvin
num_particles = 1000 # number of particles
boltzmann_constant =scp_c.Boltzmann  # Boltzmann constant in J/K
hydrogen2_mass= 3.34e-27  # Mass of a particle in kg
Gc = scp_c.gravitational_constant

rocket_payload = 400_000 # kg
rocket_mass_fixed = 5_000_000 # kg

totaltime = 10e-9
num_time_steps = 10000
time_step =totaltime/num_time_steps # Number of time steps for the simulation
time_to_v_esc = 10*60 # 10min

hole_radius = np.sqrt(((0.25*box_length**2)/np.pi))  # radius of the hole in meters
hole_center =np.array([box_length/2, box_length/2])  # center of the hole


import ast2000tools.constants as ast_c
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem

seed = utils.get_seed("simm")
system = SolarSystem(seed)

home_planet_idx = 0 # The home planet always has index 0
#print(f"My mission starts on planet {home_planet_idx}, which has a radius of {mission.system.radii[home_planet_idx]} kilometers")

#print(f"My system has a {system.star_mass} solar mass star with a radius of {system.star_radius} kilometers.")

mass_p0 = system.masses[home_planet_idx]*ast_c.m_sun    # mass of the planet in kg
radius_p0 = system.radii[home_planet_idx]*1000          # radius of the planet in m
radius_p0_au = utils.m_to_AU(radius_p0)                 # radius of the planet in AU
mass_sun = system.star_mass*ast_c.m_sun                 # mass of the sun in kg