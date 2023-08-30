import numpy as np
import scipy.constants as scp_c
import ast2000tools.constants as ast_c

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1")  # Add the directory containing the script
import goated as w
import boundrary_conditions as b_c
import velocities as velc
import consts as cs
import rocket_calculations as r_c

import ast2000tools.utils as utils
seed = utils.get_seed("simm")

from ast2000tools.solar_system import SolarSystem
system = SolarSystem(seed)

from ast2000tools.space_mission import SpaceMission
mission = SpaceMission(seed)

home_planet_idx = 0 # The home planet always has index 0
#print(f"My mission starts on planet {home_planet_idx}, which has a radius of {mission.system.radii[home_planet_idx]} kilometers")

#print(f"My system has a {system.star_mass} solar mass star with a radius of {system.star_radius} kilometers.")

mass_p0 = system.masses[home_planet_idx]*ast_c.m_sun
radii0 = system.radii[home_planet_idx]*1000

def gravity0(mass, radius):
    g = cs.Gc*mass/radius**2
    return g

def escape_vel(mass, radius):
    v_esc= np.sqrt(2*gravity0(mass, radius)*radius)
    return v_esc

time_to_v_esc = 10*60 # 10min

# n motors for ESCAPING THE PLANET       V_esc = F/m*t
def n_escape(fz, mass, time):
    a = escape_vel(mass_p0,radii0)*mass/(fz*time)
    return a

n_boosters = n_escape(r_c.fz, mass_p0, time_to_v_esc)
#print(f"amount of boosters required to reach escape velocity withing {time_to_v_esc/60} min : {n_boosters}")