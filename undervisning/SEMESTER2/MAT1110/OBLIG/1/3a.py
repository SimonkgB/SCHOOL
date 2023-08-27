import numpy as np
import matplotlib.pyplot as plt

#tidsintervallet
t = np.linspace(0, np.pi, 150)

#funksjonen
def r(t):
    x = np.cos(t)
    y = np.sin(t)
    z = 4*np.sin(4*t)**2
    return x, y, z
x, y, z = r(t)

#plotter
fig = plt.figure()
axis = fig.add_subplot(111, projection="3d")
axis.plot(x, y, z)
axis.set_xlabel("x-akse")
axis.set_ylabel("y-akse")
axis.set_zlabel("z-akse")
plt.show()


"""
Terminal> Python.exe> 1.py
"""