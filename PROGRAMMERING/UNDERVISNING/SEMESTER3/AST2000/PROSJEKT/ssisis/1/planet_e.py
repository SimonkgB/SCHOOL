#ikke kodemal
import numpy as np
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission

import sys
sys.path.append("C:/Users/simon/Skrivebord/ssisis")  # HUSK!!!! Add the directory containing the script
import rocket_calculations as r_cal
import consts as cs


# Initialize solar system and mission
system = SolarSystem(cs.seed)   
mission = SpaceMission(cs.seed)

r0 = system.initial_positions[:, 0] # initial position of the planet
v0 =  system.initial_velocities[:, 0]   # initial velocity of the planet

# Set up mission parameters
mission.set_launch_parameters(r_cal.total_thrust_z, r_cal.mass_flow[2], cs.rocket_mass_fixed,   
                              cs.time_to_v_esc,
                              r0+np.array([cs.radius_p0_au,0]), 0)
mission.launch_rocket(time_step=0.01)

mass_used_up=mission.rocket_mass_loss_rate*utils.yr_to_s(mission.time_after_launch) 

print(f"Inital fuel: {mission.initial_fuel_mass} kg")   
print(f"Initial position: {mission.launch_position}")   
print(f"The planets initial position is: {r0}") 
print(f"The time it takes to reach v_esc is: {utils.yr_to_s(mission.time_after_launch)}")   

print(f"The fuel used up is: {mass_used_up} kg")    
print(f"The rest of the rocket made of fuel: {cs.rocket_mass_fixed-mass_used_up-cs.rocket_payload} kg") 

"""
Terminal> python planet_e.py
Total Thrust for one motor: [8.07497883e-15 6.47952603e-14 7.02098771e-12] N
Number of Motors needed z dir: 4.108646584245719e+17
Total Thrust for all motors in z dir: 2884675.717434528 N
Mass Flow: [8.82133235e-22 7.07841516e-21 3.78156036e+02]
Total final mass for reaching escape vel (rocket eq): 8132.99452071161167 kg
Gravity on surface: 15.831868111403939 m/s^2
Rocket was moved down by 1.59275e-05 m to stand on planet surface.
New launch parameters set.
Launch completed, reached escape velocity in 517.921 s.
Inital fuel: 204000.0 kg
Initial position: [1.35903986 0.        ]
The planets initial position is: [1.35897907 0.        ]
The time it takes to reach v_esc is: 517.9207920792079
The fuel used up is: 195854.87375637106 kg
The rest of the rocket made of fuel: 4145.12624362894 kg
The energy with the two methods are (8.243459975504143e-20, 8.243459975504143e-20)
The pressure in the box is: 0.5495639983669427 Pa
The temperature in the box is: 3980.475836848778 K
"""