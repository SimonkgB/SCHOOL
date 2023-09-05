
import numpy as np
import scipy.constants as scp_c
import ast2000tools.constants as ast_c

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED")  #C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED Add the directory containing the script
import goated as w 
import rocket_calculations as r_cal
import consts as cs

import ast2000tools.utils as utils
seed = utils.get_seed("simm")



from ast2000tools.solar_system import SolarSystem
system = SolarSystem(seed)

#print(system.print_info())

from ast2000tools.space_mission import SpaceMission
mission = SpaceMission(seed)

import numpy as np
import scipy.constants as scp_c
import ast2000tools.constants as ast_c
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission
import matplotlib.pyplot as plt

# Import your custom modules
import goated as w 
import rocket_calculations as r_cal
import consts as cs

# Initialize solar system and mission
seed = utils.get_seed("simm")
system = SolarSystem(seed)
mission = SpaceMission(seed)

# Initial conditions
x0, y0 = system.initial_positions[0, 0], system.initial_positions[1, 0]
vx0, vy0 = system.initial_velocities[0, 0], system.initial_velocities[1, 0]
r0 = np.array([x0, y0])
v0 = np.array([vx0, vy0])


import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
mass_sun = 1.989e30  # Mass of the sun in kg
mass_planet = 5.972e24  # Mass of the planet in kg (Earth for example)
time_step = 4000  # Time step in seconds
num_time_steps = 10000  # Number of time steps

# Initial conditions
#r0 = np.array([1.496e11, 0])  # Initial position in meters (1 AU from the sun)
#v0 = np.array([0, 2.978e4])  # Initial velocity in m/s

# Initialize arrays to store trajectory
positions = np.zeros((num_time_steps, 2))
velocities = np.zeros((num_time_steps, 2))
positions[0] = r0
velocities[0] = v0

# Function to calculate gravitational force
def force_between_star_planet(mass, position):
    r = np.linalg.norm(position)
    F_magnitude = (G * mass_sun * mass) / (r ** 2)
    r_hat = position / r
    return -F_magnitude * r_hat

# Verlet integration loop
for i in range(1, num_time_steps):
    # Calculate force at current position
    F_current = force_between_star_planet(mass_planet, positions[i-1])
    
    # Update position
    positions[i] = positions[i-1] + velocities[i-1] * time_step + 0.5 * (F_current / mass_planet) * (time_step ** 2)
    
    # Calculate force at new position
    F_new = force_between_star_planet(mass_planet, positions[i])
    
    # Update velocity
    velocities[i] = velocities[i-1] + 0.5 * (F_current / mass_planet + F_new / mass_planet) * time_step

# Plotting the orbit
# Plotting the orbit
plt.figure()



plt.plot(positions[:, 0], positions[:, 1], label='Orbit')

# Adding the star at the origin
plt.scatter(0, 0, color='yellow', label='Star', zorder=5, s= 400)

# Adding the planet's initial and final positions
plt.scatter(positions[0, 0], positions[0, 1], color='blue', label='Planet Start', zorder=5, s= 20)
plt.scatter(positions[-1, 0], positions[-1, 1], color='red', label='Planet End', zorder=5)

plt.xlabel('X position (m)')
plt.ylabel('Y position (m)')
plt.title('Orbit of Planet Around Star')
plt.legend(loc='upper left')
plt.show()











mission.set_launch_parameters(r_cal.total_thrust_2[2]*10, r_cal.mass_flow[2], cs.rocket_mass_fixed,
                              cs.time_to_v_esc,
                              r0+np.array([cs.radius_p0_au,0]), 0)
mission.launch_rocket(time_step=0.01)

mass_used_up=mission.rocket_mass_loss_rate*utils.yr_to_s(mission.time_after_launch)

print(f"inital fuel: {mission.initial_fuel_mass}")
print(f"initial position: {mission.launch_position}")
print(f"the planets initial position is: {r0}")
print(f"the time it takes to reach v_esc is: {mission.time_after_launch}")

print(f"the mass used up is: {mass_used_up}")
print(f"the rest of the mass: {cs.rocket_mass_fixed-mass_used_up}")