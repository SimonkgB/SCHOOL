import numpy as np
import scipy.constants as scp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
box_length = 10e-6  # Length of the box in meters
temperature = 2e3  # Temperature in Kelvin
num_particles = 100  # Number of particles
boltzmann_constant = scp.Boltzmann  # Boltzmann constant
particle_mass = 1e-28  # Mass of a particle in kg

# Time and Time Step
num_time_steps = 2000  # Number of time steps
time_step = 10e-9 / num_time_steps  # Time step in seconds

def initialize_velocity(num_particles, temperature, boltzmann_constant, particle_mass):
    # Initialize velocities based on the Maxwell-Boltzmann distribution
    velocity = np.zeros((num_particles, 3))
    v_avg = np.sqrt((8 * boltzmann_constant * temperature) / (np.pi * particle_mass))
    for i in range(num_particles):
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2 * np.pi)
        v_x = v_avg * np.sin(theta) * np.cos(phi)
        v_y = v_avg * np.sin(theta) * np.sin(phi)
        v_z = v_avg * np.cos(theta)
        velocity[i] = [v_x, v_y, v_z]
    return velocity

def boundary_conditions(position, velocity, box_length, hole_radius, hole_center):
    # Reflective boundary conditions and hole at the bottom
    index = np.where((position >= box_length) | (position <= 0))
    velocity[index] *= -1
    for i, pos in enumerate(position):
        distance_to_center = np.linalg.norm(pos[:2] - hole_center)
        if distance_to_center <= hole_radius and pos[2] <= 0.01:
            position[i] = np.array([0, 0, 0])
            velocity[i] = np.array([0, 0, 0])
    return position, velocity

# Initialize position and velocity
position = np.random.uniform(0, box_length, (num_particles, 3))
velocity = initialize_velocity(num_particles, temperature, boltzmann_constant, particle_mass)

# Hole properties
hole_radius = 0.25e-6  # Radius of the hole in meters
hole_center = np.array([box_length / 2, box_length / 2])  # Center of the hole

# Main simulation loop
all_particle_trajectory = np.zeros((num_time_steps, num_particles, 3))
for index in range(num_time_steps):
    position, velocity = boundary_conditions(position, velocity, box_length, hole_radius, hole_center)
    position += velocity * time_step
    all_particle_trajectory[index] = position

# Animation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Setup for the first subplot
ax1.set_title("Animation of the particles (x-z plane)")
ax1.set_xlabel("x-axis")
ax1.set_ylabel("z-axis")
sc1 = ax1.scatter(position[:, 0], position[:, 2], s=20)
ax1.set_xlim(0, box_length)
ax1.set_ylim(0, box_length)

# Setup for the second subplot
ax2.set_title("Animation of the particles (x-y plane)")
ax2.set_xlabel("x-axis")
ax2.set_ylabel("y-axis")
sc2 = ax2.scatter(position[:, 0], position[:, 1], s=20)
ax2.set_xlim(0, box_length)
ax2.set_ylim(0, box_length)

def update(frame, position, velocity, box_length, hole_radius, hole_center):
    position, velocity = boundary_conditions(position, velocity, box_length, hole_radius, hole_center)
    position += velocity * time_step
    sc1.set_offsets(np.column_stack((position[:, 0], position[:, 2])))
    sc2.set_offsets(position[:, :2])

ani = animation.FuncAnimation(fig, update, frames=num_time_steps, fargs=(position, velocity, box_length, hole_radius, hole_center), interval=20, repeat=False)

plt.tight_layout()
plt.show()