import numpy as np
import math

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED")  # Add the directory containing the script
import goated as w
import boundrary_conditions as b_c
import consts as cs


momentum_particles = np.sum(w.escaped_velocities*cs.hydrogen2_mass, axis=0)  # indicates that we are suming the x-components so we dont need a for loop
momentum_rocket = -momentum_particles
velocity_rocket = momentum_rocket / cs.rocket_mass


# function for calculating total force
def thrust(v_r):
    force_x = v_r[0]/cs.time_step
    force_y = v_r[1]/cs.time_step
    force_z = v_r[2]/cs.time_step
    return np.array([force_x, force_y, force_z])*cs.hydrogen2_mass



def calculate_temperature_in_box(velocity):
    kinetic_energy = 1/2*cs.hydrogen2_mass*np.sum(velocity**2, axis=1)
    avg_kinetic_energy =np.mean(kinetic_energy)
    temperature =(2*avg_kinetic_energy)/(3*cs.boltzmann_constant)
    return temperature


def pressure():
    return cs.num_particles/(cs.box_length**3)*cs.boltzmann_constant*calculate_temperature_in_box(w.velocity) # as soon as a particle escape a new one replaces it with teh same velocity but a diffrent rvect


def energy():
    a1= 1/2*cs.hydrogen2_mass*np.mean(np.sum(w.velocity**2, axis=1))
    a2= 3/2*cs.boltzmann_constant*calculate_temperature_in_box(w.velocity)
    return a1, a2


def gravity0(mass, radius):
    return cs.Gc*mass/(radius**2)


def escape_vel(mass, radius):
    return np.sqrt(2*(gravity0(mass, radius))*(radius))

# n motors for ESCAPING THE PLANET       V_esc = F/m*t
def n_motors(t_r_mass, time):
    return (escape_vel(cs.mass_p0, cs.radius_p0))*t_r_mass/(thrust(velocity_rocket)*time)


def calculate_fuel_mass(deltaV, mDot, F, M):
    """
    Calculate the mass of the fuel consumed by a rocket.

    Parameters:
    deltaV (float): Speed boost or change in velocity in m/s
    mDot (float): Fuel consumption rate in kg/s
    F (float): Thrust force in Newtons
    M (float): Initial mass of the rocket in kg

    Returns:
    float: Mass of the fuel consumed in kg
    """
    exponent = -deltaV * mDot / F
    print("Exponent:", exponent)
    print("Exp(Exponent):", math.exp(exponent))
    
    fuel_mass = (1 - math.exp(exponent)) * M / math.exp(exponent)
    return fuel_mass

total_thrust = thrust(velocity_rocket)[2]*n_motors(cs.rocket_payload, cs.time_to_v_esc)[2]
print(total_thrust)

def massflow():
    return abs(total_thrust/np.mean(w.escaped_velocities[2])) # for n particles this will stay constant
print(massflow())

print(n_motors(cs.rocket_payload, cs.time_to_v_esc))



fuel_mass = calculate_fuel_mass(escape_vel(cs.mass_p0, cs.radius_p0), massflow(), total_thrust, cs.rocket_payload)


print(f"The mass of the fuel consumed is {fuel_mass} kg.")
"""
print(f"using the formula for kinetic energy: {energy()[0]}, and using the formula with temperature: {energy()[1]}")
print(f"amount of boosters required to reach escape velocity withing {time_to_v_esc/60} min : {n_motors(cs.mass_p0, time_to_v_esc)}")
print(f"The temperature of the system is {calculate_temperature_in_box(w.velocity)} K")
print(f"The pressure of the system is: {pressure()}")
print(f"The energy of teh system is: {energy()}")
print(f"The velocity of teh rocket is {v_r[2]}]")

print(f"kraft done by particles: {thrust(velocity_rocket)[2]}") 
"""