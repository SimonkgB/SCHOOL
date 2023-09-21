import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

# Limb darkening
def limb_darkening(u1, u2, cos_theta):
    return 1 - u1 * (1 - cos_theta) - u2 * (1 - cos_theta)**2

# Calculate flux
def calculate_flux(r_star, r_planet, d, u1, u2):
    # Calculate impact parameter
    b = np.abs(d)
    
    # Calculate distance between centers
    r_center = np.sqrt(r_star**2 - b**2)
    
    # Check for full transit
    if d <= r_star - r_planet:
        return 1 - np.pi * r_planet**2 * limb_darkening(u1, u2, np.sqrt(1 - (d/r_star)**2)) / (np.pi * r_star**2)
    
    # Check for partial transit
    elif r_star - r_planet < d < r_star + r_planet:
        theta_1 = np.arccos((r_planet**2 - r_star**2 + d**2) / (2 * d * r_planet))
        theta_2 = np.arccos((r_star**2 - r_planet**2 + d**2) / (2 * d * r_star))
        
        A1 = r_planet**2 * theta_1
        A2 = r_star**2 * theta_2
        A3 = np.sqrt((r_planet + r_star)**2 - d**2) * np.sqrt((r_planet - r_star)**2 - d**2) / 2
        A_overlap = A1 + A2 - A3
        
        return 1 - A_overlap * limb_darkening(u1, u2, np.sqrt(1 - (d/r_star)**2)) / (np.pi * r_star**2)
    
    # No transit
    else:
        return 1.0

# Parameters
r_star = 1.0  # Radius of star in arbitrary units
r_planet = 0.1  # Radius of planet in arbitrary units
a = 5.0  # Semi-major axis in arbitrary units
i = 89.5  # Inclination in degrees
e = 0.2  # Eccentricity
omega = 0.0  # Argument of periastron in degrees
u1, u2 = 0.3, 0.2  # Limb darkening coefficients

# Time array
t = np.linspace(-1, 1, 1000)
T = 1.0  # Orbital period in arbitrary units
n = 2 * np.pi / T  # Mean motion

# Calculate mean anomaly
M = n * t

# Solve for eccentric anomaly (E) using Newton's method
E = M
for _ in range(20):
    E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))

# True anomaly
f = 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(E / 2))

# Radial distance
r = a * (1 - e**2) / (1 + e * np.cos(f))

# Projected separation
d = r * np.sqrt(1 - np.sin(i * np.pi / 180)**2 * np.sin(f + omega * np.pi / 180)**2)

# Calculate flux
flux = np.array([calculate_flux(r_star, r_planet, d_val, u1, u2) for d_val in d])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, flux)
plt.xlabel("Time (arbitrary units)")
plt.ylabel("Relative Flux")
plt.title("Transiting Exoplanet Light Curve")
plt.show()
