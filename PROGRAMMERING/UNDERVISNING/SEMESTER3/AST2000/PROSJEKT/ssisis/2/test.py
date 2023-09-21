import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import csv
import os
import pandas as pd

sys.path.append("C:/Users/simon/Skrivebord/ssisis/1") 
import consts as cs
# Initialize solar system bodies
# Each row represents a body: [mass (in solar masses), x (in AU), y (in AU), vx (in AU/yr), vy (in AU/yr)]

bodies = cs.conditions
p_star = bodies[0]
p_big = bodies[4]
bodies = np.vstack((p_star, p_big))

forces = np.zeros((bodies.shape[0], 2))

def compute_forces():
    global forces
    forces.fill(0)
    G = 4*np.pi**2  # AU^3 yr^-2 M_sun^-1    39.47841760435743
    for i in range(len(bodies)):
        for j in range(i+1, len(bodies)):
            r = bodies[j, 1:3] - bodies[i, 1:3]
            r_mag = np.linalg.norm(r)
            force_mag = G*bodies[i, 0]*bodies[j, 0]/r_mag**3
            force = force_mag * r
            forces[i] += force
            forces[j] -= force

def compute_center_of_mass(bodies):
    total_mass = np.sum(bodies[:, 0])
    return np.sum(bodies[:, 0, None]*bodies[:, 1:3], axis=0)/total_mass # None adds a new axis to the array (asked chat gpt about this still dont understand it completely)

def leapfrog_integrate(dt):
    global bodies, forces
    # Half update velocities
    for i in range(len(bodies)):
        bodies[i, 3:5] += 0.5 * forces[i] * dt / bodies[i, 0]
    # Update positions
    for i in range(len(bodies)):
        bodies[i, 1:3] += bodies[i, 3:5] * dt
    # Compute new forces
    compute_forces()
    # Finish updating velocities
    for i in range(len(bodies)):
        bodies[i, 3:5] += 0.5 * forces[i] * dt / bodies[i, 0]






def write_to_csv(N, dt, bodies, csv_file='two_body_problem_adaptable_to_n.csv'):
    num_planets = len(bodies) - 1  # Excluding the star
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Create headers
        headers = ["TimeStep"]
        headers.extend(['Step', 'Star Mass', 'Star x', 'Star y', 'Star vx', 'Star vy'])
        for i in range(num_planets):
            headers.extend([f"Planet_{i}_Mass", f"Planet_{i}_x", f"Planet_{i}_y", f"Planet_{i}_vx", f"Planet_{i}_vy"])
        
        csvwriter.writerow(headers)
        
        # Time integration loop
        for step in range(N):
            leapfrog_integrate(dt)
            row = [step * dt]
            for body in bodies:
                row.extend(list(body))
            csvwriter.writerow(row)

num_planets = len(bodies)
dt=1e-2/20
N = int(cs.year*20/dt)
csv_file_name = 'two_body_problem_adaptable_to_n.csv'


if os.path.exists(csv_file_name):
    print("CSV file exists. Plotting data.")
    df =pd.read_csv(csv_file_name)

else:
    print("CSV file does not exist. Writing to csv.")
    write_to_csv(N, dt, bodies, csv_file_name)



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_energy(df):
    steps = np.arange(len(df))
    
    # Extract data from DataFrame
    star_mass = df['Star Mass'].values
    star_x = df['Star x'].values
    star_y = df['Star y'].values
    star_vx = df['Star vx'].values
    star_vy = df['Star vy'].values
    
    planet_mass = df['Planet_0_Mass'].values
    planet_x = df['Planet_0_x'].values
    planet_y = df['Planet_0_y'].values
    planet_vx = df['Planet_0_vx'].values
    planet_vy = df['Planet_0_vy'].values
    
    # Create bodies array
    bodies_mass = np.vstack((star_mass, planet_mass)).T
    bodies_x = np.vstack((star_x, planet_x)).T
    bodies_y = np.vstack((star_y, planet_y)).T
    bodies_vx = np.vstack((star_vx, planet_vx)).T
    bodies_vy = np.vstack((star_vy, planet_vy)).T
    
    # Calculate kinetic energy
    kinetic_energy = 0.5 * np.sum(bodies_mass * (bodies_vx**2 + bodies_vy**2), axis=1)
    
    # Calculate potential energy
    r = np.linalg.norm(np.array([bodies_x[:, 0], bodies_y[:, 0]]) - np.array([bodies_x[:, 1], bodies_y[:, 1]]), axis=0)
    potential_energy = -(4 * np.pi**2 * bodies_mass[:, 0] * bodies_mass[:, 1]) / r
    
    # Calculate center of mass
    total_mass = np.sum(bodies_mass, axis=1)
    cm_x = np.sum(bodies_mass * bodies_x, axis=1) / total_mass
    cm_y = np.sum(bodies_mass * bodies_y, axis=1) / total_mass
    cm = np.vstack((cm_x, cm_y)).T
    
    # Calculate energy relative to the center of mass
    kinetic_energy_cm = kinetic_energy - 0.5 * np.sum(cm**2, axis=1)
    total_energy = kinetic_energy_cm + potential_energy
    
    # Create the plot
    plt.figure()
    plt.plot(steps, kinetic_energy_cm, label='Kinetic Energy')
    plt.plot(steps, potential_energy, label='Potential Energy')
    plt.plot(steps, total_energy, label='Total Energy')
    plt.xlabel('Time Step')
    plt.ylabel('Energy (AU^2 yr^-2 M_sun)')
    plt.title('Change in Energy Relative to Center of Mass')
    plt.legend()
    plt.show()

# Usage example
# Assuming df is your DataFrame
# plot_energy(df)


# Usage example
plot_energy(df)
# Usage example






trails = [[] for _ in bodies]
trail_length = 1000  # Number of past positions to keep

# Initialize animation
fig, ax = plt.subplots(figsize=(12, 12))

# Set axis limits
a = 7.5
ax.set_xlim(-a, a)
ax.set_ylim(-a, a)

points = [ax.plot([], [], 'o', color=cs.color_dic[i])[0] for i in range(len(bodies))]
lines = [ax.plot([], [], '-', alpha=0.5,color=cs.color_dic[i])[0] for i in range(len(bodies))]  # Lines for trails
cm_point, = ax.plot([], [], 'X', color='red', markersize=4)  # Center of mass point

def init():
    for point in points:
        point.set_data([], [])
    for line in lines:
        line.set_data([], [])
    cm_point.set_data([], [])
    return points + lines + [cm_point]

def update(frame):
    leapfrog_integrate(dt)
    
    # Compute the center of mass
    x_cm, y_cm = compute_center_of_mass(bodies)
    
    # Shift all bodies so that the center of mass is at (0, 0)
    bodies[:, 1] -= x_cm
    bodies[:, 2] -= y_cm
    
    for i, (point, body, trail, line) in enumerate(zip(points, bodies, trails, lines)):
        point.set_data(body[1], body[2])
        
        # Update the trail with the new position
        trail.append((body[1], body[2]))
        
        # Only keep the last 'trail_length' positions
        trail = trail[-trail_length:]
        trails[i] = trail
        
        # Update the line data for the trail
        x_vals, y_vals = zip(*trail)
        line.set_data(x_vals, y_vals)
    
    # Since we've shifted everything, the center of mass is now at (0, 0)
    cm_point.set_data(0, 0)
    
    return points + lines + [cm_point]


ani = animation.FuncAnimation(fig, update, frames=range(N), init_func=init, blit=True, interval=0.01, repeat=False)

plt.show()
