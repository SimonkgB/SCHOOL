import numpy as np
import scipy.constants as scp_c
import math


import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED")  # Add the directory containing the script
import consts as cs
import rocket_calculations as r_cal


def gravity0(mass, radius):
    return cs.Gc*mass/(radius**2)

def escape_vel(mass, radius):
    return np.sqrt(2*(gravity0(mass, radius))*(radius))

radius_ = cs.radius_p0+cs.radius_p0*2

# n motors for ESCAPING THE PLANET       V_esc = F/m*t
def n_motors(mass, time):
    thrust= r_cal.thrust(r_cal.velocity_rocket)
    return (escape_vel(mass, radius_))*mass/(thrust*time)



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
    exponent =-deltaV*mDot/F
    fuel_mass = (1-math.exp(exponent))*M/math.exp(exponent)
    return fuel_mass

#print(n_motors(cs.mass_p0, cs.time_to_v_esc)[2])

fuel_mass = calculate_fuel_mass(escape_vel(cs.mass_p0, cs.radius_p0), r_cal.massflow(), r_cal.thrust(r_cal.velocity_rocket)[2],cs.rocket_mass)
#print(f"The mass of the fuel consumed is {fuel_mass} kg.")

#print(f"amount of boosters required to reach escape velocity withing {time_to_v_esc/60} min : {n_boosters}")