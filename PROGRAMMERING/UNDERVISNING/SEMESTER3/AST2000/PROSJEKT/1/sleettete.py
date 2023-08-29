import numpy as np
import matplotlib.pyplot as plt

q = 1
l = 1
e = 1
 

x = np.arange(-2, 2, 0.5)
y = np.arange(-2, 2, 0.5)
 
X, Y = np.meshgrid(x, y)

r = np.sqrt(X**2 + Y**2)

u = (q / (2 * np.pi * e * l)) * (-1/X)
v = (q / (2 * np.pi * e * l)) * (1/Y)
 
# Creating plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.quiver(X, Y, u, v)
 

 
# Show plot
plt.show()
