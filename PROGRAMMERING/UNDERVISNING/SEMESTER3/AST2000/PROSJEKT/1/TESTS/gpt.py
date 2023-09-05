import numpy as np
import scipy.constants as scp_c

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED")  #C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED Add the directory containing the script
import goated as w 
import consts as cs

# Given Constants
Gc = scp_c.gravitational_constant  # Gravitational constant
mass_p0 = cs.mass_p0  # Mass of the planet in kg (Earth as an example)
radius_p0 = cs.radius_p0  # Radius of the planet in meters (Earth as an example)
rocket_payload = cs.rocket_payload  # kg
hydrogen2_mass = cs.hydrogen2_mass  # Mass of a particle in kg

# Step 1: Calculate Escape Velocity
v_esc = np.sqrt(2 * Gc * mass_p0 / radius_p0)
print(f'Escape velocity needed: {v_esc} m/s')

# Step 2: Calculate Thrust (Assuming escaped_velocities is a list of escaped velocities)
escaped_velocities = np.array([1e5, 2e5, 3e5])  # Replace with your actual escaped velocities
thrust = np.sum(hydrogen2_mass * w.escaped_velocities[:,2])
print(f'Total thrust: {thrust} N')

# Step 3: Rocket Equation
# Assuming average exhaust velocity is the mean of escaped velocities
v_exhaust = np.mean(escaped_velocities)

# Initial mass is the payload plus fuel, final mass is just the payload
m_initial = rocket_payload  # Initial mass (without fuel)
m_final = rocket_payload  # Final mass (payload only)

# Calculate the fuel needed to achieve escape velocity
fuel_needed = m_initial - np.exp(-v_esc / v_exhaust) * m_final
print(f'Fuel mass needed: {fuel_needed} kg')

# Step 4: Number of Boosters
booster_capacity = 100_000  # kg (Assumed capacity of one booster)
num_boosters = np.ceil(fuel_needed / booster_capacity)
print(f'Number of boosters needed: {int(num_boosters)}')