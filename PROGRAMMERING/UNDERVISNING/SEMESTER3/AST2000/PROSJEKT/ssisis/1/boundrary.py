#ikke kodemal
import numpy as np

import sys
sys.path.append("C:/Users/simon/Skrivebord/ssisis/1")   # HUSK!!!! Add the directory containing the script
import consts as cs

escaped_velocities = []


def velocity_distribution(temperature,n):   # Maxwell-Boltzmann distribution
    sigma = np.sqrt((cs.boltzmann_constant * temperature) / (cs.hydrogen2_mass))
    return np.random.normal(0, sigma, (n, 3))

velocity = velocity_distribution(cs.temperature,cs.num_particles)   


def setting_velocity(): # setting the velocity dir of the particles
    return np.random.uniform(-1, 1, 3)


def boundary_conditions(position, velocity, box_length, hole_radius, hole_center):  # Apply boundary conditions and check for particles falling into the hole
    for i, pos in enumerate(position):   # Check for particles falling into the hole
        distance_to_center =np.linalg.norm(pos[:2]-hole_center)
        if distance_to_center < hole_radius and pos[2] <= 0: # Reset the position and velocity of the particle
            escaped_velocities.append(velocity[i].copy())  #storing velocities of particles escaping
            position[i]=np.array([box_length/2, box_length/2, box_length/2])    # sett particle to "spawn" in the center of x-y plane and top of z-plane

            new_velocity =velocity_distribution(cs.temperature, 1)[0]  # Set the new velocity of the particle

            velocity_magnitude =np.linalg.norm(velocity[i])    # Keep the magnitude of the velocity so we dont get a drift
            new_velocity_normalized =new_velocity / np.linalg.norm(new_velocity)*velocity_magnitude
            velocity[i]= new_velocity_normalized   

    index =np.where((position >box_length) | (position < 0)) # find the exact index of the particle that is outside the box
    velocity[index] *=-1    # Reflect the velocity of the particle
    return position, velocity, escaped_velocities