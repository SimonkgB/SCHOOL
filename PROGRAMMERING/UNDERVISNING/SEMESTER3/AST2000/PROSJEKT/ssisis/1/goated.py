#ikke kodemal
import numpy as np
import scipy.constants as scp_c
import matplotlib.pyplot as plt
import matplotlib.animation as animation


import sys
sys.path.append("C:/Users/simon/Skrivebord/ssisis/1")  # HUSK!!!! Add the directory containing the script
import boundrary as b_c
import consts as cs



np.random.seed()    # Set seed for random number generator

#################################
# INTIAL POSITION AND VELOCITY
position= np.random.uniform(0, cs.box_length, (cs.num_particles,3))   # create a variable position starting uniformly between 0, box_lengt and set it into a 1x3xn matrix 
velocity = np.random.normal(0, np.sqrt((cs.boltzmann_constant * cs.temperature) / cs.hydrogen2_mass),(cs.num_particles, 3))


######################
# HOLE PROPPERTIES
hole_radius = np.sqrt(((1/4*cs.box_length**2)/np.pi))  # radius of the hole in meters
hole_center =np.array([cs.box_length/2, cs.box_length/2])  # center of the hole

###############################
# STORE INFO ABOUT PARTICLES
all_particle_trajectory =np.zeros((cs.num_time_steps, cs.num_particles, 3))

##########################
# "EULER-CHROMER" 
for index in range(cs.num_time_steps):  # Loop over all time steps
    position, velocity, escaped_velocities =b_c.boundary_conditions(position, velocity, cs.box_length, cs.hole_radius, cs.hole_center)  # Apply boundary conditions and update positions
    position +=velocity*cs.time_step    # Update positions
    all_particle_trajectory[index] =position    # Store the positions of all particles for later use

escaped_velocities =np.array(escaped_velocities)




########################
# ANIMATION
#If intrested in animation, uncomment the code below
"""
fig = plt.figure()  # Create a new figure
ax = fig.add_subplot(111, projection="3d")  # Add a 3d axes to the figure

def update(frame, position, velocity, box_length):  # Update euler-chromer as a function for animation
    position, velocity, _ = b_c.boundary_conditions(position, velocity, box_length, hole_radius, hole_center)  # Update positions and apply boundary conditions
    position += velocity * cs.time_step
    ax.clear()  # Clear the axes

    # Make a circle in the x-y plane (z=0)
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = cs.hole_center[0]+hole_radius*np.cos(theta)
    y_circle = cs.hole_center[1]+hole_radius*np.sin(theta)
    z_circle = np.zeros_like(x_circle)  # z=0 for all points
    ax.plot(x_circle, y_circle, z_circle, "r")

    # Set labels and title
    ax.set_xlim(0, cs.box_length)
    ax.set_ylim(0, cs.box_length)
    ax.set_zlim(0, cs.box_length)
    ax.set_xlabel("x-axis (m)")
    ax.set_ylabel("y-axis (m)")
    ax.set_zlabel("z-axis (m)")
    ax.set_title("Animation of the particles (3d)")
    ax.scatter(position[:, 0], position[:, 1], position[:, 2], s=20)
    return ax

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=2000, fargs=(position, velocity, cs.box_length), interval=20)

f = r"C:/Users/simon/Skrivebord/ssisis/visuals/animation_box.gif" 
writergif = animation.PillowWriter(fps=30) 
ani.save(f, writer=writergif)
"""

# if intrested in histograms, uncomment the code below

"""
# Calculate the number of bins using the square root rule
binz_sqr =int(np.sqrt(len(velocity)))

velocity1 =np.linspace(-17000, 17000, 10000)    # Create velocity1 array for the analytical solution

# Calculate the analytical solution for the X-component
analytical_solution_x =(cs.hydrogen2_mass/(2*np.pi*cs.boltzmann_constant*cs.temperature))**(1/2)*np.exp(-cs.hydrogen2_mass*velocity1**2/(2*cs.boltzmann_constant*cs.temperature))

# Create a new figure with specified size
plt.figure(figsize=(8, 6))

# Subplot for x-component of velocity
plt.subplot(3, 1, 1)
plt.hist(velocity[:, 0], bins=binz_sqr, density=True, label="Numerical solution")
plt.plot(velocity1, analytical_solution_x, label="Analytical Solution")
plt.title("Histogram of the escaped particles (x-component)")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Frequency")
plt.legend()

# Subplot for y-component of velocity
plt.subplot(3, 1, 2)
plt.hist(velocity[:, 1], bins=binz_sqr, density=True, label="Numerical solution")
plt.plot(velocity1, analytical_solution_x, label="Analytical Solution")
plt.title("Histogram of the escaped particles (y-component)")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Frequency")
plt.legend()

# Subplot for z-component of velocity
plt.subplot(3, 1, 3)
plt.hist(velocity[:, 2], bins=binz_sqr, density=True, label="Numerical solution")
plt.plot(velocity1, analytical_solution_x, label="Analytical Solution")
plt.title("Histogram of the escaped particles (z-component)")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Frequency")
plt.legend()

# Adjust layout to prevent overlap
plt.tight_layout()

# Uncomment the next line if you want to save the figure
plt.savefig("Decompose_velocity_vector.png")    # save the figure

# Show the plot
plt.show()



velocity2 =np.linspace(0, 25000, 10000)

velocity_norm =np.linalg.norm(velocity, axis=1)
density_function =4*np.pi*velocity2**2*(cs.hydrogen2_mass/(2*np.pi*cs.boltzmann_constant*cs.temperature))**(3/2)*np.exp(-cs.hydrogen2_mass*velocity2**2/(2*cs.boltzmann_constant*cs.temperature))
plt.hist(velocity_norm, bins=binz_sqr, density=True, label="Numerical solution")
plt.plot(velocity2, density_function, label="Analytical Solution")
plt.title("Histogram of the all particles in the box")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("norm_velocity.png")    # save the figure
plt.show()
"""

#print(np.mean(position, axis=0))
#print(cs.box_length/2)