
import numpy as np
import scipy.constants as scp_c
import ast2000tools.constants as ast_c

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED")  #C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED Add the directory containing the script
import goated as w 
import rocket_calculations as r_cal
import rocket_capabilities as r_cap
import consts as cs

import ast2000tools.utils as utils
seed = utils.get_seed("simm")



from ast2000tools.solar_system import SolarSystem
system = SolarSystem(seed)

#print(system.print_info())

from ast2000tools.space_mission import SpaceMission
mission = SpaceMission(seed)

x0 =system.initial_positions[0,0]
y0 =system.initial_positions[1,0]
vx0 =system.initial_velocities[0,0]
vy0 =system.initial_velocities[1,0]
r0 =np.array([x0, y0])
v0 =np.array([vx0, vy0])
num_time_steps =1000

"""
r =np.zeros((num_time_steps, 2))
v =np.zeros((num_time_steps, 2))
r[0] =r0
v[0] =v0
for i in range(num_time_steps-1):
    r[i+1] =r[i] +v[i]*dt
    v[i+1] =v[i] +w.acceleration(r[i])*dt
"""
#r_cap.fuel_mass

<<<<<<< Updated upstream
mission.set_launch_parameters(r_cal.total_thrust, r_cal.massflow(), cs.rocket_fuel+cs.rocket_payload,
                              cs.time_to_v_esc,
                              r0+np.array([cs.radius_p0_au,0]), 0)
mission.launch_rocket(time_step=0.01)
=======
# Initialize solar system and mission
seed = utils.get_seed("simm")
system = SolarSystem(seed)
mission = SpaceMission(seed)

# Initial conditions
r0 = system.initial_positions[:, 0]
v0 = system.initial_velocities[:, 0]


mission.set_launch_parameters(r_cal.total_thrust_2, r_cal.mass_flow[2], cs.rocket_mass_fixed,
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
>>>>>>> Stashed changes
