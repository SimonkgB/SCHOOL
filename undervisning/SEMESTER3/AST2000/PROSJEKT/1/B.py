import numpy as np
import scipy.constants as scp
import matplotlib.pyplot as plt

# INITIAL VALUES
l = 10e-6
T = 2e3
n = 100
k_b = scp.Boltzmann
m = 1e-28

# TIME AND TIME STEP
time_array = np.linspace(0, 10e-9, 2000)  # How long the code should run
dt = time_array[1] - time_array[0]  # Time step

# POSITION ARRAY
position = np.random.uniform(0, l, (n, 3))  #Creates an uniform distribution for positions


# VELOCITIES
velocity = np.zeros((n, 3))     # an empty array for velocity
v = np.sqrt((8*k_b*T)/(np.pi*m))    # uses the formula from part1.pdf Challanges A 1, where we found the formula for speed of a praticle by some variables

for i in range(n):
    theta = np.random.uniform(0, np.pi) # picking a random direction for the particles to move in
    phi = np.random.uniform(0, 2 * np.pi)

    v_x = v * np.sin(theta) * np.cos(phi)   # using v = sqrt(v_x^2 +v_y^2 +v_z^2) to calculate a velocity for each particle that sums up to v
    v_y = v * np.sin(theta) * np.sin(phi)   # v_n is the decomposed v in each of the 3D 
    v_z = v * np.cos(theta)

    velocity[i] = [v_x, v_y, v_z]   # fill the previously empty v array with values

# BOUNDARY CONDITIONS
r = 0.25*l**2

center = np.array([0, 0])


# Function to check if a ball hits the hole
def hits_hole(pos):
    if pos[2] <= 0.01:
        distance_to_center = np.linalg.norm(pos[:2] - center)
        return distance_to_center <= r

def boundary(position, velocity, l, r):
    index = np.where((position >= l) | (position <= 0))
    velocity[index] *= -1
    for i, pos in enumerate(position):
        if hits_hole(pos):
            position[i] = np.array([0, 0, 0])
            velocity[i] = np.array([0, 0, 0])
    return position, velocity


print(boundary(position,velocity,l,r))


# Initialize a 3D array to store the positions of all particles over time
# Dimensions: [pos, vel for spatial dimensions (x, y, z)]
all_particle_trajectory = np.zeros((time_array.size, n, 3))


for index in range(time_array.size):
    position, velocity = boundary(position, velocity, l, r)
    position += velocity * dt
    all_particle_trajectory[index] = position
"""
for index in range(time_array.size):    #size is faster
    position += velocity * dt   # update the position according to is velocity and timestep
    velocity = boundary(position, velocity, l, r)[1]  # Updates the velocity according to the boundrary (see line 34)

    all_particle_trajectory[index] = position[0]  # store the positional data from whatever particle it just calculated before it moves on to the next 
"""
first_particle_trajectory = all_particle_trajectory[:, 0, :]    # makes a variable which only store data from the first particle


####################################
# PLOTTING (first particle)
"""
plt.title("(x,y,z) position of one particle")
plt.subplot(3, 1, 1)
plt.plot(time_array, first_particle_trajectory[:, 0], label="x")
plt.ylabel("x position")

plt.subplot(3, 1, 2)
plt.plot(time_array, first_particle_trajectory[:, 1], label="y")
plt.ylabel("y position")

plt.subplot(3, 1, 3)
plt.plot(time_array, first_particle_trajectory[:, 2], label="z")
plt.ylabel("z position")
plt.xlabel("Time (s)")

plt.show()
"""
####################################
# ANIMATION
import matplotlib.animation as animation
# Create a figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Setup for the first subplot
ax1.set_title("Animation of the particles (x-z plane)")
ax1.set_xlabel("x-axis")
ax1.set_ylabel("z-axis")
sc1 = ax1.scatter(position[:, 0], position[:, 2],s =10)
ax1.set_xlim(0, l)
ax1.set_ylim(0, l)

# Setup for the second subplot
ax2.set_title("Animation of the particles (x-y plane)")
ax2.set_xlabel("x-axis")
ax2.set_ylabel("y-axis")
sc2 = ax2.scatter(position[:, 0], position[:, 1], s =10)
ax2.set_xlim(0, l)
ax2.set_ylim(0, l)

def update(frame):
    global position, velocity  # retrieves the "global" values for position and velocity
    position += velocity * dt
    
    # Check for collisions and update velocities
    for i in range(n):
        velocity[i] = boundary(position[i], velocity[i], l, r)[1]
    
    # Update plot for each dt
    sc1.set_offsets(np.column_stack((position[:, 0], position[:, 2])))
    sc2.set_offsets(position[:, :2])

ani = animation.FuncAnimation(fig, update, frames=240, interval=20)

plt.tight_layout()
plt.show()

atm = 101235   # Pascal
print(int((atm*l**3)/(T*scp.gas_constant))) # to find amount of particels 


#####################
#     TO DO
#####################

# IMPLEMENT IDEAL GAS LAW:
# pressure*volume= n*ideal_gas_constant*temperature

# IMPLEMENT ENERGY OF MOLECULE IN IDEAL GAS


