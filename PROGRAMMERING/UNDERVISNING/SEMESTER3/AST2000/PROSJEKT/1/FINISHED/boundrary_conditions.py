import numpy as np
from numba import jit

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1")  # Add the directory containing the script
import velocities as velc
import consts as cs

escaped_velocities = []


def velocity_distribution(temperature):
    sigma = np.sqrt((cs.boltzmann_constant * temperature) / (cs.hydrogen2_mass))
    return np.random.normal(0, sigma, (cs.num_particles, 3))

velocity = velocity_distribution(cs.temperature)


def boundary_conditions(position, velocity, box_length, hole_radius, hole_center):  # Apply boundary conditions and check for particles falling into the hole
    for i, pos in enumerate(position):   # Check for particles falling into the hole
        distance_to_center =np.linalg.norm(pos[:2] - hole_center)
        if distance_to_center < hole_radius and pos[2] <= 0: # Reset the position and velocity of the particle
            escaped_velocities.append(velocity[i].copy())  #storing velocities of particles escaping
            position[i] = np.array([box_length/2, box_length/2, box_length])    # sett particle to "spawn" in the center of x-y plane and top of z-plane
            velocity[i] = np.random.normal(0, np.sqrt((cs.boltzmann_constant * cs.temperature) / (cs.hydrogen2_mass)),3)

    index =np.where((position >box_length) | (position < 0)) # Reflective boundary conditions
    velocity[index] *=-1
    return position, velocity, escaped_velocities