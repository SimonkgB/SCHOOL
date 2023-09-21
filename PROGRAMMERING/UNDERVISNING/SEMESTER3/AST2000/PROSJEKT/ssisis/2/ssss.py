import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/1")  # HUSK!!!! Add the directory containing the script
import consts as cs

def generate_light_curve(N=1001, transit_fraction=0.5):
    t = np.linspace(0, 102, N)
    star_radius = cs.radius_sun
    p_radius = cs.radius_p0[3]
    star_area = star_radius**2 * np.pi
    planet_area = p_radius**2 * np.pi
    relative_area = planet_area / star_area
    light_curve = np.ones(N)
    
    transit_duration = int(transit_fraction * N)
    start_time = (N - transit_duration) // 2
    end_time = start_time + transit_duration
    
    light_curve[start_time:end_time] = 1 - relative_area
    light_curve += np.random.normal(-1e-4, 1e-4, N)  # Reduced noise level for clarity
    return t, light_curve

t, lightcurve = generate_light_curve()

plt.plot(t, lightcurve)
plt.show()
