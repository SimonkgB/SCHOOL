import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation









fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(x, u[:,i])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=M+1, interval=40, blit=True)
plt.show()
