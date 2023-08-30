import scipy.constants as scp_c
import numpy as np

box_length =10e-6  # Length of the cubic box in meters
temperature =8e3   # Temperature in Kelvin
num_particles = 150 # number of particles
boltzmann_constant =scp_c.Boltzmann  # Boltzmann constant in J/K
hydrogen2_mass= 3.34e-27  # Mass of a particle in kg
Gc = scp_c.gravitational_constant

rocket_payload = 10
rocket_engine = 3
rocket_mass = rocket_engine + rocket_payload

totaltime = 10e-9
num_time_steps = 2000
time_step =totaltime/num_time_steps # Number of time steps for the simulation

hole_radius = np.sqrt(((0.25*box_length**2)/np.pi))  # radius of the hole in meters
hole_center =np.array([box_length/2, box_length/2])