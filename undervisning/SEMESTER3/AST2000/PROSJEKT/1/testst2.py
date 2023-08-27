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
lv = np.array([0.25 * l ** 2, 0.25 * l ** 2])
print(lv)

def boundary(position, velocity, l, lv):
    new_position = np.copy(position)
    new_velocity = np.copy(velocity)
    index = np.where((new_position >= l) | (new_position <= 0))
    new_velocity[index] *= -1
    return new_position, new_velocity

# Initialize a 3D array to store the positions of all particles over time
all_particle_trajectory = np.zeros((time_array.size, n, 3))

for index, t in enumerate(time_array):
    position, velocity = boundary(position, velocity, l, lv)
    all_particle_trajectory[index] = position
    position += velocity * dt

first_particle_trajectory = all_particle_trajectory[:, 0, :]

# ANIMATION
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.set_title("Animation of the particles (x-z plane)")
ax1.set_xlabel("x-axis")
ax1.set_ylabel("z-axis")
sc1 = ax1.scatter(position[:, 0], position[:, 2], s=10)
ax1.set_xlim(0, l)
ax1.set_ylim(0, l)

ax2.set_title("Animation of the particles (x-y plane)")
ax2.set_xlabel("x-axis")
ax2.set_ylabel("y-axis")
sc2 = ax2.scatter(position[:, 0], position[:, 1], s=10)
ax2.set_xlim(0, l)
ax2.set_ylim(0, l)

def update(frame):
    global position, velocity
    position, velocity = boundary(position, velocity, l, lv)
    position += velocity * dt
    sc1.set_offsets(np.column_stack((position[:, 0], position[:, 2])))
    sc2.set_offsets(position[:, :2])

ani = animation.FuncAnimation(fig, update, frames=240, interval=20)

plt.tight_layout()
plt.show()
