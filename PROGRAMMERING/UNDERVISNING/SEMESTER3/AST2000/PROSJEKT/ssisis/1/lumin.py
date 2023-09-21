import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append("C:/Users/simon/OneDrive/Dokumenter/GitHub/SCHOOL/PROGRAMMERING/UNDERVISNING/SEMESTER3/AST2000/PROSJEKT/ssisis/1") 
import consts as cs

radius_s = cs.radius_sun
radius_p = cs.radius_p[3]
n = 1000
a = np.ones(n)

L = 1
A_s = np.pi*radius_s**2
A_p = np.pi*radius_p**2
a *= A_s


pos_y = np.linspace(-2, 2, n)


hole_center = np.array([0, 0])  # center of star in 2D
print(A_s-A_p)
L_s = L / A_s
print(L_s * (A_s - A_p))
for i, pos in enumerate(pos_y):
    distance_to_center_p = np.linalg.norm(np.array([0, pos]) - hole_center)

    h = radius_s + radius_p - distance_to_center_p
    if 0 <= h <= 2 * radius_p: # check if the planet is in front of the star
        chord_length = 2 * np.sqrt(radius_p**2 - (radius_p - h)**2)
        cosine_theta = (radius_p - h) / radius_p
        angle = np.arccos(np.clip(cosine_theta, -1, 1))
        segment_area = (radius_p**2 * angle - 0.5 * chord_length * (radius_p - h))
        a[i] = A_s-segment_area
    elif np.abs(distance_to_center_p)<= radius_s-radius_p:
        a[i] = A_s-A_p

L_t = L_s*a
noise_std_dev = 10e-4
L_t_noisy = L_t + np.random.normal(0, noise_std_dev, L_t.shape)

plt.plot(pos_y, L_t_noisy)
plt.xlabel("Position of Planet (x-axis)")
plt.ylabel("Luminoisty of Star")
plt.show()
