import numpy as np
import scipy.constants as scp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

########################
# CONSTANTS

box_length =10e-6  # Length of the cubic box in meters
temperature =2e3   # Temperature in Kelvin
num_particles = 2000 # number of particles
boltzmann_constant =scp.Boltzmann  # Boltzmann constant in J/K
particle_mass =1e-28   # Mass of a particle in kg

#####################
# TIME
num_time_steps = 2000
time_step =10e-9/num_time_steps # Number of time steps for the simulation


####################
# STORAGE
escaped_velocities = []

######################
# INITIAL VELOCITY FUNCTION
def initialize_velocity(temperature, boltzmann_constant, particle_mass):    # Initialize velocities for particles based on the Maxwell-Boltzmann distribution

    # Calculate the average speed
    v_avg =np.sqrt((8*boltzmann_constant*temperature)/(np.pi*particle_mass))

    # Generate random angles
    theta =np.random.uniform(0, np.pi) # random intial angles
    phi =np.random.uniform(0, 2*np.pi)

    # VELOCITY COMPONENTS
    v_x =v_avg*np.sin(theta)*np.cos(phi)   #sending them in random directions
    v_y =v_avg*np.sin(theta)*np.sin(phi)
    v_z =v_avg*np.cos(theta)
    return np.array([v_x, v_y, v_z])


#########################
# BONDRARY CONDITIONS
def boundary_conditions(position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, particle_mass):  # Apply boundary conditions and check for particles falling into the hole
    
    num =0 # Initialize counter for particles falling into the hole
    
    index =np.where((position >=box_length) | (position <=0)) # Reflective boundary conditions
    velocity[index] *=-1
   
    for i, pos in enumerate(position):   # Check for particles falling into the hole
        distance_to_center =np.linalg.norm(pos[:2] - hole_center)
        if distance_to_center < hole_radius and pos[2] <=0.01: # Reset the position and velocity of the particle
            position[i] = np.array([box_length/2, box_length/2, box_length])
            velocity[i] =initialize_velocity(temperature, boltzmann_constant, particle_mass)
            num +=1    #incrment particle counter
            escaped_velocities.append(velocity[i])  #storing velocities of particles escaping
    return position, velocity, num

#################################
# INTIAL POSITION AND VELOCITY
position= np.random.uniform(0, box_length, (num_particles, 3))
velocity =np.array([initialize_velocity(temperature, boltzmann_constant, particle_mass) for _ in range(num_particles)])

######################
# HOLE PROPPERTIES
hole_radius =0.01*box_length  # radius of the hole in meters
hole_center =np.array([box_length/2, box_length/2])  # center of the hole

###############################
# STORE INFO ABOUT PARTICLES
all_particle_trajectory =np.zeros((2000, num_particles, 3))
num_particles_in_hole=0 # initialize counter for total particls falling into the hole

##########################
# "EULER-CHROMER" 
for index in range(2000):
    position, velocity, num =boundary_conditions(position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, particle_mass)     # Apply boundary conditions and update positions
    position +=velocity*time_step
    all_particle_trajectory[index] =position
    num_particles_in_hole +=num        # Update the total counter

########################
# ANIMATION
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

def update(frame, position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, particle_mass):    # fix? lær deg animations din tulling, må være en bedre methode (raskere)
    

    position, velocity, _ =boundary_conditions(position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, particle_mass)# Update positions and apply boundary conditions
    position +=velocity*time_step

    # Update the scatter plots
    sc1.set_offsets(np.column_stack((position[:, 0], position[:, 2])))
    sc2.set_offsets(position[:, :2])

# Create the animation object
ani =animation.FuncAnimation(fig, update, frames=2000, fargs=(position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, particle_mass), interval=20, repeat=False)

# SHOWTIME
plt.tight_layout()
plt.show()

# HOW MANY PARTICLES IN HOLE
print(f"Total number of particles in hole: {num_particles_in_hole}")    # i can use this number to "create" a force which will propell teh rocket


# Print the velocities of particles that escaped

##########################
#NEW DEFINITIONS FOR STUFF
rocket_mass= 10
hydrogen2_mass= 3.34e-27
escaped_velocities = np.array(escaped_velocities)

# Momentum for each escaping particle
def momentum_h_xyz(m_h, escaped_v):
    return m_h*escaped_v

# calculating teh veloocity for teh rochet using conservation of momentum (perfect elasticity)
def velocity_r(m_r, p_r):
    v_r= 0
    for k in p_r:
        v_r +=k/m_r
    return v_r

# function for calculating total force
def calculate_force(momentum):
    # Calculate the change in momentum
    delta_p_x = sum(momentum[0])
    delta_p_y = sum(momentum[1])
    delta_p_z = sum(momentum[2])
    
    # Calculate the force using F = Δp/Δt
    force_x = delta_p_x / time_step
    force_y = delta_p_y / time_step
    force_z = delta_p_z / time_step
    
    return force_x, force_y, force_z

# Calculate the force
force_x, force_y, force_z = calculate_force(momentum_h_xyz(hydrogen2_mass,escaped_velocities))
print(f"Force in x-direction: {force_x} N")
print(f"Force in y-direction: {force_y} N")
print(f"Force in z-direction: {force_z} N")

