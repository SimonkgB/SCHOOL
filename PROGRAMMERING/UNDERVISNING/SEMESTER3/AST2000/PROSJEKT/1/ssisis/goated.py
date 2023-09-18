import numpy as np
import scipy.constants as scp_c
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numba import njit

import sys
sys.path.append("C:/Users/simon/Skrivebord/ssisis")  # Add the directory containing the script
import boundrary as b_c
import consts as cs



np.random.seed()

#################################
# INTIAL POSITION AND VELOCITY
position= np.random.uniform(0, cs.box_length, (cs.num_particles,3))   # create a variable position starting uniformly between 0, box_lengt and set it into a 1x3xn matrix 
velocity = np.random.normal(0, np.sqrt((cs.boltzmann_constant * cs.temperature) / cs.hydrogen2_mass),(cs.num_particles, 3))


######################
# HOLE PROPPERTIES
hole_radius = np.sqrt(((0.25*cs.box_length**2)/np.pi))  # radius of the hole in meters
hole_center =np.array([cs.box_length/2, cs.box_length/2])  # center of the hole

###############################
# STORE INFO ABOUT PARTICLES
all_particle_trajectory =np.zeros((cs.num_time_steps, cs.num_particles, 3))

##########################
# "EULER-CHROMER" 
@njit
for index in range(cs.num_time_steps):
    position, velocity, escaped_velocities =b_c.boundary_conditions(position, velocity, cs.box_length, cs.hole_radius, cs.hole_center)  # Apply boundary conditions and update positions
    position +=velocity*cs.time_step
    all_particle_trajectory[index] =position

escaped_velocities = np.array(escaped_velocities)




########################
# ANIMATION
"""
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

def update(frame, position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, hydrogen2_mass):
    position, velocity, _ =b_c.boundary_conditions(position, velocity, box_length, hole_radius, hole_center)# Update positions and apply boundary conditions
    position +=velocity*cs.time_step
    ax.clear()
    ax.set_xlim(0, cs.box_length)
    ax.set_ylim(0, cs.box_length)
    ax.set_zlim(0, cs.box_length)
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")
    ax.set_title("Animation of the particles (3d)")
    ax.scatter(position[:, 0], position[:, 1], position[:, 2], s=20)
    return ax

ani = animation.FuncAnimation(fig, update, frames=2000, fargs=(position, velocity, cs.box_length, cs.hole_radius, cs.hole_center, cs.temperature, cs.boltzmann_constant, cs.hydrogen2_mass), interval=20, repeat=False)

f = r"C:/Users/simon/Skrivebord/ssisis/animation_box.gif" 
writergif = animation.PillowWriter(fps=30) 
ani.save(f, writer=writergif)
"""

binz = int(np.sqrt(len(velocity)+len(escaped_velocities)))

plt.figure(figsize=(8, 6))  # Adjust the figure size if needed

# Subplot 1
plt.subplot(3, 1, 1)
plt.hist(velocity[:, 0], bins=binz, density=True)
plt.title("Histogram of the escaped particles (X-component)")
plt.xlabel("Velocity")
plt.ylabel("Number of particles")

# Subplot 2
plt.subplot(3, 1, 2)
plt.hist(velocity[:, 1], bins=binz, density=True)
plt.title("Histogram of the escaped particles (Y-component)")
plt.xlabel("Velocity")
plt.ylabel("Number of particles")

# Subplot 3
plt.subplot(3, 1, 3)
plt.hist(velocity[:, 2], bins=binz, density=True)
plt.title("Histogram of the escaped particles (Z-component)")
plt.xlabel("Velocity")
plt.ylabel("Number of particles")

plt.tight_layout()  # Ensures proper spacing between subplots
plt.show()

plt.hist(np.linalg.norm(velocity, axis=1), bins=binz, density=True)
plt.title("Histogram of the all particles in the box")
plt.xlabel("Velocity")
plt.ylabel("Number of particles")
plt.show()
