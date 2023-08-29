import numpy as np
import scipy.constants as scp_c
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

#np.random.seed(2)

########################
# CONSTANTS

box_length =10e-6  # Length of the cubic box in meters
temperature =3e3   # Temperature in Kelvin
num_particles = 100 # number of particles
boltzmann_constant =scp_c.Boltzmann  # Boltzmann constant in J/K
hydrogen2_mass= 3.34e-27  # Mass of a particle in kg

#####################
# TIME
num_time_steps = 2000
time_step =10e-9/num_time_steps # Number of time steps for the simulation


####################
# STORAGE
escaped_velocities = []
hoe = []


def velocity_distribution(hydrogen2_mass):
    sigma = np.sqrt((boltzmann_constant*temperature)/(hydrogen2_mass))   #check if correct
    return np.random.normal(0, sigma)

    
######################
# INITIAL VELOCITY FUNCTION
def setting_velocity(vel_dis):    # Initialize velocities for particles based on the Maxwell-Boltzmann distribution

    # Generate random angles
    theta =np.random.uniform(0,np.pi) # random intial angles
    phi =np.random.uniform(0, 2*np.pi)

    # VELOCITY COMPONENTS
    v_x =vel_dis*np.sin(theta)*np.cos(phi)   #sending the particles in random directions
    v_y =vel_dis*np.sin(theta)*np.sin(phi)    # Using v = np.sqrt(v_x^2 + v_y^2 + v_z^2)
    v_z =vel_dis*np.cos(theta)
    return np.array([v_x, v_y, v_z])

# CHANGE ANGLE BUT KEEP ABS(V) THIS WILL KEEP SAME TEMPRATURE OF THE PARTICLE ESCAPEING
# TYNGDEKRAFT = TRYKK KRAFT

#########################
# BONDRARY CONDITIONS
def boundary_conditions(position, velocity, box_length, hole_radius, hole_center):  # Apply boundary conditions and check for particles falling into the hole
    
    num =0 # Initialize counter for particles falling into the hole
   
    for i, pos in enumerate(position):   # Check for particles falling into the hole
        distance_to_center =np.linalg.norm(pos[:2] - hole_center)
        if distance_to_center < hole_radius and pos[2] <=box_length: # Reset the position and velocity of the particle
            hoe.append(position[i])
            position[i] = np.array([box_length/2, box_length/2, box_length])    # sett particle to "spawn" in the center of x-y plane and top of z-plane
            velocity[i] =setting_velocity(velocity_distribution(hydrogen2_mass))
            num +=1    #incrment particle counter
            escaped_velocities.append(velocity[i].copy())  #storing velocities of particles escaping
    
        index =np.where((position >box_length) | (position < 0)) # Reflective boundary conditions
        velocity[index] *=-1
    return position, velocity, num

#################################
# INTIAL POSITION AND VELOCITY
position= np.random.uniform(0, box_length, (num_particles,3))   # create a variable position starting uniformly between 0, box_lengt and set it into a 1x3xn matrix 
velocity =np.array([setting_velocity(velocity_distribution(hydrogen2_mass)) for _ in range(num_particles)])

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
    position, velocity, num =boundary_conditions(position, velocity, box_length, hole_radius, hole_center)  # Apply boundary conditions and update positions
    position +=velocity*time_step
    all_particle_trajectory[index] =position
    num_particles_in_hole +=num        # Update the total counter
"""
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

def update(frame, position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, hydrogen2_mass):    # fix? lær deg animations din tulling, må være en bedre methode (raskere)
    

    position, velocity, _ =boundary_conditions(position, velocity, box_length, hole_radius, hole_center)# Update positions and apply boundary conditions
    position +=velocity*time_step

    # Update the scatter plots
    sc1.set_offsets(np.column_stack((position[:, 0], position[:, 2])))
    sc2.set_offsets(position[:, :2])

ani =animation.FuncAnimation(fig, update, frames=2000, fargs=(position, velocity, box_length, hole_radius, hole_center, temperature, boltzmann_constant, hydrogen2_mass), interval=20, repeat=False)

# SHOWTIME
plt.tight_layout()
plt.show()"""

# HOW MANY PARTICLES IN HOLE
print(f"Total number of particles in hole: {num_particles_in_hole}")    # i can use this number to "create" a force which will propell teh rocket


# Print the velocities of particles that escaped

##########################
#NEW DEFINITIONS FOR STUFF
rocket_payload = 10
rocket_engine = 3
rocket_mass = rocket_engine + rocket_payload
hydrogen2_mass= 3.34e-27
escaped_velocities = np.array(escaped_velocities)

#print(escaped_velocities[2])
# Momentum for each escaping particle
"""
momentum_particles = np.sum(escaped_velocities * hydrogen2_mass, axis=0)
print(f"partikkel fart:{momentum_particles[2]}")
v_r = momentum_particles / rocket_mass
print("Rocket Velocity:", v_r[2])



# function for calculating total force
def calculate_force(v_r):
    # Calculate the change in momentum
    
    # Calculate the force using F = Δp/Δt
    force_x = v_r[0] / time_step
    force_y = v_r[1] / time_step
    force_z = v_r[2] / time_step
    
    return np.array([force_x, force_y, force_z])


print(f"kraft: {calculate_force(v_r)[2]}")

ii = 0
kk = 0

for k in escaped_velocities:
    if k[2]<0:
        ii+=1
    elif k[2]>0:
        kk+=1
print(ii,kk)

"""
for k in hoe:
    print(k[2])