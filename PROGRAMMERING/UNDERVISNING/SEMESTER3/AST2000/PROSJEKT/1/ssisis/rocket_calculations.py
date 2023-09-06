import numpy as np
import math

import sys
sys.path.append("C:/Users/simon/Skrivebord/ssisis")  # Add the directory containing the script
import goated as w
import consts as cs


momentum_particles = cs.hydrogen2_mass*np.sum(w.escaped_velocities, axis=0)  # indicates that we are suming the x-components so we dont need a for loop
momentum_rocket = -momentum_particles
velocity_rocket = momentum_rocket / cs.rocket_mass_fixed


# function for calculating total force
def thrust(escaped_velocities, hydrogen2_mass, totaltime):
    num_escaped_particles =len(escaped_velocities)
    mass_flow_rate =(num_escaped_particles/totaltime)*hydrogen2_mass
    avg_velocity = np.abs(np.mean(escaped_velocities, axis=0))
    return mass_flow_rate*avg_velocity

def calculate_temperature_in_box(velocity): # calculate temperature in the box
    kinetic_energy = 1/2*cs.hydrogen2_mass*np.sum(velocity**2, axis=1)
    avg_kinetic_energy =np.mean(kinetic_energy)
    temperature =(2*avg_kinetic_energy)/(3*cs.boltzmann_constant)
    return temperature

def pressure(): # pressure in the box
    return cs.num_particles/(cs.box_length**3)*cs.boltzmann_constant*calculate_temperature_in_box(w.velocity) # as soon as a particle escape a new one replaces it with teh same velocity but a diffrent rvect

def energy():   # energy in the box calculated in 2 diffrent ways
    a1= 1/2*cs.hydrogen2_mass*np.mean(np.sum(w.velocity**2, axis=1))    # axis=1 means that we are summing the x,y and z all squard components so we dont need a for loop
    a2= 3/2*cs.boltzmann_constant*calculate_temperature_in_box(w.velocity)
    return a1, a2

def gravity0(mass, radius): # gravity on the surface of the planet
    return cs.Gc*mass/(radius**2)

def escape_vel(mass, radius):   # escape velocity from the surface of the planet
    return np.sqrt(2*(gravity0(mass, radius))*(radius))


def n_motors(thrust, escape_velocity, time, rocket_mass): # n motors for ESCAPING THE PLANET 
    required_thrust = escape_velocity*rocket_mass/time
    return np.abs(required_thrust/thrust)

def massflow(thrust, avg_vel):
    return np.abs(thrust/avg_vel) # for n particles this will stay constant




total_thrust = thrust(w.escaped_velocities, cs.hydrogen2_mass, cs.totaltime)
vel_mag = np.array([total_thrust[0]/cs.rocket_mass_fixed*417,total_thrust[1]/cs.rocket_mass_fixed*417,escape_vel(cs.mass_p0, cs.radius_p0)]) # the velocity we want to reach at v_esc (x,y) is as is since we want 0 drif because of the exit of the aprticles in rockets
avg_velocity = np.mean(np.linalg.norm(w.escaped_velocities, axis=1))
escape_velocity = escape_vel(cs.mass_p0, cs.radius_p0)
num_motors = n_motors(total_thrust, vel_mag, cs.time_to_v_esc, cs.rocket_mass_fixed)

mass_flow = massflow(total_thrust, avg_velocity)*num_motors
total_thrust_z = total_thrust[2]*num_motors[2]

print(f"Total Thrust for one motor: {total_thrust}")
print(f"Number of Motors: {num_motors}")
print(f"Mass Flow: {mass_flow}")
print(f"Total Thrust for all motors: {total_thrust_z}")
