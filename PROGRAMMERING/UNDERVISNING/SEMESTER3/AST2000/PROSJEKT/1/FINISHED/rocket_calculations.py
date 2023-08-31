import numpy as np
import scipy.constants as scp_c

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED")  # Add the directory containing the script
import goated as w
import boundrary_conditions as b_c
import consts as cs


momentum_particles = np.sum(w.escaped_velocities*cs.hydrogen2_mass, axis=0)  # indicates that we are suming the x-components so we dont need a for loop
momentum_rocket = -momentum_particles
velocity_rocket = momentum_rocket / cs.rocket_mass


# function for calculating total force
def thrust(v_r):
    force_x = v_r[0]/cs.time_step
    force_y = v_r[1]/cs.time_step
    force_z = v_r[2]/cs.time_step
    return np.array([force_x, force_y, force_z])


def massflow():
    return cs.hydrogen2_mass*w.escaped_velocities.shape[0]/cs.totaltime # for n particles this will stay constant


def calculate_temperature_in_box(velocity ):
    kinetic_energy = 1/2*cs.hydrogen2_mass*np.sum(velocity**2, axis=1)
    avg_kinetic_energy =np.mean(kinetic_energy)
    temperature =(2*avg_kinetic_energy)/(3*cs.boltzmann_constant)
    return temperature
temperature_in_box =calculate_temperature_in_box(w.velocity)


def pressure():
    return cs.num_particles/(cs.box_length**3)*cs.boltzmann_constant*temperature_in_box # as soon as a particle escape a new one replaces it with teh same velocity but a diffrent rvect

def energy():
        return 3/2*cs.boltzmann_constant*temperature_in_box






"""
print(f"The temperature of the system is {temperature_in_box} K")
print(f"The pressure of the system is: {pressure()}")
print(f"The energy of teh system is: {energy()}")
print(f"The velocity of teh rocket is {v_r[2]}]")
print(f"kraft done by particles: {thrust(velocity_rocket)[2]}") 
"""

