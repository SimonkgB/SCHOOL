import numpy as np
import scipy.constants as scp_c
import matplotlib.pyplot as plt
import matplotlib.animation as animation


import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1")  # Add the directory containing the script
import boundrary_conditions as b_c
import velocities as velc
import consts as cs

#np.random.seed(2)

#################################
# INTIAL POSITION AND VELOCITY
position= np.random.uniform(0, cs.box_length, (cs.num_particles,3))   # create a variable position starting uniformly between 0, box_lengt and set it into a 1x3xn matrix 


######################
# HOLE PROPPERTIES
hole_radius = np.sqrt(((0.25*cs.box_length**2)/np.pi))  # radius of the hole in meters
hole_center =np.array([cs.box_length/2, cs.box_length/2])  # center of the hole

###############################
# STORE INFO ABOUT PARTICLES
all_particle_trajectory =np.zeros((cs.num_time_steps, cs.num_particles, 3))

##########################
# "EULER-CHROMER" 
for index in range(cs.num_time_steps):
    position, velocity, escaped_velocities =b_c.boundary_conditions(position, velc.velocity, cs.box_length, cs.hole_radius, cs.hole_center)  # Apply boundary conditions and update positions
    position +=velocity*cs.time_step
    all_particle_trajectory[index] =position

escaped_velocities = np.array(escaped_velocities)








########################
# ANIMATION
"""

fig, (ax1, ax2) =plt.subplots(1, 2, figsize=(10, 5))

# "conditions" for first subplot (x-z plane)
ax1.set_title("Animation of the particles (x-z plane)")
ax1.set_xlabel("x-axis")
ax1.set_ylabel("z-axis")
sc1 =ax1.scatter(position[:, 0], position[:, 2], s=20)
ax1.set_xlim(0, box_length)
ax1.set_ylim(0, box_length)

# "conditions" for the second subplot (x-y plane)
ax2.set_title("Animation of the particles (x-y plane)")
ax2.set_xlabel("x-axis")
ax2.set_ylabel("y-axis")
sc2 =ax2.scatter(position[:, 0], position[:, 1], s=20)
ax2.set_xlim(0, box_length)
ax2.set_ylim(0, box_length)

def update(frame, position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, hydrogen2_mass):    # fix? lær deg animations din tulling, må være en bedre methode (raskere)
    

    position, velocity, _ =boundary_conditions(position, velocity, box_length, hole_radius, hole_center)# Update positions and apply boundary conditions
    position +=velocity*time_step

    # Update the scatter plots
    sc1.set_offsets(np.column_stack((position[:, 0], position[:, 2])))
    sc2.set_offsets(position[:, :2])

ani =animation.FuncAnimation(fig, update, frames=2000, fargs=(position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, hydrogen2_mass), interval=20, repeat=False)

# SHOWTIME
plt.tight_layout()
plt.show()

# HOW MANY PARTICLES IN HOLE
print(f"Total number of particles in hole: {num_particles_in_hole}")    # i can use this number to "create" a force which will propell teh rocket
"""