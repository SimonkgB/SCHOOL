import numpy as np
import scipy.constants as scp_c

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1")  # Add the directory containing the script
import goated as w
import boundrary_conditions as b_c
import velocities as velc
import consts as cs


momentum_particles = np.sum(w.escaped_velocities*cs.hydrogen2_mass, axis=0)  # indicates that we are suming the x-components so we dont need a for loop
momentum_rocket = -momentum_particles
v_r = momentum_rocket / cs.rocket_mass


# function for calculating total force
def calculate_force(v_r):
    # Calculate the change in momentum
    
    # Calculate the force using F = Δp/Δt
    force_x = v_r[0]/cs.time_step
    force_y = v_r[1]/cs.time_step
    force_z = v_r[2]/cs.time_step
    
    return np.array([force_x, force_y, force_z])

fz = calculate_force(v_r)[2]

"""
print(f"summen av partikkelenes momentum: {momentum_particles}")
print (f"rockets momentum: {momentum_rocket}")
print(f"Rocket Velocity: {v_r[2]}")
print(f"kraft done by particles: {calculate_force(v_r)[2]}")"""
