import numpy as np
import scipy.constants as scp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# INITIAL VALUES
l = 10e-6
T = 2e3
n = 100
k_b = scp.Boltzmann
m = 1e-28

# TIME AND TIME STEP
time_array = np.linspace(0, 10e-9, 2000)
dt = time_array[1] - time_array[0]

# POSITION ARRAY
position = np.random.uniform(0, l, (n, 3))

# VELOCITIES
velocity = np.zeros((n, 3))
v = np.sqrt((8 * k_b * T) / (np.pi * m))

for i in range(n):
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2 * np.pi)
    v_x = v * np.sin(theta) * np.cos(phi)
    v_y = v * np.sin(theta) * np.sin(phi)
    v_z = v * np.cos(theta)
    velocity[i] = [v_x, v_y, v_z]

# BOUNDARY CONDITIONS
r = 0.25 * l ** 2
center = np.array([0, 0])

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

# Main simulation loop
all_particle_trajectory = np.zeros((time_array.size, n, 3))

for index in range(time_array.size):
    position, velocity = boundary(position, velocity, l, r)
    position += velocity * dt
    all_particle_trajectory[index] = position

# Your plotting and animation code can go here
# ANIMATION
import matplotlib.animation as animation
# Create a figure with 2 subplots# ANIMATION
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Setup for the first subplot
ax1.set_title("Animation of the particles (x-z plane)")
ax1.set_xlabel("x-axis")
ax1.set_ylabel("z-axis")
sc1 = ax1.scatter(position[:, 0], position[:, 2], s=20)
ax1.set_xlim(0, l)
ax1.set_ylim(0, l)

# Setup for the second subplot
ax2.set_title("Animation of the particles (x-y plane)")
ax2.set_xlabel("x-axis")
ax2.set_ylabel("y-axis")
sc2 = ax2.scatter(position[:, 0], position[:, 1], s=20)
ax2.set_xlim(0, l)
ax2.set_ylim(0, l)

def update(frame):
    global position, velocity
    position, velocity = boundary(position, velocity, l, r)
    position += velocity * dt
    
    # Update plot for each dt
    sc1.set_offsets(np.column_stack((position[:, 0], position[:, 2])))
    sc2.set_offsets(position[:, :2])

ani = animation.FuncAnimation(fig, update, frames=len(time_array), interval=20, repeat=False)

plt.tight_layout()
plt.show()
