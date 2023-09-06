
import numpy as np
import scipy.constants as scp_c
import ast2000tools.constants as ast_c
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission

import sys
sys.path.append("C:/Users/simon/Skrivebord/ssisis")  #C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED Add the directory containing the script
import rocket_calculations as r_cal
import consts as cs





# Initialize solar system and mission
seed = utils.get_seed("simm")
system = SolarSystem(seed)
mission = SpaceMission(seed)

r0 = system.initial_positions[:, 0]
v0 =  system.initial_velocities[:, 0]


mission.set_launch_parameters(r_cal.total_thrust_z, r_cal.mass_flow[2], cs.rocket_mass_fixed,
                              cs.time_to_v_esc,
                              r0+np.array([cs.radius_p0_au,0]), 0)
mission.launch_rocket(time_step=0.01)

mass_used_up=mission.rocket_mass_loss_rate*utils.yr_to_s(mission.time_after_launch)

print(f"inital fuel: {mission.initial_fuel_mass}")
print(f"initial position: {mission.launch_position}")
print(f"the planets initial position is: {r0}")
print(f"the time it takes to reach v_esc is: {utils.yr_to_s(mission.time_after_launch)}")

print(f"the mass used up is: {mass_used_up}")
print(f"the rest of the mass: {cs.rocket_mass_fixed-mass_used_up}")