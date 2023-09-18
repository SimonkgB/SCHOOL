import numpy as np
import matplotlib.pyplot as plt

# Define parameters
i = 90  # Inclination angle in degrees
Rs = 1.0  # Radius of the star in arbitrary units
Rp = 0.1  # Radius of the planet in the same units as Rs

# Time array
time = np.linspace(0, 1, 1000)  # Time in arbitrary units

# Initialize relative flux array
relative_flux = np.ones_like(time)

# Simulate the transit (assuming the transit occurs around time=0.5)
transit_start =0.4
transit_end =0.6
transit_duration =transit_end-transit_start

# Calculate the gradual change in brightness
for t in np.arange(transit_start, transit_end, 0.01):
    dt = np.abs(time-t)
    change_factor =np.exp(-dt/(0.5 * transit_duration))
    flux_during_transit =(Rs**2-Rp**2)/Rs**2
    relative_flux -=change_factor*(1-flux_during_transit)

# Add Gaussian noise
noise_std_dev =1e-4  # Standard deviation of the Gaussian noise
noise =np.random.normal(0, noise_std_dev, size=time.shape)
relative_flux +=noise

# Plot the light curve
plt.figure(figsize=(10, 6))
plt.plot(time, relative_flux, label='Simulated Light Curve')
plt.xlabel('Time')
plt.ylabel('Relative Flux')
plt.title('Simulated Gradual Light Curve with Gaussian Noise')
plt.legend()
plt.show()