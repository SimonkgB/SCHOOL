import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

def f(x,t):
    return np.sin(x-3*t)

x = np.linspace(0,10*np.pi,1000)

fig, ax = plt.subplots(1,1,figsize=(8,4))
ln1, = plt.plot([],[])
time_text = ax.text(0.65,0.95,"",fontsize=15,
                    transform=ax.transAxes, bbox=dict(facecolor="white", edgecolor="black"))

ax.set_xlim(0,10*np.pi)
ax.set_ylim(-1.5,1.5)

def animate(i):
    ln1.set_data(x,f(x,1/50*i))
    time_text.set_text("t={:.2f}".format(i/50))

ani = animation.FuncAnimation(fig, animate,frames=240,interval=50)
# ani.save("ani.gif",writer='pillow',fps=50,dpi=100)

plt.show()
