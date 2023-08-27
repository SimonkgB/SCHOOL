import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

_ = np.linspace(-1, 1, 100)
x, y = np.meshgrid(_,_)
z = x**2+x*y

############################################################
"""
plt.contourf(x,y,z, levels=100,vmin = 0.1,vmax =1.5, cmap="plasma")
plt.colorbar(label="asd")

"""
############################################################
############################################################
"""
cs = plt.contour(x,y,z, levels = 20)
plt.clabel(cs, fontsize=8)
"""
############################################################
############################################################
"""
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot_surface(x,y,z, cmap="coolwarm")
"""
############################################################
############################################################
plt.style.use(["default"])

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot_surface(x,y,z,cmap="coolwarm", linewidth=0, antialiased=False)
ax.view_init(elev=10,azim=0)

def animate(i):
    ax.view_init(elev=10,azim=3*i)

ani = animation.FuncAnimation(fig,animate,frames=240,interval = 50)
ani.save("jojo.gif", writer="pillow",fps=50,dpi=100)

############################################################


plt.show()