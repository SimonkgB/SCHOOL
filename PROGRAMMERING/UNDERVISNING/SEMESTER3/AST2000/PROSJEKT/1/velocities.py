import numpy as np
import sys
sys.path.append("C:/Users/simon/Dokumenter/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/1")  # Add the directory containing the script
import consts as cs

def velocity_distribution(temprature):
    sigma = np.sqrt((cs.boltzmann_constant*cs.temperature)/(cs.hydrogen2_mass))   #check if correct
    return np.random.normal(0, sigma)

    
######################
# INITIAL VELOCITY FUNCTION
def setting_velocity(vel_dis):    # Initialize velocities for particles based on the Maxwell-Boltzmann distribution

    # Generate random angles
    theta =np.random.uniform(0,np.pi) # random intial angles
    phi =np.random.uniform(0, 2*np.pi)

    # VELOCITY COMPONENTS
    v_x =vel_dis*np.sin(theta)*np.cos(phi)   #sending the particles in random directions
    v_y =vel_dis*np.sin(theta)*np.sin(phi)    # Using v = np.sqrt(v_x^2 + v_y^2 + v_z^2)
    v_z =vel_dis*np.cos(theta)
    return np.array([v_x, v_y, v_z])

velocity =np.array([setting_velocity(velocity_distribution(cs.temperature)) for _ in range(cs.num_particles)])