from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append("C:/Users/simon/Skrivebord/ssisis")  # HUSK!!!! Add the directory containing the script
import consts as cs
import rocket_calculations as r_cal

# Constants
def rocket(t, y, f_t, mu_r, phi, G, mu_p):
    r, v =y
    drdt= v
    dvdt =f_t/(mu_r-phi*t)-G*mu_p/r**2
    return [drdt, dvdt]

# Initial conditions
r_0 =cs.radius_p0
v_0 =0

# Parameters
f_t =r_cal.total_thrust_z
phi =r_cal.mass_flow[2]
mu_r=cs.rocket_mass_fixed
G   =cs.Gc
mu_p=cs.mass_p0

# Time span
t_span =[0, 500]


target_velocity =np.sqrt(2*G*mu_p/r_0)


# Solve ODE
sol =solve_ivp(rocket, t_span, [r_0, v_0], args=(f_t, mu_r, phi, G, mu_p), t_eval=np.linspace(0, 400, 500))
maz =np.where((sol.y[1])>=target_velocity)
print(sol.t[maz])

# Plotting
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(sol.t, sol.y[0])
plt.ylabel("Height")
plt.title("Rocket Height")

plt.subplot(2, 1, 2)
plt.plot(sol.t, sol.y[1])
plt.ylabel("Velocity")
plt.title("Rocket Velocity")

plt.show()