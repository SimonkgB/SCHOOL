import numpy as np
import matplotlib.pyplot as plt

r_p =0.5
r_s =1
n= 1000


L =1
A_s =np.pi*r_s**2
A_p =np.pi*r_p**2

t =np.linspace(-2, 2, n)
hole_center =np.array([0, 0])  # center of star in 2D

L_s = L/A_s
print(L_s*(A_s-A_p))
def f(pos_y):
    a = np.ones(n)
    for i, pos in enumerate(pos_y):
        if np.abs((pos+r_p)-r_s)<= r_s:
            a[i] = A_s-A_p
        else:
            a[i] = A_s
    return a

a = f(t)
L_t = L_s*a

plt.plot(t, L_s)
plt.xlabel("Position of Planet (y-axis)")
plt.ylabel("Obscured Area of Star")
plt.show()
