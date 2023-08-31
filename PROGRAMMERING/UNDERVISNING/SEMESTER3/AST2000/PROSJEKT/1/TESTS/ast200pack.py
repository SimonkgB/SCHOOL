import numpy as np
import scipy.constants as scp_c
import ast2000tools.constants as ast_c

import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1/FINISHED")  # Add the directory containing the script
import goated as w 
import rocket_calculations as r_c
import rocket_capabilities as r_cap

import ast2000tools.utils as utils
seed = utils.get_seed("simm")

from ast2000tools.solar_system import SolarSystem
system = SolarSystem(seed)

from ast2000tools.space_mission import SpaceMission
mission = SpaceMission(seed)


print('My spacecraft has a mass of {:g} kg and a cross-sectional area of {:g} m^2.'
      .format(mission.spacecraft_mass, mission.spacecraft_area))


if not mission.rocket_launched:
    print('I have not launched the rocket yet. Let us do something about that!')
    mission.launch_rocket()